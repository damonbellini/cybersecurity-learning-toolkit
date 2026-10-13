# Windows Event Log Investigation

Windows Event Logs are a core source of evidence during incident response. They can help reconstruct logons, process activity, service changes and system events.

## Common logs

- Security: authentication, account and audit events
- System: services, drivers and operating-system events
- Application: application-level errors and activity
- Microsoft-Windows-PowerShell/Operational: PowerShell operational events when enabled
- Microsoft-Windows-Windows Defender/Operational: Defender detections and actions

## Useful event IDs

| Event ID | Typical meaning |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Account logoff |
| 4648 | Logon using explicit credentials |
| 4688 | Process creation, if auditing is enabled |
| 4720 | User account created |
| 7045 | Service installed, in the System log |

Interpret events in context and confirm the log provider and version. Audit policy determines which events are available.

## PowerShell collection

```powershell
Get-WinEvent -LogName Security -MaxEvents 100
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624,4625}
```

Export evidence using approved procedures and preserve timestamps, host identity and collection details. Do not clear logs during an investigation.