# Get patching: Cisco warns of these critical product vulnerabilities
### Cisco and CISA release alerts about multiple vulnerabilities that could provide attackers with the ability to takeover networks if they're left unpatched.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/get-patching-cisco-warns-of-these-critical-product-vulnerabilities/)
+ Date: November 5, 2021
+ Author: Danny Palmer


## Article:
Unknown

Cisco has released security updates to fix vulnerabilities in multiple products that, if left unpatched, could allow an attacker to take control of affected systems and give them the ability to perform a variety of malicious actions.

The newly disclosed critical security vulnerabilities affect Cisco Policy Suite Static SSH Keys and Cisco Cisco Catalyst PON Series Switches Optical Network Terminals. The US Cybersecurity & Infrastructure Security Agency (CISA) has urged users and administrators to [review the Cisco advisories and apply the necessary updates](https://us-cert.cisa.gov/ncas/current-activity/2021/11/04/cisco-releases-security-updates-multiple-products).


[Cisco Policy Suite](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cps-static-key-JmS92hNv) – a software package for data management – contains a vulnerability ([CVE-2021-40119](https://nvd.nist.gov/vuln/detail/CVE-2021-40119)) in the key of its Secure Shell (SHH) cryptographic network authentication mechanism, which could allow an unauthenticated, remote attacker to login to unpatched systems as the root user. 

****SEE:**[**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/)**(ZDNet special report)****

This ability could provide them with unrestricted permissions to access, read and write files, something that is extremely desirable for attackers looking to access data, install [malware](https://www.zdnet.com/article/what-is-malware-everything-you-need-to-know-about-viruses-trojans-and-malicious-software/) or perform other malicious activities.

There are also two critical security vulnerabilities in Cisco Catalyst Passive Optical Network (PON) Series Switches Optical Network Terminals that are used to help deliver deliver internet access to multiple endpoints on a single network. 

The vulnerabilities ([CVE-2021-34795](https://nvd.nist.gov/vuln/detail/CVE-2021-34795) and [CVE-2021-40112](https://nvd.nist.gov/vuln/detail/CVE-2021-40112)) in the web-based management interface of [Cisco PON terminals](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-catpon-multivulns-CE3DSYGr) could allow an unauthenticated, remote attacker to login with default credentials if Telnet – a network protocol used to virtually access a computer for collaboration and communications channels – is enabled. 






These vulnerabilities also allow attackers to perform command injections and modify configurations, both of which could be exploited for malicious actions.

The specific Cisco products vulnerable to CVE-2021-34795 and CVE-2021-40112 are:

* Catalyst PON Switch CGP-ONT-1P
* Catalyst PON Switch CGP-ONT-4P
* Catalyst PON Switch CGP-ONT-4PV
* Catalyst PON Switch CGP-ONT-4PVC
* Catalyst PON Switch CGP-ONT-4TVCW

By default, Cisco PON Series Switches only allow local LAN connections to the web management interface, so they're only exploitable if remote web management has been enabled. 

Users are urged to visit [Cisco Security Advisories](https://tools.cisco.com/security/center/publicationListing.x) as soon as possible in order to download the security patches required to fix the vulnerabilities.

**SEE:** [**Ransomware: It's a 'golden era' for cyber criminals - and it could get worse before it gets better**](https://www.zdnet.com/article/ransomware-its-a-golden-era-for-cyber-criminals-and-it-could-get-worse-before-it-gets-better/)

[Unpatched vulnerabilities](https://www.zdnet.com/article/this-one-change-could-protect-your-systems-from-attack-so-why-dont-more-companies-do-it/) are one of the most common methods cyber criminals, nation state-backed hacking operations and other malicious operations exploit in order to enter networks.

But despite cybersecurity organisations like CISA stressing the importance of patching networks, [it's still common for attackers to be able to exploit years-old vulnerabilities](https://www.zdnet.com/article/ransomware-cyber-criminals-are-still-exploiting-years-old-vulnerabilities-to-launch-attacks/) to gain access to networks because, in many cases, the updates aren't being applied. 

### **MORE ON CYBERSECURITY**

* [**CISA passes directive forcing federal civilian agencies to fix 306 vulnerabilities**](https://www.zdnet.com/article/cisa-passes-directive-forcing-federal-civilian-agencies-to-fix-306-vulnerabilities/)
* [**Ransomware: Now attackers are exploiting Windows PrintNightmare vulnerabilities**](https://www.zdnet.com/article/ransomware-now-attackers-are-exploiting-windows-printnightmare-vulnerabilities/)
* [**Businesses don't talk about being victims of cyberattacks. That needs to change**](https://www.zdnet.com/article/businesses-dont-talk-about-being-victims-of-cyberattacks-that-needs-to-change/)
* [**Cybersecurity warning: Russian hackers are targeting these vulnerabilities, so patch now**](https://www.zdnet.com/article/cybersecurity-warning-russian-hackers-are-targeting-these-vulnerabilities-so-patch-now/)
* [**Cloud security in 2021: A business guide to essential tools and best practices**](https://www.zdnet.com/article/cloud-security-in-2021-a-business-guide-to-essential-tools-and-best-practices/)





#### Tags:
[[]] [[ZDNet]]
