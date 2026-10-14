# Wi-Fi Reconnaissance Command Cheat Sheet

Use only in an authorized lab or on equipment you own.

```bash
iw dev
iw list
sudo airmon-ng start wlan0
sudo airodump-ng wlan0mon
sudo airodump-ng --band a wlan0mon
sudo airodump-ng -c <channel> --bssid <BSSID> -w <prefix> wlan0mon
```

- `iw dev` lists wireless interfaces.
- `iw list` displays wireless device capabilities.
- Monitor mode allows passive observation of 802.11 traffic.
- Capture files may contain sensitive metadata; store them securely.
