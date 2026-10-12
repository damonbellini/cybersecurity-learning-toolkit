# Single-Byte XOR Analysis

XOR combines each input byte with a key byte. Applying the same key again reverses the operation:

```text
cipher_byte XOR key_byte = plaintext_byte
plaintext_byte XOR key_byte = cipher_byte
```

A single-byte XOR key has only 256 possible values, so exhaustive testing is easy.

## Python brute force

```python
data = bytes.fromhex(
    "1c 00 05 33 1e 7b 3a 7c 17 79 3b 17 3f 7c 3c 2b "
    "20 79 26 2f 17 78 3e 2d 1a 17 31 78 3d 35"
)

for key in range(256):
    plaintext = bytes(byte ^ key for byte in data)
    if all(32 <= byte < 127 for byte in plaintext):
        print(f"key=0x{key:02x}: {plaintext.decode('ascii')}")
```

Printable output alone is not proof of correctness. Rank candidates by meaningful language, expected file or flag structure, and whether the result is consistent with the evidence.

## Packed Light result

The documented candidate key is `0x72`. Applying it to the documented byte stream produces:

```text
THM{V3r4_1s_w4tch1ng_0veR_y0u}
```

This is a lightweight obfuscation technique, not secure encryption. For real incident response, treat the decoded result as evidence and corroborate it with independent artifacts.