# Windows Persistence Triage

Persistence mechanisms allow software or an intruder to survive logoff or reboot. During incident response, investigate persistence locations methodically and compare findings with known-good baselines.

## Common locations to review

- Services and drivers
- Scheduled tasks
- Startup folders
- Run and RunOnce registry keys
- WMI permanent event subscriptions
- Browser extensions and application add-ins
- Newly created accounts and unexpected group membership

## Triage commands

```powershell
Get-ScheduledTask | Select-Object TaskName,TaskPath,State
Get-CimInstance Win32_Service | Select-Object Name,StartMode,State,PathName
Get-CimInstance Win32_StartupCommand | Select-Object Name,Command,Location,User
```

These commands are inventory aids, not proof of malicious activity. Validate paths, signatures, timestamps, parent processes and change history.

## Evidence handling

Record the host, time, command, output and collection method. Do not remove suspicious entries until evidence has been preserved and the response lead has approved containment or remediation.