# Windows Incident Response Roles and Workstreams

A clear division of responsibility reduces delays and conflicting actions during an incident.

## Core roles

- Incident lead: owns scope, priorities, coordination and decision log.
- DFIR lead: directs acquisition, analysis and technical findings.
- Endpoint analyst: investigates hosts, processes, persistence and endpoint telemetry.
- Network analyst: reviews DNS, proxy, firewall and packet evidence.
- Identity specialist: investigates accounts, authentication and Active Directory.
- Customer liaison: coordinates access, updates and business impact.
- Legal or privacy contact: advises on regulatory and evidence-handling obligations where applicable.

One person may fill multiple roles in a small team, but responsibilities should remain explicit.

## Workstreams

1. Scope and containment
2. Evidence acquisition and preservation
3. Endpoint and memory analysis
4. Identity and Active Directory analysis
5. Network and exfiltration analysis
6. Timeline and hypothesis development
7. Recovery validation and lessons learned

## Communication cadence

Agree on a regular status update time, urgent escalation route and decision owner. Keep technical evidence separate from executive summaries while maintaining traceability between them.

## Room connection

The OpenDoor scenario emphasizes assembling a small dedicated team rather than a large group of analysts who are only intermittently available.