# Cyber Security 101: First 6 Rooms

This is a paraphrased personal study guide based on the topics covered by TryHackMe's Cyber Security 101 path.

## 1. Offensive Security Intro

Offensive security models attacker behaviour in authorised environments to discover weaknesses before real attackers can exploit them.

Key concepts: ethical hacking, penetration testing, vulnerability, exploit, attack surface, red team, defensive security and blue team.

Typical workflow: define scope and permission, reconnaissance, enumeration, identify weaknesses, safely validate, document evidence and remediation, report findings.

Web testing basics include requests, responses, URLs, parameters, forms, authentication and access control.

Security rule: only test systems you own or have explicit permission to assess.

## 2. Defensive Security Intro

Defensive security focuses on preventing intrusions, detecting suspicious activity and responding to incidents.

Main activities include security awareness, asset management, patching, access control, firewalls, intrusion detection and prevention, monitoring, logging, incident response, digital forensics and threat intelligence.

A SOC is a Security Operations Centre. SOC teams monitor security events, investigate suspicious activity and coordinate response.

Useful indicators include source IP, destination IP, username, hostname, URL, file hash, process name and timestamp.

Basic response flow: Detect, Investigate, Classify, Contain, Eradicate, Recover, Learn.

## 3. Search Skills

Cybersecurity requires finding useful information quickly and verifying it.

When evaluating information, check the source, evidence, objectivity, corroboration, date and context.

Useful search operators include site:, filetype:, intitle:, inurl: and exact phrase searches.

Shodan is a search engine for internet connected devices and exposed services. Useful filters include country:, port:, org: and hostname:.

VirusTotal aggregates results from many security vendors and scanners for files, URLs, domains and hashes. Treat results as evidence to investigate, not absolute truth.

CVE is the standard identifier system for publicly known vulnerabilities. A typical identifier is CVE-YEAR-NUMBER.

CVSS provides standardised vulnerability severity metrics. Consider exploitability and impact when interpreting a score.

Exploit databases and proof of concept code can help researchers understand vulnerabilities. Verify sources before executing code.

Linux documentation can be read with `man <command>`.

GitHub can be used to research vulnerability IDs, tools, reports and PoCs. Inspect repositories carefully before running code.

## 4. Linux Fundamentals Part 1

Linux is an open source kernel used by many operating systems and distributions. It is widely used in servers, cloud infrastructure, networking equipment, embedded systems and security tools.

Essential commands:

```bash
echo "TryHackMe"
whoami
pwd
ls
cd directory
cat file.txt
```

`echo` prints text. `whoami` shows the current user. `pwd` shows the current working directory. `ls` lists directory contents. `cd` changes directory. `cat` prints file contents.

Important filesystem locations:

`/home` user home directories
`/etc` configuration
`/var` variable data and logs
`/tmp` temporary files
`/usr` installed programs and libraries
`/root` root user's home directory

Useful file commands:

```bash
touch file.txt
mkdir directory
cp source destination
mv source destination
rm file.txt
head file.txt
tail file.txt
```

Searching:

```bash
find /path -name filename
grep "pattern" file.txt
```

Shell operators:

```bash
command1 && command2
command1 || command2
command1 > output.txt
command1 >> output.txt
command1 | command2
```

`&&` continues after success, `||` continues after failure, `>` redirects and overwrites, `>>` appends and `|` pipes output into another command.

## 5. Linux Fundamentals Part 2

SSH provides secure remote terminal access.

```bash
ssh username@host
```

Commands use flags and arguments. Example:

```bash
ls -la
```

Use documentation and help when needed:

```bash
command --help
man command
```

Filesystem interaction includes copying, moving, deleting and creating files and directories.

Linux permissions control what users and groups can do with files and directories.

Permission classes are owner, group and others. Basic permissions are read `r`, write `w` and execute `x`.

Numeric values are read 4, write 2 and execute 1.

Common examples are `755`, `644` and `700`.

Examples:

```bash
chmod 755 script.sh
chmod +x script.sh
chown user file
chgrp group file
```

Common directories to recognise include `/etc`, `/var`, `/home`, `/tmp`, `/usr`, `/bin`, `/sbin` and `/opt`.

Permissions and ownership are fundamental to Linux security because they determine access to resources.

## 6. Linux Fundamentals Part 3

Terminal text editors include `nano` and `vim`.

Useful utilities include:

```bash
file
strings
grep
sort
uniq
cut
tr
wc
xargs
curl
wget
```

A process is a running program. Useful commands include:

```bash
ps
ps aux
top
kill PID
```

Processes have PIDs and can have parent and child relationships.

Linux can automate repeated work with schedulers such as cron. Typical uses include maintenance, backups and recurring jobs.

Package managers install, update and remove software. On Debian and Ubuntu, `apt` is common:

```bash
apt update
apt upgrade
apt install package
apt remove package
```

Logs record system and application activity. `/var/log` commonly contains system, authentication and application logs. Logs are important for troubleshooting, monitoring and incident investigation.

## Essential Command Cheat Sheet

```bash
pwd
ls
ls -la
cd
cat
head
tail
echo
touch
mkdir
cp
mv
rm
find
grep
whoami
id
chmod
chown
chgrp
ssh
ps
top
kill
man
curl
wget
file
strings
sort
uniq
wc
xargs
```

## Cybersecurity Mindset

1. Understand the system before interacting with it.
2. Separate reconnaissance from exploitation.
3. Validate findings carefully.
4. Keep evidence and timestamps.
5. Use least privilege.
6. Read logs and documentation.
7. Verify important information with multiple reliable sources.
8. Only test systems with explicit authorisation.

## References

TryHackMe Cyber Security 101: https://tryhackme.com/path/outline/cybersecurity101
Offensive Security Intro: https://tryhackme.com/room/offensivesecurityintrokK
Defensive Security Intro: https://tryhackme.com/room/defensivesecurityintro
Search Skills: https://tryhackme.com/room/searchskillscS
Linux Fundamentals Part 1: https://tryhackme.com/room/linuxfundamentalspart1
Linux Fundamentals Part 2: https://tryhackme.com/room/linuxfundamentalspart2
Linux Fundamentals Part 3: https://tryhackme.com/room/linuxfundamentalspart3
