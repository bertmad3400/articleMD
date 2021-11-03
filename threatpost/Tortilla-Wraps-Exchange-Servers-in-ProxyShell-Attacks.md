# ‘Tortilla’ Wraps Exchange Servers in ProxyShell Attacks
### The Microsoft Exchange ProxyShell vulnerabilities are being exploited yet again for ransomware, this time with Babuk from the new “Tortilla” threat actor.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175967)
+ Date: November 3, 2021  2:16 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/03135753/burrito-e1635962286404.jpg)
A new-ish threat actor sometimes known as “Tortilla” is launching a fresh round of ProxyShell attacks on Microsoft Exchange servers, this time with the aim of inflicting vulnerable servers with variants of the Babuk ransomware.


Cisco Talos researchers said in a Wednesday [report](https://blog.talosintelligence.com/2021/11/babuk-exploits-exchange.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+feedburner%2FTalos+%28Talos%E2%84%A2+Blog%29) that they spotted the malicious campaign a few weeks ago, on Oct. 12.


Tortilla, an actor that’s been operating since July, is predominantly targeting U.S. victims. It’s also hurling a smaller number of infections that have hit machines in the Brazil, Finland, Germany,  Honduras, Thailand, Ukraine and the U.K., as shown on the map below.


Prior to this ransomware-inflicting campaign, Tortilla has been experimenting with other payloads, such as the PowerShell-based netcat clone PowerCat.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

Netcat is a networking utility for reading from and writing to network connections using TCP or UDP, designed to be a dependable back-end that can be used directly or easily driven by other programs and scripts.


PowerCat has a penchant for Windows, the researchers explained, being “known to provide attackers with unauthorized access to Windows machines.”


ProxyShell’s New Attack Surface
-------------------------------


ProxyShell is a name given to an attack that chains a trio of vulnerabilities together (CVE-2021-34473, CVE-2021-34523, CVE-2021-31207), to enable unauthenticated attackers to perform remote code execution (RCE) and to snag plaintext passwords.


The attack was outlined in a presentation ([PDF](https://i.blackhat.com/USA21/Wednesday-Handouts/us-21-ProxyLogon-Is-Just-The-Tip-Of-The-Iceberg-A-New-Attack-Surface-On-Microsoft-Exchange-Server.pdf)) given by Devcore principal security researcher [Orange Tsai](https://twitter.com/orange_8361) at Black Hat in April. In it, Tsai disclosed an entirely new attack surface in Exchange, and a [barrage](https://threatpost.com/exchange-servers-attack-proxyshell/168661/) of [attacks](https://threatpost.com/proxyshell-attacks-unpatched-exchange-servers/168879/) soon followed. August was glutted with reports of threat actors exploiting ProxyShell to launch [webshell attacks](https://threatpost.com/proxyshell-attacks-unpatched-exchange-servers/168879/), as well as to deliver [LockFile ransomware](https://pbs.twimg.com/media/E9TmPo6XMAYCnO-?format=jpg&name=4096x4096)..


In this latest ProxyShell campaign, Cisco Talos researchers said that the threat actor is using “a somewhat unusual infection chain technique where an intermediate unpacking module is hosted on a pastebin.com clone pastebin.pl” to deliver Babuk.


They continued: “The intermediate unpacking stage is downloaded and decoded in memory before the final payload embedded within the original sample is decrypted and executed.”


Who’s Babuk?
------------


Babuk is a ransomware that’s probably best known for its starring role in a breach of the Washington D.C. police force [in April](https://threatpost.com/babuk-ransomware-washington-dc-police/165616/). The gang behind the malware has a short history, having only been [identified in 2021](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/babuk-ransomware/), but that history shows that it’s a [double-extortion](https://threatpost.com/double-extortion-ransomware-attacks-spike/154818/) player: one that threatens to post stolen data in addition to encrypting files, as a way of applying thumbscrews so victims will pay up.


That tactic has worked. As [McAfee](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/babuk-ransomware/) described in February, Babuk the ransomware had already been lobbed at a batch of at least five big enterprises, with one score: The gang walked away with $85,000 after one of those targets ponied up the money, McAfee researchers said.


Its victims have included Serco, an outsourcing firm that confirmed that it had been [slammed](https://www.computerweekly.com/news/252495684/Serco-confirms-Babuk-ransomware-attack) with a double-extortion ransomware attack in late January.


Like many ransomware strains, Babuk is ruthless: It not only encrypts a victim’s machine, it also [blows up backups](https://threatpost.com/conti-ransomware-backups/175114/) and deletes the volume shadow copies, Cisco Talos said.


What’s Under Babuk’s Hood
-------------------------


On the technical side, Cisco Talos described Babuk as a flexible ransomware that can be compiled, through a ransomware builder, for several hardware and software platforms.


It’s mostly compiled for Windows and ARM for Linux, but researchers said that, over time, they’ve also seen versions for ESX and a 32-bit, old PE executable.


In this recent October campaign though, the threat actors are specifically targeting Windows.


China Chopper Chops Again
-------------------------


Part of the infection chain involves China Chopper: A webshell that dates back to 2010 but which has [clung to relevancy since](https://threatpost.com/china-chopper-tool-multiple-campaigns/147813/), including reportedly being used in a massive 2019 attack against telecommunications providers called [Operation Soft Cell](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers). The webshell enables attackers to “retain access to an infected system using a client-side application which contains all the logic required to control the target,” as Cisco Talos [described](https://blog.talosintelligence.com/2019/08/china-chopper-still-active-9-years-later.html) the webshell in 2019.


This time around, it’s being used to get to Exchange Server systems. “We assess with moderate confidence that the initial infection vector is exploitation of ProxyShell vulnerabilities in Microsoft Exchange Server through the deployment of China Chopper web shell,” according to the Cisco Talos writeup.


The Infection Chain
-------------------


As shown in the infection flow chart below, the actors are using either a DLL or .NET executable to kick things off on the targeted system. “The initial .NET executable module runs as a child process of w3wp.exe and invokes the command shell to run an obfuscated PowerShell command,” according to Cisco Talos’ report.


“The PowerShell command invokes a web request and downloads the payload loader module using certutil.exe from a URL hosted on the domains fbi[.]fund and xxxs[.]info, or the IP address 185[.]219[.]52[.]229,” researchers said.


“The payload loader downloads an intermediate unpacking stage from the PasteBin clone site pastebin.pl,” they continued – a site that “seems to be unrelated to the popular pastebin.com.”


They continued: “The unpacker concatenates the bitmap images embedded in the resource section of the trojan and decrypts the payload into the memory. The payload is injected into the process AddInProcess32 and is used to encrypt files on the victim’s server and all mounted drives.”


More Ingredients in Tortilla’s Infrastructure
---------------------------------------------


Besides the pastebin.pl site that hosts Tortilla’s intermediate unpacker code, Tortilla’s infrastructure also includes a Unix-based download server.


The site is legitimate, but Cisco Talos has seen multiple malicious campaigns running on it, including hosting variants of the [AgentTesla trojan](https://threatpost.com/agent-tesla-microsoft-asmi/163581/) and the [FormBook malware dropper.](https://threatpost.com/new-formbook-dropper-harbors-persistence/145614/)


Babuk’s Code Spill Helps Newbies
--------------------------------


In July, Babuk gang’s source code and builder were spilled: They were [uploaded to VirusTotal](https://threatpost.com/babuk-ransomware-builder-virustotal/167481/), making it available to all security vendors and competitors. That leak has helped the ransomware spread to even an inexperienced, green group like Tortilla, Cisco Talos said.


The leak “may have encouraged new malicious actors to manipulate and deploy the malware,” researchers noted.


“This actor has only been operating since early July this year and has been experimenting with different payloads, apparently in order to obtain and maintain remote access to the infected systems,” according to its writeup.


With Babuk source code readily available, all the Tortilla actors have to know is how to tweak it a tad, researchers said: A scenario that observers predicted back when the code appeared.


“The actor displays low to medium skills with a decent understanding of the security concepts and the ability to create minor modifications to existing malware and offensive security tools,” Cisco Talos researchers said in assessing the Tortilla gang.


Decryptor Won’t Work on Variant
-------------------------------


While a free [Babuk decryptor was released](https://www.bleepingcomputer.com/news/security/babuk-ransomware-decryptor-released-to-recover-files-for-free/) last week, it won’t work on the Babuk variant seen in this campaign, according to the writeup: “Unfortunately, it is only effective on files encrypted with a number of leaked keys and cannot be used to decrypt files encrypted by the variant described in this blog post.”


How to Keep Exchange Safe
-------------------------


Tortilla is hosting malicious modules and conducting internet-wide scanning to exploit vulnerable hosts.


The researchers recommended staying vigilant, staying on top of any infection in its early stages and implementing a layered defense security, “with the behavioral protection enabled for endpoints and servers to detect the threats at an early stage of the infection chain.”


They also recommended keeping servers and apps updated so as to squash vulnerabilities, such as the trio of CVEs exploited in the ProxyShell attacks.


Also, keep an eye out for backup demolition, as the code deletes shadow copies: “Babuk ransomware is nefarious by its nature and while it encrypts the victim’s machine, it interrupts the system backup process and deletes the volume shadow copies,” according to Cisco Talos.


On top of all that, bolster detection: Watch out for system configuration changes, suspicious events generated by detection systems for an abrupt service termination, or abnormally high I/O rates for drives attached to servers, according to Cisco Talos.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Babuk]] [[Talos]] [[ransomware]] [[ProxyShell]] [[“The]] [[webshell]] [[said.]] [[campaign,]] [[malware]] [[victim’s]] [[ThreatPost]]
