# Trickbot will now try to crash researcher PCs to stop reverse engineering attempts | ZDNet
### The Trojan has been refreshed with a new set of anti-analysis capabilities.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/trickbot-will-now-try-to-crash-researcher-pcs-to-stop-reverse-engineering-attempts/
+ Date: 2022-01-26 10:00:17
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/3738498680c17b6b3158d928bd8364509fc02995/2020/04/06/f5b9f560-7814-4367-9256-8debb106c2ff/istock-1145361636.jpg?width=770&height=578&fit=crop&auto=webp)

The Trickbot Trojan has been revised with a new set of anti-reverse engineering features including the capability to crash computers if analysis tools are detected.


Over the years, Trickbot has evolved from its original state as a banking Trojan to a wider suite of malicious components. 

Following the retirement of [Dyre](https://www.zdnet.com/article/dyre-successor-trickbot-attacks-australian-banks/) in 2016 and the disruption of the [Emotet botnet](https://www.zdnet.com/article/emotet-worlds-most-dangerous-malware-botnet-disrupted-by-international-police-operation/) by law enforcement in 2021, Trickbot has filled the gap for many threat actors and is now used to steal financial data and to facilitate the execution of ransomware – and due to its versatile, modular nature, has also become a popular option for deploying other forms of malware. 

"Between takedown attempts and a global pandemic, it has been diversifying its monetization models and growing stronger," researchers from IBM Trusteer say. 

In [a new report](https://securityintelligence.com/posts/trickbot-bolsters-layered-defenses-prevent-injection/) on the malware's current development, IBM Trusteer has found that the malware's usage continues to escalate and samples of recent Trickbot injections have revealed new features designed to prevent analysis.  

Reverse engineering in cybersecurity aims to dissect a malware sample, dismantling the code to find out how it operates -- and potentially how to defend against it. There are three major lines of defense used by the malware to try and prevent reverse engineering from being successful outside of typical obfuscation. 

The first trick used by the Trojan is the use of server-side injections, rather than loading them from infected machines. 






"Keeping injections on infected machines means they are more likely to land in the hands of security researchers," the researchers explained. "Injections kept locally are also less agile and harder to manipulate in real-time. To move beyond these risks, Trickbot's operators inject from their server, known as server-side injections. To facilitate fetching the right injection at the right moment, the resident Trickbot malware uses a downloader or a JavaScript (JS) loader to communicate with its inject server." 

The second method of note is the use of HTTPS communication when injections are fetched from Trickbot's command-and-control (C2) server. Flags are used to specify the page a victim is browsing and requests from unknown – or "unwelcome" – sources can be ignored, locking up data streams and barring researchers from properly analyzing communication flows.  

Certificate errors are also blocked to stop victims from being aware of the C2 server link.  

The third line of defense, however, is the most interesting update. An anti-debugging script has been added to code that can trigger a memory overload if a security researcher performs "code beautifying," a technique use to make large swathes of code more readable and easier to analyze.  

If Trickbot detects this type of decoding, the malware will throw itself into a loop.  

"TrickBot uses a RegEx to detect the beautified setup and throw itself into a loop that increases the dynamic array size on every iteration. After a few rounds, memory is eventually overloaded, and the browser crashes," the team says. "The goal is to anticipate the typical actions researchers will take and ensure their analysis fails." 

IBM Trusteer says that Base64 obfuscation, redundant junk script and code, and native function patches are also used to sideline and confuse researchers.  

In other security news this month, the FBI [issued a warning](https://www.zdnet.com/article/fbi-warning-this-new-ransomware-makes-demands-of-up-to-500000/) related to the spread of Diavol ransomware, a strain of malware that uses similar machine fingerprint methods to Trickbot in identifying victim PCs.   

###  Previous and related coverage

* [This trojan malware is now your biggest security headache](https://www.zdnet.com/article/this-trojan-malware-is-now-your-biggest-security-headache/)
* [FBI warning: This new ransomware makes demands of up to $500,000](https://www.zdnet.com/article/fbi-warning-this-new-ransomware-makes-demands-of-up-to-500000/)
* [US Justice Department accuses Latvian national of deploying Trickbot malware](https://www.zdnet.com/article/us-justice-department-accuses-latvian-national-of-creating-and-deploying-trickbot-malware/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Dyre]] [[action.malware.name=Elise]] [[action.malware.name=Emotet]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=RTM]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=TrickBot]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Latvia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Trickbot]] [[Malware]] [[Ransomware]] [[Trusteer]] [[ZDNet]]

