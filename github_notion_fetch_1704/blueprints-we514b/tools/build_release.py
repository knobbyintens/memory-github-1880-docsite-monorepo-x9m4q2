#!/usr/bin/env python3
"""Quarterly packaging pipeline for Blueprint Atlas.

Usage:
    python tools/build_release.py --source blueprints --dest <release-dir>

A package is accepted into a release pool only when every file in
REQUIRED_FILES is present and non-empty. The list below is the authoritative
packaging contract.
"""

import argparse
import shutil
from pathlib import Path

REQUIRED_FILES = [
    "docs/task.md",
    "docs/agent_system_prompt.md",
    "evaluation/main.py",
]

# Files that may be present but are not required for a release.
OPTIONAL_FILES = [
    "preprocess/main.py",
    "groundtruth_workspace/actions.json",
    "initial_workspace/README.md",
]


def package_is_releasable(package_dir: Path) -> bool:
    for relative in REQUIRED_FILES:
        candidate = package_dir / relative
        if not candidate.is_file() or not candidate.read_text(encoding="utf-8").strip():
            return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="blueprints")
    parser.add_argument("--dest", required=True)
    args = parser.parse_args()

    source = Path(args.source)
    dest = Path(args.dest)
    accepted, rejected = [], []
    for package in sorted(p for p in source.iterdir() if p.is_dir()):
        if package_is_releasable(package):
            accepted.append(package.name)
            target = dest / package.name
            target.mkdir(parents=True, exist_ok=True)
            for relative in REQUIRED_FILES:
                src_file = package / relative
                dst_file = target / relative
                dst_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src_file, dst_file)
        else:
            rejected.append(package.name)

    print(f"accepted: {len(accepted)}")
    print(f"rejected: {len(rejected)}")
    for name in rejected:
        print(f"  - {name}: missing or empty required file")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
