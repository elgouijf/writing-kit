# writing-kit

A writing pipeline for Claude Code that makes deliverables read as a person wrote them, builds clean LaTeX reports, explains course material from the ground up, and keeps complete course books. Its rules come from months of real corrections: a supervisor who found an engineering report "looks generated", a student who rejected lecture summaries that passed every automatic scan as "AI slop", and every fix that followed.

## What is inside

| Path | What it is |
|---|---|
| `skills/` | Four skills that load on demand: `writing`, `latex-report`, `explaining`, `course-book`. A session that never writes a report pays only their one-line descriptions. |
| `rules/` | 181 rules in 13 modules, one line each in `rules/INDEX.md`. `profiles.md` sets the choices that differ by genre; `conflicts.md` shows how every contradiction between the sources was settled. |
| `templates/report/` | The report working tree (cover, abstract, contents, lists, chapters, references, glossary, appendices) and `short.tex` for one or two pages; its `README.md` defines the tree and how the LaTeX is written. |
| `templates/course-book/` | Course book: margin definitions of difficult terms, automatic glossary, definition/intuition/worked-example/trap boxes, formula sheet. |
| `templates/profile.example.md` | Template for a private profile (identity, voice preferences, private sources) kept outside the repository. |
| `tools/` | `check_style.py` (machine-writing patterns), `check_numbers.py` (every number traced to a source, or unchanged by a rewrite), `extract_annotations.py` (notes saved in a PDF), `body_pages.py` (page budget), `check_length.py` (course-book chapters against their sources, in words), `build_index.py`. |
| `lessons/INBOX.md` | Where new corrections land before they become rules. |

## Install

As a plugin, from Claude Code:

```text
/plugin marketplace add elgouijf/writing-kit
/plugin install writing-kit@writing-kit
```

Or locally, by linking the skills into your user skills folder:

```bash
git clone https://github.com/elgouijf/writing-kit ~/writing-kit
mkdir -p ~/.claude/skills
for s in writing latex-report explaining course-book; do ln -s ~/writing-kit/skills/$s ~/.claude/skills/$s; done
```

Each skill reaches the rules, templates and tools through its `kit` link to the repository root, so both installs see the same files. On Windows, enable symlinks in git (`git config core.symlinks true`) before cloning.

Requirements for the tools: Python 3, `pdftotext` (poppler) for PDF sources, PyMuPDF for annotations and page counts, a TeX distribution with `pdflatex` for the templates.

## Design

- **On demand.** Nothing loads until a task is a deliverable, a LaTeX document, an explanation or a course book. Inside a skill, an index points to the few modules the task needs.
- **One source of truth.** Every rule exists once, in `rules/`. Projects link to the kit; they never copy it, so an improvement reaches all of them.
- **Precedence.** The user in the conversation, then the project's own instructions, then a private profile, then the document profile, then the modules (`rules/README.md`).
- **Private stays private.** Identity, school logos, employer data and project-specific lessons live in a private folder (`~/writing-kit-private/` by default) that the skills read when it exists.

## Contributing

Corrections from real use are the point of the kit. See `CONTRIBUTING.md`.
