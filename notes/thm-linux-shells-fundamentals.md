# TryHackMe: Linux Shells Fundamentals

Room: [Linux Shells](https://tryhackme.com/room/linuxshells)

## What is a shell?
A shell interprets commands and provides an interface to the operating system. A terminal emulator is the application window; the shell is the command interpreter running inside it.

Common shells include Bash, Zsh, Fish, sh implementations such as Dash, and PowerShell. The default depends on the distribution and user configuration.

## Identify the environment
```bash
whoami
id
pwd
echo "$SHELL"
cat /etc/shells
ps -p $$ -o comm=
```

The SHELL environment variable often indicates the configured login shell, while the ps command helps identify the current shell process. They may differ.

## Essential navigation
- **pwd** prints the current directory.
- **ls -la** lists contents including hidden entries.
- **cd /path** changes directory.
- **cd ..** moves to the parent directory.
- **mkdir lab** creates a directory.
- **cat file.txt** prints text.
- **less file.txt** views longer files page by page.
- **man ls** opens a manual page.

## Mini lab
Run the identification commands and record the output. Compare the configured login shell with the active shell process. Use a temporary directory for file practice.

The shell does not replace the Linux kernel. It interprets commands and starts programs, while the kernel manages processes, memory, devices, and system resources.
