#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if ! command -v apt-get >/dev/null 2>&1; then
  echo 'Use the documented local TeX Live installation on non-Debian systems.'
  exit 1
fi
priv=()
if [ "$(id -u)" -ne 0 ]; then priv=(sudo); fi
# No tokens or local absolute paths. Idempotent package installation.
"${priv[@]}" apt-get update -qq
"${priv[@]}" env DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  make python3 latexmk texlive-latex-extra texlive-fonts-recommended \
  texlive-fonts-extra texlive-science texlive-pictures texlive-plain-generic poppler-utils
# Recent newtx loads binhex.tex, which Debian places in texlive-plain-generic.
kpsewhich binhex.tex >/dev/null
make verify
