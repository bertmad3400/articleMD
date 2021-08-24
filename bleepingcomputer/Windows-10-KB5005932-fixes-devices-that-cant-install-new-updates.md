# Windows 10 KB5005932 fixes devices that can't install new updates
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5005932-fixes-devices-that-cant-install-new-updates/)
+ Date: August 24, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 10](https://www.bleepstatic.com/content/hl-images/2021/02/03/Windows--10.jpg)


Microsoft has released the Windows 10 KB5005932 setup update to fix '"PSFX\_E\_MATCHING\_BINARY\_MISSING" errors when attempting to install the latest cumulative updates.


After installing the May 25, 2021 (KB5003214) and June 21, 2021 (KB5003690) cumulative updates, some Windows 10 21H1, 20H2, and 2004 users have been unable to install the latest cumulative updates (LCU) released as a preview or on Patch Tuesday.


When attempting to install the LCU, they are shown a "PSFX\_E\_MATCHING\_BINARY\_MISSING" error message, and the cumulative update fails to install. The inability to install these updates is preventing devices from receiving the latest security updates and bug fixes.


"This issue occurs on devices that have been scavenged automatically to remove outdated resource records. When a system is scavenged, the recently installed latest cumulative update (LCU) is marked as permanent and the older components are removed from the system. After scavenging is complete and a device is in this state, you cannot uninstall KB5003214 or KB5003690, and you cannot install future LCUs," explains Microsoft in a [support bulletin](https://support.microsoft.com/en-us/topic/kb5005322-some-devices-cannot-install-new-updates-after-installing-kb5003214-may-25-2021-and-kb5003690-june-21-2021-66edf7cf-5d3c-401f-bd32-49865343144f) about this issue.


Microsoft recommends users perform an in-place upgrade to automatically install the latest cumulative update as part of the installation process to resolve this issue.


Tonight, Microsoft released the 'KB5005932 Windows Setup Update' that allows users to perform a manual in-place upgrade by configuring a registry setting.


"This compatibility fix enables an in-place upgrade to be run on devices that cannot complete the installation of the latest cumulative update (LCU)," explains Microsoft in the [KB5005932](http://support.microsoft.com/en-us/topic/kb5005932-windows-setup-update-for-windows-10-version-2004-20h2-and-21h1-august-24-2021-1179a984-35aa-4178-88fb-6a49125f7dc1) support bulletin.


Once the update is installed, Windows users can initiate an in-place upgrade by creating a special Registry key using the following instructions:


1. Open an elevated command prompt.
2. In the command prompt, copy and paste the following command and press **enter** on your keyboard.

```
Reg.exe Add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion /v AllowInplaceUpgrade /t REG_DWORD /f /d 1
```


![Adding Registry entry to trigger an in-place upgrade](https://www.bleepstatic.com/images/news/Microsoft/Windows-10/w/windows-update/KB5005932/adding-registry-entry.jpg)**Adding Registry entry to trigger an in-place upgrade**
3. Type **exit** and press enter to close the command prompt.


Microsoft says it will take approximately 48 hours for the in-place upgrade to be initiated after creating this registry key.


Users should note that Microsoft states that only ARM64 users need to install the KB5005932 update. However, the KB5005932 bulletin also mentions x86 and x64 support.


BleepingComputer has contacted Microsoft to clarify which devices need this update.




#### Tags:
[[Microsoft]] [[in-place]] [[Windows]] [[KB5005932]] [[Bleeping Computer]]
