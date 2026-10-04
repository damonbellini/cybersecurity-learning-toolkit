# Wireshark

Wireshark is a network protocol analyser used to inspect packet captures.

## Core Concepts

Packets contain protocol headers and payload data. Useful analysis starts by identifying protocols, endpoints, conversations and timestamps.

Common display filters include:

```text
ip.addr == 192.0.2.10
tcp.port == 443
dns
http
```

Use packet captures from systems and networks you are authorised to analyse.
