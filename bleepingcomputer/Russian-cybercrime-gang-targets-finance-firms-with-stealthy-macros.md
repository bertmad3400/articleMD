# Russian cybercrime gang targets finance firms with stealthy macros
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/russian-cybercrime-gang-targets-finance-firms-with-stealthy-macros/)
+ Date: October 15, 2021
+ Author: Bill Toulas


## Article:
![hacker](https://www.bleepstatic.com/content/hl-images/2021/09/13/Hacker.jpg?rand=28208192)


A new phishing campaign dubbed MirrorBlast is deploying weaponized Excel documents that are extremely difficult to detect to compromise financial service organizations


The most notable feature of MirrorBlast is the low detection rates of the campaign's malicious Excel documents by security software, putting firms that rely solely upon detection tools at high risk.


Featherlight macro with zero detections
---------------------------------------


The developers of these malicious documents have made considerable effort to obfuscate malicious code, achieving zero detections on VirusTotal.



![VirusTotal results](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/detection.png)**VirusTotal results coming up with no detections**  

Source: Morphisec
However, these optimized documents have drawbacks that the actors are apparently willing to accept as trade-offs. Most notably, the macro code can only be executed on a 32-bit version of Office.


 


If the victim is tricked into opening the malicious document and “enable content” in Microsoft Office, the macro executes a JScript script which downloads and installs an MSI package."


Prior to that though, the macro performs a basic anti-sandboxing check on whether the computer name is equal to the user domain, and if the username is equal to 'admin' or 'administrator'.


According to researchers at Morphisec who analyzed several samples of the dropped MSI package, it comes in two variants, one written in REBOL and one in KiXtart.



![MirrorBlast attack chain](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/mirrorblast%20diagram.jpg)**MirrorBlast attack chain**  

Source: Morphisec
The REBOL variant, which is base64 encoded, begins by exfiltrating information like the username, OS version, and architecture.


Next, it waits for a C2 command that initiates a Powershell which will fetch the second stage. The researchers weren’t able to retrieve that stage though, so its functions are unknown.


The KiXtart payload is also encrypted and also attempts to exfiltrate basic machine information to the C2, including the domain, computer name, user name, and process list.


A highly motivated threat actor
-------------------------------


The actors behind the campaign appear to be ‘TA505,’ an active Russian threat group that has [a long history](https://www.bleepingcomputer.com/news/security/new-sdbot-remote-access-trojan-used-in-ta505-malspam-campaigns/) of creativity in the way they lace Excel documents in [malspam campaigns](https://www.bleepingcomputer.com/news/security/microsoft-detects-new-ta505-malware-attacks-after-short-break/).


[Morphisec](https://blog.morphisec.com/explosive-new-mirrorblast-campaign-targets-financial-companies) was able to link the actors with the MirrorBlast campaign thanks to infection chain similarities with past operations, the abuse of OneDrive, the particularities in domain naming methods, and the existence of an MD5 checksum mismatch that points to a 2020 attack launched by TA505.


 


TA505 is a highly sophisticated threat actor that is known for a wide-range of malicious activity over the years.



![Sample of TA505's working schedule](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Sample of TA505's working schedule from a past campaign**  

Source: NCCGroup
An [NCCGroup analysis](https://blog.fox-it.com/2020/11/16/ta505-a-brief-history-of-their-time/) on the actor’s work schedule reflects an organized and well-structured group that utilizes zero-day vulnerabilities and a variety of malware strains in its attacks. This includes the deployment of Clop ransomware in double-extortion attacks.


TA505 is also attributed to numerous attacks using a [zero-day vulnerability](https://www.bleepingcomputer.com/news/security/global-accellion-data-breaches-linked-to-clop-ransomware-gang/) in Accenture FTA secure file sharing devices to steal data from organizations.


The threat actors then attempted to extort the companies by demanding $10 million ransoms to not publicly leak the data on their Clop data leak site.


As such, the IT teams at the financial organizations targeted by the MirrorBlast campaign cannot afford to lower their shields even for a moment.




#### Tags:
[[MirrorBlast]] [[Morphisec]] [[Source:]] [[TA505]] [[Bleeping Computer]]
