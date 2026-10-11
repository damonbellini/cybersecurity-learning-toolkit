# Linux Shells: Permissions, PATH, and Environment

Room: [Linux Shells](https://tryhackme.com/room/linuxshells)

## Permissions
- **ls -l** displays file type and permission bits.
- **chmod** changes permissions.
- **chown** changes ownership and may require elevated privileges.
- **umask** shows or sets the mask used when creating files.

Example:
```bash
chmod u+x script.sh
ls -l script.sh
```

This adds execute permission for the file owner. Apply permission changes only to files you control or are authorized to administer.

## PATH and command resolution
PATH is a colon-separated list of directories searched for executable commands.

```bash
echo "$PATH"
command -v bash
type ls
which python3
```

An unexpected executable earlier in PATH can cause a different program to run than intended. Use command -v or type to inspect command resolution.

## Environment variables
```bash
echo "$HOME"
echo "$USER"
printenv
export LAB_MODE=practice
echo "$LAB_MODE"
```

Exported variables are inherited by child processes. Avoid placing passwords or API keys in shell history or world-readable scripts.

## Running scripts
A shell script often begins with a shebang such as **#!/usr/bin/env bash**. Inspect content and permissions before running it.

```bash
head -n 20 script.sh
bash -n script.sh
```

bash -n checks syntax without executing the script. It does not prove that the script is safe.

## Mini lab
Inspect permissions, add execute permission to a script you created, check command resolution, and create a harmless environment variable. Explain the difference between permissions and PATH lookup.
