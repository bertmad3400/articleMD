# Windows 10: Microsoft just revealed another Print Spooler bug
### Microsoft discloses a new PrintNightmare bug and advises admins to disable the Print Spooler service to mitigate the issue.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/windows-10-microsoft-just-revealed-another-print-spooler-bug/)
+ Date: August 12, 2021 -- 14:35 GMT (15:35 BST)
+ Author: Liam Tung


## Article:
Unknown

Microsoft's Windows 10 Print Spooler security is turning into a headache for the company and its 10  customers.

[Branded bugs](http://v) like Heatbleed from 2014 are a bit passé but the Windows 10 PrintNightmare bugs appear to be an apt choice: Microsoft released fixes [in July](https://www.zdnet.com/article/microsoft-adds-second-cve-for-printnightmare-remote-code-execution/) and August and, just after its August 10 Patch Tuesday change to the Print Spooler service, it's disclosed yet another print spooler bug. 


This one concerns a [Windows Print Spooler remote code execution vulnerability](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36958), tagged as CVE-2021-36958. 

"A remote code execution vulnerability exists when the Windows Print Spooler service improperly performs privileged file operations. An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights. The workaround for this vulnerability is stopping and disabling the Print Spooler service," Microsoft's advisory said.

The previously disclosed bug CVE-2021-34481 in the Windows Print Spooler service allows a local attacker to escalate privileges to the level of 'system', letting the attacker install malware and create new accounts on Windows 10 machines. 

To mitigate potential threats, [Microsoft this week released an update](https://www.zdnet.com/article/microsoft-fixes-windows-10-printnightmare-flaw-with-this-update/) that changes default behavior for Point and Print features in Windows which will prevent an average user from adding or updating printers. After installation, Windows 10 requires admin privileges to install these driver changes.

While it will cause extra work for admins, Microsoft says it "strongly" believes that the security risk justifies this change.






Admins have an option to disable Microsoft's mitigation, but emphasized that it "will expose your environment to the publicly known vulnerabilities in the Windows Print Spooler service."

The issues affecting the Print Spooler service have escalated over the summer as a result of researchers finding different avenues to attack the set of flaws. 

CVE-2021-36958 and another PrintNightmare bug, tracked as CVE-2021-34483, were reported to Microsoft [by an Accenture security researcher, Victor Mata](https://twitter.com/offenseindepth/status/1425586599639887874), who [says he reported the issues in December](https://twitter.com/offenseindepth/status/1425574625384206339).  Other related Print Spooler bugs include [CVE-2021-1675 and CVE-2021-34527](https://www.zdnet.com/article/microsoft-adds-second-cve-for-printnightmare-remote-code-execution/). 

Will Dormann, a vulnerability analyst at the CERT/CC, pointed out the apparently incomplete fixes in the August 2021 Patch Tuesday updates. 

As he notes, security researcher Benjamin Delpy released a proof of concept for one of the PrintNightmare bugs in July. Dormann informed Microsoft that Delpy's PoC still worked on August 11, a day after August's Patch Tuesday. Delpy's proof of concept is what prompted Microsoft's latest disclosure about CVE-2021-36958, according to Dormann.    

"Microsoft did fix *something* related to your attack in their update for CVE-2021-36936, which describes nothing about what it fixes. For example, my PoC for VU#131152 now prompts for admin creds. However, [@gentilkiwi](https://twitter.com/gentilkiwi)'s PoC still works fine. Time for MS to issue a new CVE?," [wrote Dormann](https://twitter.com/wdormann/status/1425562960714416135). 





#### Tags:
[[Microsoft]] [[Windows]] [[PrintNightmare]] [[Delpy]] [[PoC]] [[ZDNet]]
