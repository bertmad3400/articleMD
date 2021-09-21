# Microsoft PC Health Check adds detailed Windows 11 compatibility info
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-pc-health-check-adds-detailed-windows-11-compatibility-info/)
+ Date: September 21, 2021
+ Author: Lawrence Abrams


## Article:
![PC Health Check Tool](https://www.bleepstatic.com/content/hl-images/2021/09/21/header-image.jpg)


Microsoft has released an updated PC Health Check tool that provides detailed information about whether a device's hardware is compatible with Windows 11.


This tool was released alongside Microsoft's Windows 11 announcement, but it was not very useful in showing why a device was not compatible with the [new system requirements](https://www.bleepingcomputer.com/news/microsoft/microsoft-publishes-the-windows-11-system-requirements/).



![Original PC Health Check tool with little information](https://www.bleepstatic.com/images/news/Microsoft/windows-11/t/tpm-requirement/failed-upgrade-check.jpg)**Original PC Health Check tool with little information**
While Microsoft continued to refine the app to show more information, they eventually pulled the program as it did provide enough information to be helpful.


"Based on the feedback so far, we acknowledge that it was not fully prepared to share the level of detail or accuracy you expected from us on why a Windows 10 PC doesn’t meet upgrade requirements," explained Microsoft in a [blog post](https://blogs.windows.com/windows-insider/2021/06/28/update-on-windows-11-minimum-system-requirements/).


"We are temporarily removing the app so that our teams can address the feedback."


Updated PC Health Check tool released
-------------------------------------


In August, Microsoft released an updated version of the PC Health Check tool to Insiders for testing and stated it would be coming soon for all Windows users.


Yesterday, Microsoft quietly released a [new version of the PC Health Check tool](https://aka.ms/GetPCHealthCheckApp) with a far more significant amount of detailed information about why a particular device is not compatible with Windows 11.


As you can see below, the updated PC Health Check tool now explains that one of my devices needs Secure Boot enabled, a TPM 2.0 security processor was not found, and my CPU is not compatible.



![New PC Health Check tool with detailed compatibility information](https://www.bleepstatic.com/images/news/Microsoft/windows-11/p/pc-health-check/updated-version/incompatible-hardware.jpg)**New PC Health Check tool with detailed compatibility information**
While an older incompatible CPU will need to be replaced, it may be possible to [enable Secure Boot and the TPM 2.0 processor](https://www.bleepingcomputer.com/news/microsoft/windows-11-wont-work-without-a-tpm-what-you-need-to-know/) for more recent devices simply by changing some settings in the computer's BIOS.


When enabling TPM support in the BIOS, users should look for Intel Platform Trust Technology (Intel PTT) or AMD PSP fTPM settings depending on the device's CPU.



![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Enabling Intel Platform Trust Technology (Intel PTT)**
Once these settings are enabled, you can rerun the PC Health Check tool to ensure Windows properly sees the previously missing features.


While this tool will not ease the frustration shared by many users who incompatible CPUs run Windows 10 perfectly, it should help those with compatible hardware, but disabled features, get ready to upgrade to Windows 11.




#### Tags:
[[Windows]] [[Microsoft]] [[Bleeping Computer]]
