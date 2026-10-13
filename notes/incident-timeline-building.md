# Building a DFIR Incident Timeline

A timeline combines observations from different evidence sources into a coherent sequence. It helps test hypotheses and identify gaps.

## Recommended fields

| Field | Purpose |
|---|---|
| Timestamp | Event time with time zone or UTC normalization |
| Host | Source endpoint or server |
| User | Relevant account, if known |
| Event | Concise description of what happened |
| Source | Log, artifact, alert or packet capture |
| Evidence reference | Event ID, frame number, file path or record ID |
| Confidence | Confirmed, likely or unverified |
| Notes | Context and limitations |

## Workflow

1. Preserve original timestamps and time zones.
2. Normalize a working copy to a common time basis.
3. Document clock drift and ingestion delays.
4. Correlate logons, process execution, file changes and network events.
5. Separate direct observations from inferred activity.
6. Identify missing periods and alternative explanations.

## Quality checks

Do not infer causation from proximity in time alone. Validate host identity and timestamp semantics, and keep links to source artifacts so another analyst can reproduce the timeline.