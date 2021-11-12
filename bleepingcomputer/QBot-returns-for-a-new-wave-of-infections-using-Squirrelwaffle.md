# QBot returns for a new wave of infections using Squirrelwaffle
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/qbot-returns-for-a-new-wave-of-infections-using-squirrelwaffle/)
+ Date: November 12, 2021
+ Author: Bill Toulas


## Article:
![qbot](https://www.bleepstatic.com/content/hl-images/2020/12/09/Qbot.jpg?rand=1835478057)


The activity of the QBot (also known as Quakbot) banking trojan is spiking again, and analysts from multiple security research firms attribute this to the rise of Squirrelwaffle.


Squirrelwaffle [emerged last month](https://www.bleepingcomputer.com/news/security/spammers-use-squirrelwaffle-malware-to-drop-cobalt-strike/) as one of the most likely candidates to fill the void left by the take-down of Emotet, and unfortunately, these predictions are quickly being confirmed.


A new wave of attacks
---------------------


Researchers at [TrendMicro](https://www.trendmicro.com/en_us/research/21/k/qakbot-loader-returns-with-new-techniques-and-tools.html) have observed a new distribution campaign for QBot relying on Visual Basic Macros (VBA) macros in Microsoft Word documents sent as attachments in phishing emails.


Previous Qbot campaigns used Excel macros, which are still present in some cases, even if they are more scarce now.



![All of QBot's arrival variations ](https://www.bleepstatic.com/images/news/u/1220909/Security/qbot%20infections.jpg)**All of QBot's arrival variations**  
*Source: TrendMicro*
The victim still has to manually open the document and “Enable Content” on their Microsoft Office suite to let the macro code run, dropping a QBot payload on the system.


The rest of the process chain hasn't changed much compared to previous versions, still downloading a DLL file as the core payload and setting the same scheduled task for persistence as before.


Qbot is also known to partner with ransomware operations to provide them with initial access to a network. QBot has previously collaborated with ransomware gangs to deploy REvil, [Egregor](https://www.bleepingcomputer.com/news/security/qbot-partners-with-egregor-ransomware-in-bot-fueled-attacks/), [ProLock](https://www.bleepingcomputer.com/news/security/prolock-ransomware-teams-up-with-qakbot-trojan-for-network-access/), PwndLocker, and MegaCortex strains.


We shouldn't forget that even if these compromises never evolve to file-encryption events, QBot can do significant damage on its own.


The additional modules downloaded by the QBot malware can grab browser cookies, passwords, emails, drop Cobalt Strike, enable lateral movement, and turn the infected machine into a proxy for C2 traffic.


Riding the Squirrel
-------------------


[Sentinel Labs](https://www.sentinelone.com/blog/is-squirrelwaffle-the-new-emotet-how-to-detect-the-latest-malspam-loader/) published a report on the rise of the SquirrelWaffle malware loader, linking it directly to QBot, which is dropped as second stage malware.


Researchers at [Minerva Labs](https://blog.minerva-labs.com/a-new-datoploader-delivers-qakbot-trojan) have also drawn a similar conclusion, seeing the following delivery scheme:



![SquirrelWaffle's infection chain](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/infection%20chain.jpg)**SquirrelWaffle's infection chain**  
*Source: Minerva Labs*
SquirrelWaffle also uses VBA macros to execute a PowerShell command that retrieves its payload and launches it.


Unlike Emotet, who used a [wide range](https://www.bleepingcomputer.com/news/security/emotet-returns-with-thanksgiving-theme-and-better-phishing-tricks/) of [phishing lures](https://www.bleepingcomputer.com/news/security/emotet-trojan-brings-a-malware-scare-with-halloween-emails/), the SquirrelWaffle is not doing a great job creating convincing spam mails, keeping the infections in check.


The creation of more convincing phishing emails could be outsourced or quickly resolved by contacting an expert in that part of phishing operations, leading to a more significant number of SquirrelWaffle infections.




#### Tags:
[[QBot]] [[SquirrelWaffle]] [[phishing]] [[Bleeping Computer]]
