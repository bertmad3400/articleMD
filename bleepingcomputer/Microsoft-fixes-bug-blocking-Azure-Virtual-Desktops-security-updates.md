# Microsoft fixes bug blocking Azure Virtual Desktops security updates
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-bug-blocking-azure-virtual-desktops-security-updates/)
+ Date: October 7, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft fixes bug blocking Azure Virtual Desktops security updates](https://www.bleepstatic.com/content/hl-images/2021/10/07/Azure__Virtual_Desktops_headpic.jpg)


Microsoft has fixed a bug blocking some Azure Virtual Desktop (AVD) devices from downloading and installing monthly security via Windows Server Update Services (WSUS) [since early July](https://www.bleepingcomputer.com/news/microsoft/windows-update-bug-blocks-azure-virtual-desktops-security-updates/).


"This is observed in the Settings app under the Windows Update setting, which will display the message 'You're up to date' even if no updates later than May 2021 have been installed," Microsoft [explains](http://docs.microsoft.com/en-us/windows/release-health/status-windows-10-1909#1643msgdesc).


The known issue impacted both client (Windows 10 Enterprise multi-session, version 1909) and server (Windows Server multi-session, version 1909) platforms.


Redmond says it addressed the Azure Virtual Desktop issue in the [KB5005565](https://support.microsoft.com/help/5005565) cumulative update released in mid-September for devices running Windows 10, version 2004 and later.


The company did not explain on the Windows health dashboard or the associated support document why it delayed announcing the fix or why it delivers it to systems running Windows 10 1909 via a Windows 10 2004 cumulative update.


Workarounds also available
--------------------------


Microsoft also provides two workarounds that allow customers to apply monthly security updates on Azure Virtual Desktop systems using WSUS if they can't immediately deploy the KB5005565 CU that fixes the known issue.


The first workaround requires deploying up-to-date images to all impacted devices, including all Azure Marketplace security updates.


The second approach, needed on computers where image redeployment is not an option, requires manually downloading and installing the missing security updates from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).


"Microsoft publishes monthly security updates on the second Tuesday of each month. You can download these updates from the Microsoft Update Catalog as Microsoft Update (.msu) files and deploy them using your management solution," Microsoft says.


After going through procedure needed to download the updates, you will be able to add the .msu files to your endpoint management system and start deploying the security updates to devices running Windows 10 Enterprise or Education, version 1909.


Detailed instructions on deploying images and manually installing security updates on affected devices are available in [this support document](http://support.microsoft.com/help/5004926).




#### Tags:
[[Microsoft]] [[Windows]] [[Bleeping Computer]]
