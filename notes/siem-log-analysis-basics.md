# SIEM and Large-Scale Log Analysis

A Security Information and Event Management platform centralises logs and supports searching, correlation, alerting and investigations across many systems.

## Why use a SIEM?

- Search large volumes of event records.
- Correlate events from endpoints, identity systems, firewalls and cloud services.
- Build timelines across multiple hosts.
- Identify patterns that are difficult to see in one log source.
- Preserve investigation queries and support repeatable reporting.

## Investigation workflow

1. Define a time window and incident scope.
2. Identify likely data sources.
3. Search for known indicators and suspicious identities.
4. Pivot from an event to related hosts, users, IPs and processes.
5. Normalize timestamps and account for time zones.
6. Save query details and export relevant evidence.
7. Corroborate findings with endpoint and network artifacts.

## Common pitfalls

- Different systems may use different time zones.
- Missing logs do not prove an event did not happen.
- A single alert or indicator is not enough to establish attribution.
- Validate field meanings and ingestion delays before drawing conclusions.

## TryHackMe answer

For the question asking what tool is recommended for analyzing large amounts of logs, the listed answer is `SIEM`.