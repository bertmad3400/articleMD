# HP Omen Hub Exposes Millions of Gamers to Cyberattack
### A driver privilege-escalation bug gives attackers kernel-mode access to millions of PCs used for gaming.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169739)
+ Date: September 16, 2021  8:01 am
+ Author: Becky Bracken


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/16075545/the-omen-e1631793363106.jpg)
Millions of devices running the HP Omen Gaming Hub were using on a driver with a bug that could give attackers kernel-mode access without administrator privileges.


HP has since released a patch, but a new report on the flaw (CVE-2021-3437) from researchers from SentinelLabs details how the gaming software was built in part by copying [code from a problematic open-source driver](https://www.sentinelone.com/labs/cve-2021-3437-hp-omen-gaming-hub-privilege-escalation-bug-hits-millions-of-gaming-devices/) called WinRing0.sys.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


HP Omen Gaming Hub is software that comes pre-installed on HP Omen desktops and laptops and functions as an optimizer for playing games, making automatic adjustments to fan speeds, lighting and accessory controls for the best gaming experience, SentinelLabs’ report explained.


Metadata showed the researchers the HP OMEN Gaming Hub re-used code for its driver that is vulnerable unauthorized privilege escalation.


“Unfortunately, issues with the WinRing0.sys driver are well-known,” the SentinelLabs report said. “This driver enables user-mode applications to perform various privileged kernel-mode operations via (input/output controls) IOCTLs interface.”


The HP driver potentially offers access through IOCTLs using model specific registers (MSRs) to access or alter CPU data, researchers added.


“This high-severity flaw, if exploited, could allow any user on the computer, even without privileges, to escalate privileges and run code in kernel mode,” the report added. “Among the obvious abuses of such vulnerabilities are that they could be used to bypass security products.”


Once inside, attackers could gain lateral access to wider networks, Sentinel Labs reported.


Back in Oct. 2019, SafeBreach published their findings on the [same driver vulnerability](https://www.safebreach.com/blog/2019/hp-touchpoint-analytics/) in the HP Touchpoint Analytics Software, which could have clued threat actors into looking at similar vulnerabilities across other HP products.


[HP put out a fix](https://support.hp.com/us-en/document/ish_4610088-4610112-16/hpsbgn03726) on Sept. 14, adding that the company will both push out automatic updates as well as offer manual options for patching.


“To reduce the attack surface provided by device drivers with exposed IOCTLs handlers, developers should enforce strong ACLs on device objects, verify user input and not expose a generic interface to kernel-mode operations,” the report advised.


**Gaming Increasingly Under Cyber-Assault**
-------------------------------------------


This latest bug comes amid a wave of attacks aimed at gamers across all sorts of platforms. The analysts have not observed any attackers exploiting this vulnerability so far, the report said, but that doesn’t mean there aren’t attackers out there looking for the next high score on the group.


Over the summer, Akamai released its 2020 gaming report showing that [attacks on the video-game industry](https://threatpost.com/attackers-gaming-industry/167183/) exploded by 340 percent in 2020, thanks to armies of pandemic-weary people turning to games for entertainment. The report also found more attack traffic on the gaming industry than any other in 2020.


Gaming platform Steam was discovered earlier this year to have [malware lurking in profile images](https://threatpost.com/steam-gaming-delivering-malware/166784/) and in January, caches of [leaked insider credentials](https://threatpost.com/game-publishers-hit-by-leaked-credentials/162725/) were found up for sale on criminal marketplaces. More recently, a malicious network filter rootkit that would let attackers [spoof gamers’ geo-locations](https://threatpost.com/microsoft-malicious-rootkit-gaming/167323/), called Netfilter, was discovered circulating around gamer community.


For its part, HP was responsive to the issue, SentinelLabs added.


“While we haven’t seen any indicators that these vulnerabilities have been exploited in the wild up until now, using any OMEN-branded PC with the vulnerable driver utilized by OMEN Gaming Hub makes the user potentially vulnerable,” the researchers warned. “Therefore, we urge users of OMEN PCs to ensure they take appropriate mitigating measures without delay.”


***Rule #1 of Linux Security:**No cybersecurity solution is viable if you don’t have the basics down. **[JOIN](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)** Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the **[4 Golden Rules of Linux Security](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)**. Your top takeaway will be a Linux roadmap to getting the basics right! **[REGISTER NOW](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)**and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*


 


 




#### Tags:
[[Linux]] [[kernel-mode]] [[SentinelLabs]] [[IOCTLs]] [[added.]] [[ThreatPost]]
