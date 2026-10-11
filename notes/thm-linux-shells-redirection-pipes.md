# Linux Shells: Pipes, Redirection, and Command Composition

Room: [Linux Shells](https://tryhackme.com/room/linuxshells)

## Standard streams
Programs commonly use standard input (file descriptor 0), standard output (1), and standard error (2).

## Redirection
```bash
command > output.txt
command >> output.txt
command 2> errors.txt
command > all-output.txt 2>&1
```

A single > replaces the destination file. >> appends. Redirection can overwrite data, so confirm the destination first.

## Pipes
A pipe sends standard output from one command to standard input of another.

```bash
ls -la | less
grep ' 404 ' access.log
ps aux | grep '[s]sh'
find . -type f -name '*.log' 2>/dev/null
```

## Command chaining
- **cmd1 && cmd2** runs the second command only if the first succeeds.
- **cmd1 ; cmd2** runs the second command regardless of the first command's status.
- **cmd1 || cmd2** runs the second command if the first fails.

## Mini lab
1. List files and redirect output to a text file.
2. Append a second listing.
3. Search a sample log for a chosen status code.
4. Redirect error output separately.
5. Explain the difference between > and >>.

When diagnosing a failure, check the exit status immediately with **echo $?**. A pipeline may hide useful errors if only standard output is handled.
