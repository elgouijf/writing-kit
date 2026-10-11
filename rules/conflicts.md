# Conflicts found between the sources, and how they were settled

The kit merges three pipelines: the lessons of a four-month engineering internship report (119 lessons, a school's ID-tagged rules, a rewrite brief, a handoff), the coursework rules of an exchange semester (the user's own corrections S1–S9 and a course's academic-English rules), and the explaining rules for course books. Every contradiction found between them is listed here with its resolution, so that no two rules in `rules/` disagree.

| # | Conflict | Resolution | Rules |
|---|---|---|---|
| 1 | Voice. A school rule asks for indirect style except for the contribution; later author corrections ask for the first person plural; coursework corrections forbid "I" and "we"; a reflection asks for feelings | Voice belongs to the document profile; one voice per document | P1–P7, W4 |
| 2 | Contribution. The rewrite brief wanted a "personal contribution" heading under every project; the author later banned personal-contribution sections; the school requires the contribution to be unambiguous | Stated once, unambiguously, in one place | O10 |
| 3 | Hedging. "No hedging with may" against a course that teaches hedged conclusions | No reflexive or uniform hedging; claim strength calibrated to the evidence | B4, B5, P4 |
| 4 | "rather than" was to be replaced by ", not …", while "X, not Y" was later named the most recognisable machine tic | "instead of"; at most one antithesis per document | B2, B3 |
| 5 | Headings. Coursework: never a leading gerund. Internship: "Balancing strictness and tolerance" accepted over "Balance between strictness and tolerance" | Noun phrase by default; no gerund that narrates what the section does; a gerund naming a trade-off when the noun reads worse | T1, T2 |
| 6 | Headings. Coursework: never a clause. Internship: supervisors approved declarative headings ("One project consumed far more resources than the others") | An approved heading stays as approved; new headings follow T1 | T3 |
| 7 | Examples. "At most one example per point" against "analogies and worked examples are required" when explaining | Scoped by profile: deliverables against explanations | O4, P6, E1 |
| 8 | Length. "Pay for added prose with prose removed" against "longer is better, too short scores low" | Set by the brief and the profile | O13, P3 |
| 9 | Sentences. "Vary length, short sentences are human" against "short sentences read as slogans" | A short sentence with a real actor stating a decision stays; a moral with no agent goes | S1, B9 |
| 10 | Dates. "No dates in the narrative" (report with the period on its cover) against coursework where dates are content | Narrative dates out, content dates stay | B20 |
| 11 | Narrative. "Tell the story as it happened" against "not a chronological account" | Owner and causality yes, a diary structure no | W9, O17 |
| 12 | First person in reports. "Give a narrative sentence its owner" against "do not open every sentence with we" | Both hold: owner when narrating, subjects alternated | W3, W5 |
| 13 | Check scripts. Two versions (an internship one comparing two PDFs, a coursework one checking output against sources) | One script with both modes | `tools/check_numbers.py` |
| 14 | Author naming in formal documents. SURNAME in capitals (internship) and plain names elsewhere | Capitals in formal documents only | R15 |

## Where each original rule went

| Source | Now |
|---|---|
| Internship lessons 1–13 (feedback loop) | F1–F15 |
| 14–30 (verifying facts) | V1–V18; lesson 17 (one company's system names) dropped as a fact, its general form is V11; lesson 21 is O14 |
| 31–91 (register) | R, W, S, B, O, T modules; lesson 63's approved headings are T3; lesson 96 (orange reserved for two brands) generalised as G7 |
| 92–106 (figures) | G1–G14; lesson 106 is O14 |
| 107 (page budget) | O13 |
| 108–119 (build pitfalls) | X1–X15 |
| §7 convergence, §8 checklist | C1–C8 and the final checklist |
| School rules A1–A8, B, C, F (layout, length, cover, confidentiality) | Project-specific: keep them in the project; the general ones are G2, O13, O16, V20 |
| School rules D1–D8 | O1, R8, R12, O17, P1 (D5), O10 (D6), G2 (D7), T4 (D8) |
| School rule G (what to ask the author) | V19 |
| Rewrite brief, writing style | R3, R4, S1, V16, B10, B12, B13, B7 |
| Coursework S1–S9 (the user's corrections) | R6 (S1), O4 (S2), O5 (S3), W11 (S4), S11 (S5), C4 (S6), W12 (S7), T1/T5/T9 (S8), P2/P3 (S9) |
| Explaining E1–E6 | E1–E6 |
| Academic-English course rules | P4, B22 |
| Handoff and project instructions, "style as enforced" | B1, B2, B20, R16, O9, O6, V1, R5, O10, V17, G1, T7; company facts dropped |
