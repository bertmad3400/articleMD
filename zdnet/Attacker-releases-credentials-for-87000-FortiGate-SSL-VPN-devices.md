# Attacker releases credentials for 87,000 FortiGate SSL VPN devices
### Access data for FortiGate devices was obtained by exploiting a known, old vulnerability.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/attacker-releases-credentials-for-87000-fortigate-ssl-vpn-devices/)
+ Date: September 9, 2021 -- 11:18 GMT (12:18 BST)
+ Author: Charlie Osborne


## Article:
Unknown

Fortinet has warned that 87,000 sets of credentials for FortiGate SSL VPN devices have been published online. 


The California-based cybersecurity firm said [on Wednesday](https://www.fortinet.com/blog/psirt-blogs/malicious-actor-discloses-fortigate-ssl-vpn-credentials) that it is aware of the disclosure, and after investigating the incident, has come to the conclusion that the credentials have been obtained by exploiting CVE-2018-13379. 

[CVE-2018-13379](https://www.fortiguard.com/psirt/FG-IR-18-384) is a known security flaw impacting the FortiOS SSL VPN web tunnel software's portal. The bug was patched and a fix was released in 2019, including two-factor authentication mitigation. However, close to two years on, the vulnerability has now come back to the fore with the release of stolen credentials online.  

Fortinet says that the stolen information was "obtained from systems that remained unpatched" at the time an attacker performed a web scan for vulnerable devices. 

If passwords for FortiOS SSL VPN builds have not been changed since this scan, Fortinet says they remain vulnerable to compromise. Furthermore, as FortiOS SSL VPN is popular with enterprise users, this could become an avenue for network attacks.  

"Please note that a password reset following upgrade is critical to protecting against this vulnerability, in case credentials have already been compromised," the company says.

CVE-2018-13379 was reported by Meh Chang and Orange Tsai [from DEVCORE](https://blog.orange.tw/2019/08/attacking-ssl-vpn-part-2-breaking-the-fortigate-ssl-vpn.html). Described as a path traversal flaw, the bug permits unauthenticated attackers to download system files through special crafted HTTP resource requests. The critical vulnerability was awarded [a CVSS score](https://nvd.nist.gov/vuln/detail/CVE-2018-13379) of 9.8. 






FortiOS 6.0 - 6.0.0 to 6.0.4, FortiOS 5.6 - 5.6.3 to 5.6.7, and FortiOS 5.4 - 5.4.6 to 5.4.12 are impacted by the bug and are vulnerable when the SSL VPN service has been enabled.  

As noted by [AdvIntel](https://www.advintel.io/post/groove-vs-babuk-groove-ransom-manifesto-ramp-underground-platform-secret-inner-workings), that the dump was posted by the Groove ransomware group on their leak site. The threat actors said, 'everything checked as valid,' (Russian, translated) but this has not been verified. 

![screenshot-2021-09-09-at-12-15-22.png]()![screenshot-2021-09-09-at-12-15-22.png](https://www.zdnet.com/a/hub/i/r/2021/09/09/cd0b7e99-5964-49bd-9011-257fe4aa21dc/resize/1200xauto/e9b8b6e8dd92d96adedd79ace54a8d80/screenshot-2021-09-09-at-12-15-22.png)
 via Kela
 The company has previously warned customers that this vulnerability is being weaponized by hacking groups in the wild ([1](https://www.fortinet.com/blog/psirt-blogs/atp-29-targets-ssl-vpn-flaws),[2](https://www.fortinet.com/blog/psirt-blogs/patch-vulnerability-management)). In June, the FBI issued [an advisory](https://www.ic3.gov/Media/News/2021/210527.pdf) (.PDF) stating that CVE-2018-13379 had been successfully used to infiltrate a webserver hosting a US municipal government domain.

"Since these vulnerabilities were first discovered, Fortinet has taken exhaustive steps to notify and educate customers, urging them repeatedly to upgrade their affected systems to the latest patch release," the company [said in June](https://www.fortinet.com/blog/psirt-blogs/prioritizing-patching-is-essential-for-network-integrity). "It's a scenario software and firmware developers know all too well. Fortinet and organizations like the NCSC, FBI, and CISA have issued 15 separate notifications and advisories to Fortinet customers over the past two years, warning them of the risks of failing to update affected systems and providing links to critical patches."

If users suspect they may have been involved in the breach due to a failure to refresh their credentials, the tech giant recommends that VPN services are temporarily disabled while organizations perform password resets.  

Fortinet is also urging customers to upgrade to FortiOS 5.4.13, 5.6.14, 6.0.11, or 6.2.8 and above, which contain the necessary security fixes.  

###  Previous and related coverage

* [Patch released for Fortinet command injection vulnerability](https://www.zdnet.com/article/patch-released-for-fortinet-command-injection-vulnerability/)  

* [This is the perfect ransomware victim, according to cybercriminals](https://www.zdnet.com/article/this-is-the-perfect-ransomware-victim-according-to-cybercriminals/)  

* [Accenture says Lockbit ransomware attack caused 'no impact'](https://www.zdnet.com/article/accenture-says-lockbit-ransomware-attack-caused-no-impact-on-operations-or-clients/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Fortinet]] [[FortiOS]] [[VPN]] [[SSL]] [[ransomware]] [[ZDNet]]
