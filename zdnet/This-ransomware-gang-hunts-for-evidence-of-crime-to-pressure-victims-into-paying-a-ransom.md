# This ransomware gang hunts for evidence of crime to pressure victims into paying a ransom
### "Extremely disciplined" Mespinoza attackers quietly enter networks via RDP attacks and search for files related to sensitive information that they threaten to publish if the victim doesn't pay a ransom.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-ransomware-gang-hunts-for-evidence-of-crime-to-pressure-victims-into-paying-a-ransom/)
+ Date: July 15, 2021 -- 11:59 GMT (12:59 BST)
+ Author: Danny Palmer


## Article:
Unknown

A prolific ransomware group that targets organisations around the world looks for sensitive info and files that suggest its victims are aware of illegal activity, with the aim of exploiting this as additional leverage in their hunt to make money from ransom payments. 

The Mespinoza [ransomware](https://www.zdnet.com/article/ransomware-an-executive-guide-to-one-of-the-biggest-menaces-on-the-web/) group – also known as PYSA – demands millions of dollars in exchange for a decryption key and threatens to publish private information stolen from the compromised network if the victims don't pay.  


Mespinoza has claimed victims around the world, but focuses predominantly on the United States, where it has targeted organisations in manufacturing, retail, engineering, education and government. The cybercrime group has become so prolific that [the FBI issued a warning about attacks](https://www.ic3.gov/Media/News/2021/210316.pdf).  

**SEE:**[**Cybersecurity: Let's get tactical**](https://www.zdnet.com/topic/cybersecurity-lets-get-tactical/)**(ZDNet/TechRepublic special feature) |**[**Download the free PDF version**](https://www.techrepublic.com/resource-library/whitepapers/cybersecurity-let-s-get-tactical-free-pdf/?ftag=CMG-01-10aaa1b)**(TechRepublic)** 

[Cybersecurity company Palo Alto Networks](https://unit42.paloaltonetworks.com/gasket-and-magicsocks-tools-install-mespinoza-ransomware/) has analysed Mespinoza attacks and detailed what it describes as an "extremely disciplined" ransomware group, which actively searches for evidence of illegal activity as well as other sensitive information to use as blackmail for [double extortion](https://www.zdnet.com/article/ransomware-theres-been-a-big-rise-in-double-extortion-attacks-as-gangs-try-out-new-tricks/) campaigns. 

Like many ransomware groups, Mespinoza first gains a foothold in networks [by compromising remote desktop protocol (RDP) systems](https://www.zdnet.com/article/big-jump-in-rdp-attacks-as-hackers-target-staff-working-from-home/). It's uncertain whether the attackers use brute force attacks or use [phishing attacks](https://www.zdnet.com/article/what-is-phishing-how-to-protect-yourself-from-scam-emails-and-more/) to steal login credentials, but by using legitimate usernames and passwords to access systems, it's much easier for them to remain undetected as they move around the network and attempt to lay the foundations for the ransomware attack. 

But this isn't the only way in which Mespinoza ensures that it has persistent access to hacked networks, as the group also installs a backdoor, which – based on the [malware's](https://www.zdnet.com/article/what-is-malware-everything-you-need-to-know-about-viruses-trojans-and-malicious-software/) code – researchers have named Gasket. This in turn references a capability called "MagicSocks", which uses open-source tools to provide continued remote access to the network.  






All of this allows the attackers to maintain persistence as they carefully take the time to assess the network. Mespinoza takes specific interest in file and server names relating to sensitive and confidential information, financial data and even information that might allude to illegal activity by the victim for use as leverage when demanding a ransom.  

"They search using sensitive terms such as illegal, fraud, and criminal. In other words, the actors are also interested in illegal activities known to the organisation that could provide extreme leverage should a negotiation start," Alex Hinchliffe, threat intelligence analyst for Unit 42 at Palo Alto Networks, told ZDNet. 

The ransom demands are often over $1.5 million, but the group is willing to negotiate with victims and has received many payments of almost $500,000 in exchange for a decryption key as well as to prevent stolen information from being published.


The group has been active since April 2020 – a time when the global pandemic forced many organisations to suddenly adapt to remote working, [making many more vulnerable to RDP attacks](https://www.zdnet.com/article/ransomware-vs-wfh-how-remote-working-is-making-cyberattacks-easier-to-pull-off/). And while Mespinoza isn't as high-profile as other ransomware groups, the fact that it has been operating for over a year suggests it's successful.

"They're relatively new but making a large impact given the number of victims listed on their leak site, and likely making a lot of money from their extortion," said Hinchliffe. 

**SEE:**[**Ransomware: Paying up won't stop you from getting hit again, says cybersecurity chief**](https://www.zdnet.com/article/ransomware-paying-up-wont-stop-you-from-getting-hit-again-says-cybersecurity-chief/#link=%7B%22linkText%22:%22Ransomware:%20Paying%20up%20won't%20stop%20you%20from%20getting%20hit%20again,%20says%20cybersecurity%20chief%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/ransomware-paying-up-wont-stop-you-from-getting-hit-again-says-cybersecurity-chief/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

It's currently not known where Mespinoza is operating from, but it's likely that their attacks will continue so long as they're making money from ransoms – and organisations with unsecured RDP will remain a prime target for campaigns by this group and other cyber-criminal ransomware operations. 

"Organisations need to know more about their attack surface area because without knowing their footprint, especially the internet-connected part, it's almost impossible to see what's happening, let alone defend against it," said Hinchliffe. 

"Far too many organisations have services such as a RDP exposed to the internet and are exposing themselves to the risk of remotely launched attacks, negating the need from the threat actor to create and deliver phishing attacks at much higher cost to them," he added. 

Organisations can help prevent their RDP services from being compromised by avoiding the use of default passwords and by [applying multi-factor authentication](https://www.zdnet.com/article/multi-factor-authentication-use-it-for-all-the-people-that-access-your-network-all-the-time/) to user accounts. 

### **MORE ON CYBERSECURITY**

* [**Ransomware: Why we're now facing a perfect storm**](https://www.zdnet.com/article/ransomware-why-were-now-facing-a-perfect-storm/)
* [**This major ransomware attack was foiled at the last minute. Here's how they spotted it**](https://www.zdnet.com/article/this-ransomware-attack-was-foiled-at-the-last-minute-heres-how-they-spotted-it/)
* [**New DOJ task force to take on ransomware, says report**](https://www.cnet.com/news/new-doj-task-force-to-reportedly-take-on-ransomware/)
* [**Ransomware: Banning victims from paying ransoms might reduce attacks, but it won't stop them**](https://www.zdnet.com/article/ransomware-banning-victims-from-paying-ransoms-might-reduce-attacks-but-it-wont-stop-them/)
* [**Have we reached peak ransomware? How the internet's biggest security problem has grown and what happens next**](https://www.zdnet.com/article/have-we-reached-peak-ransomware-how-the-internets-biggest-security-problem-has-grown-and-what-happens-next/)





#### Tags:
[[ransomware]] [[Mespinoza]] [[organisations]] [[RDP]] [[Hinchliffe]] [[ZDNet]]
