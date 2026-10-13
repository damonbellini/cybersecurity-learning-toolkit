# TryHackMe: Detection Rules Development

Room: https://tryhackme.com/room/detectionrulesdevelopment  
Topics: detection engineering, Elastic SIEM, atomic and stateful detections, correlation, anomaly detection, tuning  
Status: Answers transcribed from the prior walkthrough; verify against the current room and data before submission.

## Task 3: The Research Process

1. User who executed recon commands: `tryhatme.thm\sysadmin`
2. False-positive image: `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ngentask.exe`
3. Recon executable missing from the suggested query: `nltest.exe`

## Task 4: Atomic Detections

1. Alerts generated for recon commands: `22`
2. Elastic rule type for atomic detections: `Custom Query`

## Task 5: Stateful Detections

1. Alerts related to password spraying: `1`
2. Attacker IP and total failed attempts: `5.62.18.132, 50`
3. Number of usernames tested: `10`

## Task 6: Correlation-Based Detections

1. Suggested suppression field: `source.ip`
2. Number of usernames tested: `10`
3. Removing “with runs” makes the detection more susceptible to: `False Positive`

## Task 7: Anomaly Detections

1. Elastic rule type using anomaly jobs and statistical baselines: `Machine Learning`
2. Login at 03:00 when normal logins are 08:00–18:00: `Contextual`

## Task 8: Detection Tuning

1. Attacker LogonId: `0x557e9`
2. Tuning strategy: `Full Rework`

## Notes

Task 1 and any other tasks not listed here did not have a verified answer in the prior notes. Do not infer answers. Confirm capitalization and exact accepted wording in the live room.

## References

- Official room: https://tryhackme.com/room/detectionrulesdevelopment
- Use the room's own event data and detection results as primary evidence.
