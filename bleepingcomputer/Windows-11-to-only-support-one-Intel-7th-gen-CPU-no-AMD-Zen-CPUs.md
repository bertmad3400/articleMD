# Windows 11 to only support one Intel 7th gen CPU, no AMD Zen CPUs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-11-to-only-support-one-intel-7th-gen-cpu-no-amd-zen-cpus/)
+ Date: August 27, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 11 to only support one Intel 7th gen CPU, no AMD Zen CPUs](https://www.bleepstatic.com/content/hl-images/2021/08/09/windows-11-square-text.jpg)


Microsoft announced today that after investigating other potentially compatible processors for Windows 11, they only found one 7th generation Intel CPU to be compatible, and no AMD Zen CPUs.


When Microsoft [first announced Windows 11](https://www.bleepingcomputer.com/news/microsoft/microsoft-announces-windows-11-here-is-what-you-need-to-know/), many users were upset, if not angry, about the new and stricter [system requirements](https://www.bleepingcomputer.com/news/microsoft/microsoft-publishes-the-windows-11-system-requirements/) for the new operating system.


With the [new TPM 2.0 requirement](https://www.bleepingcomputer.com/news/microsoft/windows-11-wont-work-without-a-tpm-what-you-need-to-know/) and a restricted list of compatible CPUs, many people found that their devices with Intel 7th generation and AMD Zen CPUs, which run Windows 10 flawlessly, cab no longer upgrade to Windows 11.


To make matters worse, Microsoft released a new tool called PC Health Check that checks if your hardware is compatible with Windows 11. However, this tool was severely lacking as it provided little information as to why a device was not compatible, as shown below.



![Windows 11 PC Health Check tool](https://www.bleepstatic.com/images/news/Microsoft/windows-11/h/hardware-requirements/pc-health-check.jpg)**Windows 11 PC Health Check tool**
Additional Windows 11 compatible CPUs
-------------------------------------


Microsoft announced today that they had expanded their list of compatible 64-bit processors to include one Intel 7th generation CPU and newer Intel Core CPUs:


* Intel Core X-series, Xeon W-series
* Intel Core 7820HQ (only select devices that shipped with modern drivers based on Declarative, Componentized, Hardware Support Apps (DCH) design principles, this includes Surface Studio 2)


Microsoft uses the Intel Core i7-7820HQ processor in their $3,500 Surface Studio 2 devices, so it is not surprising to see that this CPU found its way into the compatibility list.


According to Microsoft, these additional CPUs were added as they follow [Microsoft's DCH design principles](https://docs.microsoft.com/en-us/windows-hardware/drivers/develop/dch-principles-best-practices#dch-design-principles):



> 
> * Declarative **(D)**: Install the driver by using only declarative INF directives. Don't include co-installers or RegisterDll functions.
> 
> 
> * Componentized **(C)**: Edition-specific, OEM-specific, and optional customizations to the driver are separate from the base driver package. As a result, the base driver, which provides only core device functionality, can be targeted, flighted, and serviced independently from the customizations.
> 
> 
> * Hardware Support App **(H)**: Any user interface (UI) component associated with a Windows Driver must be packaged as a Hardware Support App (HSA) or preinstalled on the OEM device. An HSA is an optional device-specific app that's paired with a driver. The application can be a Universal Windows Platform (UWP) or Desktop Bridge app. You must distribute and update an HSA through the Microsoft Store. For details, see Hardware Support App (HSA): Steps for driver developers and Hardware Support App (HSA): Steps for app developers.
> 
> 
> 


Microsoft says that CPUs who following the DCH design principles have a 99.8% kernel crash-free experience.


"Devices that do not meet the minimum system requirements had 52% more kernel mode crashes. While devices that do meet the minimum system requirements had a 99.8% crash free experience," explained Microsoft in today's blog post.


Unfortunately, no other Intel 7th generation CPUs are compatible with Windows 11. Furthermore, after working with AMD to analyze first-generation AMD Zen CPUs, Microsoft determined that none of them were compatible with Windows 11.


Updated PC Health Check tool released soon
------------------------------------------


In addition to the minor change in CPU compatibility, Microsoft has released a new version of their [PC Health Check tool](http://www.microsoft.com/en-us/windows/windows-11#pchealthcheck) that provides more detailed information regarding why a device is not compatible with Windows 11.


With the new version, users will get detailed explanations as to what is missing to make their device compatible with Windows 11, as shown below.



![Updated PC Health Check Tool](https://www.bleepstatic.com/images/news/Microsoft/windows-11/p/pc-health-check/new-pc-health-check.jpg)**Updated PC Health Check Tool**
While users cannot resolve an incompatible CPU without buying another processor, other items like Secure Boot or a missing TPM 2.0 processor, can in many cases, be fixed by [enabling settings in the BIOS](https://www.bleepingcomputer.com/news/microsoft/windows-11-wont-work-without-a-tpm-what-you-need-to-know/).




#### Tags:
[[Windows]] [[Microsoft]] [[7th]] [[AMD]] [[CPUs,]] [[Bleeping Computer]]
