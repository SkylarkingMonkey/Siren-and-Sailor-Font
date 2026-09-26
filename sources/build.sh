#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_root"

if command -v python3.12 >/dev/null 2>&1; then
  python_bin=python3.12
else
  python_bin=python3
fi

"$python_bin" -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/build.py
