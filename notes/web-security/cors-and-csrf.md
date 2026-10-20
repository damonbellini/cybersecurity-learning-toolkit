# CORS and CSRF: Understand the Difference

This guide is for reviewing applications you own or are explicitly authorised to assess. CORS and CSRF are related to browser security, but they solve different problems.

## Learning goals

- Explain the same-origin policy and the role of CORS response headers.
- Explain why CORS is not authentication or server-side authorisation.
- Describe how CSRF can occur when browsers attach ambient credentials.
- Record evidence for a safe review of a state-changing endpoint.

## Same-origin policy and CORS

An origin is the combination of scheme, host, and port. For example, `https://app.example.test` and `https://api.example.test` are different origins because their hosts differ. The browser's same-origin policy limits how a document can read data from another origin.

Cross-Origin Resource Sharing (CORS) lets a server declare which origins may read certain cross-origin responses. It does not stop every cross-origin request from being sent, and it does not replace server-side authorisation.

| Header | Purpose | Review question |
| --- | --- | --- |
| `Access-Control-Allow-Origin` | Names an origin permitted to read the response, or uses `*` for public non-credentialed access | Is the value fixed to a trusted origin or reflected from arbitrary input? |
| `Access-Control-Allow-Credentials` | Allows credentialed browser requests to expose a response to a permitted origin | Is credentialed access necessary? |
| `Access-Control-Allow-Methods` | Lists methods allowed by a preflight response | Are only required methods listed? |
| `Access-Control-Allow-Headers` | Lists request headers permitted by preflight | Are custom headers limited to the application's needs? |
| `Vary: Origin` | Signals that a response can differ according to the Origin header | Could a shared cache serve the wrong CORS variant? |

A server must not combine `Access-Control-Allow-Origin: *` with credentialed access. If the application dynamically selects an allowed origin, compare it against an explicit allowlist and return a matching origin only after validation. Configure cache behaviour when responses vary by origin.

## CORS is not authorisation

A command-line client or another server is not governed by browser CORS enforcement. An attacker may be able to send a request even when the browser prevents the initiating page from reading the response. Sensitive endpoints must enforce authentication and authorisation on the server regardless of CORS headers.

Do not treat a permissive CORS header alone as proof of data exposure. Determine whether the browser can make the relevant request, whether credentials are included, what the response contains, and whether the initiating origin can read it.

## CSRF in plain language

Cross-site request forgery (CSRF) occurs when a browser is induced to send an unwanted state-changing request to an application where the user is already authenticated. Cookies may be attached automatically, so the server needs a way to distinguish a legitimate action from a forged request.

Common defences include:
- unpredictable anti-CSRF tokens validated on state-changing requests;
- appropriate `SameSite` cookie settings as defence in depth;
- checking `Origin` and, where appropriate, `Referer` on sensitive browser requests;
- re-authentication or confirmation for high-impact actions;
- avoiding state changes through GET requests.

CORS alone is not a general CSRF defence. A request can sometimes be sent even when the browser prevents the attacking page from reading the response.

## Safe review workflow

1. Confirm scope and use a local lab or explicitly authorised test account.
2. Identify a state-changing action in a test application.
3. Record the normal request method, content type, cookie behaviour, and response.
4. Review whether the endpoint checks the user's permission for the target object and action.
5. Check whether a CSRF token is required and validated. Never use another person's session.
6. Inspect CORS responses for a trusted origin and an untrusted test origin.
7. Document request and response evidence, impact, limitations, and remediation.
8. Restore lab data after testing.

## Example review matrix

| Test | Expected secure behaviour | Evidence |
| --- | --- | --- |
| Trusted origin reads an intended API response | Allowed only where required | Origin and relevant response headers |
| Untrusted origin attempts to read a sensitive response | Browser does not expose the response to that origin | Origin, response headers, browser result |
| State-changing request omits a required CSRF token | Request is rejected | Status, response, server-side validation result |
| User changes an object ID to another user's object | Server checks object-level authorisation | Test account, object ownership, response |
| GET is sent to a state-changing route | Route does not perform the state change | Before/after state and response |

A missing CORS header or rejected preflight does not, by itself, prove that the server-side operation is protected.

## Common misconceptions

- CORS blocks all cross-origin requests. It mainly controls browser access to responses; some requests can still be sent.
- CORS is authentication. It is not. Authentication identifies the caller; authorisation checks permitted actions.
- SameSite cookies solve every CSRF case. They reduce risk but must be considered alongside application flows and browser support.
- A CSRF token can be present but ineffective. The server must validate it and bind it appropriately to the session or request context.
- A successful request proves exploitability. Confirm browser context, credentials, response exposure, state change, and practical impact.

## Exercises

1. Explain the difference between origin and site using two example URLs.
2. Why is `Access-Control-Allow-Origin: *` unsuitable for credentialed browser access?
3. Give an example of a cross-origin request that may be sent even if its response cannot be read.
4. Why should a profile update not use GET?
5. What evidence would you collect before reporting a CSRF issue?
6. Why must object-level authorisation be checked even if CORS is restrictive?

## Further reading

- MDN: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
- OWASP CSRF Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
