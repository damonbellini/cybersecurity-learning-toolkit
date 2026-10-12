# Windows IR First Response Quick Reference

## Priorities

1. Protect people and business-critical services.
2. Establish an incident lead and trusted communications.
3. Define scope and preserve evidence.
4. Contain the threat in coordination with system owners.
5. Acquire relevant logs and forensic artifacts.
6. Build a timeline and test hypotheses.
7. Recover carefully and verify that the threat is no longer present.

## Ask immediately

- What was observed and at what time?
- Which systems and accounts are involved?
- What containment steps have already been taken?
- Which logs and forensic artifacts are available?
- What EDR/SIEM coverage exists, and has it been validated?
- Who has authority to approve disruptive actions?

## Avoid

- Deleting suspicious files before evidence is preserved.
- Reimaging hosts before acquisition decisions are made.
- Assuming a product is protecting a host just because it is licensed.
- Using a potentially compromised corporate channel for sensitive coordination.
- Making attribution claims from a single indicator.

## Useful artifacts

- Windows Event Logs
- EDR telemetry
- Authentication and directory logs
- DNS, firewall, VPN and proxy logs
- Process, service, scheduled task and registry data
- Memory and disk images when justified

## Reference

TryHackMe Introduction to Windows IR: https://tryhackme.com/room/introtowindowsir