# EDR Coverage Validation

An organisation's claim that EDR is deployed does not prove that the expected product is installed, healthy or protecting every endpoint.

## Validate the product

1. Compare the reported product with endpoint inventory and management-console records.
2. Check installed agent services and versions.
3. Confirm last check-in, policy assignment and sensor health.
4. Identify endpoints with missing, disabled or stale agents.
5. Correlate console telemetry with local logs and network observations.

## Validate coverage

Build a list of expected assets from authoritative inventory, then compare it with the set of active EDR-protected hosts. Investigate servers, domain controllers, laptops and remote endpoints separately.

A useful coverage calculation is:

`coverage = actively_protected_expected_assets / total_expected_assets * 100`

Define “actively protected” before calculating the metric. Installed-but-offline agents should not automatically count as healthy coverage.

## TryHackMe OpenDoor scenario

The public room answer guide distinguishes the EDR the customer says is deployed from the EDR actually in use:
- Reported EDR: BitDefender
- Actual EDR: TrendMicro
- Hosts actually protected: 15

These are lab-specific answers, not a general statement about either product. Confirm them against the current room state.