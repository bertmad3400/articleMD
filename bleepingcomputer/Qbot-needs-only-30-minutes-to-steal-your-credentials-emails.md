# Qbot needs only 30 minutes to steal your credentials, emails
### The widespread malware known as Qbot (aka Qakbot or QuakBot) has recently returned to light-speed attacks, and according to analysts, it only takes around 30 minutes to steal sensitive data after the initial infection.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/qbot-needs-only-30-minutes-to-steal-your-credentials-emails/
+ Date: 2022-02-08T03:12:24-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2020/12/09/Qbot.jpg)

![Qbot Trojan](https://www.bleepstatic.com/content/hl-images/2020/12/09/Qbot.jpg)


The widespread malware known as Qbot (aka Qakbot or QuakBot) has recently returned to light-speed attacks, and according to analysts, it only takes around 30 minutes to steal sensitive data after the initial infection.


According to a new report by DFIR, Qbot was performing these quick data-snatching strikes back in October 2021, and it now appears that the threat actors behind it have returned to similar tactics.


More specifically, the analysts report that it takes half an hour for the adversaries to steal browser data and emails from Outlook and 50 minutes before they jump to an adjacent workstation.


The timeline of an attack
-------------------------


As shown in the following diagram, Qbot moves quickly to perform privilege escalation immediately following an infection, while a full-fledged reconnaissance scan takes place within ten minutes.



![Timeline of a typical QBot attack](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/timeline(3).jpg)**Timeline of a typical Qbot attack**  
*Source: DFIR*
The initial access is typically achieved via an Excel (XLS) document that uses a macro to drop the DLL loader on the target machine. 


This payload then executes to create a scheduled task via the msra.exe process and elevates itself to system privileges.


Additionally, the malware adds the Qbot DLL to Microsoft Defender's exclusion list, so it won't be detected when injection into msra.exe happens.



![Discovery commands injected into msra.exe](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/discovery-commands.png)**Discovery commands injected into msra.exe**  
*Source: DFIR*
The malware steals emails in half an hour after the initial execution, which are then used for [replay-chain phishing attacks](https://www.bleepingcomputer.com/news/security/qbot-steals-your-email-threads-again-to-infect-other-victims/) and to be sold to other threat actors.


Qbot steals Windows credentials from memory using the LSASS (Local Security Authority Server Service) injections and from web browsers. These are leveraged for lateral movement to other devices on the network, initiated at an average of fifty minutes after first execution.



![QBot lateral movement](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Qbot lateral movement**  
*Source: DFIR*
Network tiptoeing
-----------------


Qbot moves laterally to all workstations in the scanned environment by copying a DLL to the next target and remotely creating a service to execute it. 


At the same time, the previous infection is cleared, so the machine that just had its credentials exfiltrated is disinfected and appears normal.


Moreover, the services created on the new workstations have the 'DeleteFlag' parameter, which causes them to be removed upon system reboot.



![Services created on the target workstation](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Services created on the target workstation**  
*Source: DFIR*
The lateral movement takes place rapidly, so if there's no network segmentation to protect the workstations, the situation becomes very challenging for defense teams.


Also, the Qbot threat actors often like to use some of the compromised systems as first-tier proxy points for easy address masking and rotation, and use multiple ports for SSL communication with the C2 server.


The impact of [these expeditious attacks](https://thedfirreport.com/2022/02/07/qbot-likes-to-move-it-move-it/) isn't limited to data loss, as Qbot has also been observed to drop ransomware payloads onto compromised corporate networks.


A Microsoft report from December 2021 captured the [versatility of Qbot attacks](https://www.bleepingcomputer.com/news/security/microsoft-these-are-the-building-blocks-of-qbot-malware-attacks/), making it harder to evaluate the scope of its infections accurately.


However, no matter how a Qbot infection unfolds precisely, it is essential to keep in mind that almost all begin with an email, so this is the main access point that organizations need to strengthen.


Today's announcement by Microsoft that they will be [blocking macros in downloaded documents by default](https://www.bleepingcomputer.com/news/microsoft/microsoft-plans-to-kill-malware-delivery-via-office-macros/) by removing the 'Enable Content' and 'Enable Editing' buttons will go a long way to protecting users from Qbot phishing attacks.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=QakBot]] [[action.malware.name=QakBot]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Qbot]] [[Dfir]] [[Malware]] [[Dll]] [[Microsoft]] [[Bleeping Computer]]

