# Password Security and Hashing

## Hashing versus encryption

A cryptographic hash maps input data to a fixed-length digest. A secure password storage system should use a password-hashing scheme designed to resist guessing, with a unique salt and appropriate cost parameters.

Encryption is reversible with the correct key. Hashing is designed to be one-way; it is not a method for recovering a forgotten password.

## Password storage principles

- Use a modern password-hashing algorithm such as Argon2id, scrypt or bcrypt.
- Generate a unique random salt for each password.
- Use parameters appropriate to the deployment and available resources.
- Prefer established libraries and frameworks over custom cryptography.
- Apply rate limits and monitoring to login attempts.
- Support multi-factor authentication where appropriate.
- Never store plaintext passwords or log credentials.

## Why salts matter

A salt is a random value stored alongside the password hash. Unique salts prevent identical passwords from producing identical stored hashes under the same scheme and make precomputed lookup tables less useful.

A salt is not a secret key. It does not replace a password-hashing algorithm or an appropriate work factor.

## Safe Python demonstration

This example computes a general-purpose SHA-256 digest to illustrate hashing only. It is **not suitable for storing passwords**.

```python
import hashlib

message = b"example text"
digest = hashlib.sha256(message).hexdigest()
print(digest)
```

For real password storage, use the password-hashing implementation provided by a trusted framework or a dedicated library supporting Argon2id, scrypt or bcrypt.

## Authentication review checklist

- Are passwords hashed with a password-specific algorithm?
- Is every password given a unique salt?
- Are password reset tokens short-lived and single-use?
- Are login attempts rate-limited?
- Are credentials excluded from logs and error messages?
- Are sessions invalidated after password changes where appropriate?
- Is multi-factor authentication available for sensitive accounts?

## Ethical testing

Only test authentication controls in environments you own or are authorised to assess. Do not attempt to access other people's accounts.
