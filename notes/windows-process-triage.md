# Windows Process Triage

Process triage identifies what is running, where it originated, which account owns it and what it is communicating with.

## Questions

- Is the process expected on this host?
- What executable path and command line does it use?
- Which user or service account launched it?
- What are its parent process and start time?
- Does the executable have a valid signature?
- Does it create unusual network connections or child processes?
- Does its hash match a trusted source?

## Basic commands

```powershell
Get-CimInstance Win32_Process |
  Select-Object ProcessId,ParentProcessId,Name,ExecutablePath,CommandLine
Get-Process | Sort-Object CPU -Descending
```

Access to command lines or process memory may require elevated privileges. Follow organisational policy and minimise changes to the host.

## Investigation cautions

A familiar process name does not prove legitimacy because names can be copied. Conversely, an unsigned executable is not automatically malicious. Correlate file metadata, signature, hash reputation, execution history, network activity and surrounding events.