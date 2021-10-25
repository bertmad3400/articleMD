# SolarWinds APT Targets Tech Resellers in Latest Supply-Chain Cyberattacks
### The Nobelium group, linked to Russia’s spy agency, is looking to use resellers as a path to infiltrate their valuable downstream customers – and it’s working.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175716)
+ Date: October 25, 2021  3:16 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/25144231/supply-chain-e1635187371700.png)
The SolarWinds attackers – an advanced persistent threat (APT) known as Nobelium – have started a new wave of supply-chain intrusions, this time using the technology reseller/service provider community to attack their targets.


The activity has affected victims in North America and Europe thus far, researchers said, and the goal is espionage: Nobelium has been linked to the Russian government’s foreign intelligence service, known as SVR.


According to an analysis from Mandiant and Microsoft, Nobelium isn’t exploiting a vulnerability or, as was the case with SolarWinds, [trojanizing legitimate code](https://threatpost.com/solarwinds-orion-bug-remote-code-execution/163618/). Instead, it’s infiltrating reseller networks using tried-and-true tactics like credential-stuffing and phishing, as well as API abuse and token theft, in order to gather legitimate account credentials and privileged access to reseller networks.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


From there, Nobelium attempts to pivot and land inside the networks of reseller customers downstream. Once inside a reseller network, it becomes much easier to impersonate the company and exploit the trusted relationship that reseller has with its customers, researchers pointed out.


“Mandiant has investigated multiple intrusions in 2021 where suspected Russian threat actors exploited supply-chain relationships between technology companies and their customers,” said Mandiant senior vice president and CTO Charles Carmakal, via email. “While the SolarWinds supply-chain attack involved malicious code inserted in legitimate software, most of this recent intrusion activity has involved leveraging stolen identities and the networks of technology solutions, services and reseller companies in North America and Europe to ultimately access the environments of organizations that are targeted by the Russian government.”


Since May, Microsoft has observed Nobelium attacking more than 140 resellers and technology service providers, it said, with about 14 of them succumbing to compromise. However, in its writeup, [issued Sunday](https://blogs.microsoft.com/on-the-issues/?p=64918), the software giant didn’t say how many downstream customers have been affected.


Mandiant’s Carmakal only said that the firm has seen successful intrusions into on-premises and cloud victim environments.


“This attack path makes it very difficult for victim organizations to discover they were compromised and investigate the actions taken by the threat actor,” Carmakal said. “Investigating these intrusions requires collaboration and information-sharing across multiple victim organizations, which is challenging due to privacy concerns and organizational sensitivities.”


The approach is also particularly effective for Nobelium because it allows the cyberattackers to avoid dealing with what could be strong defense measures at the end-user targets, he added.


“It shifts the initial intrusion away from the ultimate targets, which in some situations are organizations with more mature cyberdefenses, to smaller technology partners with less mature cyberdefenses,” he said.


If successful, an attack could allow for data theft, reconnaissance, compromise of customer systems and more.


**Systemic Access to the Technology Supply Chain**
--------------------------------------------------


“Nobelium ultimately hopes to piggyback on any direct access that resellers may have to their customers’ IT systems,” according to Microsoft. “This recent activity is another indicator that Russia is trying to gain long-term, systematic access to a variety of points in the technology supply chain and establish a mechanism for surveilling – now or in the future – targets of interest to the Russian government.”


To that point, Microsoft also said that this particular campaign is merely a subset of a larger wave of Nobelium activities, which points to significantly ramped-up efforts by Russia to establish a persistent anchor for its spy activities. For instance, in September [it was seen installing](https://threatpost.com/solarwinds-active-directory-servers-foggyweb-backdoor/175056/) the FoggyWeb custom backdoor on single sign-on servers.


“Between July 1 and Oct. 19 this year, we informed 609 customers that they had been attacked 22,868 times by Nobelium, with a success rate in the low single digits,” according to its writeup. “By comparison, prior to July 1, we had notified customers about attacks from all nation-state actors 20,500 times over the past three years.”


**The U.S. Needs to Do More**
-----------------------------


Famously, the SolarWinds attack caused widespread damage and allowed Nobelium to gain access to [several U.S. government agencies](https://threatpost.com/solarwinds-attackers-dhs-emails/165110/), by hijacking a legitimate software update from the platform to push malware to SolarWinds users.


While the reseller campaign is of a smaller scale, Jamil Jaffer, former associate White House Counsel to President George W. Bush and a senior vice president for IronNet Cybersecurity, noted that it highlights the need for the government to do more to thwart Russian hacking.


“[This showcases] the need to take more aggressive action to impose costs in order to deter such activity by Russia,” he told Threatpost via email. “It also highlights the need for the U.S. government to expand its defensive collaboration with the U.S. private sector…It is clear that the previously imposed sanctions for both hacking activity as well as Russia’s support of ransomware attacks have not adequately deterred Russian cyber-activity against the U.S. private sector.”


He added that the Biden Administration has put in place a top-notch team of cyber-experts, who could make some changes.


“They must be freed up to work more effectively and collaboratively with the private sector to create a true collective defense capability where industry and government work together to stop such attacks, including through the new Joint Cyber Defense Collaborative established by the new director of CISA at DHS, Jen Easterly,” he noted.


**How Resellers Can Defend Against Nobelium**
---------------------------------------------


For now, the intrusion activity is ongoing, and both Microsoft and Mandiant said they’re actively working with affected organizations. To protect themselves, resellers and service providers can take several basic steps to implement specific security protections for their environments, researchers noted, such as restricting access to partner portals and other customer-relationship management tools, and enabling multi-factor authentication (MFA).


They should also audit any delegated privileged accounts and remove unnecessary authority clearances, and, if possible, adopt a zero-trust security ideology.


“IT supply chain companies must act now to avoid becoming the next SolarWinds,” said Danny Lopez, CEO of Glasswall, via email. “To prevent these attackers from gaining privileged access and wreaking havoc, organizations need to adopt robust processes for onboarding and offboarding employees and affiliates that may receive access to key information systems. It’s vital to control privileged access and to monitor those that enjoy that administrator privilege.”


He added, “This will help to limit the blast radius, and in most cases, defeat the data breach.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[U.S.]] [[SolarWinds]] [[supply-chain]] [[Mandiant]] [[email.]] [[Microsoft]] [[“This]] [[ThreatPost]]
