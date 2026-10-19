# Log Analyzer: Analyst Practice Exercise

This exercise uses only the fabricated records in [the sample dataset](examples/sample-auth-events.jsonl). It is designed to teach careful reading and evidence-based reporting before automating the same steps with Python.

## Learning objectives

By the end, you should be able to explain what each record means, calculate basic counts, identify a source that crosses a review threshold, and distinguish an observation from a conclusion.

## Vocabulary

| Term | Plain-language meaning |
| --- | --- |
| JSONL | A text file where each non-blank line is a separate JSON object. |
| Event | One recorded occurrence, such as a successful or failed sign-in. |
| Source IP | The network address recorded as the origin of an event. It does not necessarily identify one person. |
| Outcome | Whether the recorded authentication succeeded or failed. |
| Threshold | A chosen count that tells an analyst which records to review first. |
| False positive | An alert or lead that looks suspicious but turns out to have a benign explanation. |
| Corroborate | Check a claim against another relevant source of evidence. |

## Step 1: Read one record

Example:

\`\`\`json
{"timestamp":"2026-10-19T08:30:00Z","source_ip":"192.0.2.10","username":"training-user","event_type":"authentication","outcome":"failed"}
\`\`\`

Explain each field in your own words:

- \`timestamp\`: when the event was recorded, including its timezone.
- \`source_ip\`: the source address recorded by the system.
- \`username\`: the account name involved in the attempt.
- \`event_type\`: the category of event.
- \`outcome\`: the result recorded by the authentication system.

The addresses in this exercise are documentation-only example addresses. The dataset is synthetic and is not evidence from a real system.

## Step 2: Make a prediction before calculating

Open \`examples/sample-auth-events.jsonl\`. Before using any script, fill in your own estimates.

| Question | Your answer |
| --- | --- |
| How many non-blank records are there? | |
| How many failed authentications are there? | |
| How many successful authentications are there? | |
| How many distinct source IP addresses appear? | |
| Which source has the most failures? | |
| Which usernames appear? | |
| If the review threshold is 3 failures per source across the whole file, which source qualifies? | |

Count an event once. A successful event is not a failed event, and it does not erase any earlier failure.

## Step 3: Build a small evidence table

Group only the failed events by source IP. Do not count successful events in the failure totals.

| Source IP | Failed events | Meets threshold of 3? | What can you safely conclude? |
| --- | ---: | --- | --- |
| 192.0.2.10 | | | |
| 198.51.100.23 | | | |

Then repeat the count by username. The source-IP view and username view answer different questions, so their counts need not match.

## Step 4: Separate facts from hypotheses

For the source that crosses the threshold, write one sentence for each category.

**Observation:** State only what the records show. Include the count and the dataset scope.

**Hypothesis:** Give at least two possible explanations. One may be malicious, but include a plausible benign explanation such as mistyped credentials, a shared network address, or an automated service with a bad password.

**Next validation:** Name the additional evidence you would request, such as identity-provider logs, MFA results, device context, approved scanner records, or a time-correlated endpoint event.

Do not label an address as an attacker based on this dataset alone.

## Step 5: Test data-quality handling on paper

Imagine that an eighth line is added containing \`{broken json\`. The parser should report that line as invalid, preserve its line number, and continue analysing the other records.

Now imagine a record has a missing \`username\`, an invalid IP address, or a timestamp without a timezone. Each record should be rejected with a clear reason rather than silently counted or guessed.

Questions:

1. Why is it useful to report malformed lines rather than stopping at the first one?
2. Why should a timestamp include a timezone before events from different systems are compared?
3. What could go wrong if the same source IP is used by many people behind a shared NAT or VPN?
4. Why is a threshold across the whole file different from three failures within five minutes?
5. What would you need before claiming that a successful login after several failures represents account compromise?

## Check your work

Use this section only after attempting the counts yourself.

- Non-blank records: **7**
- Valid records in the supplied file: **7**
- Failed authentications: **6**
- Successful authentications: **1**
- Distinct source IP addresses: **2**
- Distinct usernames: **2**
- \`192.0.2.10\`: **4 failures**, so it meets a threshold of 3.
- \`198.51.100.23\`: **2 failures**, so it does not meet a threshold of 3.

These are counts, not a verdict. The dataset does not establish who controlled either address, whether the activity was authorised, or whether an account was compromised.

## Analyst note template

Copy and complete this for your own practice:

- **Scope:** Which file and records did I review?
- **Observation:** What exactly did I count or see?
- **Evidence:** Which lines or fields support the observation?
- **Hypotheses:** What benign and malicious explanations remain possible?
- **Limitations:** What does this dataset not tell me?
- **Next step:** What evidence would reduce uncertainty?
- **Confidence:** Low, medium, or high, with a reason.

## Completion criteria

You have completed the exercise when you can explain the difference between an event, a count, a threshold and a conclusion without reading the answer key. If your explanation relies on assumptions that are not present in the records, label them as assumptions.
