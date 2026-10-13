# Windows Defender Investigation Notes

Microsoft Defender Antivirus and its operational logs can provide evidence of detections, remediation actions and configuration changes. In an enterprise, also review the organisation's central security console where applicable.

## Review locally

```powershell
Get-MpThreat
Get-MpComputerStatus
Get-WinEvent -LogName 'Microsoft-Windows-Windows Defender/Operational' -MaxEvents 100
```

Available cmdlets and fields vary by Windows version and permissions.

## Questions to answer

- What threat name or detection identifier was recorded?
- Which file, process or location was involved?
- When was the detection observed?
- Was the item quarantined, blocked or allowed?
- Did the detection recur?
- Was protection disabled or policy changed?
- Do central EDR records agree with local telemetry?

## Cautions

A detection name is not a complete incident explanation. Preserve event records and correlate them with process, file, identity and network evidence. Do not restore quarantined files or disable protection during triage without explicit authorisation.