# PowerShell Pipeline, Objects, and Filtering

Room: [Windows PowerShell](https://tryhackme.com/room/windowspowershell)

## The pipeline
The pipe character | sends output from one command to another. PowerShell commonly passes objects with properties rather than plain text.

Examples:
```powershell
Get-Process | Get-Member
Get-Process | Select-Object -First 10
Get-Service | Where-Object Status -eq 'Running'
Get-Process | Sort-Object CPU -Descending
Get-Service | Select-Object Name, Status, DisplayName
```

## Common pipeline cmdlets
- **Where-Object** filters objects.
- **Select-Object** chooses properties or limits the number of objects.
- **Sort-Object** sorts by properties.
- **Measure-Object** calculates counts, sums, and averages.
- **Format-Table** formats output for display and is usually best placed at the end.

## Exporting results
```powershell
Get-Process | Export-Csv .\processes.csv -NoTypeInformation
Get-Service | Out-File .\services.txt
```

Use a lab folder and avoid overwriting important files.

## Mini lab
1. Count running services.
2. List ten processes sorted by CPU time.
3. Export process names and IDs to CSV.
4. Explain why Where-Object is useful before exporting data.

If a property name is unclear, inspect it with Get-Member. Structured data is generally more reliable than parsing formatted screen output.
