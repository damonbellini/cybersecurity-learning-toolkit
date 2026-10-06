# Suspicious PowerShell Investigation

PowerShell is a legitimate administrative tool that can also be abused by attackers.

## Investigation checklist

- Identify the user.
- Identify the host.
- Capture the command line.
- Identify the parent process.
- Check encoded or obfuscated arguments.
- Review child processes.
- Review network connections.
- Search for persistence.
- Correlate with authentication events.

## Useful telemetry

- Windows Event Logs
- PowerShell logs
- Sysmon
- EDR telemetry
- Network logs

Do not execute unknown commands simply to reproduce an alert. Use an isolated lab when testing suspicious code.
