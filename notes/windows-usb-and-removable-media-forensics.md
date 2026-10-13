# Windows Removable Media Forensics

USB and removable storage can be relevant to data theft, malware introduction or movement of evidence. Available artifacts vary by Windows version, configuration and retention.

## Evidence sources

- Windows event logs
- Device installation and setup records
- Registry artifacts related to mounted devices
- EDR telemetry showing file access or process activity
- File-system metadata and recent-file artifacts
- DLP or endpoint device-control logs

## Questions

- Which device was connected and when?
- Which user was logged on?
- Was the device mounted or assigned a drive letter?
- Were files copied, opened or executed?
- Is there corroborating endpoint or DLP telemetry?

## Cautions

A device connection does not prove data was copied. A missing event does not prove a device was never connected. Preserve the relevant artifacts, document collection methods and correlate timestamps across sources. Avoid inserting unknown media into a live investigative workstation.