# Parallels Offers ‘Inconvenient’ Fix for High-Severity Bug
### Firm offers guidance on how to mitigate a five-months-old privilege escalation bug impacting Parallels Desktop 16 for Mac and all previous versions.  

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168997)
+ Date: August 27, 2021  4:54 pm
+ Author: Tom Spring


## Article:
The makers of Parallels Desktop has released a workaround fix for a high-severity privilege escalation bug that impacts its Parallels Desktop 16 for Mac software and all older versions. Mitigation advice comes five months after researchers first identified the bug in April.


Parallels Desktop, now owned by private equity giant KKR, is used by seven million users, according to the company, and allows Mac users to run Windows, Linux and other operating systems on their macOS.


The vulnerability allows malicious software running in a Parallels virtual machine (VM) to access macOS files shared in a default configuration of the software. The software maker stated that the recommended fixes need to be manually performed by end users and will likely “inconvenience” some while also reducing product functionality.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In a [Wednesday security bulletin](https://exchange.xforce.ibmcloud.com/vulnerabilities/208188), first to widely disclose details of the bug, it was revealed that the vulnerability (CVE-2021-34864) is caused by improper access control in the Parallels’ WinAppHelper component. The flaw, according to Parallels, is specifically tied to the software’s [Parallels Tools](https://www.parallels.com/blogs/parallels-tools/), a proxy for communications between the host macOS and the virtual machine’s operating system.


An Easy-to-Exploit Bug
----------------------


“The issue results from the lack of proper access control. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor,” according to a separate security [advisory, also posted Wednesday](https://www.zerodayinitiative.com/advisories/ZDI-21-1000/).


The severity of the vulnerability is rated as high (8.8) using the Common Vulnerability Scoring System, version 3.0. The bulletin also warns that the level of complexity needed to exploit the vulnerability is “low.”


“By default, Parallels Desktop shares files and folders between the Mac and a VM, so users can easily open macOS files from applications running in a virtual machine and save documents to Mac,” Parallels explained. “This functionality exposes the user home folder to the VM. This folder may contain configuration files, cache from different applications, etc., that malicious software can access.”


Parallels is advising users to mitigate the vulnerability via reconfiguring their software or upgrading to the latest version, which is Parallels Desktop 17 for Mac, released on August 10.


“Parallels Desktop 17 for Mac and newer versions are not affected. The entire home folder is no longer shared with a VM by default, only selected folders, like Desktop, Documents, Downloads, etc.,” according to the [vulnerability’s summary description](https://vulmon.com/vulnerabilitydetails?qid=CVE-2021-34864).


The company added, “This vulnerability allows local malicious users to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability.”


**Disclosure Timeline**
-----------------------


The flaw was initially detected by security researchers Sunjoo Park and Jack Dates on April 8, during Trend Micro’s Pawn2Own Austin event. For their efforts, the researchers earned $40,000 each, according to the event’s organizer.


On August 10, Parallels posted to its Knowledge Base information regarding the flaw, under the title “Mitigate ZDI-CAN-13543 in Parallels Desktop 16 and older”. The post described the April discovery and mitigation steps users needed to take to protect themselves. On Wednesday, a number of security alerts posted the vulnerability’s identifying number (CVE-2021-34864), assigning it a high-severity rating.


The prospect of malicious software or a threat actor breaking or escaping a virtual instance of Windows to infect a system is a worst-case scenario. Parallels did not return requests for comment for this report.


**Parallels: An Inconvenient Fix**
----------------------------------


To mitigate against the vulnerability, Parallels Desktop 16 for Mac users (and other legacy users) have a number of options. The first option is to upgrade to Parallels Desktop 17 for Mac, which does not contain the flaw. It’s unclear if affected customers will have to pay the $50 one-time upgrade fee for the Standard Edition to mitigate the flaw via an upgrade.


For customers running Parallels Desktop 16 users or earlier versions of the software, the company said the fixes available to them will “reduce functionality” of the software and cause “inconveniences,” such as file duplications when sharing documents across VM and the host macOS.


“If you don’t plan to run untrusted code in the VM, it is recommended to follow common security practices,” the company recommended. “If you run untrusted code in the VM and you want to isolate the VM from Mac, then one of the following options can be used.”


Those options, according Parallels, include:


While the above mitigates security issue, it also eliminates one of [Parallels selling points](https://www.parallels.com/products/desktop/): “Seamlessly move and share content between Mac and Windows.”


It’s also unclear whether macOS users who configure their systems to isolate the VM guest from the host operating system mitigate the flaw.


**Researchers Turn to Parallels**
---------------------------------


While Parallels Desktop for Mac is not marketed as a cybersecurity research tool, a [number of websites recommend this type of use scenario](https://www.sentinelone.com/blog/how-to-reverse-macos-malware-part-one/).


Parallels is just one of many virtual machine options for macOS users to run alternate operating systems. Others include Apple’s own Boot Camp feature, VirtualBox and VMWare for macOS.


Increased interest in Parallels has recently been sparked because in Apple’s new ARM-based Macs, which contain its security-forward M1 chip, Boot Camp has been removed. Installing Windows 10 on M1 Macs requires an ARM copy of Microsoft’s operating system.


Craig Federighi, Apple’s senior vice president of software engineering, said Apple is not planning to support Boot Camp on ARM-based Macs in the future, during a [Daring Fireball podcast](https://youtu.be/Hg9F1Qjv3iU).


Seeing an opportunity, on April 14 [Parallels released an update](https://www.parallels.com/blogs/parallels-desktop-apple-silicon-mac/) for Parallels Desktop 16 for Mac that supports Mac computers with Apple M1 chip.


***Check out our free***[***upcoming live webinar events***](https://threatpost.com/category/webinars/)***– unique, dynamic discussions with cybersecurity experts and the Threatpost community:***




#### Tags:
[[macOS]] [[VM]] [[macOS.]] [[Mac,]] [[Apple’s]] [[M1]] [[ThreatPost]]
