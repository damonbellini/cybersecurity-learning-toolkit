# Indicators of Compromise (IOCs)

An indicator of compromise is an observable artifact that may suggest malicious activity. An IOC is a lead to investigate, not automatic proof of compromise.

## Common categories
- **Network**: suspicious IP addresses, domains, URLs, DNS queries, or unusual outbound connections.
- **Host**: file hashes, unexpected executables, persistence entries, or suspicious processes.
- **Identity**: unusual sign-ins, repeated failures, unfamiliar devices, or unexpected privilege changes.
- **Email**: sender infrastructure, malicious URLs, attachment hashes, and message identifiers.
- **Cloud**: unusual API calls, newly created access keys, or unexpected role changes.

## Handling an IOC
1. Record source, first-seen time, confidence, and context.
2. Validate formatting and consider legitimate shared infrastructure.
3. Search relevant telemetry across the environment.
4. Correlate with other evidence before concluding.
5. Apply blocking only through approved procedures.
6. Record search scope and results.

IP addresses and domains can change ownership. Hashes identify exact file contents but do not prove a file is safe. Threat intelligence may be stale, so record its source and timestamp. Never upload confidential files to public scanning services without authorization.

## Study questions
- IOC means **Indicator of Compromise**.
- Why correlate multiple indicators? **To reduce false positives and add context.**
- What should accompany an IOC? **Source, timestamps, context, confidence, and observed matches.**
