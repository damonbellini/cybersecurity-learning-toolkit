# TryHackMe: Threat Hunting Introduction

Room: https://tryhackme.com/room/threathuntingintroduction  
Topics: proactive threat hunting, threat intelligence, IOCs, attack residues, APT investigation  
Status: Answers transcribed from the prior walkthrough; verify exact wording and current challenge state.

## Task 2: Introduction

1. Average days an attacker remains undetected: `Dwell time`
2. Is threat hunting reactive or proactive?: `Proactive`

## Task 3: Hunting Approaches

1. Approach when threat intelligence identifies an APT targeting your industry: `Intelligence-Driven Hunting`
2. Approach for a list of file hashes and IOCs: `Indicator-Driven Hunting`

## Task 4: Hunting Targets

1. Category representing artifacts left by attackers: `Attack Residues`

## Task 5: Hunting Techniques

1. Technique using hashes, IP addresses, and domain names: `Indicators of Compromise`
2. Word.exe spawning cmd.exe, then powershell.exe connecting externally: `Behavioral Pattern Analysis`

## Task 6: APT-Serpent Scenario

1. Known campaigns since 2021: `4`
2. Phase where CustomBackdoor is dropped: `Execution & Persistence`
3. Primary initial access vector: `Spear-phishing`
4. CustomBackdoor HTTPS C2 beacon interval, in seconds: `300`
5. Flag: `THM-APT-SERPENT-INTEL`

## Notes

Task 1 and Task 7 did not require a separate answer in the previous notes. The answers above are walkthrough-derived; validate against the current room.

## References

- Official room: https://tryhackme.com/room/threathuntingintroduction
- Walkthrough: https://github.com/9gkc/tryhackme/blob/002009f2d07f55f0ae7e33bfb80c87ec1a2c2d50/rooms/10-threat-hunting-introduction/README.md
