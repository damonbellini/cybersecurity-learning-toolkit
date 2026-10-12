# Validating Customer Claims During DFIR

During incident response, customer statements are valuable leads but should not automatically be treated as verified facts.

## Common ambiguous statements

- “The network is segmented.”
- “MFA is enabled.”
- “RDP is disabled.”
- “EDR is installed everywhere.”
- “The suspicious file was removed.”

Each statement needs a precise definition, a scope and supporting evidence.

## Validation loop

1. Capture the original statement.
2. Ask clarifying questions.
3. Restate your interpretation in plain language.
4. Ask the customer to confirm or correct it.
5. Verify against configuration, logs, inventory or artifacts.
6. Record the result and any remaining uncertainty.

## Examples

For “MFA is enabled,” ask which users and applications are covered, whether it is enforced by policy, and whether exceptions exist.

For “EDR is installed everywhere,” compare the expected asset inventory with active, healthy agent telemetry.

For “the file was removed,” ask who removed it, when, how, and whether a copy or forensic record remains.

## Reporting

Use labels such as confirmed, likely, unverified and contradicted. Keep evidence references attached to each conclusion. This avoids turning assumptions into incident facts.