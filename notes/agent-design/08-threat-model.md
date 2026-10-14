# Threat Modeling an AI Agent

## Assets
Credentials, investigation data, tool permissions, workflow state, and generated recommendations.

## Threats to consider
- Prompt injection in untrusted logs or documents.
- Excessive tool permissions.
- Sensitive data exposure.
- Incorrect conclusions from incomplete evidence.
- Unsafe retries or unintended side effects.

## Mitigations
Treat retrieved content as data, enforce authorization outside the model, minimize permissions, validate outputs, and keep audit logs.

## Review question
What happens if an input source is malicious or misleading?

## Related TryHackMe room
https://tryhackme.com/room/agentdesign
