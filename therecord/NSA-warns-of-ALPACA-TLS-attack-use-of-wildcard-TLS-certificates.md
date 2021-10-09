# NSA warns of ALPACA TLS attack, use of wildcard TLS certificates
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/nsa-warns-of-alpaca-tls-attack-use-of-wildcard-tls-certificates/)
+ Date: October 8, 2021
+ Author: Catalin Cimpanu


## Article:
![NSA warns of ALPACA TLS attack, use of wildcard TLS certificates](https://therecord.media/wp-content/uploads/2021/10/Alpaca-attack.png)

* NSA urges NSS, DoD, and DIB administrators to use wildcard certificates responsibly.
* Agency also warns of recently disclosed ALPACA attack.
* More than 119,000 web servers were vulnerable to ALPACA attacks in June 2021.


**The National Security Agency has issued a technical advisory this week warning organizations against the use of wildcard TLS certificates and the new ALPACA TLS attack.**


The NSA urged organizations to follow the technical advice included in its [advisory](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/2804293/avoid-dangers-of-wildcard-tls-certificates-the-alpaca-technique/) and secure servers against scenarios where attackers could gain access and decrypt encrypted web traffic.


### The dangers of using wildcard TLS certificates


While there are many situations and attacks that could help attackers decrypt TLS-encrypted traffic, the NSA specifically highlighted the use of wildcard TLS certificates, something that multiple security researchers have also warned against throughout the years [[1](https://blog.nameshield.com/blog/2020/11/05/the-dangers-of-wildcard-certificates/), [2](https://www.venafi.com/blog/wildcard-certificates-make-encryption-easier-but-less-secure), [3](https://www.packetlabs.net/wildcard-certificates/), [4](https://blog.sean-wright.com/wildcard-certs-not-quite-the-star/), [5](https://gist.github.com/joepie91/7e5cad8c0726fd6a5e90360a754fc568), [6](https://www.tbs-certificates.co.uk/FAQ/en/205.html)].


Also known as a domain-validated certificate, a **wildcard certificate** is a digital TLS certificate obtained by companies from certificate authorities that allow the owner to apply it to a domain and all its subdomains at the same time (**.example.com*).


Throughout the years, companies have used wildcard certificates because of reduced costs and because they are easier to manage, as administrators can apply the same certificate across all servers instead of having to manage a different one for each subdomain.


However, this ease-of-use is also an Achilles’ heel, as once a threat actor compromises a server, they effectively compromise the entire company.


“A malicious cyber actor who gains control of the private key associated with a wildcard certificate will provide them the ability to impersonate any of the sites represented, and gain access to valid user credentials and protected information,” the NSA said on Thursday, echoing similar warnings issued by security researchers in the past.


The agency is now urging administrators of both public and private networks to assess the need to use a wildcard certificate inside their networks and prepare to deploy individual certificates in order to isolate and limit possible compromises.


### New ALPACA attack


In addition, the NSA’s advisory also comes with a warning about the new **Application Layer Protocol Content Confusion Attack** (ALPACA), which was disclosed earlier this summer, and which is also exploitable because of the use of wildcard certificates.


In a simple explanation, this attack allows a threat actor to confuse web servers that run multiple protocols to respond to encrypted HTTPS requests via unencrypted protocols, such as FTP, email (IMAP, POP3), and others.


A successful attack “can extract session cookies and other private user data or execute arbitrary JavaScript in the context of the vulnerable web server, therefore bypassing TLS and web application security,” according to the research team who discovered the ALPACA technique.


![alpaca-overview](https://www-therecord.recfut.com/wp-content/uploads/2021/10/alpaca-overview.png)Image: ALPACA Team
At the time it was disclosed in June, the issue was not taken seriously because executing an ALPACA attack required that threat actors be in a position to intercept web traffic, something that is difficult in some scenarios.


But the research team who discovered the attack said that [more than 119,000 web servers](https://alpaca-attack.com/) were vulnerable to ALPACA attacks, which was quite a considerable number.


Four months later, the NSA is urging organizations to take the matter seriously, check if their servers are vulnerable, and mitigate the risk, especially if the organizations deal with sensitive information or are part of the US government network.


While the NSA recommends several defenses, the agency is asking organizations to enable Application-Layer Protocol Negotiation (ALPN), which is a TLS extension that prevents servers from responding to requests via non-allowed protocols (such as FTP, IMAP, or whatever the server owner decides to disallow).


The move also comes after Google also implemented ALPACA defenses inside the Chrome web browser earlier this year.





“NSA recommends NSS, DoD, and DIB administrators ensure their organization’s wildcard certificate usage does not create unmitigated risks, making their web servers vulnerable to ALPACA techniques,” the NSA said on Thursday.





#### Tags:
[[NSA]] [[TLS]] [[The Record]]
