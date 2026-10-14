# Least Privilege for AI Agents

Least privilege means giving an agent only the access needed for its defined task.

## Implementation practices
- Use read-only tools by default.
- Scope credentials to specific resources.
- Keep secrets out of prompts and logs.
- Require explicit authorization for state-changing actions.
- Validate parameters server-side.
- Rotate credentials and revoke unused access.
- Test denial paths as well as successful paths.

A model instruction alone is not an access control. Enforce permissions in the tool or service layer.
