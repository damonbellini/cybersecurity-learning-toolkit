# PCAP Forensics Workflow

A packet capture is a record of observed network traffic. A repeatable workflow helps prevent missed clues and unsupported conclusions.

## 1. Preserve

- Keep the original capture read-only.
- Record its filename, source, acquisition time and hash.
- Work from a copy when exporting or transforming data.

Example hash command:

```bash
sha256sum traffic.pcapng
```

## 2. Triage

- Review protocol hierarchy and packet counts.
- Identify uncommon ports, hosts and protocols.
- Inspect DNS requests and connection endpoints.
- Look for periodic connections and unusually small repeated requests.

## 3. Investigate

- Apply narrow filters.
- Inspect packet details and stream context.
- Export relevant fields with TShark.
- Keep frame numbers and timestamps to preserve provenance.

## 4. Decode carefully

Identify the exact encoding or transformation before applying it. Keep intermediate artifacts: extracted header values, decoded bytes, XOR key and final plaintext. A reproducible chain is stronger evidence than a flag copied from a walkthrough.

## 5. Report

State the observation, supporting packet numbers, transformation steps, conclusion and uncertainty. Distinguish direct observations from interpretation.

## Packed Light application

The useful chain is HTTP beacon pattern → suspicious cookie header → Base64 one-byte chunks → assembled byte stream → single-byte XOR → candidate flag.