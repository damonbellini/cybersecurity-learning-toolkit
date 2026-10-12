# DFIR War Room and Operational Security

A dedicated incident chat supports fast coordination, searchable history and asynchronous questions. It can also become a target if the organisation's accounts or endpoints are compromised.

## Membership

Keep the incident channel small, typically around 5–10 trusted participants who can actively contribute:
- DFIR lead and analysts
- IT or infrastructure specialist
- Security or SOC representative
- CISO or CTO decision maker
- Legal or DevOps contacts when required

Avoid inviting people who do not need access to sensitive incident details.

## Secure communications

- Do not assume corporate Teams, Slack or email is safe during a compromise.
- Prefer an approved end-to-end encrypted channel for incident coordination when corporate identities may be compromised.
- Secure the devices of channel members because an attacker may read messages from an infected endpoint.
- Share only the minimum necessary context with external parties.
- Establish identity verification and a backup contact method.

## Documentation

Record key decisions, timestamps, action owners and approvals in a controlled case log. Avoid placing passwords, recovery keys or unnecessary personal data in the chat.

## Room connection

In the TryHackMe Introduction to Windows IR scenario, the secure chat invitation code is listed as `56-08-32` in a public answer guide. Confirm the code in the live room before relying on it.