# Fortinet delays patching zero-day allowing remote server takeover
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/fortinet-delays-patching-zero-day-allowing-remote-server-takeover/)
+ Date: August 17, 2021
+ Author: Sergiu Gatlan


## Article:
![Fortinet delays patching zero-day allowing remote server takeover](https://www.bleepstatic.com/content/hl-images/2021/04/07/Fortinet.jpg)


Fortinet has delayed patching a zero-day command injection vulnerability found in the FortiWeb web application firewall (WAF) until the end of August.


Successful exploitation can let authenticated attackers execute arbitrary commands as the root user on the underlying system via the SAML server configuration page.


While attackers must be authenticated to the management interface of the targeted FortiWeb device to abused this bug, they can easily chain it with other vulnerabilities such as the [CVE-2020-29015 authentication bypass](https://www.bleepingcomputer.com/news/security/fortinet-fixes-critical-vulnerabilities-in-ssl-vpn-and-web-firewall/) to take full control of vulnerable servers.


"An attacker can leverage this vulnerability to take complete control of the affected device, with the highest possible privilege," [Rapid7 explained](https://www.rapid7.com/blog/post/2021/08/17/fortinet-fortiweb-os-command-injection/).


"They might install a persistent shell, crypto mining software, or use the compromised platform to reach into the affected network beyond the DMZ."


The zero-day discovered by Rapid7 researcher William Vu impacts is yet to receive a CVE ID, and it impacts Fortinet FortiWeb versions 6.3.11 and earlier.


**To defend against attacks that would try to exploit this bug until a patch is available, admins are advised to block access to the FortiWeb device's management interface from untrusted networks (i.e., the Internet).**


Such devices should only be reachable via trusted, internal networks or a secure VPN connection to block threat actors' exploitation attempts.


Disclosure Timeline:
--------------------


* June 2021: Issue discovered and validated by William Vu of Rapid7
* Thu, Jun 10, 2021: Initial disclosure to the vendor via their PSIRT Contact Form
* Fri, Jun 11, 2021: Acknowledged by the vendor (ticket 132097)
* Wed, Aug 11, 2021: Followup with the vendor
* Tue, Aug 17, 2021: Public disclosure via [this post](https://www.rapid7.com/blog/post/2021/08/17/fortinet-fortiweb-os-command-injection/)
* Tue, Aug 17, 2021: Vendor indicated that Fortiweb 6.4.1 is expected to include a fix, and will be released at the end of August


Fortinet appliances are an attractive target
--------------------------------------------


Financially motivated and state-sponsored threat actors have been heavily targeting unpatched Fortinet servers over the years.


For instance, they have abused the CVE-2018-13379 Fortinet SSL VPN vulnerability [to compromise Internet-exposed U.S. election support systems](https://www.bleepingcomputer.com/news/security/hackers-used-vpn-flaws-to-access-us-govt-elections-support-systems/), with Fortinet warning customers to patch the flaw in [August 2019](https://www.fortinet.com/blog/business-and-technology/fortios-ssl-vulnerability), [July 2020](https://www.fortinet.com/blog/business-and-technology/atp-29-targets-ssl-vpn-flaws), [November 2020](https://www.fortinet.com/blog/psirt-blogs/update-regarding-cve-2018-13379), and again in [April 2021](https://urldefense.proofpoint.com/v2/url?u=https-3A__www.fortinet.com_blog_psirt-2Dblogs_patch-2Dvulnerability-2Dmanagement&d=DwMGaQ&c=tEbGsWWjqkBSpaWdXc_mdMSanI1bDu-FKXiKGCfVmPM&r=ci047yKZbNETIRLbYhPR9hvS9MgdS6HahLetj-MiY5k&m=S-tLJEaNHed7zOH8JaLd3mVoBNXqYMeUqJMrJaXLE9s&s=m_k7PDQ0L4L0_OvdKQgGF5LkRVde6Q9EjgVXWtyg7sY&e= "https://urldefense.proofpoint.com/v2/url?u=https-3A__www.fortinet.com_blog_psirt-2Dblogs_patch-2Dvulnerability-2Dmanagement&d=DwMGaQ&c=tEbGsWWjqkBSpaWdXc_mdMSanI1bDu-FKXiKGCfVmPM&r=ci047yKZbNETIRLbYhPR9hvS9MgdS6HahLetj-MiY5k&m=S-tLJEaNHed7zOH8JaLd3mVoBNXqYMeUqJMrJaXLE9s&s=m_k7PDQ0L4L0_OvdKQgGF5LkRVde6Q9EjgVXWtyg7sY&e=").


In November, a threat actor shared [a list of one-line CVE-2018-13379 exploits](https://www.bleepingcomputer.com/news/security/hacker-posts-exploits-for-over-49-000-vulnerable-fortinet-vpns/) that could've been used to steal VPN credentials for approximately 50,000 Fortinet VPN servers, including government entities and banks.


Earlier this year, [Fortinet fixed multiple vulnerabilities](https://www.bleepingcomputer.com/news/security/fortinet-fixes-critical-vulnerabilities-in-ssl-vpn-and-web-firewall/) impacting several of its products. The patched issues include Remote Code Execution (RCE), SQL Injection, and Denial of Service (DoS) bugs in FortiProxy SSL VPN and FortiWeb Web Application Firewall (WAF) products.


In April, the FBI and CISA [warned](https://www.bleepingcomputer.com/news/security/fbi-and-cisa-warn-of-state-hackers-attacking-fortinet-fortios-servers/) of state-sponsored hacking groups gaining access to Fortinet appliances by exploiting [CVE-2018-13379](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-13379), [CVE-2020-12812](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-12812), and [CVE-2019-5591](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5591) FortiOS vulnerabilities.


Kaspersky also revealed the same month that Fortinet VPNs are being exploited by a new human-operated ransomware strain known as Cring (aka Crypt3r, Vjiszy1lo, Ghost, Phantom) to [breach and encrypt industrial sector companies' networks](https://www.bleepingcomputer.com/news/security/new-cring-ransomware-hits-unpatched-fortinet-vpn-devices/).


One month later, the FBI issued a flash alert warning of [state-sponsored attackers breaching a US municipal government server](https://www.bleepingcomputer.com/news/security/fbi-apt-hackers-breached-us-local-govt-by-exploiting-fortinet-bugs/) after compromising a Fortinet FortiGate firewall appliance.


*Update: After this article was published, Fortinet sent the following statement:*



> 
> The security of our customers is always our first priority. Fortinet recognizes the important role of independent security researchers who work closely with vendors to protect the cybersecurity ecosystem in alignment with their responsible disclosure policies. In addition to directly communicating with researchers, our disclosure policy is clearly outlined on the [Fortinet PSIRT Policy page](https://www.fortiguard.com/psirt_policy "https://www.fortiguard.com/psirt_policy"), which includes asking incident submitters to maintain strict confidentiality until complete resolutions are available for customers. As such, we had expected that Rapid7 hold any findings prior to the end of the our [90-day Responsible disclosure window](https://www.fortiguard.com/zeroday/responsible-disclosure "https://www.fortiguard.com/zeroday/responsible-disclosure").  We regret that in this instance, individual research was fully disclosed without adequate notification prior to the 90-day window.  We are working to deliver immediate notification of a workaround to customers and a patch released by the end of the week.
> 
> 
> 




#### Tags:
[[Fortinet]] [[FortiWeb]] [[VPN]] [[Rapid7]] [[state-sponsored]] [[Bleeping Computer]]
