# Windows Event IDs for SOC Analysis

Useful Windows events to learn:

## Authentication

- 4624 — Successful logon
- 4625 — Failed logon
- 4648 — Explicit credentials used
- 4672 — Special privileges assigned

## Process and execution

- 4688 — Process creation

## Account activity

- 4720 — User account created
- 4722 — User account enabled
- 4725 — User account disabled
- 4726 — User account deleted
- 4732 — Member added to a local security group

## Security investigation

Event IDs should not be analyzed in isolation. Correlate them with user, host, timestamp, process, network, and authentication context.
