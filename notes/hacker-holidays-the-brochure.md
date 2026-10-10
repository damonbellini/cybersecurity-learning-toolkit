# TryHackMe: The Brochure
## Hacker Holidays 2026 | OSINT Write-up

Room: https://tryhackme.com/room/hh-thebrochure-081f3e36  
Topic: Open-source intelligence (OSINT), image clue analysis, social-media reconnaissance and Base64 decoding.  
Difficulty: Beginner  
Status: Study notes based on a publicly available walkthrough. Verify the flag in your own active room before submitting.

## Objective

Investigate the Byte Lotus Hotel brochure, follow clues to the hotel's AI assistant VERA, find the hidden social-media account and decode the message assembled from its posts.

## Walkthrough

### 1. Inspect the provided artefact

Download the file supplied in the TryHackMe room and extract it. Inspect the brochure image carefully. Look for visible branding, account names, unusual image details and metadata that could provide leads.

Useful local inspection commands:

```bash
file brochure-image.jpg
exiftool brochure-image.jpg
strings brochure-image.jpg
```

These commands identify the file type, inspect available metadata and search for readable strings. Metadata may be absent or unhelpful, so do not rely on it alone.

### 2. Search for the hotel’s social-media presence

The public walkthrough reports using this Google query:

```text
site:instagram.com "Byte Lotus Resort"
```

This is an example of a targeted search operator. `site:` limits results to a domain and quoted text searches for a phrase. Inspect the results and corroborate account identity using names and imagery from the provided brochure.

### 3. Follow the clue to VERA

The hotel account leads to the Instagram account for its AI assistant, VERA. According to the walkthrough, three posts contain separate fragments of an encoded message.

Record the fragments in the order indicated by the challenge, then concatenate them without adding spaces or punctuation. Do not assume every image or post is relevant; use the challenge clues to establish the correct sequence.

### 4. Decode the message

The combined string reported in the public walkthrough is:

```text
VEhNe1YzckBzX2FDQzB1bnRfaDRzX2IzM25fZjB1bmQhfQ==
```

It is Base64-encoded text. Decode it with CyberChef’s “From Base64” operation, or use Python:

```python
import base64

encoded = "VEhNe1YzckBzX2FDQzB1bnRfaDRzX2IzM25fZjB1bmQhfQ=="
decoded = base64.b64decode(encoded).decode("utf-8")
print(decoded)
```

Base64 is an encoding format, not encryption. Anyone who has the encoded string can decode it; it provides no confidentiality.

## Flag

The publicly reported flag is:

```text
THM{V3r@s_aCC0unt_h4s_b33n_f0und!}
```

Treat this as a reference answer and confirm it against the live room. Flags are case-sensitive and must be entered exactly.

## Key concepts learned

- **OSINT:** collecting and analysing information from publicly accessible sources.
- **Search operators:** narrowing searches with terms such as `site:` and exact-phrase queries.
- **Pivoting:** using one verified clue, such as a brand name, to find a related account or source.
- **Evidence correlation:** matching usernames, imagery and context rather than trusting a single search result.
- **Base64:** representing bytes as printable text; decoding is not the same as decrypting.
- **Digital artefact inspection:** checking file type, metadata and strings while recognising that these sources may contain no useful clue.

## Quick reference

```text
site:instagram.com "Byte Lotus Resort"
file brochure-image.jpg
exiftool brochure-image.jpg
strings brochure-image.jpg
```

For an encoded string, identify the format before decoding it. Base64 commonly uses letters, digits, `+`, `/`, and optional trailing `=` padding, but the appearance alone is not definitive proof.

## Defensive perspective

Public posts, reused images and connected social accounts can reveal relationships that an organisation did not intend to expose. Reduce this risk by reviewing public-facing accounts, avoiding secrets in posts or image metadata, and treating AI-assistant accounts as part of the organisation’s attack surface.

## References

- TryHackMe room: https://tryhackme.com/room/hh-thebrochure-081f3e36
- Public walkthrough: https://medium.com/@devdebug/the-brochure-hacker-holidays-day-0-tryhackme-writeup-608dd82f1344
- CyberChef: https://gchq.github.io/CyberChef/

Only perform security testing in environments where you have permission. This write-up is for learning and for the authorised TryHackMe challenge.
