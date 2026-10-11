# PowerShell Variables, Scripts, and Safe Automation

Room: [Windows PowerShell](https://tryhackme.com/room/windowspowershell)

## Variables
PowerShell variable names begin with a dollar sign.

```powershell
$name = 'lab-user'
$count = 3
$names = @('alpha', 'beta', 'gamma')
$name
$names
```

## Conditions and loops
```powershell
if ($count -gt 2) {
    Write-Output 'Count is greater than two'
}
foreach ($item in $names) {
    Write-Output $item
}
```

Common comparison operators include -eq, -ne, -gt, -ge, -lt, and -le.

## Example inventory script
Save this as inventory.ps1 in a dedicated lab directory and read it before execution.

```powershell
$computer = $env:COMPUTERNAME
$user = $env:USERNAME
Write-Output "Computer: $computer"
Write-Output "User: $user"
Get-Date
```

## Script safety checklist
- Read the entire script before running it.
- Verify the source of downloaded scripts.
- Understand which permissions it uses.
- Avoid unnecessary administrator privileges.
- Review file, registry, network, and process changes.
- Do not weaken execution policy globally to run an unknown script.
- Test uncertain behavior in a disposable virtual machine.

## Learning exercise
Extend the inventory script to output the date, computer name, username, and Windows version. Explain which values come from environment variables.
