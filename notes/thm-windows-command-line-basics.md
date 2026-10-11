# TryHackMe: Windows Command Line Basics

Room: [Windows Command Line](https://tryhackme.com/room/windowscommandline)

## Purpose
The Windows Command Prompt (cmd.exe) is a text interface for navigating files, inspecting the system, and running commands. Practice in your assigned TryHackMe machine or another authorized system.

## Essential commands
- **help** lists available commands.
- **dir** lists files and folders.
- **cd** changes directory; **cd ..** moves to the parent directory.
- **cls** clears the terminal.
- **whoami** displays the current account.
- **hostname** displays the computer name.
- **ver** shows Windows version information.
- **systeminfo** displays detailed system information.
- **ipconfig /all** displays network configuration.
- **tasklist** lists running processes.
- **command /?** displays help for a command, for example **ipconfig /?**.

## File operations
- **mkdir lab** creates a directory.
- **type notes.txt** prints a text file.
- **copy source.txt backup.txt** copies a file.
- **move old.txt archive\old.txt** moves a file.
- **ren draft.txt final.txt** renames a file.
- **where notepad** searches for a command in PATH.

Use **del** and other destructive commands only after verifying the target path.

## Mini lab
1. Run **whoami** and **hostname**.
2. Inspect the current directory with **cd** and **dir**.
3. Run **ipconfig /all** and identify the active adapter.
4. Run **tasklist** and find a process you recognize.
5. Record each command, its output, and what you learned.

## Review
1. How are cmd.exe and PowerShell different?
2. What does whoami reveal?
3. Why should you check the current directory before deleting files?
