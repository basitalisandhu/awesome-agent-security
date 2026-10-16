"""Tests for scripts/check_links.py. Offline: no request leaves the machine."""
import socket
import sys
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_links  # noqa: E402

HEADER = "# Awesome Test [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n\n> A list.\n\n"


def write(tmp_path, body, contents=("Tools",)):
    toc = "## Contents\n\n" + "".join(f"- [{t}](#{check_links.slug(t)})\n" for t in contents) + "\n"
    path = tmp_path / "README.md"
    path.write_text(HEADER + toc + body, encoding="utf-8")
    return path


def test_the_real_list_passes():
    assert check_links.check(ROOT / "README.md") == []


def test_a_well_formed_list_passes(tmp_path):
    path = write(tmp_path, "## Tools\n\n- [a](https://github.com/o/a) - Does a thing.\n")
    assert check_links.check(path) == []


@pytest.mark.parametrize("entry,message", [
    ("- [a](https://github.com/o/a) - does a thing.", "capital letter"),
    ("- [a](https://github.com/o/a) - Does a thing", "end with a period"),
    ("- [a](https://github.com/o/a) - The best thing.", "superlative"),
    ("- [a](https://github.com/o/a): Does a thing.", "entry must be"),
    ("- [a](github.com/o/a) - Does a thing.", "entry must be"),
])
def test_entry_format_problems(tmp_path, entry, message):
    path = write(tmp_path, f"## Tools\n\n{entry}\n")
    problems = check_links.check(path)
    assert any(message in p for p in problems), problems


def test_duplicate_links_ignore_case_and_trailing_slash(tmp_path):
    path = write(tmp_path, "## Tools\n\n- [a](https://github.com/O/A) - Does a.\n- [b](https://github.com/o/a/) - Does b.\n")
    assert any("duplicate link (first on line" in p for p in check_links.check(path))


def test_contents_must_match_sections(tmp_path):
    path = write(tmp_path, "## Tools\n\n- [a](https://github.com/o/a) - Does a.\n\n## More\n\n- [b](https://github.com/o/b) - Does b.\n")
    assert any("contents is out of sync" in p for p in check_links.check(path))


def test_fix_toc_rewrites_stale_contents(tmp_path):
    path = write(tmp_path, "## Tools\n\n- [a](https://github.com/o/a) - Does a.\n\n## More\n\n- [b](https://github.com/o/b) - Does b.\n")
    assert any("contents is out of sync" in p for p in check_links.check(path))
    assert check_links.main(["--fix-toc", str(path)]) == 0
    assert check_links.check(path) == []
    assert path.read_text(encoding="utf-8").count("- [Tools](#tools)") == 1
    assert "- [More](#more)" in path.read_text(encoding="utf-8")
    before = path.read_text(encoding="utf-8")
    assert check_links.main(["--fix-toc", str(path)]) == 0
    assert path.read_text(encoding="utf-8") == before


def test_title_badge_trailing_space_and_empty_section(tmp_path):
    path = tmp_path / "README.md"
    path.write_text("# Test\n\nno quote\n\n## Contents\n\n- [Tools](#tools)\n\n## Tools \n", encoding="utf-8")
    problems = " | ".join(check_links.check(path))
    for expected in ("awesome badge", "blockquote", "trailing whitespace"):
        assert expected in problems


def test_slug_matches_github_anchors():
    assert check_links.slug("Runtime controls and authorization") == "runtime-controls-and-authorization"
    assert check_links.slug("Scanners for MCP servers and skills") == "scanners-for-mcp-servers-and-skills"


class Response:
    def __init__(self, status):
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def fake_opener(outcomes):
    """outcomes maps (url, method) to a status code or an exception."""
    def opener(req, timeout=None):
        outcome = outcomes[(req.full_url, req.get_method())]
        if isinstance(outcome, Exception):
            raise outcome
        if outcome >= 400:
            raise urllib.error.HTTPError(req.full_url, outcome, "x", {}, None)
        return Response(outcome)
    return opener


def test_live_check_fails_only_on_dead_links(tmp_path):
    urls = {u: f"https://example.org/{u}" for u in ("ok", "gone", "walled", "headless", "nohost", "slow")}
    body = "## Tools\n\n" + "".join(f"- [{k}]({v}) - Does {k}.\n" for k, v in urls.items())
    path = write(tmp_path, body)
    dns = urllib.error.URLError(socket.gaierror(8, "nodename nor servname provided"))
    outcomes = {
        (urls["ok"], "HEAD"): 200,
        (urls["gone"], "HEAD"): 404,
        (urls["walled"], "HEAD"): 403, (urls["walled"], "GET"): 403,
        (urls["headless"], "HEAD"): 405, (urls["headless"], "GET"): 200,
        (urls["nohost"], "HEAD"): dns,
        (urls["slow"], "HEAD"): TimeoutError(), (urls["slow"], "GET"): TimeoutError(),
    }
    problems, warnings = check_links.live_check(path, 1.0, opener=fake_opener(outcomes))
    assert sorted(problems) == sorted([f"{urls['gone']}: dead (404)", f"{urls['nohost']}: dead (unknown host)"])
    assert sorted(warnings) == sorted([f"{urls['walled']}: 403", f"{urls['slow']}: TimeoutError"])
