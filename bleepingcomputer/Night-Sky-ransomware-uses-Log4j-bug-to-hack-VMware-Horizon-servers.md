# Night Sky ransomware uses Log4j bug to hack VMware Horizon servers
### The Night Sky ransomware gang has started to exploit the critical CVE-2021-4422 vulnerability in the Log4j logging library, also known as Log4Shell, to gain access to VMware Horizon systems.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/night-sky-ransomware-uses-log4j-bug-to-hack-vmware-horizon-servers/
+ Date: 2022-01-11T06:24:43-05:00
+ Author: Ionut Ilascu


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j_headpic.jpg)

![Night Sky ransomware uses Log4j bug to hack VMware Horizon servers](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j_headpic.jpg)


The Night Sky ransomware gang has started to exploit the critical CVE-2021-44228 vulnerability in the Log4j logging library, also known as Log4Shell, to gain access to VMware Horizon systems.


The threat actor is targeting vulnerable machines exposed on the public web from domains that impersonate legitimate companies, some of them in the technology and cybersecurity sectors.


### Attacks started in early January


Spotted in late December 2021 by security researcher MalwareHunterTeam, [Night Sky ransomware focuses on locking enterprise networks](https://www.bleepingcomputer.com/news/security/night-sky-is-the-latest-ransomware-targeting-corporate-networks/). It has encrypted multiple victims, asking for an $800,000 ransom from one of them.


On Monday, Microsoft [posted a warning](https://twitter.com/MsftSecIntel/status/1480730559739359233) about a new campaign from a China-based actor it tracks as DEV-0401 to exploit the Log4Shell vulnerability on VMware Horizon systems exposed on the internet, and deploy Night Sky ransomware.


VMware Horizon is used for desktop and app virtualization in the cloud, allowing users to access them remotely through a dedicated client or a web browser.


It is also a solution for administrators for better management, security compliance, and automation across the entire fleet of virtual systems.


VMware has patched Log4Shell in Horizon products and provided [workarounds](https://kb.vmware.com/s/article/87073) for customers that could not install the new version containing the fix ([2111, 7.13.1, 7.10.3](https://customerconnect.vmware.com/en/downloads/info/slug/desktop_end_user_computing/vmware_horizon/2111)). However, some companies have yet to apply the fix.



“As early as January 4, attackers started exploiting the CVE-2021-44228 vulnerability in internet-facing systems running VMware Horizon. Our investigation shows that successful intrusions in these campaigns led to the deployment of the NightSky ransomware” [Microsoft](https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/#NightSky)



The company adds that the group is known for deploying other ransomware families in the past, such as LockFile, AtomSilo, and Rook.


Previous attacks from this actor also exploited security issues in internet-facing systems like Confluence ([CVE-2021-26084](https://www.bleepingcomputer.com/news/security/us-govt-warns-orgs-to-patch-massively-exploited-confluence-bug/)) and on-premises Exchange servers (CVE-2021-34473 - [ProxyShell](https://www.bleepingcomputer.com/tag/proxyshell/)). It is believed that Night Sky is a continuation of the aforementioned ransomware operations.


Microsoft notes that Night Sky ransomware operators rely on command and control servers that impersonate domains used by legitimate companies such as cybersecurity firms Sophos, Trend Micro, technology companies Nvidia and Rogers Corporation.


### Attractive attack vector


Log4Shell is an attractive attack vector for nation-state hackers and cybercriminals alike because the open-source Log4J component is present in a wide range of systems from [dozens of vendors](https://www.bleepingcomputer.com/news/security/log4j-list-of-vulnerable-products-and-vendor-advisories/).


Exploiting the bug to achieve code execution without authentication requires minimum effort. A threat actor can initiate a callback or request to a malicious server that passes needs only visit a site or search it for a specific string to cause a server callback to a malicious location.


The security flaw can be leveraged remotely on vulnerable machines exposed on the public internet or from the local network, by a local adversary to move laterally to sensitive internal systems.



![Exploiting Log4j vulnerability CVE-2021-44228](https://www.bleepstatic.com/images/news/u/1100723/2022/Vulnerabilities/Log4Shell/Log4ShellExploit.jpg)source: [Microsoft](https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/)
One of the first “top-tier” ransomware gangs to [integrate Log4Shell](https://www.bleepingcomputer.com/news/security/conti-ransomware-uses-log4j-bug-to-hack-vmware-vcenter-servers/) in their attacks is Conti, who showed an interest in it as a potential attack avenue on December 12, just three days after the first proof-of-concept (PoC) exploit became public.


Another ransomware gang, a newcomer called [Khonsari](https://www.bleepingcomputer.com/news/security/new-ransomware-now-being-deployed-in-log4shell-attacks/), started to leverage the exploit the very next day the PoC emerged on GitHub.


In the days following its disclosure, multiple threat [actors started to leverage the Log4j bug](https://www.bleepingcomputer.com/news/security/log4j-vulnerability-now-used-by-state-backed-hackers-access-brokers/). The first to take advantage were cryptocurrency miners, with state-backed hackers and ransomware gangs following suit.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Log4shell]] [[Vmware]] [[Microsoft]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-44228]] [[CVE-2021-26084]] [[CVE-2021-34473]]

