# There's been a big rise in phishing attacks using Microsoft Excel XLL add-ins | ZDNet
### Cybersecurity researchers warn that multiple forms of malware are being stealthily delivered via Microsoft Excel XLL files.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/theres-been-a-big-rise-in-phishing-attacks-using-microsoft-excel-xll-add-ins/
+ Date: 2022-01-27 15:04:21
+ Author: Danny Palmer


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/1cbf3917fb2e5bdc41c603bfcb1af8f57d67d302/2019/04/04/720fe18d-fa0e-4596-aafc-4711ed1f5f98/woman-checking-email.jpg?width=770&height=578&fit=crop&auto=webp)

A wave of cyber attacks are exploiting Microsoft Excel add-in files in order to deliver several forms of malware in campaigns which could leave businesses vulnerable to data theft, ransomware and other cyber crime. 

Detailed by researchers at [HP Wolf Security](https://threatresearch.ext.hp.com/hp-wolf-security-threat-insights-report-q4-2021/), the campaigns use malicious Microsoft Excel add-in (XLL) files to infect systems and there was an almost six-fold increase – a 588% rise – in attacks using this technique during the final quarter of 2021 when compared to the previous three months. 

XLL add-in files are popular because they enable users to deploy a wide variety of extra tools and functions in Microsoft Excel. [But like macros](https://www.zdnet.com/article/microsoft-were-switching-off-excel-4-0-macros-by-default-to-protect-you-against-security-threats/), they're a tool which can be exploited by cyber criminals. 

The attacks are [distributed via phishing emails](https://www.zdnet.com/article/what-is-phishing-how-to-protect-yourself-from-scam-emails-and-more/) based around payment references, invoices, quotes, shipping documents and orders which come with malicious Excel documents with XLL add-in files. Running the malicious file prompts users to install and activate the add-in - which will secretly run the malware on the victim's machine. 

Malware families identified as being delivered in attacks leveraging XLL files include – [Dridex](https://www.zdnet.com/article/ta575-criminal-group-using-squid-game-lures-for-dridex-malware/), IcedID, [BazaLoader](https://www.zdnet.com/article/this-phishing-attack-is-using-a-call-centre-to-trick-people-into-installing-malware-on-their-windows-pc/), [Agent Tesla](https://www.zdnet.com/article/agent-tesla-ramps-up-its-game-in-bypassing-security-walls-attacks-endpoint-protection/), [Raccoon Stealer](https://www.zdnet.com/article/raccoon-stealer-as-a-service-will-now-try-to-steal-your-cryptocurrency/), [Formbook](https://www.zdnet.com/article/49-malware-receives-major-upgrade-to-strike-windows-and-mac-pcs/) and Bitrat. Many of these forms of malware can create backdoors onto compromised Windows systems, providing attackers with the ability to remotely access machines, monitor activity and steal data. 

Researchers also warn that malware backdoors provide attackers with ability to deliver other malware, [including ransomware](https://www.zdnet.com/article/have-we-reached-peak-ransomware-how-the-internets-biggest-security-problem-has-grown-and-what-happens-next/), meaning the XLL attacks could be exploited as a means of encrypting networks and demanding large ransom payments. 

These XLL attacks are effective at compromising victims – something that's reflected in the prices of those offering services related to them on underground dark web forums.  






**SEE:**[**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/)**(ZDNet special report)**

Some XLL Excel Dropper services are advertised as costing over $2,000, which is quite expensive for community malware but criminal forum users seem willing to pay the price. 

In addition to the XLL-based campaigns, researchers note that [QakBot](https://www.zdnet.com/article/this-decade-old-malware-has-picked-up-some-nasty-new-tricks/), a prominent form of trojan malware, often used as a precursor to ransomware attacks, is also abusing Excel to compromise victims. 

Attackers are hijacking email threads in order to deliver malicious Excel documents to their chosen victims, who are sent a ZIP archive containing a Microsoft Excel Binary Workbook (XLSB). If this is run, QakBot is downloaded onto the machine. 

"Abusing legitimate features in software to hide from detection tools is a common tactic for attackers, as is using uncommon file types that may be allowed past email gateways. Security teams need to ensure they are not relying on detection alone and that they are keeping up with the latest threats and updating their defenses accordingly," said Alex Holland, senior malware analyst at HP Wolf Security. 

"Attackers are continually innovating to find new techniques to evade detection, so it's vital that enterprises plan and adjust their defenses based on the threat landscape and the business needs of their users. Threat actors have invested in techniques such as email thread hijacking, making it harder than ever for users to tell friend from foe," he added. 

In order to avoid falling victim to the spate of attacks abusing XLL files, it's recommended that administrators configure email gateways to block incoming .xll attachments and only permit add-ins to be delivered by trusted partners – or even disable Excel add-ins entirely. 

**MORE ON CYBERSECURITY**

* [**Ransomware is still the biggest security worry for business, but it's not the only headache**](https://www.zdnet.com/article/ransomware-is-still-the-biggest-security-worry-for-business-but-its-not-the-only-headache/)
* [**Hackers are turning to this simple technique to install their malware on PCs**](https://www.zdnet.com/article/hackers-are-turning-to-this-simple-technique-to-install-their-malware-on-pcs/)
* [**This stealthy malware delivers a 'silent threat' that wants to steal your passwords**](https://www.zdnet.com/article/this-stealthy-malware-delivers-a-silent-threat-that-wants-to-steal-your-passwords/)
* [**Microsoft: We're cracking down on Excel macro malware**](https://www.zdnet.com/article/microsoft-were-cracking-down-on-malware-that-uses-excel-macros/)
* [**A company spotted a security breach. Then investigators found this new mysterious malware**](https://www.zdnet.com/article/a-company-spotted-a-security-breach-then-investigators-found-this-new-mysterious-malware/)





## Tags:

#### Action:
[[action.malware.name=Agent Tesla]] [[action.malware.name=at]] [[action.malware.name=CHOPSTICK]] [[action.malware.name=Conti]] [[action.malware.name=Dridex]] [[action.malware.name=IcedID]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=QakBot]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Malware]] [[Xll]] [[Add-in]] [[Microsoft]] [[Ransomware]] [[ZDNet]]

