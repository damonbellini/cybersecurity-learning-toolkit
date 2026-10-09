# Defense in Depth

## What it means
Defense in depth uses multiple independent security controls so that one failed control does not expose the entire system.

## Example layers
1. Asset inventory and secure configuration
2. Identity controls, MFA, and least privilege
3. Network segmentation and firewalls
4. Endpoint protection and application controls
5. Centralized logging and alerting
6. Tested backups and incident response

## Practical example
If a phishing email bypasses the mail filter, MFA may prevent account takeover. Conditional access may restrict the sign-in, and SIEM alerts may help analysts investigate the attempt.

## Study checklist
- Identify preventive, detective, and corrective controls.
- Explain why overlapping controls reduce single points of failure.
- Record which layer detects an event and which layer responds.

## Key takeaway
Security is strongest when controls complement one another rather than relying on one product.