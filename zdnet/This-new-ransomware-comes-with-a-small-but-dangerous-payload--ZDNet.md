# This new ransomware comes with a small but dangerous payload | ZDNet
### Cybersecurity researchers identify White Rabbit, which is a new ransomware that appears to have links to FIN8, a hacking group that previously focused on finances.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/this-new-ransomware-comes-with-a-small-but-dangerous-payload/
+ Date: 2022-01-19 13:12:03
+ Author: Danny Palmer


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/63303617f8fc64c1e691f0abd797028662e8403f/2021/07/09/3700feb7-54c2-4ea8-95cc-08c2741dcdad/annoyed-woman-at-a-computer-in-an-office.jpg?width=770&height=578&fit=crop&auto=webp)

A new form of ransomware that uses discreet techniques to avoid detection before encrypting files and demanding payment in exchange for the decryption key could be linked to a notorious financial crime group. 

White Rabbit [ransomware](https://www.zdnet.com/article/ransomware-an-executive-guide-to-one-of-the-biggest-menaces-on-the-web/) emerged in December 2021 with an attack against a US bank and has since been examined [by cybersecurity researchers](https://www.trendmicro.com/en_no/research/22/a/new-ransomware-spotted-white-rabbit-and-its-evasion-tactics.html), who say that the ransomware appears to be connected to FIN8, a financially motivated cyber-criminal gang. 


FIN8 was first identified in 2016 and [typically targets point-of-sale (POS) systems with malware attacks](https://www.zdnet.com/article/cybercrime-gang-adds-new-tactics-to-credit-card-data-stealing-campaign/) designed to steal credit card information. Now it appears that FIN8 could be following the money and shifting towards ransomware campaigns. 

**SEE:** [**Your cybersecurity training needs improvement because hacking attacks are only getting worse**](https://www.zdnet.com/article/your-cybersecurity-training-needs-improvement-because-hacking-attacks-are-only-getting-worse/#link=%7B%22linkText%22:%22Your%20cybersecurity%20training%20needs%20improvement%20because%20hacking%20attacks%20are%20only%20getting%20worse%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/your-cybersecurity-training-needs-improvement-because-hacking-attacks-are-only-getting-worse/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

[According to cybersecurity researchers at Trend Micro](https://www.trendmicro.com/en_no/research/22/a/new-ransomware-spotted-white-rabbit-and-its-evasion-tactics.html), White Rabbit uses tactics that have been seen before, most notably by [Egregor](https://www.zdnet.com/article/ukrainian-police-arrest-members-of-ransomware-affiliate/), in that it's payload binary requires a specific command-line password before it goes ahead with the ransomware and encryption routine – a technique that allows the payload to remain undetected until it's executed. 

The payload is also hard to detect because the file is small, only 100KB, which appears to show no signs of activity. It contains strings for logging – something that could give away the malicious intent – but these could only be accessed with the correct password. In the sample analysed by Trend Micro, the password was 'KissMe' – although the password could be different for each campaign. 

Like many other ransomware groups, White Rabbit uses [double extortion](https://www.zdnet.com/article/ransomware-theres-been-a-big-rise-in-double-extortion-attacks-as-gangs-try-out-new-tricks/), threatening the victim of the attack with publishing or selling data stolen from the compromised network if a ransom payment isn't received. They also threaten to leak the data if the victim contacts the FBI about the attack. 






It's not detailed how the cyber criminals behind White Rabbit initially compromise networks, but researchers note the use of Cobalt Strike, a penetration-testing tool, to gather information and move around affected systems. 

But something that has been detailed by [researchers at cybersecurity company Lodestone](https://lodestone.com/insight/white-rabbit-ransomware-and-the-f5-backdoor/) is what appears to be a connection between White Rabbit and FIN8. They note that a malicious URL connected to the attack has previously been connected with FIN8 activity. 

****SEE:****[****A winning strategy for cybersecurity****](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/?ftag=CMG-01-10aaa1b)****(ZDNet special report)****

In addition to this, Lodestone has identified White Rabbit being used alongside a never-before-seen version of [Badhatch](https://www.zdnet.com/article/cybercrime-gang-adds-new-tactics-to-credit-card-data-stealing-campaign/), a form of malware designed to create backdoors into compromised networks and that is associated with previous FIN8 campaigns targeting point-of-sale systems. 

"Currently, we are still determining if FIN8 and White Rabbit are indeed related or if they share the same creator. Given that FIN8 is known mostly for its infiltration and reconnaissance tools, the connection could be an indication of how the group is expanding its arsenal to include ransomware," Trend Micro wrote in a blog post. 

For financially motivated cyber criminals, a shift towards ransomware could be seen as desirable because of the amount of money that can be made from encrypting networks, [which can reach millions of dollars](https://www.zdnet.com/article/average-ransomware-payment-for-us-victim-more-than-6-million-mimecast/). 

It isn't without precedent – [cybersecurity researchers have previously detailed how FIN11](https://www.zdnet.com/article/this-major-criminal-hacking-group-just-switched-to-ransomware-attacks/), an established financial crime group that previously focused on phishing and malware campaigns, changed tactics and switched to ransomware attacks. 

### **MORE ON CYBERSECURITY**

* [**Ransomware attackers targeted this company. Then defenders discovered something curious**](https://www.zdnet.com/article/ransomware-attackers-targeted-this-company-then-defenders-discovered-something-curious/)
* [**Bosses are reluctant to spend money on cybersecurity. Then they get hacked**](https://www.zdnet.com/article/too-many-bosses-are-reluctant-to-spend-money-on-cybersecurity-then-they-get-hacked/)
* [**Russian authorities take down REvil ransomware gang**](https://www.zdnet.com/article/russian-authorities-take-down-revil-ransomware-gang/)
* **[**This company was hit with ransomware, but didn't have to pay up. Here's how they did it**](https://www.zdnet.com/article/this-company-was-hit-with-ransomware-but-didnt-have-to-pay-up-heres-how-they-did-it/)**
* **[**Have we reached peak ransomware? How the internet's biggest security problem has grown and what happens next**](https://www.zdnet.com/article/have-we-reached-peak-ransomware-how-the-internets-biggest-security-problem-has-grown-and-what-happens-next/)**





## Tags:

#### Threatactor:
[[threatactor.name=FIN8]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Egregor]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=REvil]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Fin8]] [[Cybersecurity]] [[Malware]] [[ZDNet]]

