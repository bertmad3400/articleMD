# Microsoft warns over password attacks against 250 Office 365 customers
### Another good reason to turn on multi-factor authentication now.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-warns-over-password-attacks-against-250-office-365-customers/)
+ Date: October 12, 2021
+ Author: Liam Tung


## Article:
Unknown

Microsoft says 250 Office 365 customers in the US and Israeli defense technology sector have bee targeted with 'password-spraying' attacks, where attackers try to access many accounts with commonly used passwords. The technique [relies on people using variations of common passwords](https://www.zdnet.com/article/microsoft-just-took-another-big-step-towards-getting-rid-of-passwords-forever/). 

The password attacks focussed on critical infrastructure companies operating in the Persian Gulf and were carried out by a group Microsoft is tracking as DEV-0343 – most likely a new group from Iran.  


The 'DEV' tag indicates that the group is not a confirmed state-sponsored attack group, but it could become one eventually. 

**SEE:** [**BYOD security warning: You can't do everything securely with just personal devices**](https://www.zdnet.com/article/byod-security-warning-you-cant-do-everything-securely-with-personal-devices-says-cybersecurity-body/)

The Microsoft Threat Intelligence Center (MSTIC) said it had observed DEV-0343 "conducting extensive password spraying against more than 250 Office 365 tenants, with a focus on US and Israeli defense technology companies, Persian Gulf ports of entry, or global maritime transportation companies with business presence in the Middle East."

Microsoft said "less than 20" of the targeted tenants were successfully compromised.

The risk of compromise from password-spraying attacks is significantly reduced for organizations that roll out multi-factor authentication.    






The hacking group targeted companies that support US, European Union and Israeli organizations producing military radars, drones, satellite systems, and emergency response communication systems, as well as geographic information systems (GIS), spatial analytics, Persian Gulf ports, and maritime and cargo transportation companies in the region.

"Microsoft assesses this targeting supports Iranian government tracking of adversary security services and maritime shipping in the Middle East to enhance their contingency plans. Gaining access to commercial satellite imagery and proprietary shipping plans and logs could help Iran compensate for its developing satellite program," [Microsoft said](https://www.microsoft.com/security/blog/2021/10/11/iran-linked-dev-0343-targeting-defense-gis-and-maritime-sectors/). 

Microsoft last week raised a red flag over Russian state-sponsored hacking, labelling Russia's [intelligence hackers the most active cyber threat in the world](https://www.zdnet.com/article/russia-poses-the-biggest-nation-state-cyber-threat-says-microsoft/). Not only are Kremlin-backed hackers more prolific, they're also increasingly effective, according to Microsoft. It also flagged a significant uptick in Iranian hacks against Israeli organizations. 

"This year marked a near quadrupling in the targeting of Israeli entities, a result exclusively of Iranian actors, who focused on Israel as tensions sharply escalated between the adversaries," Microsoft noted in its latest Digital Defense Report.

Its latest warning to US and Israeli organizations operating in the Middle East says they should be on the lookout for suspicious Tor connections to their networks. 


"DEV-0343 conducts extensive [password sprays](https://www.microsoft.com/security/blog/2020/04/23/protecting-organization-password-spray-attacks/) emulating a Firefox browser and using IPs hosted on a Tor proxy network. They are most active between Sunday and Thursday between 7:30 AM and 8:30 PM Iran Time (04:00:00 and 17:00:00 UTC) with significant drop-offs in activity before 7:30 AM and after 8:30 PM Iran Time. They typically target dozens to hundreds of accounts within an organization, depending on the size, and enumerate each account from dozens to thousands of times. On average, between 150 and 1,000+ unique Tor proxy IP addresses are used in attacks against each organization," [Microsoft warned in a blogpost](https://www.microsoft.com/security/blog/2021/10/11/iran-linked-dev-0343-targeting-defense-gis-and-maritime-sectors/). 

**SEE:** [**Microsoft's Windows 11: How to get it now (or later)**](https://www.zdnet.com/article/microsofts-windows-11-how-to-get-it-now-or-later/)

DEV-0343 frequently targets the Exchange endpoints, including Autodiscover and ActiveSync, with password-spraying attacks. This allows DEV-0343 to validate active accounts and passwords, and further refine its password-spray activity, Microsoft said.

Microsoft's primary recommended defense is enabling multi-factor authentication since this should block remote access to accounts with compromised credentials. 

It also recommends admins check and enforce Exchange Online access policies and to block all incoming traffic coming from services like the Tor network. 





#### Tags:
[[Microsoft]] [[DEV-0343]] [[ZDNet]]
