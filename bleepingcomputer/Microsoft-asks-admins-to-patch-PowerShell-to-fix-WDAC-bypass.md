# Microsoft asks admins to patch PowerShell to fix WDAC bypass
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-asks-admins-to-patch-powershell-to-fix-wdac-bypass/)
+ Date: October 18, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft asks admins to patch PowerShell to fix WDAC bypass](https://www.bleepstatic.com/content/hl-images/2021/06/16/PowerShell.jpg)


Microsoft has asked system administrators to patch PowerShell 7 against two vulnerabilities allowing attackers to bypass Windows Defender Application Control (WDAC) enforcements and gain access to plain text credentials.


[PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1) is a cross-platform solution that provides a command-line shell, a framework, and a scripting language focused on automation for processing PowerShell cmdlets.


Redmond released PowerShell 7.0.8 and PowerShell 7.1.5 to address these security flaws in the PowerShell 7 and PowerShell 7.1 branches in September and October.


Leaked passwords and WDAC bypass
--------------------------------


WDAC is designed to protect Windows devices against potentially malicious software by ensuring that only trusted apps and drivers can run, thus blocking malware and unwanted software from launching.


When the software-based WDAC security layer is enabled in Windows, PowerShell automatically goes into [constrained language mode](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/), restricting access to only a limited set of Windows APIs.


By exploiting the Windows Defender Application Control security feature bypass vulnerability tracked as [CVE-2020-0951](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-0951), threat actors can circumvent WDAC's allowlist, which allows them to execute PowerShell commands that would otherwise be blocked when WDAC is enabled.


"To exploit the vulnerability, an attacker need administrator access on a local machine where PowerShell is running. The attacker could then connect to a PowerShell session and send commands to execute arbitrary code," Microsoft [explains](https://github.com/PowerShell/Announcements/issues/27).


The second flaw, tracked as [CVE-2021-41355](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41355), is an information disclosure vulnerability in .NET Core where credentials could be leaked in clear text on devices running non-Windows platforms.


"An Information Disclosure vulnerability exists in .NET where System.DirectoryServices.Protocols.LdapConnection may send credentials in plain text on non-Windows Operating systems," Microsoft [said](https://github.com/PowerShell/Announcements/issues/26).


How to tell if you are affected
-------------------------------


The CVE-2020-0951 vulnerability affects both PowerShell 7 and PowerShell 7.1 versions, while CVE-2021-41355 only impacts users of PowerShell 7.1.


To check the PowerShell version you are running and determine if you are vulnerable to attacks exploiting these two bugs, you can execute the `pwsh -v` command from a Command Prompt.


Microsoft says no mitigation measures are currently available to block the exploitation of these security flaws.


Admins are advised to install the updated PowerShell [7.0.8](https://github.com/PowerShell/PowerShell/releases/tag/v7.0.8) and [7.1.5](https://github.com/PowerShell/PowerShell/releases/tag/v7.1.5) versions as soon as possible to protect systems from potential attacks.


"System administrators are advised to update PowerShell 7 to an unaffected version," Microsoft added. Details on what PowerShell versions are affected and the fixed versions can be found [here](https://github.com/PowerShell/Announcements/issues/27) and [here](https://github.com/PowerShell/Announcements/issues/26).


In July, Microsoft [warned](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-critical-powershell-7-code-execution-vulnerability/) of another high severity .NET Core remote code execution vulnerability in PowerShell 7.


Microsoft recently announced that it would be making it [easier to update PowerShell](https://www.bleepingcomputer.com/news/microsoft/microsoft-will-release-future-powershell-updates-via-windows-update/) for Windows 10 and Windows Server customers by releasing future updates via the Microsoft Update service.




#### Tags:
[[PowerShell]] [[Microsoft]] [[Windows]] [[WDAC]] [[.NET]] [[Bleeping Computer]]
