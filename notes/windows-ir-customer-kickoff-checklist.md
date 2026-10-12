# Windows Incident Response: Customer Kickoff Checklist

Based on the preparation concepts in TryHackMe Introduction to Windows IR.

## Before the call

- Identify the incident lead and decision maker.
- Assemble a small dedicated DFIR team with clear roles.
- Confirm a trusted contact method.
- Ask the customer to include a technical employee who understands the incident.
- Invite a suitable executive sponsor such as the CISO or CTO.

## Questions to ask

### Incident details
- What happened and when?
- Who detected it and how?
- Which systems, sites and business units are affected?
- What response actions have already been taken?
- What indicators, suspicious files, IP addresses or accounts have been identified?
- What is the current containment status?

### Environment profile
- What does the network architecture look like?
- Which remote access entry points exist?
- Which services are exposed to the internet?
- Which SIEM, EDR and IDS products are configured?
- Who can provide technical access and operational context?
- What outcomes does the customer expect from the investigation?

## Validate claims

Do not accept statements such as “MFA is enabled” or “RDP is disabled” without clarifying scope and verifying logs or configuration. Restate the claim, ask the customer to confirm your interpretation, then corroborate it with evidence.

## Preserve evidence

Tell responders not to delete suspicious files, reinstall systems, clear logs or run cleanup tools before discussing the forensic impact. Record every action already performed.

## Outcome

Document scope, contacts, communication channel, evidence sources, access needs, decision authority and the next update time.