# Windows CLI: File Management and Searching

Room: [Windows Command Line](https://tryhackme.com/room/windowscommandline)

## Navigation
Use **cd** to move between directories and **dir** to inspect contents. Quote paths containing spaces, for example: **cd "C:\Program Files"**.

## Useful patterns
- **dir /a** lists hidden and system entries too.
- **dir /s *.log** searches recursively for matching log files.
- **where /r C:\Windows notepad.exe** searches a directory tree for a filename.
- **type file.txt** prints text content.
- **find "error" app.log** searches for a string.
- **findstr /i "failed denied" *.log** searches without case sensitivity.
- **copy report.txt report.bak** copies a file.
- **fc before.txt after.txt** compares two files.

The wildcard **\*** matches multiple characters. The wildcard **?** matches one character in common filename patterns.

## Safe practice
Create a temporary folder and use sample files. Before copying, moving, or deleting, verify the current directory and inspect the target with **dir**.

## Mini lab
1. Create a folder named cli-lab.
2. Create a text file and save it there.
3. Display it with **type**.
4. Search for a word with **findstr**.
5. Copy the file and compare the two versions with **fc**.

## Troubleshooting
“File not found” can mean the path is wrong or the current directory is unexpected. “Access is denied” can indicate insufficient permissions or a protected location.
