# Lessons inbox

Every use of the kit appends here when the user corrects a text or an explanation. Newest first. Status: `open` (waiting for a decision, or specific to one context) or `promoted → ID` (written into a rule). Keep entries free of personal and confidential data; those go to the private inbox of your profile.

Format:

```text
## YYYY-MM-DD · <scope tag> · <open | promoted → ID>
What was wrong, in one or two lines (quote the user when possible).
The rule it suggests, in one line.
```

Scope tags: `all`, `reports`, `coursework`, `academic-english`, `explaining`, `latex`, `professional`.

---

## 2026-10-16 · course book · promoted → E16
The user asked for a general check that a course book is shorter than its sources and each chapter shorter than its source by a factor depending on its importance, measured in a unit other than pages (the margin column and boxes inflate pages).
Cap each chapter's word share of its source (default 50 %, lower for less important sources); check with tools/check_length.py.

## 2026-10-16 · course book · promoted → E15
Two clarifications (TF-IDF log, word present in every document) were written into the course book unasked: "don't add things to the course book without telling me".
Answer in chat; add to the user's study document only after asking.

## 2026-10-16 · course book · promoted → E10 (revised)
The compact rewrite cut week 3 from 15 to 7 pages but dropped worked-example arithmetic, four figures, a code listing and the intuition boxes; asked "are you losing detail?", the user chose to restore all of them.
Compress prose, not content; check word share against the source and lost numbers with check_numbers before delivering.

## 2026-10-16 · course book · promoted → E10
A chapter for an 18-page lecture filled 15 pages, as long as the two previous chapters together; the user asked why a summary is that long and asked for "compact phrases" that keep the necessary detail.
Write a chapter in compact phrases (fragments, symbols, one-line bullets) instead of full prose; no roadmap, no reproduced code listing, no exam-question list that repeats the traps; a chapter stays well under the source's length.

## 2026-10-11 · explaining · promoted → E10
Course books "should start from all of previous weeks" and stay "as short as possible without losing any of the important information".
Every week from the first; complete content, each thing said once.

## 2026-10-11 · explaining · promoted → E1–E9
Explanations showed a widget before explaining the mechanism, used terms such as n-gram or Transformer undefined, needed three attempts at a coefficient until formula, symbols and meaning were given in text, and kept the full content out of the user's reach.
Build from zero, define every term, formula then meaning in words, text when text is asked for, complete content available.

## 2026-10-09 · coursework · promoted → R6, O4, O5, W11, S11, W12, T1, T5, P2, P3, C4
Lecture summaries that passed every automatic scan were rejected as "AI slop"; a report draft used the first person and question headings.
State content directly, one example per point, synthesis, connected reasoning, noun-phrase headings, impersonal voice; scans are not enough.

## 2026-10-14 · course book · promoted → X5
A plain `tabular` (isolation-level table) ran under the margin glossary notes; the build had been delivered with 3 overfull boxes left.
Size every course-book table with `tabularx` at `\linewidth`, and deliver only at 0 overfull boxes (X4).

## 2026-10-14 · explanation · promoted → E11
A tree / fat-tree explanation drew the networks as ASCII art in code blocks; the user rejected them and asked for real graphs.
Draw a structure (network, tree, pipeline, memory layout) as a rendered figure: SVG widget in chat, TikZ in a course book. Never ASCII art.

## 2026-10-14 · course book · promoted → E12, E13
A chapter pointed to the slides in nearly every paragraph ("(slide 10)") and explained a hash file, joins and recovery with text and tables only.
A course book replaces the slides: present every example in full, never refer the reader to a slide, and draw each mechanism on a small concrete instance.

## 2026-10-14 · course book · promoted → E14
Push-down was defined by its purpose ("move selections close to the table"); the reader could not apply it and did not see how an operator tree computes.
Define a transformation by its equivalence and condition, give numbered steps, and run them on a toy instance showing each intermediate result.
