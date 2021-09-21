# Turla hacking group launches new backdoor in attacks against US, Afghanistan
### The Russian cyberattackers are using the new module to become more stealthy.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/turla-hacking-group-launches-new-backdoor-in-attacks-against-us-afghanistan/)
+ Date: September 21, 2021 -- 12:00 GMT (13:00 BST)
+ Author: Charlie Osborne


## Article:
Unknown

The Turla hacking group is back with new weaponry, recently used in attacks against the US, Germany, and Afghanistan.


On Tuesday, [Cisco Talos said](https://blog.talosintelligence.com/2021/09/tinyturla.html) that the advanced persistent threat (APT) group, Russian in origin, has developed a new backdoor for persistence and stealth.  

Dubbed TinyTurla, the previously unknown backdoor is simple in design but suitable for particular purposes: dropping payloads and staying under the radar if Turla's primary malware is wiped from a compromised machine.  

Active since at least 2004, Turla, also known as [Snake and Uroburos](https://attack.mitre.org/groups/G0010/), is a sophisticated operation with a long list of high-profile victims in its portfolio. [Past targets](https://www.zdnet.com/article/turla-hacker-group-steals-antivirus-logs-to-see-if-its-malware-was-detected/) include the Pentagon, government and diplomatic agencies, military groups, research institutions, and more in at least 45 countries. 

Now, it appears the APT is honing in on the US, Germany, and also Afghanistan -- the latter of which being targeted before the Taliban took over the country and Western military forces pulled out.  

Talos says it is likely the malware was used in attempts to compromise the systems of the previous government.  

A sample acquired by the team revealed that the backdoor, which is formed as a .DLL, was installed as a service on a Windows machine. The file is named w64time.dll, and as there is a legitimate Windows w32time.dll, it may not immediately appear to be malicious. 






Named "Windows Time Service," the backdoor links to a command-and-control (C2) server controlled by Turla and contacts the system via an encrypted HTTPS channel every five seconds in order to check for any new commands or instructions.  

TinyTurla is able to upload and either execute files and payloads, create subprocesses, and exfiltrate data. It may be that the backdoor was limited in its functionality and code on purpose, to prevent detection as malicious software.  

Talos says that the backdoor has been in use since at least 2020.    

"One public reason why we attributed this backdoor to Turla is the fact that they used the same infrastructure as they used for other attacks that have been clearly attributed to their [Penguin Turla](https://www.leonardocompany.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9Dfinal.pdf/ee404bb4-8458-9206-bbb3-f1e8bcd2b042?t=1589526441442) Infrastructure," the researchers say. "It's often difficult for an administrator to verify that all running services are legitimate. It is important to have software and/or automated systems detecting unknown running services and a team of skilled professionals who can perform proper forensic analysis on potentially infected systems." 

Recently, [Kaspersky researchers](https://securelist.com/sunburst-backdoor-kazuar/99981/) found code overlaps between Turla, the DarkHalo/UNC2452 APT, the Sunburst backdoor, and the Kazuar backdoor. While there are shared features between Sunburst and Kazuar, it is not possible to conclude with certainty any concrete links between the threat groups and these tools.  

###  Previous and related coverage

* [Turla hacker group steals antivirus logs to see if its malware was detected](https://www.zdnet.com/article/turla-hacker-group-steals-antivirus-logs-to-see-if-its-malware-was-detected/)  

* [Cyber-espionage campaign opens backdoor to steal documents from infected PCs](https://www.zdnet.com/article/cyber-espionage-campaign-opens-backdoor-to-steal-documents-from-infected-pcs/)  

* [US Cyber Command exposes new Russian malware](https://www.zdnet.com/article/us-cyber-command-exposes-new-russian-malware/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Turla]] [[malware]] [[Talos]] [[ZDNet]]
