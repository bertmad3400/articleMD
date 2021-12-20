# Conti Ransomware Gang Has Full Log4Shell Attack Chain
### Conti has become the first professional-grade, sophisticated ransomware group to weaponize Log4j2, now with a full attack chain.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177173
+ Date: 2021-12-20T22:11:30+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/20170634/attack-chain-e1640038007418.jpeg)

The Conti ransomware gang, which last week became the first professional crimeware outfit to adopt and weaponize the Log4Shell vulnerability, has now built up a holistic attack chain.


The sophisticated Russia-based Conti group – which Palo Alto Networks [has called](https://unit42.paloaltonetworks.com/conti-ransomware-gang/) “one of the most ruthless” of dozens of ransomware groups currently known to be active – was in the right place at the right time with the right tools when [Log4Shell hit the scene](https://threatpost.com/zero-day-in-ubiquitous-apache-log4j-tool-under-active-attack/176937/) 10 days ago, security firm Advanced Intelligence (AdvIntel) said in a [report](https://www.advintel.io/post/ransomware-advisory-log4shell-exploitation-for-initial-access-lateral-movement) shared with Threatpost on Thursday.


As of today, Monday, Dec. 20, the attack chain has taken the following form, AdvIntel’s Yelisey Boguslavskiy told Threatpost: Emotet -> Cobalt Strike -> Human Exploitation -> (no ADMIN$ share) -> Kerberoast -> brute -> vCenter ESXi with log4shell scan for vCenter.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Attack Chain
------------


Stepping through that attack chain:


1. **Emotet** is a botnet that resurfaced last month on the back of TrickBot, now with the ability to directly install …
2. [**Cobalt Strike**](https://threatpost.com/cobalt-strike-cybercrooks/167368/), the legitimate, commercially available tool used by network penetration testers on infected devices and pervasively adopted by cybercriminals. It gives threat actors direct access to targets and, according to Boguslavskiy, precedes…
3. **Human Exploitation**, followed by …
4. **Missing ADMIN$ share.** Administrative shares are hidden network shares created by Microsoft’s Windows NT operating systems that grant system administrators remote access to every disk volume on a network-connected system. As [Microsoft](https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/problems-administrative-shares-missing) puts it, “Missing administrative shares typically indicate that the computer in question has been compromised by malicious software.” Next up comes …
5. **Kerberoast.** Kerberoasting, a common, pervasive attack that exploits a combination of weak encryption and poor service account password hygiene, is a post-exploitation attack that extracts service account credential hashes from Active Directory for offline cracking. Once credentials are in hand, the next step is …
6. **Brute forcing**. [Brute-force attacks](https://threatpost.com/kubernetes-brute-force-attacks-russia-apt28/167518/) are launched with sets of credentials that threat actors plug in wily nily, systematically checking all possible passwords and passphrases until they hit a match. The Conti gang last week had zeroed in on …
7. **VMware vCenter servers.** As of Wednesday, Dec. 15, Conti was looking for vulnerable VMWare networks for initial access and lateral movement. The VMware servers are on a dismayingly [long list](https://github.com/YfryTchsGD/Log4jAttackSurface) of affected components and vendors whose products have been found to be vulnerable to Log4Shell.


Within two days of the public disclosure of the vulnerability in Apache’s Log4j logging library on Dec. 10 – a bug that came under attack within hours – Conti group members were discussing how to exploit it as an initial attack vector, according to AdvIntel.


Apache patched the bug on Dec. 11, but its patch, Log4J2, [was found to be incomplete](https://threatpost.com/apache-patch-log4shell-log4j-dos-attacks/177064/) in certain non-default configurations and paved the way for denial-of-service (DoS) attacks in certain scenarios.


As if two bugs aren’t enough, yet another, similar but distinct bug was [discovered](https://threatpost.com/third-log4j-bug-dos-apache-patch/177159/) last week in the Log4J logging library. Apache issued a patch on Friday.


Conti Winds Up Its Exploit Machine
----------------------------------


According to the Thursday AdvIntel writeup, from Vitali Kremez and Yelisey Boguslavskiy, multiple Conti group members on Dec. 12 began to chat about exploiting the Log4Shell vulnerability as an initial attack vector. That led to scanning for vulnerable systems that AdvIntel first tracked the next day, on Dec. 13.


“This is the first time this vulnerability entered the radar of a major ransomware group,” according to the writeup. The emphasis is on “major,” given that the first ransomware group to target Log4Shell was a ransomware newcomer named [Khonsari](https://businessinsights.bitdefender.com/technical-advisory-zero-day-critical-vulnerability-in-log4j2-exploited-in-the-wild). As Microsoft has [reported](https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/#Minecraft), Khonsari was locking up Minecraft players via unofficial servers. First spotted by [Bitdefender](https://www.bleepingcomputer.com/news/security/new-ransomware-now-being-deployed-in-log4shell-attacks/) in Log4Shell attacks, the ransomware’s demand note [lacked a way to contact](https://www.bleepingcomputer.com/news/security/microsoft-khonsari-ransomware-hits-self-hosted-minecraft-servers/) the operators to pay a ransom. That means that Khonsari is more of a wiper, meant to troll Minecraft users by taking down their servers, rather than ransomware.


Khonsari ransomware was just one malware that’s been thrown at vulnerable servers over the course of the Log4j saga. Within hours of public disclosure of the flaw, [attackers](https://threatpost.com/patching-time-log4j-exploits-vaccine/177017/) were scanning for vulnerable servers and [unleashing quickly evolving attacks](https://threatpost.com/apache-log4j-log4shell-mutations/176962/) to drop coin-miners, Cobalt Strike, the Orcus remote access trojan (RAT). reverse bash shells for future attacks, [Mirai and other botnets](https://threatpost.com/log4shell-attacks-origin-botnet/176977/), and backdoors.


A Perfect Storm
---------------


Log4Shell has become a focal point for threat actors, including suspected nation state actors who’ve been observed investigating Log4j2, AdvIntel researchers noted. The compressed timeline of the public disclosure followed fast by threat actor interest and exploits exemplifies the accelerated trajectory of threats witnessed since the [ProxLogon](https://threatpost.com/microsoft-exchange-servers-proxylogon-patching/165001/) family of bugs in Exchange Server in March and the subsequent attacks, they said: “if one day a major CVE is spotted by APTs, the next week it is weaponized by ransomware,” according to their writeup.


But out of all the threat actors, Conti “plays a special role in today’s threat landscape, primarily due to its scale,” they explained. It’s a highly sophisticated organization, comprising several teams. AdvIntel estimates that, based on scrutiny of Conti’s logs, the Russian-speaking gang made over $150 million over the past six months.


But still they continue to expand, with Conti continually looking for new attack surfaces and methods.


AdvIntel listed a number of Conti’s innovations since August, including:


* [Secret backdoors](https://www.advintel.io/post/secret-backdoor-behind-conti-ransomware-operation-introducing-atera-agent): Conti’s Atera Agent allows the gang to gain persistence on infected protected environments: especially those equipped with more aggressive machine learning endpoint detention and response anti-virus productions. “The IT management solution enables monitoring, management and automation of hundreds of SMB IT networks from a single console,” AdvIntel described in an August report.
* New [backup removal](https://www.advintel.io/post/backup-removal-solutions-from-conti-ransomware-with-love) solutions that expanded Conti’s ability to [blow up backups](https://threatpost.com/conti-ransomware-backups/175114/).
* An entire operation to revive [Emotet](https://www.advintel.io/post/corporate-loader-emotet-history-of-x-project-return-for-ransomware), which [resurfaced](https://threatpost.com/emotet-resurfaces-trickbot/176362/) in November.


The writeup shared a timeline of Conti’s search for new attack vectors, shown below.


Keeping Your Head Above the Logjam’s Water
------------------------------------------


AdvIntel shared these suggested recommendations and mitigations for Log4Shell:


* The Dutch National Cyber Security Center shared a list of the affected software and recommendations linked to each one of them [on GitHub](https://github.com/NCSC-NL/log4shell/tree/main/software).
* Here are [VMWare’s workaround instructions](https://kb.vmware.com/s/article/87081) to address CVE-2021-44228 in vCenter Server and vCenter Cloud Gateway (87081).


When Will It All End?
---------------------


Lou Steinberg, former chief technology officer at TD Ameritrade, said it ain’t over til it’s over, “And it’s not over.”


“We don’t know if we patched systems after they were compromised from Log4J, so it may be a while before we know how bad things are,” he said in an article shared with Threatpost on Monday. “This will happen again. Modern software and systems are built from components which aren’t always trustworthy. Worse, bad actors know this and look to subvert the components to create a way into otherwise trusted software.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Emotet]] [[action.malware.name=Expand]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]] [[action.malware.name=TrickBot]] [[action.malware.name=Wiper]] [[action.malware.name=Zen]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Conti]] [[Advintel]] [[Ransomware]] [[Log4shell]] [[Vcenter]] [[Threatpost]] [[Khonsari]] [[Boguslavskiy]] [[Emotet]] [[Microsoft]] [[ThreatPost]]
#### CVE's
[[CVE-2021-44228]]

