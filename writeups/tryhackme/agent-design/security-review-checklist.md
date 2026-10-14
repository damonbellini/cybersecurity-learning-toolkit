# Security Review Checklist for an Agent

## Before deployment
- [ ] Purpose and scope are documented.
- [ ] Tool permissions follow least privilege.
- [ ] Untrusted content is treated as data, not trusted instructions.
- [ ] Sensitive data access is minimized.
- [ ] Outputs are validated against a schema.
- [ ] Evidence and limitations are included in findings.
- [ ] Retry and timeout limits are enforced.
- [ ] Consequential actions require authorization.
- [ ] Human escalation paths are tested.
- [ ] Logs support auditing without exposing unnecessary secrets.

## Related room
https://tryhackme.com/room/agentdesign

## Ethical use
Use these concepts only in authorized labs and systems.