# DNS Record Types and Troubleshooting

This note expands the basic idea of DNS into the records a beginner is likely to encounter in networking and security labs.

## What DNS does

The Domain Name System lets applications look up information associated with domain names. A resolver can answer from cache, query other DNS servers or return an error when the requested information is unavailable. DNS is not only a directory of website addresses; it stores several record types for different purposes.

## Common record types

| Type | Purpose | Example of what it tells you |
| --- | --- | --- |
| A | Maps a name to an IPv4 address | A service name has an IPv4 address |
| AAAA | Maps a name to an IPv6 address | A service name has an IPv6 address |
| CNAME | Makes one name an alias of another name | A hostname points to its canonical target |
| MX | Identifies mail exchangers for a domain | Which mail servers receive mail for the domain |
| NS | Identifies authoritative name servers for a zone | Which servers publish the zone's DNS data |
| TXT | Stores text associated with a name | May contain domain-verification or email-policy data |
| PTR | Supports reverse lookup from an IP address to a name | A reverse-DNS name is associated with an address |
| SOA | Provides administrative information about a DNS zone | Includes the primary server field and zone timing values |

A record's presence does not prove that the associated service is online, safe or correctly configured. DNS data is one piece of evidence.

## Recursive and authoritative answers

A **recursive resolver** performs lookups on behalf of a client and may return cached results.

An **authoritative name server** publishes the records for a DNS zone and provides authoritative answers for that zone.

A client normally asks its configured resolver. The resolver may use cached data or consult the DNS hierarchy before returning an answer.

## TTL and caching

The **time to live (TTL)** indicates how long a DNS response may be cached before it should be refreshed. A change to a record may therefore not appear everywhere immediately. Different resolvers can temporarily hold different cached answers, depending on when they last refreshed the data.

Do not assume that an old answer means a domain has been hijacked. Check the record, TTL, resolver and time of observation before drawing a conclusion.

## A structured troubleshooting approach

When a name does not resolve as expected, ask these questions in order:

1. Is the hostname spelled correctly?
2. Does the issue affect one application or several?
3. Is the client using the expected DNS resolver?
4. Does the resolver return an address, an alias, or an error?
5. Is the returned record type the one expected by the application?
6. Could a cached response explain the difference?
7. Is the destination reachable after name resolution succeeds?
8. Is there authoritative evidence for the record, and was it collected recently?

Keep name resolution separate from connectivity. A name can resolve correctly while the destination service is unavailable. Conversely, a destination might be reachable by address while a hostname lookup fails.

## Security considerations

- Unexpected changes to important records should be investigated through the organisation's approved change history.
- Email-related DNS records can help receiving systems evaluate sender policy, but their presence alone does not guarantee that every message is legitimate.
- DNS queries can reveal patterns about software and services a device is trying to use. Follow privacy and logging requirements when reviewing them.
- Use trusted sources and record when the evidence was collected. DNS information can change.

## Practice exercise

Use a training domain or a domain you are authorised to inspect.

1. Find one A or AAAA record and explain what the answer represents.
2. Find an MX record and explain why a domain might publish it.
3. Identify the TTL for one answer and explain how it affects caching.
4. Explain the difference between a recursive resolver and an authoritative server.
5. Describe one reason a DNS answer may differ between two observations.
6. Explain why a successful DNS lookup does not prove that a web application is available.

## Self-check

Try to answer without reading the note:

- Which record type is commonly used for IPv6 addresses?
- What is the purpose of an MX record?
- What does a CNAME represent?
- Why can a recent DNS change take time to appear consistently?
- What additional evidence would you gather if a hostname resolves but the service does not respond?

## Explain it simply

DNS is a distributed naming system. Different record types publish different kinds of information about a name, and caching helps reduce repeated lookups. When troubleshooting, record exactly what was queried, which resolver answered, what result was returned and when it was observed.
