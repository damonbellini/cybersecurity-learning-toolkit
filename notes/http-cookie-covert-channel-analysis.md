# HTTP Cookie Covert-Channel Analysis

A covert channel hides information inside traffic that appears ordinary. HTTP headers and cookies can carry data without putting it in the URL or request body.

## Indicators

- Repeated requests to one host at regular intervals.
- A custom or implausible User-Agent string.
- Cookie names that do not fit the apparent application.
- Cookie values that are unusually short, encoded-looking or change on every request.
- A request pattern that is inconsistent with normal user interaction.

In Packed Light, the suspicious cookie name is `hotel_sess_state`. The important signal is not the name alone, but the repeated sequence of requests and changing encoded values.

## Analysis method

1. Identify the client, destination, port and request cadence.
2. Compare normal requests with the repeated beacon requests.
3. Inspect every relevant header.
4. Extract candidate values in chronological or frame order.
5. Determine whether values are encoding, compression, encryption or obfuscation.
6. Validate any recovered content against the original packets.

## Defensive response

Correlate packet captures with proxy logs, DNS logs and endpoint telemetry. Do not block traffic based solely on a suspicious-looking cookie; preserve evidence and validate the destination and behavior first.

Cookies are not inherently secret or encrypted. HTTPS protects them in transit when correctly configured, but an endpoint that controls the request can still place data inside them.