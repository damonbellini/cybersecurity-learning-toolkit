# Digital Evidence and Chain of Custody

Chain of custody is the documented history of evidence collection, transfer, access, storage, and handling. It helps demonstrate that evidence was controlled and that changes can be accounted for.

## Record for each item
- Unique evidence identifier and description.
- Source system and collection location.
- Collection date and time, including timezone.
- Collector identity and collection method.
- Cryptographic hash where appropriate, such as SHA-256.
- Storage location and access restrictions.
- Each transfer or access: who, when, why, and authorization.
- Any transformation or analysis performed on a working copy.

## Safe handling
- Follow organizational policy and applicable law.
- Preserve the original when feasible and analyze a verified copy.
- Use approved tools and document tool versions and commands.
- Restrict access and store evidence securely.
- Avoid unnecessary changes to the source system.
- If a live system must be changed to contain a threat, document the action and rationale.

A cryptographic hash can help detect changes to file contents. A matching hash does not prove who created a file or that its contents are authentic.

## Study questions
- What documents who handled evidence? **Chain-of-custody record**.
- Why calculate a hash? **To help verify integrity**.
- Should analysts alter the only original copy? **Avoid it when feasible and document handling carefully.**
