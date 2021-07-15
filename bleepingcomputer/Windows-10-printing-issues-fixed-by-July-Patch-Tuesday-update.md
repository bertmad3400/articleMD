# Windows 10 printing issues fixed by July Patch Tuesday update
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-10-printing-issues-fixed-by-july-patch-tuesday-update/)
+ Date: July 15, 2021
+ Author: Sergiu Gatlan


## Article:
![Windows 10 printing issues fixed by July Patch Tuesday update](https://www.bleepstatic.com/content/hl-images/2021/02/04/Windows-_-10.jpg)


Microsoft has addressed the Windows 10 printing issues caused by changes introduced in the June 2021 cumulative update preview with an update issued during this month's Patch Tuesday.


After releasing the [KB5004760 and KB5004945 security updates](https://www.bleepingcomputer.com/news/security/microsoft-printnightmare-now-patched-on-all-windows-versions/) on July 7 to fix the actively exploited [PrintNightmare vulnerability](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/), Microsoft acknowledged user reports saying they could no longer use their USB Zebra and Dymo label and receipt printers.



While users pinned the issues on the PrintNightmare patch, Microsoft announced that the problems are "not related to [CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) or [CVE-2021-1675](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1675)," and were the result of June 2021 cumulative update preview changes.


To resolve the printing issues, Microsoft released an emergency fix for Windows 10 2004, Windows 10 20H2, and Windows 10 21H1 on July 9, rolling it out via the [Known Issue Rollback (KIR) feature](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-10-known-issue-rollback-auto-fixes-update-bugs/).


Redmond also added that "for enterprise-managed devices that have installed an affected update and encountered this issue, it can be resolved by installing and configuring a special [Group Policy](https://download.microsoft.com/download/c/2/9/c2903486-685d-4924-ae49-a1e57901bb41/Windows%2010%20(2004%20&%2020H2)%20Known%20Issue%20Rollback%20070821%2001.msi)."


Separate update pushed to fix printing problems
-----------------------------------------------


To provide a fix for customers who do not want or can't use KIR to resolve these printing problems, Microsoft also released the KB5004237 update as part of the [July 2021 Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-july-2021-patch-tuesday-fixes-9-zero-days-117-flaws/).


"This issue was resolved in  [KB5004237](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5004237-and-kb5004245-cumulative-updates-released/), released July 13, 2021. If you are using an update released before July 13, 2021, you can resolve this issue using Known Issue Rollback (KIR)," Microsoft [said](https://docs.microsoft.com/en-us/windows/release-health/status-windows-10-20h2#1647msgdesc) in a new update to the Windows release health dashboard


"This issue affects various brands and models, but primarily receipt or label printers that connect using a USB port. After installing this update, you do not need to use a Known Issue Rollback (KIR) or a special Group Policy to resolve this issue."


Customers also [encountered printing issues](https://www.bleepingcomputer.com/news/microsoft/windows-10-crashes-when-printing-due-to-microsoft-march-updates/) in March after installing the March 2021 Patch Tuesday updates. Users reported that Windows 10 would [crash when printing](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-10-crash-issue-due-to-march-updates/) or [print jobs would be missing graphics elements](https://www.bleepingcomputer.com/news/microsoft/microsoft-warns-of-more-printing-issues-caused-by-march-updates/), blank pages, or other issues.


To resolve these issues, Microsoft released two out-of-band emergency updates for Windows 10 one week later: [KB5001567](https://www.bleepingcomputer.com/news/microsoft/windows-10-emergency-updates-released-to-fix-printing-crashes/) on March 15 to fix the crashes and [KB5001649](https://www.bleepingcomputer.com/news/microsoft/new-windows-10-emergency-updates-fix-remaining-printing-issues/) on March 18 to fix the printing issues.




#### Tags:
[[Microsoft]] [[Windows]] [[KIR]] [[Bleeping Computer]]
