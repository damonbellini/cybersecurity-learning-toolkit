# Alert Triage

Alert triage determines whether an alert is benign, suspicious, or malicious and decides what happens next.

## Triage checklist

1. Read the detection name and severity.
2. Identify the affected user, host, IP, and timestamp.
3. Determine what process or activity triggered the alert.
4. Check surrounding events.
5. Look for related authentication, network, and endpoint activity.
6. Enrich indicators with trusted intelligence sources.
7. Decide whether the alert is a false positive or a true positive.
8. Document the reasoning.
9. Escalate when necessary.

## Questions to ask

- What happened?
- When did it happen?
- Which account was involved?
- Which endpoint was involved?
- Was the activity expected?
- What happened immediately before and after?
- Are there related alerts?
- What is the potential impact?

Never close an alert simply because the activity looks unusual. Document the evidence supporting the decision.
