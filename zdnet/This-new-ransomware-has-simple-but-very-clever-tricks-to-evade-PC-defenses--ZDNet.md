# This new ransomware has simple but very clever tricks to evade PC defenses | ZDNet
### 'Up-and-coming' ransomware strain is ramping up attacks.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/this-new-ransomware-has-simple-but-very-clever-tricks-to-evade-pc-defenses/
+ Date: 2021-12-23 11:28:47
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/f06cee73e7dec3048bb3073f4f25cb600225502a/2020/10/30/388263c2-6ef9-4278-ada2-3bd0a5d26e0d/istock-11296385861.jpg?width=770&height=578&fit=crop&auto=webp)

AvosLocker, a newcomer to the ransomware service scene, is ramping up attacks while using some new techniques to try and evade security software.

Security firm Sophos warns that AvosLocker, a human-operated ransomware gang that emerged this summer, is [on the hunt for partners](https://blog.malwarebytes.com/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners/) – such as ['access brokers' who sell access to already-hacked machines](https://www.zdnet.com/article/log4j-flaw-now-state-backed-hackers-are-using-bug-as-part-of-attacks-warns-microsoft/) – in the hope of filling the gap [left by REvil's withdrawal](https://www.zdnet.com/article/revil-ransomware-group-resurfaces-after-brief-hiatus/).  


One of the key features of AvosLocker is using the AnyDesk remote IT administration tool and running it Windows Safe Mode. The latter option was used by REvil, Snatch and BlackMatter as a way to disable a target's intended security and IT admin tools. As Sophos points out, many endpoint security products do not run in Safe Mode – a special diagnostic configuration in which Windows disables most third-party drivers and software, and can render otherwise protected machines unsafe.

**SEE:** [**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/#link=%7B%22role%22:%22standard%22,%22href%22:%22http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22%3Cstrong%3EA%20winning%20strategy%20for%20cybersecurity%3C/strong%3E%22%7D) **(ZDNet special report)**

AnyDesk, a legitimate remote admin tool, has [become a popular alternative](https://www.trendmicro.com/en_us/research/18/e/legitimate-application-anydesk-bundled-with-new-ransomware-variant.html) among criminals to TeamViewer, which offered the same functionality. Running AnyDesk in Safe Mode while connected to the network allows the attacker to maintain control of infected machines. 

While AvosLocker merely repackages techniques from other gangs, Peter Mackenzie, director of incident response at Sophos, [described their use as](https://www.sophos.com/en-us/press-office/press-releases/2021/12/avoslocker-ransomware-uses-anydesk-in-safe-mode-to-launch-attacks.aspx) "simple, but very clever".    

Mackenzie says that while Avos copied the Safe Mode technique, installing AnyDesk for command and control of machines while in Safe Mode is a first. 






The AvosLocker attackers reboot the machines into Safe Mode for the final stages of the attack, but also modify the Safe Mode boot configuration to allow AnyDesk to be installed and run.

Sophos [notes in a blogpost](https://news.sophos.com/en-us/2021/12/22/avos-locker-remotely-accesses-boxes-even-running-in-safe-mode/) that legitimate owners might not be able to remotely manage a computer if it is configured to run AnyDesk in Safe Mode. An admin might need physical access to the infected computer to manage it, which could pose problems for a large network of Windows PCs and servers. 

Sophos has detected several more curious techniques used by AvosLocker. A Linux component, for example, targets VMware ESXi hypervisor servers by killing any virtual machines (VMs), then encrypting the VM files. Sophos is investigating how the attackers obtained the admin credentials needed to enable the ESX Shell or access the server. 

**SEE:** [**Hackers are turning to this simple technique to install their malware on PCs**](https://www.zdnet.com/article/hackers-are-turning-to-this-simple-technique-to-install-their-malware-on-pcs/#link=%7B%22linkText%22:%22Hackers%20are%20turning%20to%20this%20simple%20technique%20to%20install%20their%20malware%20on%20PCs%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/hackers-are-turning-to-this-simple-technique-to-install-their-malware-on-pcs/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

The attackers also used the IT management tool PDQ Deploy to push several Windows batch scripts to intended target machines, including Love.bat, update.bat, and lock.bat. As Sophos explains, in about five seconds, these scripts disable security products that can run in Safe Mode, disable Windows Defender, and allow the attacker's AnyDesk tool to run in Safe Mode. They also set up a new account with automatic login details and then connects to the target's domain controller to remotely access and run the ransomware executable, update.exe.      

Sophos warns: "Ransomware, especially when it has been hand-delivered (as has been the case in these Avos Locker instances), is a tricky problem to solve because one needs to deal not only with the ransomware itself, but with any mechanisms the threat actors have set up as a back door into the targeted network. No alert should be treated as "low priority" in these circumstances, no matter how benign it might seem." 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=REvil]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=Oslo]] [[victim.country.name=Norway]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Sophos]] [[Avoslocker]] [[Anydesk]] [[Windows]] [[Ransomware]] [[ZDNet]]

