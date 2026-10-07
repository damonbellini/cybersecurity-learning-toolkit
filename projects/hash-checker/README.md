# SHA256 Hash Checker

A small defensive security utility for verifying file integrity.

## What it does

The tool calculates a SHA256 digest for a file and can compare it with an expected digest.

## Usage

```bash
python3 hash_checker.py sample.txt
python3 hash_checker.py sample.txt --expected <sha256>
```

A matching digest produces `Status: MATCH`. A different digest produces `Status: MISMATCH`.

## Security concept

Cryptographic hashes provide a compact representation of file contents. If the contents change, the resulting SHA256 digest should change as well.

Use this tool only on files and systems you are authorised to inspect.
