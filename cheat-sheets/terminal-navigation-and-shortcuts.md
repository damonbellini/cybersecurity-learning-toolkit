# Terminal Navigation and Keyboard Shortcuts

A practical reference for beginners learning Linux shells, Windows Command Prompt and PowerShell. Shortcuts depend on the terminal application, shell, operating system and keyboard layout, so practise these in a disposable terminal before relying on them.

## First, understand the layers

- **Shell:** reads commands and runs programs, such as Bash or PowerShell.
- **Terminal emulator:** provides the window, text display, tabs and copy/paste behaviour.
- **Command line:** the text interface where you enter commands.
- **Keyboard shortcut:** a key combination handled by the terminal, shell or operating system.

The same shortcut can behave differently in different applications. For example, Ctrl+C usually interrupts a foreground command in a Unix-like terminal, but in many graphical applications it copies selected text.

## Linux terminal and Bash

| Shortcut | Typical behaviour | When it helps |
| --- | --- | --- |
| Tab | Completes a command or path | Avoids typing long names |
| Up Arrow / Down Arrow | Moves through command history | Repeats a previous command |
| Ctrl+C | Sends an interrupt to the foreground process | Stops a command that is running too long |
| Ctrl+L | Clears or redraws the terminal display | Makes output easier to read |
| Ctrl+A | Moves the cursor to the start of the current line | Edits a long command |
| Ctrl+E | Moves the cursor to the end of the current line | Adds an option at the end |
| Ctrl+U | Removes text from the cursor to the start of the line in common Bash setups | Clears a mistyped command before running it |
| Ctrl+K | Removes text from the cursor to the end of the line in common Bash setups | Removes an unwanted suffix |
| Ctrl+W | Deletes the word before the cursor in common Bash setups | Corrects part of a command |
| Ctrl+R | Searches command history interactively in Bash | Finds a command used earlier |
| Ctrl+D | Sends EOF; on an empty shell prompt it commonly exits the shell | Ends input or leaves a shell |

**Important:** Ctrl+C is not the same as closing the terminal. It normally asks the foreground process to stop. A program may handle or ignore the interrupt, and some operations may already have completed.

## Moving around the filesystem

Practise these commands in a directory that contains only training files.

```bash
pwd
ls
ls -la
cd ..
cd ~
mkdir shortcut-practice
cd shortcut-practice
touch example.txt
printf 'training note\n' > example.txt
cat example.txt
```

| Command | Meaning |
| --- | --- |
| `pwd` | Print the current working directory |
| `ls -la` | List entries, including hidden entries, with details |
| `cd ..` | Move to the parent directory |
| `cd ~` | Move to the current user's home directory |
| `mkdir name` | Create a directory |
| `touch name` | Create an empty file if it does not exist, or update its timestamp |
| `cat name` | Print a file's contents |

Use `Tab` completion with directory names. Type the first few characters, press Tab, and inspect the completed path before pressing Enter.

## Windows Command Prompt

| Shortcut or command | Typical behaviour |
| --- | --- |
| Up Arrow / Down Arrow | Browse command history |
| Tab | Complete file and directory names in supported contexts |
| Ctrl+C | Interrupt a running command or program |
| `cd` | Display or change the current directory |
| `dir` | List files and directories |
| `cd ..` | Move to the parent directory |
| `cls` | Clear the screen |

Some Windows terminal hosts add their own copy, paste, tab and selection shortcuts. Those are terminal-host features, not universal Command Prompt features.

## Windows PowerShell

| Command or shortcut | Typical behaviour |
| --- | --- |
| Up Arrow / Down Arrow | Browse command history |
| Tab | Complete commands, parameters or paths |
| Ctrl+C | Interrupt a running command |
| `Get-Location` | Show the current location |
| `Get-ChildItem` | List files and directories |
| `Set-Location ..` | Move to the parent directory |
| `Clear-Host` | Clear the visible console |
| `Get-Help Get-ChildItem` | Open help for a command |

PowerShell commands are often called *cmdlets*. Their usual naming pattern is Verb-Noun, such as `Get-Process` or `Get-Service`.

## Safe practice drill

Complete this without copying the commands from the table after the first attempt.

1. Open a terminal and identify which shell you are using.
2. Print the current directory.
3. List the files.
4. Move to the parent directory and then return to your home directory.
5. Create a directory named `shortcut-practice`.
6. Enter the directory and create `notes.txt`.
7. Start typing a command, use Ctrl+A and Ctrl+E to move the cursor, then correct the line without running it.
8. Run a harmless command such as `pwd` or `Get-Location`.
9. Use the Up Arrow to recall the command.
10. Use Ctrl+R in Bash to find a command from history, then press Esc or Ctrl+G to leave the search without running an unintended command.
11. Explain the difference between a shell, terminal emulator and command.
12. Explain what you should do before interrupting a command that may be writing or modifying important data.

## Troubleshooting

- If Tab completion shows several matches, press Tab again or type more characters to narrow the result.
- If Ctrl+C does not stop a program, wait briefly and read the output before taking another action. Avoid force-closing processes without understanding what they are doing.
- If a shortcut behaves differently, identify the terminal application and shell first.
- If command history contains secrets, do not copy or publish the history file. Avoid placing passwords, tokens or private data directly into commands.

## Self-test

Try to answer these without looking above:

1. What does Ctrl+C normally do in a terminal?
2. Why might Ctrl+C copy text in one application but interrupt a command in another?
3. What is the difference between `pwd` and `ls`?
4. What does Tab completion help prevent?
5. Why should you understand a command before using it on a real system?
6. Name one Linux command and its closest basic PowerShell equivalent.
7. Which shortcut can search Bash command history?
8. Why is command history potentially sensitive?

## Notes for your own study

For every new shortcut, record the application, key combination, expected behaviour and one safe example. Mark it as **known**, **needs practice** or **not understood**. Re-test it later from memory instead of only rereading the table.

Only practise commands on systems and files you own or are authorised to use.
