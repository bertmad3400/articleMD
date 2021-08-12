# Microsoft confirms another Windows print spooler zero-day bug
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-another-windows-print-spooler-zero-day-bug/)
+ Date: August 11, 2021
+ Author: Lawrence Abrams


## Article:
![Microsoft Windows vulnerability](https://www.bleepstatic.com/content/hl-images/2021/05/17/0_Windows-headpic.jpg)


Microsoft has issued an advisory for another zero-day Windows print spooler vulnerability tracked as CVE-2021-36958 that allows local attackers to gain SYSTEM privileges on a computer.


This vulnerability is part of a class of bugs known as '[PrintNightmare](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/),' which abuses configuration settings for the Windows print spooler, print drivers, and the Windows Point and Print feature.



Microsoft released security updates in both [July](https://www.bleepingcomputer.com/news/security/microsoft-pushes-emergency-update-for-windows-printnightmare-zero-day/) and [August](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-print-spooler-printnightmare-vulnerability/) to fix various PrintNightmare vulnerabilities.


However, a vulnerability disclosed by security researcher [Benjamin Delpy](https://twitter.com/gentilkiwi) still allows threat actors to [quickly gain SYSTEM privileges](https://www.bleepingcomputer.com/news/microsoft/remote-print-server-gives-anyone-windows-admin-privileges-on-a-pc/) simply by connecting to a remote print server, as demonstrated below.



This vulnerability uses the CopyFile registry directive to copy a DLL file that opens a command prompt to the client along with a print driver when you connect to a printer.


While Microsoft's [recent security updates](https://support.microsoft.com/en-gb/topic/kb5005652-manage-new-point-and-print-default-driver-installation-behavior-cve-2021-34481-873642bf-2634-49c5-a23b-6d8e9a302872) changed the new printer driver installation procedure so that it requires admin privileges, you will not be required to enter admin privileges to connect to a printer when that driver is already installed.


Furthermore, if the driver exists on a client, and thus does not need to be installed, connecting to a remote printer will still execute the CopyFile directive for non-admin users. This weakness allows Delpy's DLL to be copied to the client and executed to open a SYSTEM-level command prompt.


Microsoft releases advisory on CVE-2021-36958
---------------------------------------------


Today, Microsoft [issued an advisory](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36958) on a new Windows Print Spooler vulnerability tracked as CVE-2021-36958.


"A remote code execution vulnerability exists when the Windows Print Spooler service improperly performs privileged file operations," reads the [CVE-2021-36958 advisory](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36958).


"An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights."


"The workaround for this vulnerability is stopping and disabling the Print Spooler service."


[Will Dormann](https://twitter.com/wdormann), a vulnerability analyst for CERT/CC, told BleepingComputer that Microsoft confirmed the CVE-2021-36958 corresponds to the PoC exploit [shared by Delpy on Twitter](https://twitter.com/gentilkiwi/status/1416429860566847490) and described above.


In the advisory, Microsoft attributes the bug to [Victor Mata](https://twitter.com/offenseindepth) of FusionX, Accenture Security, who also discovered the bug in December 2020.




> 
> Hey guys, I reported the vulnerability in Dec'20 but haven't disclosed details at MSRC's request. It looks like they acknowledged it today due to the recent events with print spooler.
> 
> 
> — Victor Mata (@offenseindepth) [August 11, 2021](https://twitter.com/offenseindepth/status/1425574625384206339?ref_src=twsrc%5Etfw)


Strangely, Microsoft has classified this as a remote code execution vulnerability, even though the attack needs to be performed locally on a computer.


When BleepingComputer asked Dormann to clarify if this was incorrect labeling, we were told "it's clearly local (LPE)" based on the CVSS:3.0 7.3 / 6.8 score.


"They just recycled "A remote code execution vulnerability exists when the Windows Print Spooler service improperly performs privileged file operations" : [https://google.com/search?q=%22A+](https://t.co/IRpM5bjAYn?amp=1)." Dormann told BleepingComputer.


Microsoft will likely update their advisory over the next few days to change its 'impact' rating to 'Elevation of Privilege.'


Mitigating the CVE-2021-36958 vulnerability
-------------------------------------------


Microsoft has not yet released a security update for this flaw, but states you can remove the attack vector by disabling the Print Spooler.


As disabling the Print Spooler will prevent your device from printing, a better method is only to allow your device to install printers from authorized servers.


This restriction can be done using the 'Package Point and print - Approved servers' group policy, preventing non-administrative users from installing print drivers using Point and Print unless the print server is on the approved list. 



![Package Point and print - Approved servers group policy](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/p/print-spooler-queue-specific/approved-servers-policyt.jpg)**Package Point and print - Approved servers group policy**
To enable this policy, launch the Group Policy Editor (gpedit.msc) and navigate to **User Configuration** > **Administrative Templates** > **Control Panel** > **Printers** > **Package Point and Print – Approved Servers**.


When toggling on the policy, enter the list of servers that you wish to allow to use as a print server, and then press **OK**to enable the policy. If you do not have a print server on your network, you can enter a fake server name to enable the feature.


Using this group policy will provide the best protection against CVE-2021-36958 exploits but will not prevent threat actors from taking over an authorized print server with malicious drivers.




#### Tags:
[[Microsoft]] [[Windows]] [[CVE-2021-36958]] [[Delpy]] [[policy,]] [[Bleeping Computer]]
