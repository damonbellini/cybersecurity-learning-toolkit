# Windows Event Viewer Basics

## What it is
Event Viewer lets an analyst inspect Windows event logs for system, application, security, and service activity.

## Useful log areas
- Windows Logs: Application, Security, Setup, System
- Applications and Services Logs: product-specific operational logs

## Investigation workflow
1. Record the host, time range, user, and reported symptom.
2. Filter by time, source, level, and Event ID.
3. Read the full event details, not just the summary.
4. Correlate related events and confirm timestamps and time zones.
5. Preserve relevant evidence and document conclusions separately from assumptions.

## Important caution
An Event ID is not a verdict by itself. Interpret it with the event source, fields, host role, surrounding activity, and baseline behavior.

## Practice exercise
Open Event Viewer on a lab Windows machine, inspect System events from the last 24 hours, and write down three event sources and what each records.

## Key takeaway
Context and correlation matter more than searching for one supposedly suspicious ID.