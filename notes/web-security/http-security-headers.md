# HTTP Security Headers

HTTP response headers communicate security policies to browsers. They complement secure application design; they do not fix vulnerabilities in application logic.

## Headers to know
- **Strict-Transport-Security (HSTS)**: tells browsers to use HTTPS for a configured period. Enable only when HTTPS is correctly deployed.
- **Content-Security-Policy (CSP)**: restricts permitted content sources and can reduce the impact of some injection attacks.
- **X-Content-Type-Options: nosniff**: asks browsers not to infer a different MIME type.
- **Referrer-Policy**: controls how much referrer information is sent to other sites.
- **Permissions-Policy**: controls access to selected browser features.

## Cookie attributes
- **Secure**: send the cookie over HTTPS.
- **HttpOnly**: prevent ordinary JavaScript from reading the cookie.
- **SameSite**: restrict some cross-site cookie sending and can help mitigate CSRF depending on the application.

## Inspecting headers in an authorized lab
    curl -I https://example.com

Review redirects and the full response rather than treating one command as a complete security assessment.

## Common mistakes
- Treating headers as a substitute for output encoding or parameterized database queries.
- Deploying a restrictive CSP without testing required resources.
- Enabling HSTS before HTTPS and certificate configuration are reliable.
- Assuming HttpOnly prevents every form of session theft.

## Study questions
- Which header helps enforce HTTPS on future visits? **Strict-Transport-Security**.
- Which cookie attribute blocks ordinary JavaScript access? **HttpOnly**.
- Do security headers replace secure coding? **No**.
