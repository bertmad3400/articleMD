# Microsoft: Iran-linked hackers target US defense tech companies
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-iran-linked-hackers-target-us-defense-tech-companies/)
+ Date: October 11, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft: Iran-linked hackers target US defense tech companies](https://www.bleepstatic.com/content/hl-images/2021/05/25/Iran-fingerprint_(1).jpg)


Iran-linked threat actors are targeting the Office 365 tenants of US and Israeli defense technology companies in extensive password spraying attacks.


In password spray attacks, threat actors attempt to brute-force accounts by using the same passwords across multiple accounts simultaneously, which allows them to hide failed attempts using different IP addresses.


This enables them to defeat automated defenses like password lockout and malicious IP blocking designed to block multiple failed login attempts.


The activity cluster was temporarily dubbed DEV-0343 by researchers at Microsoft Threat Intelligence Center (MSTIC) and Microsoft Digital Security Unit (DSU), who have tracked it since late July.


Attacks aligned with Iranian govt interests
-------------------------------------------


According to Microsoft, this ongoing malicious activity lines up with Iranian national interests based on techniques and targets aligning with another Iran-linked threat actor.


DEV-0343 was also linked to Iran based on pattern-of-life analysis and an extensive crossover in sectoral and geographic targeting with other Iranian hacking groups.


"Targeting in this DEV-0343 activity has been observed across defense companies that support United States, European Union, and Israeli government partners producing military-grade radars, drone technology, satellite systems, and emergency response communication systems,' Microsoft [says](https://www.microsoft.com/security/blog/2021/10/11/iran-linked-dev-0343-targeting-defense-gis-and-maritime-sectors/).


"Further activity has targeted customers in geographic information systems (GIS), spatial analytics, regional ports of entry in the Persian Gulf, and several maritime and cargo transportation companies with a business focus in the Middle East."


The DEV-0343 operators' end goal is likely to gain access to commercial satellite imagery and proprietary shipping plans and logs, which would be used to augment Iran's in-development satellite program.


Microsoft has directly notified customers that have been targeted or compromised, providing them with the information they need to secure their accounts.


Less than 20 targets breached
-----------------------------


Since the attacks have started, less than 20 targets have been compromised, with Microsoft noting that Office 365 accounts with multifactor authentication (MFA) toggled are resilient against DEV-0343's password spray attacks.


DEV-0343 targets the Autodiscover and ActiveSync Exchange endpoints with their enumeration/password spray tool to validate active accounts and refine their attacks.


"They typically target dozens to hundreds of accounts within an organization, depending on the size, and enumerate each account from dozens to thousands of times," Microsoft says.


"On average, between 150 and 1,000+ unique Tor proxy IP addresses are used in attacks against each organization."


How to defend against attacks
-----------------------------


Companies exposed to this activity are encouraged to look for DEV-0343 behaviors and tactics in logs and network activity, including:


* Extensive inbound traffic from Tor IP addresses for password spray campaigns
* Emulation of FireFox (most common) or Chrome browsers in password spray campaigns
* Enumeration of Exchange ActiveSync (most common) or Autodiscover endpoints
* Use of enumeration/password spray tool similar to the [‘o365spray’ tool](https://github.com/0xZDH/o365spray)
* Use of Autodiscover to validate accounts and passwords
* Observed password spray activity commonly peaking between 04:00:00 and 11:00:00 UTC


Microsoft recommends taking the following measures as a defense against DEV-0343's attacks:


* [Enable multifactor authentication](https://docs.microsoft.com/azure/active-directory/authentication/concept-mfa-howitworks) to mitigate compromised credentials.
	+ For Office 365 users, see [multifactor authentication support](https://docs.microsoft.com/office365/admin/security-and-compliance/set-up-multi-factor-authentication?view=o365worldwide).
	+ For Consumer and Personal email accounts, see [how to use two-step verification](https://support.microsoft.com/help/12408/microsoft-account-how-to-use-two-step-verification).
* Microsoft strongly encourages all customers to download and [use passwordless](https://www.microsoft.com/security/blog/2021/09/15/the-passwordless-future-is-here-for-your-microsoft-account/) solutions.
* Review and enforce recommended [Exchange Online access policies](https://docs.microsoft.com/microsoft-365/security/office-365-security/secure-email-recommended-policies):
	+ [Block ActiveSync clients from bypassing Conditional Access policies](https://docs.microsoft.com/microsoft-365/security/office-365-security/secure-email-recommended-policies?view=o365-worldwide#block-activesync-clients).
* Block all incoming traffic from anonymizing services where possible.


MSTIC and DSU researchers also shared Microsoft 365 Defender and Azure Sentinel advanced hunting queries [at the end of the blog post](https://www.microsoft.com/security/blog/2021/10/11/iran-linked-dev-0343-targeting-defense-gis-and-maritime-sectors/) to help SecOps teams to detect DEV-0343 related activity.




#### Tags:
[[DEV-0343]] [[Microsoft]] [[IP]] [[attacks.]] [[Autodiscover]] [[ActiveSync]] [[Bleeping Computer]]
