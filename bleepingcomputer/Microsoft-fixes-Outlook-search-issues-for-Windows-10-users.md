# Microsoft fixes Outlook search issues for Windows 10 users
### Microsoft has fixed a known issue causing search issues for Outlook users after installing Windows 10 security updates released since November 2021.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-outlook-search-issues-for-windows-10-users/
+ Date: 2022-01-20T05:08:45-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/05/11/Outlook_headpic.jpg)

![Outlook](https://www.bleepstatic.com/content/hl-images/2021/05/11/Outlook_headpic.jpg)


Microsoft has fixed a known issue causing search issues for Outlook users after installing Windows 10 security updates released since November 2021.


As the company explained, searches on the Outlook desktop app might fail and recent emails might not appear in search results if they're stored locally in PST or OST files.


"It might affect POP and IMAP accounts, as well as Microsoft Exchange and Microsoft 365 hosted accounts," Microsoft [explaine](https://docs.microsoft.com/en-us/windows/release-health/status-windows-10-21h2#2778msgdesc)d in a newly added entry on the Windows health dashboard.


"If the default search in the Outlook app is set to server search, the issue will only affect the advanced search."


Windows platforms affected by this known issue ([first acknowledged earlier this month](https://www.bleepingcomputer.com/news/microsoft/microsoft-kb5008212-windows-security-update-breaks-outlook-search/)) include both client (multiple Windows 10 releases and Windows 11) and server versions:


* Client: Windows 11, version 21H2; Windows 10, version 21H2; Windows 10, version 21H1; Windows 10, version 20H2; Windows 10, version 1809; Windows 10 Enterprise LTSC 2019
* Server: Windows Server, version 20H2; Windows Server, version 1809; Windows Server 2019

Outlook search fixed on Windows 10
----------------------------------


Microsoft has fixed this issue on affected Windows 10 devices either through [out-of-band Windows updates released on Monday](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-emergency-fixes-for-windows-server-vpn-bugs/) or via the [Known Issue Rollback (KIR) feature](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-10-known-issue-rollback-auto-fixes-update-bugs/).


Those receiving the fix via KIR might have to wait until the rollout reaches their systems until it propagates to all affected systems.


"Please note that it might take up to 24 hours for the resolution to propagate automatically to consumer devices and non-managed business devices. Restarting your Windows device might help the resolution apply to your device faster," Microsoft said.


Windows admins can also install and configure group policies to resolve the issue on enterprise-managed devices.


Microsoft has released the following group policies for enterprise environments (a restart is required after configuring the Group Policy):


* [Windows 10, version 20H2, Windows 10, version 21H1 and Windows 10, version 21H2](https://download.microsoft.com/download/4/a/d/4adcd2e9-413d-4d49-9f0e-c69629dfd292/Windows%2010%20%282004%2c%2020H2%20&%2021H1%29%20Known%20Issue%20Rollback%20011422%2001.msi)
* [Windows 10, version 1809, Windows 10 Enterprise LTSC 2019, and Windows Server 2019](https://download.microsoft.com/download/4/a/d/4adcd2e9-413d-4d49-9f0e-c69629dfd292/Known%20Issue%20Rollback%20011422%2001.msi)

Workaround for Windows 11 users
-------------------------------


While a fix for the Outlook search issue is already rolling out to all impacted Windows 10 devices, Microsoft says it's still "working on a resolution and will provide an update in an upcoming release" for affected Windows 11 systems. 


As a temporary workaround, Microsoft advises Windows 11 customers and those who haven't yet received the fix via KIR to mitigate the Outlook search bug by disabling Windows Desktop Search and switching to Outlook's built-in search engine.


"To mitigate the issue, you can disable Windows Desktop Search which will cause Outlook to use its built-in search. For instructions, see [Outlook Search not showing recent emails after Windows update KB5008212](https://support.microsoft.com/office/outlook-search-not-showing-recent-emails-after-windows-update-kb5008212-cc5345cf-8007-403a-bb23-f3818653c2df)," Microsoft said.


As previously [reported in December](https://www.bleepingcomputer.com/news/microsoft/microsoft-shares-fix-for-broken-outlook-search-in-windows-11/), Outlook users have also experienced search issues in Outlook for Microsoft 365, Outlook 2019, and Outlook 2016 after upgrading to Windows 11.


Those problems started showing up in June 2021 after the first Windows 11 preview builds surfaced, and they also impacted emails and other items stored locally in PST or OST files, such as POP and IMAP accounts.


As mitigation, Microsoft also recommended switching to Outlook's built-in search engine, which would workaround the cause: Windows search being broken after the search index gets deleted during the Windows 11 upgrade.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Emails]] [[Built-in]] [[Bleeping Computer]]

