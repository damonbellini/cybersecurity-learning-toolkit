# Cyber Security 101 Study Method

This is a personal workflow for learning actively instead of only completing room questions.

## The Goal

For every topic, aim to:
1. Explain it in simple language.
2. Recognise the important technical terms.
3. Use the basic command or tool associated with it.
4. Understand the output.
5. Reproduce a small authorised lab exercise.
6. Explain why the result matters for security.

## Five Passes

### 1. Understand the question

Before using a tool, identify what the task wants.

Ask:
- What object am I looking for?
- Which host, file, process, account or service matters?
- Does the answer require a name, number, path, value or explanation?
- What information has the room already provided?

If the wording is confusing, rewrite it in your own words.

### 2. Identify the concept

Write a one sentence definition and list unfamiliar terms.

Example:

DNS translates domain names into IP addresses and can also provide other records used by network services.

### 3. Perform the task

Use the smallest useful command first.

```bash
pwd
whoami
ls -la
```

Do not run a complicated command just because it looks advanced. Learn what each option changes.

### 4. Record evidence

For every important command, record:

| Field | Example |
| --- | --- |
| Command | `ip addr` |
| Purpose | Show network interfaces |
| Important output | Interface and IP |
| Security relevance | Helps identify network configuration |
| Next question | What route is configured? |

### 5. Reproduce from memory

Close the walkthrough and repeat the exercise. If you cannot reproduce it, mark the concept for review.

## How to Use Help

Linux:

```bash
command --help
man command
```

Windows PowerShell:

```powershell
Get-Help <command>
Get-Command
```

Use documentation before searching for a solution.

## How to Ask for Help

When a TryHackMe task is difficult:
1. Explain what you think it asks.
2. Show what you tried.
3. Show relevant output.
4. State where your reasoning stopped.
5. Ask for a hint before asking for the answer.

This preserves the learning process.

## Command Card

For each new command, record:

- Command
- Pronunciation
- What it does
- Important options
- Safe example
- Security use

## Shortcuts to Learn First

| Shortcut | Typical terminal use |
| --- | --- |
| Ctrl + C | Interrupt the foreground process |
| Ctrl + L | Clear or redraw the screen |
| Ctrl + D | Send EOF or exit |
| Tab | Complete commands and paths |
| Up Arrow | Recall previous command |
| Ctrl + A | Move to line start |
| Ctrl + E | Move to line end |
| Ctrl + R | Search command history |

Exact behaviour can vary by shell and terminal.

## What Belongs in GitHub

Good learning material includes concise definitions, command explanations, lab exercises, troubleshooting notes, defensive examples, safe Python utilities, detection ideas and CTF writeups written after solving the lab.

Avoid copying entire room text. Paraphrase the concept and record your own reasoning.

## Review

Review important topics later the same day, the next day, several days later and one week later. First try to recall the concept without opening the notes.

## Mastery Test

A topic is becoming useful when you can answer:
1. What is it?
2. Why does it exist?
3. How does it work at a high level?
4. What command or tool can I use?
5. What does the output mean?
6. What security problem is related to it?
7. How would I investigate it in an authorised lab?
8. How would I explain it to a beginner?
9. How would I explain it in a junior interview?

## Ethics

All exercises must target systems you own or systems for which you have explicit permission to test.
