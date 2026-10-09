# Windows Event Logs: First Look

Windows records operating-system, application, security, and service events.

## Main logs in Event Viewer
- **Application**: application events.
- **System**: Windows components, drivers, and services.
- **Security**: security auditing events, depending on audit policy and permissions.
- **Setup**: setup and servicing events.
- **Forwarded Events**: events collected from other systems when forwarding is configured.

## Example security event IDs
- **4624**: successful logon.
- **4625**: failed logon.
- **4634**: logoff.
- **4688**: process creation, if required auditing is enabled.
- **4720**: user account created.
- **4728**: member added to a security-enabled global group.

## Investigation workflow
1. Establish the time window and host timezone.
2. Filter by time, provider, event ID, account, or keyword.
3. Read event details and correlate them with other records.
4. Build a timeline and record queries and findings.
5. Check whether the required audit policy was enabled.

Event IDs need context. Logs may be disabled, overwritten, cleared, or never collected centrally. A missing event does not prove an action did not happen.

## Study questions
- Which log commonly contains logon audit events? **Security**.
- What does event 4625 usually indicate? **A failed logon**.
- Why correlate events across hosts? **To establish sequence and scope**.
