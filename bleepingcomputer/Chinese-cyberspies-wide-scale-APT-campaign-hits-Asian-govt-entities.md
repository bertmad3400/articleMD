# Chinese cyberspies’ wide-scale APT campaign hits Asian govt entities
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/chinese-cyberspies-wide-scale-apt-campaign-hits-asian-govt-entities/)
+ Date: July 14, 2021
+ Author: Sergiu Gatlan


## Article:
![Chinese cyberspies’ wide-scale APT campaign hits Asian govt entities](https://www.bleepstatic.com/content/hl-images/2021/05/28/China-world-map.jpg)


Kaspersky researchers have revealed an ongoing and large-scale advanced persistent threat (APT) campaign with hundreds of victims from Southeast Asia, including Myanmar and the Philippines government entities.


This cluster of APT activity, tracked as LuminousMoth by Kaspersky, has been linked to the [HoneyMyte](https://securelist.com/ksb-2019-review-of-the-year/95394/#established-threat-actors-continue-to-revamp-their-tools) Chinese-speaking threat group with medium to high confidence.



The links found include network infrastructure connections such as command-and-control servers used by both groups and similar tactics, techniques, and procedures (TTPs) when deploying Cobalt Strike beacon payloads. 


They are also both known to launch wide-scale attacks against significant numbers of targets with the end goal of hitting just a small subset matching their interests.


While analyzing LuminousMoth's cyberespionage attacks against several Asian government entities that started since at least October 2020, Kaspersky researchers discovered a total of 100 victims in Myanmar and 1,400 in the Philippines.


"The massive scale of the attack is quite rare. It's also interesting that we've seen far more attacks in the Philippines than in Myanmar," Kaspersky GReAT security researcher Aseel Kayal said.


"This could be due to the use of USB drives as a spreading mechanism or there could be yet another infection vector that we're not yet aware of being used in the Philippines."



![LuminousMoth and HoneyMyte C2 connections](https://www.bleepstatic.com/images/news/u/1109292/2021/LuminousMoth-vs-HoneyMyte.png)*LuminousMoth and HoneyMyte C2 connections (Kaspersky)*
Malware spreading via USB drives reaches wide
---------------------------------------------


The threat actors use spear-phishing emails with malicious Dropbox download links that deliver RAR archives camouflaged as Word documents and bundling malware payloads to gain access to their targets' systems.


After being executed on a victim's device, the malware tries to make its way onto other systems via removable USB drives together with files stolen from already compromised computers.


LuminousMoth's malware also features post-exploitation tools that the operators can use for later movement within their victims' networks: one of them being hidden in plain sight in the form of a fake Zoom app and the other designed to steal Chrome browser cookies


The threat actors exfiltrate data collected from infected devices to their command and control (C2) servers which, in some cases, were impersonating news outlets to evade detection.


Once downloaded on a system, the malware attempts to infect other hosts by spreading through removable USB drives. If a drive is found, the malware creates hidden directories on the drive where it then moves all of the victim's files, along with the malicious executables. 


"This new cluster of activity might once again point to a trend we've been witnessing over the course of this year: Chinese-speaking threat actors re-tooling and producing new and unknown malware implants," Kaspersky GReAT senior security researcher Mark Lechtik added.


Further technical details and a list of indicators of compromise (IOCs), including malware hashes and C2 domains, can be found at the end of [Kaspersky's report](https://securelist.com/apt-luminousmoth/103332/).




#### Tags:
[[Kaspersky]] [[malware]] [[LuminousMoth]] [[USB]] [[Myanmar]] [[C2]] [[Bleeping Computer]]
