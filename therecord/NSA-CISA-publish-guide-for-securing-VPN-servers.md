# NSA, CISA publish guide for securing VPN servers
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/nsa-cisa-publish-guide-for-securing-vpn-servers/)
+ Date: September 28, 2021
+ Author: Catalin Cimpanu


## Article:
![NSA, CISA publish guide for securing VPN servers](https://therecord.media/wp-content/uploads/2021/09/server-data-center-router.jpg)

The National Security Agency (NSA) and the Cybersecurity and Infrastructure Security Agency (CISA) have published today technical guidance on properly securing VPN servers used by organizations to allow employees remote access to internal networks.


The NSA said it put together the nine-page guide [[PDF](https://media.defense.gov/2021/Sep/28/2002863184/-1/-1/0/CSI_SELECTING-HARDENING-REMOTE-ACCESS-VPNS-20210928.PDF)] after “multiple nation-state advanced persistent threat (APT) actors” weaponized vulnerabilities in common VPN servers as a way to breach organizations.


“Exploitation of these CVEs [*vulnerabilities*] can enable a malicious actor to steal credentials, remotely execute code, weaken encrypted traffic’s cryptography, hijack encrypted traffic sessions, and read sensitive data from the device,” the NSA said today in a [press release](https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/2791320/nsa-cisa-release-guidance-on-selecting-and-hardening-remote-access-vpns/) announcing the guide’s publication.


“If successful, these effects usually lead to further malicious access and could result in a large-scale compromise to the corporate network,” the agency added.


For example, Chinese, Iranian, and Russian state-sponsored groups have been spotted abusing vulnerabilities in Pulse Secure and Fortinet VPNs in campaigns that have taken place between 2019 and 2021.


Ransomware gangs such as Conti, Ryuk, REvil, DoppelPaymer, LockBit, and several others have also been spotted using VPN servers as their entry points into organizations before escalating access to internal networks and launching their file-encrypting attacks. Furthermore, cryptomining botnets have also abused VPN servers as a way to enter corporate networks and then compromise internal systems with hidden cryptocurrency mining software that exhausts computing resources for the attackers’ financial profits.


“Exploiting remote access VPNs can become a gateway to large-scale compromise,” Rob Joyce, Director of Cybersecurity at NSA, told The Record.


“We created guidance to help organizations understand what to look for when choosing VPNs and how to configure them to reduce the risk of being exploited. Use these recommendations to verify any VPNs are securely configured.”





The guide, which is expected to receive updates in the future as new issues and recommendations are discovered, contains advice on the following topics:


* Considerations for selecting remote access VPNs
* Directions on configuring strong cryptography and authentication
* Advice on reducing the VPN’s attack surface by running only strictly necessary features
* Guidance on protecting and monitoring access to and from the VPN


Today’s guidance release comes after the two agencies also released another joint guide on [hardening the security of Kubernetes clusters](https://therecord.media/nsa-cisa-publish-kubernetes-hardening-guide/) last month, in August 2021.





#### Tags:
[[VPN]] [[VPNs]] [[The Record]]
