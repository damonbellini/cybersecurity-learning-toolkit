# Patch Management

## Purpose
Patch management reduces exposure to known vulnerabilities in operating systems, applications, firmware, and dependencies.

## Lifecycle
1. Maintain an accurate asset inventory.
2. Identify missing updates and relevant advisories.
3. Prioritize by severity, exploitability, exposure, and business impact.
4. Test updates in a representative environment.
5. Deploy according to risk and change procedures.
6. Verify installation and monitor for regressions.
7. Document exceptions, owners, and deadlines.

## Prioritization factors
A critical internet-facing flaw with known exploitation usually deserves faster action than a low-impact issue on an isolated test device. CVSS is useful input, not the only decision factor.

## Useful metrics
- Percentage of supported assets patched within policy
- Median time to remediate critical vulnerabilities
- Number and age of approved exceptions

## Key takeaway
A patch is not complete until deployment is verified and exceptions are tracked.