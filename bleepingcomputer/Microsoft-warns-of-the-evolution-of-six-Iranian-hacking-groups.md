# Microsoft warns of the evolution of six Iranian hacking groups
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-the-evolution-of-six-iranian-hacking-groups/)
+ Date: November 16, 2021
+ Author: Bill Toulas


## Article:
![Iran Flag](https://www.bleepstatic.com/content/hl-images/2021/11/09/iran-flag-header.jpg)


The Microsoft Threat Intelligence Center (MSTIC) has presented an analysis of the evolution of several Iranian threat actors at the CyberWarCon 2021, and their findings show increasingly sophisticated attacks.


Since September 2020, Microsoft has been tracking six Iranian hacking groups deploying ransomware and exfiltrating data to cause disruption and destruction for victims.


Over time, these hacking groups have evolved into competent threat actors capable of conducting cyber-espionage, using multi-platform malware, disrupting operations with wipers and ransomware, carrying out phishing and password spraying attacks, and even setting up sophisticated supply chain operations.



![Timeline of Iranian actors' activity](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/ransomware_actors.jpg)**Timeline of Iranian actors' activity**  
*Source: Microsoft*
All of these groups deploy ransomware to achieve their objectives and were deployed in waves, usually six to eight weeks apart.


This year, Microsoft observed the actors scanning for many vulnerabilities, including those targeting Fortinet FortiOS SSL VPN, Microsoft Exchange Servers vulnerable to ProxyShell, and more.


It is estimated that by scanning for unpatched Fortinet VPN systems alone, the actors obtained over 900 valid credentials in plain text form so far this year.


Patient credential harvesting
-----------------------------


Another trend that has emerged this past year is an upgraded level of patience and persistence in social engineering campaigns, indicative of a sophisticated actor.


Previously, actors like Phosphorus (Charming Kitten) were sending unsolicited emails with malicious links and laced attachments, a bulk tactic that [had limited success](https://www.bleepingcomputer.com/news/security/microsoft-discovers-iranian-hacking-campaign-targeting-us-politics/).


Now, Phosphorus follows the time-consuming path of "interview invitations," a method ushered by the North Korean hacking group "Lazarus."


During these attacks, Phosphorus actors call the targets and walk them through clicking on credential harvesting pages as part of the interview process.


A new group that follows equally patient tactics is called "Curium," and Microsoft's analysts say this actor leverages an extensive network of fake social media accounts, usually masqueraded as attractive women.


They contact the targets and build rapport over some time, chatting daily and winning their trust.


Then, one day, they send a malicious document that looks similar to benign files sent previously, resulting in stealthy malware drops.


A similar tactic was used by the hacking group linked to Hamas, who [created fake dating apps to lure Israel Defence Forces](https://www.bleepingcomputer.com/news/security/hamas-lures-israeli-soldiers-to-malware-disguised-in-world-cup-and-dating-apps/) (IDF) into installing malware-laced mobile apps.


It is unclear if these two campaigns are linked.


Brute forcing a way in
----------------------


Although some actors move more methodically, others prefer to use "brute force" attacks to obtain access to Office 365 accounts aggressively.


One such threat actor is DEV-0343, who was seen [targeting US defense tech companies](https://www.bleepingcomputer.com/news/security/microsoft-iran-linked-hackers-target-us-defense-tech-companies/) and running massive password spraying attacks [last month](https://www.bleepingcomputer.com/news/microsoft/microsoft-warns-of-rise-in-password-sprays-targeting-cloud-accounts/).


Microsoft reports that DEV-0343 moves a lot quicker than the groups mentioned above, typically gaining access to the target accounts on the same day.


Also, the researchers have seen overlaps such as the simultaneous targeting of specific accounts by both DEV-0343 and 'Europium' operators, clear evidence of coordinated action.


Iranian hackers continue to evolve
----------------------------------


Microsoft has been tracking Iranian actors since almost a decade ago, and the tech giant has had some success in [taking parts of their infrastructure offline](https://www.bleepingcomputer.com/news/security/microsoft-retaliates-against-apt35-hacker-group-by-seizing-99-domains/).


Despite these efforts, Phosphorus has managed to deliver significant blows, with a notable example being the [hacking of high-ranking officials](https://www.bleepingcomputer.com/news/security/microsoft-iranian-attackers-hacked-security-conference-attendees/) in October last year.


MSTIC’s [most recent observations](https://www.microsoft.com/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021/) underline that Phosphorus is not only alive and well, but a shape-shifting threat backed by collaborators of unprecedented pluralism.




#### Tags:
[[Microsoft]] [[Bleeping Computer]]
