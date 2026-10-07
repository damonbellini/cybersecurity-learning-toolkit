#!/usr/bin/env python3
"""
SHA256 Hash Checker

A small defensive security utility for verifying file integrity.
Use it to calculate a file's SHA256 hash and optionally compare it
with an expected hash.
"""

import argparse
import hashlib
from pathlib import Path


def calculate_sha256(file_path: Path) -> str:
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate and verify a file's SHA256 hash."
    )
    parser.add_argument("file", type=Path, help="Path to the file to check")
    parser.add_argument(
        "--expected",
        help="Expected SHA256 hash to compare against",
    )

    args = parser.parse_args()

    if not args.file.is_file():
        raise SystemExit(f"File not found: {args.file}")

    actual_hash = calculate_sha256(args.file)

    print(f"File:   {args.file}")
    print(f"SHA256: {actual_hash}")

    if args.expected:
        expected = args.expected.strip().lower()

        if actual_hash == expected:
            print("Status: MATCH")
        else:
            print("Status: MISMATCH")
            raise SystemExit(1)


if __name__ == "__main__":
    main()
