# TCP/IP, Ports and the Journey of a Web Request

Beginner study note for authorised learning environments.

## The big picture

A network request is not one single action. Several layers cooperate to move information from an application on one device to an application on another.

A useful simplified model is:

1. **Application layer**: protocols such as HTTP, HTTPS, DNS and SSH describe application-level communication.
2. **Transport layer**: TCP provides a reliable ordered byte stream; UDP sends independent datagrams without TCP's delivery guarantees.
3. **Internet layer**: IP addresses packets between networks.
4. **Link layer**: Ethernet or Wi-Fi carries frames across a local network.

This is a learning model, not a claim that every protocol fits perfectly into one box.

## IP address versus port

An IP address identifies a network interface or destination address at the Internet layer. A port number identifies a transport-layer endpoint used by an application or service.

Think of an IP address as the building address and a port as a particular reception desk inside it. The analogy is imperfect, but it helps separate two different ideas.

- **IP address**: where traffic is being sent.
- **Port**: which transport endpoint should receive it.
- **Protocol**: the rules used to communicate.
- **Socket**: an endpoint used by software for network communication.
- **Listening service**: a program waiting for connections or datagrams on a local endpoint.

A port number alone does not prove which application is running, whether it is exposed to the internet, or whether it is vulnerable.

## TCP and UDP

TCP establishes a connection and provides ordered delivery and retransmission where needed. Applications use it when those properties are useful.

UDP does not provide TCP's connection and delivery guarantees. It can be useful when an application handles timing, retries or loss itself.

Neither protocol is inherently secure. Confidentiality and authenticity depend on the application protocol and its configuration, such as correctly configured TLS.

## Common port associations

These are common defaults, not proof of what a host is running.

| Port | Common association | What to remember |
| --- | --- | --- |
| 22/TCP | SSH | Remote administration; restrict access and use strong authentication |
| 25/TCP | SMTP | Mail transfer between servers in many configurations |
| 53/UDP and TCP | DNS | UDP is common for ordinary queries; TCP is also required in several situations |
| 80/TCP | HTTP | Web traffic without transport encryption by default |
| 443/TCP | HTTPS | HTTP protected by TLS when correctly configured |
| 445/TCP | SMB | Windows file and printer sharing; exposure should be carefully controlled |
| 3389/TCP | RDP | Remote desktop; restrict access and monitor authentication |

Services can use non-default ports. Verify the service with authorised evidence rather than guessing from a number.

## What happens when a browser opens an HTTPS URL?

A simplified sequence:

1. The browser parses the URL and identifies the hostname and destination service.
2. The system resolves the hostname through its configured name-resolution process, often involving DNS.
3. The client establishes network connectivity to the destination IP address and port.
4. For HTTPS over TCP, the client and server negotiate TLS parameters and validate the server certificate according to the client's trust rules.
5. The browser sends an HTTP request over the protected connection.
6. The server returns an HTTP response, which may include a status code, headers and content.
7. The browser processes the response and renders the page.

Modern protocols can use different transport arrangements, so treat this as a common HTTPS-over-TCP path rather than the only possible implementation.

## Status codes are not transport ports

HTTP status codes are application-level response indicators, not network ports.

- **200**: the request succeeded.
- **301 / 302**: the resource is being redirected.
- **400**: the server considers the request invalid.
- **401**: authentication is required or failed.
- **403**: the server refuses the request.
- **404**: the resource was not found, or the server is not revealing it.
- **429**: the client has sent too many requests within a policy-defined interval.
- **500**: the server encountered an internal error.
- **503**: the service is temporarily unavailable or unable to handle the request.

Interpret status codes in context. A single 404 or 500 does not by itself prove a security incident.

## Practical exercise

Use a TryHackMe room, your own virtual machine or another explicitly authorised lab.

1. Write down one example of an IP address and one example of a port. Explain the difference.
2. For the common ports table, explain what each service is normally used for and one defensive concern.
3. Draw the simplified browser request sequence in your own words.
4. Explain why HTTPS does not automatically mean a website is trustworthy.
5. Explain why seeing port 443 open does not prove that the service is correctly configured.
6. Explain the difference between an HTTP 403 response and a network connection timeout.

## Check your understanding

Try answering without looking at the note:

- What problem does DNS help solve?
- How are an IP address and a port different?
- What does TCP provide that UDP does not guarantee?
- At which layer does TLS commonly protect HTTPS traffic?
- Why should a port number be treated as a clue rather than a conclusion?
- What additional evidence would help you decide whether a network event is suspicious?

## Explain it to another person

A good beginner explanation might be:

"An IP address helps route traffic to a destination, while a port helps the operating system deliver transport traffic to the right application endpoint. Protocols define how the communicating systems exchange information. For security work, we identify the service, understand why it should be reachable, and verify the evidence before drawing conclusions."

Rewrite that explanation in your own words before adding it to your personal notes.

## Safety and scope

Only inspect or test systems that you own or have explicit permission to assess. The exercises above are conceptual and do not require scanning public systems.
