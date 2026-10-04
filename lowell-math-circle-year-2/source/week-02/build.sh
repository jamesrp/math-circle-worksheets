#!/bin/sh
set -eu
cd "$(dirname "$0")"
repo_dir=$(cd ../../.. && pwd)
build_dir="$repo_dir/tmp/pdfs/week-02-shared"
bundle_python="/Users/jamespfeiffer/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
shared_python=${SHARED_PYTHON:-$bundle_python}
if [ ! -x "$shared_python" ]; then shared_python=python3; fi
mkdir -p "$build_dir"
python3 verify.py
python3 "$repo_dir/plans/verify-week-02-shared.py"
"$shared_python" build-shared-explore.py
for name in shared-collect shared-shortest shared-networks; do
 pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$name.tex" > "$build_dir/$name.console.txt"
 pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$name.tex" > "$build_dir/$name.console.txt"
done
"$shared_python" assemble-shared.py
"$shared_python" build-shared-guide.py
"$shared_python" build-shared-catalog.py
"$shared_python" -c "import importlib.util; s=importlib.util.spec_from_file_location('shared','assemble-shared.py'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); print('Guide structural checks:',m.check(m.OUT.with_name('week-02-shared-facilitator.pdf')),'pages')"
