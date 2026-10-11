"""Prove that a text's numbers come from its sources, or that a rewrite moved none (rule C6).

usage:
  python3 check_numbers.py OUTPUT SOURCE [SOURCE ...]   numbers of OUTPUT found in no SOURCE
  python3 check_numbers.py --compare OLD NEW            numbers gained or lost between two versions

Files can be .pdf (read with pdftotext), .tex, .md or .txt. A hit is a question to answer,
not an automatic error: a section number, a value computed in the text, or a number that sits
only in an image of a slide (pdftotext cannot see it; read the rendered page) can be legitimate.
"""
import collections
import re
import subprocess
import sys
from pathlib import Path


def text_of(path):
    p = Path(path)
    if p.suffix == '.pdf':
        return subprocess.run(['pdftotext', '-layout', str(p), '-'],
                              capture_output=True, text=True, check=True).stdout
    return p.read_text(encoding='utf-8', errors='replace')


def numbers(text):
    text = re.sub(r'(?<!\\)%.*', '', text)                       # LaTeX comments
    text = text.replace(' ', '').replace(' ', ' ').replace('{,}', ',').replace('\\,', '')
    text = re.sub(r'(?<=\d)[ ,](?=\d{3}\b)', '', text)            # 1 000 and 1,000 -> 1000
    return collections.Counter(re.findall(r'\d+(?:\.\d+)?', text))


def main(args):
    if not args or (args[0] == '--compare' and len(args) != 3) or (args[0] != '--compare' and len(args) < 2):
        sys.exit(__doc__)
    if args[0] == '--compare':
        a, b = numbers(text_of(args[1])), numbers(text_of(args[2]))
        print('only in', args[1] + ':', dict(sorted((a - b).items())))
        print('only in', args[2] + ':', dict(sorted((b - a).items())))
        return
    out = numbers(text_of(args[0]))
    known = set()
    for s in args[1:]:
        known |= set(numbers(text_of(s)))
    missing = {n: c for n, c in out.items() if n not in known}
    print('numbers of %s found in no source: %d' % (args[0], len(missing)))
    for n, c in sorted(missing.items(), key=lambda kv: float(kv[0])):
        print('  %s (x%d)' % (n, c))


if __name__ == '__main__':
    main(sys.argv[1:])
