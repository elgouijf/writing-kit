# Contributing

## From a correction to a rule

1. **Record it at once.** When the user corrects a text or an explanation, append an entry to `lessons/INBOX.md` (format at its top): date, scope tag, what was wrong, the rule it suggests.
2. **Promote it when it is general and contradicts nothing.** Write it into the right module as `- **ID. Title.** Explanation, one example at most. (source)`, with the next free ID of that module, then run `python3 tools/build_index.py`, and mark the inbox entry `promoted → ID`.
3. **When it contradicts a rule or fits one context only**, leave it `open` and ask the user. If the user settles it, record the resolution in `rules/conflicts.md` and adjust the profiles or the rules so that no two rules disagree.
4. **Commit the kit right away** (`git -C <kit> add -A && git -C <kit> commit -m "rule: ..."`), pulling first when a remote exists, so that parallel sessions and worktrees do not overwrite each other.

## What never goes in

- Personal data: names, student or employee IDs, addresses, e-mail addresses.
- Anything from an employer or a client: figures, system names used as facts, customer data, screenshots. Generalise the lesson and keep the example generic.
- Logos and images you do not own.

These belong in a private profile or in the project's own repository.

## Rule style

Rules obey themselves: active voice, a real actor, no em-dash, no "rather than", one example at most, the source in brackets (`user`, `review`, `school`, `exp`).

## Releases

Bump `version` in `.claude-plugin/plugin.json` and add a line to `CHANGELOG.md` when rules change meaning; typo fixes need neither.
