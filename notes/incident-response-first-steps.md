# Incident Response: First Steps

## Purpose

Incident response is a structured process for identifying, containing and recovering from security events while preserving evidence and limiting harm.

## Core phases

1. **Preparation:** define roles, escalation paths, logging and response procedures.
2. **Detection and analysis:** validate alerts and determine likely scope.
3. **Containment:** prevent further impact while preserving essential evidence.
4. **Eradication:** remove the cause, such as malicious persistence or exploited weaknesses.
5. **Recovery:** restore services safely and monitor for recurrence.
6. **Lessons learned:** document root causes and improve controls.

## Initial triage checklist

- Record the alert source and timestamp, including timezone.
- Identify affected systems, accounts and business services.
- Preserve relevant logs and evidence.
- Determine whether the event is ongoing.
- Escalate according to the organisation's incident plan.
- Avoid destructive actions before evidence and business impact are understood.

## Evidence handling

Record who collected each item, when it was collected and how it was stored. Preserve original files where possible and use verified copies for analysis. Follow the organisation's retention and privacy requirements.

## Example investigation commands

```bash
date -u
whoami
hostname
ps aux
ss -tulpn
```

These provide basic system context. Run them only where you have appropriate access. Their output alone does not establish that a compromise occurred.

## Communication

Use a clear timeline and separate confirmed facts from hypotheses. Share sensitive details only with authorised responders. Do not publish indicators or personal data if doing so could increase risk.

## After-action review

Ask what happened, how it was detected, what limited or increased the impact, which controls failed, and which measurable improvements should be prioritised.
