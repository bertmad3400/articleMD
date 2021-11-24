# Attackers Actively Target Windows Installer Zero-Day
### Researcher discovered a “more powerful” variant of an elevation-of-privilege flaw for which Microsoft released a botched patch earlier this month.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176558)
+ Date: November 24, 2021  9:09 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/24090827/Windows-11.jpg)
Attackers are actively exploiting a Windows Installer zero-day vulnerability that was discovered when a patch Microsoft issued for another security hole inadequately fixed the original and unrelated problem.


Over the weekend, security researcher [Abdelhamid Naceri](https://github.com/klinix5) discovered a Windows Installer elevation-of-privilege vulnerability tracked as [CVE-2021-41379](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41379) that Microsoft [patched](https://threatpost.com/microsoft-nov-patch-tuesday-fixes-six-zero-days-55-bugs/176143/) a couple of weeks ago as part of its November [Patch Tuesday updates](https://msrc.microsoft.com/update-guide/).


However, after examining the fix, Naceri found a bypass as well as an even more concerning zero-day privilege-elevation bug. The researcher posted a [proof of concept (POC) exploit](https://github.com/klinix5/InstallerFileTakeOver) Tuesday on GitHub for the newly discovered bug that he said works on all currently-supported versions of Windows.


If exploited, the POC, called InstallerFileTakeOver, gives an actor administration privileges in Windows 10, Windows 11 and Windows Server when logged onto a Windows machine with Edge installed.


**Peer Research Confirms Exploit and Active Attacks**
-----------------------------------------------------


Researchers at Cisco Talos Security Intelligence and Research Group as well as others confirmed the POC can be reproduced as well as corroborating evidence that threat actors were already exploiting the bug.


“This vulnerability affects every version of Microsoft Windows, including fully patched Windows 11 and Server 2022,” according to a [post on the Cisco Talos blog](https://blog.talosintelligence.com/2021/11/attackers-exploiting-zero-day.html) by


Jaeson Schultz, technical leader for Cisco Talos. “Talos has already detected malware samples in the wild that are attempting to take advantage of this vulnerability.”


Other researchers also confirmed on Twitter that the POC functions as advertised to deliver local privilege escalation.


“Can confirm this works, local priv esc,” [tweeted](https://twitter.com/GossiTheDog/status/1462721449425264645?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1462721449425264645%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.theregister.com%2F2021%2F11%2F23%2Fwindows_lpe%2F) security researcher [Kevin Beaumont](https://twitter.com/GossiTheDog), who said he tested it on Windows 10 20H2 and Windows 11. “The prior patch MS issued didn’t fix the issue properly.”


**Discovery and More Details**
------------------------------


As detailed by Microsoft, CVE-2021-41379 is a Windows Installer elevation of privilege vulnerability with a rating of low on the Common Vulnerability Scoring System.


“An attacker would only be able to delete targeted files on a system,” according to [Microsoft’s notes](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41379) on the flaw. “They would not gain privileges to view or modify file contents.”


However, Microsoft’s patch for the bug did not fix the vulnerability correctly, allowing Naceri to bypass it during his analysis of the patch, he said in his GitHub post of the POC.


However, that bypass was small potatoes compared to a variant of CVE-2021-41379 that he discovered during his research that is “more powerful than the original one,” which is why Naceri chose to publish a POC of that flaw instead, he wrote.


The code Naceri released leverages the discretionary access control list (DACL) for Microsoft Edge Elevation Service to replace any executable file on the system with an MSI file, allowing an attacker to run code as an administrator, Cisco Talos’ Schultz explained in his post.


**Wait for the Patch**
----------------------


The associated POC works in every supporting windows installation, including Windows 11 and Server 2022 with the November 2021 patch, as well as in server installations, Naceri wrote.


“While group policy by default doesn’t allow standard users to do any MSI operation,  the administrative install feature thing seems to be completely bypassing group policy,” he wrote.


Due to the “complexity” of the vulnerability, Naceri said that the best workaround available for the flaw at this time “is to wait Microsoft to release a security patch.


“Any attempt to patch the binary directly will break Windows installer,” he wrote, adding that those affected should “wait and see how Microsoft will screw the patch again” before taking any mitigation action.


A Microsoft spokesperson told BleepingComputer that the company is aware of Naceri’s disclosure and “will do what is necessary” to keep customers “safe and protected,” according to [a published report](https://www.bleepingcomputer.com/news/security/malware-now-trying-to-exploit-new-windows-installer-zero-day/).


“An attacker using the methods described must already have access and the ability to run code on a target victim’s machine,” the spokesperson said, according to the report.


***Cybersecurity for multi-cloud environments is notoriously challenging. OSquery and CloudQuery is a solid answer. Join Uptycs and Threatpost for “***[***An Intro to OSquery and CloudQuery***](https://bit.ly/3wf2vTP)***,” an on-demand Town Hall with Eric Kaiser, Uptycs’ senior security engineer, and find out how this open-source tool can help tame security across your organization’s entire campus.***


[***Register NOW***](https://bit.ly/3wf2vTP) ***to access the on-demand event!***




#### Tags:
[[Windows]] [[Microsoft]] [[Naceri]] [[POC]] [[CVE-2021-41379]] [[However,]] [[“An]] [[wrote.]] [[ThreatPost]]
