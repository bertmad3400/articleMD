# FIN7’s Liquor Lure Compromises Law Firm with Backdoor
### Using a lure relating to a lawsuit against the owner of Jack Daniels whiskey, the cybergang launched a campaign that may be bent on ransomware deployment.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168086)
+ Date: July 23, 2021  12:24 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/23122248/jack-daniels-e1627057381602.jpg)
Financial cybercrime gang FIN7 has rebounded after [the jailing](https://threatpost.com/fin7-pen-tester-jail/167293/) of some key members, launching a campaign that uses as a lure a legal complaint involving the liquor company that owns Jack Daniels whiskey. The gambit successfully compromised at least one law firm, giving them a shot of the JSSLoader remote-access trojan (RAT), researchers said.


According to eSentire’s Threat Response Unit (TRU), the successful breach for FIN7 (aka Carbanak Group or Navigator Group) was part of a wider, non-targeted email campaign. It purports to relate to a legal complaint centering around liquor giant Brown-Forman.


“One of the victims of the malicious legal complaint campaign was a law firm,” researchers said [in a posting](https://www.esentire.com/security-advisories/notorious-cybercrime-gang-fin7-lands-malware-in-law-firm-using-fake-legal-complaint-against-jack-daniels-owner-brown-forman-inc) this week. “The lure successfully bypassed the law firm’s email filters, and it was not detected as suspicious by any of the firm’s employees.”



The ultimate purpose of installing the backdoor is unclear. FIN7 usually carries out targeted attacks on point-of-sale systems at casual-dining restaurants, casinos and hotels; or, it [infiltrates systems](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/) to steal bank-card data and sell it. Since 2020, it has also added ransomware/data exfiltration attacks to its mix, carefully selecting targets according to revenue using the ZoomInfo service.


“It is plausible that proficient financial cybercrime groups, such as FIN7, are providing initial access to seasoned ransomware groups, such as REvil (aka Sodinokibi), Ryuk, etc. as a way to monetize their access,” according to TRU.


**Savvy Email Lures**
---------------------


The lawsuit campaign was geared to take advantage of a certain amount of zeitgeist, according to the analysis. The messages were sent the first week of June, just one month before settlement claims were due for a real class action suit against Brown-Forman regarding a ransomware breach the company [suffered last August](https://threatpost.com/jack-daniels-ritz-london-cyberattacks/158409/).


“The infamous REvil gang [took credit](https://www.bloomberg.com/news/articles/2020-08-14/brown-forman-was-target-of-apparent-ransomware-attack) for the ransomware attack,” according to TRU. “Although the company said they were able to disrupt the attack before their data could be encrypted, the REvil gang broadcasted on their blog/leak site that they had access to Brown-Forman’s systems for over a month and stole a terabyte of their company data.”


While using such a specific lure lawsuit in a wide-scale campaign may seem counterintuitive, it can net lucrative fish, researchers noted.


“Corporate users might immediately suspect a random legal complaint, that arrives via email, from a large spirits and wine company,” they wrote. “However, law firms deal with legal complaints across industry verticals regularly, so the content would not be considered out of the ordinary. Thus, law firms may be more susceptible to this topic.”


This isn’t the only activity from FIN7 of late; researchers have also observed a campaign using a USPS mail delivery notification lure, and a campaign themed with Windows 11 that delivered the JSSLoader malware.


“Whatever the specific intentions of FIN7, they appear to be actively adjusting their lures to maximize campaign success,” according to TRU researchers. “Cybercriminals use well-timed lures and try to predict the susceptibility of a theme for their threat campaigns, and they will use lures built around social trends, global crises and routine events.”


**Robust Cybercriminal Infrastructure**
---------------------------------------


Despite the group’s incarceration woes, FIN7’s infrastructure appears to be robust, researchers said, with a network of servers at the ready:


TRU recently observed the registration of a new lookalike domain within this web of infrastructure, brown-formam[.]com, on June 9.


“While in-the-wild use has not been observed, the registration and TLS certificate patterns match the previous landing page,” researchers said. “We assess this domain will replace the prior one given that it has been exposed publicly.”


Notably for the Brown-Forman case, FIN7 threat actors registered the infrastructure months before the TRU saw it in action.


“Either the attackers were using it for months before eSentire saw the activity, or they weaponized it after a period of time to evade email filtering by newly registered domains. If that is the case, this shows a degree of planning and sophistication on the part of FIN7.”


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 




#### Tags:
[[FIN7]] [[TRU]] [[Brown-Forman]] [[ransomware]] [[REvil]] [[ThreatPost]]
