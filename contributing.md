# Contribution guidelines

Thank you for helping keep this list useful. Please read the inclusion criteria before opening a pull request.

## Inclusion criteria

An entry is accepted when all of the following hold:

- It is about securing AI agents, tool-using LLM applications or the protocols they use (MCP, A2A), or about measuring their failures. General security tools are included only when agent runtimes depend on them (for example sandboxes).
- It is public, documented (a README that explains what it does and how to use it) and maintained: not archived, not deprecated, with activity in the last twelve months.
  Papers, datasets, benchmarks, talk material and other lists are finished artefacts, so the activity rule does not apply to them; they must still not be archived or deprecated.
- It exists and can be checked: a GitHub repository, or for papers the paper's official code repository. Links to recordings or pages that cannot be verified are not accepted.
- The description is one sentence in the project's own words, shortened, without superlatives or marketing. It says what the project does, not how good it is.
- It is not already listed. Duplicate links are rejected by the check script.

Projects by the list maintainer follow the same rules and are listed in their sections without preference.

## Format

Entries follow the [awesome](https://github.com/sindresorhus/awesome/blob/main/awesome.md) conventions:

```markdown
- [Project Name](https://github.com/owner/repo) - What it does, starting with a capital letter and ending with a period.
```

- Add the entry at the end of the most specific section. Do not create a new section for one entry.
- Keep the table of contents in sync with the section headings.
- Do not add badges, images, star counts or "inspired by" lines.

## Checks

```bash
python3 scripts/check_links.py            # format, table of contents, duplicate links (offline)
python3 scripts/check_links.py --live     # also request every link; fails on 404, 410 or an unknown host
python3 -m pip install pytest && python3 -m pytest -q   # tests for the check script
```

CI runs the format check, the tests and the live link check on every pull request, and the live check again every Monday. Bot walls and timeouts in the live check are printed as warnings and do not fail the build.

## Removing entries

Open an issue or a pull request when a project is archived, has not been updated in a year, no longer matches its description, or has been superseded by its own successor. Mention the evidence (archive banner, last commit date, redirect).

## Security

If a listed project has turned malicious or been taken over, report it privately as described in [SECURITY.md](SECURITY.md) rather than in a public issue.

## Code of conduct

This project follows the [code of conduct](code-of-conduct.md).
