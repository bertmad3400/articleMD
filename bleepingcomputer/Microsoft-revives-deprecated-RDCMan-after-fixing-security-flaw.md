# Microsoft revives deprecated RDCMan after fixing security flaw
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-revives-deprecated-rdcman-after-fixing-security-flaw/)
+ Date: August 10, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft revives deprecated RDCMan after fixing security flaw](https://www.bleepstatic.com/content/hl-images/2020/10/07/Microsoft.jpg)


Microsoft has revived the Remote Desktop Connection Manager (RDCMan) app that was deprecated last year due to an important severity information disclosure bug the company decided not to fix.


RDCMan is a Windows RDP (Remote Desktop Protocol) client used by system admins to manage multiple remote desktop connections.





After discontinuing the app, Microsoft [advised customers](https://docs.microsoft.com/en-US/troubleshoot/windows-client/remote/use-mstsc-universal-remote-desktop-client-instead-rdman) to switch to Windows built-in Remote Desktop Connection (%windir%\system32\mstsc.exe) or the [universal Remote Desktop client](https://aka.ms/rdwin).


"An information disclosure vulnerability exists in the Remote Desktop Connection Manager (RDCMan) application when it improperly parses XML input containing a reference to an external entity," Microsoft [explained](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-0765) in the March 2020 security advisory.


"An attacker who successfully exploited this vulnerability could read arbitrary files via an XML external entity (XXE) declaration."


Attackers could exploit the bug (tracked as CVE-2020-0765) by tricking authenticated targets into opening RDG files containing maliciously crafted XML content.


RDCMan revived as a Sysinternals tool
-------------------------------------


However, as Microsoft Azure CTO Mark Russinovich revealed earlier this year, the company added RDCMan to the Windows Sysinternals toolkit and released [version 2.8](https://twitter.com/markrussinovich/status/1407402603458088960) in late June.


"Good news for RDCMan (Remote Desktop Connection Manager) fans (like me): we've saved it from abandonment by bringing into Sysinternals," Russinovich [said in February](https://twitter.com/markrussinovich/status/1361734164421218304), confirming the tool's revival. "Look for its Sysinternals debut in the near future."



While the company didn't share any details on the security flaw addressed in RDCMan 2.8, the patched vulnerability was not the one that led to the app being discontinued last year.


Microsoft disclosed today [in an update to the initial security advisory](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-0765) that the flaw was fixed in RDCMan 2.82, released on July 27 through the [Sysinternals documentation website](https://docs.microsoft.com/en-us/sysinternals/downloads/rdcman).


The new Remote Desktop Connection Manager version runs on Windows 8.1 and higher or Windows Server 2012 and higher.


"User with OS versions prior to Win7/Vista will need to get version 6 of the Terminal Services Client," Microsoft says. "You can obtain this from the Microsoft Download Center: XP; Win2003."




#### Tags:
[[Microsoft]] [[RDCMan]] [[Windows]] [[Sysinternals]] [[XML]] [[Bleeping Computer]]
