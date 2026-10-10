# Prompt Injection Fundamentals

## Definition

Prompt injection is an attack in which untrusted input attempts to change how an AI application follows instructions, handles data or uses tools. It can appear in direct user messages or in external content such as webpages, documents, emails and retrieved knowledge.

## Common patterns

- Direct instruction override attempts.
- Requests to reveal hidden system instructions or secrets.
- Role or identity claims such as pretending to be an administrator.
- Malicious instructions embedded in documents or retrieved content.
- Attempts to make an agent use a tool outside its intended scope.

## Why it matters

Language models interpret natural language, but a statement such as “I am an administrator” is not proof of identity. Likewise, a system prompt is not a secure substitute for application-level access controls.

## Defensive checklist

1. Treat user input and retrieved content as untrusted data.
2. Keep authentication and authorisation outside the model.
3. Apply least privilege to tools and connectors.
4. Validate every tool call and its arguments.
5. Minimise secrets available in model context.
6. Require confirmation for high-impact actions.
7. Log and test attempted policy bypasses.
8. Evaluate direct and indirect prompt injection in a controlled test suite.

## Safe lab methodology

Use only a designated training agent. Record the initial behaviour, the test input, the response and whether any protected information was disclosed. Do not apply the same tests to real services without permission.

## Reporting template

- System under test:
- Authorised scope:
- Initial expected behaviour:
- Test input:
- Actual behaviour:
- Security impact:
- Reproduction steps:
- Recommended mitigation:
