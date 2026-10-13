# Authentication Log Analyzer: Design and Investigation Workflow

This guide defines the first safe, testable version of the Log Analyzer learning project. It is intended for synthetic datasets and logs that you are authorised to examine. The project performs offline analysis only.

## What the project should answer

A junior analyst should be able to answer five questions from a small authentication dataset:

1. How many valid events were processed?
2. How many authentications failed or succeeded?
3. Which source addresses generated the most failures?
4. Which usernames were targeted most often?
5. Which source addresses crossed a configurable review threshold?

A high count is a lead for investigation, not proof of malicious activity or account compromise.

## Input format

Use one JSON object per line, commonly called JSON Lines or JSONL. Keep each record small and use consistent field names.

| Field | Required | Meaning | Example |
| --- | --- | --- | --- |
| timestamp | Yes | Event time in ISO 8601 with a timezone | 2026-10-13T08:30:00Z |
| source_ip | Yes | Address recorded by the authentication system | 192.0.2.10 |
| username | Yes | Account name associated with the attempt | training-user |
| event_type | Yes | Event category | authentication |
| outcome | Yes | Normalised result | failed or success |

Addresses in examples should use documentation ranges such as 192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24. These are reserved for examples and avoid publishing real client data.

Example records:

```json
{"timestamp":"2026-10-13T08:30:00Z","source_ip":"192.0.2.10","username":"training-user","event_type":"authentication","outcome":"failed"}
{"timestamp":"2026-10-13T08:31:00Z","source_ip":"192.0.2.10","username":"training-user","event_type":"authentication","outcome":"failed"}
{"timestamp":"2026-10-13T08:32:00Z","source_ip":"192.0.2.10","username":"training-user","event_type":"authentication","outcome":"success"}
```

These are fabricated training records, not evidence from a real environment.

## Processing workflow

### 1. Read safely

Read the file as UTF-8 and process it line by line. Ignore blank lines. Do not silently discard malformed records: retain the line number and a concise reason so that the analyst can assess data quality.

### 2. Validate before counting

Reject a record when it is not a JSON object, lacks a required field, has an invalid IP address, has a timestamp without a timezone, or uses an unsupported outcome. Do not guess what malformed values mean.

### 3. Normalise carefully

Normalise outcome values to lowercase and trim whitespace from usernames. Parse IP addresses with a standard library rather than a hand-written regular expression. Preserve the timestamp's timezone information. If multiple log sources are combined, document how each source represents time before comparing events.

### 4. Summarise

Calculate totals for valid events, failed attempts, successful attempts, distinct source addresses and distinct usernames. Group failed events by source address and by username. Sort results deterministically so repeated runs over the same file produce the same report.

### 5. Apply a review threshold

A configurable threshold can list sources with several failures in the input file. In this first version, the threshold applies to the whole file, not a rolling time window. A production detection should define a time window, entity scope, exclusions, data source and response procedure.

### 6. Interpret in context

Before escalating a source, check whether it belongs to a known scanner, VPN, shared NAT, monitoring service or approved test. Compare the timestamps with successful logins, identity-provider events, endpoint activity and relevant network logs. A shared source IP can represent many users, and one user can appear behind different addresses.

## Example analyst notes

Use a short evidence table during a lab:

| Observation | Evidence | Possible explanation | Next validation |
| --- | --- | --- | --- |
| One source has repeated failures | Count and time range in the report | Typing errors, a scheduled integration, or password guessing | Review account pattern and adjacent events |
| A failure is followed by success | Same account and source, ordered timestamps | Legitimate retry or suspicious authentication sequence | Confirm identity, device and MFA context |
| Many usernames have failures from one source | Grouped event counts | Shared service, misconfiguration, or broad guessing | Check allow-listed services and time distribution |

Record what is known separately from what is inferred. Use language such as “consistent with” or “requires validation” until corroborating evidence exists.

## Test plan

A useful first version should cover the following cases:

- A valid failed event is counted as a failure.
- A valid successful event is counted as a success.
- An invalid JSON line is reported with its line number and does not crash the full run.
- A missing required field is rejected.
- An invalid IP address is rejected.
- A timestamp without timezone information is rejected.
- A threshold of one is accepted, while zero and negative values are rejected.
- Equal counts are sorted consistently.
- An empty file produces a valid zero-event summary.
- A file containing only invalid records clearly reports that no valid events were analysed.

Keep test data synthetic and small. Do not commit production authentication logs, real usernames, customer IP addresses, tokens, session identifiers or other personal or secret information.

## Suggested command-line interface

The project can expose a local command with this shape:

```text
python log_analyzer.py sample-auth-events.jsonl --threshold 3
python log_analyzer.py sample-auth-events.jsonl --threshold 3 --json
```

The first form should produce a readable report. The second should produce machine-readable JSON suitable for later automation. The tool should never transmit data or modify the source file.

## Learning exercises

1. Add three synthetic failures from a second documentation-range IP. Predict how the summary should change before running the tool.
2. Add one successful login and explain why it does not erase earlier failed attempts.
3. Add a malformed line. Confirm that valid records are still analysed and the error is reported.
4. Change the threshold from three to five. Explain why the list of review candidates changes.
5. Sort the same input in a different order. Decide which report values should remain identical.
6. Explain why a source that crosses a threshold is not automatically an attacker.
7. Describe how you would extend the project to use a time window without treating events from different timezones incorrectly.

## Definition of done

- Input is read-only and local.
- Required fields are validated before analysis.
- Bad records are reported, not hidden.
- Results are repeatable and understandable.
- Tests cover valid, invalid and empty input.
- Documentation explains the threshold's limitations.
- The report distinguishes observations from conclusions.
