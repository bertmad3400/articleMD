# Microsoft patches Excel zero-day used in attacks, asks Mac users to wait
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-excel-zero-day-used-in-attacks-asks-mac-users-to-wait/)
+ Date: November 10, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft patches Excel zero-day used in attacks, asks Mac users to wait](https://www.bleepstatic.com/content/hl-images/2021/11/10/Excel.jpg)


During this month's [Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2021-patch-tuesday-fixes-6-zero-days-55-flaws/), Microsoft has patched an Excel zero-day vulnerability exploited in the wild by threat actors.


Zero-days, as defined by Microsoft, are publicly disclosed bugs with no official security updates.


The vulnerability, tracked as CVE-2021-42292, is a high severity security feature bypass that unauthenticated attackers can exploit locally in low complexity attacks that don't require user interaction.


Microsoft also patched a second Excel security flaw used during the Tianfu Cup hacking contest last month, a remote code execution bug tracked as [CVE-2021-40442](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-40442) and exploitable by unauthenticated attackers.


Luckily, Microsoft says that the Windows Explorer preview pane is not an attack vector for the two bugs.


This means that successful exploitation requires fully opening maliciously crafted Excel files instead of just clicking to select them.


Mac users asked to wait for a patch
-----------------------------------


While Redmond released security updates for systems running Microsoft 365 Apps for Enterprise and Windows versions of Microsoft Office and Microsoft Excel, it failed to patch the vulnerabilities on macOS.


Mac customers running macOS versions of Microsoft Office and Microsoft were told they'd have to wait a little longer for CVE-2021-42292 patches.


"The security update for Microsoft Office 2019 for Mac and Microsoft Office LTSC for Mac 2021 are not immediately available," Microsoft [said](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-42292). "The updates will be released as soon as possible, and when they are available, customers will be notified via a revision to this CVE information."


The two bugs were discovered by security researchers with the Microsoft Threat Intelligence Center.


Microsoft also [warned admins on Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-urges-exchange-admins-to-patch-bug-exploited-in-the-wild/) to immediately patch a high severity Exchange Server vulnerability tracked as [CVE-2021-42321](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-42321) and impacting on-premises servers running Exchange Server 2016 and Exchange Server 2019.


As explained in yesterday's security advisories, successful exploitation may enable authenticated attackers to execute code remotely on vulnerable servers.




#### Tags:
[[Microsoft]] [[Bleeping Computer]]
