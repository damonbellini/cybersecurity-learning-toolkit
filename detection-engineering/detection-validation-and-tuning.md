# Detection Rule Validation and Tuning

A detection rule is not finished when it matches one suspicious-looking event. It needs a clear hypothesis, known data requirements, repeatable tests, an owner and a plan for reducing false positives without hiding real threats.

## 1. Start with a testable hypothesis

Write the behavior you want to identify in one sentence.

Example: "An account produces an unusually high number of failed authentication events from one source in a short period."

Define the scope before writing a query:

- **Data source:** which log provider or table contains the events?
- **Required fields:** timestamp, account, source, destination and outcome, as available.
- **Time semantics:** event time versus ingestion time, and the time zone.
- **Detection condition:** threshold, grouping keys and time window.
- **Exclusions:** documented expected activity, with an owner and review date.
- **Response:** what should an analyst do when the rule fires?

Do not describe a broad label such as "detect hacking" as a testable hypothesis.

## 2. Build a small test matrix

Create examples that should trigger the rule and examples that should not. Use synthetic records or an authorised lab.

| Test case | Expected result | Why it matters |
| --- | --- | --- |
| Threshold reached inside the time window | Alert | Basic positive test |
| One event below the threshold | No alert | Basic negative test |
| Same number of events spread outside the window | No alert | Validates time logic |
| Successful authentication mixed with failures | Count failures only, preserve success as context | Prevents incorrect counting |
| Missing source or timestamp | Reject, flag or handle according to documented policy | Tests data quality |
| Duplicate event delivered twice | Follow documented deduplication policy | Prevents inflated counts |
| Approved test or known service account | Alert or suppress only according to explicit scope | Prevents accidental blind spots |

Record the exact test input, rule version, expected result, actual result and any discrepancy. A test that has not been run is not a passing test.

## 3. Validate the data before tuning the query

Confirm that the expected log source is enabled and that events arrive with the fields the rule uses. Check:

- field names and data types;
- missing values and inconsistent casing;
- event timestamps, ingestion delay and clock skew;
- duplicate ingestion;
- coverage gaps on endpoints or accounts;
- whether the test event is actually present in the search window.

A query can be logically correct and still fail when the data source is incomplete or mapped differently.

## 4. Measure alert quality

Use a labelled test set where possible. Define the terms consistently:

- **True positive:** the rule alerted on activity that meets the documented detection objective.
- **False positive:** the rule alerted on activity that does not meet that objective.
- **False negative:** relevant test activity occurred but the rule did not alert.
- **True negative:** the rule correctly did not alert on irrelevant test activity.

Precision is the proportion of alerts that are true positives. Recall is the proportion of relevant positive cases that were detected. A small hand-built lab is useful for checking logic, but it is not enough to claim production performance.

Also track operational measures such as alert volume, analyst time, data latency and the percentage of alerts that cannot be investigated because required fields are absent.

## 5. Tune carefully

When a rule is noisy, identify the cause before adding exclusions. Useful tuning options include:

1. correct a field mapping or timestamp issue;
2. improve grouping keys so unrelated events are not combined;
3. choose a threshold based on observed baseline behaviour;
4. add narrowly scoped exclusions for verified expected activity;
5. enrich the alert with context so an analyst can decide faster;
6. split a broad rule into clearer, separately testable conditions.

For every exclusion, document the reason, scope, approver and review date. Avoid broad allow-lists based only on a username, hostname or IP address. Attackers can use legitimate accounts and infrastructure.

## 6. Treat changes as versioned releases

Before deployment, record:

- rule name and unique identifier;
- objective and threat behaviour;
- required data sources and fields;
- severity and rationale;
- test cases and results;
- known limitations and exclusions;
- owner, version and last validation date;
- analyst response instructions;
- rollback method.

After deployment, review alert volume and sample both alerts and non-alerting periods. Re-test the rule after schema changes, logging changes or major environment changes. A detection that used to work can silently degrade.

## 7. Practical exercise

Use the synthetic authentication scenario in the SOC authentication-failure investigation lab.

1. State the detection hypothesis in one sentence.
2. Specify the grouping key, threshold and time window.
3. List three positive tests and three negative tests.
4. Explain how a successful logon following failures affects triage without proving compromise.
5. Name two data-quality problems that could cause a missed or noisy alert.
6. Write a change note for one proposed tuning adjustment, including the risk of the adjustment.
7. State what evidence would be required before claiming the rule works reliably in production.

## Completion checklist

- [ ] The detection objective is specific and testable.
- [ ] Required fields and data sources are documented.
- [ ] Positive and negative tests have expected results.
- [ ] Time zones, ingestion delay and duplicate events were considered.
- [ ] Exclusions have a narrow scope and an owner.
- [ ] The analyst knows what to investigate after an alert.
- [ ] The rule can be versioned, reviewed and rolled back.
