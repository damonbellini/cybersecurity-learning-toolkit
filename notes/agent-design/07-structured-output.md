# Structured Output Design

## Why structure matters
A stable schema makes agent results easier to validate, compare, automate, and audit.

## Example JSON shape
```json
{
  "finding": "string",
  "priority": "low | medium | high | undetermined",
  "evidence": [],
  "limitations": [],
  "requires_human_review": true
}
```

## Validation checklist
- Required fields are present.
- Enum values are valid.
- Evidence is traceable.
- Unknown values are explicit.
- Output is rejected or repaired safely when invalid.

## Related TryHackMe room
https://tryhackme.com/room/agentdesign
