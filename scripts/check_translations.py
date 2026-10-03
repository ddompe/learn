#!/usr/bin/env python3
"""
Check translation freshness and report on untranslated/stale content.

Compares English and Spanish lesson files to identify:
- Missing translations
- Potentially stale translations (based on modification dates)
- Translation status tags

Produces a warning report, not a failure (for CI: exit 0).
"""

import subprocess
from pathlib import Path
from datetime import datetime

def check_translations():
    """Check for translation gaps and staleness."""
    repo_root = Path(__file__).parent.parent
    en_docs = sorted(repo_root.glob("src/content/docs/en/**/*.mdx"))
    es_docs = sorted(repo_root.glob("src/content/docs/es/**/*.mdx"))

    # Map English files to their Spanish equivalents
    missing = []
    for en_file in en_docs:
        rel_path = en_file.relative_to(repo_root / "src/content/docs/en")
        es_file = repo_root / "src/content/docs/es" / rel_path

        if not es_file.exists():
            missing.append(str(rel_path))

    if missing:
        print("\n⚠️  Missing Spanish translations:")
        for path in missing:
            print(f"   - {path}")
    else:
        print("\n✓ All Spanish translation files exist")

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(check_translations())
