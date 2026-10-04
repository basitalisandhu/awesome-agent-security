# Good first issues

Issues the maintainer intends to open under the `good first issue` label. Each is a small,
self-contained change; read [contributing.md](../contributing.md) first and run
`python3 scripts/check_links.py` before opening a pull request.

## 1. Add a verified talk recording to the Talks section

**Context.** The Talks section lists only repository-hosted material because recordings were not
verifiable when the list was created.

**Acceptance criteria.**

- One entry per pull request: a talk about agent security (prompt injection in agents, MCP
  security, agent sandboxing or authorization) given at a public conference.
- The link points at the conference's own page or the official recording, and the description
  names the speaker, the event and the year in the project-neutral style of the other entries.
- The check script passes.

## 2. Add an "Observability and detection" section

**Context.** Several projects record and analyse agent tool calls after the fact (traces, audit
logs, anomaly detection) rather than blocking them. They do not fit the current sections.

**Acceptance criteria.**

- A new `## Observability and detection` section placed after "Runtime controls and authorization",
  with at least four entries that meet the inclusion criteria.
- The Contents list is updated and the check script passes.

## 3. Mark the maintenance status of every entry in a monthly check

**Context.** Entries must be maintained (activity in the last twelve months). Nothing checks that
today.

**Acceptance criteria.**

- `scripts/check_links.py --activity` queries the GitHub API (unauthenticated, with a token when
  `GITHUB_TOKEN` is set) for `archived` and `pushed_at` of every `github.com` entry and reports
  archived repositories and repositories with no push in twelve months.
- The weekly CI job runs it as informational (`continue-on-error: true`), like the liveness check.
- Rate limits are handled (sleep and retry once, then report "unknown").

## 4. Issue form for proposing an entry

**Acceptance criteria.**

- `.github/ISSUE_TEMPLATE/add-entry.yml` with fields: section (dropdown over the current
  sections), repository URL, one-sentence description, and a checkbox list restating the
  inclusion criteria.
- `.github/ISSUE_TEMPLATE/config.yml` disabling blank issues.
- Both parse as YAML; contributing.md links the form.

## 5. Generate the Contents list from the headings

**Context.** The Contents list is kept by hand and the check script only reports drift.

**Acceptance criteria.**

- `scripts/check_links.py --fix-toc` rewrites the Contents block from the section headings.
- A test (`tests/test_check.py`, run in CI) covers a README with a stale Contents list before and
  after `--fix-toc`.
