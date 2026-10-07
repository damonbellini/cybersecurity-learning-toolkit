# File Integrity Monitoring

File integrity monitoring detects unexpected changes to important files.

A basic workflow is:

1. Select files that require monitoring.
2. Generate trusted baseline hashes.
3. Store the baseline securely.
4. Recalculate hashes during later checks.
5. Investigate unexpected differences.

Useful targets can include configuration files, scripts, and other security sensitive resources.

A change is an alert for investigation, not automatic proof of compromise.
