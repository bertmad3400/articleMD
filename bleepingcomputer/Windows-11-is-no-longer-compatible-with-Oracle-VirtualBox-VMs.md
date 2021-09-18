# Windows 11 is no longer compatible with Oracle VirtualBox VMs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-11-is-no-longer-compatible-with-oracle-virtualbox-vms/)
+ Date: September 18, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 11](https://www.bleepstatic.com/content/hl-images/2021/08/09/windows-11-square-text.jpg)


Windows 11 is no longer compatible with the immensely popular Oracle VirtualBox virtualization platform after Microsoft changed its hardware requirement policies for virtual machines.


When Microsoft first announced Windows 11, they stated that computers needed [new system requirements](https://www.bleepingcomputer.com/news/microsoft/microsoft-publishes-the-windows-11-system-requirements/) to install the operating system, including a [TPM 2.0 security processor](https://www.bleepingcomputer.com/news/microsoft/windows-11-wont-work-without-a-tpm-what-you-need-to-know/) and Secure Boot.


Even though many people were angry with these new hardware requirements, Microsoft has not wavered as these components are used to power numerous security features in Windows 11.


However, as the enterprise and software developers commonly use virtual machines to test new operating systems, Microsoft said that Windows 11 would not check for compatible hardware when installed or upgraded.


"Microsoft recognizes that the user experience when running the Windows 11 in virtualized environments may vary from the experience when running non-virtualized. So, while Microsoft recommends that all virtualized instances of the Windows 11 follow the same minimum hardware requirements as described in Section 1.2, the Windows 11 does not apply the hardware-compliance check for virtualized instances either during setup or upgrade," explains Microsoft in their Windows 11 [minimum hardware requirements document](https://download.microsoft.com/download/7/8/8/788bf5ab-0751-4928-a22c-dffdc23c27f2/Minimum%20Hardware%20Requirements%20for%20Windows%2011.pdf).


Microsoft this week [suddenly did an about-face](http://blogs.windows.com/windows-insider/2021/09/15/announcing-windows-11-insider-preview-build-22458/) without ample warning and is now enforcing the Windows 11 system requirements on virtual machines (VMs).



> 
> "This build includes a change that aligns the enforcement of the Windows 11 system requirements on Virtual Machines (VMs) to be the same as it is for physical PCs. Previously created VMs running Insider Preview builds may not update to the latest preview builds.
> 
> 
> In Hyper-V, VMs need to be created as a Generation 2 VM. Running Windows 11 in VMs in other virtualization products from vendors such as VMware and Oracle will continue to work as long as the hardware requirements are met." - Microsoft.
> 
> 
> 


Now when Windows Insiders attempt to update their Windows 11 builds running on virtual machines that do not have TPM support or use a small system disk, they will see a message stating, "This PC doesn't currently meet Windows 11 system requirements," as shown below.



![Windows 11 virtual machines are no longer compatible](https://www.bleepstatic.com/images/news/Microsoft/windows-11/v/virtualbox-support/windows-11-upgrade-stopped.jpg)**Windows 11 virtual machines are no longer compatible**
For VMWare Workstation, Hyper-V, Parallels, and QEMU users, this is not a problem as they support TPM passthrough and Secure Boot.



![Adding TPM to a VMware virtual machine](https://www.bleepstatic.com/images/news/Microsoft/windows-11/v/virtualbox-support/vmware-tpm.jpg)**Adding TPM to a VMware virtual machine**
However, Oracle VirtualBox does not currently support these features, causing Microsoft's new policy change to effectively make it so you cannot use Windows 11 on VirtualBox.


In response to our question about VirtualBox no longer supporting Windows 11 due to these changes, he replied that the OS will still run on other platforms.


[![tweet](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](https://twitter.com/brandonleblanc/status/1438885347174203393)


VirtualBox devs are working on a fix
------------------------------------


With Oracle VirtualBox devs dropping the ball on TPM support, they are [now working on a passthrough driver](http://www.virtualbox.org/changeset/90946/vbox) that will allow a host's TPM to pass through to the Windows 11 guest.


Once this is completed, a Windows 11 device will see a host's TPM and should allow Windows 11 upgrades and installs to continue.



![Source code for VirtualBox TPM passthrough Driver](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Source code for VirtualBox TPM passthrough Driver**
Unlike VMware, which creates a virtual TPM, VirtualBox's new driver will require a host to have a TPM 2.0 processor for this feature to work.


However, as the driver is still in its early stages, it is unclear if it will be available when Windows 11 is officially released on October 5th.


With VirtualBox being a very popular virtualization platform due to it being free and easy to use, this lack of support will affect many people who wish to continue testing or get stated with the operating system.


BleepingComputer has contacted Oracle about this TPM passthrough driver and when it's expected to be ready but has not heard back at this time.




#### Tags:
[[Windows]] [[VirtualBox]] [[Microsoft]] [[passthrough]] [[virtualization]] [[However,]] [[virtualized]] [[VMs]] [[Bleeping Computer]]
