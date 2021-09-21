# Hackers Are Going ‘Deep-Sea Phishing,’ So What Can You Do About It?
### Nick Kael, CTO at Ericom, discusses how phishing is gaining sophistication and what it means for businesses.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174868)
+ Date: September 21, 2021  1:49 pm
+ Author: Nick Kael


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/21134528/phishing-1-e1632246346826.jpg)
Hackers are upping their game, using an approach I call “Deep Sea Phishing,” which is the use of a combination of the techniques described below to become more aggressive. To keep pace, cybersecurity innovators have been working diligently to develop tools, techniques and resources to improve defenses. But how can organizations fight against evolving threats that have yet to be launched—or even conceived of?


For example, in February, [10,000 Microsoft users were targeted in a phishing campaign](https://threatpost.com/microsoft-fedex-phishing-attack/164143/) which sent emails purporting to be from FedEx, DHL Express and other couriers which contained links to phishing pages hosted on legitimate domains, with the goal of obtaining recipients’ work email credentials. Use of legitimate domains allowed the emails to evade security filters, and people’s pandemic-related reliance on delivery services and habituation to similar messages boosted success rates.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


And in May, attackers launched a massive, [sophisticated payment-themed phishing campaign](https://twitter.com/MsftSecIntel/status/1395138351917764608). The phishing emails urged users to open an attached “payment advice” – which was, in fact, not an attachment at all but rather an image containing a link to a malicious domain. When opened, Java-based STRRAT malware was downloaded onto the endpoint and via a command-and-control (C2) server connection, ran backdoor functions such as collecting passwords from browsers, running remote commands and PowerShell, logging keystrokes and other criminal activity.


Phishing is no longer the basement-brewed, small-scale nuisance of cyber lore, either. Today, nearly 70 percent of cyberattacks – like like those cited above – are orchestrated by organized crime or nation-state affiliated actors. With many recovery tabs running into the millions, organizations need a solution that can safeguard them from attacks that have not yet been engineered — i.e., zero-day attacks that can cause the most damage.


But before we tackle the issue of defense, let’s first take a look at just what we’re defending against. The types of phishing tactics noted below are listed in ascending order of sophistication.


**Types of Phishing**
---------------------


Not all phishing attacks are created equal but all, by design, inflict damage on organizations that can involve significant financial payouts, remediation costs, revenue loss and damage to reputations. Attacks range from typical phishing emails to sophisticated spear-phishing schemes and “whaling.”


Garden-variety phishing succeeds as a numbers game. Phishers send out weaponized emails to a large list of recipients, with the well-founded expectation that some small percentage will click. Phishing emails are generally designed to appear to be official messages from trusted companies. However, when the recipient clicks on a seemingly innocuous link embedded within the email, malware may be downloaded straight onto their device, or a malicious webpage opens that either downloads malware or requests personal information like credentials, account numbers or other valuable data to be entered.


Unlike phishing, which casts a wide net, spear-phishing emails are highly targeted, going after a specific individual or organization. Cybercriminals use social media and other public information to create personalized email for specific individuals and adopt the guise of a trusted sender.


For instance, in April, personal information of 500 million LinkedIn accounts [was scraped and leaked](https://threatpost.com/data-500m-linkedin-users-online/165329/) from the social-media platform and sold as bait for spear-phishing attacks. Because spear-phishing emails are personalized, recipients are more likely to click on a malicious link within and even enter credentials on a landing page.


Whaling, which is a form of spear-phishing, targets prominent individuals like CEOs and CFOs to gain highly sensitive personal or business data. The “sender” may pose as a business associate, customer or someone who has a critical business issue that needs to be addressed by the targeted individual. The primary goal of a whaling email is to steal sensitive business information.


What sets spear-phishing and whaling apart from average phishing attacks is the use of personal and professional data that builds increased legitimacy in the eyes of the recipient. They are creative and effective forms of phishing that everyone needs to guard against.


**Cybercriminals are Ahead, Thanks to Humans**
----------------------------------------------


More sophisticated phishing attacks require more development time and effort – investment that is repaid in larger expected payouts, especially when layering on malware. These methods continue to work very well for the bad guys: In fact, according to a [survey](https://www.statista.com/statistics/700965/leading-cause-of-ransomware-infection/) of MSPs worldwide, 67 percent of respondents indicated that phishing emails were the most common delivery channel for ransomware attacks.


This is alarming, given that many companies require employees to periodically undergo anti-phishing training. But alas, not surprising. Employee training falls short of protecting organizations because humans are the weakest link in the cybersecurity chain. Gullible, habit-driven creatures that we are, we continue to click on links that compromise organizations’ entire networks.


Verizon’s 2021 Data Breach Investigations Report (DBIR) top finding states that 85 percent of breaches involved a human element, 36 percent involved phishing (11 percent more than the previous year), and 10 percent of breaches involved ransomware – double the rate of the previous year.


**The Ransomware-Phishing Link**
--------------------------------


Organizations of all sizes should be considering what a ransomware attack – which often starts with phishing – could do to their performance, financial stability and future. More importantly, they should be assessing their cybersecurity strategies and security architecture, especially in light of the disappearing perimeter associated with increasingly distributed workforces.


According to [SonicWall](https://www.securitymagazine.com/articles/94831-ransomware-soars-with-62-increase-since-2019), ransomware attacks increased by 62 percent since 2019.


This onslaught includes small businesses. An estimated half of all cyberattacks target this group, which may not have the same phishing awareness training in place as larger organizations. The resulting revenue loss and costs of remediation, downtime, reputational damage and legal expenses are all big hits for small businesses.


New developments make ransomware even more of a threat. [According to the FBI](https://blog.malwarebytes.com/malwarebytes-news/2021/03/ryuk-ransomware-develops-worm-like-capability/), Ryuk is the top ransomware in terms of payments completed. Now, a [worm-like capability](https://threatpost.com/ryuk-ransomware-worming-self-propagation/164412/) has been added, which makes it no longer reliant on human clicks to spread. This is a significant and very worrisome development.


Consider this: An initial infection occurs within just a few seconds. Ransomware that is launched when a user clicks a link in a phishing email rapidly begins to spread laterally throughout the network, encrypting PCs and servers for maximum damage – and maximum profit for the cybercriminals targeting your organization.


The ransomware then reads infected files, in search of user credentials that will enable it to spread faster via remote desktop connections between network computers or mapped drives. Backing up data on a cloud, while good practice, may not necessarily be sufficient.


Sophisticated strains of ransomware can target files on shared network drives and cloud backup services, thus paralyzing your entire organization and leaving you at the (dubious) mercy of cybercriminals.


The impact of ransomware may also extend well beyond the business itself. For instance, the May ransomware attack on Colonial Pipeline—a 900-person company—shut down [5,500 miles of pipeline that carry 45 percent of the U.S. East Coast’s fuel supplies](https://threatpost.com/pipeline-crippled-ransomware/165963/). The company paid the $4.4 million ransom, largely due to pressure to restore service for the tens of millions of people and organizations that depend on the pipeline for fuel, including medical services, law enforcement agencies, fire departments, airports and the public at large.


An email just needs to hit at one vulnerable moment, with a lure that resonates with one employee who receives it, for that individual to click on a seemingly legitimate link in a phishing email to download an infected file. With today’s zero-day threats and advanced malware, stronger defenses than signature-based scanning techniques and lookups for known malicious domains are needed – and needed *now*.


Organizations cannot depend on their users as a last line of defense against phishing. After all, user vulnerability is why phishing is so effective and so widely used. Don’t fault your employees: Cybercriminals are among the most sophisticated experts in human behavior as well as in exploiting technologies that allow their efforts to remain undetected.


**Defense Options: Remote Browser Isolation**
---------------------------------------------


For these reasons and more, a very different approach must be considered—one that *assumes breach* yet prevents exposure to malware and ransomware. And with phishing attacks becoming more layered and multifaceted, it’s hard to tell what the next cybercrime innovation will be, so future-proofing becomes important.


Remote browser isolation (RBI) provides organizations with a defense against even the most sophisticated web-based attacks. When a user clicks a link in an email or opens a new browser tab, RBI executes the web content in a virtual browser located in a remote, isolated container in the cloud. Only safe rendering data is sent to the user’s regular endpoint browser, providing a fully interactive, regular browsing experience. No web content reaches the user device, and potentially risky sites can be opened in read-only mode to prevent credential theft, so users are 100 percent protected from malware from malicious websites and URLs in phishing emails.


Phishing is not only here to stay, but it is getting more advanced and dangerous each day. Accepting that humans are fallible and easily manipulated is essential, so that organizations stop relying primarily on training and opt for solutions that effectively protect the organizations from the cybercriminals’ best efforts, as well as from their own users’ errors. Using RBI to isolate users and “air gap” them from the dangers of malicious email links and phishing sites is an innovative approach that organizations can adopt today to keep themselves out of the phishing and ransomware headlines.


***Nick Kael is CTO at Ericom.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[phishing]] [[ransomware]] [[emails]] [[malware]] [[spear-phishing]] [[Phishing]] [[cybersecurity]] [[Cybercriminals]] [[attacks.]] [[ThreatPost]]
