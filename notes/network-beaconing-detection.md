# Detecting Network Beaconing

Beaconing is repeated communication from a host to another system at regular or semi-regular intervals. Malware may use it to check in with command-and-control infrastructure or transmit small amounts of data.

## What to measure

- Destination IP, hostname and port.
- Inter-arrival times between connections or requests.
- Repetition of URI, method and headers.
- Changes in cookies, parameters or payload lengths.
- User-Agent and TLS characteristics.
- Whether the destination is expected for the endpoint.

## Basic workflow

1. Filter the capture to the suspected port or destination.
2. Export timestamps and request metadata.
3. Sort by time and calculate inter-arrival intervals.
4. Compare the pattern with normal application behavior.
5. Inspect changing fields for possible data transfer.
6. Correlate with DNS, proxy and endpoint records.

A request approximately every second, repeated to the same destination, is a useful lead but not conclusive proof of malware. Legitimate polling and monitoring can also be regular.

## Packed Light clue

The room's scenario mentions a laptop contacting a destination on port 8080 with suspiciously regular timing. The repeated HTTP GET requests and unusual `ByteLotusClient/1.1` User-Agent provide context for inspecting the cookie header.

## Detection ideas

Use proxy logs or network detection rules to alert on unusual periodicity and rare User-Agent values. Alerts should include evidence and be reviewed in context to limit false positives.