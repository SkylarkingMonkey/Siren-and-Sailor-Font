#!/usr/bin/env python3
"""Apply owner-approved OFL metadata locally; never publish or contact GitHub.

The default mode validates inputs and prints the planned changes without writing.
Use --approve-ofl only after the copyright owner has approved public OFL release.
This does not sign the CLA, certify ownership, or establish repository existence.
"""

from __future__ import annotations

import argparse
from datetime import date
from html import escape
import json
import os
from pathlib import Path
import plistlib
import re
import tempfile
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
FAMILY = "Siren and Sailor"
ORIGINAL_COPYRIGHT = "Copyright 2026 Jean-Marc Daecius"
LICENSE_TEXT = (
    "This Font Software is licensed under the SIL Open Font License, Version 1.1. "
    "This license is available with a FAQ at: https://openfontlicense.org"
)


def repository_url(value: str) -> str:
    """Validate a canonical GitHub repository URL, without any network action."""
    parsed = urlsplit(value.strip())
    if (
        parsed.scheme != "https"
        or parsed.netloc != "github.com"
        or parsed.query
        or parsed.fragment
    ):
        raise argparse.ArgumentTypeError(
            "Use https://github.com/ACCOUNT/REPOSITORY without credentials, port, query, or fragment."
        )
    parts = parsed.path.rstrip("/").split("/")
    if len(parts) != 3 or parts[0] != "":
        raise argparse.ArgumentTypeError("Supply a repository URL, not a branch, file, or profile URL.")
    account, repository = parts[1:]
    if repository.endswith(".git"):
        repository = repository[:-4]
    if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?", account):
        raise argparse.ArgumentTypeError("Invalid GitHub account name.")
    if "--" in account or not re.fullmatch(r"[A-Za-z0-9._-]{1,100}", repository):
        raise argparse.ArgumentTypeError("Invalid GitHub repository path.")
    placeholders = {"account", "actual", "example", "owner", "username", "your", "your-account", "your-repo", "repository", "repo"}
    if account.lower() in placeholders or repository.lower() in placeholders or repository in {".", ".."}:
        raise argparse.ArgumentTypeError("Replace placeholder account/repository names with the real public repository.")
    return f"https://github.com/{account}/{repository}"


def atomic_write(path: Path, content: bytes) -> None:
    """Replace a single preflighted file atomically, using its own directory."""
    with tempfile.NamedTemporaryFile(prefix=f".{path.name}.", dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(content)
    try:
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def catalog_date(value: str) -> str:
    """Require an explicit, valid ISO calendar date; do not infer one."""
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise argparse.ArgumentTypeError("Use the actual Google Fonts catalog date in YYYY-MM-DD format.")
    try:
        date.fromisoformat(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("The supplied catalog date is not a valid calendar date.") from error
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-url", required=True, type=repository_url)
    parser.add_argument(
        "--catalog-date",
        type=catalog_date,
        help="Actual Google Fonts intake date, YYYY-MM-DD. Only supply when known; without it no live METADATA.pb is emitted.",
    )
    parser.add_argument(
        "--approve-ofl",
        action="store_true",
        help="Apply the owner's explicit approval to release this family under SIL OFL 1.1. Without this flag no files change.",
    )
    args = parser.parse_args()
    copyright_notice = f"Copyright 2026 The {FAMILY} Project Authors ({args.repository_url})"

    info_path = ROOT / "sources/SirenandSailor-Regular.ufo/fontinfo.plist"
    stage = ROOT / "googlefonts/ofl/sirenandsailor"
    metadata_template = ROOT / "documentation/METADATA.pb.in"
    metadata_path = stage / "METADATA.pb"
    description_path = stage / "DESCRIPTION.en_us.html"
    proposed = ROOT / "documentation/OFL-proposed.txt"
    root_license = ROOT / "OFL.txt"
    license_source = proposed if proposed.exists() else root_license

    # Preflight every input before making changes. Refuse an unexpected rights notice.
    info = plistlib.loads(info_path.read_bytes())
    if info.get("familyName") != FAMILY:
        raise ValueError("The source family name does not match this finalizer.")
    if info.get("copyright") not in {ORIGINAL_COPYRIGHT, copyright_notice}:
        raise ValueError("Unexpected source copyright; review all rights holders before changing it.")
    old_license = license_source.read_text(encoding="utf-8")
    first_line, separator, body = old_license.partition("\n")
    if not separator or first_line not in {ORIGINAL_COPYRIGHT, copyright_notice}:
        raise ValueError("Unexpected proposed license copyright; review it manually.")
    if "SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007" not in body:
        raise ValueError("The proposed file is not the expected OFL 1.1 text.")
    if "https://openfontlicense.org" not in body:
        raise ValueError("The proposed file does not contain the expected OFL URL.")
    if root_license.exists() and root_license.read_text(encoding="utf-8").partition("\n")[2] != body:
        raise ValueError("Existing root OFL differs from the proposal; refusing to overwrite it.")
    license_bytes = (copyright_notice + "\n" + body).encode("utf-8")

    if metadata_path.exists() and not args.catalog_date:
        raise ValueError("A live METADATA.pb already exists. Supply its confirmed catalog date to update it; do not silently rewrite it without a date.")
    metadata = metadata_template.read_text(encoding="utf-8")
    if re.search(r"^date_added:", metadata, re.MULTILINE):
        raise ValueError("The input metadata template should not contain a catalog date; review it manually.")
    copyrights = re.findall(r'^\s*copyright:\s*"([^"\n]*)"\s*$', metadata, re.MULTILINE)
    if len(copyrights) != 1 or copyrights[0] not in {ORIGINAL_COPYRIGHT, copyright_notice}:
        raise ValueError("Unexpected staging copyright fields; inspect METADATA.pb manually.")
    metadata = re.sub(
        r'^(\s*copyright:)\s*"[^"\n]*"\s*$',
        lambda match: match.group(1) + " " + json.dumps(copyright_notice),
        metadata,
        count=1,
        flags=re.MULTILINE,
    )
    source_urls = re.findall(r'^\s*repository_url:\s*"([^"\n]*)"', metadata, re.MULTILINE)
    if source_urls:
        if source_urls != [args.repository_url]:
            raise ValueError("Staging metadata already identifies a different upstream repository.")
    elif re.search(r"^source\s*\{", metadata, re.MULTILINE):
        raise ValueError("Existing source block has no repository URL; inspect it manually.")
    else:
        metadata = metadata.rstrip() + "\nsource {\n  repository_url: " + json.dumps(args.repository_url) + "\n}\n"
    metadata = metadata.replace(
        "# Draft: public upstream source URL and matching project copyright are pending.\n", ""
    )

    description = description_path.read_text(encoding="utf-8")
    upstream_paragraph = (
        '<!-- upstream-repository -->\n<p>To contribute, see <a href="'
        + escape(args.repository_url, quote=True)
        + '">'
        + escape(args.repository_url.removeprefix("https://"))
        + '</a>.</p>\n<!-- /upstream-repository -->'
    )
    upstream_pattern = r"<!-- upstream-repository -->.*?<!-- /upstream-repository -->"
    if re.search(upstream_pattern, description, re.DOTALL):
        description = re.sub(upstream_pattern, lambda _: upstream_paragraph, description, count=1, flags=re.DOTALL)
    else:
        description = description.rstrip() + "\n" + upstream_paragraph + "\n"

    info["copyright"] = copyright_notice
    info["openTypeNameLicense"] = LICENSE_TEXT
    info["openTypeNameLicenseURL"] = "https://openfontlicense.org"
    updates = {
        info_path: plistlib.dumps(info, sort_keys=True),
        metadata_template: metadata.encode("utf-8"),
        description_path: description.encode("utf-8"),
        root_license: license_bytes,
        stage / "OFL.txt": license_bytes,
    }
    if args.catalog_date:
        catalog_metadata = metadata.replace(
            "# Draft: date_added must be set when Google Fonts actually adds the family.\n", ""
        )
        catalog_metadata, count = re.subn(
            r'^(category:\s*"[^"\n]+")$',
            lambda match: match.group(1) + '\ndate_added: ' + json.dumps(args.catalog_date),
            catalog_metadata,
            count=1,
            flags=re.MULTILINE,
        )
        if count != 1:
            raise ValueError("Could not identify the catalog metadata category field.")
        updates[metadata_path] = catalog_metadata.encode("utf-8")
    print("Repository URL syntax accepted. Existence, public visibility, and ownership are not checked.")
    print("Proposed copyright:", copyright_notice)
    for path in updates:
        print("Update:", path.relative_to(ROOT))
    if proposed.exists():
        print("Move proposal to root OFL.txt after successful writes:", proposed.relative_to(ROOT))
    if not args.approve_ofl:
        print("DRY RUN: no files changed. Apply --approve-ofl only after the owner approves public OFL release.")
        return 0

    for path, content in updates.items():
        atomic_write(path, content)
    if proposed.exists():
        proposed.unlink()
    print("Approved OFL metadata applied locally. Nothing has been published or submitted.")
    print("Required next step: run python scripts/build.py and rerun the complete QA on the rebuilt font.")
    print("Do not rerun prepare_sources.py after finalization: it is a one-time preparation script with draft metadata.")
    if args.catalog_date:
        print("Live catalog metadata emitted using the explicitly supplied date. Validate its complete schema and rerun catalog QA.")
    else:
        print("Updated only documentation/METADATA.pb.in; no live catalog metadata was emitted because the actual intake date is unknown.")
        print("An upstream issue submission does not require catalog METADATA.pb. Catalog-dependent QA checks remain inapplicable until intake.")
    print("Update pending statements in the release documents using the owner's confirmed decisions.")
    print("CLA, public repository verification, designer approval, and actual Google Fonts intake remain separate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
