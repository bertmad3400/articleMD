# Partially Unpatched VMware Bug Opens Door to Hypervisor Takeover
### ESXi version 7 users are still waiting for a full fix for a high-severity heap-overflow security vulnerability, but Cloud Foundation, Fusion and Workstation users can go ahead and patch.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177428
+ Date: 2022-01-06T16:47:44+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2016/11/06232507/vmware-patch.jpg)

A security vulnerability in VMware’s Cloud Foundation, ESXi, Fusion and Workstation platforms could pave the way for hypervisor takeover in virtual environments – and a patch is still pending for some users.


The issue affects a wide swath of the virtualization specialist’s portfolio and affects Windows, Linux and Mac users. Details about the platforms:


* Cloud Foundation is VMware’s multicloud management platform, providing software-defined services for compute, storage, network, security, Kubernetes and so on.
* ESXi is a bare-metal hypervisor that installs on a server and partitions it into multiple virtual machines (VMs).
* Fusion is a software hypervisor that allows Intel-based Macs to run VMs with guest operating systems – such as Microsoft Windows, Linux, NetWare, Solaris or macOS.
* Workstation enables users to set up VMs on a single physical machine.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The bug (CVE-2021-22045) is a high-severity heap-overflow vulnerability carrying a CVSS rating of 7.7 out of 10. Heap overflows are memory issues that can result in data corruption or unexpected behavior by any process that accesses the affected memory area – in some cases resulting in remote code execution (RCE).


In this case, the problem specifically exists in the CD-ROM device emulation function of the affected products.


“A malicious actor with access to a virtual machine with CD-ROM device emulation may be able to exploit this vulnerability in conjunction with other issues, to execute code on the hypervisor from a virtual machine,” the vendor noted in its advisory. “Successful exploitation requires a CD image to be attached to the virtual machine.”


Taking over a hypervisor, which is the highly privileged software that creates and runs VMs and governs how resources are shared among them (such as memory and processing), can give cybercriminals a clear path to accessing any of the data or applications stored in the VMs it controls, depending on the security controls that are implemented.


Researcher “Jaanus K\xc3\xa4\xc3\xa4p” with Clarified Security, working with the Trend Micro Zero Day Initiative, was credited with discovering the bug.


**Patch VMware CVE-2021-22045 Now**
-----------------------------------


Affected product versions are: ESXi 6.5, 6.7 and 7 (version 7 remains unpatched for now); Fusion 12.x; Workstation 16.x; and all versions of VMware Cloud Foundation. Patch information can be found in the [vendor’s advisory](https://www.vmware.com/security/advisories/VMSA-2022-0001.html).


Users should patch as soon as possible, given that VMware is a favorite target for cybercriminals. For instance, just days after a critical CVE-2021-22005 RCE vulnerability in VMware vCenter was disclosed, a full working exploit [was public and being used](https://threatpost.com/working-exploit-vmware-vcenter-cve-2021-22005/175059/) in the wild.


ESXi users are especially at risk: While the solution makes it easy for multiple VMs to share the same hard-drive storage, it also sets systems up to be one-stop shopping spots for attacks, researchers say, since attackers can target the centralized virtual hard drives used to store data from across VMs.


“ESXi servers represent an attractive target for ransomware threat actors because they can attack multiple VMs at once, where each of the VMs could be running business-critical applications or services,” Andrew Brandt, principal researcher at Sophos, [recently explained](https://threatpost.com/vmware-esxi-encrypted-python-script-ransomware/175374/). “Attacks on hypervisors can be both fast and highly disruptive.”


He was discussing a spate of attacks in October that used a Python code that took less than three hours to complete a ransomware attack on ESXi servers, from initial breach to encryption. That incident joined other ransomware efforts targeting the hypervisor: REvil ransomware threat actors last year came up with a [Linux variant](https://threatpost.com/linux-variant-ransomware-vmwares-nas/167511/) that targeted VMware ESXi; and in September [HelloKitty joined](https://threatpost.com/linux-variant-of-hellokitty-ransomware-targets-vmware-esxi-servers/167883/) the growing list going after the juicy target. DarkSide [also targeted](https://cybersecurity.att.com/blogs/labs-research/darkside-raas-in-linux-version) ESXi servers last year.


**Workaround for ESXi v.7 Users**
---------------------------------


Of course, all of that is bad news for ESXi v.7 users, who don’t yet have a patch for this latest bug. VMware did, however, [issue a workaround](https://kb.vmware.com/s/article/87249) that can be used for now, involving disabling CD-ROM/DVD functionality.


The steps are:


1. Log in to a vCenter Server system using the vSphere Web Client.
2. Right-click the virtual machine and click Edit Settings.
3. Select the CD/DVD drive and uncheck “Connected” and “Connect at power on” and remove any attached ISOs.


To enumerate the VMs that have a CD-ROM/DVD device attached, users can run the following command, according to the vendor:


**Get-VM | Get-CDDrive | Where {$\_.extensiondata.connectable.connected -eq $true} | Select Parent**


Then the following command will remove and disconnect the attached CD-ROM/DVD device:


**Get-VM | Get-CDDrive | Where {$\_.extensiondata.connectable.connected -eq $true} | Set-CDDrive -NoMedia -confirm:$false**


***Password******Reset: [On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):*** *Fortify 2022 with a password-security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken.****[Register & stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)****– sponsored by Specops Software.*


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=HELLOKITTY]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=REvil]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Bern]] [[victim.country.name=Switzerland]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Vms]] [[Vmware]] [[Esxi]] [[Hypervisor]] [[Ransomware]] [[Cloud]] [[Linux]] [[ThreatPost]]
#### CVE's
[[CVE-2021-22045]] [[CVE-2021-22005]]

