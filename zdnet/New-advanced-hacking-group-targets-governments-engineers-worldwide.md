# New advanced hacking group targets governments, engineers worldwide
### The APT was one of many groups that took part in the Microsoft Exchange Server hacks.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/new-advanced-hacking-group-targets-governments-engineers-worldwide/)
+ Date: September 23, 2021
+ Author: Charlie Osborne


## Article:
Unknown

A new hacking group targeting entities worldwide to spy on them has been unmasked by researchers.  

Dubbed FamousSparrow by ESET, on Thursday, the team said that the advanced persistent threat (APT) group -- many of whom are state-sponsored -- is a new entry to the cyberespionage space.  

Believed to have been active since at least 2019, the APT has been linked to attacks against governments, international organizations, engineering firms, legal companies, and the hospitality sector.   

Victims are located in Europe, the United Kingdom, Israel, Saudi Arabia, Taiwan, Burkina Faso in West Africa, and the Americas -- including Brazil, Canada, and Guatemala.  

![screenshot-2021-09-23-at-10-15-23.png](https://www.zdnet.com/a/hub/i/r/2021/09/23/05d99713-493c-42c1-ad80-fc4d9e2b03f0/resize/1200xauto/7fcee909a0323b6a9c88b46ec64d9fd7/screenshot-2021-09-23-at-10-15-23.png)![screenshot-2021-09-23-at-10-15-23.png](https://www.zdnet.com/a/hub/i/r/2021/09/23/05d99713-493c-42c1-ad80-fc4d9e2b03f0/resize/1200xauto/7fcee909a0323b6a9c88b46ec64d9fd7/screenshot-2021-09-23-at-10-15-23.png)
 ESET
 ESET says that current threat data indicates that FamousSparrow is a separate group independent from other active APTs, however, there do appear to be several overlaps. In one case, exploit tools used by the threat actors were set up with a command-and-control (C2) server linked to the DRDControl APT, and in another, a variant of a loader employed by SparklingGoblin appears to have been in use. 


What makes this new APT interesting is that the group joined at least 10 other APT groups that exploited ProxyLogon, a chain of zero-day vulnerabilities [disclosed in March](https://www.zdnet.com/article/everything-you-need-to-know-about-microsoft-exchange-server-hack/) which was used to compromise Microsoft Exchange servers worldwide.  

The researchers say that ProxyLogon was first exploited by the group on March 3, before Microsoft released emergency patches to the public, which indicates "it is yet another APT group that had access to the details of the ProxyLogon vulnerability chain in March 2021." 






The APT tends to compromise internet-facing applications as its initial attack vector, and this does not only include Microsoft Exchange servers -- Microsoft SharePoint and Oracle Opera are in the line of fire, too.  

FamousSparrow is the only known APT to make use of a custom backdoor, dubbed SparrowDoor by the team. The backdoor is deployed via a loader and DLL search order hijacking, and once established, a link to the attacker's C2 is created for the exfiltration of data.  

In addition, FamousSparrow accounts for two customized versions of the open source, post-exploit password tool Mimikatz, a legitimate penetration testing kit that has been widely abused by cybercriminals. A version of this tool is dropped upon initial infection, as well as the NetBIOS scanner, Nbtscan, and a utility for gathering in-memory data, such as credentials.  

"This is another reminder that it is critical to patch internet-facing applications quickly, or, if quick patching is not possible, to not expose them to the internet at all," the researchers commented. "The targeting, which includes governments worldwide, suggests that FamousSparrow's intent is espionage." 

###  Previous and related coverage

* [Chinese APT LuminousMoth abuses Zoom brand to target gov't agencies](https://www.zdnet.com/article/chinese-apt-luminousmoth-abuses-zoom-brand-to-target-govt-agencies/)  

* [DeadRinger: Chinese APTs strike major telecommunications companies](https://www.zdnet.com/article/deadringer-chinese-apts-strike-major-telecommunications-companies/)  

* [New APT hacking group leverages 'KilllSomeOne' DLL side-loading](https://www.zdnet.com/article/new-active-hacking-group-leverages-killlsomeone-dll-side-loading/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0 



---





#### Tags:
[[FamousSparrow]] [[Microsoft]] [[ZDNet]]
