# Incident Triage Timeline and Evidence Notes

Use this template during an authorised lab or an incident where you have permission to review the relevant records. Its purpose is to keep observations, interpretations and decisions separate so another analyst can reproduce the reasoning.

## 1. Case header

- Case or exercise ID:
- Analyst:
- Date opened:
- Time zone used in notes:
- Systems and log sources in scope:
- Authorisation or ticket reference:
- Initial question to answer:

Do not include passwords, session tokens, private keys or unnecessary personal information in the case notes.

## 2. Timeline

Record events in a consistent time zone, ideally preserving the original timestamp as well when converting it. A collection timestamp is not necessarily the same as the time the event occurred.

| Event time | Collection time | Source | Host or account | Observation | Evidence reference | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD HH:MM:SS TZ | YYYY-MM-DD HH:MM:SS TZ | Example log | Example host | Describe the recorded fact | File or event ID | High / medium / low |

Guidelines:

- Use one row per relevant observation.
- Preserve the original event time and time zone.
- Label estimated or converted times.
- Link to the source record rather than paraphrasing away important fields.
- Mark missing, delayed or duplicate telemetry.
- Avoid describing an event as malicious unless the evidence supports that assessment.

## 3. Evidence register

| Evidence ID | Source and location | Acquired by | Acquisition time | Integrity check | Notes |
| --- | --- | --- | --- | --- | --- |
| E-001 | Example exported log | Analyst name | Timestamp and zone | Hash recorded / not applicable | Synthetic training record |

For a file that needs integrity verification, calculate a cryptographic hash using an approved tool and record the algorithm and result. A matching hash can help show that two copies are identical; it does not prove that the original file was truthful or complete.

Never alter the only copy of original evidence. Follow the applicable retention and chain-of-custody procedure. For a learning exercise, use fabricated records rather than publishing logs from a real organisation.

## 4. Findings: separate the three categories

### Observed facts

Write only what the source directly shows. Include event IDs, timestamps, account names or other fields only when necessary and authorised.

### Interpretation

Explain what the facts may indicate and why. State confidence and consider alternative explanations such as expected administration, user error, software retries or clock differences.

### Unknowns

List the information needed to test the interpretation. Examples include missing endpoint telemetry, unavailable authentication fields, uncertain time zones or a change that has not been checked against an approved record.

## 5. Hypothesis testing

For each hypothesis, record:

- Hypothesis:
- Evidence that supports it:
- Evidence that contradicts it:
- Benign alternatives:
- Additional data needed:
- Current assessment:
- Confidence and reason:
- Next action and owner:

Do not treat the absence of a log record as proof that an event did not occur. First check whether the source was configured to generate it, whether collection was healthy and whether retention covers the time period.

## 6. Decision log

| Time | Decision | Evidence considered | Reason | Owner or approver |
| --- | --- | --- | --- | --- |
| Timestamp and zone | Example: collect additional endpoint logs | Evidence IDs | Why this is the next proportionate step | Role or name |

Record significant changes in assessment and why the assessment changed. If the case is escalated, provide enough context for the next analyst to continue without repeating every collection step.

## 7. Handover summary

- **Question investigated:**
- **Scope and time range:**
- **Most important observations:**
- **Current assessment:**
- **Confidence and limitations:**
- **Actions already taken:**
- **Outstanding questions:**
- **Recommended next steps:**
- **Evidence references:**

## Practice exercise

Use a fictional scenario in which several failed logons are followed by one successful logon. A separate endpoint record shows a process starting a few minutes later.

1. Build a timeline without claiming that the account was compromised.
2. Separate direct observations from your interpretation.
3. List at least three benign explanations that should be checked.
4. Identify two additional records that could help test your hypothesis.
5. Write a two-sentence handover that clearly states what is known and what remains uncertain.

A strong triage note is concise, reproducible and honest about uncertainty. The goal is not to sound certain; it is to make the next investigative decision defensible.
