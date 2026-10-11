# Lab: Investigate a Burst of Failed Logons

## Purpose

Practise turning a small set of authentication events into a defensible triage decision. This lab uses invented data and reserved documentation IP addresses. It does not contact or test any real system.

## Learning objectives

By the end, you should be able to:

- distinguish an individual failed logon from a pattern worth investigating;
- group events by source, account and time;
- explain why a threshold is a signal rather than proof of malicious activity;
- record evidence, uncertainty and next steps in a concise analyst note.

## Scenario

A monitoring rule reports several failed logons from one source. The table below is synthetic. All timestamps are UTC.

| Timestamp | Source IP | Username | Event | Outcome |
| --- | --- | --- | --- | --- |
| 09:00:10 | 192.0.2.25 | alex | authentication | failure |
| 09:01:04 | 192.0.2.25 | alex | authentication | failure |
| 09:02:12 | 192.0.2.25 | alex | authentication | failure |
| 09:03:01 | 192.0.2.25 | alex | authentication | failure |
| 09:04:43 | 192.0.2.25 | alex | authentication | failure |
| 09:05:20 | 192.0.2.25 | alex | authentication | success |
| 09:06:11 | 198.51.100.17 | maria | authentication | failure |
| 09:20:00 | 198.51.100.17 | maria | authentication | failure |

The addresses are from RFC 5737 documentation ranges and are not indicators to block.

## Investigation workflow

### 1. Validate the alert

Confirm the detection logic, threshold, time zone and log source. Check whether the event records are complete and whether duplicate ingestion could inflate the count.

### 2. Establish the pattern

For each source, count failed authentication events inside the configured time window. Record the first and last event timestamps, affected accounts and whether a successful logon followed the failures.

Do not count successful logons as failures. Do not combine events from unrelated sources without a clear reason.

### 3. Add context

In an authorised lab or approved investigation, pivot to:

- the destination host and authentication service;
- the account's normal sign-in pattern and expected source locations;
- successful logons immediately after the failures;
- VPN, firewall and endpoint events around the same timestamps;
- maintenance, password changes, service accounts or other benign explanations.

Use only logs you are authorised to access. Avoid copying passwords, tokens or unnecessary personal information into notes.

### 4. Decide and document

Possible outcomes include:

- **Benign / expected:** evidence supports a known user mistake or approved test.
- **Suspicious, needs more context:** the pattern is unusual but evidence is incomplete.
- **Likely malicious:** multiple independent signals support attempted account compromise.
- **Inconclusive:** the available telemetry is insufficient.

A burst of failures alone does not prove password spraying, brute force or account compromise. A success after failures increases investigative priority but still needs context.

## Analyst note template

Copy and complete this template for the scenario.

- **Alert name:**
- **Time range (UTC):**
- **Source and destination:**
- **Accounts involved:**
- **Observed evidence:**
- **Related events checked:**
- **Benign explanations considered:**
- **Assessment and confidence:**
- **Potential impact:**
- **Recommended next action:**
- **Evidence still needed:**

Keep facts separate from assumptions. Include exact timestamps and the query or filter used so another analyst can reproduce the result.

## Exercises

1. How many failed events came from 192.0.2.25 between 09:00 and 09:10 UTC?
2. Why should the successful event at 09:05:20 remain part of the timeline even though it is not counted as a failure?
3. Does the data prove an account was compromised? Explain what is missing.
4. Name two benign explanations and two additional data sources that could help test them.
5. What could make a threshold-based alert noisy?
6. Write a two-sentence escalation summary that states the evidence and uncertainty without claiming more than the data supports.

## Suggested reasoning

The first source has five failures in a short interval and then a success, so it deserves contextual review. The second source has two failures separated by nearly twenty minutes and does not meet a five-failures-in-ten-minutes rule. Neither observation, by itself, establishes malicious intent.

## Completion checklist

- [ ] I can explain the alert in plain language.
- [ ] I can reproduce the count from the timestamps.
- [ ] I separated observations from assumptions.
- [ ] I listed evidence that would confirm or weaken my hypothesis.
- [ ] I wrote a conclusion with an appropriate confidence level.
