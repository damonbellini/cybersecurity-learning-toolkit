# Nmap

Nmap is a network discovery and security auditing tool used to identify hosts, ports and services in authorised environments.

## Common Commands

```bash
nmap <target>
nmap -sV <target>
nmap -O <target>
nmap -p 80,443 <target>
nmap -p- <target>
```

`-sV` attempts service version detection. `-O` attempts operating system detection. `-p` selects ports. `-p-` scans all TCP ports.

Always define scope before scanning and only scan systems you own or have explicit permission to assess.
