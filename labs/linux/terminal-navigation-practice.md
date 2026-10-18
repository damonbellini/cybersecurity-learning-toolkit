# Linux Terminal Navigation Practice Lab

**Level:** Beginner  
**Estimated time:** 25–35 minutes  
**Environment:** A Linux VM, TryHackMe terminal or local machine where you are authorised to work  
**Prerequisites:** Read [Terminal Navigation and Keyboard Shortcuts](../../cheat-sheets/terminal-navigation-and-shortcuts.md)

## Objective

Practise moving around the filesystem, editing a command line, using command history and describing what each action does. The goal is not speed. The goal is to understand the shell and be able to repeat the steps without a walkthrough.

## Safety and setup

Use a temporary directory that you own. Do not practise with important files, production logs or directories containing secrets.

Create the workspace:

```bash
mkdir -p ~/terminal-practice
cd ~/terminal-practice
pwd
```

Before continuing, confirm that the printed path ends in `terminal-practice`.

## Task 1: Create and inspect files

Run each command and write down what you expect before pressing Enter.

```bash
printf 'INFO training started\n' > sample.log
printf 'WARN training example\n' >> sample.log
printf 'INFO training finished\n' >> sample.log
ls -la
cat sample.log
wc -l sample.log
```

Record:
- How many lines does the file contain?
- Which command created or replaced the file?
- Which commands appended to it?
- Why is it important to understand the difference between `>` and `>>`?

Expected result: the file contains three lines. If it does not, inspect the commands and the current directory before changing anything.

## Task 2: Search without changing the file

```bash
grep -n 'WARN' sample.log
grep -i 'training' sample.log
```

Record the difference between the two results. Explain what `-n` and `-i` change. Confirm that the file still has three lines.

## Task 3: Practise command-line editing

1. Type `printf 'this is a practice command\n'` but do not press Enter yet.
2. Use Ctrl+A to move to the beginning of the line.
3. Use Ctrl+E to move to the end.
4. Use the arrow keys to move the cursor within the line.
5. Correct a word, then inspect the full command before running it.
6. Use the Up Arrow to recall a previous harmless command.

In Bash, press Ctrl+R and type a distinctive word to search command history. Press Esc or Ctrl+G to leave the search if you do not want to run the selected command.

Write down which shortcuts worked in your terminal. If one behaves differently, record the terminal application and shell rather than assuming that your system is broken.

## Task 4: Use help instead of guessing

Run:

```bash
grep --help
command -v grep
```

Answer:
- What does `command -v` tell you?
- Where would you look for the full manual for grep?
- Why should you inspect an unfamiliar command's options before running it?

## Task 5: Explain a small investigation

Imagine the training log contained repeated WARN lines. Do not label the activity malicious based on the word WARN alone.

Write a short note with these headings:

1. **Observation:** What did the command output actually show?
2. **Evidence:** Which command and file support the observation?
3. **Interpretation:** What might explain the result?
4. **Next check:** What additional information would help distinguish normal activity from a problem?

This is the same discipline used in security analysis: separate facts from assumptions and make conclusions proportional to the evidence.

## Knowledge check

Answer without looking at the reference sheet:

1. What is the difference between a shell and a terminal emulator?
2. What does Ctrl+C usually do to a foreground process?
3. Why can Ctrl+D exit a shell when the input line is empty?
4. What is the difference between standard output and standard error?
5. Why can a command that succeeds still produce a result you did not intend?
6. Why is a high count or warning message not, by itself, proof of malicious activity?

## Completion checklist

- [ ] I confirmed my working directory before creating files.
- [ ] I can explain each command I used.
- [ ] I can use Tab and command history.
- [ ] I know how to interrupt a foreground command.
- [ ] I can find command help.
- [ ] I recorded the actual output instead of inventing expected output.
- [ ] I can explain one result in plain language and one in technical language.

## Reflection template

Complete these sentences after the lab:

- The command I understand best is ___ because ___.
- The shortcut I need to practise is ___.
- I expected ___, but the output showed ___.
- The next time I get stuck, I will first ___.
- In a security investigation, I would avoid concluding ___ until I had checked ___.

All data in this lab is synthetic. Use only systems and files you own or are authorised to access.
