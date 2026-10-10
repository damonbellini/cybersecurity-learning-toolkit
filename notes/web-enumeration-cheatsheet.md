# Web Enumeration Cheat Sheet

Use these commands only against local labs, systems you own or targets explicitly authorised for testing.

## Confirm connectivity

```bash
curl -I https://example.com
curl -sS https://example.com/robots.txt
```

- `curl -I` requests response headers.
- `curl -sS` suppresses progress output while still reporting errors.

Replace the example domain with an authorised lab target.

## Inspect DNS records

```bash
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com TXT
```

These queries help identify address records, mail servers and text records. DNS data can be incomplete or intentionally restricted.

## Inspect TLS certificates

```bash
openssl s_client -connect example.com:443 -servername example.com
```

Review the certificate chain, validity and hostname. Press Ctrl+C to stop the interactive connection if needed.

## Nmap basics for an authorised lab

```bash
nmap -sV -oN scan.txt 192.0.2.10
```

This performs service-version detection against the example documentation address and saves results to a file. Substitute only a target included in your approved scope.

## What to document

- Target and scope
- Date and time
- Commands and options used
- Open ports and observed services
- HTTP status codes and notable headers
- Unexpected behaviour and supporting evidence
- Recommended next step

## Important cautions

Enumeration results are observations, not proof of a vulnerability. Avoid aggressive scans against production systems without explicit approval. Do not infer that a hidden path or banner guarantees exploitable access.
