# Charming Kitten Sharpens Its Claws with PowerShell Backdoor
### The notorious Iranian APT is fortifying its arsenal with new malicious tools and evasion tactics and may even be behind the Memento ransomware.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178158
+ Date: 2022-02-02T13:58:34+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/02/02085054/Kitten-scaled-e1643809874722.jpg)

The Iranian advanced persistent threat (APT) Charming Kitten is sharpening its claws with a new [set of tools](https://threatpost.com/iran-linked-charming-kitten-touts-new-spearphishing-tactics/149109/), including a novel PowerShell backdoor and related stealth tactics, that show the group evolving yet again. The new tools may signal that it’s getting ready to pounce on new victims, researchers believe.


Researchers at cybersecurity firm [Cybereason](https://www.cybereason.com/) discovered the tools, which include a backdoor they dubbed “PowerLess Backdoor,” as well as an evasive maneuver to run the backdoor in a .NET context rather than as one that triggers a PowerShell process, the Cybereason Nocturnus Team wrote [in a report](https://www.cybereason.com/blog/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage) published Tuesday.


“The Cybereason Nocturnus Team was able to identify a new toolset that includes a novel backdoor, malware loaders, a browser info stealer, and a keylogger,” Cybereason Senior Malware Researcher Daniel Frank wrote in the report.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The team also identified links between Charming Kitten and [the Memento ransomware](https://www.sophos.com/en-us/press-office/press-releases/2021/11/sophos-discovers-new-memento-ransomware) that [emerged](https://threatpost.com/conti-deadbolt-delta-qnap-ransomware/178083/) late last year and until now has been unattributed, signaling that the APT may be moving beyond its typical cyberespionage tactics and into new cybercriminal territory, researchers said.


Charming Kitten is [a prolific APT](https://threatpost.com/black-hat-charming-kitten-opsec-goofs-training-videos/168394/) believed to be backed by the Iranian government and known by a number of other names – including TA453, APT35, Ajax Security Team, NewsBeef, Newscaster and Phosphorus.


The group – which first [rose to prominence](https://threatpost.com/charming-kitten-iranian-2fa/139979/) in 2018 – was extremely active throughout 2020 and 2021 and is best known for targeted [cyber-espionage attacks](https://threatpost.com/charming-kitten-iranian-2fa/139979/) against politicians, journalists, human-rights activists, researchers, [scholars](https://threatpost.com/apt-ta453-siphons-intel-mideast/167715/) and think tanks.


Some of the APT’s more high-profile attacks occurred in 2020, when the group targeted the [Trump and Biden presidential campaigns](https://threatpost.com/trump-biden-campaign-apt-phishing-emails/156319/) as well as attendees of [two global geo-political summits](https://threatpost.com/microsoft-iranian-apt-t20-summit-munich-security-conference/160654/), the Munich Security Conference and the Think 20 (T20) Summit, in separate and various incidents.


**New Quiver of Malware**
-------------------------


The Cybereason Nocturnus team uncovered a raft of new Charming Kitten activity when they investigated threat-intelligence efforts that “included pivoting on an IP address (162.55.136[.]20) that was already attributed to Iranian threat actors by multiple sources, including [US CERT](https://www.cisa.gov/uscert/ncas/alerts/aa21-321a),” Frank explained.


The team took a deeper dive into different files that were downloaded from the IP address and discovered a treasure trove of novel tools as well as links to Memento ransomware, he said.


Charming Kitten is now using what researchers have dubbed PowerLess Backdoor, a previously undocumented PowerShell trojan that supports downloading additional payloads, such as a keylogger and an info stealer.


The team also discovered a unique new PowerShell execution process related to the backdoor aimed at slipping past security-detection products, Frank wrote.


**“**The PowerShell code runs in the context of a .NET application, thus not launching ‘powershell.exe’ which enables it to evade security products,” he wrote.


Overall, the new tools show Charming Kitten developing more “modular, multi-staged malware” with payload-delivery aimed at “both stealth and efficacy,” Frank noted. The group also is leaning heavily on open-source tools such as cryptography libraries, weaponizing them for payloads and communication encryption, he said.


This reliance on open-source tools demonstrates that the APT’s developers likely lack “specialization in any specific coding language” and possess “intermediate coding skills,” Frank observed.


**The Memento Connection**
--------------------------


Cybereason Nocturnus also found that another IP that US CERT has linked to Charming Kitten,91.214.124[.]143, has been communicating with malicious files and has “unique URL directory patterns that reveal a potential connection to Memento ransomware,” Frank wrote.


“The string ‘gsdhdDdfgA5sS’ appears to be generated by the same script as the one listed in the [Memento ransomware IOCs](https://github.com/sophoslabs/IoCs/blob/master/ransomware_memento.csv) – “gadfTs55sghsSSS” – he explained, citing specific directory activity that researchers observed. “The domain ‘google.onedriver-srv[.]ml’ was previously resolved to the IP address 91.214.124[.]143 mentioned in the [US CERT](https://www.cisa.gov/uscert/ncas/alerts/aa21-321a) alert about Iran state-sponsored actors activity.”


Analyzing this directory activity points to the IP potentially serving as a domain being used as command and control (C2) for Memento, researchers found.


Indeed, this connection makes sense when noting that Charming Kitten’s activity last year to exploit the [ProxyShell vulnerability](https://threatpost.com/exchange-fortinet-exploited-iranian-apt-cisa/176395/) – [an RCE flaw](https://threatpost.com/exchange-servers-attack-proxyshell/168661/) in Microsoft Exchange servers that suffered a [barrage of attacks](https://threatpost.com/microsoft-barrage-proxyshell-attacks/168943/) – “took place in about the same time frame as Memento,” Frank observed.


“Iranian threat actors were also reported to be turning to ransomware during that period, which strengthens the hypothesis that Memento is operated by an Iranian threat actor,” he wrote.


**Organizations on Alert**
--------------------------


Charming Kitten’s continuous evolution of its capabilities has been [well-documented,](https://threatpost.com/iran-linked-charming-kitten-touts-new-spearphishing-tactics/149109/) so its new tools and potential to branch out in terms of the type of attacks it can deliver should come as little surprise.


Indeed, threat groups in general are just like any legitimate businesses in that they must bob and weave constantly to meet business objectives, especially when old tactics don’t serve them anymore or authorities are on to them, noted one security professional.


“Cybercriminals, like any business, work to evolve their software to improve, evolve and scale to bring about the best results needed to be successful,” observed James McQuiggan, security awareness advocate at KnowBe4, in an email to Threatpost.


In the same way, organizations need to constantly be on their toes and create “a strong security culture” so they aren’t caught unawares by novel tactics used by APTs like Charming Kitten and other highly organized threat groups, he said.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=Ajax Security Team]] [[threatactor.name=APT3]] [[threatactor.name=Magic Hound]] [[threatactor.name=Magic Hound]] [[threatactor.name=Magic Hound]] [[threatactor.name=Magic Hound]] [[threatactor.name=Magic Hound]]

#### Action:
[[action.malware.name=Arp]] [[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Agriculture]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cybereason]] [[Powershell]] [[Ip]] [[Nocturnus]] [[“the]] [[Ransomware]] [[ThreatPost]]

