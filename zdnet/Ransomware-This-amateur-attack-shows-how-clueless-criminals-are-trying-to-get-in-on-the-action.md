# Ransomware: This amateur attack shows how clueless criminals are trying to get in on the action
### Researchers dissect an email from an attacker asking people to help install ransomware on their company's network for a cut of the profit. But while this campaign isn't very successful, it shows how appealing ransomware has become.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/ransomware-this-amateur-attack-shows-how-clueless-criminals-are-trying-to-get-in-on-the-action/)
+ Date: August 19, 2021 -- 12:00 GMT (13:00 BST)
+ Author: Danny Palmer


## Article:
Unknown

Ransomware is one of the biggest cybersecurity threats to businesses today, and cyber criminals can potentially make millions of dollars in Bitcoin for a single successful attack. 

This lure of quickly making large sums of money is attracting interest from across the cyber-criminal spectrum, from [sophisticated gangs](https://www.zdnet.com/article/ransomware-now-attackers-are-exploiting-windows-printnightmare-vulnerabilities/) specialising in [ransomware attacks](https://www.zdnet.com/article/ransomware-an-executive-guide-to-one-of-the-biggest-menaces-on-the-web/), to affiliate schemes where wannabe ransomware kingpins can lease out [ransomware as a service](https://www.zdnet.com/article/ransomware-as-a-service-is-the-new-big-problem-for-business/) in exchange for a cut of the profits. 


It's also attracted low-level cyber criminals, who see an opportunity to grab a slice of the ransomware pie – even if they have little idea what they're doing. 

****SEE:****[****A winning strategy for cybersecurity****](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/)****(ZDNet special report)****

Cybersecurity researchers at Abnormal Security [have detailed](https://www.abnormalsecurity.com/blog/nigerian-ransomware-soliciting-employees-demonware.) an amateur ransomware campaign using social engineering in an attempt to fool employees into installing DemonWare ransomware on their organisation's network, in return for a slice of the payout.

DemonWare ransomware – also known as Black Kingdom and DEMON – is one of the least sophisticated forms of ransomware around, but that hasn't stopped cyber criminals trying to use it. 

In this instance, the attacker uses LinkedIn and other publicly available information to identify targets and reaches out to them by email, asking if they want to install DemonWare ransomware on the network in exchange for a million dollars – a 40% cut of a $2.5 million ransom.  






The attacker leaves an email address and a Telegram username for interested parties to contact – which researchers did, using a fictitious persona, in order to find out more about the campaign and those behind it. 

It quickly became apparent that the ransomware attacker wasn't the most sophisticated cyber criminal in the world, and they quickly lowered the proposed cost of the ransom down to $120,000. For the attacker, however, that would still be a lot of money. 

"Like most financially motivated cyber criminals, this actor is simply trying to make any amount of money from this scam. Although he quickly pivoted to a much lower ransom amount over the course of our conversation, $100,000 or $1 million would both be a life-changing amount for him," Crane Hassold, director of threat intelligence at Abnormal Security, told ZDNet. 

The attacker claimed that the person responsible for installing ransomware on the network wouldn't be caught, claiming that DemonWare would encrypt everything, including CCTV files. Researchers note that this approach suggests the attacker is "not very familiar with digital forensics or incident response investigations". 

But analysis of the files sent by the attacker confirmed that they're really attempting to distribute a working version of DemonWare ransomware. The attacker claims that they've coded the ransomware themselves, but this is a lie – DemonWare is freely available to download from GitHub, its actual author having placed it there "to demonstrate how easy ransomware are [sic] easy to make and how it work [sic]." 

The attacker's self-coding claims are likely just another part of the attempt to persuade people to go through with the scheme. According to the attacker, they've successfully encouraged people to help them to deploy ransomware, although their claims are unlikely to be trustworthy. 

But who is this wannabe ransomware attacker? By using the email and Telegram contact details they provided in their initial message, researchers were able to trace them to a trading website for Naira, the currency of Nigeria, as well as a Russian social media platform. When presented with this information in messages, the attacker confirmed they are Nigerian – which might explain the initial attempts at social engineering. 

**SEE:**[**Cybersecurity: Let's get tactical**](https://www.zdnet.com/topic/cybersecurity-lets-get-tactical/)**(ZDNet special feature)**

Cyber criminals [working out of Nigeria](https://www.zdnet.com/article/phishing-scams-a-quarter-of-all-business-email-compromise-attacks-come-from-the-us/) tend to focus their efforts around phishing and [business email compromise](https://www.zdnet.com/article/this-cybersecurity-threat-costs-business-millions-and-its-the-one-they-often-forget-about/) (BEC) attacks, but in this case, they've taken what they know and attempted to apply it to ransomware. 

"Knowing the actor behind this campaign is Nigerian really adds a lot of context to the tactics he's using. For years, cyber criminals in Nigeria have used basic social engineering techniques to commit a wide variety of scams, so it makes sense that this actor is trying to use the same tactics to deploy ransomware," said Hassold 

"It seems this actor is trying to jump on the ransomware bandwagon due to the attention recent attacks have gotten in the media; however, he's adapted historical ransomware delivery methods to fit within the attack framework he's likely used to," he added. 

While this attacker might not be very successful, other more experienced ransomware operations benefit from finding insiders to help them gain access to networks. For example, LockBit ransomware – [which has surged in popularity in recent months](https://www.zdnet.com/article/this-ransomware-has-returned-with-new-techniques-to-make-attacks-more-effective/) – regularly advertises for insiders to help carry out campaigns. 

To help prevent the network from being compromised with ransomware – be it via an outside intrusion or an insider threat – information security teams should limit permissions of users unless it's necessary for them to have admin privileges. This can prevent cyberattacks from exploiting regular user accounts as a means of gaining access to key parts of the network. 

Regularly [applying security patches](https://www.zdnet.com/article/this-one-change-could-protect-your-systems-from-attack-so-why-dont-more-companies-do-it/), enforcing the use of [multi-factor authentication](https://www.zdnet.com/article/multi-factor-authentication-use-it-for-all-the-people-that-access-your-network-all-the-time/) and [storing offline backups](https://www.zdnet.com/article/a-nas-is-not-enough/) can also help prevent disruptive ransomware attacks. 

### **MORE ON CYBERSECURITY**

* [**Business email compromise: 23 charged over 'sophisticated' fraud ring**](https://www.zdnet.com/article/business-email-compromise-23-charged-over-sophisticated-fraud-ring/)
* [**Ransomware: These are the two most common ways hackers get inside your network**](https://www.zdnet.com/article/ransomware-these-are-the-two-most-common-ways-hackers-get-inside-your-network/)
* [**New DOJ task force to take on ransomware, says report**](https://www.cnet.com/tech/services-and-software/new-doj-task-force-to-reportedly-take-on-ransomware/)
* [**Have we reached peak ransomware? How the internet's biggest security problem has grown and what happens next**](https://www.zdnet.com/article/have-we-reached-peak-ransomware-how-the-internets-biggest-security-problem-has-grown-and-what-happens-next/)
* [**This major ransomware attack was foiled at the last minute. Here's how they spotted it**](https://www.zdnet.com/article/this-ransomware-attack-was-foiled-at-the-last-minute-heres-how-they-spotted-it/)





#### Tags:
[[ransomware]] [[DemonWare]] [[ZDNet]]
