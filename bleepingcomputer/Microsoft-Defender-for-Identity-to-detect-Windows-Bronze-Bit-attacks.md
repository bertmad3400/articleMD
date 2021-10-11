# Microsoft Defender for Identity to detect Windows Bronze Bit attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-for-identity-to-detect-windows-bronze-bit-attacks/)
+ Date: October 11, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft Defender for Identity to detect Windows Bronze Bit attacks](https://www.bleepstatic.com/content/hl-images/2020/10/16/Windows---10.jpg)


Microsoft is working on adding support for Bronze Bit attacks detection to Microsoft Defender for Identity to make it easier for Security Operations teams to detect attempts to abuse a Windows Kerberos security bypass bug tracked as CVE-2020-17049.


[Microsoft Defender for Identity](https://www.microsoft.com/en-us/microsoft-365/security/identity-defender) (previously Azure Advanced Threat Protection or Azure ATP) is a cloud-based security solution that leverages on-premises Active Directory signals.


It enables SecOps teams to detect and investigate compromised advanced threats, identities, and malicious insider activity targeting enrolled organizations.


Landing in two months
---------------------


"An alert will be triggered when there is evidence of suspicious Kerberos delegation attempts using the BronzeBit method, where a user has attempted to use a ticket to delegate access to a particular resource," Microsoft explains on the Microsoft 365 roadmap.


The flaw (patched by Microsoft during November 2020's Patch Tuesday) can be exploited in what Jake Karnes, the security consultant who discovered, has named [Kerberos Bronze Bit attacks](https://www.bleepingcomputer.com/news/security/windows-kerberos-bronze-bit-attack-gets-public-exploit-patch-now/).


Microsoft addressed the Bronze Bit vulnerability in a [two-phase staged rollout](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049), with the initial deployment phase on December 8 and an automatic enforcement phase on February 9.


One month after Microsoft issued the CVE-2020-17049 patches, Karnes published a proof-of-concept (PoC) exploit code and full details on how it could be used.


The exploit can bypass Kerberos delegation protection, allowing attackers to escalate privileges, impersonate targeted users, and move laterally within compromised environments.


He has shared a [low-level overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory) with additional info on the [Kerberos](https://www.bleepingcomputer.com/tag/kerberos/) protocol, including [practical exploit scenarios](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack) and details on implementing and using Kerberos Bronze Bit attacks against vulnerable servers.


The release of all these additional details and the PoC exploit would probably make it a lot easier to breach Windows servers unpatched against CVE-2020-17049 and was what likely prompted Redmond to add Bronze Bit detection support to Microsoft Defender for Identity.


PrintNightmare and Zerologon attack detection also available
------------------------------------------------------------


In July, Microsoft also added support for [PrintNightmare](https://www.bleepingcomputer.com/tag/printnightmare/) exploitation detection to Microsoft Defender for Identity after including [Zerologon](https://www.bleepingcomputer.com/tag/zerologon/) exploitation detection in November 2020.


Both are critical security vulnerabilities, with PrintNightmare (CVE-2021-34527) allowing [attackers to take over affected servers](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/) by elevating privileges to Domain Administrator while Zerologon (CVE-2020-1472) can be exploited to elevate privileges to spoof a domain controller account that leads to complete control of the entire domain.


Multiple threat actors, including ransomware gangs like [Vice Society](https://www.bleepingcomputer.com/news/security/vice-society-ransomware-joins-ongoing-printnightmare-attacks/), [Conti](https://twitter.com/John_Fokker/status/1425749521569624065), and [Magniber](https://www.bleepingcomputer.com/news/security/ransomware-gang-uses-printnightmare-to-breach-windows-servers/), already use PrintNightmare exploits to compromise unpatched Windows servers.


Both state-backed and financially motivated threat actors are also exploiting systems unpatched against the ZeroLogon vulnerability since [the end of October](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-ongoing-attacks-using-windows-zerologon-flaw/) and [in September](https://www.bleepingcomputer.com/news/microsoft/microsoft-hackers-using-zerologon-exploits-in-attacks-patch-now/), with more having joined since then, including:


* [Iranian-backed MuddyWater hacking group (aka SeedWorm and MERCURY),](https://www.bleepingcomputer.com/news/security/microsoft-iranian-hackers-actively-exploiting-windows-zerologon-flaw/)
* [TA505 (aka Chimborazo)](https://www.bleepingcomputer.com/news/security/ransomware-gang-now-using-critical-windows-flaw-in-attacks/) known for providing a delivery channel for Clop ransomware,
* [Chinese APT10 hackers](https://www.bleepingcomputer.com/news/security/chinese-apt10-hackers-use-zerologon-exploits-against-japanese-orgs/).


Also in July, Microsoft rolled out another Defender for Identity update that enables security operations (SecOps) teams to block attack attempts by [locking compromised users' Active Directory accounts](https://www.bleepingcomputer.com/news/security/microsoft-365-to-let-secops-lock-hacked-active-directory-accounts/).


Defender for Identity is bundled with Microsoft 365 E5 but, if you don't have a subscription already, you can also get a [Security E5 trial](https://go.microsoft.com/fwlink/p/?LinkID=2077047&clcid=0x409&culture=en-us&country=US) to give these features a spin.




#### Tags:
[[Microsoft]] [[Kerberos]] [[PrintNightmare]] [[teams]] [[Windows]] [[Zerologon]] [[Bleeping Computer]]
