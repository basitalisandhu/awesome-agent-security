#!/usr/bin/env python3
"""Check the list against the awesome conventions: format, table of contents, duplicates.

Offline by default. ``--live`` also requests every entry link (needs network access) and
fails on dead links only (404, 410, unknown host); bot walls and timeouts are warnings.
Exit code 1 when any problem is found.
"""

from __future__ import annotations

import argparse
import re
import socket
import sys
from pathlib import Path

ENTRY_RE = re.compile(r"^- \[(?P<name>[^\]]+)\]\((?P<url>https?://[^)\s]+)\) - (?P<desc>.+)$")
HEADING_RE = re.compile(r"^(#{2,3}) (.+?)\s*$")
BADGE = "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)"
SKIP_SECTIONS = {"Contents", "Contributing", "Related projects"}


def slug(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s+", "-", s.strip())


def check(path: Path) -> list[str]:
    problems: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or not lines[0].startswith("# Awesome ") or BADGE not in lines[0]:
        problems.append("line 1: title must be '# Awesome ...' with the awesome badge")
    if len(lines) < 3 or not lines[2].startswith("> "):
        problems.append("line 3: a one-line blockquote description must follow the title")

    toc: list[str] = []
    in_toc = False
    sections: list[tuple[str, int]] = []
    section = None
    seen_urls: dict[str, int] = {}
    entries_per_section: dict[str, int] = {}
    for number, line in enumerate(lines, start=1):
        if line.rstrip() != line:
            problems.append(f"line {number}: trailing whitespace")
        heading = HEADING_RE.match(line)
        if heading:
            level, title = heading.group(1), heading.group(2)
            if level == "##":
                sections.append((title, number))
                in_toc = title == "Contents"
                section = None if title in SKIP_SECTIONS else title
            else:
                if section is None:
                    problems.append(f"line {number}: '### {title}' outside a list section")
                section = title
            if section:
                entries_per_section.setdefault(section, 0)
            continue
        if in_toc:
            m = re.match(r"^- \[([^\]]+)\]\(#([^)]+)\)$", line)
            if m:
                toc.append(m.group(2))
            elif line.strip():
                problems.append(f"line {number}: contents entries must be '- [Name](#anchor)'")
            continue
        if section is None or not line.startswith("- "):
            continue
        m = ENTRY_RE.match(line)
        if not m:
            problems.append(f"line {number}: entry must be '- [Name](https://...) - Description.'")
            continue
        entries_per_section[section] = entries_per_section.get(section, 0) + 1
        desc = m.group("desc")
        if not desc[0].isupper():
            problems.append(f"line {number}: description must start with a capital letter")
        if not desc.endswith("."):
            problems.append(f"line {number}: description must end with a period")
        if re.search(r"\b(best(?! practice)|fastest|most powerful|world-class|leading|number one|#1)\b", desc, re.I):
            problems.append(f"line {number}: description contains a superlative")
        url = m.group("url").rstrip("/").lower()
        if url in seen_urls:
            problems.append(f"line {number}: duplicate link (first on line {seen_urls[url]})")
        else:
            seen_urls[url] = number

    expected_toc = [slug(t) for t, _ in sections if t != "Contents"]
    if toc != expected_toc:
        problems.append(f"contents is out of sync with the sections: {toc} != {expected_toc}")
    if sections and sections[0][0] != "Contents":
        problems.append("the first section must be 'Contents'")
    for name, count in entries_per_section.items():
        if count == 0:
            problems.append(f"section '{name}' has no entries")
    return problems


DEAD_STATUSES = {404, 410}


def request_status(url: str, timeout: float, opener=None) -> int | str:
    """HTTP status for url (HEAD, then GET when HEAD is refused), or an error name.

    ``opener`` defaults to urllib's urlopen and is injectable for tests.
    """
    import urllib.error
    import urllib.request

    opener = opener or urllib.request.urlopen
    status: int | str = "error"
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": "awesome-agent-security-check/1.1"})
        try:
            with opener(req, timeout=timeout) as resp:  # noqa: S310 - https links from the list
                return resp.status
        except urllib.error.HTTPError as exc:
            status = exc.code
            if exc.code in DEAD_STATUSES:
                return exc.code
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            reason = getattr(exc, "reason", exc)
            if isinstance(reason, socket.gaierror):
                return "unknown host"
            status = type(reason).__name__
    return status


def live_check(path: Path, timeout: float, opener=None) -> tuple[list[str], list[str]]:
    """Request every entry link. Returns (problems, warnings).

    A link is a problem only when it is dead: 404, 410 or a host that does not resolve.
    Anything else that is not 2xx (bot walls, rate limits, timeouts) is a warning.
    """
    problems: list[str] = []
    warnings: list[str] = []
    urls = sorted({m.group("url") for line in path.read_text(encoding="utf-8").splitlines() if (m := ENTRY_RE.match(line))})
    for url in urls:
        status = request_status(url, timeout, opener)
        if isinstance(status, int) and 200 <= status < 400:
            continue
        if status in DEAD_STATUSES or status == "unknown host":
            problems.append(f"{url}: dead ({status})")
        else:
            warnings.append(f"{url}: {status}")
    return problems, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readme", nargs="?", default=str(Path(__file__).resolve().parent.parent / "README.md"))
    parser.add_argument("--live", action="store_true", help="also request every link")
    parser.add_argument("--timeout", type=float, default=10.0)
    args = parser.parse_args(argv)
    path = Path(args.readme)
    problems = check(path)
    if args.live:
        dead, warnings = live_check(path, args.timeout)
        problems += dead
        for w in warnings:
            print(f"warning: {w}")
    entries = sum(1 for line in path.read_text(encoding="utf-8").splitlines() if ENTRY_RE.match(line))
    for p in problems:
        print(f"error: {p}")
    print(f"{entries} entries checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
