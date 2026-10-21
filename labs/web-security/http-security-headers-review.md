# Lab: Review HTTP Security Headers

**Level:** Beginner to intermediate  
**Estimated time:** 30–45 minutes  
**Scope:** A local application or a staging host for which you have explicit permission  
**Goal:** Collect evidence, compare headers with application requirements and write a defensible remediation note.

This lab does not require exploiting a site. Do not test public hosts unless you have authorisation. Use a local training app or a designated staging environment.

## Learning outcomes

By the end, you should be able to:

- capture response headers without saving a response body;
- distinguish an observed fact from a risk hypothesis;
- assess whether CSP, HSTS, MIME-sniffing and framing controls fit the application;
- record compatibility questions and retest evidence;
- explain why header presence alone does not prove that an application is secure.

## Part A: Prepare the scope

Fill in the following before sending requests.

| Item | Your value |
| --- | --- |
| Approved host or local origin | |
| Routes in scope | |
| Test environment and date | |
| Person or team who authorised the test | |
| Routes requiring authentication | |
| Expected legitimate third-party resources | |

If you cannot identify the approved host and scope, stop and obtain permission before testing.

## Part B: Capture evidence

For a host in scope, run:

```sh
curl --silent --show-error --dump-header headers.txt --output /dev/null https://app.example.test/
```

The command writes response headers to a local text file and discards the body. Replace the example hostname with the approved target. Protect the output if it contains internal hostnames or other sensitive metadata.

Inspect the file:

```sh
cat headers.txt
```

If the endpoint redirects, record each relevant status and `Location` value. Do not assume the headers on the first response are the same as those on the final page. For a simple first pass, you can ask curl to follow redirects:

```sh
curl --silent --show-error --location --dump-header redirect-headers.txt --output /dev/null https://app.example.test/
```

This can produce multiple header blocks, one per response. Keep the status line with each block so the evidence is interpretable. Do not include credentials, session cookies or bearer tokens in shared notes.

Repeat the capture for a small, representative set of approved routes: a public page, a static asset, an error response and an authenticated page if the test account and authorisation permit it. Avoid changing application state.

## Part C: Build the header matrix

Use this worksheet. Mark a control as **not applicable** only when you can explain why.

| Control | Observed value | Expected behaviour | Evidence or concern | Next action |
| --- | --- | --- | --- | --- |
| Content-Security-Policy | | | | |
| Strict-Transport-Security | | | | |
| X-Content-Type-Options | | | | |
| Referrer-Policy | | | | |
| Permissions-Policy | | | | |
| CSP frame-ancestors or X-Frame-Options | | | | |
| Cache-Control on sensitive routes | | | | |
| Set-Cookie attributes where applicable | | | | |

Do not recommend copying a generic header bundle without checking application behaviour. A CSP must reflect the actual resources a page needs. HSTS is meaningful only after HTTPS is reliably configured. Cookie attributes should be reviewed on the actual `Set-Cookie` response, not inferred from a browser storage view alone.

## Part D: Interpret three scenarios

### Scenario 1: No CSP on a marketing page

You observe that a public page has no CSP header. You have not found script injection, and you do not know whether the page loads third-party scripts.

Answer:
1. What is the observation?
2. What potential benefit could CSP provide?
3. What additional inventory and testing are needed before a policy is proposed?
4. Why would “confirmed XSS” be an unsupported conclusion?

### Scenario 2: HSTS is present on the main host

The main host returns HSTS, but a legacy subdomain is still served over HTTP.

Answer:
1. Is `includeSubDomains` automatically safe to add?
2. Which owners and hostnames must be checked first?
3. What deployment and rollback constraints should be documented?

### Scenario 3: Framing is allowed

A sensitive account page can be embedded by any site, and no framing control is present.

Answer:
1. Which header directive can restrict which sites embed the page?
2. What legitimate embedding use cases must be checked?
3. What controlled test would demonstrate the actual risk without targeting real users?

## Part E: Prioritise findings

Rate each finding using evidence and context rather than a missing-header checklist alone.

- **Impact:** What sensitive action, data or trust boundary could be affected?
- **Exposure:** Which routes and users are affected?
- **Exploit preconditions:** What would an attacker need to control or induce?
- **Existing mitigations:** Are there other controls that materially change the risk?
- **Confidence:** Is the issue directly observed, inferred or still unverified?
- **Fix complexity:** Could the change break legitimate application behaviour?

A useful finding describes a concrete route, observed response, plausible impact, limitation and recommended validation. Do not claim compromise or exploitability without evidence.

## Deliverable

Write a short report with:

1. Scope and test date.
2. Commands used and routes sampled.
3. A header matrix with observations.
4. Two prioritised findings or a reasoned statement that no actionable issue was confirmed.
5. Recommended changes and compatibility risks.
6. Retest evidence and unresolved questions.

Use this format for each finding:

```text
Title:
Affected route:
Observation:
Evidence:
Security impact:
Confidence and limitations:
Recommendation:
Retest criteria:
```

## Completion checklist

- [ ] The target and routes were explicitly in scope.
- [ ] Response status and headers were captured.
- [ ] Redirects were distinguished from final responses.
- [ ] Sensitive tokens and cookies were excluded from notes.
- [ ] Observations were separated from assumptions.
- [ ] Recommendations were tailored to application behaviour.
- [ ] The report explains what was not tested.
- [ ] Retest criteria are measurable.

## Review questions

1. Why might a missing header be a hardening gap rather than a confirmed vulnerability?
2. Why should CSP be tested in report-only mode before enforcement when that option is available?
3. Why can HSTS configuration create availability problems if subdomains are not ready?
4. What does `X-Content-Type-Options: nosniff` not protect against?
5. How would you explain a finding to a developer without overstating its severity?
