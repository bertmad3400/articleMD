# Ransomware warning: Hackers are using Log4j flaw as part of their attacks, warns Microsoft | ZDNet
### A new China-based double extortion ransomware has started exploiting the Log4Shell bug in VMware server products.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/ransomware-warning-hackers-are-using-log4j-flaw-as-part-of-their-attacks-warns-microsoft/
+ Date: 2022-01-11 11:04:09
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/9051218ee8d0bbca720cca05db1d8b24534894c2/2022/01/11/d6054b2b-da4c-4a72-b7d9-18147cd212e2/shutterstock-1173443506.jpg?width=770&height=578&fit=crop&auto=webp)

Microsoft has confirmed that suspected China-based cyber criminals are targeting the Log4j 'Log4Shell' flaw in VMware's Horizon product to install NightSky, a new ransomware strain that emerged on December 27. 

The financially motivated ransomware attacks target CVE-2021-44228, the original Log4Shell flaw [disclosed on December 9](https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/), and mark one new threat posed by the critical vulnerability that affects internet-facing software, systems and devices where vulnerable versions of the Java-based Log4j application error-logging component are present.


"As early as January 4, attackers started exploiting the CVE-2021-44228 vulnerability in internet-facing systems running VMware Horizon. Our investigation shows that successful intrusions in these campaigns led to the deployment of the NightSky ransomware," [Microsoft notes in an update to its recommendations for mitigating Log4Shell](https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/). 

**SEE:** [**Log4j zero-day flaw: What you need to know and how to protect yourself**](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/#link=%7B%22linkText%22:%22Log4j%20zero-day%20flaw:%20What%20you%20need%20to%20know%20and%20how%20to%20protect%20yourself%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

Microsoft's findings add more details to a [report last week from the digital arm of the UK's National Health Service](https://www.zdnet.com/article/log4j-flaw-attackers-are-targeting-log4shell-vulnerabilities-in-vmware-horizon-servers-says-nhs/) (NHS) that attackers are targeting VMware's Horizon server software that use vulnerable versions of Log4j. That report noted attackers installed a malicious Java file that injects a web shell into the VM Blast Secure Gateway service, but it didn't indicate whether ransomware was deployed.   

Horizon is [one of a number of VMware's software products affected by Log4j flaws](https://www.zdnet.com/article/vmware-patches-critical-non-log4j-flaw-as-ibm-cisco-release-log4j-fixes/). The case demonstrates the difficulties admins face in identifying systems affected by Log4j. VMware has detailed which versions of Horizon components are or are not vulnerable, and the different remediation steps for each if they are vulnerable. 

Its [advisory indicates that at least one version of each Horizon on-premise component is vulnerable](https://kb.vmware.com/s/article/87073?lang=en_US). Vulnerable on-premise components include Connection Server and HTML Access, the Horizon Windows Agent, Linux Agent, Linux Agent Direct Connect, Cloud Connector, and vRealize Operations for Desktop Agent. VMware has released updated versions or provided scripted mitigation workarounds.   






Microsoft says the attacks are being performed by a China-based ransomware operator it's tracking as DEV-0401, which has previously deployed LockFile, AtomSilo, and Rook. The group has also exploited internet-facing systems running Confluence (CVE-2021-26084) and on-premises Exchange servers (CVE-2021-34473), according to Microsoft.  

[According to BleepingComputer](https://www.bleepingcomputer.com/news/security/night-sky-is-the-latest-ransomware-targeting-corporate-networks/), malware researchers at [MalwareHunterTeam identified NightSky](https://twitter.com/malwrhunterteam/status/1477381209147723788) as a new ransomware group on December 27.   

However, Czech-based malware analyst Jiří Vinopal, who published an [analysis of NightSky on GitHub](https://github.com/Dump-GUY/Malware-analysis-and-Reverse-engineering/blob/main/NightSky_Ransomware%E2%80%93just_a_Rook_RW_fork_in_VMProtect_suit/NightSky_Ransomware%E2%80%93just_a_Rook_RW_fork_in_VMProtect_suit.md) today, argues [NightSky is just a new version of Rook ransomware](https://twitter.com/vinopaljiri/status/1480059715392622597) with a few key design and encryption changes, including that NightSky is delivered as a VMProtect file. 

BleepingComputer notes that NightSky is using "double extortion", where the attacker not only encrypts a target's data but steals it and threatens to leak it if a ransom is not paid. One victim received an $800,000 ransom demand for a NightSky decryptor.

**SEE:** [**Log4j flaw could be a problem for industrial networks 'for years to come'**](https://www.zdnet.com/article/log4j-flaw-could-be-a-problem-for-industrial-networks-for-years-to-come/#link=%7B%22linkText%22:%22Log4j%20flaw%20could%20be%20a%20problem%20for%20industrial%20networks%20'for%20years%20to%20come'%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-flaw-could-be-a-problem-for-industrial-networks-for-years-to-come/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

[As ZDNet reported](https://www.zdnet.com/article/cisa-director-we-have-not-seen-significant-intrusions-from-log4j/) yesterday, the US Cybersecurity and Infrastructure Security Agency (CISA) on Monday said it had not seen Log4Shell exploitation result in significant intrusions beyond the attack on the Belgian Defense Ministry. 

However, it also warned the lack of significant intrusions was no reason to reduce the urgency of remediation. Attackers who have already exploited targets can lay low for months afterwards, waiting for defenders to drop their guard before moving on their new access. 

And big penalties might await firms that don't apply available patches if vulnerable systems expose consumer data. The FTC [last week warned](https://www.zdnet.com/article/ftc-to-pursue-companies-that-expose-customer-data-due-to-not-patching-log4j/) it would come after private sector firms that failed to protect consumer data exposed as a result of Log4j. 

CISA's assessment that the Log4j threat is far from over chimes with Microsoft's assessment, which stresses that Log4j is a "high-risk situation" in part because many organizations can't easily tell what products and services are affected by Log4j. 

Microsoft said the Log4j vulnerabilities represent a complex and high-risk situation for companies across the globe: "The vulnerabilities affect not only applications that use vulnerable libraries, but also any services that use these applications, so customers may not readily know how widespread the issue is in their environment." 

Microsoft also said customers should use scripts and scanning tools to assess their risk and impact, but warns that it has seen attackers using many of the same inventory techniques to locate targets: "Sophisticated adversaries (like nation-state actors) and commodity attackers alike have been observed taking advantage of these vulnerabilities. There is high potential for the expanded use of the vulnerabilities."





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=CHOPSTICK]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Nightsky]] [[Microsoft]] [[Ransomware]] [[Vmware]] [[Log4shell]] [[Internet-facing]] [[ZDNet]]
#### CVE's
[[CVE-2021-44228]] [[CVE-2021-26084]] [[CVE-2021-34473]]

