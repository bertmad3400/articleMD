# Microsoft Defender for Endpoint fails to start on Windows Server
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-for-endpoint-fails-to-start-on-windows-server/)
+ Date: November 25, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft Defender for Endpoint fails to start on Windows Server](https://www.bleepstatic.com/content/hl-images/2021/11/25/Microsoft_Defender.jpg)


Microsoft has confirmed a new issue impacting Windows Server devices preventing the Microsoft Defender for Endpoint security solution from launching on some systems.


The enterprise endpoint security platform (previously known as Microsoft Defender Advanced Threat Protection or Defender ATP) might fail to start or run on devices with a Windows Server Core installation.


The known issue only impacts devices where customers have installed [KB5007206](https://support.microsoft.com/help/5007206) or later updates on Windows Server 2019 and [KB5007205](https://support.microsoft.com/help/5007205) or later updates on Windows Server 2022.


"After installing  [KB5007205](https://support.microsoft.com/help/5007205) or later updates, Microsoft Defender for Endpoint might fail to start or run on devices with a Windows Server Core installation," Microsoft [explained](https://docs.microsoft.com/en-us/windows/release-health/status-windows-server-2022#2764msgdesc) on the Windows Server 2022 health dashboard.


As the company further revealed, this newly confirmed issue does not affect Microsoft Defender for Endpoint running on Windows 10 devices.


Redmond is currently working on a solution to address this bug and will provide the fix in an upcoming update.


BleepingComputer is also aware of [reports](https://twitter.com/SecGuru_OTX/status/1463437470972919812) that Windows Defender turns off Realtime Protection and crashes with EventID 3002 notifications after installing [security intelligence updates](https://www.microsoft.com/en-us/wdsi/defenderupdates) between versions 1.353.1477.0 and 1.353.1486.0.


Microsoft seems to have fixed the Windows Defender bug with version 1.353.1502.0 but, according to Dutch security expert [SecGuru\_OTX](https://twitter.com/SecGuru_OTX), your device might require a hard reboot to re-enable features such as behavior monitoring.


Other issues stemming from November's Windows updates
-----------------------------------------------------


This month's KB5007206 and KB5007205 cumulative updates have also generated other problems for Windows users, including a [Windows Installer bug that would break apps](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-installer-breaks-apps-after-updates-repairs/) after repairing or updating them and [errors trying to connect to remote printers](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-kb5006674-kb5006670-updates-break-printing/) shared on Windows print servers.


Microsoft claims to have fixed the Installer and network printing issues with the [optional KB5007253 Preview cumulative update](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5007253-update-released-with-network-printing-fixes/) on Wednesday.


You can install this update by going into **Settings**, clicking on **Windows Update,** and manually performing a **'Check for Updates**.'


Since it is an optional update, you will be asked to install it by clicking on the 'Download and install' link.


You can also download and install the KB5007253 preview update manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5007253).




#### Tags:
[[Windows]] [[Microsoft]] [[KB5007205]] [[Bleeping Computer]]
