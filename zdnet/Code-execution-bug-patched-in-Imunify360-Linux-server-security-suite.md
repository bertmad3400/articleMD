# Code execution bug patched in Imunify360 Linux server security suite
### The vulnerability could be used to hijack web servers.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/code-execution-bug-patched-in-imunity360-linux-security-suite/)
+ Date: November 23, 2021
+ Author: Charlie Osborne


## Article:
Unknown

A severe PHP deserialization vulnerability leading to code execution has been patched in Imunify360. 


Discovered by [Cisco Talos](https://talosintelligence.com/vulnerability_reports/TALOS-2021-1383) researcher Marcin 'Icewall' Noga, the vulnerability "could cause a deserialization condition with controllable data and then execute arbitrary code," leaving web servers open to hijacking. 

Tracked as [CVE-2021-21956](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21956) and issued a CVSSv3 score of 8.2, the security flaw is present in CloudLinux's Imunify360 versions 5.8 and 5.9. [Imunify360](https://www.imunify360.com/) is a security suite for Linux web servers including patch management, domain blacklisting, and firewall features.  

In a security advisory published on Monday, Cisco Talos said the flaw was found in the Ai-Bolit malware scanner functionality of the software.  

The Ai-Bolit component is used to scan and check website-related files, such as .php, .js, or .html content, and is installed natively as a service with root privileges. Within a deobfuscation class of the module, a failure to sanitize data that has been submitted means that arbitrary code execution can be performed during unserialization.  

If the software is configured for real-time file system scanning, attackers could trigger an attack by creating a malicious file in the target server, or if a user is duped into performing a scan on a crafted payload file on behalf of the threat actor.  

Cisco reported its findings to the vendor on October 1 and coordinated public disclosure was agreed upon. Linux web developers making use of Imunify360 should upgrade their builds to the latest release, at the time of writing, [version 6.1](https://blog.imunify360.com/release-notes-imunify360-v.6.1-beta). 






ZDNet has reached out to the vendor and we will update when we hear back.  

###  Previous and related coverage

* [FBI warning: This zero-day VPN software flaw was exploited by APT hackers](https://www.zdnet.com/article/fbi-warning-this-zero-day-vpn-software-flaw-was-exploited-by-apt-hackers/)
* [Data from millions of Brazilians exposed in Wi-Fi management software firm leak](https://www.zdnet.com/article/millions-of-brazilians-exposed-in-wi-fi-management-software-firm-leak/)
* [Facebook's Meta pushes back Messenger and Instagram encryption plans until 2023](https://www.zdnet.com/article/facebooks-meta-pushes-back-messenger-and-instagram-encryption-plans-until-2023/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Imunify360]] [[ZDNet]]
