# Microsoft fixes Windows 10 auth issue impacting Remote Desktop
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-10-auth-issue-impacting-remote-desktop/)
+ Date: October 18, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft fixes Windows 10 auth issue impacting Remote Desktop](https://www.bleepstatic.com/content/hl-images/2021/07/09/Windows_headpic.jpg)


Microsoft has fixed a known Windows 10 issue causing smartcard authentication to fail when trying to connect using Remote Desktop after installing the cumulative updates released during [last month's Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2021-patch-tuesday-fixes-2-zero-days-60-flaws/).


As explained by the company, devices attempting to make Remote Desktop connections to devices in untrusted domains might be unable to connect.


"After installing  [KB5005611](https://support.microsoft.com/help/5005611) or later updates, when connecting to devices in an untrusted domain using Remote Desktop, connections might fail to authenticate when using smart card authentication," Microsoft [explained](https://docs.microsoft.com/en-us/windows/release-health/status-windows-10-21h1#1729msgdesc).


"You might receive the prompt, 'Your credentials did not work. The credentials that were used to connect to [device name] did not work. Please enter new credentials.' and 'The login attempt failed' in red."


Windows platforms affected by this issue include both client (Windows 10 21H1, Windows 10 20H2, and Windows 10 2004) and server (Windows Server 2022, Windows Serve 20H2, and Windows Server 2004).


Fixed via Known Issue Rollback
------------------------------


Microsoft has already rolled out a fix to address this issue via the [Known Issue Rollback (KIR) feature](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-10-known-issue-rollback-auto-fixes-update-bugs/) to affected Windows 10 devices.


"This issue is resolved using [Known Issue Rollback (KIR)](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/known-issue-rollback-helping-you-keep-windows-devices-protected/ba-p/2176831). Please note that it might take up to 24 hours for the resolution to propagate automatically to consumer devices and non-managed business devices. Restarting your Windows device might help the resolution apply to your device faster."


On enterprise-managed devices, customers can also install and configure group policies to resolve the issue.


Microsoft has released the following group policies to address this specific issue (a restart is required after configuring the Group Policy):


* [Windows Server 2022](https://download.microsoft.com/download/1/e/3/1e36d9a4-e8de-4b35-8566-efdb6aab08fe/Windows%20Server%202022%20Known%20Issue%20Rollback%20101521%2001.msi)
* [Windows 10, version 2004, Windows 10, version 20H2 and Windows 10, version 21H1](https://download.microsoft.com/download/1/e/3/1e36d9a4-e8de-4b35-8566-efdb6aab08fe/Windows%2010%20(2004,%2020H2%20&%2021H1)%20Known%20Issue%20Rollback%20101521%2001.msi)


Redmond has been using the Known Issue Rollback feature to roll back computers impacted by problematic bug fixes to a working state [since late 2019](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-10-known-issue-rollback-auto-fixes-update-bugs/).


A fully working version of KIR was introduced in Windows 10 2004 when all components started working together as a complete system. 


While fixes issued through KIR are distributed via Windows Update, they are not delivered as actual updates. Instead, they are deployed by creating Windows Registry entries that disable changes made in previous updates.


Known Issue Rollout fixes usually propagate to all affected systems within 24 hours, and that restarting impacted computers may speed up the process.


Microsoft previously used Known Issue Rollout fixes to [performance issues while gaming](https://www.bleepingcomputer.com/news/microsoft/microsoft-pushes-emergency-fix-for-windows-10-kb5001330-gaming-issues/), [resolve printing issues](https://www.bleepingcomputer.com/news/microsoft/microsoft-pushes-emergency-fix-for-windows-10-kb5004945-printing-issues/), and [app freezes and crashes](https://www.bleepingcomputer.com/news/microsoft/windows-10-emergency-update-resolves-kb5005565-app-freezes-crashes/).




#### Tags:
[[Windows]] [[Microsoft]] [[Bleeping Computer]]
