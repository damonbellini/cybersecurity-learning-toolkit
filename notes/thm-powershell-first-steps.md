# TryHackMe: Windows PowerShell First Steps

Room: [Windows PowerShell](https://tryhackme.com/room/windowspowershell)

## What is PowerShell?
PowerShell is a command-line shell and scripting language. Unlike traditional Command Prompt, it commonly passes structured .NET objects through the pipeline instead of only passing text.

## Discover commands
- **Get-Help Get-Process** opens help for a command.
- **Get-Command** lists available commands.
- **Get-Command *Service*** searches command names.
- **Get-Alias** lists aliases.
- **Get-Member** inspects object properties and methods.

Cmdlets commonly follow the Verb-Noun pattern, such as Get-Process, Get-Service, and Get-ChildItem.

## Navigation and files
- **Get-Location** shows the current location.
- **Set-Location C:\Windows** changes directory.
- **Get-ChildItem** lists items.
- **New-Item -ItemType Directory -Name Lab** creates a directory.
- **Get-Content .\notes.txt** reads a text file.
- **Copy-Item .\notes.txt .\notes-copy.txt** copies a file.

## System inspection
- **Get-ComputerInfo** returns system information.
- **Get-Process** lists processes.
- **Get-Service** lists services.
- **Get-NetIPConfiguration** shows network configuration on supported Windows systems.

## Mini lab
1. Run **Get-Command *Process***.
2. Run **Get-Process** and inspect the output.
3. Pipe the result to **Get-Member**.
4. Run **Get-Service** and select a few properties.
5. Use **Get-Help Get-ChildItem -Examples**.

Use an ordinary user shell for learning. Do not run downloaded scripts or launch commands as administrator unless you understand why it is necessary.
