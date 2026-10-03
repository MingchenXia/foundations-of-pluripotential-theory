#!/usr/bin/env python3
"""Conservative lint checks for the Mingchen mathematical writing style."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


RESULT_ENVS = (
    "maintheorem",
    "maincorollary",
    "theorem",
    "proposition",
    "corollary",
    "lemma",
    "conjecture",
    "question",
    "example",
    "definition",
    "condition",
    "remark",
)

ALLOWED_NEWTHEOREMS = set(RESULT_ENVS) | {"problem"}
LABEL_PREFIXES = {
    "sec",
    "subsec",
    "thm",
    "prop",
    "lem",
    "cor",
    "conj",
    "prob",
    "ques",
    "ex",
    "def",
    "cond",
    "rem",
    "eq",
}
FORBIDDEN_LOCAL_ENVS = {
    "claim",
    "fact",
    "observation",
    "notation",
    "setup",
    "keylemma",
    "keyfact",
    "technicalclaim",
    "technicallemma",
    "proofstep",
}

ENV_LABEL_PREFIX = {
    "maintheorem": "thm",
    "maincorollary": "cor",
    "theorem": "thm",
    "proposition": "prop",
    "corollary": "cor",
    "lemma": "lem",
    "conjecture": "conj",
    "question": "ques",
    "example": "ex",
    "definition": "def",
    "condition": "cond",
    "remark": "rem",
}

AI_PATTERNS = {
    r"\bin this section,? we (?:delve into|explore)\b": "replace the generic section opener with standing assumptions and the precise goal",
    r"\bit is (?:important|worthwhile) to (?:note|observe)\b": "state the mathematical fact directly and explain where it is used",
    r"\b(?:this|it) (?:plays|serves) (?:as )?a key role\b": "name the exact role in the argument",
    r"\bas we shall see\b": "replace the loose promise with a precise cross-reference or delete it",
    r"\bwe (?:now )?(?:leverage|utilize)\b": "use the concrete mathematical operation instead",
    r"\bkey insight\b": "state the mechanism rather than evaluating it",
    r"\bmain technical (?:insight|lemma|proposition|result|step)\b": "use a semantic result type without promotional naming",
    r"\b(?:clearly|obviously|straightforwardly)\b": "give the immediate reason or omit the adverb",
    r"\bby (?:a |the )?standard arguments?\b": "identify the actual theorem or argument",
    r"\bby continuity\b": "specify the map and topology",
    r"\bone can show\b": "state who proves the claim and supply the argument or citation",
    r"\b(?:powerful|crucial|groundbreaking|remarkable|seamless)\b": "replace evaluation with mathematical content",
    r"\b(?:by )?(?:a |the )?standard [a-z-]+ arguments?\b": "name the exact compactness, comparison, approximation, or descent argument",
    r"\b(?:the|this) result follows\b": "state the short implication or the exact criterion closing the proof",
    r"\bthe construction works\b": "replace the vague conclusion with existence, uniqueness, equality, or compatibility data",
}


@dataclass(frozen=True)
class Finding:
    severity: str
    path: Path
    line: int
    message: str


def uncommented(text: str) -> str:
    """Replace TeX comments by spaces while preserving offsets and line numbers."""
    output: list[str] = []
    for line in text.splitlines(keepends=True):
        cut = None
        for index, char in enumerate(line):
            if char != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cut = index
                break
        if cut is None:
            output.append(line)
            continue
        suffix = line[cut:]
        newline = "\n" if suffix.endswith("\n") else ""
        output.append(line[:cut] + " " * (len(suffix) - len(newline)) + newline)
    return "".join(output)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def add(
    findings: list[Finding], severity: str, path: Path, text: str, offset: int, message: str
) -> None:
    findings.append(Finding(severity, path, line_number(text, offset), message))


def scan_group(text: str, start: int, opener: str, closer: str) -> tuple[str, int] | None:
    """Return one balanced TeX group and the offset following it."""
    if start >= len(text) or text[start] != opener:
        return None
    depth = 0
    for cursor in range(start, len(text)):
        char = text[cursor]
        if char == opener and (cursor == 0 or text[cursor - 1] != "\\"):
            depth += 1
        elif char == closer and (cursor == 0 or text[cursor - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return text[start + 1 : cursor], cursor + 1
    return None


def extract_cite_keys(text: str) -> set[str]:
    """Extract keys from singular and plural BibLaTeX citation commands."""
    keys: set[str] = set()
    command_re = re.compile(r"\\(?P<command>[A-Za-z]*cite[A-Za-z]*|cite)\*?", re.I)
    for match in command_re.finditer(text):
        command = match.group("command").lower()
        cursor = match.end()
        plural = command.endswith("cites")
        volumetric = "volcite" in command

        if plural:
            for _ in range(2):
                while cursor < len(text) and text[cursor].isspace():
                    cursor += 1
                group = scan_group(text, cursor, "(", ")")
                if group is None:
                    break
                _, cursor = group

        while cursor < len(text):
            while cursor < len(text) and text[cursor].isspace():
                cursor += 1
            while cursor < len(text) and text[cursor] == "[":
                group = scan_group(text, cursor, "[", "]")
                if group is None:
                    break
                _, cursor = group
                while cursor < len(text) and text[cursor].isspace():
                    cursor += 1

            if volumetric:
                volume_group = scan_group(text, cursor, "{", "}")
                if volume_group is None:
                    break
                _, cursor = volume_group
                while cursor < len(text) and text[cursor].isspace():
                    cursor += 1
                while cursor < len(text) and text[cursor] == "[":
                    group = scan_group(text, cursor, "[", "]")
                    if group is None:
                        break
                    _, cursor = group
                    while cursor < len(text) and text[cursor].isspace():
                        cursor += 1

            group = scan_group(text, cursor, "{", "}")
            if group is None:
                break
            raw_keys, cursor = group
            if raw_keys.strip() == "*":
                break
            keys.update(key.strip() for key in raw_keys.split(",") if key.strip())
            if not plural:
                break
    return keys


def extract_bib_field(entry: str, field: str) -> str | None:
    """Extract one BibTeX field while preserving nested braced content."""
    match = re.search(rf"(?im)^\s*{re.escape(field)}\s*=\s*", entry)
    if match is None:
        return None
    cursor = match.end()
    while cursor < len(entry) and entry[cursor].isspace():
        cursor += 1
    if cursor >= len(entry):
        return None
    if entry[cursor] == "{":
        group = scan_group(entry, cursor, "{", "}")
        return group[0].strip() if group else None
    if entry[cursor] == '"':
        end = cursor + 1
        while end < len(entry):
            if entry[end] == '"' and entry[end - 1] != "\\":
                return entry[cursor + 1 : end].strip()
            end += 1
        return None
    end = entry.find(",", cursor)
    if end < 0:
        end = len(entry)
    return entry[cursor:end].strip()


def family_components(family: str) -> list[str]:
    """Return whitespace- or hyphen-separated components of a BibTeX family name."""
    plain = family
    plain = re.sub(
        r"\\(?:['\"`^~=.uvHckbdtr])\s*\{?([A-Za-z])\}?",
        r"\1",
        plain,
    )
    plain = re.sub(r"\\[A-Za-z@]+", "", plain)
    plain = plain.replace("{", "").replace("}", "")
    return [
        component
        for component in re.split(r"[\s-]+", plain.strip())
        if re.search(r"[A-Za-z]", component)
    ]


def compound_label_code(entry: str) -> str | None:
    """Return the house author code when an entry contains a compound family name."""
    author = extract_bib_field(entry, "author")
    if not author:
        return None
    names = re.split(r"\s+and\s+", author, flags=re.I)
    author_codes: list[str] = []
    has_compound_family = False
    for name in names:
        if "," not in name:
            return None
        family = name.split(",", 1)[0].strip()
        components = family_components(family)
        if not components:
            return None
        has_compound_family = has_compound_family or len(components) > 1
        initials: list[str] = []
        for component in components:
            initial = re.search(r"[A-Za-z]", component)
            if initial is None:
                return None
            initials.append(initial.group(0).upper())
        author_codes.append("".join(initials))
    return "".join(author_codes) if has_compound_family else None


def audit_tex(path: Path) -> tuple[list[Finding], set[str], list[tuple[str, int]]]:
    original = path.read_text(encoding="utf-8")
    text = uncommented(original)
    findings: list[Finding] = []

    for match in re.finditer(r"\\\(", text):
        add(
            findings,
            "ERROR",
            path,
            text,
            match.start(),
            r"inline mathematics must use $...$, not \(...\)",
        )

    for match in re.finditer(r"\\[cC]ref\{[^}]*\beq:", text):
        add(
            findings,
            "ERROR",
            path,
            text,
            match.start(),
            r"equation labels must be cited with \eqref, not \cref or \Cref",
        )

    for match in re.finditer(
        r"\\addbibresource(?:\[[^\]]*\])?\s*\{([^}]+)\}", text
    ):
        resource = Path(match.group(1).strip()).name
        if resource != "ComplexGeometry.bib":
            add(
                findings,
                "ERROR",
                path,
                text,
                match.start(),
                "house-style manuscripts use only the project-local ComplexGeometry.bib",
            )

    for match in re.finditer(
        r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, re.DOTALL
    ):
        abstract = match.group(1).strip()
        if not abstract:
            continue
        if re.search(r"\n\s*\n", abstract):
            add(
                findings,
                "WARNING",
                path,
                text,
                match.start(),
                "keep the abstract as one concise, clear paragraph whenever possible",
            )
        prose = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", abstract)
        prose = re.sub(r"[{}$\\]", " ", prose)
        if len(re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*", prose)) > 180:
            add(
                findings,
                "WARNING",
                path,
                text,
                match.start(),
                "abstract exceeds 180 prose words; retain only the setting, main result, and sharp consequence",
            )

    for match in re.finditer(r"\\newtheorem\*?\s*\{([^}]+)\}", text):
        name = match.group(1)
        if name not in ALLOWED_NEWTHEOREMS:
            add(
                findings,
                "ERROR",
                path,
                text,
                match.start(),
                f"non-house theorem environment {name!r}; use an existing semantic environment or prose",
            )

    font_commands = r"(?:mathcal|mathbb|mathbf|mathfrak|mathsf|mathscr|mathds)"
    font_alias_patterns = (
        rf"\\(?:newcommand|renewcommand|providecommand)\*?\s*"
        rf"\{{\\[A-Za-z@]+\}}\s*(?:\[[^\]]*\]\s*)?"
        rf"\{{\s*\\{font_commands}\b",
        rf"\\def\s*\\[A-Za-z@]+\s*(?:#\d\s*)*"
        rf"\{{\s*\\{font_commands}\b",
    )
    for pattern in font_alias_patterns:
        for match in re.finditer(pattern, text):
            add(
                findings,
                "ERROR",
                path,
                text,
                match.start(),
                "do not define a macro solely to abbreviate a special math alphabet; write the font command directly",
            )

    forbidden = "|".join(re.escape(name) for name in sorted(FORBIDDEN_LOCAL_ENVS))
    for match in re.finditer(rf"\\begin\{{({forbidden})\}}", text):
        environment = match.group(1)
        if environment in {"keylemma", "technicallemma"}:
            message = (
                f"ad hoc result environment {environment!r}; use lemma, proposition, or theorem "
                "according to its logical role"
            )
        else:
            message = (
                f"ad hoc environment {environment!r}; keep a local assertion or step inside "
                "the proof, or use an existing semantic environment if it is reusable"
            )
        add(
            findings,
            "ERROR",
            path,
            text,
            match.start(),
            message,
        )

    env_names = "|".join(RESULT_ENVS)
    begin_re = re.compile(rf"\\begin\{{(?P<env>{env_names})\}}")
    for match in begin_re.finditer(text):
        cursor = match.end()
        while cursor < len(text) and text[cursor].isspace():
            cursor += 1

        title = None
        if cursor < len(text) and text[cursor] == "[":
            title_group = scan_group(text, cursor, "[", "]")
            if title_group is None:
                add(
                    findings,
                    "ERROR",
                    path,
                    text,
                    match.start(),
                    f"{match.group('env')} has an unbalanced optional title",
                )
                continue
            title, cursor = title_group

        label_match = re.match(r"\s*\\label\{([^}]+)\}", text[cursor:])
        if label_match is None:
            add(
                findings,
                "ERROR",
                path,
                text,
                match.start(),
                f"{match.group('env')} lacks an immediate semantic label",
            )
        elif label_match.group(1).split(":", 1)[0] != ENV_LABEL_PREFIX[match.group("env")]:
            add(
                findings,
                "ERROR",
                path,
                text,
                match.start(),
                f"{match.group('env')} label {label_match.group(1)!r} has the wrong type prefix",
            )
        if title and not re.search(r"\\cref\{|\\Cref\{", title):
            add(
                findings,
                "WARNING",
                path,
                text,
                match.start(),
                "optional result title requires a recognized historical or source-given name",
            )
        if title and re.search(
            r"\b(?:key|crucial|fundamental|master|powerful|technical)\b", title, re.I
        ):
            add(
                findings,
                "ERROR",
                path,
                text,
                match.start(),
                "evaluative theorem title; importance must come from mathematical role",
            )

    for match in re.finditer(
        r"\\begin\{equation\}(.*?)\\end\{equation\}", text, re.DOTALL
    ):
        if "\\label{eq:" not in match.group(1):
            add(
                findings,
                "ERROR",
                path,
                text,
                match.start(),
                "numbered equation lacks an eq: semantic label; use an unnumbered display if it is not referenced",
            )

    labels: list[tuple[str, int]] = []
    for match in re.finditer(r"\\label\{([^}]+)\}", text):
        label = match.group(1)
        labels.append((label, line_number(text, match.start())))
        if ":" not in label or label.split(":", 1)[0] not in LABEL_PREFIXES:
            add(
                findings,
                "WARNING",
                path,
                text,
                match.start(),
                f"label {label!r} does not use a house-style type prefix",
            )
            continue
        slug = label.split(":", 1)[1]
        if re.fullmatch(r"(?:\d+|key|technical|new|main\d+|result\d*)", slug, re.I):
            add(
                findings,
                "ERROR",
                path,
                text,
                match.start(),
                f"generic label {label!r}; describe the mathematical mechanism or conclusion",
            )

    for match in re.finditer(r"\\ref\{", text):
        add(
            findings,
            "WARNING",
            path,
            text,
            match.start(),
            "raw \\ref; use \\cref, \\Cref, or \\eqref",
        )

    for pattern, message in AI_PATTERNS.items():
        for match in re.finditer(pattern, text, re.I):
            add(findings, "WARNING", path, text, match.start(), message)

    for match in re.finditer(r"\b([A-Za-z]{2,})\s+\1\b", text, re.I):
        add(
            findings,
            "WARNING",
            path,
            text,
            match.start(),
            f"possible repeated word {match.group(0)!r}",
        )

    for command in ("bibliography", "bibliographystyle"):
        for match in re.finditer(rf"\\{command}\s*\{{", text):
            add(
                findings,
                "WARNING",
                path,
                text,
                match.start(),
                f"BibTeX command \\{command}; a house-style project uses BibLaTeX/Biber and \\printbibliography",
            )
    for match in re.finditer(r"\\nocite\s*\{\s*\*\s*\}", text):
        add(findings, "ERROR", path, text, match.start(), "do not use \\nocite{*}")

    return findings, extract_cite_keys(text), labels


def parse_bib(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    starts = list(re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,", text, re.I))
    entries: dict[str, str] = {}
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        entries[match.group(1)] = text[match.start() : end]
    return entries


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tex", nargs="+", type=Path, help="TeX source files to audit")
    parser.add_argument("--bib", type=Path, help="bibliography used by these files")
    parser.add_argument("--strict", action="store_true", help="fail on warnings as well as errors")
    args = parser.parse_args()

    findings: list[Finding] = []
    cited: set[str] = set()
    label_locations: dict[str, tuple[Path, int]] = {}
    for path in args.tex:
        if not path.is_file():
            parser.error(f"TeX file not found: {path}")
        local_findings, local_cites, local_labels = audit_tex(path)
        findings.extend(local_findings)
        cited.update(local_cites)
        for label, line in local_labels:
            first = label_locations.get(label)
            if first is None:
                label_locations[label] = (path, line)
                continue
            first_path, first_line = first
            findings.append(
                Finding(
                    "ERROR",
                    path,
                    line,
                    f"duplicate label {label!r}; first defined at {first_path}:{first_line}",
                )
            )

    if args.bib:
        if not args.bib.is_file():
            parser.error(f"bibliography not found: {args.bib}")
        entries = parse_bib(args.bib)
        bib_text = args.bib.read_text(encoding="utf-8")
        for key in sorted(cited - entries.keys()):
            findings.append(Finding("ERROR", args.bib, 1, f"cited key {key!r} is missing"))
        for key in sorted(cited & entries.keys()):
            entry = entries[key]
            entry_offset = bib_text.find(entry)
            entry_line = line_number(bib_text, max(entry_offset, 0))
            arxiv = re.search(r"(?:archiveprefix|eprint|arxiv\.org)", entry, re.I)
            published = re.search(
                r"^\s*(?:journal|journaltitle|booktitle|publisher)\s*=", entry, re.I | re.M
            )
            if arxiv and not published:
                findings.append(
                    Finding(
                        "WARNING",
                        args.bib,
                        entry_line,
                        f"cited entry {key!r} appears arXiv-only; verify whether a published version now exists",
                    )
                )
            expected_label = compound_label_code(entry)
            if expected_label:
                actual_label = extract_bib_field(entry, "label")
                normalized_label = (
                    re.sub(r"[^A-Za-z]", "", actual_label).upper()
                    if actual_label
                    else None
                )
                if normalized_label != expected_label:
                    detail = (
                        f"label={{{expected_label}}}"
                        if actual_label is None
                        else f"label={{{expected_label}}}, not label={{{actual_label}}}"
                    )
                    findings.append(
                        Finding(
                            "ERROR",
                            args.bib,
                            entry_line,
                            f"cited entry {key!r} has a compound family name; use {detail}",
                        )
                    )

    findings.sort(key=lambda item: (str(item.path), item.line, item.severity, item.message))
    for finding in findings:
        print(f"{finding.path}:{finding.line}: {finding.severity}: {finding.message}")

    errors = sum(finding.severity == "ERROR" for finding in findings)
    warnings = sum(finding.severity == "WARNING" for finding in findings)
    print(f"Mingchen audit: {errors} error(s), {warnings} warning(s)")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
