# New APT ChamelGang Targets Russian Energy, Aviation Orgs
### First appearing in March, the group has been leveraging ProxyShell against targets in 10 countries and employs a variety of malware to steal data from compromised networks.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175272)
+ Date: October 1, 2021  8:36 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/01083402/chameleon-e1633091654806.jpeg)
A new APT group has emerged that’s specifically targeting the fuel and energy complex and aviation industry in Russia, exploiting known vulnerabilities like Microsoft Exchange Server’s [ProxyShell](https://threatpost.com/microsoft-barrage-proxyshell-attacks/168943/) and leveraging both new and existing malware to compromise networks.


Researchers at security firm [Positive Technologies](https://www.ptsecurity.com/ww-en/) have been tracking the group, dubbed ChamelGang for its chameleon-like capabilities, since March. Though attackers mainly have been seen targeting Russian organizations, they have attacked targets in 10 countries so far, researchers said in a [report](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/new-apt-group-chamelgang/) by company researchers Aleksandr Grigorian, Daniil Koloskov, Denis Kuvshinov and Stanislav Rakovsky published online Thursday.


To avoid detection, ChamelGang hides its malware and network infrastructure under legitimate services of established companies like Microsoft, TrendMicro, McAfee, IBM and Google in a couple of unique ways, researchers observed.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


One is to acquire domains that imitate their legitimate counterparts – such as newtrendmicro.com, centralgoogle.com, microsoft-support.net, cdn-chrome.com and mcafee-upgrade.com. The other is to place SSL certificates that also imitate legitimate ones – such as github.com, www.ibm.com, jquery.com, update.microsoft-support.net – on its servers, researchers said.


Moreover, ChamelGang – like [Nobelium](https://threatpost.com/solarwinds-active-directory-servers-foggyweb-backdoor/175056/) and [REvil](https://threatpost.com/kaseya-patches-zero-days-revil-attacks/167670/) before it – has hopped on the bandwagon of attacking the supply chain first to gain access to its ultimate target, they said. In one of the cases analyzed by Positive Technologies, “the group compromised a subsidiary and penetrated the target company’s network through it,” according to the writeup.


The attackers also appear malware-agnostic when it comes to tactics, using both known malicious programs such as [FRP](https://howtofix.guide/frp-exe-virus/), [Cobalt Strike Beacon](https://threatpost.com/cobalt-strike-cybercrooks/167368/), and Tiny Shell, as well as previously unknown malware ProxyT, BeaconLoader and the DoorMe backdoor, researchers said.


**Two Separate Attacks**
------------------------


Researchers analyzed two attacks by the novel APT: one in March and one in August. The first investigation was triggered after a Russia-based energy company’s antivirus protection repeatedly reported the presence of the Cobalt Strike Beacon in RAM.


Attackers gained access to the energy company’s network through the supply chain, compromising a vulnerable version of a subsidiary company’s web application on the JBoss Application Server. Upon investigation, researchers found that attackers exploited a critical vulnerability, [CVE-2017-12149](https://access.redhat.com/security/cve/CVE-2017-12149), to remotely execute commands on the host.


Once on the energy company’s network, ChamelGang moved laterally, deploying a number of tools along the way. They included Tiny Shell, with which a UNIX backdoor can receive a shell from an infected host, execute a command and transfer files; an old DLL hijacking technique associated with the Microsoft Distributed Transaction Control (MSDTC) Windows service to gain persistence and escalate privileges; and the Cobalt Strike Beacon for calling back to attackers for additional commands.


Researchers were successful in accessing and exfiltrating data in the attack, researchers said. “After collecting the data, they placed it on web servers on the compromised network for further downloading … using the Wget utility,” they wrote.


**Cutting Short a ProxyShell Attack**
-------------------------------------


The second attack was on an organization from the Russian aviation production sector, researchers said. They notified the company four days after the server was compromised, working with employees to eliminate the threat shortly after.


“In total, the attackers remained in the victim’s network for eight days,” researchers wrote. “According to our data, the APT group did not expect that its backdoors would be detected so quickly, so it did not have time to develop the attack further.”


In this instance, ChamelGang used a known chain of vulnerabilities in Microsoft Exchange called ProxyShell – CVE-2021-34473, CVE-2021-34523, CVE-2021-31207 – to compromise network nodes and gain a foothold. Indeed, a number of attackers took advantage of ProxyShell throughout August, [pummeling](https://threatpost.com/proxyshell-attacks-unpatched-exchange-servers/168879/) unpatched Exchange servers with attacks after a [researcher at BlackHat revealed](https://threatpost.com/exchange-servers-attack-proxyshell/168661/) the attack surface.


Once on the network, attackers then installed a modified version of the backdoor DoorMe v2 on two Microsoft Exchange mail servers on the victim’s network. Attackers also used BeaconLoader to move inside the network and infect nodes, as well as the Cobalt Strike Beacon.


**Victims Across the Globe**
----------------------------


Further threat intelligence following the investigation into attacks on the Russian companies revealed that ChamelGang’s activity has not been limited to that country.


Positive Technologies eventually identified 13 more compromised organizations in nine other countries – the U.S., Japan, Turkey, Taiwan, Vietnam, India, Afghanistan, Lithuania and Nepal. In the last four countries mentioned, attackers targeted government servers, they added.


Attackers often used ProxyLogon and ProxyShell vulnerabilities in Microsoft Exchange Server against victims, who were all notified by the appropriate national security authorities in their respective countries.


ChamelGang’s tendency to reach its targets through the supply chain also is likely one that it – as well as other APTs – will continue, given the success attackers have had so far with this tactic, researchers added. “New APT groups using this method to achieve their goals will appear on stage,” they said.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[said.]] [[Microsoft]] [[ProxyShell]] [[ChamelGang]] [[company’s]] [[malware]] [[ThreatPost]]
