# C. The convergence loop and the final checklist

A pass is not done when the last paragraph is rewritten. Loop until two consecutive passes find nothing. Scans are necessary, never sufficient: the first lecture summaries passed every scan and were still rejected as "AI slop" because a dozen sentences opened with "The lecture". (user)

- **C1. Rewrite one section at a time**, with replacements that fail loudly when a passage has moved (X3).
- **C2. Scan the source.** `python3 tools/check_style.py <file-or-dir>` flags passives, "may", clefts, "rather than", em-dashes, `, -ing` adjuncts, "X, not Y", intensifiers, "there is", "by -ing", two colons in a sentence, bare "This is" openers, ordinals and sentences over 45 words. Count colons in prose sentences, not in TikZ keys or tables.
- **C3. Scan openers and rhythm.** Count the first two words of every sentence (no opener more than about four times per text), the spread of sentence lengths, and the uses of "also", "therefore" and tricolons.
- **C4. Read the whole built output**, not the source. Only reading finds an abrupt sentence, a maxim, or three sentences in a row with the same subject. Ask whether it sounds like a person explaining what they understood.
- **C5. Scan for repetition**: repeated 5-grams across the whole text; terms of the subject are exempt.
- **C6. Prove the content did not move.** `python3 tools/check_numbers.py OUTPUT SOURCE…` lists every number of the output that no source contains; `--compare OLD.pdf NEW.pdf` lists every number gained or lost by a rewrite. Accepted differences: a number written as a word, and the numbers a requested addition brings.
- **C7. Decide which flags to overrule.** A stative "is", the author's own wording or the source's own enumeration can stay; knowing which flags to overrule is part of the pass.
- **C8. Grep the headings** (T9) and every removed claim (F2).

## Final checklist

1. The brief's own requirements are met point by point (length, format, language, required sections, a school's checklist confirmed ID by ID).
2. Annotations extracted from the previous PDF and the annotated file backed up (F11).
3. Every note applied, or its deviation explained in the reply.
4. Every changed number re-read from its live source.
5. A grep finds no trace of any removed claim, number or label.
6. No em-dash, no "rather than", no maxim endings, no numbers in the conclusion, no dates as narrative.
7. LaTeX: clean builds (X4), rendered pages looked at (X5), no float before its citation, body length reported.
8. The AI-use statement, when the context requires one, says which tool was used, where and how, and the text is the author's own.
9. The reply lists what changed, what was not applied and why, and what the author still has to supply.
