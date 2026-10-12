# Packed Light: Wireshark Filter Cheatsheet

Room: https://tryhackme.com/room/hh-packedlight-02e5330c

## Display filters

| Goal | Filter |
|---|---|
| TCP traffic using port 8080 | `tcp.port == 8080` |
| HTTP requests | `http.request` |
| HTTP GET requests | `http.request.method == "GET"` |
| Requests with cookies | `http.cookie` |
| Destination port 8080 | `tcp.dstport == 8080` |
| One destination host | `ip.dst == 192.0.2.10` |
| DNS traffic | `dns` |
| TCP retransmissions | `tcp.analysis.retransmission` |

Replace example IP addresses with addresses actually observed in the capture.

## Workflow

1. Open the PCAP/PCAPNG in Wireshark.
2. Review Statistics → Protocol Hierarchy.
3. Filter for TCP port 8080.
4. Identify repeated requests, destination, URI and User-Agent.
5. Select a suspicious request and inspect Hypertext Transfer Protocol headers.
6. Use Follow → HTTP Stream to inspect the conversation.
7. Filter for requests containing cookies and export the relevant values in frame order.

Display filters only change what is shown; they do not delete packets. Keep a copy of the original capture and record the exact filter used for each observation.

## Caution

A port number alone does not prove malicious activity. Correlate the port, destination, timing, request pattern, headers and payload before drawing conclusions.