# Phishing Triage Checklist

## Initial assessment
- Record report time, reporter, recipient, and delivery channel.
- Preserve the original message in the approved evidence system.
- Review sender and reply-to addresses, headers, and authentication results.
- Inspect links using approved analysis tools rather than opening them on a normal workstation.
- Treat unexpected attachments and credential prompts as suspicious until validated.

## Scope and impact
- Search mail telemetry for the same sender, subject, URL, attachment hash, or campaign identifier.
- Determine whether the message was delivered, opened, clicked, or replied to.
- Check identity logs for unusual sign-ins after interaction.
- If credentials may be exposed, follow the identity team's process for session revocation and credential reset.
- Escalate suspected malware execution or account compromise.

## Useful indicators
- Lookalike domains and mismatched display names.
- Urgent requests for payment, secrets, or account verification.
- Unexpected file types or unfamiliar login pages.
- Failed SPF, DKIM, or DMARC results. These are signals, not proof by themselves.

Document message identifiers, timestamps, affected users, indicators, queries, decisions, and containment actions. Avoid casually forwarding suspicious messages.

## Study questions
- Does a failed SPF check alone prove a message is malicious? **No.**
- What helps scope a campaign? **Searching shared senders, URLs, hashes, and message identifiers.**
- Why preserve the original? **To retain headers and evidence for analysis.**
