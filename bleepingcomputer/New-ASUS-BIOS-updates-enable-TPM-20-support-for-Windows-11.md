# New ASUS BIOS updates enable TPM 2.0 support for Windows 11
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/new-asus-bios-updates-enable-tpm-20-support-for-windows-11/)
+ Date: August 9, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 11](https://www.bleepstatic.com/content/hl-images/2021/08/09/windows-11-square-text.jpg)


ASUS has released BIOS updates for over two hundred motherboard models to automatically enable the built-in TPM 2.0 security process so that users can upgrade to Windows 11.


To explain what this means, it is important to give a bit of a background on TPMs and why they are required by Windows 11.



The Windows 11 + TPM 2.0 controversy
------------------------------------


When Microsoft first announced Windows 11, one of the biggest surprises was the new [requirement that computers would need a TPM 2.0](https://www.bleepingcomputer.com/news/microsoft/windows-11-wont-work-without-a-tpm-what-you-need-to-know/) security processor to install or upgrade to the new operating system.


For those unfamiliar with trusted platform modules (TPM), they are a dedicated security processor used to perform hardware-based cryptographic functions to secure encryption keys and prevent tampering with hardware drivers and the boot process.


While some motherboards have dedicated slots that users can install a TPM module, since 2013, Intel and AMD built firmware TPM technology into many of their CPUs that perform the same functionality as a TPM 2.0 processor.


For Intel processors, the built-in TPM 2.0 is called Intel Platform Trust Technology (Intel PTT), and for AMD, it is called AMD Platform Security Processor.


TPM 2.0 processors are now a requirement for Windows 11 as they are used to power many of the security features in the operating system.


"The following Windows features require TPM 2.0: Measured Boot, Device Encryption, WD System Guard, Device Health Attestation, Windows Hello/Hello for Business, TPM Platform Crypto Provider Key Storage, SecureBIO, DRTM, vTPM in Hyper-V," Microsoft told BleepingComputer.


After learning about this requirement, many users were angry, as their hardware that runs Windows 10 flawlessly would no longer work with Windows 11.


While a method to [bypass the Windows 11 TPM requirement](https://www.bleepingcomputer.com/news/microsoft/how-to-bypass-the-windows-11-tpm-20-requirement/) has been discovered, it will not be an easy task for many.


ASUS BIOS updates automatically enabled TPM 2.0
-----------------------------------------------


For owners of compatible CPUs and ASUS motherboards, users can enter a device's BIOS and enable the TPM 2.0 by enabling Intel Platform Trust Technology (Intel PTT) or AMD Platform Security Processor settings.



![Intel PTT BIOS setting](https://www.bleepstatic.com/images/news/hardware/asus-ptt-support.jpg)**Intel PTT BIOS setting**
However, for many people, entering the BIOS and making changes can be a confusing process.


To make it easier for ASUS owners, last week, ASUS announced that they had released [new BIOS updates for 207 motherboard models](https://www.asus.com/microsite/motherboard/ASUS-motherboards-Win11-ready/) that automatically enable the built-in TPM 2.0 processor on supported CPUs.


To check if your motherboard is supported, you can consult this [list of Windows 11 supported ASUS motherboards](http://www.asus.com/microsite/motherboard/ASUS-motherboards-Win11-ready/). If your motherboard is listed, click on the download button to download a ZIP file.


To install the new BIOS, simply extract the zip file, execute the BIOSRenamer.exe program, and follow the instructions.


While performing the BIOS update, do not shut down or reboot your computer until prompted, as it could cause an issue with the operation of your computer.


ASUS states that they continue testing other motherboards for compatibility and will update the list as they finish testing.




#### Tags:
[[Windows]] [[ASUS]] [[built-in]] [[AMD]] [[Bleeping Computer]]
