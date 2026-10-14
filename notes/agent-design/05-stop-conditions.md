# Agent Stop Conditions

## Why stop conditions matter
An agent that retries indefinitely can waste resources, repeat harmful actions, or hide a persistent failure.

## Define explicit limits
- Maximum retries and time budget.
- Stop when required evidence is unavailable.
- Stop on permission or scope violations.
- Stop when outputs fail schema validation repeatedly.
- Escalate unresolved cases to a human.

## Review question
Does every failure path end in a safe, observable state?

## Related TryHackMe room
https://tryhackme.com/room/agentdesign
