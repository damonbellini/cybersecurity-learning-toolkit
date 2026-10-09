# Web Session Management

## Why sessions exist
After authentication, a web application often uses a session identifier or token to recognize subsequent requests without asking the user to log in each time.

## Common risks
- Session identifiers exposed through insecure storage or transport
- Session fixation
- Tokens that remain valid too long
- Missing logout or revocation behavior
- Cross-site scripting that enables session theft in some circumstances

## Defensive controls
- Use HTTPS throughout the session.
- Set cookies with Secure and HttpOnly; use an appropriate SameSite policy.
- Rotate session identifiers after login and privilege changes.
- Apply idle and absolute expiration where appropriate.
- Revoke sessions after logout, password reset, or account compromise.
- Avoid placing sensitive tokens in URLs.
- Protect state-changing requests against CSRF where relevant.

## Review questions
- Where is the session identifier stored?
- Can it be invalidated server-side?
- Does the application rotate it after authentication?
- Are cookie attributes configured correctly?

## Key takeaway
Authentication establishes identity; session management must maintain that identity safely.