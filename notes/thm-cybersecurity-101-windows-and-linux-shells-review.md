# Cyber Security 101: Windows and Linux Shells Review

Related rooms:
- [Windows Command Line](https://tryhackme.com/room/windowscommandline)
- [Windows PowerShell](https://tryhackme.com/room/windowspowershell)
- [Linux Shells](https://tryhackme.com/room/linuxshells)

## Quick comparison

| Task | Windows Command Prompt | PowerShell | Linux shell |
|---|---|---|---|
| Current directory | cd | Get-Location | pwd |
| List files | dir | Get-ChildItem | ls -la |
| Current identity | whoami | whoami | whoami |
| Read text file | type file.txt | Get-Content file.txt | cat file.txt |
| Search text | findstr | Select-String | grep |
| Processes | tasklist | Get-Process | ps, top |
| Network config | ipconfig | Get-NetIPConfiguration | ip addr |

Exact command availability depends on operating system version and installed tools.

## Repeatable lab method
1. Read the task and identify its learning objective.
2. Try the command in the TryHackMe machine before looking up an answer.
3. Record the command and explain its important arguments.
4. Capture useful output, excluding secrets and unrelated personal data.
5. Write one sentence about why the result matters to a defender.
6. Change one variable and repeat the experiment.
7. Record errors and how you resolved them.

## Notes template
- **Objective**
- **Command or script**
- **Expected behavior**
- **Observed output**
- **Explanation in my own words**
- **Security relevance**
- **Common mistake**
- **Question to revisit**

## Self-test
- Explain the difference between Command Prompt and PowerShell.
- Explain why PowerShell pipelines can pass objects.
- Explain the difference between a terminal and a shell.
- Describe how redirection differs from a pipe.
- Identify a safe way to inspect a script before running it.
- Explain why least privilege matters.

## Ethics and scope
Use these techniques only on your own systems, the assigned TryHackMe environment, or systems for which you have explicit authorization. Never copy credentials, tokens, or private information into public notes.
