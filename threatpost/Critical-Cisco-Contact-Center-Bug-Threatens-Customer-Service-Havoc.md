# Critical Cisco Contact Center Bug Threatens Customer-Service Havoc
### Attackers could access and modify agent resources, telephone queues and other customer-service systems – and access personal information on companies’ customers.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177681
+ Date: 2022-01-14T16:37:13+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/14112707/customer-service-e1642177641219.jpg)

A critical security bug affecting Cisco’s Unified Contact Center Enterprise (UCCE) portfolio could allow privilege-escalation and platform takeover.


Cisco UCCE is an on-premises customer-service platform [capable of](https://www.cisco.com/c/en/us/products/contact-center/unified-contact-center-enterprise/index.html) supporting up to 24,000 customer-service agents using channels that include inbound voice, outbound voice, outbound interactive voice response (IVR) and digital channels. It also offers a feedback loop via post-call IVR, email and web intercept surveys; and various reporting options to gather information on agent performance to use in establishing metrics and informing business intelligence.


It counts some heavy hitters among its users, including T-Mobile USA, according to the product website.


The bug in question (CVE-2022-20658) is a particularly nasty one, with a critical rating of 9.6 out of 10 on the CVSS vulnerability-severity scale, and could allow authenticated, remote attackers to elevate their privileges to administrator, with the ability to create other administrator accounts.


It specifically exists in the web-based management interface of Cisco Unified Contact Center Management Portal (Unified CCMP) and Cisco Unified Contact Center Domain Manager (Unified CCDM) and stems from the fact that the server relies on authentication mechanisms handled by the client side. That opens the door to an attacker modifying the client-side behavior to bypass protection mechanisms.


The CCMP is [a management tool](https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/unified-contact-center-enterprise/data_sheet_c78-713333.html) that gives contact-center supervisors the ability to move, add and change agents working in different areas of the contact center between different call queues, brands, product lines and more. The CCDM is a suite of server components ([PDF](https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/CCDM_Documents/CCDM125_Administration_Guide.pdf)) for back-end management, including authentication and other security functions, resource allocation, and a database that holds information about all the resources (such as agents and dialed numbers) and actions taken (such as phone calls and agent state changes) within the system.


Armed with additional admin accounts, attackers could access and modify telephony and user resources across all of platforms that are associated to the vulnerable Cisco Unified CCMP, Cisco warned. One can extrapolate the operational and brand-identity havoc that an attacker could wreak by hamstringing a major company’s customer-service systems – not to mention the damage that could be done with access to the data trove of personal information that the system must house on companies’ customers, including phone and email communications.


It’s also not hard to exploit: “This vulnerability is due to the lack of server-side validation of user permissions,” Cisco explained [in an advisory](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ccmp-priv-esc-JzhTFLm4) this week. “An attacker could exploit this vulnerability by submitting a crafted HTTP request to a vulnerable system.”


However, to successfully exploit the vulnerability, attackers would need valid “Advanced User” credentials, so the bug would need to be chained with another for initial access.


There are patches available for this issue, but not work-arounds. Patch information is as follows:


* Versions 11.6.1 and earlier: Fixed release is 11.6.1 ES17
* Version 12.0.1: Fixed release is 12.0.1 ES5
* Version 12.5.1: Fixed release is 12.5.1 ES5
* Version 12.6.1: Not affected


There are no known public exploits thus far, according to the networking giant.


Cisco’s contact-center solutions have faced critical bugs before. For instance, in 2020 a critical bug in its “contact center in-a-box” platform, Unified Contact Center Express, [was found to allow](https://threatpost.com/critical-cisco-rce-flaw-unified-ccx/155980/) remote code-execution.


***Password******Reset:******[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):*** *Fortify 2022 with a password-security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken.****[Register & stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)****– sponsored by Specops Software.*


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Customer-service]] [[ThreatPost]]
#### CVE's
[[CVE-2022-20658]]

