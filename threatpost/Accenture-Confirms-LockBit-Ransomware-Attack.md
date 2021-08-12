# Accenture Confirms LockBit Ransomware Attack
### LockBit offered Accenture’s purported databases and made a requisite jab at its purportedly sad security. Accenture says it recovered just fine from backups.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168594)
+ Date: August 11, 2021  5:56 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/11175256/LockBit-screen-grab-e1628718789810.png)
The LockBit ransomware-as-a-service (RaaS) gang has published the name and logo of what’s purportedly one of its latest victims: Accenture, the global business consulting firm with an insider track on some of the world’s biggest, most powerful companies.


Accenture’s clients include 91 of the Fortune Global 100 and more than three-quarters of the Fortune Global 500. According to its [2020 annual report;](https://www.accenture.com/us-en/about/company/annual-report) that includes e-commerce giant Alibaba, Cisco and Google. Valued at $44.3 billion, Accenture is one of the world’s largest tech consultancy firms, and employs around 569,000 people across 50 countries.


In a post on its Dark Web site, LockBit offered up Accenture databases for sale, along with a requisite jab at what the gang deemed to be Accenture’s pathetic security.



> “These people are beyond privacy and security. I really hope that their services are better than what I saw as an insider. If you are interested in buying some databases, reach us.”  
> 
> —LockBit site post.
> 
> 


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


According to [Security Affairs](https://securityaffairs.co/wordpress/121048/data-breach/accenture-lockbit-2-0-ransomware-attack.html?utm_source=rss&utm_medium=rss&utm_campaign=accenture-lockbit-2-0-ransomware-attack), at the end of a ransom payment clock’s countdown, a leak site showed a folder named W1 that contained a collection of PDF documents allegedly stolen from the company. LockBit operators claimed to have gained access to Accenture’s network and were preparing to leak files stolen from Accenture’s servers at 17:30:00 GMT.


The news hit the headlines late Wednesday morning Eastern Time, after CNBC reporter Eamon Javers [tweeted](https://twitter.com/EamonJavers/status/1425476619934838785) about the gang’s claim that it would be releasing data within coming hours and that it was offering to sell insider Accenture information to interested parties.



Blessed Be the Backups
----------------------


Yes, we were hit, but we’re A-OK now, Accenture confirmed: “Through our security controls and protocols, we identified irregular activity in one of our environments. We immediately contained the matter and isolated the affected servers,” it said in a statement. “We fully restored our affected systems from backup, and there was no impact on Accenture’s operations, or on our clients’ systems.”


According to [BleepingComputer](https://www.bleepingcomputer.com/news/security/accenture-confirms-hack-after-lockbit-ransomware-data-leak-threats/), the group that threatened to publish Accenture’s data – allegedly stolen during a recent cyberattack – is known as LockBit 2.0.


As explained by Cybereason’s Tony Bradley in a Wednesday [post](https://www.cybereason.com/blog/rising-threat-from-lockbit-ransomware), the LockBit gang is similar to its ransomware-as-a-service (RaaS) brethren DarkSide and REvil: Like those other operations. LockBit uses an affiliate model to rent out its ransomware platform, taking a cut of any ransom payments that result.


Bradley noted that the LockBit gang is apparently on a hiring spree in the wake of [DarkSide](https://threatpost.com/darksides-servers-shutdown/166187/) and [REvil](https://threatpost.com/whats-next-revil-victims/167926/) both shutting down operations.


“The wallpaper displayed on compromised systems now includes text inviting insiders to help compromise systems – promising payouts of millions of dollars,” Bradley wrote.


Insider Job?
------------


Cyble researchers suggested in a [Tweet stream](https://twitter.com/AuCyble/status/1425422006690881541) that this could be an insider job. “We know #LockBit #threatactor has been hiring corporate employees to gain access to their targets’ networks,” the firm tweeted, along with a clock counting down how much time was left for Accenture to cough up the ransom.



Cyble said that LockBit claimed to have made off with databases of more than 6TB and that it demanded $50 million as ransom. The threat actors themselves alleged that this was an insider job, “by someone who is still employed there,” though Cyble called that “unlikely.”


Sources familiar with the attack told BleepingComputer that Accenture confirmed the ransomware attack to at least one computer telephony integration (CTI) vendor and that it’s in the process of notifying more customers. According to a [tweet](https://twitter.com/HRock/status/1425447533598453760?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1425447533598453760%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.bleepingcomputer.com%2Fnews%2Fsecurity%2Faccenture-confirms-hack-after-lockbit-ransomware-data-leak-threats%2F) from threat intelligence firm Hudson Rock, the attack compromised 2,500 computers used by employees and partners, leading the firm to suggest that “this information was certainly used by threat actors.”


In a [security alert](https://www.cyber.gov.au/acsc/view-all-content/alerts/lockbit-20-ransomware-incidents-australia) issued last week, the Australian Cyber Security Centre (ACSC) warned that LockBit 2.0 ransomware attacks against Australian organizations had started to rise last month, and that they were coupled with threats to publish data in what’s known as [double-extortion attacks](https://threatpost.com/double-extortion-ransomware-attacks-spike/154818/).


“This activity has occurred across multiple industry sectors,” according to the alert. “Victims have received demands for ransom payments. In addition to the encryption of data, victims have received threats that data stolen during the incidents will be published.”


The ACSC noted ([PDF](https://www.cyber.gov.au/sites/default/files/2021-08/2021-006%20ACSC%20Ransomware%20Profile%20-%20Lockbit%202.0.pdf)) that it’s recently observed LockBit threat actors actively exploiting existing vulnerabilities in the Fortinet FortiOS and FortiProxy products, identified as CVE-2018-13379, in order to gain initial access to specific victim networks. That vulnerability, a path-traversal flaw in the SSL VPN, has been exploited in multiple attacks over the years:


In April, the FBI and the Cybersecurity and Infrastructure Security Agency (CISA) [warned](https://threatpost.com/fbi-apts-actively-exploiting-fortinet-vpn-security-holes/165213/) that advanced persistent threat (APT) nation-state actors were actively exploiting it to gain a foothold within networks before moving laterally and carrying out recon, for example.


Known Vulnerability Exploited?
------------------------------


Ron Bradley, vice president of third-party risk-management firm Shared Assessments, told Threatpost on Wednesday that the Accenture incident is “a prime example of the difference between business resiliency and business continuity. Business resiliency is like being in a boxing match, you take a body blow but can continue the fight. Business continuity comes into play when operations have ceased or severely impaired and you have to make major efforts to recover.


“This particular example with Accenture is interesting in the fact that it was a known/published vulnerability,” Bradley continued. It highlights the importance of making sure systems are properly patched in a timely manner. The ability for Accenture to manage the repercussions of potentially stolen data will be an important lesson for many organizations going forward.”


Hitesh Sheth, president and CEO at the cybersecurity firm Vectra, said that all businesses should expect attacks like this, but particularly a global consultancy firm with links to so many companies.


“First reports suggest Accenture had data backup protocols in place and moved quickly to isolate affected servers,” he told Threatpost on Wednesday. “It’s too soon for an outside observer to assess damage. However, this is yet another reminder to businesses to scrutinize security standards at their vendors, partners, and providers. Every enterprise should expect attacks like this – perhaps especially a global consulting firm with links to so many other companies. It’s how you anticipate, plan for and recover from attacks that counts.”


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[LockBit]] [[Accenture]] [[Accenture’s]] [[companies.]] [[ransomware]] [[Cyble]] [[ThreatPost]]
