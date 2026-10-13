# Windows Memory Forensics Basics

A memory image may preserve volatile evidence that is absent from disk, including process state, loaded modules, network connections and fragments of decrypted data.

## When memory acquisition may help

- A suspected fileless intrusion
- A process that disappears after reboot
- Possible credential theft or code injection
- Suspicious processes with little corresponding disk evidence
- A need to examine active connections and runtime state

## Acquisition principles

1. Obtain approval and consider business impact.
2. Use a trusted, documented acquisition tool.
3. Record host identity, date/time, time zone, operator and tool version.
4. Store the image in access-controlled evidence storage.
5. Hash the image and verify integrity after transfer.
6. Analyse a working copy.

Memory acquisition changes system state to some extent. Document that limitation.

## Analysis areas

- Process and parent-child relationships
- Loaded modules and suspicious regions
- Network connections and sockets
- Command lines and handles
- Evidence of code injection
- Cross-checks against endpoint and event logs

Use tools and procedures approved for the environment. Do not upload sensitive memory images to public services.