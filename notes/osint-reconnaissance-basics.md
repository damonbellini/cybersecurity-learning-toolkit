# OSINT Reconnaissance Basics

## What is OSINT?

Open-source intelligence (OSINT) is the process of collecting and analysing information from publicly accessible sources. The goal is to answer a defined question using evidence, not to collect information indiscriminately.

## A repeatable workflow

1. Define the question and authorised scope.
2. Identify likely public sources.
3. Search with focused keywords and operators.
4. Record URLs, timestamps and relevant observations.
5. Corroborate findings with independent sources.
6. Separate confirmed facts from assumptions.
7. Summarise the result and its limitations.

## Useful search operators

```text
site:example.com keyword
"exact phrase"
filetype:pdf topic
intitle:report keyword
inurl:docs keyword
```

Use these operators to narrow searches. Search results can be outdated, duplicated or misleading, so open the original source and verify context.

## Pivoting between clues

A pivot is a transition from one lead to another. For example, a company name on a brochure may lead to an official website, which may link to an official social profile. Confirm that each link is credible before treating accounts as connected.

## Evidence log template

| Time (UTC) | Source URL | Observation | Confidence | Follow-up |
|---|---|---|---|---|
| YYYY-MM-DD HH:MM | URL | What was observed | Low / Medium / High | What to verify |

Preserve the original URL and the exact observation. Do not label an inference as a confirmed fact.

## Ethics and safety

Use public sources and stay within the challenge scope. Do not bypass access controls, impersonate people, or expose private personal information. Only test systems with explicit permission.
