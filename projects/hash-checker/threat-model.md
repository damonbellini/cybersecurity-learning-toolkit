# Hash Checker Threat Model

## Purpose

The tool helps identify unexpected changes to files by comparing cryptographic hashes.

## Trust assumptions

The expected hash must come from a trusted source.

## Limitations

A hash comparison does not prove that a file is safe.

If an attacker can modify both the file and the stored expected hash, the comparison can be defeated.

## Defensive use

Store trusted reference hashes separately and protect the process that generates and verifies them.
