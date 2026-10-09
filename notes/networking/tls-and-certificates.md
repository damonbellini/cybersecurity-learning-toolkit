# TLS and Certificates

## Purpose
Transport Layer Security protects data in transit by providing encryption and integrity, and it can authenticate the server using a certificate.

## Certificate validation
A client should validate the certificate chain, validity dates, hostname, and trust status. A padlock alone does not prove that a website is honest or safe.

## Handshake at a high level
The client and server negotiate supported parameters, authenticate as required, establish shared session keys, and then protect application traffic.

## Common problems
- Expired certificates
- Hostname mismatch
- Missing intermediate certificates
- Incorrect system clock
- Outdated protocol or cipher configuration

## Defensive practice
Use supported TLS versions, automate certificate renewal where possible, protect private keys, and monitor expiry dates. Never bypass certificate warnings without understanding the cause.

## Key takeaway
TLS protects a connection, but it does not guarantee that the destination itself is trustworthy.