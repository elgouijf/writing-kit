# Report working tree

Every LaTeX report built with the kit uses this tree and these conventions. A project copies the whole folder once and keeps its structure; the content (chapters, metadata, figures) is then the project's own. The tree comes from an engineering internship report that went through nine review rounds; the layout was taken from a reference report the school supplied and is not redesigned.

## Tree

```text
main.tex                   wires everything; its \input order is the document order
short.tex                  one- or two-page variant: header block, no cover, no contents
config/packages.tex        packages only, no settings
config/layout.tex          page geometry, spacing, numbering, captions, palette, macros
config/metadata.tex        the ONLY file with personal and document data (never public)
frontmatter/titlepage.tex  cover, reads metadata; one line per item a school prescribes
front/abstract.tex         abstract
chapters/NN-name.tex       one file per section, so any section can be rewritten alone
back/bibliography.tex      plain thebibliography, no biber step
back/glossary.tex          \gdefn entries, linked from the text by \gterm
back/appendices.tex        heavy material; letters come from \ref
figures/                   images and PDF figures; TikZ figures live in the chapter files
```

Delete what a document does not need (abstract, lists, glossary, appendices) together with its `\input` line; do not rename or merge the rest.

## Layout, set once

`report` class, 12 pt, A4, 2 cm margins on all sides, single spacing, one column, Computer Modern through `lmodern`, page numbers. Sections numbered 1, 1.1 (no chapter level); table of contents two levels deep. A school's hard layout rules (font size, maximum margins, spacing) are checked here first, because a breach can get a report rejected.

## Writing the code

- **One `\section` per chapter file**, file name `NN-topic.tex`; a comment at the top says what the section must contain and, when a school has ID-tagged rules, which IDs it satisfies (`% E3: problem statement`).
- **Labels by type**: `sec:`, `fig:`, `tab:`, `app:`, `eq:`. Cite with `\figref{}`, `\tabref{}`, `\appref{}` (bold), never by typed numbers.
- **Floats**: `[H]`, placed right after the paragraph that first cites them; `\centering`; every `\caption[short form]{full caption}` with a noun-phrase short form so the lists stay one line per entry (T6, T7). A phone-shaped screenshot uses `wrapfigure` instead of a float of its own.
- **Tables**: `booktabs` rules only (`\toprule`, `\midrule`, `\bottomrule`), no vertical lines; `tabularx` for prose cells; shrink `\tabcolsep` before the font (G14).
- **Figures**: TikZ in the chapter file, black outlines, fills from the palette in `config/layout.tex` (`figdark` … `figbg`, `sevone` … `sevfour` for a severity scale), every fill a different grey (G6); bar charts drawn on a linear scale unless the caption says otherwise; logos as vector PDFs from simple-icons (G10). Precompute coordinates in centimetres (X10).
- **Glossary**: `\gterm{key}{Term}` at the first use in the text, `\gdefn{key}{Term}{definition}` in `back/glossary.tex`.
- **Gaps**: `\tofill{what the author must supply}` prints a visible box; never fill one by inference (V13).
- **One statement the report stands on**: `\keyclaim{}`, two or three per document at most.
- **Watermark**: off unless `\watermarkimage` in metadata names an image the author may use.
- **Numbers**: thin space in thousands (`32\,989`), `\%` after the number with a thin space (`3.5\,\%`), one decimal convention per document.
- **Prose in the source**: no em-dashes (`---`), no "rather than" (B1, B2).

## Build and review

- `pdflatex` twice (three times with a margin glossary). Clean means 0 errors, 0 undefined references, 0 overfull boxes, and rendered pages looked at (X4, X5).
- Under a page budget: `python3 ../../tools/body_pages.py main.pdf` after every change (O13).
- When the author annotates the PDF: extract first, build to another job name (F11). To compare versions, build a copy tree (`main_copyN.tex` + `copyN/`) and promote it only when asked (F12).
- Never edit `.tex` through heredocs or `sed` (X1).
