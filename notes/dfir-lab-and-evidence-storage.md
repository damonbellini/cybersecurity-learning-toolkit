# DFIR Lab and Evidence Storage

A forensic lab separates investigation activity from the compromised environment and provides a controlled place to inspect artifacts.

## Minimum lab

- Dedicated Windows analysis machine or equivalent trusted environment
- Approved forensic utilities and documented versions
- Restricted access and strong authentication
- Isolated or controlled connectivity to the customer network
- Sufficient CPU, memory and disk for the expected artifacts
- A process for safely handling potentially malicious files

## Evidence storage requirements

Evidence storage should be:
- Private, with access limited to authorised investigators
- Fast enough for large artifact transfers
- Auditable, including upload, modification and deletion events
- Able to store suspicious or malicious files without silently deleting them
- Protected by encryption, retention controls and backups where appropriate

Cloud storage may be convenient, but review provider scanning, retention and access behavior before uploading sensitive or malicious evidence.

## Chain of custody

For each item, record case ID, source system, collector, acquisition time, hash, transfer history and analysis actions. Hash evidence before and after transfer to check integrity.

## Room-specific notes

The TryHackMe room uses a DefenseBox analysis environment. The public answer guide lists the flag `THM{happy_investigation!}` at the bottom of its Usage Instructions page and identifies DumpIt as the first tool in the Artifact Collection folder. Confirm these details inside the active lab.