# VMware Warns of Ransomware-Friendly Bug in vCenter Server
### VMware urged immediate patching of the max-severity, arbitrary file upload flaw in Analytics service, which affects all appliances running default 6.5, 6.7 and 7.0 installs.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174901)
+ Date: September 22, 2021  12:17 pm
+ Author: Lisa Vaas


## Article:
VMware has released a [security update](https://www.vmware.com/security/advisories/VMSA-2021-0020.html) that includes patches for 19 CVE-numbered vulnerabilities that affect the company’s vCenter Server virtualization management platform and its hybrid Cloud Foundation platform for managing VMs and orchestrating containers.


They’re all serious, but one – CVE-2021-22005, a critical arbitrary file upload vulnerability in the Analytics service that’s been assigned the maximum CVSSv3 base score of 9.8 – is uber nasty.


“This vulnerability can be used by anyone who can reach vCenter Server over the network to gain access, regardless of the configuration settings of vCenter Server,” [said Bob Plankers](https://blogs.vmware.com/vsphere/2021/09/vmsa-2021-0020-what-you-need-to-know.html), Technical Marketing Architect at VMware.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The time to act is yesterday, Plankers wrote:



> “In this era of ransomware it is safest to assume that an attacker is already inside your network somewhere, on a desktop and perhaps even in control of a user account, which is why we strongly recommend declaring an emergency change and patching as soon as possible.” —Bob Planker, [VMware vSphere blog](https://blogs.vmware.com/vsphere/2021/09/vmsa-2021-0020-what-you-need-to-know.html)
> 
> 


The security update addresses flaws in vCenter Server 6.5, 6.7, and 7.0.


When to Act?
------------


The time to act is “Right now,” Plankers said. “These updates fix a critical security vulnerability, and your response needs to be considered at once.”


CVE-2021-22005 can be used to execute commands and executables on the vCenter Server Appliance. The company didn’t tiptoe around the need for urgent action: Users should patch this vulnerability “immediately,” VMware said in its [FAQ for VMSA-2021-0020](https://core.vmware.com/vmsa-2021-0020-questions-answers-faq). The bug could have nasty repercussions, with exploits likely being hammered out “minutes after the disclosure,” it said:



> “The ramifications of this vulnerability are serious and it is a matter of time – likely minutes after the disclosure – before working exploits are publicly available.” [—VMware FAQ](https://core.vmware.com/vmsa-2021-0020-questions-answers-faq)
> 
> 


Assume That Attackers Are Already In Your System
------------------------------------------------


This is a ransomware-friendly bug. VMware pointed to the [all-too-real threat](https://threatpost.com/ransomware-volumes-record-highs-2021/168327/) of spiraling ransomware attacks: a growing risk that makes the “safest stance” the assumption that threat actors have already seized control of a desktop and a user account via [phishing](https://threatpost.com/hackers-deep-sea-phishing/174868/) or [spearphishing](https://threatpost.com/linkedin-spear-phishing-job-hunters/165240/) attacks, it said.


If a phishing attack has compromised an account(s), it means that the attacker “may already be able to reach vCenter Server from inside a corporate firewall, and time is of the essence,” VMware stressed.


This patch is considered an “emergency change” for organizations that practice change management using the [ITIL definitions](https://wiki.en.it-processmaps.com/index.php/Change_Management) of change types, the company said. An emergency change is one that must be introduced ASAP: for example, to resolve a major incident or implement a security patch.


Granted, the decision on how to proceed is up to individual organizations, all of which have different environments, tolerance for risk, security controls and risk mitigation strategies. “The decision on how to proceed is up to you,” VMware said, but still, given the severity, the company strongly recommends that users act.


The Other 18 Flaws Are Still Attacker Candy
-------------------------------------------


The other security issues addressed in Tuesday’s update have lower CVSS scores, but they’re still ripe for the plucking by any attacker that’s already compromised organizations’ networks. That’s one of the “biggest problems facing IT today,” Plankers wrote: the fact that cyberattackers can persist on a compromised network, “patiently and quietly” biding their time to eventually move laterally as they use compromised accounts to break into other systems over long periods of time.


“They steal confidential data, intellectual property, and at the end install ransomware and extort payments from their victims,” Plankers explained. “Less urgent security vulnerabilities can still be potential tools in the hands of attackers, so VMware always recommends patching to remove them.”


How to CYA (Cover Your Assets)?
-------------------------------


If possible, the quickest way to resolve these serious issues is to patch vCenter Server. If that’s not possible, VMware has workarounds, but only for the critical vulnerability, CVE-2021-22005. The workaround is listed in the [response matrix](https://www.vmware.com/security/advisories/VMSA-2021-0020.html) at the bottom of VMware’s VMware Security Advisory (VMSA), VMSA-2021-0020.


The workaround involves editing a text file on the VCSA and restarting services.


Still, if possible, patching should be the first choice for a few reasons, Plankers advised:



> First, if you can patch vCenter Server, do it. In general, this is the fastest way to resolve this problem, doesn’t involve editing files on the vCenter Server Appliance (VCSA), and removes the vulnerabilities completely. Patching also carries less technical debt and less risk than using a workaround. —Bob Plankers
> 
> 


Other security controls that can help to protect users’ networks until they can patch include using network perimeter access controls or the vCenter Server Appliance firewall to curtail access to the vCenter Server management interfaces. “We always strongly suggest limiting access to vCenter Server, ESXi, and vSphere management interfaces to only vSphere Admins,” Plankers said. “Drive all other workload management activity through the VM network connections. This simplifies access control and makes the RDP or ssh management traffic subject to other security controls, such as IDS/IPS and monitoring.”


More Resources
--------------


VMware offered this list of resources:


Can’t Patch What You Don’t Know Is There
----------------------------------------


Greg Fitzgerald, co-founder of the cybersecurity firm Sevco Security, noted that vulnerabilities such as this one point to the need to go far beyond patching this vCenter bug. “It’s critical for enterprises to take the first step of patching this vCenter vulnerability, but it can’t stop there,” he told Threatpost on Wednesday.


Beyond patching the initial vulnerability ASAP, enterprises would be well-advised to know what IT assets they have. Even the most fastidious approach to patch management “cannot ensure that all enterprise assets are accounted for,” he said via email. “You can’t patch something if you don’t know it’s there, and attackers have figured out that the easiest path to accessing your network and your data is often through unknown or abandoned IT assets.”


**Rule #1 of Linux Security:** No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.




#### Tags:
[[vCenter]] [[VMware]] [[Plankers]] [[Linux]] [[said.]] [[that’s]] [[ransomware]] [[vSphere]] [[vulnerability,]] [[possible,]] [[ThreatPost]]
