---
name: course-book
description: Use when creating or extending a course book: a complete, cumulative LaTeX document for one course with a chapter per lecture, margin definitions of difficult terms, an automatic glossary, boxes for definitions, intuitions, worked examples and exam traps, and a formula sheet.
---

# Course books

Template, macros and step-by-step usage: `kit/templates/course-book/README.md`. Content rules: `kit/rules/explaining.md` (section "Course book" and E1–E9). Build pitfalls: `kit/rules/latex.md`.

## New book

```bash
cp -r kit/templates/course-book/example <course>/book
```

Fix the two `\input` paths at the top of `main.tex` (they must reach `templates/course-book/preamble` and `titlepage`), fill `metadata.tex`.

## Each new lecture

1. Write `chapters/week-NN.tex`: every derivation, table and rule of the slides, the background they assume and every clarification the user agreed to add (E15), each said once and as briefly as it allows (E10). A new book starts at week 1, backfilling every past week.
2. Declare new terms in `glossary.tex`; `\term{key}` at first use in running text only, `\gls{key}` inside boxes, tables and figures.
3. Add the `\input`, extend the formula sheet, update `\coverage` and `\updated`.
4. Check the length against the sources in words (E16): `python3 kit/tools/check_length.py <course>/book/chapters/week-NN.tex:<source.pdf> ...`
5. Build, then render and look at every new page (X5):

```bash
kit/templates/course-book/build.sh <course>/book
pdftoppm -r 60 -png <course>/book/<course>-course-book.pdf /tmp/page
```
