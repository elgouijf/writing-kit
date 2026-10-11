"""Report where the body of a report ends: the PDF page where "References" starts (rule O13).

usage: python3 body_pages.py main.pdf [first_body_page]
first_body_page is the PDF page of the first numbered page (default: found from page labels,
else 1). Needs PyMuPDF.
"""
import sys

import fitz

if len(sys.argv) < 2:
    sys.exit(__doc__)
doc = fitz.open(sys.argv[1])
first = int(sys.argv[2]) if len(sys.argv) > 2 else next(
    (i + 1 for i in range(doc.page_count) if doc[i].get_label() == '1'), 1)
for i in range(first - 1, doc.page_count):
    if doc[i].get_text('text').lstrip().startswith(('References', 'Bibliography')):
        print('body: PDF pages %d to %d, %d pages; references start on PDF page %d'
              % (first, i, i - first + 1, i + 1))
        break
else:
    print('no page starting with "References" found')
