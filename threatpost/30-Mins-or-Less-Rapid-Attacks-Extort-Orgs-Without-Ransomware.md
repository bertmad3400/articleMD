# 30 Mins or Less: Rapid Attacks Extort Orgs Without Ransomware
### The previously unknown SnapMC group exploits unpatched VPNs and webserver apps to breach systems and carry out quick-hit extortion in less time than it takes to order a pizza.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175445)
+ Date: October 13, 2021  7:22 am
+ Author: Becky Bracken


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/13071817/pizza-delivery-e1634123918695.jpg)
In less time than it takes to get a stuffed crust pizza delivered, a new group called SnapMC can breach an organization’s systems, steal their sensitive data, and demand payment to keep it from being published, according to a new [report from NCC Group’s threat intelligence team](https://blog.fox-it.com/2021/10/11/snapmc-skips-ransomware-steals-data/) — no ransomware required.


Rather than disrupting business operations by locking down a target’s data and systems, SnapMC just focuses on straight-up extortion. However, this low-tech, ransomware-free approach to extortion on a compressed timeline relies on known vulnerabilities with patches readily available.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“In the extortion emails we have seen from SnapMC have given victims 24 hours to get in contact and 72 hours to negotiate,” the report said. “These deadlines are rarely abided by, since we have seen the attacker to start increasing the pressure well before countdown hits zero.”


The researchers weren’t able to link the group to any known threat actors and gave it the name for it’s speed (“Snap”) and its mc.exe exfiltration tool of choice.


As evidence the group has the data, SnapMC provides victims with a list of the exfiltrated data. If they fail to engage in negotiations within the timeframe, the attackers threaten to publish the data and report the breach to customers and the media.


Analysts said they’ve observed SnapMC successfully breaching unpatched and vulnerable VPNs using the [CVE-2019-18935](https://nvd.nist.gov/vuln/detail/CVE-2019-18935) remote code execution bug in Telerik UI for ASPX.NET, and webserver apps using SQL injections.


**VPN Vulnerabilities**
-----------------------


A recent rise in VPN vulnerabilities has left companies exposed, according to Hank Schless, a senior manager with Lookout cloud security.


“While VPN solutions have their place, there have been multiple stories of vulnerabilities within these solutions that were exploited in the wild,” Schless explained to Threatpost. “Ensuring that only authorized and secure users or devices can access corporate infrastructure requires zero trust network access (ZTNA) policies for on-premise or private apps and cloud access security broker (CASB) capabilities for cloud-based apps and infrastructure.”


Last June the Colonial Pipeline was breached with an [old VPN password](https://threatpost.com/darkside-pwned-colonial-with-old-vpn-password/166743/). And last July [SonicWall issued a patch](https://threatpost.com/sonicwall-vpn-bugs-attack/167824/) for a bug in its old VPN models no longer supported by the company after attacks came to light — which were part of an ongoing wider campaign to exploit ([CVE-2019-7418](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-7481)).


The following month, [Cisco Systems issued a handful of patches](https://threatpost.com/critical-cisco-bug-vpn-routers/168449/) for the 8,800 Gigabit VPN routers vulnerable to compromise through [CVE-2021-1609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-1609).


And by late last month, the National Security Agency (NSA) and Cybersecurity and Infrastructure Security Agency (CSIA) issued guidance to the Department of Defense, National Security Systems and the Defense Industrial Base to [harden their VPNs](https://threatpost.com/vpns-nsa-cisa-guidance/175150/) against threats from multiple nation-state advanced persistent threat (APT) actors.


Nation-state actors aside, basic patching would protect against this latest smash-and-grab attempt at data extortion from the likes of SnapMC.


**Ransomware’s Evolution**
--------------------------


Oliver Tavakoli, CTO with Vectra, said that getting rid of the encryption piece of the attack altogether is a “natural evolution” of the ransomware [business model](https://threatpost.com/ransomware-volumes-record-highs-2021/168327/). The NCC team likewise predicts the trend toward simple attacks on shorter timelines is likely to continue.


“NCC Group’s Threat Intelligence team predicts that data-breach extortion attacks will increase over time, as it takes less time, and even less technical in-depth knowledge or skill in comparison to a full-blown ransomware attack,” the team said. “Therefore, making sure you are able to detect such attacks in combination with having an incident response plan ready to execute at short notice, is vital to efficiently and effectively mitigate the threat SnapMC poses to your organization.”


***Check out our free***[***upcoming live and on-demand online***](https://threatpost.com/category/webinars/) ***town halls*** ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[SnapMC]] [[VPN]] [[ransomware]] [[apps]] [[ThreatPost]]
