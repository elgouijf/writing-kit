"""Flag sentences that break rules/banned.md and its neighbours (convergence loop, rule C2).

usage: python3 check_style.py <file-or-dir> [more ...]
Scans .tex and .md files. A flag is a question to look at, not an automatic error.
"""
import re
import sys
from pathlib import Path

BE = r'\b(is|are|was|were|be|been|being|gets|got)\b'
PART = r'\b\w+(ed|en|own|ought|eld|ent|ade|old)\b'
CHECKS = [
    ('passive', re.compile(BE + r'\s+(?:not\s+|also\s+|still\s+|never\s+|already\s+|only\s+)?' + PART, re.I)),
    ('may-hedge', re.compile(r'\bmay\b', re.I)),
    ('cleft', re.compile(r'\b(it is what|that is what|what .{0,40} is that|it is why|what remains)\b', re.I)),
    ('rather-than', re.compile(r'\brather than\b', re.I)),
    ('em-dash', re.compile(r'\u2014|---')),
    ('filler', re.compile(r'\b(simply|of course|in order to|it should be noted|notably|indeed|arguably|crucially|essentially|leverage|utilise|utilize|robust|seamless|comprehensive|delve)\b', re.I)),
    ('nominalisation', re.compile(r'\b(the fact that|the use of|the ability to|the presence of|in terms of|with respect to)\b', re.I)),
    ('two-colons', re.compile(r':[^.:;]*[:;][^.]*\.')),
    ('aphorism', re.compile(r'(^|\. )(A|An|The) \w+( \w+)? (is|are) (only |never |always |not )?\w+( \w+)?\.', re.M)),
    ('x-not-y', re.compile(r', not (a |an |the )?\w+', re.I)),
    ('vague-intensifier', re.compile(r'\b(key|critical|significant|powerful|holistic|vital|essential)\b', re.I)),
    ('there-is', re.compile(r'\bthere (is|are|was|were)\b', re.I)),
    ('by-gerund', re.compile(r'(^|\. )By \w+ing')),
    ('not-only', re.compile(r'\bnot only\b', re.I)),
    ('showcase', re.compile(r'\b(highlights?|underscores?|showcases?|serves as a)\b', re.I)),
    ('ordinal-synthesis', re.compile(r'(^|\. )(The )?(first|second|third)(ly)?[, ]', re.I)),
    ('ing-adjunct', re.compile(r',\s+\w+ing\b(?!\s+(?:list|pass|pipeline|script|file|model|data|set|time|step|stage|rate|tools?|costs?|order|question))', re.I)),
    ('bare-this', re.compile(r'(^|\. )(This|That|These|Those) (is|are|was|were|shows|means|gives)\b')),
]


def clean_tex(text):
    text = re.sub(r'(?<!\\)%.*', '', text)
    text = re.sub(r'\\begin\{(figure|table|tikzpicture|lstlisting|tabular|minipage|equation|align)\*?\}.*?\\end\{\1\*?\}', ' . ', text, flags=re.S)
    text = re.sub(r'\$[^$]*\$', ' X ', text)
    text = re.sub(r'\\(label|ref|cite|figref|tabref|appref|includegraphics)\*?(\[[^\]]*\])?\{[^}]*\}', ' XREF ', text)
    text = re.sub(r'\\(textbf|emph|texttt|textit|section|subsection|subsubsection|paragraph)\*?\{([^}]*)\}', r'\2', text)
    text = re.sub(r'\\[a-zA-Z]+\*?', ' ', text)
    return re.sub(r'[{}&\\]', ' ', text)


def clean_md(text):
    text = re.sub(r'```.*?```', ' . ', text, flags=re.S)
    text = re.sub(r'\$\$.*?\$\$', ' . ', text, flags=re.S)
    text = re.sub(r'^\s*\|.*\|\s*$', ' . ', text, flags=re.M)   # tables
    text = re.sub(r'^#+ .*$', ' . ', text, flags=re.M)          # headings
    text = re.sub(r'[*_`>]', '', text)
    return text


def sentences(text):
    text = re.sub(r'\s+', ' ', text)
    return [s.strip() for s in re.split(r'(?<=[.:!?])\s+(?=[A-Z])', text) if len(s.strip()) > 25]


files = []
for arg in sys.argv[1:] or ['.']:
    p = Path(arg)
    files += [f for f in sorted(p.rglob('*.tex')) + sorted(p.rglob('*.md'))
              if 'config' not in f.parts] if p.is_dir() else [p]

total = 0
for f in files:
    raw = f.read_text(encoding='utf-8', errors='replace')
    text = clean_tex(raw) if f.suffix == '.tex' else clean_md(raw)
    for s in sentences(text):
        hits = [name for name, rx in CHECKS if rx.search(s)]
        words = len(s.split())
        if words > 45:
            hits.append('long-%d' % words)
        if hits:
            total += 1
            print('[%s] %s\n    %s\n' % (f.name, ','.join(hits), s[:300]))
print('flagged sentences:', total)
