# E. Explaining a concept, summarising a lecture, writing a course book

These rules govern what is written to **teach the user**, not what the user hands in (profiles P1–P5 cover that).

- **E1. Build every mechanism from zero before using it.** Analogy in plain words, then a step-by-step construction on a tiny example, then the formula, then the source's own example. An interactive table of an inverted index was useless to a reader who did not know what an index is. (user)
- **E2. Define every difficult term where it first appears.** Not only the source's keywords: anything a first-year student would not know. In a course book, a margin definition; in chat, one plain sentence or a short glossary block. (user)
- **E3. Formula first, then each symbol, then the meaning in words.** Write the formula; define each symbol on its own line; say what the numerator and the denominator (or each part) mean; give one analogy; then a minimal numeric example; then how to read the value (what 0, 1 or a negative value means). A coefficient needed three attempts because the first two leaned on graphics and on the result instead of on the meaning of the formula. (user)
- **E4. When the user asks for text, answer in text.** No widget or diagram for that answer: graphics help an explanation, they never replace the sentence that explains. (user)
- **E5. Put the full content where the user can read it.** A summary in chat is not enough when the user needs the material: lay out every definition and every formula in the chat when asked, and keep a complete version (every derivation, table and rule of the source, plus the background it assumes) in the course book. (user)
- **E6. Say what a quantity or a tool is for, and what it does not do.** A coefficient measures agreement and does not raise it; an LLM judge grades and does not search. (user)
- **E7. Connect to what the reader already knows.** Attention is a search inside the sentence; retrieval-augmented generation is the search engine of an earlier week feeding the language model of a later one. (exp)
- **E8. Mark everything that is not in the source.** "(added, not in the lecture)" on examples, a side note on added background, "illustrative values" in a caption. Never invent a number; recompute every worked number. (user)
- **E9. Show the source when a claim depends on it.** When the user asks how a deliverable relates to its sources, give screenshots of the sources themselves and map each part of the text to the record it comes from. (user)
- **E10. A course book is complete and as short as possible.** It covers every week from the first, keeps every definition, derivation, table and rule, and says each thing once: no restated boxes, recaps that repeat the chapter or padding around a formula. (user)
- **E11. Draw structures as real figures, never ASCII art.** A network, a tree, a pipeline or a memory layout gets a rendered diagram (an SVG widget in chat, TikZ in a course book), with the explaining sentences still in text (E4). ASCII drawings of a tree and a fat tree were rejected. (user)
- **E12. A course book stands on its own.** It presents the source in full (schemas, data, examples, rules) so the reader never needs the slides: no "(slide 10)", no "see the slide", no slide numbers as references. Attribute in words when it matters ("the lecture's example"); the source file is named once, in the lecture card. A chapter citing a slide in nearly every paragraph was rejected. (user)
- **E13. Every mechanism gets a figure that explains better than the source's.** A storage structure, an algorithm, a protocol or a timeline is drawn on a small concrete instance with real values and the path of one operation (a hash file with its keys and an overflow page, a join with the comparisons it makes, a log with what is redone). A table or a sentence alone was rejected where a figure fits. (user)

## Shape of an explanation

1. One line on what it is for.
2. An intuition: an everyday analogy (the index at the back of a book; a true/false exam corrected for guessing; a phone keyboard predicting the next word).
3. A construction on a toy example of 3 to 10 items, every number recomputed.
4. The formula, its symbols and the reading of its value (E3).
5. The source's own example and numbers, quoted exactly.
6. The connection to earlier material (E7).
7. The traps an exam sets.

## Course book (template `templates/course-book/`)

- One cumulative, complete, self-sufficient book per course (E12), one chapter per week, a figure per mechanism (E13); definitions in the margin column (`\term{key}`), declared once in the course's `glossary.tex`.
- Boxes: `definition` (formula or rule to know), `intuition` (analogy), `worked` (example, `\addedtag` when added), `traps`, `recap`, `lecturecard` (source, lecturer, assignment verdict).
- `\term` only in running paragraphs (X13); `\gls{key}` inside boxes, tables and figures.
- Figures within the text width; split long equations with `align*`; render and look at every new page (X5).
- Fold every clarification the user asked for during the session into the chapter.
