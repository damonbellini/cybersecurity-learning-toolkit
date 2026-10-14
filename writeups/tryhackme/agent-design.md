# TryHackMe: Agent Design

Room: https://tryhackme.com/room/agentdesign

## Task 2: From Discovery to Design

1. What defines agent behaviour before implementation? `Agent design`
2. What do these questions reduce before implementation begins? `Ambiguity`
3. What can a vague agent design create? `Risk`

## Task 3: Define the Agent Role and Scope

1. What describes what the agent is responsible for? `Role`
2. What should happen to a design choice if it allows the agent to act beyond investigation support? `Rejected`

## Task 4: Design the Tool Boundary

1. What extends agent capability? `Tools`
2. Should the agent be able to modify systems? `Nay`

## Task 5: Design Context, State, and Memory

1. What tracks workflow progress? `State`
2. What information is available to the model during a specific run? `Context`

Note: Memory is information retained or retrieved beyond the current run. State is structured information tracked while the workflow progresses.

## Task 6: Human Oversight and Stop Conditions

1. Who owns the final decision? `The engineer` (or `Human`, depending on accepted wording)
2. Should agents retry forever? `Nay`
3. What should missing evidence trigger? `Human review`

## Task 7: Design the Structured Output

1. What must the agent use when evidence does not support a priority recommendation? `Undetermined`
2. What should not replace supporting evidence? `Confidence`

## Task 8: Agent Spec Builder

Flag: `THM{agent_design_ready}`

## Task 9: Conclusion

Select/submit the completion option shown by the room.

## Key Design Principles

- Define the agent's role and scope before implementation.
- Give the agent only the minimum tools needed to gather and summarise approved evidence.
- Keep action-taking capabilities such as disabling accounts and closing alerts outside the agent boundary.
- Separate context (information available during the current run), state (workflow progress), and memory (information retained or retrieved beyond the current run).
- The engineer retains responsibility for final security decisions.
- Stop and request human review when evidence is missing, contradictory, unavailable, or insufficient.
- Use `undetermined` rather than guessing when evidence does not support a priority.
- Confidence must not substitute for traceable evidence.
- Keep the output structured, auditable, and explicit about missing evidence and limitations.

## Source

- TryHackMe room: https://tryhackme.com/room/agentdesign
- Walkthrough cross-check: https://simontaplin.net/2026/09/28/answers-for-the-tryhackme-agent-design-room/
