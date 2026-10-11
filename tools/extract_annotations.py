"""Print every highlight and note saved inside a PDF, page by page (rule F11).

usage: python3 extract_annotations.py annotated.pdf
Run it on a COPY of the annotated file, before any rebuild: pdflatex overwrites the
PDF and the notes with it. Needs PyMuPDF (pip install pymupdf).
"""
import sys

import fitz

if len(sys.argv) != 2:
    sys.exit(__doc__)
doc = fitz.open(sys.argv[1])
count = 0
for i in range(doc.page_count):
    page = doc[i]
    for a in page.annots() or []:
        quads, text = a.vertices, ''
        if quads:
            for k in range(0, len(quads), 4):
                text += page.get_text('text', clip=fitz.Quad(quads[k:k + 4]).rect).replace('\n', ' ')
        count += 1
        print('p%d  %s: %r' % (i + 1, a.type[1], text.strip()[:300]))
        note = a.info.get('content', '').strip()
        if note:
            print('     NOTE:', note)
print(count, 'annotations')
