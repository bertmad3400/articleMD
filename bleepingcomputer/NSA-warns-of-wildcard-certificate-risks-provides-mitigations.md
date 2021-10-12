# NSA warns of wildcard certificate risks, provides mitigations
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/nsa-warns-of-wildcard-certificate-risks-provides-mitigations/)
+ Date: October 12, 2021
+ Author: Ionut Ilascu


## Article:
![NSA provides mitigations against wildcard certificate risks](https://www.bleepstatic.com/content/hl-images/2021/07/29/NSA_headpic.jpg)


The U.S. National Security Agency (NSA) is warning of the dangers stemming from the use of broadly-scoped certificates to authenticate multiple servers in an organization.


In a document released last week, the agency provides mitigations against the risks that come with the use of wildcard certificates. These include a recently disclosed ALPACA technique that could be used for various traffic redirect attacks.


### ALPACA can bite


The agency is referring to the dangers posed by wildcard or multi-domain digital certificates that validate server identity to allow a trusted, secure connection via the Transport Layer Security (TLS) cryptographic protocol.


In a presentation two months ago, researchers showed that TLS servers running different protocols but with compatible certificates (e.g. wildcard, multi-domain) could be exploited via an application layer protocol content confusion attack.


They named the technique [ALPACA](https://alpaca-attack.com/), short for Application Layer Protocols Allowing Cross-Protocol Attack, noting that a malicious actor meeting certain conditions could at least steal cookies or perform cross-site scripting attacks.


A wildcard digital certificate can be used with multiple subdomains on the same domain, so it can cover multiple servers (e.g. email, FTP, apps), while a multi-domain certificate is used for multiple domains on a single IP address.


The [NSA says](https://media.defense.gov/2021/Oct/07/2002869955/-1/-1/0/CSI_AVOID%20DANGERS%20OF%20WILDCARD%20TLS%20CERTIFICATES%20AND%20THE%20ALPACA%20TECHNIQUE_211007.PDF) [PDF] that “ALPACA is a complex class of exploitation techniques that can take many forms,” and that a realistic scenario for such an attack would require the following:


* a target web application that uses TLS
* another service/application (typically not a web server) that presents a valid TLS certificate with a subject name that would be valid for the targeted web app, such as when wildcard certificates are too broadly scoped
* a means for the malicious actor to redirect victim network traffic intended for the target web app to the second service (likely achieved through Domain Name System (DNS) poisoning or a man-in-the-middle compromise)
* an HTTP request that is accepted by the second service that results in at least part of the request being reflected back to the sender


A threat actor meeting these “relatively uncommon conditions” would be able to run at least phishing, watering hole, malvertising, or man-in-the-middle (MitM) attacks.


Using the ALPACA technique, an adversary could cause the victim’s web browser to trust and execute responses reflected from a malicious service that are signed with the correct certificate.


This opens the door to stealing session cookies, private user data, and executing arbitrary code in the context of a vulnerable server.


![Compromising a secure web application using the ALPACA technique](https://www.bleepstatic.com/images/news/u/1100723/2021/ALPACA_exploit.jpg)


1. The malicious actor induces the user to visit a crafted URL (phishing, malvertising, etc)
2. The user sends a request for the URL to app.example.com
3. Using one of many network manipulation techniques, the user’s request is redirected by the malicious actor to service.example.com instead
4. The non-HTTP service.example.com (e.g., a File Transfer Protocol [FTP], Simple Mail Transfer Protocol [SMTP], or other non-web server) attempts to process the HTTP request causing an error that reflects the malicious content into the server’s response
5. The server’s response is signed by the *.example.com certificate
6. The user’s browser receives the response to their request. Since the request was to app.example.com and the response is authenticated by *.example.com, the browser trusts the response and executes it within the context of app.example.com. This gives the malicious script access to user data and cookies for app.example.com within the browser


The NSA also reminds organizations of the role wildcard certificates play in a trust architecture since they "can be used to represent any system within its scope."


For this reason, they should ensure the protection of the private key of a wildcard certificate and keep it on a well-maintained server to avoid the risk of an attacker getting it by compromising a poorly-secured machine.


![Jumping to secure server after hacking insecure machine within the same certificate scope](https://www.bleepstatic.com/images/news/u/1100723/2021/CertNotSafe.jpg)


### MItigating wildcard certificate risks


The NSA recommends organizations make sure that wildcard certificates are used responsibly and their scope within the organization is well understood.


Companies should identify where the private keys for these certificates are stored and use the security level required by all apps in the certificates’ scope.


Using an application gateway or a Web Application Firewall (WAF) in front of servers, non-HTTP ones included, is another recommendation from the agency.


Encrypted DNS and validating DNS Security Extensions (DNSSEC) to prevent DNS redirection that could land target users in a malicious location.


The NSA also recommends enabling the Application-Layer Protocol Negotiation (ALPN) if this is possible, and keeping browsers updated to their latest version.




#### Tags:
[[NSA]] [[attacks.]] [[TLS]] [[app.example.com]] [[DNS]] [[Bleeping Computer]]
