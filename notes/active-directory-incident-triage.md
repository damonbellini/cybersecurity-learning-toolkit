# Active Directory Incident Triage

Active Directory incidents can affect many systems because domain identities and policies control access across an organisation.

## Initial questions

- Which accounts and computers are suspected to be affected?
- Are privileged accounts involved?
- Were unexpected users, groups or delegated permissions created?
- Are there unusual authentication patterns or logon sources?
- Have Group Policy objects or domain configuration changed?
- Are domain controllers healthy and appropriately monitored?

## Evidence sources

- Security event logs on domain controllers
- Identity provider and authentication telemetry
- EDR process and network data
- Group membership and directory change records
- VPN, firewall and remote access logs
- Relevant Group Policy and configuration history

## Response principles

Preserve relevant logs, identify the scope, and coordinate containment with identity and infrastructure owners. Avoid indiscriminate account disabling or domain-wide changes without understanding operational impact and having an approved response plan.

Use least privilege and corroborate each finding with more than one evidence source when possible.