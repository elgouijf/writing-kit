# Q. Independent second opinion

Before submitting a long document, ask a reviewer that did not write it (another model, another session, a human) for a blunt, read-only review. Treat the answer under F13 and F14.

- **Q1. Give the reviewer the rules, not the conversation.** It reads the project's instructions, the school's rules and the text as the reader will see it (the built PDF), then the source for line references.
- **Q2. Make it check numbers against the sources, never against the text itself**, and say "unverifiable from here" when a source is out of reach.
- **Q3. Tell it what not to flag**: deliberate `\tofill` gaps, items already listed as open questions, the approved layout, and the author's deliberate structural choices.
- **Q4. Ask for a ranked, located, short output.**

## Prompt template

```text
You are reviewing <document> before it is submitted to <reader>. Read only; make no edits.

Read, in this order: <project instructions>, <school or brief rules, ID-tagged>,
<built PDF>, <source tree for line references>, <list of deliberate open items>.

Hard constraints: <page budget>, <caption rule>, clean build (0 errors, 0 undefined
references, 0 overfull boxes). Anything you propose adding must name what comes out.

Style rules the author enforces: <paste the relevant rule IDs and one-line forms>.

Numbers: check every figure against its source, never against another sentence of the
document. If a source is unreachable, say the claim is unverifiable and name the file
that would settle it. Never substitute a plausible number.

Look for, in order: factual errors and unverifiable claims; internal contradictions;
corrections that made things worse; redundancy; slop and filler; unsupported reasoning;
structure and school rules; language (calques, prepositions, tense drift); LaTeX hygiene.

Do not flag: <deliberate gaps>, <open questions>, <approved layout>, <deliberate choices>.

Output: (1) a five-line verdict and the single biggest risk; (2) the top ten findings,
each with file:line, a quote of at most 20 words, the problem, a one-sentence fix and a
severity (blocking / should fix / nice to have); (3) the remaining findings by category;
(4) a verification log: each number checked, its source, confirmed / contradicted /
unverifiable. Be blunt. Do not praise.
```
