# Windows CLI: System and Network Troubleshooting

Room: [Windows Command Line](https://tryhackme.com/room/windowscommandline)

## System discovery
- **whoami** shows the current identity.
- **hostname** shows the computer name.
- **systeminfo** displays operating system and hardware details.
- **tasklist** lists processes.
- **tasklist /svc** shows services associated with processes.
- **driverquery** lists driver information.
- **sc query** displays service status information.

## Network discovery
- **ipconfig /all** shows adapter addresses, DNS, DHCP, and gateway details.
- **ping 127.0.0.1** tests the local TCP/IP stack.
- **ping <gateway-address>** tests reachability to a gateway when ICMP is allowed.
- **tracert example.com** displays the route toward a destination.
- **nslookup example.com** queries DNS.
- **netstat -ano** lists connections and listening ports with process IDs.
- **arp -a** displays the local ARP cache.

Replace placeholders with values from your lab. Firewalls and routing can affect results, so one failed test does not prove a host is offline.

## Practical triage
1. Check the adapter with **ipconfig /all**.
2. Test loopback.
3. Test the default gateway.
4. Resolve a domain using **nslookup**.
5. Inspect connections with **netstat -ano** if investigating a local service.

## Lab worksheet
- Hostname:
- Current user:
- IPv4 address:
- Default gateway:
- DNS server:
- One listening port or established connection:
- What the result means:

Record timestamps and relevant output. Do not assume an unfamiliar process is malicious without validating its path, signer, parent process, and expected role.
