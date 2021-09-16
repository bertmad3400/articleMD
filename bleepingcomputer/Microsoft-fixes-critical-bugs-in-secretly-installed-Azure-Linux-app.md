# Microsoft fixes critical bugs in secretly installed Azure Linux app
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-critical-bugs-in-secretly-installed-azure-linux-app/)
+ Date: September 15, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft fixes critical bugs impacting over 50% of Azure instances](https://www.bleepstatic.com/content/hl-images/2021/09/15/OMIGOD-headpic.jpg)


Microsoft has addressed four critical vulnerabilities collectively known as OMIGOD, found in the Open Management Infrastructure (OMI) software agent silently installed on Azure Linux machines accounting for more than half of Azure instances.


[OMI](https://cloudblogs.microsoft.com/windowsserver/2012/06/28/open-management-infrastructure/) is a software service for IT management with support for most UNIX systems and modern Linux platforms, used by multiple Azure services, including [Open Management Suite](https://azure.microsoft.com/en-us/resources/videos/operations-management-suite-oms-overview/) (OMS), [Azure Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-overview), [Azure Automation](https://azure.microsoft.com/en-us/services/automation/).


These vulnerabilities were found by cloud security firm Wiz researchers Nir Ohfeld and Shir Tamari, who dubbed them [**OMIGOD**](https://www.wiz.io/blog/secret-agent-exposes-azure-customers-to-unauthorized-code-execution).


"Problematically, this 'secret' agent is both widely used (because it is open source) and completely invisible to customers as its usage within Azure is completely undocumented," [Ohfeld said](https://www.wiz.io/blog/omigod-critical-vulnerabilities-in-omi-azure).


Millions of endpoints exposed to attacks
----------------------------------------


The researchers "conservatively estimate" that thousands of Azure customers and millions of endpoints are impacted by these security flaws:


* [CVE-2021-38647](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38647) – Unauthenticated RCE as root (Severity: 9.8/10)
* [CVE-2021-38648](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38648) – Privilege Escalation vulnerability (Severity: 7.8/10)
* [CVE-2021-38645](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38645) – Privilege Escalation vulnerability (Severity: 7.8/10)
* [CVE-2021-38649](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38649) – Privilege Escalation vulnerability (Severity: 7.0/10)


All Azure customers with Linux machines running one of the following tools or services are at risk:


* Azure Automation
* Azure Automatic Update
* Azure Operations Management Suite (OMS)
* Azure Log Analytics
* Azure Configuration Management
* Azure Diagnostics


"When users enable any of these popular services, OMI is silently installed on their Virtual Machine, running at the highest privileges possible," [Ohfeld added](https://www.wiz.io/blog/secret-agent-exposes-azure-customers-to-unauthorized-code-execution). "This happens without customers’ explicit consent or knowledge. Users simply click agree to log collection during set-up and they have unknowingly opted in."


Other Microsoft customers are also impacted by the OMIGOD flaws, given that the OMI agent can also be manually installed on-premise as it is built in the System Center for Linux, which is Microsoft's server management tool.


"This is a textbook RCE vulnerability that you would expect to see in the 90’s – it’s highly unusual to have one crop up in 2021 that can expose millions of endpoints," Ohfeld added regarding the CVE-2021-38647 RCE bug. 


"With a single packet, an attacker can become root on a remote machine by simply removing the authentication header. It’s that simple.


"[T]his vulnerability can be also used by attackers to obtain initial access to a target Azure environment and then move laterally within it."




> 
> This is even more severe. The RCE is the simplest RCE you can ever imagine. Simply remove the auth header and you are root. remotely. on all machines. Is this really 2021? [pic.twitter.com/iIHNyqgew4](https://t.co/iIHNyqgew4)
> 
> 
> — Ami Luttwak (@amiluttwak) [September 14, 2021](https://twitter.com/amiluttwak/status/1437898746747097090?ref_src=twsrc%5Etfw)


How to secure your Azure Linux endpoint
---------------------------------------


"Microsoft released a patched OMI version (1.6.8.1). In addition, Microsoft advised customers to manually OMI, see the suggested steps by Microsoft [here](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38647)," Wiz security researcher Nir Ohfeld said.


"If you have OMI listening on ports 5985, 5986, 1270 we advise limiting network access to those ports immediately in order to protect from the RCE vulnerability (CVE-2021-38647)."


Even though Microsoft introduced a [Enhanced Security commit](https://github.com/microsoft/omi/commit/4ce2cf1cb0aa656b8eb934c5acc3f4d6a6796bfa) on August 11, 2021, effectively exposing all the details threat actors needed to develop an exploit, the company only released a [patched OMI software agent version](https://github.com/microsoft/omi/releases) on September 8 and only assigned CVEs one week later, as part of this month's Patch Tuesday. 


To make things worse, there is no auto-update mechanism Microsoft can use to update the vulnerable agents on all Azure Linux machines, which means that customers have to upgrade it manually to secure endpoints from any incoming attacks using OMIGOD exploits.


To manually update the OMI agent, you have to:


* Add the MSRepo to your system. Based on the Linux OS that you are using, refer to this link to install the MSRepo to your system: [Linux Software Repository for Microsoft Products | Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/administration/Linux-Package-Repository-for-Microsoft-Software)


* You can then use your platform's package tool to upgrade OMI (for example, `sudo apt-get install omi` or `sudo yum install omi`).







#### Tags:
[[Microsoft]] [[OMI]] [[Linux]] [[RCE]] [[Ohfeld]] [[(Severity:]] [[Bleeping Computer]]
