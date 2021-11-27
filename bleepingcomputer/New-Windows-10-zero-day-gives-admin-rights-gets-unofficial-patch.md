# New Windows 10 zero-day gives admin rights, gets unofficial patch
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-windows-10-zero-day-gives-admin-rights-gets-unofficial-patch/)
+ Date: November 27, 2021
+ Author: Sergiu Gatlan


## Article:
![New Windows 10 MDM privesc zero-day gets a free micropatch](https://www.bleepstatic.com/content/hl-images/2021/07/23/Windows-attack.jpg)


Free unofficial patches have been released to protect Windows users from a local privilege escalation (LPE) zero-day vulnerability in the Mobile Device Management Service impacting Windows 10, version 1809 and later.


The security flaw resides under the "Access work or school" settings, and it bypasses a patch released by Microsoft in February to address an information disclosure bug tracked as [CVE-2021-24084](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-24084).


However, security researcher Abdelhamid Naceri (who also reported the initial vulnerability) discovered this month that the [incompletely patched](https://twitter.com/KLINIX5/status/1460338968780804098) flaw could also be exploited to gain admin privileges after publicly [disclosing the newly spotted bug](https://halove23.blogspot.com/2021/06/CVE-2021-24084-Unpatched-ID.html) in June. 


"Namely, as [HiveNightmare/SeriousSAM](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36934) has taught us, an arbitrary file disclosure can be upgraded to local privilege escalation if you know which files to take and what to do with them," 0patch co-founder Mitja Kolsek [explained](https://blog.0patch.com/2021/11/micropatching-unpatched-local-privilege.html) today.


"We confirmed this by using the procedure described in [this blog post by Raj Chandel](https://www.hackingarticles.in/windows-privilege-escalation-hivenightmare/) in conjunction with Abdelhamid's bug - and being able to run code as local administrator."


While Microsoft has most likely also noticed Naceri's June disclosure, the company is yet to patch this LPE bug, exposing Windows 10 systems with the latest November 2021 security updates to attacks.


Luckily, attackers can only exploit the vulnerability if two very specific conditions are met:


* System protection must be enabled on drive C, and at least one restore point created. Whether system protection is enabled or disabled by default [depends on various parameters](https://docs.microsoft.com/en-US/troubleshoot/windows-client/deployment/system-restore-points-disabled).
* At least one local administrator account must be enabled on the computer, or at least one "Administrators" group member's credentials cached.


Unnoficial patches for all impacted Windows 10 systems
------------------------------------------------------


Until Microsoft releases security updates to address this security issue (likely during next month's Patch Tuesday), the [0patch micropatching service](https://0patch.com/) has released free and unofficial patches for all affected Windows 10 versions (Windows 10 21H2 is also impacted but is not yet supported by 0patch):


1. **Windows 10 v21H1 (32 & 64 bit)** updated with November 2021 Updates
2. **Windows 10 v20H2 (32 & 64 bit)**updated with November 2021 Updates
3. **Windows 10 v2004 (32 & 64 bit)**updated with November 2021 Updates
4. **Windows 10 v1909 (32 & 64 bit)**updated with November 2021 Updates
5. **Windows 10 v1903 (32 & 64 bit)**updated with November 2021 Updates
6. **Windows 10 v1809 (32 & 64 bit)**updated with May 2021 Updates


"Windows Servers are not affected, as the vulnerable functionality does not exist there. While some similar diagnostics tools exist on servers, they are being executed under the launching user's identity, and therefore cannot be exploited," Kolsek added.


"Windows 10 v1803 and older Windows 10 versions don't seem to be affected either. While they do have the 'Access work or school' functionality, it behaves differently and cannot be exploited this way. Windows 7 does not have the 'Access work or school' functionality at all."




> 
> We'd like to thank Abdelhamid Naceri ([@KLINIX5](https://twitter.com/KLINIX5?ref_src=twsrc%5Etfw)) for finding this issue and sharing details, which allowed us to create a micropatch and protect our users.
> 
> 
> — 0patch (@0patch) [November 26, 2021](https://twitter.com/0patch/status/1464297203552378880?ref_src=twsrc%5Etfw)


How to install the micropatch
-----------------------------


To install the unofficial patch on your system, you will need to [register a 0patch account](https://central.0patch.com/) and install the [0patch agent](https://0patch.com/).


Once you launch the agent on your device, the patch will be applied automatically (if there are no custom patching enterprise policies enabled to block it) without requiring a restart.


This is the second Windows zero-day that received a micropatch this month after Naceri found that patches for another bug ([CVE-2021-34484](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34484)) in the Windows User Profile Service [could be bypassed to escalate privileges on all Windows versions](https://www.bleepingcomputer.com/news/microsoft/zero-day-bug-in-all-windows-versions-gets-free-unofficial-patch/), even if fully patched.


Microsoft also needs to patch [a third zero-day bug in the Microsoft Windows Installer](https://www.bleepingcomputer.com/news/microsoft/new-windows-zero-day-with-public-exploit-lets-you-become-an-admin/) with a proof-of-concept (PoC) exploit released by Naceri over the weekend.


If successfully exploited, the zero-day [allows attackers to gain SYSTEM privileges on up-to-date devices running the latest Windows versions](https://www.bleepingcomputer.com/news/microsoft/new-windows-zero-day-with-public-exploit-lets-you-become-an-admin/), including Windows 10, Windows 11, and Windows Server 2022.


Malware creators have since [started testing the PoC exploit](https://www.bleepingcomputer.com/news/security/malware-now-trying-to-exploit-new-windows-installer-zero-day/) in low volume attacks likely focused on testing and tweaking it for future full-blown campaigns.




#### Tags:
[[Windows]] [[bit)]] [[Microsoft]] [[Naceri]] [[0patch]] [[zero-day]] [[Abdelhamid]] [[micropatch]] [[Bleeping Computer]]
