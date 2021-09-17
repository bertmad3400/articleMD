# Microsoft asks Azure Linux admins to manually patch OMIGOD bugs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-asks-azure-linux-admins-to-manually-patch-omigod-bugs/)
+ Date: September 17, 2021
+ Author: Sergiu Gatlan


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/09/15/OMIGOD.jpg)


Microsoft has issued additional guidance on securing Azure Linux machines impacted by recently addressed critical OMIGOD vulnerabilities.


The four security flaws (allowing remote code execution and privilege escalation) were found in the Open Management Infrastructure (OMI) software agent silently installed on more than half of Azure instances.


According to Wiz researchers Nir Ohfeld and Shir Tamari, these bugs impact thousands of Azure customers and millions of endpoints.


Root privileges with a single packet
------------------------------------


[OMIGOD](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-critical-bugs-in-secretly-installed-azure-linux-app/) affects Azure VMs who use Linux management solutions with services such as Azure Automation, Azure Automatic Update, Azure Operations Management Suite (OMS), Azure Log Analytics, Azure Configuration Management, or Azure Diagnostics.


Successful exploitation enables attackers to escalate privileges and execute code remotely on compromised Linux VMs.


"This is a textbook RCE vulnerability that you would expect to see in the 90’s – it’s highly unusual to have one crop up in 2021 that can expose millions of endpoints," Wiz researcher Nir Ohfeld said regarding the CVE-2021-38647 RCE bug.


"With a single packet, an attacker can become root on a remote machine by simply removing the authentication header. It’s that simple.


"[T]his vulnerability can be also used by attackers to obtain initial access to a target Azure environment and then move laterally within it."


Manual updates required for existing Azure VMs
----------------------------------------------


While working to address these bugs, Microsoft introduced an [Enhanced Security commit](https://github.com/microsoft/omi/commit/4ce2cf1cb0aa656b8eb934c5acc3f4d6a6796bfa) on August 11, exposing all the details a threat actor would need to create an OMIGOD exploit.


The company released a [patched OMI software agent version](https://github.com/microsoft/omi/releases) on September 8 and assigned CVEs only one week later, as part of the September Patch Tuesday.


To make things worse for affected customers, Microsoft has no mechanism available to auto-update vulnerable agents on all impacted Azure Linux machines.


Instead, the company [has urged customers](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38647) to upgrade the vulnerable software manually to secure their endpoints from attacks using OMIGOD exploits.


"*Customers must update vulnerable extensions for their Cloud and On-Premises deployments* as the updates become available per schedule outlined in table below," the Microsoft Security Response Center team said. [emphasis ours]


"New VMs in these regions will be protected from these vulnerabilities post the availability of updated extensions."


To manually update the OMI agent, you can also use a Linux package manager:


* Add the MSRepo to your system. Based on the Linux OS that you are using, refer to this link to install the MSRepo to your system: [Linux Software Repository for Microsoft Products | Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/administration/Linux-Package-Repository-for-Microsoft-Software)


* You can then use your platform's package tool to upgrade OMI (for example, `sudo apt-get install omi` or `sudo yum install omi`).




Microsoft will update vulnerable Azure VM management extensions across Azure regions on cloud deployments with auto-update turned on (the extensions will be transparently patched without a VM restart).


However, this means that customers you will still have to make changes manually to your Azure Linux machines if the automatic extension updates are not toggled on.


"Updates are already available for DSC and SCOM to address the remote execution vulnerability (RCE)," the MSRC team added.


"While updates are being rolled out using safe deployment practices, customers can protect against the RCE vulnerability by ensuring VMs are deployed within a Network Security Group (NSG) or behind a perimeter firewall and restrict access to Linux systems that expose the OMI ports (TCP 5985, 5986, and 1207)."




#### Tags:
[[Linux]] [[Microsoft]] [[OMIGOD]] [[VMs]] [[OMI]] [[RCE]] [[Bleeping Computer]]
