"""Check that each course-book chapter is shorter than its source by a set factor (rule E16).

usage:
  python3 check_length.py [--max R] CHAPTER:SOURCE[:R] [CHAPTER:SOURCE[:R] ...]

Length is counted in words, never pages: margin definitions, boxes and figures change the page
count without changing the content. A chapter's .tex excludes the margin glossary, which lives in
glossary.tex. R is the largest allowed chapter/source ratio (default 0.5); give a lower R to a less
important source. Exits 1 when a chapter, or the whole book, is over its limit.
"""
import re
import subprocess
import sys
from pathlib import Path


def text_of(path):
    p = Path(path)
    if p.suffix == '.pdf':
        return subprocess.run(['pdftotext', str(p), '-'],
                              capture_output=True, text=True, check=True).stdout
    return p.read_text(encoding='utf-8', errors='replace')


def words(path):
    text = text_of(path)
    if Path(path).suffix == '.tex':
        text = re.sub(r'(?<!\\)%.*', '', text)
        text = re.sub(r'\\(begin|end)\{[^}]*\}(\[[^\]]*\])?', ' ', text)
        text = re.sub(r'\\[A-Za-z]+\*?(\[[^\]]*\])?', ' ', text)
    return len(re.findall(r"[A-Za-z][A-Za-z'-]*|\d+(?:[.,]\d+)?", text))


def main(args):
    default = 0.5
    if args[:1] == ['--max']:
        default, args = float(args[1]), args[2:]
    if not args:
        sys.exit(__doc__)
    over, total_c, total_s = False, 0, 0
    print(f"{'chapter':40} {'words':>7} {'source':>7} {'ratio':>6} {'max':>5}")
    for arg in args:
        parts = arg.split(':')
        chapter, source = parts[0], parts[1]
        limit = float(parts[2]) if len(parts) > 2 else default
        c, s = words(chapter), words(source)
        total_c, total_s = total_c + c, total_s + s
        flag = '  OVER' if c > limit * s else ''
        over |= bool(flag)
        print(f"{Path(chapter).name:40} {c:7} {s:7} {c / s:6.2f} {limit:5.2f}{flag}")
    flag = '  OVER' if total_c >= total_s else ''
    over |= bool(flag)
    print(f"{'book':40} {total_c:7} {total_s:7} {total_c / total_s:6.2f} {1:5.2f}{flag}")
    sys.exit(1 if over else 0)


if __name__ == '__main__':
    main(sys.argv[1:])
