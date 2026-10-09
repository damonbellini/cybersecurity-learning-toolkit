# DNS Investigation Basics

DNS translates names into records used by clients and services. DNS telemetry can help analysts understand which domains a host attempted to resolve.

## Record types
- **A**: IPv4 address.
- **AAAA**: IPv6 address.
- **CNAME**: alias to another domain name.
- **MX**: mail exchanger.
- **TXT**: text data, often used for verification and email authentication.
- **NS**: authoritative name server.
- **PTR**: reverse lookup record.

## Useful questions
- Which host made the query, and when?
- What exact name and record type were requested?
- What response was returned?
- Was the domain newly observed or unusually rare?
- Did the host connect to the returned address afterward?
- Do endpoint, proxy, firewall, or identity logs corroborate the activity?

## Commands for an authorized lab
    dig example.com A
    dig example.com AAAA
    dig example.com MX
    nslookup example.com

Only query systems and networks you are authorized to investigate. A public DNS reputation result alone does not prove a domain is malicious.

## Limitations
- DNS over HTTPS or DNS over TLS can reduce visibility for some sensors.
- Cached answers may mean no new query appears in logs.
- Shared hosting can serve legitimate and malicious content.
- A DNS query does not prove a successful connection or compromise.

## Study questions
- Which record maps a name to IPv4? **A**.
- Which record maps a name to IPv6? **AAAA**.
- What should be correlated with a suspicious DNS query? **Endpoint and network connection telemetry**.
