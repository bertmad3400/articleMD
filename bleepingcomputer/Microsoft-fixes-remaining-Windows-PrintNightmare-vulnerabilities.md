# Microsoft fixes remaining Windows PrintNightmare vulnerabilities
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-remaining-windows-printnightmare-vulnerabilities/)
+ Date: September 14, 2021
+ Author: Lawrence Abrams


## Article:
![Windows printer spooler](https://www.bleepstatic.com/content/hl-images/2021/06/30/Printer.jpg)


Microsoft has released a security update to fix the last remaining PrintNightmare zero-day vulnerabilities that allowed attackers to gain administrative privileges on Windows devices quickly.


In June, a zero-day Windows print spooler vulnerability dubbed PrintNightmare (CVE-2021-34527) was [accidentally disclosed](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/). This vulnerability exploits the Windows [Point and Print](https://docs.microsoft.com/en-us/windows-hardware/drivers/print/introduction-to-point-and-print) feature to perform remote code execution and gain local SYSTEM privileges.


While Microsoft released two security updates to fix various PrintNightmare vulnerabilities, another vulnerability publicly disclosed by security researcher [Benjamin Delpy](https://twitter.com/gentilkiwi) still allowed threat actors to [quickly gain SYSTEM privileges](https://www.bleepingcomputer.com/news/microsoft/remote-print-server-gives-anyone-windows-admin-privileges-on-a-pc/) simply by connecting to a remote print server.


As demonstrated below, Delpy's vulnerability abused the [CopyFiles directive](https://docs.microsoft.com/en-us/windows-hardware/drivers/print/downloading-queue-specific-files) to copy and execute malicious DLL using SYSTEM privileges when a user installed a remote printer. Once the exploit launched the DLL, it would open a console Window where all commands are executed with SYSTEM privileges.



To make matters worse, ransomware gangs, such as [Vice Society](https://www.bleepingcomputer.com/news/security/vice-society-ransomware-joins-ongoing-printnightmare-attacks/), [Magniber](https://www.bleepingcomputer.com/news/security/ransomware-gang-uses-printnightmare-to-breach-windows-servers/), and [Conti](https://twitter.com/John_Fokker/status/1425749521569624065), began utilizing the bug to gain elevated privileges on compromised devices.


This remaining PrintNightmare vulnerability is tracked as CVE-2021-36958 and is attributed to [Victor Mata](https://twitter.com/offenseindepth) of FusionX, Accenture Security, who privately disclosed the bug to Microsoft in December 2020.


New security update fixes PrintNightmare bug
--------------------------------------------


In today's September 2021 Patch Tuesday security updates, Microsoft has released a new security update for [CVE-2021-36958](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36958) that fixes the remaining PrintNightmare vulnerability.


Delpy, who tested his exploit against the new security update, confirmed to BleepingComputer that the bug is now fixed.




> 
> [#printnightmare](https://twitter.com/hashtag/printnightmare?src=hash&ref_src=twsrc%5Etfw) patch tuesday looks like promising [pic.twitter.com/OjwCL79Io9](https://t.co/OjwCL79Io9)
> 
> 
> — Benjamin Delpy (@gentilkiwi) [September 14, 2021](https://twitter.com/gentilkiwi/status/1437850150513295369?ref_src=twsrc%5Etfw)


In addition to fixing the vulnerability, Delpy told BleepingComputer that Microsoft has disabled the CopyFiles feature by default and added an undocumented group policy that allows admins to enable it again.


This policy can be configured in the Windows Registry under **HKLM\Software\Policies\Microsoft\Windows NT\Printers** key and by adding a value named **CopyFilesPolicy**. When set to '1', CopyFiles will be enabled again.


However, even when enabled, Delpy told BleepingComputer that it would only allow Microsoft's **C:\Windows\System32\mscms.dll** file to be used with this feature.



![Checking the Windows Registry for the CopyFilesPolicy](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/p/printnightmare/fixed/copyfile-policy-check-reverse.jpg)**Checking the Windows Registry for the CopyFilesPolicy**  
*Source: Benjamin Delpy*
As this change will affect the default behavior of Windows, it is unclear what issues it will cause when printing in Windows.


Microsoft has not released any information on this new group policy at this time, and it is not available in the Group Policy Editor.


In addition to the PrintNightmare vulnerability, today's updates also fix an actively exploited [Windows MSHTML zero-day vulnerability](https://www.bleepingcomputer.com/news/security/microsoft-shares-temp-fix-for-ongoing-office-365-zero-day-attacks/).


As both of these vulnerabilities are known to be abused by the threat actors in attacks, it is critical to install today's [Patch Tuesday security updates](https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2021-patch-tuesday-fixes-2-zero-days-60-flaws/) as soon as possible.




#### Tags:
[[Microsoft]] [[PrintNightmare]] [[Windows]] [[Delpy]] [[zero-day]] [[CopyFiles]] [[BleepingComputer]] [[Bleeping Computer]]
