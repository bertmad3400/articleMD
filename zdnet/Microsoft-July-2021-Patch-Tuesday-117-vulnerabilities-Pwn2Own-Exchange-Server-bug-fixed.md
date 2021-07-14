# Microsoft July 2021 Patch Tuesday: 117 vulnerabilities, Pwn2Own Exchange Server bug fixed
### Over 100 CVEs, many of which lead to RCE, have been tackled this month.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-july-2021-patch-tuesday-117-vulnerabilities-pwn2own-exchange-server-bug-fixed/)
+ Date: July 13, 2021 -- 18:16 GMT (19:16 BST)
+ Author: Charlie Osborne


## Article:
Unknown

[Microsoft](https://www.zdnet.com/topic/microsoft/) has released 117 security fixes for software including a remote code execution (RCE) vulnerability in Exchange Server found by participants of the Pwn2Own competition. 


The Redmond giant's latest [round of patches](https://msrc.microsoft.com/update-guide/releaseNote/2021-Jul), usually released on the second Tuesday of each month in what is known as Patch Tuesday, includes fixes for 117 flaws tackling RCEs, privilege escalation, spoofing, memory corruption, and information disclosure. Thirteen are considered critical and nine are zero-days -- with four under active exploit. 

Products impacted by Microsoft's latest security update, issued on July 13, include Microsoft Office, SharePoint, Excel, Microsoft Exchange Server, Windows Defender, Windows Kernel, and Windows SMB.  

***Read on*****:**  

* [Microsoft acquires cybersecurity company RiskIQ](https://www.zdnet.com/article/microsoft-acquires-cybersecurity-company-riskiq/)


* [The best parts of Windows 11 are already in Windows 10. You just have to enable them](https://www.zdnet.com/article/best-parts-of-windows-11-are-already-in-windows-10-you-just-have-to-enable-them/)



Some of the most interesting vulnerabilities resolved in this update are:  

* [**CVE-2021-31206**](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-31206): A Microsoft Exchange Server RCE found during Pwn2Own.
* [**CVE-2021-34448**](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34448): An actively exploited scripting engine memory corruption vulnerability, requiring a victim to actively visit a malicious website or to click a malicious link.
* [**CVE-2021-34494**](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34494): A Windows DNS Server RCE, albeit restricted to DNS servers only.
* [**CVE-2021-34458**](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34458): A Windows Kernel RCE which permits a single root input/output virtualization (SR-IOV) device, assigned to a guest, to potentially tamper with PCIe associates.

The latest round of patches comes just a week after [an emergency fix](https://www.zdnet.com/article/microsofts-printnightmare-patch-is-now-causing-problems-for-some-printers/) was issued by Microsoft to rectify a security flaw nicknamed "PrintNightmare." Tracked under CVE-2021-1675 and CVE-2021-34527, the combination of RCE and a local privilege escalation flaw is already impacting some printers, and exploit code has been released. 

In total, four of the vulnerabilities -- [CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) (PrintNightmare), [CVE-2021-34448](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34448), [CVE-2021-31979](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31979), and [CVE-2021-33771](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-33771) -- are listed as exploited in the wild.  






Microsoft thanked researchers from Google Security, Checkmarx, the Trend Micro Zero Day Initiative, and Fortinet's FortiGuard Lab, among other organizations, for reporting the now-patched security flaws, A number of vulnerabilities were also reported by Microsoft Threat Intelligence Center (MSTIC). 

According to the [Zero Day Initiative](https://www.zerodayinitiative.com/blog/2021/7/13/the-july-2021-security-update-review) (ZDI), which reported 17 of the bugs, this month's volume of fixes "is more than the last two months combined and on par with the monthly totals from 2020." 

Last month, [Microsoft resolved 50 vulnerabilities](https://www.zdnet.com/article/microsoft-june-2021-patch-tuesday-50-vulnerabilities-patched-including-six-zero-days-exploited-in-the-wild/) in the June batch of security fixes. These included seven zero-day bugs, six of which were reported by the Redmond giant as being actively exploited.  

A month prior, the tech giant tackled 55 security flaws during [May Patch Tuesday](https://www.zdnet.com/article/microsofts-may-2021-patch-tuesday-55-flaws-fixed-four-critical/). Four of which were deemed critical, and three were zero-days. 



---

Alongside Microsoft's Patch Tuesday round, other vendors, too, have published security updates which can be accessed below. 

* Adobe [security updates](https://helpx.adobe.com/security.html)
* SAP [security updates](https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=580617506)
* VMWare [security advisories](https://www.vmware.com/security/advisories.html)
* Intel [security updates](https://www.intel.com/content/www/us/en/security-center/default.html)





#### Tags:
[[Microsoft]] [[Windows]] [[RCE]] [[--]] [[ZDNet]]
