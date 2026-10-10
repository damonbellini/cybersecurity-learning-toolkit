# Base64 Encoding and Decoding Cheat Sheet

## What Base64 does

Base64 represents binary data using a printable character set. It is an encoding scheme, not encryption. It does not require a secret key and provides no confidentiality.

The common alphabet uses A–Z, a–z, 0–9, plus `+` and `/`. The `=` character may appear as padding.

## Decode with Python

```python
import base64

encoded = "SGVsbG8gV29ybGQh"
decoded_bytes = base64.b64decode(encoded, validate=True)
print(decoded_bytes.decode("utf-8"))
```

Expected output:

```text
Hello World!
```

## Encode with Python

```python
import base64

message = "Hello World!"
encoded = base64.b64encode(message.encode("utf-8")).decode("ascii")
print(encoded)
```

## Linux command line

```bash
printf '%s' 'SGVsbG8gV29ybGQh' | base64 --decode
printf '%s' 'Hello World!' | base64
```

On some systems, the decode flag may be `-d` instead of `--decode`.

## Troubleshooting

- Preserve the complete string, including any trailing padding.
- Check whether fragments must be joined before decoding.
- Avoid adding spaces or line breaks unless the challenge explicitly includes them.
- If decoding produces unreadable bytes, the input may be incomplete, may use another encoding, or may decode to binary data.
- Decoding a string is not the same as decrypting it.

## Lab workflow

1. Copy the candidate string accurately.
2. Identify the likely encoding based on clues and format.
3. Decode locally using a trusted tool.
4. Inspect the output and validate it against the challenge context.
5. Keep a note of the exact input and resulting output for reproducibility.
