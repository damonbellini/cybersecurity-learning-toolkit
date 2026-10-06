# Sigma Rules

Sigma is a generic rule format for describing suspicious log events in a platform independent way.

## Basic structure

```yaml
title: Suspicious PowerShell Activity
status: experimental
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    Image|endswith: '\\powershell.exe'
  condition: selection
level: medium
```

## Good detection practice

A useful detection should:

- Have a clear purpose
- Minimize unnecessary noise
- Include meaningful metadata
- Define severity
- Explain what behavior is detected
- Be tested against benign activity

Detection engineering is an iterative process. Tune rules after observing real logs.
