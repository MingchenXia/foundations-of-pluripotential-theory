#!/usr/bin/env python3
"""Build a source-only archive from tracked files and verify it in a fresh directory."""
from pathlib import Path
import subprocess
import tarfile
import tempfile
import shutil
import hashlib

root = Path(__file__).resolve().parents[1]
destination = root / 'build/release'
destination.mkdir(parents=True, exist_ok=True)
tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
archive = destination / 'foundations-source.tar.gz'
with tarfile.open(archive, 'w:gz') as stream:
    for name in tracked:
        if name:
            stream.add(root / name, arcname=name, recursive=False)
with tempfile.TemporaryDirectory(prefix='foundations-release-') as folder:
    fresh = Path(folder)
    with tarfile.open(archive) as stream:
        stream.extractall(fresh, filter='data')
    subprocess.run(['make', 'verify'], cwd=fresh, check=True)
    def pages(pdf):
        return subprocess.check_output(['pdftotext', '-layout', str(pdf), '-'])
    if pages(root / 'build/book.pdf') != pages(fresh / 'build/book.pdf'):
        raise SystemExit('Fresh archive build differs in page text; inspect before release.')
shutil.copy2(root / 'build/book.pdf', destination / 'foundations-draft.pdf')
with (destination / 'SHA256SUMS').open('w') as stream:
    for p in sorted(destination.iterdir()):
        if p.name != 'SHA256SUMS':
            stream.write(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.name + '\n')
print('Source archive rebuilt in an empty directory; page text matches the current draft.')
