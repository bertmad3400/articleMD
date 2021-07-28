# Critical Microsoft Hyper-V bug could haunt orgs for a long time
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/critical-microsoft-hyper-v-bug-could-haunt-orgs-for-a-long-time/)
+ Date: July 28, 2021
+ Author: Ionut Ilascu


## Article:
![Critical Microsoft Hyper-V bug could haunt orgs for a long time](https://www.bleepstatic.com/content/hl-images/2021/07/28/Microsoft_Hyper-V.jpg)


Technical details are now available for a vulnerability that affects Hyper-V, Microsoft's native hypervisor for creating virtual machines on Windows systems and in the Azure cloud computing environment.


Currently tracked as CVE-2021-28476, the security issue has a critical severity score of 9.9 out of 10. Exploiting it on unpatched machines can have a devastating impact as it allows crashing the host (denial of service) or execute arbitrary code on it.


### Terminate VMs or take full control


The bug is in Hyper-V's network switch driver (*vmswitch.sys*) and affects Windows 10 and Windows Server 2012 through 2019. It emerged in a build from August 2019 and [received a patch](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-28476) earlier this year in May.


Public details about the flaw are scarce at the moment but in a blog post today, researchers [Peleg Hadar](https://twitter.com/peleghd) of SafeBreach and [Ophir Harpaz](https://twitter.com/OphirHarpaz) of Guardicore explain where the fault is and why it is exploitable. The two researchers found the bug together and disclosed it privately to Microsoft.


The flaw stems from the fact that Hyper-V’s virtual switch (*vmswitch*) does not validate the value of an OID (object identifier) request that is intended for a network adapter (external or connected to *vmswitch*).


An OID request can include hardware offloading, Internet Protocol security (IPsec), and single root I/O virtualization (SR-IOV) requests.



“While processing OID requests, vmswitch traces their content for logging and debugging purposes; this also applies to OID\_SWITCH\_NIC\_REQUEST. However, due to its encapsulated structure, vmswitch needs to have special handling of this request and dereference OidRequest to trace the inner request as well. The bug is that vmswitch never validates the value of OidRequest and can thus dereference an invalid pointer,” [Harpaz explains](https://www.guardicore.com/labs/critical-vulnerability-in-hyper-v-allowed-attackers-to-exploit-azure/)



An attacker successfully leveraging this vulnerability needs to have access to a guest virtual machine (VM) and send a specially crafted packet to the Hyper-V host.


The result can be either crashing the host - and terminate all the VMs running on top of it, or gaining remote code execution on the host, which gives complete control over it and the attached VMs.


### Orgs are slow to patch


While the Azure service is safe from this issue, some local Hyper-V deployments are likely still vulnerable as not all admins update Windows machines when patches come out.


Harpaz told BleepingComputer that vulnerabilities that remain unpatched for years on machines in enterprise networks are a common encounter for Guardicore.


One of the most common examples is EternalBlue that became known in April 2017 - patched a month earlier and leveraged in the destructive WannaCry and NotPetya cyberattacks.



“There are so many Windows Servers today that are vulnerable to well-known bugs, I won't be surprised if this bug stays unpatched for a very long time in organizations” - Ophir Harpaz



Harpaz and Hadar are scheduled for a [presentation at the Black Hat](https://www.blackhat.com/us-21/briefings/schedule/#hafl-our-journey-of-fuzzing-hyper-v-and-discovering-a--day-23498) security conference on August 4 on their research and how found the vulnerability using an in-house fuzzing program called hAFL1.




#### Tags:
[[Windows]] [[Harpaz]] [[Hyper-V]] [[OID]] [[vmswitch]] [[Bleeping Computer]]
