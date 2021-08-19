# Postmortem on U.S. Census Hack Exposes Cybersecurity Failures
### Government says cybersecurity failures were many within failed January hack of U.S. Census Bureau systems. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168814)
+ Date: August 19, 2021  10:35 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/19103444/people-population-security.jpg)
Threat actors exploited an [unpatched Citrix flaw](https://threatpost.com/unpatched-citrix-flaw-exploits/151748/) to breach the network of the U.S. Census Bureau in January in an attack that was ultimately halted before a backdoor could be installed or sensitive data could be stolen, according [to a report](https://www.oig.doc.gov/OIGPublications/OIG-21-034-A.pdf) by a government watchdog organization.


However, investigators found that officials were informed of the flaw in its servers and had at least two opportunities to fix it before the attack, mainly due to lack of coordination between teams responsible for different security tasks, according to the report, published Tuesday by the U.S. Department of Commerce Office of Inspector General. The bureau also lagged in its discovery and reporting of the attack after it happened.


The report details and reviews the incident that occurred on Jan. 11, 2020, when attackers used the publicly available exploit for a critical flaw to target remote-access servers operated by the bureau.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

Citrix released a public notice about the zero-day flaw—tracked as [CVE-2019-19781](https://nvd.nist.gov/vuln/detail/CVE-2019-19781)–in December. In January, a representative from the bureau’s Computer Incident Response Team (CIRT\_ attended two meetings in which the flaw was discussed and attendees even received a link to steps to use fixes which already had been issued by Citrix.


“Despite the publicly available notices released in December and attending two meetings on the issue in January, the bureau CIRT did not coordinate with the team responsible for implementing these mitigation steps until after the servers had been attacked,” according to the report. Doing so could have prevented the attack, investigators noted.


**‘Partially Successful’ Attack**
---------------------------------


The Citrix products affected by the flaw–[discovered](https://threatpost.com/critical-citrix-bug-80000-corporate-lans-at-risk/151444/) by Mikhail Klyuchnikov, a researcher at Positive Technologies—are used for application-aware traffic management and secure remote access, respectively. At least 80,000 organizations in 158 countries—about 38 percent in the U.S.—use these products, formerly called NetScaler ADC and Gateway.


The initial compromise at the Census Bureau was on servers used to provide the bureau’s enterprise staff with remote-access capabilities to production, development and lab networks. The servers did not provide access to 2020 decennial census networks, officials told investigators.


“The exploit was partially successful, in that the attacker modified user account data on the systems to prepare for remote code execution,” according to the report. “However, the attacker’s attempts to maintain access to the system by creating a backdoor into the affected servers were unsuccessful.”


Attackers were able to make unauthorized changes to the remote-access servers, including the creation of new user accounts, investigators reported. However, the bureau’s firewalls blocked the attacker’s attempts to establish a backdoor to communicate with the attacker’s external command and control infrastructure.


**Other Mistakes**
------------------


Another security misstep the bureau took that could have mitigated the attack before it even happened was that it was not conducting vulnerability scanning of the remote-access servers as per federal standards and Commerce Department policy, according to the OIG.


“We found that the bureau vulnerability scanning team maintained a list of devices to be scanned,” investigators wrote. “However, the remote-access servers were not included on the list, and were therefore not scanned. This occurred because the system and vulnerability scanning teams had not coordinated the transfer of system credentials required for credentialed scanning.”


The bureau also made mistakes after the attack by not discovering nor reporting the incident in a timely manner, the OIG found.


IT administrators were not aware that servers were compromised until Jan. 28, more than two weeks after the attack, because the bureau was not using a a security information and event management tool (SIEM) to proactively alert incident responders of suspicious network traffic, investigators found.




#### Tags:
[[remote-access]] [[Citrix]] [[attack,]] [[bureau’s]] [[attacker’s]] [[ThreatPost]]
