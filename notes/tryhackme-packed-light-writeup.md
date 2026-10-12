# TryHackMe: Packed Light — Room Write-up

Room: https://tryhackme.com/room/hh-packedlight-02e5330c  
Focus: PCAP analysis, HTTP beaconing, covert data channels, Base64, single-byte XOR.

## Investigation summary

The scenario describes a laptop repeatedly contacting a host on TCP port 8080. The capture contains ordinary traffic as well as repeated HTTP GET requests to `byte-lotus-hotel.thm:8080`. The unusual User-Agent is `Mozilla/5.0 (Windows NT 10.0; Win64; x64) ByteLotusClient/1.1`.

The repeated requests contain a suspicious cookie named `hotel_sess_state`. Its values are short Base64 strings. Each decoded value contributes one byte to a larger message. The assembled bytes are obfuscated with single-byte XOR.

## Useful investigation commands

```bash
unzip packed-light-forensics-*.zip
tshark -r traffic.pcapng -q -z io,phs
tshark -r traffic.pcapng -Y "http.request" -T fields \
  -e frame.number -e ip.dst -e tcp.dstport -e http.host \
  -e http.request.uri -e http.user_agent
tshark -r traffic.pcapng -Y "http.request && http.cookie" -T fields \
  -e frame.number -e frame.time_relative -e http.cookie
```

In Wireshark, start with `tcp.port == 8080`, then narrow to `http.request` and inspect request headers. Follow an HTTP stream to understand the context, but also extract all relevant cookie values in packet order.

## Data recovery

1. Extract the `hotel_sess_state` cookie value from every beacon request, preserving packet order.
2. Remove the cookie name and Base64-decode each value separately, or concatenate values only if the encoding scheme supports that.
3. Convert each decoded one-byte result into a byte stream.
4. Test single-byte XOR keys and check for readable ASCII and the expected `THM{...}` flag format.

The published byte stream is:

```text
1c 00 05 33 1e 7b 3a 7c 17 79 3b 17 3f 7c 3c 2b
20 79 26 2f 17 78 3e 2d 1a 17 31 78 3d 35
```

XOR key: `0x72`

Recovered flag from the byte stream and XOR key:

```text
THM{V3r4_1s_w4tch1ng_0veR_y0u}
```

## Verification note

A second public walkthrough gives a different flag, but does not show the same reproducible byte-stream derivation. Treat the flag above as the better-supported candidate because the documented bytes XORed with `0x72` reproduce it. Confirm it in the live TryHackMe room before treating the platform submission as verified.

## Lessons

- Repeated, evenly spaced requests can indicate beaconing.
- Inspect headers and cookies, not only URLs and request bodies.
- Base64 is encoding, not encryption.
- XOR obfuscation is reversible and must not be mistaken for strong cryptography.
- Preserve packet order and document the exact transformation chain.

Use these techniques only on authorised captures and lab files.