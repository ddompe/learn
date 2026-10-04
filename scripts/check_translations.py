#!/usr/bin/env python3
"""
Check translation freshness and report on untranslated/stale content.

Compares English and Spanish lesson files to identify:
- Missing translations (English page with no Spanish counterpart)
- Stale translations (Spanish `sourceHash` differs from the current English body hash)
- Spanish pages without a `sourceHash` (cannot be checked)

The hash covers the body only (everything after the closing frontmatter `---`),
stripped of leading and trailing whitespace, sha256 hex truncated to 12 characters.
Frontmatter edits such as `lastVerified` therefore do not make a translation stale.
See planning/05-i18n.md.

Produces a warning report, not a failure (for CI: always exit 0).

Usage:
    python3 scripts/check_translations.py           # print the report
    python3 scripts/check_translations.py --markdown  # report as a Markdown table
    python3 scripts/check_translations.py --stamp   # rewrite sourceHash in Spanish pages
"""

import hashlib
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
EN_ROOT = REPO_ROOT / "src/content/docs/en"
ES_ROOT = REPO_ROOT / "src/content/docs/es"

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL)
SOURCE_HASH_RE = re.compile(r"^sourceHash:[ \t]*(.*?)[ \t]*$", re.MULTILINE)
STATUS_RE = re.compile(r"^translationStatus:[ \t]*(.*?)[ \t]*$", re.MULTILINE)


def split_frontmatter(text):
    """Return (frontmatter, body). Frontmatter is '' when the file has none."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return "", text
    return match.group(1), text[match.end():]


def body_hash(text):
    """sha256 of the page body, stripped, truncated to 12 hex characters."""
    _, body = split_frontmatter(text)
    return hashlib.sha256(body.strip().encode("utf-8")).hexdigest()[:12]


def frontmatter_value(frontmatter, pattern):
    match = pattern.search(frontmatter)
    if not match:
        return None
    return match.group(1).strip().strip("'\"") or None


def stamp(es_file, new_hash):
    """Set sourceHash in a Spanish page's frontmatter (add the key if missing)."""
    text = es_file.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return False
    frontmatter = match.group(1)
    if SOURCE_HASH_RE.search(frontmatter):
        frontmatter = SOURCE_HASH_RE.sub(f"sourceHash: '{new_hash}'", frontmatter)
    else:
        frontmatter += f"\nsourceHash: '{new_hash}'"
    new_text = f"---\n{frontmatter}\n---\n" + text[match.end():]
    es_file.write_text(new_text, encoding="utf-8")
    return True


def collect():
    """Classify every English page as missing, stale, unchecked, or current."""
    missing, stale, unchecked, current = [], [], [], []
    for en_file in sorted(EN_ROOT.glob("**/*.mdx")):
        rel = en_file.relative_to(EN_ROOT)
        es_file = ES_ROOT / rel
        if not es_file.exists():
            missing.append(rel)
            continue
        en_hash = body_hash(en_file.read_text(encoding="utf-8"))
        es_front, _ = split_frontmatter(es_file.read_text(encoding="utf-8"))
        es_hash = frontmatter_value(es_front, SOURCE_HASH_RE)
        status = frontmatter_value(es_front, STATUS_RE) or "unknown"
        if es_hash is None:
            unchecked.append(rel)
        elif es_hash != en_hash:
            stale.append((rel, es_hash, en_hash))
        else:
            current.append((rel, status))
    return missing, stale, unchecked, current


def check_translations(argv):
    if "--stamp" in argv:
        count = 0
        for en_file in sorted(EN_ROOT.glob("**/*.mdx")):
            rel = en_file.relative_to(EN_ROOT)
            es_file = ES_ROOT / rel
            if es_file.exists():
                new_hash = body_hash(en_file.read_text(encoding="utf-8"))
                count += stamp(es_file, new_hash)
        print(f"Stamped sourceHash on {count} Spanish pages.")
        return 0

    missing, stale, unchecked, current = collect()

    if "--markdown" in argv:
        print("| Page | State |")
        print("| ---- | ----- |")
        for rel in missing:
            print(f"| {rel} | missing |")
        for rel, _, _ in stale:
            print(f"| {rel} | stale |")
        for rel in unchecked:
            print(f"| {rel} | no sourceHash |")
        return 0

    print(f"\nTranslated and current: {len(current)}")
    by_status = {}
    for _, status in current:
        by_status[status] = by_status.get(status, 0) + 1
    for status, count in sorted(by_status.items()):
        print(f"   - {status}: {count}")

    if stale:
        print(f"\nWARNING: Stale Spanish translations ({len(stale)}):")
        for rel, es_hash, en_hash in stale:
            print(f"   - {rel} (sourceHash {es_hash}, English now {en_hash})")
    else:
        print("\nOK: No stale Spanish translations")

    if unchecked:
        print(f"\nWARNING: Spanish pages without sourceHash ({len(unchecked)}):")
        for rel in unchecked:
            print(f"   - {rel}")

    if missing:
        print(f"\nWARNING: Missing Spanish translations ({len(missing)}):")
        for rel in missing:
            print(f"   - {rel}")
    else:
        print("\nOK: All Spanish translation files exist")

    return 0


if __name__ == "__main__":
    sys.exit(check_translations(sys.argv[1:]))
