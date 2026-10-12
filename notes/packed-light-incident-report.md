# Packed Light: Mini Incident Report

## Scope

Training exercise based on the TryHackMe Packed Light room. All analysis is limited to the provided lab capture.

## Observations

- The scenario calls attention to repeated communication over TCP port 8080.
- The HTTP traffic contains repeated GET requests to `byte-lotus-hotel.thm:8080`.
- A custom-looking User-Agent is present: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) ByteLotusClient/1.1`.
- A cookie named `hotel_sess_state` carries changing short values.
- The values are Base64-encoded chunks that decode to individual bytes.

## Analysis

The request cadence suggests beaconing. The cookie values can be collected in frame order, decoded from Base64 and assembled into a byte stream. The documented stream can be decoded with single-byte XOR key `0x72`.

## Candidate recovered value

```text
THM{V3r4_1s_w4tch1ng_0veR_y0u}
```

Confidence is moderate to high for the derivation because the published byte stream and key reproduce the value. However, public walkthroughs conflict on the final flag, so the answer should be confirmed against the live room before claiming the TryHackMe submission was accepted.

## Recommended follow-up in a real environment

1. Preserve packet captures and related endpoint logs.
2. Identify the source endpoint and process responsible for the traffic.
3. Correlate destination and timing with proxy and DNS logs.
4. Determine whether data was transmitted beyond the observed capture.
5. Escalate and contain according to the organisation's incident-response process.

## Evidence quality

Record packet numbers, timestamps, extraction commands, decoded bytes and the XOR key. Do not present a behavioral inference as confirmed fact without corroborating evidence.