# Course book template

A complete, cumulative course book per course: one chapter per lecture, the definition of every difficult term in the right margin where it first appears, an automatic glossary, boxes for definitions, intuitions, worked examples and exam traps, and TikZ/pgfplots figures. Content rules: `../../rules/explaining.md` (profile P6).

## Files

| Here (shared) | Per course (`<course>/book/`) |
|---|---|
| `preamble.tex`: packages, layout with a 4.6 cm margin column, boxes, `\term`, glossary | `main.tex`: inputs the shared preamble and title page, then the chapters |
| `titlepage.tex` | `metadata.tex`: institution, course, lecturers, author, coverage, date |
| `build.sh` | `glossary.tex`: `\defterm{key}{Name}{Definition}`, grouped by week |
| `example/`: a minimal book to copy | `chapters/week-NN.tex`, `chapters/formula-sheet.tex` |

Editing `preamble.tex` restyles every book that inputs it. A book inputs it by a relative path (through a symlink to the kit) or by an absolute path.

## Start a book

```bash
cp -r <kit>/templates/course-book/example <course>/book
```

Then fix the two `\input` paths at the top of `main.tex` so they reach `preamble.tex` and `titlepage.tex`, fill `metadata.tex`, and build.

## Add a week

1. Write `chapters/week-NN.tex`: `\chapter{Title}`, a `lecturecard` (source, lecturer, assignment verdict), a roadmap `recap`, one section per lecture section (intuition, construction, formula, lecture example, a TikZ figure for each mechanism), self-sufficient: no slide numbers or "see the slide" (rules E12, E13), a closing `recap`, likely exam questions and `traps`.
2. Declare the week's new terms in `glossary.tex`; use `\term{key}` at first use in running text.
3. Add `\input{chapters/week-NN}` to `main.tex`, extend the formula sheet, update `\coverage` and `\updated`.
4. Build and look at every new page (rule X5):

```bash
<kit>/templates/course-book/build.sh <course>/book
```

## Macros

- `\term{key}` / `\term[shown text]{key}`: bold term, definition in the margin, page in the glossary. Running text only (rule X13).
- `\gls{key}`: the term without a margin note (inside boxes, tables, figures, or on later uses).
- `\sidenote{text}`: a margin remark (added background, a source).
- Boxes: `definition{Title}`, `intuition[Title]`, `worked{Title}` (with `\addedtag` when not from the source), `traps`, `recap[Title]`, `lecturecard`.
- TikZ styles: `bx`, `bxhi`, `bxdark`, `bxwarn`, `ar`, `grp`, `lbl`.
