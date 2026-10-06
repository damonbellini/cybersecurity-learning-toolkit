# Log Analysis

Logs are the raw evidence used to investigate security activity.

## Useful log sources

- Windows Event Logs
- Sysmon
- Linux authentication logs
- Firewall logs
- DNS logs
- Proxy logs
- VPN logs
- Cloud audit logs
- Endpoint detection logs

## Investigation method

Start with a precise timestamp and pivot through:

- User
- Host
- Source IP
- Destination IP
- Process
- Parent process
- File hash
- Domain
- URL
- Authentication event

## Correlation

A single event may be harmless. Multiple related events can reveal a complete attack chain.

Example:

```
Failed logins
    ↓
Successful login
    ↓
PowerShell execution
    ↓
Network connection
    ↓
New scheduled task
```

The correlation is often more important than any individual event.
