# Microsoft shares Windows 11 TPM check bypass for unsupported PCs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-shares-windows-11-tpm-check-bypass-for-unsupported-pcs/)
+ Date: October 6, 2021
+ Author: Bill Toulas


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/09/03/windows-11-dark-storm-clouds.jpg?rand=1795172990)


Microsoft has published a new support webpage where they provide an official method to bypass the TPM 2.0 check and have Windows 11 installed on unsupported systems.


This is somewhat surprising considering the unwavering stance the tech giant chose to maintain in relation to the minimum requirements for the new Windows version.


As it seems though, Microsoft couldn’t ignore the fact that bypassing TPM checks [is fairly simple](https://www.bleepingcomputer.com/news/microsoft/new-windows-11-install-script-bypasses-tpm-system-requirements/), so to avoid having people breaking their systems by using non-standardized third-party scripts, they decided to just give users an official way to do it.


To install Windows 11 on unsupported systems, users are instructed to do the following:


* Visit the Windows 11 [software download page](https://www.microsoft.com/en-gb/software-download/windows11), select “Create tool now”, and follow the installation instructions.
* On Windows, click ‘Start’, type ‘Registry Editor’ and click on the icon to launch the tool
* Create a new registry entry on HKEY\_LOCAL\_MACHINE\SYSTEM\Setup\MoSetup Use the “REG\_DWORD” type
* Name it “AllowUpgradesWithUnsupportedTPMOrCPU”
* Set value to “1”
* Reboot your system


![registry key](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/registry%20value.jpg)Adding the new registry value. Image: BleepingComputer
Having done all that, you may then upgrade by launching Setup on the media while running Windows 10, or by simply booting from the media to launch Setup. Standard installation options such as 'Full Upgrade', 'Keep Data Only', and 'Clean Install', will all be available as normal.


Not a dependable solution
-------------------------


At this point, we should warn you that even if the above appears to be fairly simple and straight forward, there are risks involved when adding registry keys or modifying existing entries.


Doing something wrong in the Registry Editor could result in a corrupted filesystem or unbootable OS, leaving you with the only option to reinstall it. As such, if you want to experiment with [Microsoft’s guidelines](https://support.microsoft.com/en-us/windows/ways-to-install-windows-11-e0edbbfb-cfc5-4011-868b-2ce77ac7c70e), you are doing so at your own risk.


Also, TPM 2.0 remains an important security feature that is the source of a wide range of ‘peace of mind’ benefits, so if you’re installing Windows 11 on a non-TPM 2.0 chip, you will miss out on all of them.


Understanding and accepting these risks is important, as is the fact that Microsoft is not recommending to install Windows 11 on an unsupported system unless you are instructed otherwise by support.


Some of the underlying incompatibilities may introduce minor or major functional problems in the future, so we would recommend this path only to those who have a good reason to take it. Plain curiosity and fear of missing out aren’t.


For the rest, just wait until you can upgrade your hardware or buy a new and supported system. The Windows 10 EOL (end of life) date is in October 2025, so there’s plenty of time.




#### Tags:
[[Windows]] [[Microsoft]] [[it.]] [[Bleeping Computer]]
