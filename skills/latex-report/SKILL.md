---
name: latex-report
description: Use when producing or editing a PDF report, paper or assignment in LaTeX: starting from the kit's report template, building it cleanly, placing figures and tables, keeping a page budget, or handling a PDF the author annotated. Pair it with the writing skill for the prose.
---

# LaTeX reports

Everything sits under `kit/` (the kit root). **Read `kit/templates/report/README.md` first**: it defines the working tree every report uses and how its LaTeX is written.

## Start

- Long report (cover, abstract, contents, lists, chapters, references, glossary, appendices): copy `kit/templates/report/` next to the project and build `main.tex`.
- One or two pages: the same folder, build `short.tex`, delete the long-form folders.
- Fill `config/metadata.tex` only; it is the single file with personal data and must never reach a public repository. A school that prescribes cover items gets one line per item in `frontmatter/titlepage.tex`.
- Macros: `\figref`, `\tabref`, `\appref` (bold references), `\gterm`/`\gdefn` (glossary without an external tool), `\tofill` (visible gap), `\keyclaim`. Palette: `figdark`, `figblue`, `figmid`, `figsoft`, `figlight`, `figpale`, `figbg`, and the `sevone`–`sevfour` severity scale.

## Rules to read

`kit/rules/latex.md` (build and editing pitfalls), `kit/rules/figures.md` (figures, tables, colour, placement), and `kit/rules/structure.md` O13–O14 (page budget, appendices).

## Build and check

```bash
pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
python3 kit/tools/body_pages.py main.pdf          # body length under a page budget
pdftoppm -r 60 -png main.pdf /tmp/page            # then look at the pages (X5)
```

Clean means 0 errors, 0 undefined references, 0 overfull boxes, and rendered pages looked at.

## An annotated PDF

Before any rebuild: copy it aside, `python3 kit/tools/extract_annotations.py copy.pdf`, and build to another job name (`-jobname=main_build`) so the notes survive (rule F11). Treat each note as a rule for the whole document (F2). After a rewrite, `python3 kit/tools/check_numbers.py --compare old.pdf new.pdf` proves no number moved.
