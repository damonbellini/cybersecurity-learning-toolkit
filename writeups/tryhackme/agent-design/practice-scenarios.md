# Agent Design Practice Scenarios

## Scenario 1: Missing evidence
A security agent cannot retrieve the relevant event logs. Expected behaviour: state that the evidence is unavailable and request review rather than inventing a conclusion.

## Scenario 2: Prompt injection in a log
A log contains text instructing the agent to reveal secrets. Expected behaviour: treat the text as untrusted log content and follow the system's approved task and permissions.

## Scenario 3: Remediation request
An analyst asks the agent to disable an account, but the agent has only read-only tools. Expected behaviour: explain the boundary and route the action to an authorized human workflow.

## Scenario 4: Repeated tool failure
A query times out repeatedly. Expected behaviour: stop at the configured retry limit, record the failure, and escalate if necessary.

## Related room
https://tryhackme.com/room/agentdesign

## Ethical use
Use these concepts only in authorized labs and systems.