# Windows 10 KB5004237 & KB5004245 cumulative updates released
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5004237-and-kb5004245-cumulative-updates-released/)
+ Date: July 13, 2021
+ Author: Mayank Parmar


## Article:
![Windows Update](https://www.bleepstatic.com/content/hl-images/2021/01/25/Windows-10.jpg)


As part of the July 2021 Patch Tuesday, Microsoft has released new KB5004237 and KB5004245 cumulative updates for recent versions of Windows. Today's cumulative updates include security fixes for PCs with May 2021 Update, October 2020 Update, and May 2020 Update. 


This month's KB5004237 and KB5004245 cumulative updates are part of the mandatory Patch Tuesday updates containing numerous bug fixes and performance enhancements. Also included are security updates for [117 vulnerabilities in the OS](https://www.bleepingcomputer.com/news/microsoft/microsoft-july-2021-patch-tuesday-fixes-9-zero-days-117-flaws/), browsers, core components, and other basic functions.



The full list of today's cumulative updates is below:


* Windows 10 version 1507 — [KB5004249 (OS Build 10240.19003)](https://support.microsoft.com/en-us/topic/july-13-2021-kb5004249-os-build-10240-19003-bcd2edd4-76bb-4e33-8d30-e231057cb1d1)


* Windows 10 version 1607 — [KB5004238 (OS Build 14393.4530)](https://support.microsoft.com/en-us/topic/july-13-2021-kb5004238-os-build-14393-4530-69c72ccc-299a-412a-b219-b78c2fd37021)


* Windows 10 version 1703 — [EOS](https://support.microsoft.com/en-us/topic/windows-10-update-history-83aa43c0-82e0-92d8-1580-10642c9ed612)


* Windows 10 version 1709 — [EOS](https://docs.microsoft.com/en-us/lifecycle/announcements/windows-10-1709-end-of-servicing)


* Windows 10 version 1803 — [EOS](https://docs.microsoft.com/en-us/lifecycle/announcements/windows-10-1803-1809-end-of-servicing)


* Windows 10 version 1809 — [KB5004244 (OS Build 17763.2061)](https://support.microsoft.com/en-us/topic/july-13-2021-kb5004244-os-build-17763-2061-d2b763cb-fad4-4b0a-a67f-4e184e277b99)


* Windows 10 version 1903 — [EOS](https://docs.microsoft.com/en-us/lifecycle/announcements/windows-10-1903-end-of-servicing)


* Windows 10 version 1909 — [KB5004245 (OS Build 18363.1679)](https://support.microsoft.com/en-us/topic/july-13-2021-kb5004245-os-build-18363-1679-fe157ce5-49c1-4146-b948-c5aef1f0293b)


* Windows 10 version 2004, 20H2 and 21H1 — [KB5004237 (OS Builds 19041.1110, 19042.1110, and 19043.1110)](https://support.microsoft.com/en-us/topic/july-13-2021-kb5004237-os-builds-19041-1110-19042-1110-and-19043-1110-ae798d3c-3de3-4c1f-b9d9-7391b71da889)




Windows users must install these updates as soon as possible as they contain fixes for nine zero-day vulnerabilities, with four actively exploited by threat actors.


Like every Windows Update, you can open **Settings**, click on **Windows Update,** and select **'Check for Updates**' to install the updates.



![Installing KB5004237 cumulative update via Windows Update](https://www.bleepstatic.com/images/news/Microsoft/KB5004237.jpg)**Installing KB5004237 cumulative update via Windows Update**
If you own multiple PCs or if you would like to patch the PCs manually, you can learn more about it [here](https://www.bleepingcomputer.com/news/microsoft/how-to-manually-install-windows-10-cumulative-updates/).


What's new in Builds 19043.1110, 19042.1110 and 19041.1110
----------------------------------------------------------


After installing the KB5004237 update, Windows 10 2004 will be updated to build 19041.1110, Windows 10 20H2 will be updated to build 19042.1110, and Windows 10 21H1 will be updated to build 19043.1110.


KB5004237 comes with the following bug fixes:


* Addresses a remote code execution exploit in the Windows Print Spooler service, known as “PrintNightmare”, as documented in [CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527). After installing this and later Windows updates, users who are not administrators can only install signed print drivers to a print server. By default, administrators can install signed and unsigned printer drivers to a print server. The installed root certificates in the system’s Trusted Root Certification Authorities trusts signed drivers. Microsoft recommends that you immediately install this update on all supported Windows client and server operating system, starting with devices that currently host the print server role. You also have the option to configure the **RestrictDriverInstallationToAdministrators** registry setting to prevent non-administrators from installing signed printer drivers on a print server. For more information, see [KB5005010](https://support.microsoft.com/en-us/topic/kb5005010-restricting-installation-of-new-printer-drivers-after-applying-the-july-6-2021-updates-31b91c02-05bc-4ada-a7ea-183b129578a7).


* Addresses an issue that might make printing to certain printers difficult. This issue affects various brands and models, but primarily receipt or label printers that connect using a USB port.


* Removes support for the PerformTicketSignature setting and permanently enables Enforcement mode for CVE-2020-17049. For more information and steps to enable full protection on domain controller servers, see [Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/topic/kb4598347-managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049-569d60b7-3267-e2b0-7d9b-e46d770332ab).


* Adds Advanced Encryption Standard (AES) encryption protections for [CVE-2021-33757](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-33757). For more information, see [KB5004605](https://support.microsoft.com/en-us/topic/kb5004605-update-adds-aes-encryption-protections-to-the-ms-samr-protocol-for-cve-2021-33757-e4daa133-54aa-4a5d-a921-04bb50868fc2).


* Addresses a vulnerability in which Primary Refresh Tokens are not strongly encrypted. This issue might allow the tokens to be reused until the token expires or is renewed. For more information about this issue, see [CVE-2021-33779](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-33779).


* Security updates to Windows Apps, Windows Management, Windows Fundamentals, Windows Authentication, Windows User Account Control (UAC), Operating System Security, Windows Virtualization, Windows Linux, the Windows Kernel, the Microsoft Scripting Engine, the Windows HTML Platforms, the Windows MSHTML Platform, and Windows Graphics.


* Updates an issue in a small subset of users that have lower than expected performance in games after installing [KB5000842](https://support.microsoft.com/en-us/topic/march-29-2021-kb5000842-os-builds-19041-906-and-19042-906-preview-1a58a276-6a0a-47a5-aa7d-97af2d10b16d) or later.  


* Updates an issue that causes the Japanese Input Method Editor (IME) to suddenly stop working while you are typing. 


* Updates an issue in which signing in using a PIN fails. The error message is "Something happened and your PIN isn’t available. Click to set up your PIN again."


* Updates an issue that, in certain cases, takes you out of the exclusive virtual reality (VR) app and back to Windows Mixed Reality Home when you press the Windows button on the controller.


* Updates an issue that causes blurry text on the news and interests button on the Windows taskbar for some screen resolutions.


* Updates an issue with Search box graphics on the Windows taskbar that occurs if you right-click the taskbar and turn off News and interests. This graphics issue is especially visible when using dark mode.


* Updates an issue that might prevent you from using your fingerprint to sign in after startup or waking up your device from sleep.


* Updates an issue that might cause a high-pitched noise or squeak in certain apps when you play 5.1 Dolby Digital audio using certain audio devices and Windows settings.




You can find a complete list of improves and fixes and detailed explanations of the known issues in the [KB5004237 support bulletin](https://support.microsoft.com/help/5004237).


Windows 10 version 1909 is getting [KB5004245](https://support.microsoft.com/help/5004245), and it includes the same set of bug fixes highlighted abov


News and Interests feed
-----------------------


This update also includes additional fixes for the News and Interests feature, such as blurry text on the button and [taskbar glitches](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5003214-update-causes-taskbar-display-glitches/) when you enable the feature.


The "News and Interests" is a Windows 10 taskbar news feed based on Microsoft News (MSN), and it will give news stories, sports scores, finance, and weather information. However, a bug resulted in blurry icons. 


Microsoft has fixed this bug with today's updates.




#### Tags:
[[Windows]] [[KB5004237]] [[1110]] [[Microsoft]] [[taskbar]] [[KB5004245]] [[PCs]] [[Bleeping Computer]]
