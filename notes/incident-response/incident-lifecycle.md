# Incident Response Lifecycle

## NIST SP 800-61 Rev. 2 phases
1. **Preparation**: define roles, escalation paths, tools, playbooks, backups, and communication channels.
2. **Detection and Analysis**: validate alerts, determine scope and severity, build a timeline, and identify affected assets.
3. **Containment, Eradication, and Recovery**: limit damage, remove the cause, restore services, and verify systems are safe.
4. **Post-Incident Activity**: document what happened, preserve lessons learned, and improve controls.

An **event** is an observable occurrence. An **alert** signals activity that may need investigation. An **incident** meets the organization's criteria for coordinated response.

## Practical checklist
- Record alert source and timestamp, including timezone.
- Identify affected accounts, endpoints, servers, and services.
- Preserve relevant logs before they rotate or are overwritten.
- Track response actions and who authorized them.
- Define conditions for containment and safe restoration.

## Study questions
- Which phase includes lessons learned? **Post-Incident Activity**.
- Is every alert a confirmed incident? **No. Validate and scope it first.**
- Why document actions? **Accountability, reproducibility, and an accurate timeline.**

Reference: NIST SP 800-61 Rev. 2, https://csrc.nist.gov/pubs/sp/800/61/r2/final
