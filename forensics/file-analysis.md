# File Analysis

File analysis examines file content, metadata and structure to understand what a file is and whether it may be suspicious.

## Useful Checks

```bash
file sample
strings sample
sha256sum sample
```

Metadata, hashes, file signatures and embedded strings can provide useful evidence. Never execute an unknown file on a production system. Use an isolated analysis environment.
