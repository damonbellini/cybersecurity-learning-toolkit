# TryHackMe: Introduction to Windows IR

Room: https://tryhackme.com/room/introtowindowsir

## Room answers

These answers were cross-checked against a publicly available room answer guide and the published TryHackMe room material. Dynamic lab answers should still be confirmed in the active room because the platform may change the environment.

### Task 3: Meet OpenDoor LTD

| Question | Answer |
|---|---|
| Where is the affected data center located? | London |
| Whom does OpenDoor suspect of starting the attack? | Ruby Evans |
| Indicator of compromise and host | hello.exe, DC-04 |
| What EDR is deployed across OpenDoor's network? | BitDefender |

### Task 4: Organize DFIR Chat

| Question | Answer |
|---|---|
| What EDR is really in use by OpenDoor? | TrendMicro |
| How many hosts are actually protected with EDR? | 15 |
| Secure chat invitation code | 56-08-32 |

### Task 5: Prepare DFIR Lab

| Question | Answer |
|---|---|
| What tool was recommended for analyzing large amounts of logs? | SIEM |
| Flag at the bottom of the DefenseBox Usage Instructions page | THM{happy_investigation!} |
| First tool in DFIR Tools → Artifact Collection | DumpIt |

### Task 6: What's Next

Select the option to complete the room and continue to the next room in the module.

## Important verification note

The answers above match a public answer guide published in September 2026 and the visible room description. I did not operate the authenticated TryHackMe AI agent or launch the user's DefenseBox instance, so the invitation code and lab flag are cross-checked against that guide, not independently submitted to the platform in this session.

## Core lessons

- Establish a small, trusted incident response team.
- Ask the customer clear questions and validate their claims against logs and artifacts.
- Do not assume the EDR product named by an organisation is the product actually deployed or healthy.
- Keep incident coordination in a trusted, end-to-end encrypted channel when corporate accounts or devices may be compromised.
- Prepare a dedicated forensic workstation and evidence storage with privacy, performance, audit logs and safe malware handling.
- Preserve evidence and record every acquisition and analysis step.

References:
- TryHackMe room: https://tryhackme.com/room/introtowindowsir
- Public answer cross-check: https://simontaplin.net/2026/09/08/answers-for-the-tryhackme-introduction-to-windows-ir-room/