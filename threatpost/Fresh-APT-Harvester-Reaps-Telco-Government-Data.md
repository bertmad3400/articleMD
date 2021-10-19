# Fresh APT Harvester Reaps Telco, Government Data
### The group is likely nation-state-backed and is mounting an ongoing spy campaign using custom malware and stealthy tactics.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175585)
+ Date: October 19, 2021  4:15 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/19160326/harvest2-e1634673821762.jpg)
A previously unseen advanced persistent threat (APT) group dubbed Harvester by researchers is attacking telcos, IT companies and government-sector targets in a campaign that’s been ongoing since June.


According to a Symantec [analysis](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/harvester-new-apt-attacks-asia), the group sports a veritable cornucopia of advanced and custom tools, and it’s on a quest to carry out espionage activities in Afghanistan and elsewhere in that region.


As of October, the campaign was still ongoing, looking to dig up a bounty of sensitive data.


**A Sharp Set of Tools**
------------------------


Harvester has invested in a range of tools for scything through organizations’ defenses, Symantec found, including the “Graphon” custom backdoor.


Graphon is deployed alongside a tool for gathering screenshots and downloaders for other malware and tools – offering a host of remote-access and data-exfiltration capabilities.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“We do not know the initial infection vector that Harvester used to compromise victim networks, but the first evidence we found of Harvester activity on victim machines was a malicious URL,” according to Symantec’s writeup. “The group then started to deploy various tools, including its custom Graphon backdoor, to gain remote access to the network.”


The APT also attempts to avoid notice by using legitimate CloudFront and Microsoft infrastructure for its command-and-control (C2) activity, in a bid to go unnoticed amidst legitimate network traffic.


The primary tools used by Harvester are as follows:


**Graphon:** A custom backdoor that uses Microsoft infrastructure for its C2 activity. According to Symantec, it’s compiled as a .NET PE DLL. When executed, it allows Harvester operators to run commands to control their input stream and capture the output and error streams. “They also periodically send GET requests to the C2 server, with the content of any returned messages extracted and then deleted,” according to the analysis. “Data that cmd.exe pulled from the output and error streams is encrypted and sent back to the attackers’ servers.”


**Custom Downloader:** This also uses Microsoft infrastructure for its C2 activity, and it leverages an interesting additional evasion tactic, according to the research: a registry value to create a new loadpoint for the malware, which is a location within the file system and registry that’s used to load applications and related files. Then, it opens an embedded web browser within its own interface. “While it initially appeared that this URL may have been a loadpoint for Backdoor.Graphon, upon further investigation it appears to be a decoy to confuse any affected users,” researchers noted.


**Custom Screenshotter:** This tool periodically logs screenshots to a file. It saves them to a password-protected .ZIP archive for exfiltration, with all archives older than a week deleted.


**Cobalt Strike Beacon:** This is a commercial, off-the-shelf penetration-testing tool that allows red teams to emulate an attack. Cybercriminals have [increasingly used it](https://threatpost.com/cobalt-strike-cybercrooks/167368/) for nefarious purposes, including spreading laterally within an enterprise environment, uploading files, injecting or elevating processes, and more. In the Harvester implementation, it uses CloudFront infrastructure for its C2 activity.


**Metasploit**: This is another off-the-shelf tool often used by cyberattackers. It’s a modular framework that’s usually used for privilege escalation, but it can also do other malicious things, like screen captures and implementing a persistent backdoor.


**Do Fear the Reaper**
----------------------


The Symantec team doesn’t yet have enough information to make a specific attribution for who’s behind Harvester, but given its general M.O., it’s likely backed by a specific government, researchers said.


“The capabilities of the tools, their custom development and the victims targeted, all suggest that Harvester is a nation-state-backed actor,” according to the [Monday posting](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/harvester-new-apt-attacks-asia) from the firm. “The activity carried out by Harvester makes it clear the purpose of this campaign is espionage, which is the typical motivation behind nation-state-backed activity.”


While the group is mainly targeting organizations in Afghanistan in the current campaign, it has also struck other targets in the South Asia region. Entities “should be alert to the malicious activity,” Symantec warned.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Symantec]] [[C2]] [[that’s]] [[tools,]] [[it’s]] [[“The]] [[Microsoft]] [[ThreatPost]]
