# Linux Processes and Services

## Core concepts
A process is a running program instance with a process ID (PID). A service is a background function, commonly managed by a service manager such as systemd.

## Useful commands
```bash
ps aux
 top
 pgrep -a ssh
 systemctl status ssh
 journalctl -u ssh --since today
```

Remove the leading space before `top`, `systemctl`, or `journalctl` if copying commands into a script; each command is shown separately for readability.

## Investigation workflow
- Identify the process name, PID, owner, and parent process.
- Review command-line arguments and resource usage.
- Check whether the service is expected on that host.
- Inspect relevant logs and recent configuration changes.
- Validate findings before stopping or killing a process.

## Safety note
Do not terminate unfamiliar processes on production systems just because the name looks unusual. Confirm business impact and follow approved procedures.

## Key takeaway
Process inspection, service state, and logs together provide more context than any one command.