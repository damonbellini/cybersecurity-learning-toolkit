# TryHackMe: Wi-Fi Fundamentals and Reconnaissance

Room: https://tryhackme.com/room/wififundamentalsandrecon

## Answers

### Task 2: How Wi-Fi Works

1. MAC address uniquely identifying one access point: `BSSID`
2. Human-readable wireless network name: `SSID`

### Task 3: 802.11 Frames

1. Periodic access point advertisement: `Beacon Frame`
2. Client frame actively searching for a network by name: `Probe Request`

### Task 4: Monitor Mode

1. Monitor-mode interface created from `wlan0`: `wlan0mon`

### Task 5: Scanning the Airwaves With airodump-ng

1. AUTH value for enterprise (802.1X): `MGT`
2. Channel used by the enterprise networks in this lab: `44`
3. Number of access points advertising `CorpNet`: `2`

### Task 6: Uncovering Hidden Networks

1. Hidden network SSID: `Staff-Net`
2. Channel: `11`
3. Hidden ESSID length: `9`
4. `wpa_supplicant` option to actively probe by SSID: `scan_ssid=1`
5. Gateway flag: `THM{0e6521916c3adf08e5b6830f6675351e4eebec92}`

### Task 7: Organising Your Recon

1. `airodump-ng` flag for writing captures to files: `-w`

## Key Concepts

- **BSSID** identifies a specific access point radio; **SSID** is the human-readable network name.
- **Beacon frames** advertise an access point. **Probe requests** let a station actively search for a network.
- **Monitor mode** allows a wireless interface to observe 802.11 frames instead of acting only as a normal client.
- `airodump-ng` should scan both 2.4 GHz and 5 GHz where in scope. Enterprise networks in this lab are on channel 44.
- In `airodump-ng`, `ENC`, `CIPHER`, and `AUTH` describe security mode, encryption cipher, and authentication method. `MGT` indicates enterprise authentication; `PSK` indicates a pre-shared key; `SAE` is associated with WPA3-Personal.
- Hiding an SSID is not meaningful access control. Beacon metadata can still disclose the network's presence and SSID length, and clients may reveal the name when probing.
- `scan_ssid=1` configures `wpa_supplicant` to actively search for a hidden SSID.
- `airodump-ng -w <prefix>` writes capture files using the specified prefix. Use `--output-format csv` when only the CSV summary is needed.

## Core Commands

```bash
sudo iw dev
sudo airmon-ng check kill
sudo airmon-ng start wlan0
sudo airodump-ng --band bg wlan0mon
sudo airodump-ng --band a -c 44 wlan0mon
sudo airodump-ng -c 44 --bssid <BSSID> -w <capture-prefix> wlan0mon
sudo airodump-ng --output-format csv --bssid <BSSID> -c <channel> -w <csv-prefix> wlan0mon
```

Use wireless capture and injection commands only in the authorised TryHackMe lab or on networks and equipment you have explicit permission to test.

## Quick Answers

`BSSID` · `SSID` · `Beacon Frame` · `Probe Request` · `wlan0mon` · `MGT` · `44` · `2` · `Staff-Net` · `11` · `9` · `scan_ssid=1` · `THM{0e6521916c3adf08e5b6830f6675351e4eebec92}` · `-w`

## Sources

- TryHackMe room: https://tryhackme.com/room/wififundamentalsandrecon
- Cross-check: https://simontaplin.net/2026/09/23/answers-for-the-tryhackme-fundamentals-and-reconnaissance-room/
