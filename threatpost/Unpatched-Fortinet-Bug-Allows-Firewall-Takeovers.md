# Unpatched Fortinet Bug Allows Firewall Takeovers
### The OS command-injection bug, in the web application firewall (WAF) platform known as FortiWeb, will get a patch at the end of the month.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168764)
+ Date: August 18, 2021  8:07 am
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/05/18082749/Bug-Digital.jpg)
An unpatched OS command-injection security vulnerability has been disclosed in Fortinet’s web application firewall (WAF) platform, known as FortiWeb. It could allow privilege escalation and full device takeover, researchers said.


FortiWeb is a cybersecurity defense platform, [aimed at](https://www.fortinet.com/products/web-application-firewall/fortiweb) protecting business-critical web applications from attacks that target known and unknown vulnerabilities. The firewall has been to keep up with the deployment of new or updated features, or the addition of new web APIs, according to Fortinet.


The bug (CVE pending) exists in FortiWeb’s management interface (version 6.3.11 and prior), and carries a CVSSv3 base score of 8.7 out of 10, making it high-severity. It can allow a remote, authenticated attacker to execute arbitrary commands on the system, via the SAML server configuration page, according to Rapid7 researcher William Vu who discovered the bug.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“Note that while authentication is a prerequisite for this exploit, this vulnerability could be combined with another authentication-bypass issue, such as [CVE-2020-29015](https://www.fortiguard.com/psirt/FG-IR-20-124),” according to a [Tuesday writeup](https://www.rapid7.com/blog/post/2021/08/17/fortinet-fortiweb-os-command-injection/) on the issue.


Once attackers are authenticated to the management interface of the FortiWeb device, they can smuggle commands using backticks in the “Name” field of the SAML Server configuration page. These commands are then executed as the root user of the underlying operating system.


“An attacker can leverage this vulnerability to take complete control of the affected device, with the highest possible privileges,” according to the writeup. “They might install a persistent shell, crypto mining software, or other malicious software.”


The damage could be worse if the management interface is exposed to the internet: Rapid7 noted that attackers could pivot to the wider network in that case. However, Rapid7 researchers identified less than three hundred appliances that appeared to be doing so.


In the analysis, Vu provided a proof-of-concept exploit code, which uses an HTTP POST request and response.


Fortinet plans to release a fix for the problem with FortiWeb 6.4.1, which will be released at the end of August, it said.


“In the absence of a patch, users are advised to disable the FortiWeb device’s management interface from untrusted networks, which would include the internet,” according to Rapid7. “Generally speaking, management interfaces for devices like FortiWeb should not be exposed directly to the internet anyway — instead, they should be reachable only via trusted, internal networks, or over a secure VPN connection.”


The researchers said that the vulnerability appears to be related to [CVE-2021-22123](https://www.fortiguard.com/psirt/FG-IR-20-120), which was patched in June.


**Fortinet: Popular for Exploit**
---------------------------------


The vendor [is no stranger](https://threatpost.com/fortigate-vpn-default-config-mitm-attacks/159586/) to cybersecurity bugs in its platforms. And, Fortinet’s cybersecurity products are popular as exploitation avenues with cyberattackers, including nation-state actors.


In April, the FBI and the Cybersecurity and Infrastructure Security Agency (CISA) [warned that](https://threatpost.com/fbi-apts-actively-exploiting-fortinet-vpn-security-holes/165213/) various advanced persistent threats (APTs) were actively exploiting three security vulnerabilities in the Fortinet SSL VPN for espionage. Exploits for CVE-2018-13379, CVE-2019-5591 and CVE-2020-12812 were being used for to gain a foothold within networks before moving laterally and carrying out recon, they warned.


One of those bugs, a Fortinet vulnerability in FortiOS, [was also seen](https://threatpost.com/hackers-exploit-flaw-cring-ransomware/165300/) being used to deliver a new ransomware strain, dubbed Cring, that is targeting industrial enterprises across Europe.


Threatpost has reached out to Fortinet for comment.




#### Tags:
[[FortiWeb]] [[Fortinet]] [[cybersecurity]] [[Rapid7]] [[ThreatPost]]
