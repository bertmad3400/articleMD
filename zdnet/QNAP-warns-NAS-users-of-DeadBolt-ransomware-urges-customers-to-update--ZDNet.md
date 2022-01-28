# QNAP warns NAS users of DeadBolt ransomware, urges customers to update | ZDNet
### QNAP released a warning this week about a ransomware strain targeting all NAS instances exposed to the internet.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/qnap-warns-nas-users-of-deadbolt-ransomware-urges-customers-to-update/
+ Date: 2022-01-27 22:59:07
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/ef8e6f6aeacf39cd54e9bf9420044e300d46d280/2020/07/30/8b685d65-9d29-4c8b-80c1-6b75797773a3/cisa-says-62000-qnap-nas-devices-have-be-5f2171d1931ab320db2de039-1-jul-30-2020-14-50-40-poster.jpg?width=770&height=578&fit=crop&auto=webp)

Taiwanese network-attached storage giant QNAP [urged](https://www.qnap.com/en/security-news/2022/take-immediate-actions-to-stop-your-nas-from-exposing-to-the-internet-and-fight-against-ransomware-together) its customers to update their systems this week after the DeadBolt ransomware was discovered targeting all NAS instances exposed to the internet.

"QNAP urges all QNAP NAS users to follow the security setting instructions below to ensure the security of QNAP NAS and routers, and immediately update QTS to the latest available version," the company said in a statement. 

Attached to the statement is a [detailed guide](https://www.qnap.com/go/how-to/faq/article/how-to-know-which-ports-on-the-router-are-opened-to-the-internet) for customers, noting that if you go to the Security Counselor on your QNAP NAS and see "The System Administration service can be directly accessible from an external IP address via the following protocols: HTTP" on the dashboard, you are at high risk. 

"If your NAS is exposed to the Internet, please follow the instructions below to ensure NAS security: Go to the management interface of your router, check the Virtual Server, NAT or Port Forwarding settings, and disable the port forwarding setting of NAS management service port (port 8080 and 443 by default)," the company said. 

"Go to myQNAPcloud on the QTS menu, click the "Auto Router Configuration", and unselect "Enable UPnP Port forwarding."

Two days ago, dozens of people took to [QNAP message boards](https://forum.qnap.com/viewtopic.php?f=45&t=164797&start=30) and [Reddit](https://www.reddit.com/r/qnap/comments/scm0zv/deadbolt_ransomware_attack_against_qnaps/) to say they logged on only to find the Deadbolt ransomware screen. People reported losing decades of photos, videos and irreplaceable files. Even an MIT professor was hit. 




> I just got hacked. Ransomware named DeadBolt found an exploit in [@QNAP\_nas](https://twitter.com/QNAP_nas?ref_src=twsrc%5Etfw) storage devices, encrypting all files. They ask $1,000 from individuals or $1.8 million from QNAP. I have 50tb of data there, none of it essential or sensitive, but it hurts a lot. Time for a fresh start. [pic.twitter.com/E8ZkyIbdfp](https://t.co/E8ZkyIbdfp)
> 
> — Lex Fridman (@lexfridman) [January 27, 2022](https://twitter.com/lexfridman/status/1486609372176429057?ref_src=twsrc%5Etfw)




One user on Reddit said they were saved because they had a folder titled "Absolutely Worthless" at the top of their directory full of data. The ransomware started with that folder, giving them time to pull the plug before it encrypted anything of value. 






The ransom note demands .03 of Bitcoin for the decryption key and says, "You have been targeted because of the inadequate security provided by your vendor (QNAP)." At least one user on Reddit reported paying the ransom and not getting the decryption key. 

![fmdg2mw.png]()![fmdg2mw.png](https://www.zdnet.com/a/img/resize/f7cde90990a23d58610f7ff1f57017b9793a9aa3/2022/01/27/b940b0bc-f42a-44a7-b83f-99eb6a213608/fmdg2mw.png?width=370&fit=bounds&auto=webp)
 QNAP message board
 On the QNAP message board, someone shared a message from the Deadbolt ransomware group that was allegedly sent to QNAP. 

"All you affected customers have been targeted using a zero-day vulnerability in your product. We offer you two options to mitigate this (and future) damage," the group said.  

The group demanded a Bitcoin payment of 5 BTC in exchange for details about an alleged zero day used to launch the attack or 50 BTC for a universal decryption master key and information about the zero day. 

"There is no way to contact us. These are our only offers," the alleged message says. 

QNAP did not respond to requests for comment about whether a zero day was used during the attack. 

Chris Morgan, senior cyber threat intelligence analyst at Digital Shadows, said QNAP NAS devices have been a frequent target of ransomware groups, including by the QLocker ransomware in April 2021 and January 2021 as well as the [ech0raix ransomware](https://www.theregister.com/2021/04/22/qnap_nas_ransomware_qlocker_ech0raix/) in December 2020. QNAP [has also been hit](https://www.zdnet.com/article/unityminer-cryptocurrency-malware-hijacks-qnap-storage-devices/) by [malware](https://www.zdnet.com/article/qnap-warns-users-of-a-new-crypto-miner-named-dovecat-infecting-their-devices/) in the past. 

"The latest activity—which has been attributed to the Deadbolt ransomware—is reportedly unsophisticated and relies on targeting unpatched devices. Mitigation for this attack—and other similar ransomware variants—can be achieved simply by ensuring devices are not internet facing and are routinely patched with the most regular updates," Morgan explained. 

Vulcan Cyber's Mike Parkin questioned why an organization would have a NAS system exposed on the internet in the first place, noting that while there may be some business cases for making mass storage available to outsiders, there is no reason to have administration functions available through an unencrypted, unauthenticated, connection. 

"Cases like this highlight how important it is to be sure systems are deployed and maintained to industry best practices. Network scanning and vulnerability management tools can work together to identify risky configurations after the fact, but it's always best to make sure systems are deployed securely in the first place," Parkin said. 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Derusbi]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Location:
[[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Qnap]] [[Nas]] [[Ransomware]] [[Reddit]] [[Deadbolt]] [[ZDNet]]

