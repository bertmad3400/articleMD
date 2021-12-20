# Third Log4J Bug Can Trigger DoS; Apache Issues Patch
### The new Log4j vulnerability is similar to Log4Shell in that it also affects the logging library, but this DoS flaw has to do with Context Map lookups, not JNDI.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177159
+ Date: 2021-12-20T16:01:57+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/20105658/bug-trio.jpg)

No, you’re not seeing triple: On Friday, Apache released yet another patch – [version 2.17](https://logging.apache.org/log4j/2.x/download.html) – for yet another flaw in the ubiquitous log4j logging library, this time for a DoS bug.


Trouble comes in threes, and this is the third one for log4j. The latest bug isn’t a variant of the Log4Shell remote-code execution (RCE) bug that’s plagued IT teams since Dec. 10, coming [under active attack](https://threatpost.com/zero-day-in-ubiquitous-apache-log4j-tool-under-active-attack/176937/) [worldwide](https://threatpost.com/log4shell-attacks-origin-botnet/176977/) within hours of its public disclosure, spawning [even nastier mutations](https://threatpost.com/apache-log4j-log4shell-mutations/176962/) and leading to the [potential for denial-of-service](https://threatpost.com/apache-patch-log4shell-log4j-dos-attacks/177064/) (DoS) in Apache’s initial patch.


It does have similarities, though: The new bug affects the same component as the Log4Shell bug. Both the Log4Shell, tracked as [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) (criticality rating of CVSS 10.0) and the new bug, tracked as [CVE-2021-45105](https://nvd.nist.gov/vuln/detail/CVE-2021-45105) (CVSS score: 7.5) abuse attacker-controlled lookups in logged data.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The difference: The lookups in the new bug, CVE-2021-45105, are Context Map lookups instead of the Java Naming and Directory Interface (JNDI) lookups to an LDAP server that allow attackers to execute any code that’s returned in the Log4Shell vulnerability.


ContextMapLookup allows applications to store data in the Log4j ThreadContext Map and then retrieve the values in the Log4j configuration: For example, an app would store the current user’s login id in the ThreadContext Map with the key “loginId”.


The weakness has to do with improper input validation and uncontrolled recursion that can lead to DoS.


As [explained](https://www.zerodayinitiative.com/blog/2021/12/17/cve-2021-45105-denial-of-service-via-uncontrolled-recursion-in-log4j-strsubstitutor) by Guy Lederfein of the Trend Micro Research Team, “the Apache Log4j API supports variable substitution in lookups. However, a crafted variable can cause the application to crash due to uncontrolled recursive substitutions. An attacker with control over lookup commands (e.g., via the Thread Context Map) can craft a malicious lookup variable, which results in a Denial-of-Service (DoS) attack.”


The new vulnerability affects all versions of the tool from 2.0-beta9 to 2.16, which Apache shipped last week to remediate the [second flaw](https://threatpost.com/new-log4shell-attack-vector-local-hosts/177128/) in the trio. That second bug was the RCE flaw [CVE-2021-45046](https://nvd.nist.gov/vuln/detail/CVE-2021-45046), which, in turn, stemmed from Apache’s [incomplete fix](https://threatpost.com/apache-patch-log4shell-log4j-dos-attacks/177064/) for [CVE-2021-44228](https://thehackernews.com/2021/12/extremely-critical-log4j-vulnerability.html), aka the Log4Shell vulnerability.


Lederfein continued: “When a nested variable is substituted by the StrSubstitutor class, it recursively calls the substitute() class. However, when the nested variable references the variable being replaced, the recursion is called with the same string. This leads to an infinite recursion and a DoS condition on the server. As an example, if the Pattern Layout contains a Context Lookup of ${ctx.apiversion}, and its assigned value is ${${ctx.apiversion}}, the variable will be recursively substituted with itself.”


The vulnerability has been tested and confirmed on Log4j versions up to and including 2.16, he said.


Apache has listed mitigating factors, but ZDI recommends upgrading to the latest version to ensure that the bug is completely addressed.


The latest bug and Apache’s new round of fixes are just the latest news in the ongoing, ever-shifting log4j situation. As exploits flood in, new vulnerabilities emerge and patches turn out to need patching, huge tech players [such as SAP](https://threatpost.com/sap-log4shell-vulnerability-apps/177069/) have been hurrying to hunt down the logging library and to release product patches.


CISA Mandates Immediate Patching
--------------------------------


On Thursday, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) issued an [emergency directive](https://www.cisa.gov/uscert/ncas/current-activity/2021/12/17/cisa-issues-ed-22-02-directing-federal-agencies-mitigate-apache) mandating federal civilian departments and agencies to immediately patch their internet-facing systems for the Log4j vulnerabilities by Thursday, Dec. 23.


The risk presented by the library’s vulnerabilities is sky-high, as multiple threat actors have jumped on the opportunities to exploit vulnerable systems. As Check Point Research (CPR) [highlighted](https://blog.checkpoint.com/2021/12/11/protecting-against-cve-2021-44228-apache-log4j2-versions-2-14-1/) last week, real-life attacks have included a crypto-mining group that launched attacks in five countries.


Last week, Microsoft reported that nation-state groups Phosphorus (Iran) and [Hafnium](https://threatpost.com/microsoft-exchange-zero-day-attackers-spy/164438/) (China), as well as unnamed APTs from North Korea and Turkey, are actively exploiting Log4Shell in targeted attacks. Hafnium is known for targeting Exchange servers with the ProxyLogon zero-days back in March, while Phosphorus – aka [Charming Kitten](https://threatpost.com/charming-kitten-whatsapp-linkedin-effort/158813/), APT35, Ajax Security Team, NewsBeef and Newscaster – [made headlines](https://threatpost.com/microsoft-iranian-apt-t20-summit-munich-security-conference/160654/) for targeting global summits and conferences in 2020.


CPR said that Charming Kitten had gone after seven Israeli targets as of Wednesday.


Conti Ransomware Gang Is Among the Attackers
--------------------------------------------


The Conti ransomware gang is in on it too: AdvIntel researchers said last week that they’re seen Conti operators going after VMware vCenter.


“The current exploitation led to multiple use cases through which the Conti group tested the possibilities of utilizing the Log4j 2 exploit,” the researchers [said](https://www.advintel.io/post/ransomware-advisory-log4shell-exploitation-for-initial-access-lateral-movement) last week. “The criminals pursued targeting specific vulnerable [Log4j 2 VMware vCenter](https://www.vmware.com/security/advisories/VMSA-2021-0028.html) [servers] for lateral movement directly from the compromised network resulting in vCenter access affecting U.S. and European victim networks from the pre-existent Cobalt Strike sessions.”


Last week, a ransomware attack that some suspect may be attributable to the [Conti gang](https://threatpost.com/conti-ransomware-backups/175114/) forced a family-run chain of restaurants, hotels and breweries, [McMenamins](https://www.mcmenamins.com/), to [shut down some operations.](https://threatpost.com/conti-gang-ransomware-attack-mcmenamins/177119/)


The bugs are also being leveraged by botnets, remote access trojans (RATs), initial access brokers, and a new ransomware strain called Khonsari. As of Monday, CPR said that it’s seen more than 4.3 million attempted exploits, more than 46 percent of which were made by “known malicious groups.”


Yet More Sleepless Nights
-------------------------


Trend Micro’s Lederfein noted that the log4j component has had quite a run in the vulnerability spotlight, having received “quite a bit of attention” since the Log4Shell vulnerability was revealed 10 days ago. Expect more of the same, he predicted, as “it would not be a surprise to see further bugs disclosed – with or without a patch.”


Tom Garrubba, CISO with Shared Assessments, concurred: “This vulnerability has been keeping a lot of security professionals up at night,” he told Threatpost. This Javageddon has even percolated up to the C-suite, he said, with the vulnerability “keeping a lot of security professionals up at night.”


“Executives and board members are also gaining interest as to how this will affect them as well,” he said via email. “Log4j is used all throughout the Internet and [affects] multiple applications and systems with deep roots.”


“The best path you can take right now it’s a stay alert of all patches that are coming out to address this vulnerability and put them into place immediately,” Garrubba advised. “Sadly, it appears this is going to affect organization’s continuously into the future as they identify more items that are affected by this vulnerability.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=Ajax Security Team]] [[threatactor.name=APT3]] [[threatactor.name=HAFNIUM]] [[threatactor.name=Magic Hound]] [[threatactor.name=Magic Hound]] [[threatactor.name=Magic Hound]] [[threatactor.name=Magic Hound]] [[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=RTM]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Accomodation]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.country.name=Israel]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Turkey]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Log4shell]] [[Log4j]] [[Conti]] [[Log4j]] [[Lederfein]] [[Ransomware]] [[Vcenter]] [[“the]] [[ThreatPost]]
#### CVE's
[[CVE-2021-44228]] [[CVE-2021-45105]] [[CVE-2021-45046]]

