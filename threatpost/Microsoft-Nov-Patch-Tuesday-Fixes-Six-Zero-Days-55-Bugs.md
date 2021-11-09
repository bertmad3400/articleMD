# Microsoft Nov. Patch Tuesday Fixes Six Zero-Days, 55 Bugs
### Experts urged users to prioritize patches for Microsoft Exchange and Excel, those favorite platforms so frequently targeted by cybercriminals and nation-state actors.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176143)
+ Date: November 9, 2021  4:41 pm
+ Author: Lisa Vaas


## Article:
[Microsoft reported](https://msrc.microsoft.com/update-guide/vulnerability) a total of 55 vulnerabilities, six of which are rated critical, with the remaining 49 being rated important. The flaws are found in Microsoft Windows and Windows Components, Azure, Azure RTOS, Azure Sphere, Microsoft Dynamics, Microsoft Edge (Chromium-based), Exchange Server, Microsoft Office and Office Components, Windows Hyper-V, Windows Defender, and Visual Studio.


All in all, it’s a pretty light month, according to the Zero Day Initiative’s (ZDI’s) Dustin Childs. “Historically speaking, 55 patches in November is a relatively low number,” he commentd. “Even going back to 2018 when there were only 691 CVEs fixed all year, there were more November CVEs.”


Still, as always, this Patch Tuesday delivers high-priority fixes, the most urgent of which being the duo that are under attack.


High-Priority, Actively Exploited Pair of Bugs
----------------------------------------------


[**CVE-2021-42321**](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42321)**: Microsoft Exchange Server Remote Code Execution Vulnerability.**


This is a critical remote code execution (RCE) weakness in Exchange Server caused by issues with the validation of command-let (cmdlet) arguments – i.e., lightweight commands used in the PowerShell environment. They’re invoked by PowerShell runtime within the context of automation scripts that are provided at the command line or invoked programmatically by the PowerShell runtime through APIs. Microsoft said that the vulnerability, rated 8.8 in criticality, has low attack complexity.


In order to exploit this flaw, an attacker would need to be authenticated, which limits some of the impact, as noted by Satnam Narang, staff research engineer at Tenable. Microsoft says they are aware of “limited targeted attacks” using this vulnerability in the wild.


Microsoft has a [blog post describing the vulnerabilit](https://techcommunity.microsoft.com/t5/exchange-team-blog/released-november-2021-exchange-server-security-updates/ba-p/2933169)y and how it’s exploited.


Microsoft Exchange Server has been the subject of several notable vulnerabilities throughout 2021, including [ProxyLogon](https://threatpost.com/microsoft-exchange-servers-proxylogon-patching/165001/) and associated vulnerabilities as well as [ProxyShell](https://threatpost.com/tortilla-exchange-servers-proxyshell/175967/), Narang pointed out.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)“Though unconfirmed, this may be similar to an Exchange Server vulnerability that was discovered at the [Tianfu Cup](https://borncity.com/win/2021/10/17/tifanu-cup-2021-exchange-2019-und-iphone-gehackt/) hacking competition last month,” Narang suggested.


Narang said that federal or government bodies in the United States may be bound by the recent [CISA directive 22-01](https://cyber.dhs.gov/bod/22-01/) that puts an emphasis on faster patching of exploits that are actively being used by attackers. “This vulnerability – along with CVE-2021-42292 – would likely fall into that category,” he noted in an email on Tuesday.


In spite of playing a starring role at the Tianfu Cup, this flaw was actually discovered by the Microsoft Threat Intelligence Center (MSTIC). Microsoft said that it’s been actively used in attacks.


[**CVE-2021-42292**](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42292)**: Microsoft Excel Security Feature Bypass Vulnerability.**


This patch fixes a security feature bypass vulnerability ​​in Microsoft Excel for both Windows and MacOS computers that could allow code execution when opening a specially crafted file. It too was discovered by MSTIC, which said that it’s also been exploited in the wild as a zero day.


According to Trend Micro’s Zero Day Initiative (ZDI) [November Security Update](https://www.zerodayinitiative.com/blog/2021/11/9/the-november-2021-security-update-review), “This is likely due to loading code that should be behind a prompt, but for whatever reason, that prompt does not appear, thus bypassing that security feature.”


Microsoft doesn’t suggest what effect the vulnerability might have, but its CVSS score of 7.8 gives it a severity rating of high. Kevin Breen, director of cyber threat research at Immersive Labs, told Threatpost on Tuesday that the lack of detail “can make it hard to prioritize, but anything that is being exploited in the wild should be at the very top of your list to patch.”


Microsoft said that the Outlook Preview Pane isn’t an attack vector for this weakness, so a target would need to open the file in order for exploitation to occur.


Updates are available for Windows systems, but updates for Office for Mac aren’t out yet.


Narang suggested that given the lack of description and a lack of updates for a vulnerability being exploited in the wild, “it may be worth telling anyone in your organization using Office for Mac to be more cautious until patches are made available.”


Other Bugs of Note
------------------


[**CVE-2021-42298**](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42298)**: Microsoft Defender Remote Code Execution Vulnerability.**


Defender is designed to scan every file and run with some of the highest levels or privileges in the operating system. This means an attacker could trigger the exploit by simply sending a file – the victim wouldn’t even need to open or run anything, explained Kevin Breen, director of cyber threat research at Immersive Labs.


Breen told Threatpost on Tuesday that this is the reason that CVE-2021-42298 is marked as “exploitation more likely.”


“As it’s not being exploited in the wild, it should get updated without any manual intervention from administrators,” he said via email. “That being said, it’s definitely worth checking to make sure your Defender installations are getting their updates set correctly.”


Microsoft’s advisory includes steps to verify that users have the latest versions installed.


[**CVE-2021-38666**](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38666)**: Remote Desktop Client Remote Code Execution Vulnerability.**


Microsoft said that in the case of a Remote Desktop connection, an attacker with control of a Remote Desktop Server could trigger an RCE on the RDP client machine when a victim connects to the attacking server with the vulnerable Remote Desktop Client.


That’s not the clearest description, Breen noted, but the attack vector suggests that the remote desktop client installed on all supported versions of Windows contains a vulnerability.


“To exploit it, an attacker would have to create their own server and convince a user to connect to the attacker,” Breen explained. “There are several ways an attacker could do this, one of which could be to send the target an RDP shortcut file, either via email or a download. If the target opens this file, which in itself is not malicious, they could be giving the attacker access to their system.”


Breen said in an email that in addition to patching this flaw, a sensible step would be to add detections for RDP files being shared in emails or downloads.


[**CVE-2021-38631**](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38631) **&** [**CVE-2021-41371**](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41371)**: Information Disclosure Vulnerabilities in Microsoft Remote Desktop Protocol (RDP).**


These flaws were previously publicly disclosed by security researchers. Successful exploitation of would allow an attacker to see RDP passwords for the vulnerable system.


The issue affects RDP running on Windows 7 – 11 and Windows Server 2008 – 2019. They’re rated “Important” by Microsoft. Given the interest that cybercriminals (especially ransomware initial access brokers) have in RDP, “it is likely that it will be exploited at some point,” Liska said.


Continuous Exchange Vulnerabilities
-----------------------------------


Exchange vulnerabilities have been of particular concern this year, noted Allan Liska, senior security architect at Recorded Future. Liska pointed to both Chinese nation state actors and the cybercriminals behind the [DearCry](https://threatpost.com/microsoft-exchange-exploits-ransomware/164719/) ransomware (also believed to be operating out of China) as having exploited earlier vulnerabilities in Microsoft Exchange ([CVE-2021-26855 and CVE-2021-27065](https://threatpost.com/microsoft-exchange-cyberattacks-one-click-fix/164817/)).


“While Microsoft only rates the vulnerability as ‘Important’ because an attacker has to be authenticated to exploit it, Recorded Future has noted that gaining legitimate credential access to Windows systems has become trivial for both nation state and cybercriminal actors,” Liska said via email. Hence, he recommended prioritizing this flaw for patching.


Prioritize CVE-2021-42292, Too
------------------------------


Microsoft wasn’t clear about which security feature is bypassed by this security feature bypass vulnerability for Microsoft Excel for both Windows and MacOS computers, which affects versions 2013 – 2021. But the fact that it’s being exploited in the wild “is concerning,” Liska said and “means it should be prioritized for patching.”


Microsoft Excel is a frequent target of both [nation-state attackers](https://threatpost.com/spear-phishing-attack-lures-victims-with-hiv-results/153536/) and cybercriminals, he noted.


***Want to win back control of the flimsy passwords standing between your network and the next cyberattack? Join Darren James, head of internal IT at Specops, and Roger Grimes, data-driven defense evangelist at KnowBe4, to find out how during a free, LIVE Threatpost event,*** [***“Password Reset: Claiming Control of Credentials to Stop Attacks,”***](https://bit.ly/3bBMX30) ***on Wed., Nov. 17 at 2 p.m. ET. Brought to you by Specops.***


[***Register NOW***](https://bit.ly/3bBMX30) ***for the LIVE event and submit questions ahead of time to Threatpost’s Becky Bracken at*** [***becky.bracken@threatpost.com.***](mailto:becky.bracken@threatpost.com)




#### Tags:
[[Microsoft]] [[Windows]] [[it’s]] [[RDP]] [[Vulnerability.]] [[Narang]] [[Breen]] [[Liska]] [[PowerShell]] [[Threatpost]] [[ThreatPost]]
