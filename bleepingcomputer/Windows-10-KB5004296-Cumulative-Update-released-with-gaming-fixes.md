# Windows 10 KB5004296 Cumulative Update released with gaming fixes
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5004296-cumulative-update-released-with-gaming-fixes/)
+ Date: July 29, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 10](https://www.bleepstatic.com/content/hl-images/2021/02/04/Windows_10.jpg)


Microsoft has released the optional KB5004296 Preview cumulative update for Windows 10 2004, Windows 10 20H2, and Windows 10 21H1. This update contains fixes for gaming issues experienced by Windows 10 users since March.


This cumulative update is part of Microsoft's July 2021 monthly "C" update, allowing users to test the upcoming fixes scheduled for next month's August 2021 Patch Tuesday.


Unlike Patch Tuesday cumulative updates, this preview update only contains bug fixes, performance enhancements, and improvements to existing features and does not include any security updates.


Windows users can install this update by going into **Settings**, clicking on **Windows Update,** and selecting **'Check for Updates**.'


As this is an optional update, you will be prompted to click on the download and install button before Windows 10 will install the update, as shown below.



![Windows Update offering the optional KB5004296 update](https://www.bleepstatic.com/images/news/Microsoft/windows-updates/kb5004296.jpg)**Windows Update offering the optional KB5004296 update**
Windows 10 users can also manually download and install the KB5004296 preview update from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5004296).


Gaming fixes included
---------------------


Since March, Windows 10 users have complained about performance issues, stuttering, and low frame rates when playing games.


It was so widely reported at the time that [NVIDIA recommended](https://www.bleepingcomputer.com/news/microsoft/nvidia-staff-suggests-rolling-back-windows-10-update-to-fix-game-issues/) users should roll back to older Windows 10 updates to resolve the gaming issues.


In April, Microsoft released a Known Issue Rollback (KIR) to Windows 10 users to resolve the gaming issues, but the problems persisted for many users.


Today, as part of the KB5004296 update, Microsoft has now fixed an issue that prevented power plans and game mode from working, caused lower FPS, and reduced performance for gamers.


"Addresses an issue that prevents power plans and Game Mode from working as expected. This results in lower frame rates and reduced performance while gaming," the company noted in the [changelog](https://support.microsoft.com/en-us/topic/july-29-2021-kb5004296-os-builds-19041-1151-19042-1151-and-19043-1151-preview-6aba536a-6ed2-41cb-bc3d-3980e8693cc4).


What's new in Windows 10 KB5004296
----------------------------------


After installing this update, Windows 10 2004 will be updated to build 19041.1151, Windows 10 20H2 will be updated to build 19042.1151, and Windows 10 21H1 will be updated to build 19043.1151.


The Windows 10 KB5004296 cumulative update preview includes multiple improvements or fixes, with the highlighted ones listed below:


* Addresses an issue with searchindexer. After you sign out, searchindexer continues to hold handles to the per user search database in the profile path, “C:\Users\username\AppData\Roaming\Microsoft\Search\Data\Applications\\”. As a result, searchindexer stops working and duplicate profile names are created.


* Addresses an issue that prevents gaming services from opening certain games for desktop users.


* Addresses an issue that prevents you from entering text using the Input Method Editor (IME). This might occur, for example, after startup if you have set the power options to shut down a laptop by closing its lid.


* Changes the functionality for uploading new activity into Timeline. If you sync your activity history across your devices using your Microsoft account (MSA), you cannot upload new activity into the Timeline. You can still use Timeline and see your activity history (information about recent apps, websites, and files) on your local device. This does not affect Azure Active Directory (AAD) accounts. To view web history, Microsoft Edge and other browsers provide the option to view recent web activities. You can also view recently used files using Microsoft OneDrive and Microsoft Office.


* Addresses an issue that might cause the File Explorer window to lose focus when you are mapping a network drive.


* Addresses an issue that causes File Explorer to stop working after reaching 99% completion when you are deleting many files on a mapped network drive.


* Addresses a timing issue in the Group Policy Registry Telemetry that causes Group Policy extension processing to fail.


* Addresses an issue that repeatedly rebuilds the Windows Filtering Platform (WFP) filters. This issue occurs when a device is enrolled in a mobile device management (MDM) service and “MDMWinsOverGP” is set.


* Addresses an issue with an MDM service that fails to correctly apply certain junk mail rules.


* Addresses an issue that always reports the update build revision (UBR) as zero (0) on a device during enrollment to an MDM service.


* Addresses an issue that causes the enrollment of the Elliptic Curve Digital Signature Algorithm (ECDSA) certificate to fail with the error, “0x80090027 NTE\_INVALID\_PARAMETER”. This issue occurs when the Trusted Platform Module (TPM) provider (the Microsoft Software Key Storage Provider) stores the key.


* Addresses an issue with auditing events 4624 and 5142 that display the wrong event template when Dutch is the display language.


* Addresses an issue that causes System Integrity to leak memory.


* Addresses an issue that plays the sound for selecting something in a game loudly when you press the trigger button on a game controller.


* Addresses an issue that prevents power plans and Game Mode from working as expected. This results in lower frame rates and reduced performance while gaming.


* Addresses an issue in which "Network Internal Access" appears on the taskbar network icon on systems that access the internet from certain domains.


* Addresses an issue in which the Network Connectivity Status Indicator (NCSI) fails to detect internet connectivity after you connect to a virtual private network (VPN).


* Addresses an issue that causes printing to stop or prints the wrong output. This issue occurs when you print using a USB connection after updating to Windows 10, version 2004 or later.


* Addresses a rare issue that might degrade performance in applications that call **Gdiplus.dll!GdipMeasureString** in a tight loop with a new font on each call. This issue occurs after installing Windows updates released on and after February 2021.


* Addresses an issue that incorrectly routes some audio channels when streaming using certain fixed channel layouts.


* Addresses an issue that always displays devices that RemoteFX USB redirects as "Remote Desktop Generic USB Device" instead of the actual device name.


* Addresses an issue in which Set-RDSessionCollectionConfiguration does not set the **camerastoredirect:s:value** custom property.


* Addresses a Local Security Authority Subsystem Service (LSASS) domain controller memory leak that is reported in Privileged Access Management (PAM) deployments.


* Addresses an issue that prevents you from accessing a network drive that maps to a Distributed File System (DFS) root after you sign out.


* Addresses an issue that prevents you from reconnecting to mapped network drives after you sign in and displays an access denied error. This issue occurs if you use the **net use** **/****deep** option to create multiple drive mappings to different paths on the same encrypted file share.


* Addresses an issue that prevents access to files on a Server Message Block (SMB) share when you enable Access Enabled Enumeration (ABE).


* Addresses an issue that prevents the Windows Server service from starting if **SrvComment** is greater than 128 characters.


* Addresses an issue in the Windows Network File System (NFS) client that might prevent you from renaming a file after mounting an NFS share. This issue occurs if you rename the file using File Explorer, but does not occur if you rename the file using command line.


* Addresses an issue with an unhandled Open File dialog critical exception. As a result, Microsoft Foundation Class (MFC) applications might close unexpectedly.


* Adds a new policy that creates generic strings and removes branding-specific terms, such as “Windows” or “PC”, for IoT Enterprise editions. For example, we changed “computer” to “device”. Instead of "Getting Windows ready," we changed that to "Getting things ready" and so on. These generic strings display on a user’s screen when an update is in progress.


* Addresses an issue in which the Storage Sense page in Settings might incorrectly report the size of some storage devices that use the GUID Partition Table (GPT). The affected devices will incorrectly report in Storage Sense that the size is twice as large as the size reported in File Explorer. **Note**: This issue does not affect storage devices that use a master boot record (MBR).






#### Tags:
[[Windows]] [[Microsoft]] [[KB5004296]] [[update,]] [[USB]] [[Bleeping Computer]]
