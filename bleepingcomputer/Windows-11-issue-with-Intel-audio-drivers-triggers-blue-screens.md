# Windows 11 issue with Intel audio drivers triggers blue screens
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-11-issue-with-intel-audio-drivers-triggers-blue-screens/)
+ Date: November 17, 2021
+ Author: Sergiu Gatlan


## Article:
![Windows 11 issue with Intel audio drivers triggers blue screens](https://www.bleepstatic.com/content/hl-images/2021/09/01/windows-11-glow-glass.jpg)


Microsoft has confirmed a new known issue impacting Windows 11 customers and triggering to blue screens of death (BSODs) on affected systems.


The new issue is caused by compatibility issues between Intel Smart Sound Technology (SST) audio drivers and Windows 11, version 21H2.


[Intel SST](https://www.intel.com.au/content/www/au/en/architecture-and-technology/smart-sound-technology.html) is an integrated audio DSP (Digital Signal Processor) that works with the latest Intel Core and Intel Atom processors to handle audio, voice, and speech interactions.


"The affected driver will be named Intel® Smart Sound Technology (Intel® SST) Audio Controller under System Devices in Device Manager and have the file name IntcAudioBus.sys and a file version of 10.29.0.5152 and earlier or 10.30.0.5152 and earlier," Microsoft explained on the Windows Health dashboard.


The company has also added a compatibility hold to block systems with impacted Intel SST audio drivers from being offered the Windows 11 upgrade (the safeguard ID is 36899911).


Customers are advised not to manually update to Windows 11 using the Media Creation Tool or the 'Update now' button if their systems are affected by this known issue until Microsoft addresses the problem and removes the safeguard.


Workaround available for some systems
-------------------------------------


According to Microsoft, some of the impacted Windows 11 uses might work around this issue by checking if Intel can provide an updated driver for their systems.


"To mitigate the safeguard, you will need to check with your device manufacturer (OEM) to see if an updated driver is available and install it. This issue is resolved by updating the Intel® Smart Sound Technology drivers to a version 10.30.00.5714 and later or 10.29.00.5714 and later," Microsoft [added](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#2746msgdesc).


"Once you have updated to a compatible version of the Intel® Smart Sound Technology drivers, you should be able to upgrade to Windows 11."


Those who cannot find an updated driver addressing this issue will need to reach out to their device manufacturer (OEM) for more information.


After updating the affected drivers, it can take up to 48 hours before upgrading to Windows 11 if no other safeguard holds are in place for your device.


Right now, there's only one other compatibility hold [blocking Windows 11 from being offered to eligible systems running Oracle VirtualBox](https://www.bleepingcomputer.com/news/microsoft/windows-11-microsoft-is-investigating-these-eight-problems/) when Hyper-V or Windows Hypervisor are also installed.




#### Tags:
[[Windows]] [[Microsoft]] [[Intel®]] [[Bleeping Computer]]
