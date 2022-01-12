# New Windows Server updates cause DC boot loops, break Hyper-V
### The latest Windows Server updates are causing severe issues for administrators, with domain controllers having spontaneous reboots, Hyper-V not starting, and inaccessible ReFS volumes until the updates are rolled back

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/new-windows-server-updates-cause-dc-boot-loops-break-hyper-v/
+ Date: 2022-01-12T14:53:07-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/12/windows-server.jpg)

![Windows Server](https://www.bleepstatic.com/content/hl-images/2022/01/12/windows-server.jpg)


The latest Windows Server updates are causing severe issues for administrators, with domain controllers having spontaneous reboots, Hyper-V not starting, and inaccessible ReFS volumes until the updates are rolled back


Yesterday, Microsoft released the Windows Server 2012 R2 KB5009624 update, the Windows Server 2019 KB5009557 update, and the Windows Server 2022 KB5009555 update as part of the [January 2022 Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-january-2022-patch-tuesday-fixes-6-zero-days-97-flaws/).


After installing these updates, administrators have been battling multiple issues that are only resolved after removing the updates.


Windows domain controller boot loops
------------------------------------


The most serious issue introduced by these updates is that Windows domain controllers enter a boot loop, with servers getting into an endless cycle of Windows starting and then rebooting after a few minutes.


As first reported by [BornCity](https://borncity.com/win/2022/01/12/windows-server-januar-2022-sicherheitsupdates-verursachen-boot-schleife/), this issue affects all supported Windows Server versions.


"Looks KB5009557 (2019) and KB5009555 (2022) are causing something to fail on domain controllers, which then keep rebooting every few minutes," a [user posted](https://www.reddit.com/r/sysadmin/comments/s21ae1/january_updates_causing_unexpected_reboots_on/) to Reddit.


A Windows Server administrator told BleepingComputer that they see the LSASS.exe process use all of the CPU on a server and then ultimately terminate.


As LSASS is a critical process required for Windows to operate correctly, the operating system will automatically restart when the process is terminated.


The following error will be logged to the event viewer when restarting due to a crashed LSASS process, as another user [on Reddit](http://Other%20users%20are%20reporting%20that%20reboots%20are%20caused%20by%20the%20LSASS.exe%20process) shared.



> 
> "The process wininit.exe has initiated the restart of computer [computer\_name] on behalf of user for the following reason: No title for this reason could be found Reason Code: 0x50006 Shutdown Type: restart Comment: The system process 'C:\WINDOWS\system32\lsass.exe' terminated unexpectedly with status code -1073741819. The system will now shut down and restart."
> 
> 
> 


Hyper-V no longer starts
------------------------


In addition to the boot loops, BleepingComputer has been told by Windows administrators that after installing the patches, Hyper-V no longer starts on the server.


This bug primarily affects Windows Server 2012 R2 server, but other unverified reports say it affects newer versions of Windows Server.


As Hyper-V is not started, when attempting to launch a virtual machine, users will [receive an error](https://www.reddit.com/r/sysadmin/comments/s24o7k/kb5009624_breaks_hyperv/) stating the following:



> 
> "Virtual machine xxx could not be started because the hypervisor is not running."
> 
> 
> 


Microsoft released security updates to fix four different Hyper-V vulnerabilities yesterday (CVE-2022-21901, CVE-2022-21900, CVE-2022-21905, and CVE-2022-21847), which are likely causing this issue.


ReFS file systems are no longer accessible
------------------------------------------


Finally, numerous admins are reporting that Windows Resilient File System (ReFS) volumes are no longer accessible or are seen as RAW (unformatted) after installing the updates.


The Resilient File System (ReFS) is a Microsoft proprietary file system that has been designed for high availability, data recovery, and high performance for very large storage volumes.


"Installed [these](https://i.imgur.com/xoqUiEB.png) updates tonight, in a two server Exchange 2016 CU22 DAG, running on Server 2012 R2. After a really long reboot, the server came back up with all the ReFS volumes as RAW," [explained](https://www.reddit.com/r/exchangeserver/comments/s1y5pw/january_updates_refs_became_raw_for_database/) a Microsoft Exchange administrator on Reddit.


"NTFS volumes attached were fine. I realize this is not exclusively an exchange question but it is impacting my ability to bring services for Exchange back online."


Uninstalling the Windows Server updates made the ReFS volumes accessible again.


Yesterday, Microsoft fixed seven remote code execution vulnerabilities in ReFS, with one or more likely behind the inaccessible ReFS volumes.


These vulnerabilities are tracked as CVE-2022-21961, CVE-2022-21959, CVE-2022-21958, CVE-2022-21960, CVE-2022-21963, CVE-2022-21892, CVE-2022-21962, CVE-2022-21928.


How to fix?
-----------


Unfortunately, the only way to fix these issues is to uninstall the corresponding cumulative update for your Windows version.


Admins can do this by using one of the following commands:



```
Windows Server 2012 R2: wusa /uninstall /kb:KB5009624 
Windows Server 2019: wusa /uninstall /kb:KB5009557 
Windows Server 2022: wusa /uninstall /kb:KB5009555
```

As Microsoft bundles all security fixes into the single update, removing the cumulative update may fix the bugs, but will also remove all fixes for recently patched vulnerabilities.


Therefore, uninstalling these updates should only be done if absolutely necessary.


Not to be outdone by Windows Server, Windows 10 and Windows 11's updates are also [breaking L2TP VPN connections](https://www.bleepingcomputer.com/news/microsoft/new-windows-kb5009543-kb5009566-updates-break-l2tp-vpn-connections/).


BleepingComputer has reached out to Microsoft for fixes on these issues but has not heard back at this time.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Hyper-v]] [[R2]] [[Uninstall]] [[Reddit]] [[Bleepingcomputer]] [[Wusa]] [[Bleeping Computer]]
#### CVE's
[[CVE-2022-21901]] [[CVE-2022-21900]] [[CVE-2022-21905]] [[CVE-2022-21847]] [[CVE-2022-21961]] [[CVE-2022-21959]] [[CVE-2022-21958]] [[CVE-2022-21960]] [[CVE-2022-21963]] [[CVE-2022-21892]] [[CVE-2022-21962]] [[CVE-2022-21928]]

