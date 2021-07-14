# Kaseya patches VSA vulnerabilities used in REvil ransomware attack
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/kaseya-patches-vsa-vulnerabilities-used-in-revil-ransomware-attack/)
+ Date: July 11, 2021
+ Author: Lawrence Abrams


## Article:
![Kaseya](https://www.bleepstatic.com/content/hl-images/2021/07/05/Kaseya__headpic.jpg)


Kaseya has released a security update for the VSA zero-day vulnerabilities used by the REvil ransomware gang to attack MSPs and their customers.


Kaseya VSA is a remote management and monitoring solution commonly used by managed service providers to support their customers. MSPs can deploy VSA on-premise using their servers or utilize Kaseya's cloud-based SaaS solution.



In April, the [Dutch Institute for Vulnerability Disclosure](https://csirt.divd.nl/) (DIVD) disclosed seven vulnerabilities to Kaseya:


* [CVE-2021-30116](https://csirt.divd.nl/cves/CVE-2021-30116) - A credentials leak and business logic flaw, to be included in 9.5.7
* [CVE-2021-30117](https://csirt.divd.nl/cves/CVE-2021-30117) - An SQL injection vulnerability, resolved in May 8th patch.
* [CVE-2021-30118](https://csirt.divd.nl/cves/CVE-2021-30118) - A Remote Code Execution vulnerability, resolved in April 10th patch. (v9.5.6)
* [CVE-2021-30119](https://csirt.divd.nl/cves/CVE-2021-30119) - A Cross Site Scripting vulnerability, to be included in 9.5.7
* [CVE-2021-30120](https://csirt.divd.nl/cves/CVE-2021-30120) - 2FA bypass, to be resolved in v9.5.7
* [CVE-2021-30121](https://csirt.divd.nl/cves/CVE-2021-30121) - A Local File Inclusion vulnerability, resolved in May 8th patch.
* [CVE-2021-30201](https://csirt.divd.nl/cves/CVE-2021-30201) - A XML External Entity vulnerability, resolved in May 8th patch.


Kaseya had implemented patches for most of the vulnerabilities on their VSA SaaS service but had not completed the patches for the on-premise version of VSA.


Unfortunately, the REvil ransomware gang beat Kaseya to the finish line and utilized these vulnerabilities to [launch a massive attack](https://www.bleepingcomputer.com/news/security/revil-ransomware-hits-1-000-plus-companies-in-msp-supply-chain-attack/) on July 2nd against approximately 60 MSPs using on-premise VSA servers and 1,500 business customers.


It is unclear which vulnerabilities were used in the attack, but it is believed to be one or a combination of CVE-2021-30116, CVE-2021-30119, and CVE-2021-30120.


Kaseya releases security updates
--------------------------------


Since the attack, Kaseya has urged on-premise VSA customers to shut down their servers until a patch is ready.


Almost ten days after the attacks, Kaseya has [released the VSA 9.5.7a (9.5.7.2994) update](https://helpdesk.kaseya.com/hc/en-gb/articles/4403785889041) to fix the vulnerabilities used in the REvil ransomware attack.


With this release, Kaseya has fixed the following vulnerabilities:


* Credentials leak and business logic flaw: [CVE-2021-30116](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30116)
* Cross Site Scripting vulnerability: [CVE-2021-30119](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30119)
* 2FA bypass: [CVE-2021-30120](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30120)
* Fixed an issue where secure flag was not being used for User Portal session cookies.
* Fixed an issue where certain API responses would contain a password hash, potentially exposing any weak passwords to brute force attack. The password value is now masked completely.
* Fixed a vulnerability that could allow unauthorized upload of files to the VSA server.


However, Kaseya is urging customers to follow the '[On Premises VSA Startup Readiness Guide](https://helpdesk.kaseya.com/hc/en-gb/articles/4403709150993incident-response)' steps before installing the update to prevent further breaches and make sure devices are not already compromised.


Below are the basic steps that admins should perform before starting up VSA servers again and connecting them to the Internet:


* Ensure your VSA server is isolated
* Check System for Indicators of Compromise (IOC)
* Patch the Operating Systems of the VSA Servers
* Using URL Rewrite to control access to VSA through IIS
* Install FireEye Agent
* Remove Pending Scripts/Jobs


Of these steps, it is critical that on-premise VSA servers not be publicly accessible from the Internet to prevent compromise while installing the patch.


Kaseya also urges customers to utilize their "Compromise Detection Tool," a collection of PowerShell scripts to detect whether a VSA server or endpoints have been compromised.


The scripts will check VSA servers for the presence of 'Kaseya\webpages\managedfiles\vsaticketfiles\agent.crt' and 'Kaseya\webpages\managedfiles\vsaticketfiles\agent.exe,' and 'agent.crt' and 'agent.exe' on endpoints. 


The REvil affiliate used the agent.crt and agent.exe files to deploy the REvil ransomware executable.


For additional security, Kaseya is also suggesting on-premise VSA admin restrict access to the web GUI to local IP addresses and those known to be used by security products.


"For VSA On-Premises installations, we have recommended limiting access to the VSA Web GUI to local IP addresses by blocking port 443 inbound on your internet firewall.  Some integrations may require inbound access to your VSA server on port 443.  Below are a list of IP addresses you can whitelist in your firewall (allow 443 inbound to FROM ), if you are using these integrations with your VSA On-Premises product." [explains](https://helpdesk.kaseya.com/hc/en-gb/articles/4403869952657) Kaseya.


After installing the patch, all users will be required to change their password to one using new password requirements.




#### Tags:
[[VSA]] [[Kaseya]] [[-]] [[on-premise]] [[REvil]] [[ransomware]] [[MSPs]] [[CVE-2021-30116]] [[5]] [[8th]] [[Bleeping Computer]]
