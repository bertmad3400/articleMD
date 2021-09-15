# OMIGOD: Azure users running Linux VMs need to update now
### If your Linux machine in Azure has port 5986, 5985, or 1270 externally exposed, you need to update it as soon as possible.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/omigod-azure-users-running-linux-vms-need-to-update-now/)
+ Date: September 15, 2021 -- 01:44 GMT (02:44 BST)
+ Author: Chris Duckett


## Article:
Unknown

![omi-auth-header.gif](https://www.zdnet.com/a/hub/i/2021/09/15/4d3eed75-aa2e-4099-815f-1ab7dd33449d/omi-auth-header.gif)
 Image: Wiz.io
 Users of Azure who are running Linux virtual machines may not be aware they are have a severely vulnerable piece of management software installed on their machine by Microsoft, that can be remotely exploited in an incredibly surprising and equally stupid way. 


As detailed by [Wiz.io](https://www.wiz.io/blog/secret-agent-exposes-azure-customers-to-unauthorized-code-execution), which found four vulnerabilities in Microsoft's [Open Management Infrastructure](https://github.com/Microsoft/omi) project, an attacker would be able to gain root access on a remote machine if they sent a single packet with the authentication header removed. 

"This is a textbook RCE vulnerability that you would expect to see in the 90's -- it's highly unusual to have one crop up in 2021 that can expose millions of endpoints," Wiz security researcher Nir Ohfeld wrote. 

"Thanks to the combination of a simple conditional statement coding mistake and an uninitialized auth struct, any request without an Authorization header has its privileges default to uid=0, gid=0, which is root." 

If OMI externally exposes port 5986, 5985, or 1270 then the system is vulnerable. 

"This is the default configuration when installed standalone and in Azure Configuration Management or System Center Operations Manager. Fortunately, other Azure services (such as Log Analytics) do not expose this port, so the scope is limited to local privilege escalation in those situations," Ohfeld added. 

The issue for users, as described by Ohfeld, is that OMI is silently installed when users install log collection, has a lack of public documentation, and runs with root privileges. Wiz found over 65% of Azure customers running Linux it looked at were vulnerable. 






In its advisory on the four CVEs released today -- [CVE-2021-38647](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38647) rated 9.8, [CVE-2021-38648](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38648%22) rated 7.8, [CVE-2021-38645](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38645) rated 7.8, and [CVE-2021-38649](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38649) rated 7.0 -- Microsoft said the fix for the vulnerabilities was pushed to its OMI code on August 11 to give its partners time to update before detailing the issues. 

Users should ensure they are running OMI version 1.6.8.1, with Microsoft adding instructions in its advisories to pull down the OMI updates from its repositories if machines are not updated yet. 

"System Center deployments of OMI are at greater risk because the Linux agents have been deprecated. Customers still using System Center with OMI-based Linux may need to manually update the OMI agent," Wiz warned. 

The vulnerabilities were part of Microsoft's [latest Patch Tuesday](https://www.zdnet.com/article/microsoft-september-2021-patch-tuesday-remote-code-execution-flaws-in-mshtml-open-management-fixed/). 

Like many vulnerabilities these days, a catchy name must be attached to them, in this case, Wiz dubbed them OMIGOD. 

### Related Coverage

* [Windows 11: Here's how to get Microsoft's free operating system update](/article/windows-11-heres-how-to-get-microsofts-free-operating-system-update/)
* [Azure Cosmos DB alert: This critical vulnerability puts users at risk](/article/azure-cosmos-db-alert-critical-vulnerability-puts-users-at-risk/)
* [AlmaLinux arrives on Azure cloud](/article/almalinux-arrives-on-azure-cloud/)
* [Microsoft grows Azure Space Australia with Nokia, SA govt and University of Adelaide](/article/microsoft-australia-grows-azure-space-with-nokia-sa-government-and-university-of-adelaide/)
* [Microsoft: We've fixed Azure container flaw that could have leaked data](/article/cloud-computing-microsoft-fixes-azure-container-flaw-that-could-have-leaked-data/)





#### Tags:
[[OMI]] [[Microsoft]] [[Linux]] [[ZDNet]]
