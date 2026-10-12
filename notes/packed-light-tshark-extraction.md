# Packed Light: Extracting HTTP Evidence with TShark

TShark is Wireshark's command-line packet analyzer. It is useful for repeatable extraction and documenting forensic steps.

## Inspect the protocol mix

```bash
tshark -r traffic.pcapng -q -z io,phs
```

## List HTTP request metadata

```bash
tshark -r traffic.pcapng -Y "http.request" -T fields \
  -e frame.number -e frame.time_relative -e ip.src -e ip.dst \
  -e tcp.dstport -e http.host -e http.request.method \
  -e http.request.uri -e http.user_agent
```

## Extract cookie headers

```bash
tshark -r traffic.pcapng -Y "http.request && http.cookie" -T fields \
  -e frame.number -e frame.time_relative -e http.cookie
```

## Preserve evidence

Redirect output to a text file when appropriate, note the TShark version, and keep the original capture unchanged. If multiple cookies or requests appear in a frame, inspect the full packet before assuming each output row maps to one complete application action.

## Troubleshooting

- If HTTP fields are empty, confirm the traffic is actually HTTP and consider whether a non-standard port needs protocol decoding.
- If output ordering matters, include frame number and timestamp fields.
- If a field name is rejected, check available field names with `tshark -G fields`.
- Avoid copying only a screenshot; retain the underlying extracted text for reproducibility.