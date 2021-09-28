# New Windows 11 install script bypasses TPM, system requirements
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/new-windows-11-install-script-bypasses-tpm-system-requirements/)
+ Date: September 28, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 11](https://www.bleepstatic.com/content/hl-images/2021/08/09/windows-11-square-text.jpg)


A new script allows you to install Windows 11 on devices with incompatible hardware, such as missing TPM 2.0, incompatible CPUs, or the lack of Secure Boot. Even better, the script also works on virtual machines, allowing you to upgrade to the latest Windows Insider build.


When Windows 11 was first announced, Microsoft released the operating system's [new system requirements](https://www.bleepingcomputer.com/news/microsoft/microsoft-publishes-the-windows-11-system-requirements/), which included a [TPM 2.0 security processor](https://www.bleepingcomputer.com/news/microsoft/windows-11-wont-work-without-a-tpm-what-you-need-to-know/), Secure Boot, newer CPUs, and at least 64 GB of hard drive space.


As Microsoft realized that many people, especially those in the enterprise, would be testing Windows 11 preview builds on virtual machines, they [exempted them from the system requirements](https://download.microsoft.com/download/7/8/8/788bf5ab-0751-4928-a22c-dffdc23c27f2/Minimum%20Hardware%20Requirements%20for%20Windows%2011.pdf).


However, Microsoft is now [requiring compatible hardware even on virtual machines](https://www.bleepingcomputer.com/news/microsoft/windows-11-is-no-longer-compatible-with-oracle-virtualbox-vms/) and taking a firm stance on its system requirement, going as far as to say that people who install Windows 11 on incompatible hardware [may not get security updates](https://www.bleepingcomputer.com/news/microsoft/windows-11-may-not-get-security-updates-on-unsupported-devices/).


For those willing to risk running Windows 11 on incompatible hardware, a script has been released that allows new installations and upgrades to bypass the operating system's system requirements.


Script bypasses Windows 11 system requirements
----------------------------------------------


This new script was released as part of the extremely useful [Universal MediaCreationTool wrapper](https://www.bleepingcomputer.com/news/microsoft/download-isos-for-any-version-of-windows-10-with-this-script/), a batch file that allows you to create an ISO for any version of Windows 10, with Windows 11 support added last week.



![Universal MediaCreationTool wrapper](https://www.bleepstatic.com/images/news/Microsoft/windows-11/h/bypass-system-requirements/mediacreationtool.jpg)**Universal MediaCreationTool wrapper**  
*Source: BleepingComputer*
While the main script of this [open-source project](https://gist.github.com/AveYo/c74dc774a8fb81a332b5d65613187b15) is the '[MediaCreationTool.bat](https://gist.github.com/AveYo/c74dc774a8fb81a332b5d65613187b15#file-mediacreationtool-bat)' used to create Windows ISOs, it also includes a script named '[Skip\_TPM\_Check\_on\_Dynamic\_Update.cmd](https://gist.github.com/AveYo/c74dc774a8fb81a332b5d65613187b15#file-skip_tpm_check_on_dynamic_update-cmd),' which configures the device to bypass compatible hardware checks.


When executed on a Windows 10 or Windows 11 device, the Skip\_TPM\_Check\_on\_Dynamic\_Update.cmd script will perform a variety of tasks, including:


* When executed, the script will create the '**AllowUpgradesWithUnsupportedTPMOrCPU**' value under the **HKEY\_LOCAL\_MACHINE\SYSTEM\Setup\MoSetup** Registry key and set it to **1**.
* Registers a WMI event subscription named 'Skip TPM Check on Dynamic Update' that deletes the '**C:\$WINDOWS.~BT\appraiserres.dll**' file when the **vdsldr.exe** executable is launched during Windows 11 setup.
It should be noted that the created WMI event subscription will remain in effect until you run the Skip\_TPM\_Check\_on\_Dynamic\_Update.cmd script again, which will cause the event subscriptions to be deleted. You can do this after installing or upgrading Windows 11.




Before using this script, when attempting to upgrade a Windows 11 build 22449 virtual machine to the latest preview build, the upgrade failed as the setup could not see the secure boot feature, a TPM 2.0 processor, and the system disk was too small.



![Windows 11 setup failing on incompatible hardware](https://www.bleepstatic.com/images/news/Microsoft/windows-11/h/bypass-system-requirements/windows-11-setup-not-compatible.jpg)**Windows 11 setup failing on incompatible hardware**  
*Source: BleepingComputer*
However, after running this script, we could install the latest Windows 11 preview build 22463 without a problem.



![Windows 11 preview build 22463 installed in VirtualBox](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Windows 11 preview build 22463 installed in VirtualBox**
Anyone who decides to use this bypass should be aware that this is an unsupported method to install Windows 11 and could lead to performance issues or other bugs when using the operating system. Furthermore, Microsoft may not provide security updates to unsupported devices, so your installation will likely be less secure.


Therefore, you should only use this method in test environments and not on production devices.




#### Tags:
[[Windows]] [[Microsoft]] [[Bleeping Computer]]
