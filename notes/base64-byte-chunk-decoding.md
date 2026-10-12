# Base64 Byte-Chunk Decoding

Base64 represents binary data using printable characters. It is an encoding scheme, not encryption.

## Padding and small values

The characters `=` and `==` are common Base64 padding. A short value such as `HA==` decodes to one byte, hexadecimal `1c`. A sequence of one-byte Base64 values can be used to transport a larger byte stream, provided the values are collected in the correct order.

## Python example

```python
import base64

values = ["HA==", "AA==", "BQ==", "Mw=="]
decoded = [base64.b64decode(value) for value in values]
stream = b"".join(decoded)

print(stream.hex(" "))
print(stream)
```

Keep each chunk separate during initial inspection. If each value is independently padded, concatenating the Base64 text first may not decode correctly.

## Validation checklist

- Preserve packet order.
- Check that each value is valid Base64.
- Inspect the length of each decoded chunk.
- Print bytes as hexadecimal before assuming they are text.
- Do not call Base64 output encrypted merely because it is unreadable.

In the Packed Light investigation, individual cookie values decode to one byte each. Those bytes require another transformation before the message becomes readable.