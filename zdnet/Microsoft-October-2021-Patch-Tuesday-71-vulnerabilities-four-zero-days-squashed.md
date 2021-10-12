# Microsoft October 2021 Patch Tuesday: 71 vulnerabilities, four zero-days squashed
### This month's round of security fixes includes patches for zero-days, one of which is being actively exploited.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-october-2021-patch-tuesday-71-vulnerabilities-four-zero-days-squashed/)
+ Date: October 12, 2021
+ Author: Charlie Osborne


## Article:
Unknown


[Microsoft](https://www.zdnet.com/topic/microsoft/) has released 71 security fixes for software including an actively-exploited zero-day bug in Win32k. 

The Redmond giant's latest [round of patches](https://msrc.microsoft.com/update-guide/en-us), usually released on the second Tuesday of each month in what is known as Patch Tuesday, includes fixes for a total of four zero-day flaws, three of which are public.

Products impacted by October's security update include Microsoft Office, Exchange Server, MSHTML, Visual Studio, and the Edge browser. 

The zero-day bugs are tracked as CVE-2021-40449, CVE-2021-41338, CVE-2021-40469, and CVE-2021-41335.   

[CVE-2021-40449](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40449) is being actively exploited. Issued a CVSS severity score of 7.8, this vulnerability impacts the Win32K kernel driver. Boris Larin (oct0xor) with Kaspersky reported the flaw to Microsoft, and [in a blog post](https://securelist.com/mysterysnail-attacks-with-windows-zero-day/104509/) published today, the cybersecurity firm said a clutter of activity, dubbed MysterySnail, is utilizing the use-after-free flaw.

"Besides finding the zero-day in the wild, we analyzed the malware payload used along with the zero-day exploit, and found that variants of the malware were detected in widespread espionage campaigns against IT companies, military/defense contractors, and diplomatic entities," Kaspersky says.

Immersive Labs' Kevin Breen, Director of Cyber Threat Research, said that this issue "should definitely be a priority to patch." 






"It's noted as 'exploitation detected', meaning attackers are already using it against organizations to gain admin rights," Breen commented. "Gaining this level of access on a compromised host is the first step towards becoming a domain admin -- and securing full access to a network."

*Read on*: 

* [EU regulators asking Teams rivals about Microsoft's bundling practices, per Slack's 2020 complaint](https://www.zdnet.com/article/eu-regulators-said-to-be-askingteams-rivals-about-microsofts-bundling-practices-per-slacks-2020-complaint/)  

* [Broke your Xbox? Right to repair just took a big step forward at Microsoft](https://www.zdnet.com/article/right-to-repair-microsoft-meets-shareholder-demands/)  


The three other zero-day vulnerabilities resolved in this round of patches are [CVE-2021-41338](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41338) (CVSS 5.5), a Windows AppContainer Firewall bug that permits attackers to bypass security features; [CVE-2021-40469](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40469) (CVSS 7.2), an RCE in Windows DNS Server; and [CVE-2021-41335](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41335) (CVSS 7.8), an elevation of privilege bug in the Windows Kernel. 

Three critical bugs, [CVE-2021-40486](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40486), [CVE-2021-38672](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38672), and [CVE-2021-40461](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40461), are also of note. The first security flaw impacts Microsoft Word whereas the other two affect Hyper-V. If exploited, all of them can lead to remote code execution.

According to the [Zero Day Initiative](https://www.zerodayinitiative.com/blog) (ZDI), 11 of the security flaws patched this month were submitted through the ZDI program, including bugs resolved earlier in the month by the Edge browser team.

[Last month](https://www.zdnet.com/article/microsoft-september-2021-patch-tuesday-remote-code-execution-flaws-in-mshtml-open-management-fixed/), Microsoft resolved over 60 bugs in the September batch of security fixes including an RCE flaw in MSHTML and a Windows DNS privilege escalation zero-day vulnerability. 

A month prior, the tech giant tackled 45 security flaws -- seven of which were deemed critical -- during the [August Patch Tuesday](https://www.zdnet.com/article/microsofts-august-2021-patch-tuesday-45-flaws-fixed-seven-critical-including-print-spooler-vulnerability/).

In other Microsoft news, the tech giant is readying a [new Feedback Portal](https://www.zdnet.com/article/microsoft-readies-new-feedback-portal-preview-for-end-of-2021/), expected to be ready in preview mode, by the end of 2021. The portal will be opened first for Microsoft 365 and Microsoft Edge products. The Redmond giant has also [recently warned](https://www.zdnet.com/article/microsoft-warns-over-password-attacks-against-250-office-365-customers/) of password spraying attacks being launched against Office 365 customers. 



---

Alongside Microsoft's Patch Tuesday round, other vendors, too, have published security updates which can be accessed below.

* Adobe [security updates](https://helpx.adobe.com/security.html)
* SAP [security updates](https://wiki.scn.sap.com/wiki/display/PSR/The+Official+SAP+Product+Security+Response+Space)
* VMWare [security advisories](https://www.vmware.com/security/advisories.html)
* Intel [security updates](https://www.intel.com/content/www/us/en/security-center/default.html)





#### Tags:
[[Microsoft]] [[zero-day]] [[Windows]] [[(CVSS]] [[ZDNet]]
