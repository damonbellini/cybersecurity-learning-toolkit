# DHCP Basics

## What DHCP does
Dynamic Host Configuration Protocol automatically provides network configuration to clients, commonly an IP address, subnet mask, default gateway, DNS servers, and lease duration.

## DORA sequence
1. Discover: client looks for DHCP servers.
2. Offer: server offers configuration.
3. Request: client requests an offered lease.
4. Acknowledge: server confirms the lease.

## Troubleshooting
- Check whether the client received an address and valid lease.
- Look for an APIPA address such as 169.254.x.x on many IPv4 systems; this can indicate DHCP was unavailable.
- Verify VLAN, relay configuration, DHCP scope capacity, and server logs.
- Confirm gateway and DNS settings after a lease is obtained.

## Security notes
Rogue DHCP servers can provide malicious gateway or DNS settings. Network access controls, switch protections, and monitoring can help reduce this risk.

## Key takeaway
DHCP supplies configuration; DNS resolves names, and the default gateway routes traffic off the local subnet.