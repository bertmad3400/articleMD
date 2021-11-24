# Windows 10 KB5007253 update released with network printing fixes
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5007253-update-released-with-network-printing-fixes/)
+ Date: November 24, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 10](https://www.bleepstatic.com/content/hl-images/2021/01/25/Windows-10.jpg)


Microsoft has released the optional KB5007253 Preview cumulative update for Windows 10 2004, Windows 10 20H2, Windows 10 21H1, and Windows 10 21H2.


Microsoft claims this update fixes network printing issues causing 0x000006e4, 0x0000007c, or 0x00000709 error codes to be displayed.


The KB5007253 cumulative update preview is part of Microsoft's September 2021 monthly "C" update, allowing admins to test fixes coming as part of the December 2021 Patch Tuesday.


However, unlike Patch Tuesday updates, the "C" preview updates are optional and do not include any security updates.


Windows users can install this update by going into **Settings**, clicking on **Windows Update,** and manually performing a **'Check for Updates**.'


As this is an optional update, you will be asked whether you wish to install it by clicking on the 'Download and install' link, as shown in the image below.


Windows 10 users can also manually download and install the KB5007253 preview update from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5007253).


Microsoft claims to fix networking printing errors
--------------------------------------------------


After Microsoft modified the Windows printing experience to deal with PrintNightmare vulnerabilities, users began experiencing [errors when attempting to print to network printers](https://www.bleepingcomputer.com/news/microsoft/new-windows-10-kb5006670-update-breaks-network-printing/).


Print jobs would fail when attempting to print to a network printer, and Windows would display a 0x000006e4, 0x0000007c, or 0x00000709 error, as shown below.



![Windows 0x0000007c error when adding a new printer](https://www.bleepstatic.com/images/news/Microsoft/Windows-10/p/0x0000007c-printing-errors/0000007c-error.jpg)**Windows 0x0000007c error when adding a new printer**  
*Source: [Microsoft Forums](https://docs.microsoft.com/en-us/answers/questions/617683/error-0x0000007c-connecting-to-to-a-shared-printer.html)*
Last month, Microsoft began privately sharing printing fixes using ADMX installers that manually added [Known Issue Rollback](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/known-issue-rollback-helping-you-keep-windows-devices-protected/ba-p/2176831) (KIR) fixes to the Windows Registry.


These [installers fixed the Windows 0x0000007c printing errors](https://www.bleepingcomputer.com/news/microsoft/how-to-fix-the-windows-0x0000007c-network-printing-error/) but did not help with the other error codes people were receiving. However, Microsoft told Windows admin in private support chats that the fixes would formally be released as part of the December 2021 Patch Tuesday updates.


These fixes are now being released as part of this week's Windows 10 KB5007253 update and allegedly fix the 0x000006e4, 0x0000007c, or 0x00000709 printing errors.


BleepingComputer has not tested this update to see if it resolves this error. If you install the update, please share whether it resolved your network printing problems.


What's new in Windows 10 KB5007253
----------------------------------


After installing this update, Windows 10 2004 will be updated to build 19041.1387, Windows 10 20H2 will be updated to build 19042.1387, Windows 10 21H1 will be updated to build 19043.1387, and Windows 10 21H2 will be updated to build 19044.1387


The Windows 10 KB5007253 cumulative update preview includes thirty-three improvements or fixes, with eleven highlighted fixes below:


* Updates an issue that that causes some variable fonts to display incorrectly.
* Updates an issue that might cause the 32-bit version of Microsoft Excel to stop working on certain devices when you export to PDF.
* Updates an issue that displays letters or characters at the wrong angle when you use the Meiryo UI font and other vertical fonts. These fonts are frequently used in Japan, China, or other countries in Asia.
* Updates an issue that causes Internet Explorer to stop working when using the Input Method Editor (IME) to insert elements.
* Updates an issue that causes the Settings page to unexpectedly close after you uninstall a font.
* Updates an issue that affects your ability to rename a file using folder view in File Explorer when you use the new Japanese IME.
* Updates an issue that turns off screen capture and recording functionalities on the Windows Game Bar after a service failure.
* Updates an issue that prevents the applications that you use often from appearing on the Start menu as they should.
* Updates an issue that causes Internet Explorer to stop working.
* Addresses a known issue that causes error codes 0x000006e4, 0x0000007c, or 0x00000709 when connecting to a remote printer that is shared on a Windows print server.
* Addresses a known issue that might prevent apps, such as [Kaspersky](https://support.kaspersky.com/15819) apps, from opening after you attempt to repair or update the apps using the Microsoft Installer (MSI).


You can find a complete list of fixes in the [KB5007253 support bulletin](https://support.microsoft.com/en-us/topic/november-22-2021-kb5007253-os-builds-19041-1387-19042-1387-19043-1387-and-19044-1387-preview-d1847be9-46c1-49fc-bf56-1d469fc1b3af).




#### Tags:
[[Windows]] [[Microsoft]] [[KB5007253]] [[0x000006e4,]] [[0x0000007c,]] [[0x00000709]] [[update,]] [[Bleeping Computer]]
