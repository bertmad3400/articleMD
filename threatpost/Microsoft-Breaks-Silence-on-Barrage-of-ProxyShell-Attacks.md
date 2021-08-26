# Microsoft Breaks Silence on Barrage of ProxyShell Attacks
### versions of the software are affected by a spate of bugs under active exploitations.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168943)
+ Date: August 26, 2021  8:39 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/26083932/exchange-server-microsoft.jpg)
Microsoft has broken its silence on the [recent barrage of attacks](https://threatpost.com/proxyshell-attacks-unpatched-exchange-servers/168879/) on several ProxyShell vulnerabilities in that were [highlighted](https://threatpost.com/exchange-servers-attack-proxyshell/168661/) by a researcher at Black Hat earlier this month.


The company [released an advisory](https://techcommunity.microsoft.com/t5/exchange-team-blog/proxyshell-vulnerabilities-and-your-exchange-server/ba-p/2684705) late Wednesday letting customers know that threat actors may use unpatched Exchange servers “to deploy ransomware or conduct other post-exploitation activities” and urging them to update immediately.


“Our recommendation, as always, is to install the latest CU and SU on all your Exchange servers to ensure that you are protected against the latest threats,” the company said. “Please update now!”  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)Customers that have installed the [May 2021 security updates](https://techcommunity.microsoft.com/t5/exchange-team-blog/released-may-2021-exchange-server-security-updates/ba-p/2335209) or the [July 2021 security updates](https://techcommunity.microsoft.com/t5/exchange-team-blog/released-july-2021-exchange-server-security-updates/ba-p/2523421) on their Exchange servers are protected from these vulnerabilities, as are Exchange Online customers so long as they ensure that all hybrid Exchange servers are updated, the company wrote.


“But if you have not installed either of these security updates, then your servers and data are vulnerable,” according to the advisory.


The ProxyShell bugs that Devcore principal security researcher [Orange Tsai](https://twitter.com/orange_8361) outlined in a presentation at Black Hat. The three vulnerabilities (CVE-2021-34473, CVE-2021-34523, CVE-2021-31207) enable an adversary to trigger remote code execution on Microsoft Exchange servers. Microsoft said the bugs can be exploited in the following cases:


–The server is running an older, unsupported CU;


–The server is running security updates for older, unsupported versions of Exchange that were [released](https://techcommunity.microsoft.com/t5/exchange-team-blog/march-2021-exchange-server-security-updates-for-older-cumulative/ba-p/2192020) in March 2021; or


–The server is running an older, unsupported CU, with the [March 2021 EOMT](https://msrc-blog.microsoft.com/2021/03/15/one-click-microsoft-exchange-on-premises-mitigation-tool-march-2021/) mitigations applied.


“In all of the above scenarios, you *must* install one of latest supported CUs and all applicable SUs to be protected,” according to Microsoft. “Any Exchange servers that are not on a supported CU *and* the latest available SU are vulnerable to ProxyShell and other attacks that leverage older vulnerabilities.”


**Sounding the Alarm**


Following Tsai’s presentation on the bugs, the SANS Internet Storm Center’s Jan Kopriva [reported](https://isc.sans.edu/forums/diary/ProxyShell+how+many+Exchange+servers+are+affected+and+where+are+they/27732/) that [he found more](https://threatpost.com/exchange-servers-attack-proxyshell/168661/) than 30,000 vulnerable Exchange servers via a Shodan scan and that any threat actor worthy of that title would find exploiting then easy to execute, given how much information is available.


Security researchers at Huntress also reported seeing [ProxyShell vulnerabilities](https://www.huntress.com/blog/rapid-response-microsoft-exchange-servers-still-vulnerable-to-proxyshell-exploit) being actively exploited throughout the month of August to install backdoor access once the [ProxyShell exploit code](https://peterjson.medium.com/reproducing-the-proxyshell-pwn2own-exploit-49743a4ea9a1) was published on Aug. 6. But starting last Friday, Huntress reported a “surge” in attacks after finding 140 webshells launched against 1,900 unpatched Exchange servers.


The Cybersecurity & Infrastructure Security Agency (CISA) joined those sounding the alarm over the weekend, issuing [an urgent alert](https://us-cert.cisa.gov/ncas/current-activity/2021/08/21/urgent-protect-against-active-exploitation-proxyshell). They, too, urged organizations to immediately install the latest Microsoft Security Update.


At the time, researcher Kevin Beaumont expressed [criticism over Microsoft’s messaging efforts](https://doublepulsar.com/multiple-threat-actors-including-a-ransomware-gang-exploiting-exchange-proxyshell-vulnerabilities-c457b1655e9c) surrounding the vulnerability and the urgent need for its customers to update their Exchange Server security.


“Microsoft decided to downplay the importance of the patches and treat them as a standard monthly Exchange patch, which [has] been going on for – obviously – decades,” Beaumont explained.


But Beaumont said these remote code execution (RCE) vulnerabilities are “…as serious as they come.” He noted that the company did not help matters by failing to allocate CVEs for them until July — four months after the patches were issued.


In order of patching priority, according to Beaumont, the vulnerabilities are: [CVE-2021–34473](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34473), [CVE-2021–34523](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34523) and [CVE-2021–31207](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-31207).


CVE-2021-34473, a vulnerability in which a pre-auth path confusion leads to ACL Bypass, was patched in April. CVE-2021-34523, also patched in April, is an elevation of privilege on Exchange PowerShell backend. CVE-2021-31207, a bug in which a post-auth Arbitrary-File-Write leads to remote code execution, was patched in May.




#### Tags:
[[ProxyShell]] [[Microsoft]] [[–The]] [[older,]] [[ThreatPost]]
