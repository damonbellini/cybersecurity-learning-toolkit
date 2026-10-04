# Hashing

A cryptographic hash function maps input data to a fixed length digest.

## Security Properties

A useful cryptographic hash should make it computationally difficult to recover the original input, find collisions and predict a digest for a chosen input.

Common modern families include SHA 2 and SHA 3.

Hashes are useful for file integrity checks, password storage schemes and identifying known files. Passwords should be stored with dedicated password hashing schemes rather than plain general purpose hashes.
