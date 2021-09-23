# Russian missile fuel maker targeted with recent Office zero-day
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/russian-missile-fuel-maker-targeted-with-recent-office-zero-day/)
+ Date: September 23, 2021
+ Author: Catalin Cimpanu


## Article:
![Russian missile fuel maker targeted with recent Office zero-day](https://therecord.media/wp-content/uploads/2021/09/Russia-military-army-Moscow.png)

Russian organizations, including a major defense contractor, have been targeted in a suspected cyber-espionage operation that is abusing a recently disclosed Office zero-day.


Security firm Malwarebytes, which first spotted some of the attacks, identified one of the targets as [JSC GREC Makeyev](https://www.globalsecurity.org/wmd/world/russia/makeyev-grc.htm), a known developer of liquid and solid fuel for Russia’s ballistic missiles and space rocket program.





The attacks were a classic spear-phishing campaign that sent boobytrapped Office documents to the organization’s employees.


The documents, claiming to be Word files from the company’s HR department, contained an exploit for [**CVE-2021-40444**](https://therecord.media/tag/cve-2021-40444/), a vulnerability in the old Internet Explorer MHTML component that can be exploited via Office files to run malicious code on unpatched Windows systems and install malware.


“The email asks employees to please fill out the form and send it to HR, or reply to the mail. When the receiver wants to fill out the form they will have to enable editing. And that action is enough to trigger the exploit,” Malwarebytes researchers explained today.


“The attack depends on MSHTML loading a specially crafted ActiveX control when the target opens a malicious Office document. The loaded ActiveX control can then run arbitrary code to infect the system with more malware.”


### Identity of the attackers still unknown


Other Office documents containing the same exploit were also spotted, this time posing as fines for “illegal activity,” issued by Russia’s Ministry of the Interior.


Malwarebytes said it was unable to link these documents to specific targets and that it is still investigating the identity of the group or groups behind the attacks leveraging the CVE-2021-40444 exploit.


“Given the targets, especially the first one, we suspect that there may be a state-sponsored actor behind these attacks,” [the company said today](https://blog.malwarebytes.com/reports/2021/09/mshtml-attack-targets-russian-state-rocket-centre-and-interior-ministry/).


Malwarebytes noted that attacks against Russian organizations are generally rare, which the company isn’t wrong about.


In May 2021, in a rare report, the FSB said that [foreign “cyber mercenaries”](https://therecord.media/fsb-nktski-foreign-cyber-mercenaries-breached-russian-federal-agencies/) had breached several Russian government agencies. Those attacks were later tied to Chinese cyber-espionage groups by security firms like [SentinelOne](https://www.sentinelone.com/labs/thundercats-hack-the-fsb-your-taxes-didnt-pay-for-this-op/) and [Group-IB](https://blog.group-ib.com/task).


[Microsoft patched CVE-2021-40444](https://therecord.media/microsoft-patches-office-zero-day-in-todays-patch-tuesday/) on September 14, during the September 2021 Patch Tuesday.


Attacks abusing this former zero-day have also targeted [Russian telcos](https://twitter.com/alex_lanstein/status/1437565704778223618), and, according to RiskIQ, an [individual associated with the Ryuk/Conti ransomware gang](https://www.riskiq.com/blog/external-threat-management/wizard-spider-windows-0day-exploit/) has also started experimenting with this vector.





#### Tags:
[[Malwarebytes]] [[The Record]]
