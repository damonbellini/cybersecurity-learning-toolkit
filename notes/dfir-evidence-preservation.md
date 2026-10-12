# DFIR Evidence Preservation Checklist

## First principles

- Preserve the original evidence and analyse working copies.
- Record who collected the item, when, from where and by what method.
- Compute a cryptographic hash such as SHA-256 when acquiring and transferring files.
- Maintain an access and transfer log.
- Document any changes or transformations made during analysis.

## Before taking action

Coordinate with the incident lead before deleting files, wiping systems, reinstalling operating systems, clearing logs or running remediation tools. These actions may destroy evidence or alter timestamps.

## Acquisition notes

For each artifact, record:
- Case identifier and artifact identifier
- Hostname and source path
- Collection date and time with time zone
- Collector and tool/version
- Original filename and size
- SHA-256 hash
- Storage location and access restrictions
- Any known limitations

## Integrity verification

Recompute the hash after transfer and compare it with the acquisition hash. A mismatch should be investigated and documented rather than ignored.

## Reporting

Distinguish direct observations from hypotheses. Include commands, filters, time windows and relevant event IDs so another analyst can reproduce the result.