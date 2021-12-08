# Emotet’s Behavior & Spread Are Omens of Ransomware Attacks
### The botnet, which resurfaced last month on the back of TrickBot, can now directly install Cobalt Strike on infected devices, giving threat actors direct access to targets.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176845
+ Date: 2021-12-08T14:47:59+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/08094345/ransomware-e1638974638687.jpg)

The rapid spread of [Emotet](https://threatpost.com/emotet-returns-100k-mailboxes/162584/) via [TrickBot](https://threatpost.com/trickbot-switches-to-a-new-windows-10-uac-bypass-to-evade-detection/152477/) and its behavior since the malware resurfaced last month could signal that a spate of ransomware attacks are on the way, spurring researchers to warn organizations to buckle up and get ready.


In mid-November, a team of researchers from [Cryptolaemus](https://twitter.com/Cryptolaemus1/status/1460302706954981385), [G DATA](https://cyber.wtf/2021/11/15/guess-whos-back/) and [AdvIntel](https://twitter.com/VK_Intel/status/1460308855129313281) [revealed](https://threatpost.com/emotet-resurfaces-trickbot/176362/) that they had observed the TrickBot trojan launching what appears to be a new loader for the notorious Emotet, which has been called “the world’s most dangerous malware.”


Now Emotet has been observed directly installing [Cobalt Strike beacons](https://tria.ge/211207-t5l24sbean) on infected devices, warned Cryptolaemus, a global group of security experts, on Twitter. This behavior can give threat actors direct access to install ransomware on target systems, researchers said.



> **We want to know what your biggest cloud security concerns and challenges are, and how your company is dealing with them. Weigh in with our exclusive, anonymous [Threatpost Poll](https://threatpost.com/cloud-security-challenges-poll/176702/)!**
> 
> 


“We have confirmed that [#Emotet](https://twitter.com/hashtag/Emotet?src=hashtag_click) is dropping CS Beacons on E5 Bots,” according to [a post](https://twitter.com/Cryptolaemus1/status/1468266929014157316) on the Cryptolaemus Twitter feed.



> 
> 🚨🚨WARNING 🚨🚨 We have confirmed that [#Emotet](https://twitter.com/hashtag/Emotet?src=hash&ref_src=twsrc%5Etfw) is dropping CS Beacons on E5 Bots and we have observed the following as of 10:00EST/15:00UTC. The following beacon was dropped: <https://t.co/imJDQTGqxV> Note the traffic to lartmana[.]com. This is an active CS Teams Server. 1/x
> 
> 
> — Cryptolaemus (@Cryptolaemus1) [December 7, 2021](https://twitter.com/Cryptolaemus1/status/1468266929014157316?ref_src=twsrc%5Etfw)
> 
> 



“No TrickBot or other intermediate garbage. Straight to CS and lateral movement to DCs/Critical Parts of the network,” researchers [tweeted](https://twitter.com/Cryptolaemus1/status/1468266931874578436). “You need to pay attention to this and you need to prepare.”


On Wednesday, Check Point Research also published a [report](https://research.checkpoint.com/2021/when-old-friends-meet-again-why-emotet-chose-trickbot-for-rebirth/) that warned of imminent ransomware attacks now that TrickBot is dropping Emotet samples, especially given that TrickBot has amassed 140,000 victims across 149 countries in only 10 months.


Check Point researchers have spotted 223 different TrickBot campaigns in the last six months, with targets in government, finance and manufacturing, with the geographic regions of Portugal and the United States topping the list.


While the fact that 129 out of 223 campaigns stopped their activity in July may seem to indicate “that TrickBot activity has dropped in scale,” it hasn’t, researchers said.


“Combined with all the other facts we can conclude that it is quite the opposite,” they wrote. “The campaigns became more massive and widely targeted as the number of victims continues to grow despite the drop in the number of campaigns.”


Moreover, TrickBot’s recently discovered spread of Emotet is a strong indicator of future ransomware attacks, as the malware provides ransomware gangs a backdoor into compromised machines, researchers said in the report.


“With Emotet back and using the Trickbot malware as a delivery service, the malware landscape is doing its best to be as threatening and effective as possible,” they wrote.


**Botnet Partners in Crime**
----------------------------


TrickBot and Emotet – “two of the largest botnets in history,” according to Check Point – are cozy bedfellows and have been [paired together](https://threatpost.com/un-weathers-emotet-trickbot-malware/151894/) often in the past by threat actors to mount numerous attacks. Often, it was Emotet using its vast network to deliver TrickBot as a payload in [targeted email phishing campaigns](https://threatpost.com/un-weathers-emotet-trickbot-malware/151894/), though TrickBot also has delivered Emotet samples – the dangerous scenario at hand now.


Emotet started life as a banking trojan in 2014 and has continually evolved to become a full-service threat-delivery mechanism. The botnet was “once an overbearing threat that held more than 1.5 million machines under its sway … capable of infecting those machines with additional bankers, trojans and ransomware,” according to Check Point.


Indeed, at the end of its heyday, the estimated damage from Emotet was around $2.5 billion dollars, researchers said in the report.


Emotet appeared to be [put out of commission](https://threatpost.com/emotet-takedown-infrastructure-netwalker-offline/163389/) by an international law-enforcement collaborative takedown of a network of hundreds of botnet servers supporting the system in January 2021.


[TrickBot](https://threatpost.com/trickbot-custom-stealthy-backdoor/151663/) also started life as a banking trojan, first developed in 2016, and also was [dealt a serious blow](https://threatpost.com/trickbot-takedown-crimeware-apparatus/160018/) by law enforcement in October 2020, only to [resurface](https://threatpost.com/trickbot-returns-bootkit-functions/161873/) last December.


Now that both botnets are back and being weaponized together, their ability to spread ransomware is worrying, with attacks at a [record high](https://threatpost.com/ransomware-volumes-record-highs-2021/168327/) in terms of volume that’s keeping [international law enforcement](https://threatpost.com/feds-offer-10-million-bounty-on-darkside-info/176030/) up at night.


**Armed with New Tricks**
-------------------------


Emotet also has added new capabilities since its resurgence, with its perpetrators using their 10 months of downtime to upgrade the bot, according to Check Point.


“These include using Elliptic curve cryptography instead of RSA cryptography, improving its control flow flatting methods, adding to the initial infection by using malicious Windows app installer packages that imitate legitimate software and more,” researchers wrote.


Emotet also is now back to using malicious documents to drop its samples, as well as riding along with TrickBot, according to Check Point, which detailed an Emotet infection carried out in this way.


Specifically, researchers analyzed a malicious Excel document being loaded from several sources with a script inside using PowerShell to download Emotet payloads, they wrote.


Overall, this novel Emotet activity, paired with the enduring proliferation of TrickBot, spells nothing but trouble for the security landscape, particularly for a potential explosion of ransomware, researchers said.


“Emotet is not a threat to be taken lightly, as seen in the past it can grow to monstrous scope,” they wrote. “The return can also cause an increase in ransomware attacks as Emotet is known to drop various ransomware in the past.”


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** [***REGISTER TODAY***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This*** [***LIVE, interactive Threatpost Town Hall***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***, sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***  

[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***for the LIVE event!***





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Emotet]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=RTM]] [[action.malware.name=Tor]] [[action.malware.name=TrickBot]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]] [[victim.industry.name=Finance]] [[victim.industry.name=Manufacturing]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Portugal]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Emotet]] [[Trickbot]] [[Ransomware]] [[Malware]] [[Cryptolaemus]] [[Threatpost]] [[ThreatPost]]
#### urls
https://t.co/imJDQTGqxV

