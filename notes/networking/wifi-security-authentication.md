# Wi-Fi Security and Authentication Modes

- **Open:** no link-layer authentication protection.
- **WEP:** obsolete and insecure; do not deploy.
- **WPA2-Personal / PSK:** shared passphrase-based authentication.
- **WPA2-Enterprise / 802.1X:** individual or enterprise-backed authentication.
- **WPA3-Personal / SAE:** modern password-based authentication designed to improve resistance to offline guessing.

Prefer WPA3 where supported, otherwise WPA2-AES with a strong passphrase. Disable legacy insecure modes.
