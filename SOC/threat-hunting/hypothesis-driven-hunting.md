# Hypothesis Driven Threat Hunting

Threat hunting begins with a hypothesis about suspicious behavior.

## Example hypothesis

A compromised account may be used to authenticate to an unusual workstation.

## Hunt steps

1. Define the hypothesis.
2. Identify required telemetry.
3. Query the relevant logs.
4. Establish normal behavior.
5. Identify anomalies.
6. Investigate suspicious results.
7. Document findings.
8. Create or improve a detection.

## Example data sources

- Authentication logs
- Endpoint telemetry
- DNS
- Proxy
- Firewall
- Cloud audit logs

A good hunt should produce either useful findings or a better understanding of why the hypothesis was not supported.
