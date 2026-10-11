#!/usr/bin/env bash
# Build a course book from any project:
#   <kit>/templates/course-book/build.sh <book-dir> [jobname]
#   e.g.  ~/writing-kit/templates/course-book/build.sh mycourse/book
# Three pdflatex runs: contents, glossary page numbers, then stable references.
# Output: <book-dir>/<jobname>.pdf, jobname defaulting to <course>-course-book.
set -euo pipefail
dir="${1:?usage: build.sh <book-dir> [jobname]}"
[ -f "$dir/main.tex" ] || { [ -f "$dir/book/main.tex" ] && dir="$dir/book"; }
[ -f "$dir/main.tex" ] || { echo "no main.tex in $dir"; exit 1; }
cd "$dir"
job="${2:-$(basename "$(dirname "$PWD")")-course-book}"
for i in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error -jobname="$job" main.tex > /dev/null || {
    echo "pdflatex failed on run $i; see $PWD/$job.log"; grep -n -A3 '^!' "$job.log" | head -20; exit 1; }
done
grep -E 'Warning: (Reference|Citation|Glossary)|undefined' "$job.log" | sort -u || true
echo "overfull boxes: $(grep -c 'Overfull' "$job.log" || true)"
rm -f "$job".{aux,log,out,toc,glsdefs,ist,lof,lot}
echo "built $PWD/$job.pdf ($(pdfinfo "$job.pdf" | awk '/Pages/{print $2}') pages)"
