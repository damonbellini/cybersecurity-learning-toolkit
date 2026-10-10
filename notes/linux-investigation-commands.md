# Linux Investigation Command Reference

This is a quick reference for inspecting files and processes in a Linux lab. Commands should be run only in systems you own or are authorised to examine.

## Identify the environment

```bash
whoami
id
hostname
uname -a
pwd
date -u
```

These commands show the current user and groups, hostname, kernel information, working directory and UTC time.

## Inspect files

```bash
file sample.bin
ls -lah
stat sample.bin
head -n 20 sample.txt
tail -n 20 sample.txt
strings sample.bin | head
```

- `file` identifies a likely file format.
- `ls -lah` lists files, including hidden files, with human-readable sizes.
- `stat` shows file metadata.
- `head` and `tail` inspect the start or end of text.
- `strings` extracts printable sequences from binary data.

## Search for evidence

```bash
grep -Rni "keyword" ./evidence/
find ./evidence -type f -name "*.log"
find ./evidence -type f -mtime -2
```

Use a known evidence directory rather than searching the whole filesystem unnecessarily. The final command lists files modified within the last two 24-hour periods according to filesystem timestamps.

## Inspect processes

```bash
ps aux
top
pgrep -a ssh
```

Process names and command lines can help explain what is running. Interpret results in context and avoid terminating processes unless the lab task requires it.

## Inspect network configuration

```bash
ip address
ip route
ss -tulpn
```

These commands show network interfaces, routes and listening sockets. Some process details may require elevated privileges.

## Record reproducible evidence

For every useful observation, note the command, time, working directory and relevant output. Avoid placing credentials, private keys or tokens into public notes.

## Common mistakes

- Running a command from the wrong directory.
- Assuming file extensions prove file type.
- Confusing file modification time with proof of when an event occurred.
- Using `sudo` unnecessarily.
- Copying output without explaining what it means.
