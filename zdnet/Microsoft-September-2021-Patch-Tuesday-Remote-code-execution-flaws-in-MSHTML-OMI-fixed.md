# Microsoft September 2021 Patch Tuesday: Remote code execution flaws in MSHTML, OMI fixed
### This month's round of security fixes tackles critical software issues including a zero-day flaw known to be exploited in the wild.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-september-2021-patch-tuesday-remote-code-execution-flaws-in-mshtml-open-management-fixed/)
+ Date: September 14, 2021 -- 18:14 GMT (19:14 BST)
+ Author: Charlie Osborne


## Article:
Unknown


[Microsoft](https://www.zdnet.com/topic/microsoft/) has released over 60 security fixes and updates resolving issues including a remote code execution (RCE) flaw in MSHTML and other critical bugs.

The Redmond giant's latest [round of patches](https://msrc.microsoft.com/update-guide/en-us), usually released on the second Tuesday of each month in what is known as Patch Tuesday, landed on September 14.

Products impacted by September's security update include Azure Open Management Infrastructure, Azure Sphere, Office Excel, PowerPoint, Word, and Access; the kernel, Visual Studio, Microsoft Windows DNS, and BitLocker, among other software.  

*Read on*: 

* [Microsoft Teams: This new feature will make your meetings more interactive](https://www.zdnet.com/article/microsoft-teams-this-new-feature-will-make-your-meetings-more-interactive/)  

* [What's the fastest Windows 10 web browser in 2021?](https://www.zdnet.com/article/whats-2021-windows-10-fastest-web-browser/)  


On September 7, Microsoft said a remote code execution flaw [in MSHTML](https://www.zdnet.com/article/microsoft-cisa-urge-use-of-mitigations-and-workarounds-for-office-document-vulnerability/) had been identified and was being used in a limited number of attacks against Windows systems. The zero-day vulnerability, tracked as [CVE-2021-40444](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40444), has been resolved in this patch round and the firm is urging users to accept the security fix immediately. 

Some other notable vulnerabilities resolved in this update are: 

* [CVE-2021-38647](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38647): With a CVSS score of 9.8, this is the most critical bug on September's list. This vulnerability impacts the Open Management Infrastructure (OMI) program and allows attackers to perform RCE attacks without authentication by sending malicious messages via HTTPS to port 5986.

"Some Azure products, such as Configuration Management, expose an HTTP/S port for interacting with OMI (port 5986 also known as WinRMport)," Microsoft says. "This configuration where the HTTP/S listener is enabled could allow remote code execution. It is important to mention that most Azure services that use OMI deploy it without exposing the HTTP/S port."

* [CVE-2021-36968](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36968):  A publicly disclosed Windows DNS privilege escalation zero-day vulnerability, issued a CVSS score of 7.8. Microsoft has not found any evidence, as of yet, of exploitation in the wild.
* [CVE-2021-26435](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26435): A critical flaw (CVSS 8.1) in the Microsoft Windows scripting engine. However, this memory corruption flaw requires user interaction to trigger.  

* [CVE-2021-36967](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36967): A vulnerability, deemed critical and issued a CVSS score of 8.0, in the Windows WLAN AutoConfig service which can be used for elevation of privileges.   







According to the [Zero Day Initiative](https://www.zerodayinitiative.com/blog/2021/9/14/the-september-2021-security-update-review-kpgpb) (ZDI), the 66 CVEs -- including three critical, one moderate, and the rest deemed important -- reveal a volume slightly higher than the average patch rate across 2021, while this is still below 2020 volume. In addition, 20 CVEs were patched by Microsoft Edge (Chromium) earlier in September. In total, 11 of these vulnerabilities were submitted through the Zero Day Initiative, for a total of 86 CVEs.

On Wednesday, Microsoft warned of "[Azurescape](https://msrc-blog.microsoft.com/2021/09/08/coordinated-disclosure-of-vulnerability-in-azure-container-instances-service/)," a vulnerability mitigated by the Redmond giant that impacts Azure Container Instances (ACI). The bug was reported by a researcher from [Palo Alto Networks](https://unit42.paloaltonetworks.com/azure-container-instances/). 

Last month, Microsoft resolved [44 vulnerabilities](https://www.zdnet.com/article/microsofts-august-2021-patch-tuesday-45-flaws-fixed-seven-critical-including-print-spooler-vulnerability/) in the August batch of security fixes. In total, three were categorized as zero-day flaws, and 13 allowed attackers to perform RCE attacks. Included in the patch release was a fix for a well-publicized [Windows Print Spooler](https://www.zdnet.com/article/windows-print-spooler-hit-with-local-privilege-escalation-vulnerability/) vulnerability which could be weaponized for the purposes of local privilege escalation.

A month prior, the tech giant tackled [117 bugs](https://www.zdnet.com/article/microsoft-july-2021-patch-tuesday-117-vulnerabilities-pwn2own-exchange-server-bug-fixed/) during the July Patch Tuesday.

In other security news, Apple has [patched a zero-day](https://www.zdnet.com/article/apple-releases-update-fixing-nso-spyware-vulnerability-affecting-macs-iphones-ipads-and-watches/) vulnerability reportedly exploited by NSO Group to spy on users of Mac, iPhone, iPad, and Watch products. In addition, Google has pushed out [a security update](https://www.zdnet.com/article/google-patches-two-chrome-zero-days/) resolving two zero-day bugs being actively exploited in the wild. 



---

Alongside Microsoft's Patch Tuesday round, other vendors, too, have published security updates which can be accessed below.

* Adobe [security updates](https://helpx.adobe.com/security.html)
* SAP [security updates](https://wiki.scn.sap.com/wiki/display/PSR/The+Official+SAP+Product+Security+Response+Space)
* VMWare [security advisories](https://www.vmware.com/security/advisories.html)
* Intel [security updates](https://www.intel.com/content/www/us/en/security-center/default.html)





#### Tags:
[[Microsoft]] [[Windows]] [[zero-day]] [[vulnerability,]] [[CVSS]] [[HTTP/S]] [[ZDNet]]
