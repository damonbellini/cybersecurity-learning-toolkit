# EDR Alert Triage Checklist

## Validate the alert

- Record alert ID, severity, detection time and affected asset.
- Identify the detection logic and its limitations.
- Capture process path, command line, parent process and user.
- Review file hash, signature and prevalence.
- Inspect network connections and related DNS activity.
- Search for related alerts across other hosts and accounts.

## Scope and impact

- Determine whether the host is critical or exposed.
- Check for privileged account use.
- Identify related processes, persistence and lateral movement indicators.
- Establish whether the alert is isolated or part of a broader sequence.

## Decide and document

Classify the alert as malicious, benign, or unresolved with evidence. Follow the incident response playbook for containment decisions. Do not isolate a critical host or terminate a process without considering business impact and the authorised response procedure.

## Preserve

Export the alert details and relevant telemetry, note the query and time window, and record any response actions with timestamps and owners.