# AI Agent Security Quick Reference

- Define role and scope before implementation.
- Apply least privilege to every tool.
- Treat retrieved documents, logs, and webpages as untrusted data.
- Enforce authorization outside the model.
- Validate tool arguments and structured outputs.
- Keep a record of tool calls and consequential decisions.
- Use bounded retries and explicit stop conditions.
- Escalate missing or contradictory evidence to a human.
- Do not let confidence replace evidence.
