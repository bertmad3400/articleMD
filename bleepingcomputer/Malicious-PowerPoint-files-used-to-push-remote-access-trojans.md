# Malicious PowerPoint files used to push remote access trojans
### Since December 2021, a growing trend in phishing campaigns has emerged that uses malicious PowerPoint documents to distribute various types of malware, including remote access and information-stealing trojans.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/malicious-powerpoint-files-used-to-push-remote-access-trojans/
+ Date: 2022-01-24T09:37:15-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/04/16/malware-phishing-header.jpg)

![Malware spread via phishing](https://www.bleepstatic.com/content/hl-images/2021/04/16/malware-phishing-header.jpg)


Since December 2021, a growing trend in phishing campaigns has emerged that uses malicious PowerPoint documents to distribute various types of malware, including remote access and information-stealing trojans.


According to a report by Netskope’s Threat Labs shared with Bleeping Computer before publication, the actors are using PowerPoint files combined with legitimate cloud services that host the malware payloads.


The families deployed in the tracked campaign are Warzone (aka AveMaria) and AgentTesla, two powerful RATs and info-stealers that target many applications, while the researchers also noticed the dropping of cryptocurrency stealers.


Sliding malware into Windows devices
------------------------------------


The malicious PowerPoint phishing attachment contains obfuscated macro executed via a combination of PowerShell and MSHTA, both built-in Windows tools.


The VBS script is then de-obfuscated and adds new Windows registry entries for persistence, leading to the execution of two scripts. The first one fetches AgentTesla from an external URL, and the second disables Windows Defender.



![VBS execution stages](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/vbs-execution-stages.jpg)**VBS execution stages**  
*Source: Netskope*
Additionally, the VBS creates a scheduled task that executes a script every hour, which fetches a PowerShell cryptocurrency stealer from a Blogger URL.



![Blogger page abused for dropping payloads](https://www.bleepstatic.com/images/news/u/1220909/Website%20snaps/blogger-page.jpg)**Blogger page abused for dropping payloads**  
*Source: Netskope*
The malware payloads
--------------------


AgentTesla is a .NET-based RAT (remote access trojan) that can steal browser passwords, log keystrokes, steal clipboard contents, etc.


It is executed by PowerShell and comes slightly obfuscated, while there’s also a function that injects the payload into an instance of “aspnet\_compiler.exe”.



![PowerShell that executes AgentTesla](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**PowerShell that executes AgentTesla**  
*Source: Netskope*
The second payload delivered in this campaign is Warzone, also a RAT, but Netskope doesn’t give many details about it in the report.


The cryptocurrency stealer is the third payload of this campaign, which checks the clipboard data with a regex that matches cryptocurrency wallet patterns. If found, it replaces the recipient’s address with one under the actor’s control.


The stealer supports Bitcoin, Ethereum, XMR, DOGE, and more. Netskope has published the complete list of IoCs (indicators of compromise) for this campaign, including all wallets used by the actors on [this GitHub page](https://github.com/netskopeoss/NetskopeThreatLabsIOCs/tree/main/AgentTesla/IOCs).



![Some of the wallets that actors use for stealing crypto](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Some of the wallets that adversaries use for snatching crypto**  
*Source: Netskope*
PowerPoint becoming a problem
-----------------------------


In December 2021, Fortinet reported about a similar [DHL-themed](https://www.bleepingcomputer.com/news/security/dhl-dethrones-microsoft-as-most-imitated-brand-in-phishing-attacks/) campaign that [also used PowerPoint documents](https://www.bleepingcomputer.com/news/security/phishing-campaign-uses-powerpoint-macros-to-drop-agent-tesla/) to drop Agent Tesla.


Users must treat this document type with as much vigilance as they have when receiving Excel files since macro code in PP files can be equally as dangerous and catastrophic.


In this case, the actors also threw cloud services in the mix, hosting their malicious payloads on various legitimate platforms that are unlikely to raise any red flags with security tools.


As such, the most dependable protection measure is to handle all unsolicited communications with caution and also to keep macros on your Microsoft Office suite disabled.





## Tags:

#### Action:
[[action.malware.name=Agent Tesla]] [[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=CHOPSTICK]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Netskope]] [[Powerpoint]] [[Malware]] [[Windows]] [[Powershell]] [[Agenttesla]] [[Vbs]] [[Bleeping Computer]]

