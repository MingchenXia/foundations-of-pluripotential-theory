PYTHON ?= python3
.PHONY: check progress audit build verify release clean
check:
	$(PYTHON) scripts/project.py check
progress:
	$(PYTHON) scripts/project.py progress
audit:
	$(PYTHON) .agents/skills/mingchen-writing/scripts/audit_tex.py --bib ComplexGeometry.bib $$( $(PYTHON) scripts/project.py tex-files )
build:
	latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error book.tex
	$(PYTHON) scripts/project.py check-log
verify: check audit build
release: verify
	$(PYTHON) scripts/release.py
clean:
	latexmk -C book.tex
