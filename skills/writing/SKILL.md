---
name: writing
description: Use when writing, revising or reviewing prose that the user will hand in or publish under their own name: a report, an assignment answer, a lecture summary, an essay, a reflection, a cover letter, a README. Gives the profile to pick, the rules to load for that profile, and the convergence loop to run before delivering. Not for code, commit messages or ordinary chat answers.
---

# Writing a deliverable in the user's voice

Everything this skill needs sits under `kit/` (the kit root). Load only what the task needs.

## 1. Before writing

1. If `~/writing-kit-private/profile.md` exists, read it: the user's identity, voice preferences and private sources.
2. Read the project's own instructions (its `CLAUDE.md`, the brief, a school's rules). They outrank the kit (`kit/rules/README.md`, precedence).
3. Pick the profile in `kit/rules/profiles.md` (P1 report, P2 short assignment, P3 lecture summary, P4 academic essay, P5 reflection, P7 professional writing). Say which in the reply when it is not obvious.
4. Collect what only the user knows (rule V19); never invent it, leave a visible gap (V13).

## 2. Which rules to read

Open `kit/rules/INDEX.md` (one line per rule), then the modules the profile lists. Typical loads:

| Task | Read |
|---|---|
| Any deliverable | `register.md`, `voice.md`, `banned.md`, `facts.md` |
| Revising after the user's notes | add `feedback.md` |
| A report or anything with sections | add `structure.md`, `titles.md`, `sentences.md` |
| Figures or tables | add `figures.md` |
| LaTeX output | use the `latex-report` skill as well |
| Before submission of a long document | `review.md` (independent second opinion) |

When two rules seem to disagree, `kit/rules/conflicts.md` says how it was settled.

## 3. Before delivering

Run the convergence loop of `kit/rules/loop.md` until two passes find nothing:

```bash
python3 kit/tools/check_style.py <file-or-dir>
python3 kit/tools/check_numbers.py <output> <source> [...]
```

The scans are not enough: read the whole output as the reader will (C4).

## 4. When the user corrects something

Append the lesson to `kit/lessons/INBOX.md` (format at its top) in the same turn, promote it into a module when it is clearly general and contradicts nothing, run `python3 kit/tools/build_index.py`, and commit the kit if it is a git repository. A lesson that conflicts with a rule stays open and is mentioned to the user.
