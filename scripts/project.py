#!/usr/bin/env python3
"""Repository integrity and honest mathematical progress; no third-party modules."""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
STATES = {'planned', 'drafting', 'proof-review', 'second-read', 'verified', 'blocked'}


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def uncomment(text):
    return re.sub(r'(?<!\\)%[^\n]*', '', text)


def active_files(path=Path('book.tex'), seen=None):
    seen = set() if seen is None else seen
    if path in seen:
        return []
    seen.add(path)
    full = ROOT / path
    if not full.is_file():
        raise ValueError(f'Missing active TeX input: {path}')
    paths = [path]
    for name in re.findall(r'\\(?:input|include)\{([^}]+)\}', uncomment(full.read_text())):
        child = Path(name)
        if not child.suffix:
            child = child.with_suffix('.tex')
        paths.extend(active_files(child, seen))
    return paths


def dag(nodes, id_key, dep_key, errors, kind):
    index = {x[id_key]: x for x in nodes}
    if len(index) != len(nodes):
        errors.append(f'Duplicate {kind} IDs')
    visiting, done = set(), set()

    def visit(key):
        if key in visiting:
            errors.append(f'{kind} dependency cycle through {key}')
            return
        if key in done:
            return
        visiting.add(key)
        for dep in index[key][dep_key]:
            if dep not in index:
                errors.append(f'Unknown {kind} dependency {key} -> {dep}')
            else:
                visit(dep)
        visiting.remove(key)
        done.add(key)

    for key in index:
        visit(key)
    return index


def check():
    errors = []
    chapters, tasks = read('plan/chapters.json'), read('plan/tasks.json')
    ci = dag(chapters, 'id', 'depends_on', errors, 'chapter')
    ti = dag(tasks, 'id', 'depends_on', errors, 'task')
    sources = {s['id'] for s in read('references/catalog.json')}
    external = {s['id']: s for s in read('plan/external-inputs.json')}
    for c in chapters:
        if c['status'] not in STATES:
            errors.append(f'Invalid chapter state {c["id"]}')
        if not (ROOT / c['path']).is_file():
            errors.append(f'Missing chapter file {c["path"]}')
        if c['status'] == 'verified':
            if any(t['status'] != 'verified' for t in tasks
                   if t['chapter'] == c['id'] and t.get('prequel_scope', 'required') == 'required'):
                errors.append(f'Chapter {c["id"]} verified while tasks remain')
            if any(ci[d]['status'] != 'verified' for d in c['depends_on'] if d in ci):
                errors.append(f'Chapter {c["id"]} verified before prerequisites')
    for t in tasks:
        if t['chapter'] not in ci or t['status'] not in STATES:
            errors.append(f'Invalid task state/chapter: {t["id"]}')
        for sid in t.get('source_ids', []):
            if sid not in sources:
                errors.append(f'Unknown source {sid} for {t["id"]}')
        for eid in t['external_inputs']:
            if eid not in external or external[eid]['status'] != 'accepted-policy':
                errors.append(f'Unaccepted external input {eid} for {t["id"]}')
        if t['status'] == 'blocked' and not t.get('blocker'):
            errors.append(f'Blocked task lacks concrete blocker: {t["id"]}')
        if t['status'] == 'verified':
            if any(ti[d]['status'] != 'verified' for d in t['depends_on'] if d in ti):
                errors.append(f'Task verified before its prerequisites: {t["id"]}')
            if not t['result_labels'] or not t['evidence'] or not t.get('review_record'):
                errors.append(f'Verified task lacks labels/evidence/review: {t["id"]}')
            else:
                try:
                    review = read(t['review_record'])
                    for field in ['first_complete_read', 'second_complete_read', 'final_build', 'visual_inspection']:
                        if review.get(field) is not True:
                            errors.append(f'{t["id"]}: review does not confirm {field}')
                    if t['id'] not in review.get('task_ids', []):
                        errors.append(f'Review does not cover {t["id"]}')
                    for field in ['files_read', 'source_locators_checked', 'proof_scope', 'build_log', 'pdf_pages_inspected']:
                        if not review.get(field):
                            errors.append(f'{t["id"]}: missing review scope {field}')
                except (OSError, ValueError, TypeError) as e:
                    errors.append(f'Invalid review for {t["id"]}: {e}')
        for path in t['evidence']:
            if not (ROOT / path).is_file():
                errors.append(f'Missing evidence {path}')
    manifest = read('references/manifest.json')
    recorded = {e['path'] for e in manifest}
    actual = {str(p.relative_to(ROOT)) for p in (ROOT / 'references/originals').rglob('*') if p.is_file()}
    if recorded != actual:
        errors.append('Original source files and manifest do not match')
    for e in manifest:
        p = ROOT / e['path']
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != e['sha256']:
            errors.append(f'Original source changed or missing: {e["path"]}')
    labels = Counter()
    refs, cites = set(), set()
    paths = active_files()
    for path in paths:
        text = uncomment((ROOT / path).read_text())
        labels.update(re.findall(r'\\label\{([^}]+)\}', text))
        for group in re.findall(r'\\(?:[cC]ref|ref|eqref)\{([^}]+)\}', text):
            if '#' not in group:  # Template macro parameters are not literal references.
                refs.update(x.strip() for x in group.split(','))
        for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', text):
            cites.update(x.strip() for x in group.split(','))
        if r'\nocite{*}' in text:
            errors.append(f'Forbidden bibliography dump in {path}')
    errors.extend(f'Duplicate active label {k}' for k, n in labels.items() if n > 1)
    errors.extend(f'Unresolved active reference {k}' for k in sorted(refs - labels.keys()))
    bib = set(re.findall(r'@[A-Za-z]+\s*\{\s*([^,\s]+)', (ROOT / 'ComplexGeometry.bib').read_text()))
    errors.extend(f'Missing bibliography key {k}' for k in sorted(cites - bib))
    for t in tasks:
        if t['status'] == 'verified' and t.get('prequel_scope', 'required') == 'required':
            errors.extend(f'Verified task result not active: {k}' for k in t['result_labels'] if k not in labels)
    for t in tasks:
        c = ci.get(t['chapter'])
        if not c:
            continue
        for dep in c['depends_on']:
            if dep not in ci:
                continue
            # Chapter prerequisites are enforced in addition to the finer task graph.
            if t['status'] == 'verified' and ci[dep]['status'] != 'verified':
                errors.append(f'{t["id"]}: chapter prerequisite {dep} is not verified')
    if errors:
        print('\n'.join('ERROR: ' + e for e in errors))
        return 1
    print(f'Integrity OK: {len(chapters)} chapter units, {len(tasks)} obligations, '
          f'{len(manifest)} immutable source files, {len(paths)} active TeX files. '
          'Mathematical proofs are not automatically verified.')
    return 0


def progress():
    chapters, tasks = read('plan/chapters.json'), read('plan/tasks.json')
    required = [t for t in tasks if t.get('prequel_scope', 'required') == 'required']
    counts = Counter(t['status'] for t in required)
    table = ['# Writing progress', '', 'Generated by `make progress` from JSON; build success is not mathematical completion.', '',
             'Scope: self-contained foundations for SGPT Part I, plus the explicitly requested foundations of Example 6.1.3 and Theorem 1.2 of arXiv:2607.12797. Broader Parts II and III are excluded. The missing-proof/overlap audit remains unfinished, so these task counts are provisional and are not an overall completion percentage.', '',
             f'{len(required)} current required proof obligations; ' + '; '.join(f'{s}: {counts[s]}' for s in sorted(STATES)) + '.', '',
             f'{len(tasks) - len(required)} old tasks are retained outside scope and do not count toward completion.', '',
             '| ID | Chapter | Scope | State | Verified required tasks | Prerequisites |', '|---|---|---|---|---:|---|']
    cm = ['# Chapter map', '', 'Stable IDs; numerical chapter numbers are generated by TeX.', '',
          'Required units form the current prequel; excluded units preserve historical working material.', '',
          '| ID | Part | Scope | Title | Prerequisites | Source |', '|---|---|---|---|---|---|']
    chapter_states = {c['id']: c['status'] for c in chapters}
    ready = [c for c in chapters if c.get('prequel_scope', 'required') == 'required' and c['status'] != 'verified'
             and any(t['chapter'] == c['id'] and t['status'] in {'planned', 'drafting', 'proof-review'}
                     for t in required)
             and all(chapter_states.get(dep) == 'verified' for dep in c['depends_on'])]
    next_unit = (f'Next coherent writing unit: **{ready[0]["id"]}**.' if ready else
                 'All required chapter units are verified.' if all(c['status'] == 'verified' for c in chapters
                     if c.get('prequel_scope', 'required') == 'required') else
                 'No unfinished writing unit has verified chapter prerequisites. Continue independent work according to WRITING_SEQUENCE.md while preserving the recorded dependency gates.')
    queue = ['# Unfinished proof and writing obligations', '',
             'Required SGPT Part I foundations, the explicitly requested Example 6.1.3 foundations and Theorem 1.2 of arXiv:2607.12797 only. These are missing work in this book; they are not claims that the results are open in the literature. See research/SGPT_PART_I_GAPS.md for the missing-proof and overlap audit.', '',
             next_unit, '']
    for c in chapters:
        ct = [t for t in required if t['chapter'] == c['id']]
        verified = sum(t['status'] == 'verified' for t in ct)
        table.append(f'| {c["id"]} | {c["title"]} | {c.get("prequel_scope", "required")} | {c["status"]} | {verified}/{len(ct)} | {", ".join(c["depends_on"]) or "—"} |')
        cm.append(f'| {c["id"]} | {c["part"]} | {c.get("prequel_scope", "required")} | {c["title"]} | {", ".join(c["depends_on"]) or "—"} | [{c["path"]}](../{c["path"]}) |')
        pending = [t for t in ct if t['status'] != 'verified']
        if pending:
            queue.extend([f'## {c["id"]} — {c["title"]}', ''])
            for t in pending:
                queue.append(f'- `{t["id"]}` [{t["status"]}] {t["title"]}')
                if t.get('blocker'):
                    queue.append(f'  Concrete blocker: {t["blocker"]}')
            queue.append('')
    for path, lines in [('plan/PROGRESS.md', table), ('plan/CHAPTER_MAP.md', cm), ('plan/OPEN_TASKS.md', queue)]:
        (ROOT / path).write_text('\n'.join(lines) + '\n')
    print('Updated chapter map, progress and unfinished obligations.')


def check_log():
    log = ROOT / 'build/book.log'
    if not log.is_file():
        print('Missing build/book.log')
        return 1
    text = log.read_text(errors='replace')
    patterns = [r'undefined references', r'undefined citations', r'Citation .* undefined',
                r'Reference .* undefined', r'Label .* multiply defined', r'LaTeX Error:',
                r'Fatal error', r'Rerun to get cross-references right']
    found = [p for p in patterns if re.search(p, text, re.I)]
    if found:
        print('Unresolved build diagnostics: ' + ', '.join(found))
        return 1
    print('Final build log has no unresolved citations/references or fatal errors.')
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['check', 'progress', 'tex-files', 'check-log'])
    args = parser.parse_args()
    if args.command == 'check':
        return check()
    if args.command == 'progress':
        progress()
        return 0
    if args.command == 'tex-files':
        print('\n'.join(str(x) for x in active_files() if not str(x).startswith('style/')))
        return 0
    return check_log()


if __name__ == '__main__':
    sys.exit(main())
