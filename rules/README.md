# Rules

The single source of truth of the kit. Skills point here; nothing else holds a rule.

## How to read them

1. Pick the **profile** of the document (`profiles.md`). It says which modules apply and settles the choices that differ between genres (voice, length, examples, hedging).
2. Open `INDEX.md` (one line per rule) and read only the sections the task needs.
3. Run the convergence loop (`loop.md`) before delivering.

## Precedence (highest first)

1. What the user says in the current conversation.
2. The project's own instructions (`CLAUDE.md`, an assignment brief, a school's rules, a style guide the course teaches).
3. The user's private profile, if one exists (see `templates/profile.example.md`).
4. The document profile in `profiles.md`.
5. The modules below.

Inside the modules, a rule marked **(user)** comes from a direct correction by the user and outranks an unmarked rule. A later correction outranks an earlier one. When a lower level is overridden, say so in the reply.

## Modules

| File | Prefix | Covers |
|---|---|---|
| `profiles.md` | P | Document types and their settings |
| `feedback.md` | F | Working with the author's notes and reviews |
| `facts.md` | V | Verification, numbers, honesty, gaps |
| `register.md` | R | Tone, precision, naming, explaining to a lay reader |
| `voice.md` | W | Voice, subjects, tense, sentence order |
| `sentences.md` | S | Length, punctuation, connectors, lists |
| `banned.md` | B | Forms that read as machine-written, and their replacements |
| `structure.md` | O | Paragraphs, synthesis, conclusions, objectives, appendices |
| `titles.md` | T | Headings, captions, table headers |
| `figures.md` | G | Figures, tables, colour, screenshots, placement |
| `latex.md` | X | LaTeX build and editing pitfalls |
| `loop.md` | C | The convergence loop and the final checklist |
| `review.md` | Q | Asking for an independent second opinion |
| `explaining.md` | E | Teaching a concept, summarising a lecture, course books |
| `conflicts.md` | – | Every contradiction found between sources, and how it was settled |

## Writing a new rule

`- **ID. Title in one line.** Explanation, one example at most. (source)` inside the right module, then `python3 tools/build_index.py`. Sources: `user` for the user's own correction, `review` for a supervisor or reviewer, `school` for an institution's rules, `exp` for something learnt by failing.
