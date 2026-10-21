# HTTP Security Headers and Content Security Policy

This guide is a defensive reference for reviewing an application you own or are explicitly authorised to assess. Header presence is only one signal: verify the policy against the application's real behaviour and test both expected and unexpected use cases.

## Review method

1. Identify the exact origin and routes in scope. Include redirects and error pages where relevant.
2. Capture response headers for representative pages, authenticated pages and static assets.
3. Record the observed value, the intended protection, the evidence and any compatibility concern.
4. Check whether the policy is applied consistently at the application, reverse proxy and CDN layers.
5. Test changes in a staging environment before enforcing them in production.

For a host you are authorised to test, inspect response headers with:

```sh
curl --silent --show-error --head https://app.example.test/
```

Some servers handle HEAD differently from GET. If the result is incomplete, use a GET request while discarding the body:

```sh
curl --silent --show-error --dump-header - --output /dev/null https://app.example.test/
```

Replace the example host with an in-scope test host. Do not scan unrelated systems.

## Important headers

| Header | Security purpose | Review questions |
| --- | --- | --- |
| `Content-Security-Policy` | Restricts where a page may load scripts, styles, images, frames and other resources. | Is the policy tailored to the application? Are broad sources or `unsafe-inline` justified and documented? |
| `Strict-Transport-Security` | Tells browsers to use HTTPS for future visits after receiving the header over HTTPS. | Is HTTPS correctly deployed first? Are `includeSubDomains` and preload appropriate for every affected subdomain? |
| `X-Content-Type-Options: nosniff` | Helps prevent browsers from interpreting a response as a different MIME type. | Are correct `Content-Type` values sent for assets and downloads? |
| `Referrer-Policy` | Controls how much referrer information is sent with requests. | Does the chosen policy avoid leaking sensitive URL paths or query parameters? |
| `Permissions-Policy` | Restricts access to selected browser features. | Are camera, microphone, geolocation and other features limited to the origins that need them? |
| `frame-ancestors` in CSP | Controls which origins may embed the page in a frame, helping mitigate clickjacking. | Is embedding required? If so, are only trusted origins allowed? |
| `X-Frame-Options` | Legacy framing control supported by many browsers. | Is it present where needed as a fallback for clients that do not support CSP framing controls? |

No single set of headers is universally correct. A static site, a public API and an authenticated web application have different requirements.

## Building a Content Security Policy

Start with an inventory of resources the page legitimately needs. A restrictive starting point for a simple application might look like this:

```http
Content-Security-Policy: default-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'
```

This is an illustration, not a drop-in policy. It can break applications that legitimately load scripts, fonts, images, API calls or frames from other origins. Add only the specific sources required by observed application behaviour.

Useful directives include:

- `default-src`: fallback for many resource types.
- `script-src`: allowed JavaScript sources and nonce or hash requirements.
- `style-src`: allowed stylesheets and inline-style policy.
- `img-src`: allowed image sources, including whether `data:` is necessary.
- `connect-src`: destinations used by fetch, XHR, WebSocket and related APIs.
- `frame-src`: frames the page may load.
- `frame-ancestors`: sites allowed to embed the page.
- `object-src 'none'`: disables legacy plugin content.
- `base-uri 'self'`: restricts document base URLs.

For inline scripts, prefer a per-response nonce or a carefully managed hash over broadly allowing `'unsafe-inline'`. A nonce must be unpredictable and generated for each response; the same static nonce must not be reused across responses.

`frame-ancestors` cannot be delivered through a CSP meta element. Configure it as an HTTP response header. Use report-only mode during rollout when supported, review reports for real breakage and suspicious violations, then move to enforcement after testing.

## HSTS rollout cautions

A typical HSTS header may use a max-age value, but the correct duration depends on deployment readiness. Start only after HTTPS is reliable. Add `includeSubDomains` only if every affected subdomain supports HTTPS. Browser preload programs have additional requirements and should not be enabled casually because reversing a preload decision can take time.

HSTS does not make an insecure origin safe, and it does not replace certificate management, redirect configuration or secure application design.

## Cookies and sensitive responses

Review cookie attributes separately from general security headers:

- `Secure` limits cookie transmission to HTTPS.
- `HttpOnly` prevents JavaScript from reading the cookie through the document cookie API.
- `SameSite` affects cross-site cookie sending and can help reduce some CSRF risk, but is not a complete CSRF defence.
- Narrow `Domain` and `Path` scope where practical.
- Use appropriate cache controls for responses containing sensitive or user-specific data.

Cookie flags do not replace server-side session invalidation, authorisation checks or CSRF protections.

## Evidence and triage template

| Field | Record |
| --- | --- |
| Asset and route | |
| Date and test environment | |
| Request method and status | |
| Observed header and value | |
| Expected policy and rationale | |
| Reproduction steps | |
| Security impact supported by evidence | |
| Compatibility or business impact | |
| Recommended change | |
| Retest result | |

Classify findings based on demonstrated impact and application context, not merely on a missing header. For example, a missing framing control is more consequential when a sensitive action page can be embedded and the application has no other relevant mitigations.

## Knowledge checks

1. Why can a restrictive CSP break a legitimate application?
2. Why is `frame-ancestors` different from `frame-src`?
3. Why should HSTS be deployed only after HTTPS is reliable?
4. Why is `SameSite` not a complete replacement for CSRF tokens or other request validation?
5. What evidence would you collect before recommending a change?
6. Why should a report-only CSP be reviewed before enforcement?
7. Which headers should be checked on redirects, error responses and authenticated pages?

## Further reading

- MDN, HTTP headers: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
- MDN, Content Security Policy: https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
- OWASP Secure Headers Project: https://owasp.org/www-project-secure-headers/
- OWASP Clickjacking Defense Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html

Use these references to verify browser behaviour and framework-specific configuration before deploying changes.
