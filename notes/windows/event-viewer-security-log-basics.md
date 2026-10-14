# Windows Security Log Triage: Beginner Field Guide

This guide is for learning on a Windows machine or lab where you are authorised to inspect logs. Event identifiers and available fields depend on Windows version, audit policy, log source and configuration. Treat an event as evidence to investigate, not a verdict by itself.

## Learning objectives

After working through this guide, you should be able to open Event Viewer, filter a time range, recognise several common Security log event IDs, preserve useful context and write a short evidence-based triage note.

## Where to look

1. Open **Event Viewer** from the Start menu or run `eventvwr.msc`.
2. Expand **Windows Logs**.
3. Select **Security** for authentication and audit events, if your account has permission to read it.
4. Use **Filter Current Log** to narrow the view by time range, event ID, level or other available criteria.
5. Open an event and inspect both the **General** and **Details** views.
6. Record the computer, event time, event ID, account fields, source information and logon type when present.

A missing event does not necessarily mean that the activity did not happen. The relevant audit policy might not be enabled, the event may be stored in another log, retention may have removed it, or your account may not have permission to read it.

## Common event IDs

| Event ID | Common meaning | Questions to ask |
| --- | --- | --- |
| 4624 | A logon was successful | Which account, logon type, host and source context are recorded? |
| 4625 | A logon attempt failed | Is the failure repeated? Is the account or source expected? |
| 4634 | A logon session ended | Does it match the session being investigated? |
| 4648 | A logon was attempted using explicit credentials | Is there an expected administrative or application reason? |
| 4688 | A new process was created, when the relevant auditing is enabled | What process and parent process are recorded? Is command-line capture configured? |
| 4720 | A user account was created | Was the change approved? Who performed it and when? |
| 4728 | A member was added to a security-enabled global group | Which group was changed, and was the membership approved? |

The meaning of an event ID is only the starting point. Review the event's fields and surrounding activity. Some fields may be empty or unavailable depending on the event and configuration.

## A repeatable triage workflow

### 1. Define the question

Write down the host, time range and activity you are investigating. Use a consistent time zone. If an alert gives UTC but the workstation displays local time, document the conversion rather than comparing the displayed clock values blindly.

### 2. Confirm the log source

Make sure you are looking at the right computer and log. Record any collection or retention limitations. Do not assume every Windows device has identical audit settings.

### 3. Filter before interpreting

Start with the smallest useful time range and relevant event IDs. Expand the window when you need context before or after the event. Avoid drawing conclusions from one isolated row.

### 4. Correlate related evidence

Where authorised logs are available, compare nearby events for the same account, device or session. Useful context may include successful and failed logons, account changes, process creation, VPN activity and approved maintenance. Correlation is stronger when independent records agree, but timestamps and identities must be checked carefully.

### 5. Separate facts from hypotheses

Use three headings in your notes:

- **Observed:** values directly present in the records.
- **Interpretation:** what those values may indicate.
- **Unknown:** information still needed to confirm or rule out the hypothesis.

For example, repeated failures followed by a success justify checking the account, source and session context. They do not by themselves prove that an account was compromised.

## Optional PowerShell query

On a system you are authorised to inspect, this command retrieves recent failed logon events from the local Security log. Access may require elevated permissions, and results depend on audit configuration.

```powershell
$start = (Get-Date).AddHours(-24)

Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4625
    StartTime = $start
} -ErrorAction SilentlyContinue |
    Select-Object TimeCreated, Id, ProviderName, Message |
    Format-List
```

This is a local read-only query. It does not change policy, delete events or contact another computer. For repeatable investigations, export or record relevant event fields in accordance with the organisation's evidence-handling rules. Be careful not to paste secrets or unnecessary personal data into public notes.

## Synthetic exercise

Assume a lab timeline contains these fictional observations:

- 10:02: a failed logon for account `training-user`
- 10:03: another failed logon for the same account
- 10:04: a successful logon for the same account
- 10:06: a process creation event on the same host

All times are from the same documented time zone. No other context is provided.

Answer in your own words:

1. Which observations are facts, and which are hypotheses?
2. What fields from the failed and successful logon events would you compare?
3. What context would help determine whether the success was expected?
4. What information would you inspect in the process creation event?
5. What would you write as the next investigative step without claiming a compromise prematurely?

### Example note structure

- **Question:**
- **Host and time range:**
- **Events reviewed:**
- **Observed facts:**
- **Interpretation and confidence:**
- **Benign explanations considered:**
- **Evidence still needed:**
- **Recommended next step:**

## Knowledge check

Try answering without looking back:

1. Why can a 4625 event not prove a brute-force attack by itself?
2. Why does audit policy matter when investigating missing events?
3. What is the difference between an event's timestamp and the time you collected it?
4. Why should a triage note distinguish observed facts from interpretation?
5. What additional context could make a successful logon after several failures less suspicious?

## Safety and evidence handling

Use only systems and logs you are authorised to access. Preserve original evidence according to your lab or organisation's procedure. Do not disable auditing, clear logs or change security settings as part of this exercise. Use synthetic data in public writeups and remove usernames, addresses, tokens and other sensitive information from real records before sharing.
