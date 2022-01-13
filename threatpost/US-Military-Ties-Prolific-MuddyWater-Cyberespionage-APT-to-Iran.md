# US Military Ties Prolific MuddyWater Cyberespionage APT to Iran
### US Cyber Command linked the group to Iranian intelligence and detailed its multi-pronged, increasingly sophisticated suite of malware tools.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177633
+ Date: 2022-01-13T17:35:34+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2019/02/01142104/iran-apt.jpg)

U.S. Cyber Command has confirmed that [MuddyWater](https://threatpost.com/wirte-middle-eastern-governments/176688/) – an advanced persistent threat (APT) cyberespionage actor aka Mercury, Static Kitten, TEMP.Zagros or Seedworm that’s historically [targeted government victims](https://threatpost.com/muddywater-apt-custom-tools/144193/) in the Middle East – is an Iranian intelligence outfit.


The link has been suspected, and now it’s government-stamped. On Wednesday, USCYBERCOM not only confirmed the tie; it also disclosed the plethora of open-source [tools and strategies](https://www.cisa.gov/uscert/ncas/current-activity/2022/01/12/cnmf-identifies-and-discloses-malware-used-iranian-apt-muddywater) MuddyWater uses to break into target systems and released malware samples.


“MuddyWater has been seen using a variety of techniques to maintain access to victim networks,” according to USCYBERCOM’S National Mission Force (CNMF). “These include side-loading DLLs in order to trick legitimate programs into running malware and obfuscating PowerShell scripts to hide command and control functions.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


USCYBERCOM has uploaded multiple MuddyWater-attributed malware samples to [VirusTotal](https://www.virustotal.com/gui/user/CYBERCOM_Malware_Alert).




USCYBERCOM’s [press release](https://www.cybercom.mil/Media/News/Article/2897570/iranian-intel-cyber-suite-of-malware-uses-open-source-tools/) described MuddyWater as being “a subordinate element within the Iranian Ministry of Intelligence and Security (MOIS).” The [Congressional Research Service](https://crsreports.congress.gov/product/pdf/RL/RL32048) describes MOIS as conducting “domestic surveillance to identify regime opponents” and said that the agency is responsible for surveillance of anti-regime activists abroad through a network of agents placed in Iran’s embassies.


New Variants of PowGoop Malware
-------------------------------


Among multiple malware sets, MuddyWater is using new variants of the PowGoop malware family, CNMF said.


PowGoop was first [described](https://unit42.paloaltonetworks.com/thanos-ransomware/) by Palo Alto Networks in September 2020, when it was used in attacks on two state-run organizations in the Middle East and North Africa that ultimately installed and ran a variant of the [Thanos](https://threatpost.com/thanos-ransomware-weaponize-riplace-tactic/156438/) ransomware.


At the time, Palo Alto suspected that the threat actors were using a downloader – one that researchers dubbed PowGoop – to reach out to a remote server to download and execute PowerShell scripts. The name comes from the use of GoogleUpdate.exe to load a malicious, modified version of goopdate.dll – a DLL that’s used to load a malicious PowerShell script from an external file.


PowGoop has been buffed up since it was first spotted: SentinelLabs on Wednesday [explained](https://www.sentinelone.com/labs/wading-through-muddy-waters-recent-activity-of-an-iranian-state-sponsored-threat-actor/) that significantly enhanced, newer variants of PowGoop have shown up in the wild, discovered in recently triaged incidents, “suggesting the group continues to use and maintain it even after recent exposures.”


“The new variants reveal that the threat group has expanded its arsenal of legitimate software used to load malicious DLLs,” SentinelOne intelligence researcher Amitai Ben Shushan Ehrlich wrote.


Ehrlich explained that, aside from GoogleUpdate.exe, three more benign pieces of software are abused in order to sideload malicious DLLs: Git.exe, FileSyncConfig.exe and Inno\_Updater.exe.


CNMF has shared new samples showing the different parts of MuddyWater’s new suite of tools, along with JavaScript files used to establish connections back to malicious infrastructure. They include new PowGoop command-and-control (C2) beacon variants as well as the Mori Backdoor: a backdoor used for cyber espionage that employes DNS tunneling to communicate with the C2 infrastructure.


“Any instances of these files may indicate an attacker in the network,” CNMF reiterated about newly released and already known indicators of compromise (IoC). “Should a network operator identify multiple of the tools on the same network, it may indicate the presence of Iranian malicious cyber actors.”


Love of Tunneling, Exchange Exploits & Ruler Abuse
--------------------------------------------------


SentinelLabs drilled down into multiple additional recent findings about MuddyWater’s techniques, tactics and procedures (TTPs), including:


**MuddyWater Tunneling Activity:** “The operators behind MuddyWater activities are very fond of tunneling tools,” SentinelOne’s Ehrlich wrote. “The custom tools used by the group often provide limited functionality, and are used to drop tunneling tools which enable the operators to conduct a wider set of activities.”


MuddyWater attackers are using tunneling tools including Chisel, SSF and Ligolo: tools that enable the threat actor to connect to machines within target environments as if they were inside the operator LAN, he explained.


**Exploiting Microsoft Exchange:** Sentinel Labs has also tracked MuddyWater targeting Exchange servers of high-profile organizations. “This subset of Exchange exploitation activity is rather interesting, as without context it would be difficult to attribute it to MuddyWater because the activity relies almost completely on publicly available offensive security tools,” Ehrlich noted.


They’re using two tools to try to exploit Exchange servers: a publicly available script for exploiting [CVE-2020-0688](https://threatpost.com/microsoft-exchange-exploited-flaw/159669/) – a vulnerability that enables remote code execution (RCE) for an authenticated user – and Ruler, an open source Exchange exploitation framework recently used to target a string of Middle Eastern telecom operators and IT companies, as [reported](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/espionage-campaign-telecoms-asia-middle-east) by Symantec’s Threat Hunter Team last month.


MuddyWater: Better & Better at Stirring Up Muck
-----------------------------------------------


Analysis shows that the MuddyWater APT continues to evolve and adapt its techniques Sentinel Labs summarized. “While still relying on publicly available offensive security tools, the group has been refining its custom toolset and utilizing new techniques to avoid detection,” Ehrlich observed, pointing to evolution of the PowGoop malware family, the group’s use of tunneling tools, and its targeting of Exchange servers in high-profile organizations.


The group doesn’t have to be fancy to be effective, he noted: “Like many other Iranian threat actors, the group displays less sophistication and technological complexity compared to other state-sponsored APT groups. Even so, it appears MuddyWater’s persistency is a key to their success, and their lack of sophistication does not appear to prevent them from achieving their goals.”


**Password** **Reset:** **[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):** Fortify 2022 with a password security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken. **[Register & Stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)** – sponsored by Specops Software.





## Tags:

#### Threatactor:
[[threatactor.name=MuddyWater]] [[threatactor.name=MuddyWater]] [[threatactor.name=MuddyWater]] [[threatactor.name=MuddyWater]] [[threatactor.name=MuddyWater]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Ruler]] [[action.malware.name=Tor]] [[action.malware.name=XTunnel]]

#### Location:
[[victim.continent.name=Africa]] [[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Muddywater]] [[Powgoop]] [[Malware]] [[Ehrlich]] [[Uscybercom]] [[Powershell]] [[Cnmf]] [[“the]] [[ThreatPost]]
#### CVE's
[[CVE-2020-0688]]

