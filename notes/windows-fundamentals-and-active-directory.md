# Windows Fundamentals and Active Directory

This is a paraphrased personal study guide based on the topics covered by TryHackMe.

## 1. Windows Fundamentals 1

Windows Fundamentals 1 introduces the Windows desktop environment, the NTFS file system, User Account Control, the Control Panel and core Windows concepts.

### Windows Desktop

Important desktop elements include the Start Menu, Taskbar, Search, Notification Area and system settings.

The Start Menu provides access to applications, settings and system tools.

The Taskbar provides quick access to running and pinned applications.

File Explorer is used to navigate drives, folders and files.

### NTFS

NTFS is the primary file system used by modern Windows systems.

Important concepts include files, folders, permissions, ownership and metadata.

NTFS permissions control which users and groups can read, modify or execute resources.

### User Account Control

User Account Control, or UAC, helps prevent unauthorised changes that require administrative privileges.

UAC prompts the user when an action requires elevated permissions.

### Control Panel and Settings

Windows provides graphical tools for managing hardware, applications, user accounts, networking and system configuration.

The Control Panel contains many legacy configuration interfaces while modern Windows versions also use the Settings application.

## 2. Windows Fundamentals 2

Windows Fundamentals 2 covers System Configuration, UAC settings, Resource Monitoring, the Windows Registry and additional administrative tools.

### System Configuration

System Configuration can be accessed with:

`msconfig`

It provides access to boot configuration, services and startup related settings.

### UAC Settings

UAC behaviour can be configured through Windows security settings.

The purpose of UAC is to reduce the risk of unwanted privileged actions.

### Resource Monitoring

Windows includes tools for monitoring system activity.

Task Manager can display running applications, processes, CPU usage, memory usage, disk activity, network usage and startup applications.

Resource Monitor provides more detailed information about CPU, memory, disk and network activity.

### Windows Registry

The Windows Registry is a hierarchical database containing configuration information used by Windows and installed applications.

Common registry hives include:

`HKEY_LOCAL_MACHINE`

`HKEY_CURRENT_USER`

`HKEY_CLASSES_ROOT`

`HKEY_USERS`

`HKEY_CURRENT_CONFIG`

Registry changes should be made carefully because incorrect modifications can affect system behaviour.

## 3. Windows Fundamentals 3

Windows Fundamentals 3 covers built in Microsoft security and maintenance features including Windows Updates, Windows Security and BitLocker.

### Windows Updates

Windows Update provides operating system and security updates.

Keeping systems patched is an important defensive security practice because updates can address vulnerabilities and reliability issues.

### Windows Security

Windows Security provides access to several security controls including antivirus protection, firewall settings, account protection and device security.

Microsoft Defender Antivirus helps detect and respond to malicious software.

### Windows Firewall

Windows Firewall controls network traffic based on configured rules.

Firewall rules can allow or block connections depending on network profile, program, port and protocol.

### BitLocker

BitLocker provides full volume encryption for supported Windows editions and devices.

Encryption helps protect data if a device or drive is lost or stolen.

Recovery information is important because encryption can prevent access to protected data without the required credentials or recovery key.

## 4. Active Directory Basics

Active Directory is Microsoft's directory service for Windows domain environments.

It provides centralised management of identities, computers, resources and access.

### Domain

A domain is a logical administrative boundary containing users, computers and other directory objects.

### Domain Controller

A Domain Controller hosts Active Directory Domain Services and authenticates users and computers in the domain.

### Users and Groups

User accounts represent identities.

Groups allow administrators to manage permissions for multiple users or computers more efficiently.

### Organizational Units

Organizational Units, or OUs, are containers used to organise objects inside Active Directory.

OUs can also be used as a scope for applying Group Policy.

### Group Policy

Group Policy allows administrators to centrally configure settings for users and computers.

Policies can control security settings, software configuration, system behaviour and other Windows features.

### Authentication

Active Directory commonly uses Kerberos and also supports NTLM for authentication scenarios.

A domain login allows a user to authenticate against the domain and access authorised resources.

### LDAP

Lightweight Directory Access Protocol, or LDAP, is used to query and interact with directory services.

### Security Principles

Important Active Directory security concepts include least privilege, strong authentication, appropriate group membership, account management, patching, auditing and monitoring.

## Essential Windows Tools

```text
File Explorer
Task Manager
Resource Monitor
Control Panel
Settings
System Configuration (msconfig)
Registry Editor (regedit)
Windows Security
Windows Firewall
BitLocker
Computer Management
Event Viewer
```

## Study Notes

Understand Windows authentication, permissions, users, groups, processes and system configuration before moving into more advanced Windows security topics.

Active Directory is especially important for enterprise security because identities, computers, policies and access controls are often centrally managed.

Only test Windows systems and Active Directory environments that you own or have explicit permission to assess.

## References

Windows Fundamentals 1: https://tryhackme.com/room/windowsfundamentals1xbx
Windows Fundamentals 2: https://tryhackme.com/room/windowsfundamentals2x0x
Windows Fundamentals 3: https://tryhackme.com/room/windowsfundamentals3xzx
Active Directory Basics: https://tryhackme.com/room/winadbasics
