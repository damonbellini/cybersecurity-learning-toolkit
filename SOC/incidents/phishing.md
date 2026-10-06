# Phishing Investigation

## Initial questions

- Who received the message?
- Who sent it?
- What domain was used?
- Was the sender spoofed?
- Was a link clicked?
- Was an attachment opened?
- Were credentials entered?
- Did the endpoint generate suspicious activity afterward?

## Investigation evidence

Collect:

- Email headers
- Sender and recipient information
- URLs
- Domains
- Attachment hashes
- Authentication events
- Endpoint telemetry

## Response

Depending on the findings:

- Remove malicious messages
- Reset compromised credentials
- Revoke active sessions
- Block malicious indicators
- Investigate affected endpoints
- Document the incident

Perform testing only with authorized mailboxes and infrastructure.
