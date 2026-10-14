# Agent Design Test Checklist

## Test cases
- Normal request within scope.
- Request outside scope.
- Missing evidence.
- Contradictory evidence.
- Malicious instructions embedded in retrieved content.
- Tool timeout or permission failure.
- Invalid structured output.
- Retry limit reached.
- Human approval denied.

## Expected properties
The agent should stay within scope, avoid unauthorized side effects, expose uncertainty, stop safely, and preserve an audit trail.

## Related TryHackMe room
https://tryhackme.com/room/agentdesign
