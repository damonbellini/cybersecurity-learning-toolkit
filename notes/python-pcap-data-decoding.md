# Python Workflow for Decoding Extracted PCAP Data

Python is useful after a packet analyzer has extracted candidate values. Keep extraction and decoding separate so every step can be repeated.

## Decode independent Base64 chunks

```python
import base64

cookies = ["HA==", "AA==", "BQ==", "Mw=="]
chunks = [base64.b64decode(value, validate=True) for value in cookies]
data = b"".join(chunks)

print("Hex:", data.hex(" "))
print("Length:", len(data))
```

## Try a single-byte XOR key

```python
key = 0x72
plaintext = bytes(byte ^ key for byte in data)
print(plaintext)
```

## Good practice

- Preserve the original extracted values.
- Validate Base64 input instead of silently accepting malformed values.
- Print intermediate bytes in hexadecimal.
- Track the order in which values were extracted.
- Avoid assuming output is UTF-8 until the bytes support that conclusion.
- Save scripts with clear names and document the expected input format.

## Reproducibility

A strong write-up should allow another analyst to begin with the same packet capture, run the same extraction, reproduce the byte stream and obtain the same decoded output. This is how a result can be independently checked rather than merely repeated.