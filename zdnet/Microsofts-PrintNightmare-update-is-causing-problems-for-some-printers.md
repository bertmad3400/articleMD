# Microsoft's PrintNightmare update is causing problems for some printers
### Microsoft acknowledges its patch to fix the print spooler flaw has affected some printers.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsofts-printnightmare-patch-is-now-causing-problems-for-some-printers/)
+ Date: July 9, 2021 -- 14:54 GMT (15:54 BST)
+ Author: Liam Tung


## Article:
Unknown

Microsoft's emergency update which included a fix for the so-called PrintNightmare print spooler problem has the unexpected side-effect of causing a problem with some printers.


The PrintNightmare flaw is a major security risk for enterprise, where print spoolers are used on Windows machines. Microsoft considered it serious enough to [rush out a patch last week](https://www.zdnet.com/article/install-immediately-microsoft-delivers-emergency-patch-for-printnightmare-security-bug/), before its usual Patch Tuesday update.   

**Also:** [**Best printers for your home office**](https://www.zdnet.com/article/best-printer/)

The PrintNightmare bug is being [tracked as CVE-2021-1675 and CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527). One of them is a remote code execution flaw and the other is a local privilege escalation flaw. An additional concern was that exploit code was in the public domain before Microsoft released a patch for it.

Microsoft notes that an attacker can use the bug to write whatever code they want with system privileges. From there, they could install programs; view, change, or delete data; or create new accounts with full user rights. 

But now that patches are being installed, some customers are reporting an impact on some printers.

Microsoft itself has warned of the issue.






"After installing this update, you might have issues printing to certain printers. Most affected printers are receipt or label printers that connect via USB. Note This issue is not related to CVE-2021-34527 or CVE-2021-1675," it said.

"This issue is resolved using Known Issue Rollback (KIR). Please note that it might take up to 24 hours for the resolution to propagate automatically to consumer devices and non-managed business devices.

"Restarting your Windows device might help the resolution apply to your device faster. For enterprise-managed devices that have installed an affected update and encountered this issue, it can be resolved by installing and configuring a special Group Policy," it said.

Printer maker Zebra confirmed that some of its devices were being affected."We are aware of issues affecting multiple brands of printers when printing from PCs that have been recently updated via the Windows Update Service (KB5004945, KB5004760, or KB5003690). The most common symptom is print jobs being sent, but not actually printing," it said.

"This issue is observed after users install the Windows 10 out-of-band security update KB5004945 (or previous updates, KB5004760 and KB5003690). The KB5004945 security update addresses a remote code execution exploit in the Windows Print Spooler service, known as 'PrintNightmare,'"it added.

Microsoft rounded out its patches for Windows 10 systems this week, delivering patches for Windows 10 version 1607, Windows Server 2016, and Windows Server 2012. It was serious enough for Microsoft to release patches for Windows 7, which reached mainstream end of support in January 2020. Microsoft still provides security updates to organizations paying for extended support on Windows 7. 

Microsoft has advised customers to disable the print spooler service until patches are applied. 

The patch introduces some changes to how organizations handle the installation of drivers on Windows machines. It prevents general users from installing printer driver software updates. Some security researchers have found [there are ways to bypass Microsoft's patch](https://www.zdnet.com/article/get-updating-microsoft-delivers-printnightmare-patch-for-more-windows-versions/).





#### Tags:
[[Windows]] [[Microsoft]] [[PrintNightmare]] [[KB5004945]] [[ZDNet]]
