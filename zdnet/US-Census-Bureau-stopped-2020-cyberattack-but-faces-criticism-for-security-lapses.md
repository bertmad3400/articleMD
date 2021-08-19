# US Census Bureau stopped 2020 cyberattack but faces criticism for security lapses
### An OIG report said the Bureau routinely used end-of-life systems and wasted time in responding to the attack before it was stopped.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/us-census-bureau-stopped-202-cyberattack-but-faces-criticism-for-security-lapses/)
+ Date: August 18, 2021 -- 23:31 GMT (00:31 BST)
+ Author: Jonathan Greig


## Article:
Unknown

The Office of Inspector General (OIG) [has released a report](https://www.oig.doc.gov/OIGPublications/OIG-21-034-A.pdf) this week saying the US Census Bureau dealt with a cyberattack on January 11, 2020.

OIG investigators [reviewed the incident](https://www.oig.doc.gov/OIGPublications/OIG-21-034-A_Announcement.pdf) from November 2020 and March 2021, finding that while the Census Bureau was successful in stopping the attackers from gaining access to sensitive data, they left open a slate of vulnerabilities that hackers could have exploited.

The investigators found that servers operated by the Census Bureau -- which were in place to allow employees to access production, development, and lab networks remotely -- were attacked using a publicly available exploit. 

"According to system personnel, these servers did not provide access to 2020 decennial census networks. The exploit was partially successful, in that the attacker modified user account data on the systems to prepare for remote code execution," the report found.  

"However, the attacker's attempts to maintain access to the system by creating a backdoor into the affected servers were unsuccessful."

The attack was initially handled by the Department of Commerce's Enterprise Security Operations Center (ESOC), which manages security incidents and facilitates information sharing between the department, the Census Bureau and CISA. 

While commending the Bureau for stopping the attack, the OIG investigators found many other problems with how the incident was responded to and the way the Bureau used the servers. 






The report said the Bureau "missed opportunities to mitigate a critical vulnerability which resulted in the exploitation of vital servers." Even after the servers had been exploited, the Bureau did not discover and report the incident "in a timely manner."

"Additionally, the Bureau did not maintain sufficient system logs, which hindered the incident investigation. Following the incident, the Bureau did not conduct a lessons-learned session to identify improvement opportunities," the OIG report said. 

"We also found that the Bureau was operating servers that were no longer supported by the vendor. Since the January 2020 incident, the Bureau has made changes to its incident response program. By addressing the findings and recommendations in this report, the Bureau can continue to improve and have a more effective response to future cybersecurity incidents."

The Bureau had multiple opportunities to mitigate the vulnerability in its remote-access servers -- in December 2019 and January 2020. 

Investigators found that on December 17, 2019, Citrix, the vendor the Bureau worked with on the servers, released information about the vulnerability along with steps to mitigate it. 

NIST gave the vulnerability a severity rating of "critical" and a member of the Bureau's CIRT team attended security meetings with CISA where it was discussed. CISA even sent out a link for ways to mitigate the vulnerability.

The changes were not made until after the attack had been started. The attack would have failed if the Bureau had simply made the changes necessary, the OIG said. 

They noted that the Bureau was also not conducting vulnerability scanning of the remote-access servers and the servers were not even included in a list of devices to be scanned.

"This occurred because the system and vulnerability scanning teams had not coordinated the transfer of system credentials required for credentialed scanning," the report said, noting that while the attackers failed to gain access to systems, they still were able to create new user accounts. 

"The Bureau was not aware that the servers had been compromised until January 28, 2020, more than two weeks later. We found that this delay occurred because, at the time of the incident, the Bureau was not using a security information and event management tool (SIEM) to proactively alert incident responders of suspicious network traffic. Instead, the Bureau's SIEM was only being used for reactive, investigative actions."

The report said that by not using a SIEM to generate automated security alerts, it took the Bureau longer to confirm that the servers have been attacked. Their systems also failed to catch much of the attack at first.

The investigators found that one of the remote-access servers was trying to communicate to a malicious IP address outside of the Bureau's network and their SOC misidentified the direction of the malicious network traffic, concluding it had been blocked.

The OIG said this was a missed opportunity that was compounded by the failure of the ESOC to immediately share critical information about the exploited servers.

ESOC allegedly was contacted by CISA about the attack on January 16, 2020 but did not respond. CISA sent another notice on January 30 to investigate the issue, which was then forwarded by ESOC to other Bureau leaders. 

There were a number of other delays that they said "wasted time during the critical period following the attack." They urged the director of the US Census Bureau to ensure the CIO reviews automated alert capabilities on the Bureau's SIEM and develop procedures to handle alerts from outside entities like CISA. 

The Bureau also did not maintain sufficient system logs, hindering the investigation. A number of servers were configured to send system logs to a SIEM that had been decommissioned since July 2018. 

Even after migrating the capabilities of a number of remote access servers to new server hardware in September and December 2020, the report said investigators found in February 2021 that the Bureau was still running all of the original servers that were involved in the incident. All of the servers were operating past their end-of-life date which occurred on January 1, 2021. 

Despite the mistakes made, the Bureau's firewalls blocked the attacker's attempts to establish a backdoor to communicate with the attacker's external command and control infrastructure.

In a [letter attached to the report](https://www.oig.doc.gov/Pages/The-US-Census-Bureaus-Mishandling-of-a-January-2020-Cybersecurity-Incident-Demonstrated-Opportunities-for-Improvement.aspx), Acting Director of the US Census Bureau Ron Jarmin reiterated that there are "no indications of compromise on any 2020 Decennial Census systems nor any evidence of malicious behavior impacting the 2020 Decennial counts." 

"Furthermore, no system or data maintained and managed by the census bureau on behalf of the public were compromised, manipulated, or lost because of the incident highlighted in the OIG report," Jarmin said. 

His office noted that this was a "federal-wide incident that impacted numerous departments and agencies."

"The Census Bureau's response to this incident was in line with federal direction and response activities," Jarmin added. 

While they admitted to waiting too long to report the exploitation of the servers, they claimed they were waiting for further direction from CISA. 

In response to the criticisms about using legacy systems that needed to be decommissioned, the Census Bureau said in late 2020, they were working with Citrix engineers to migrate capabilities to new devices. 

"Due to circumstances outside the bureau's control -- including a dependency on Citrix engineers who were already at capacity supporting customers across the federal government who had realized greater impacts from the January 2020 attack, to complete the migration, and the COVID-19 pandemic -- the migration was delayed," Jarmin's office explained. 

Jarmin pledged to take end-of-life concerns more serious and said they have already made changes to how they respond to critical vulnerabilities and share information with other departments. They have also developed automated alerting capabilities and established information sharing procedures, Jarmin said.

The OIG report [suggested](https://www.oig.doc.gov/OIGPublications/OIG-21-034-A_Abstract.pdf) the Census Bureau introduce a slate of further changes to how vulnerability notifications are handled and how assets are scanned for vulnerabilities. They also said Bureau incident responders need to ensure that they comply with Departmental and Bureau requirements to report confirmed computer security incidents to ESOC within 1 hour.

But the report criticized the Bureau for not holding any kind of formal lessons-learned meeting, roundtable or talk after the attack at any level of the organization. 

"One incident responder stated that the team was consumed with responding to data requests from outside entities, which interfered with holding a lessons-learned session," the investigators said. 

"Furthermore, after reviewing Bureau incident response policies and procedures, we were unable to locate any requirement or guideline prescribing the timeframe in which to hold a lessons-learned session."

The Bureau said in a letter on July 19 that it concurred with all nine of OIG's recommendations and sent in plans to achieve all of them. 





#### Tags:
[[OIG]] [[Jarmin]] [[lessons-learned]] [[said.]] [[CISA]] [[SIEM]] [[CISA.]] [[incident,]] [[remote-access]] [[ESOC]] [[ZDNet]]
