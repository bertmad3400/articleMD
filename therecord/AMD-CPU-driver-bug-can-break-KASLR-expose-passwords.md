# AMD CPU driver bug can break KASLR, expose passwords
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/amd-cpu-driver-bug-can-break-kaslr-expose-passwords/)
+ Date: September 16, 2021
+ Author: Catalin Cimpanu


## Article:
![AMD CPU driver bug can break KASLR, expose passwords](https://therecord.media/wp-content/uploads/2021/09/AMD-Ryzen.jpg)

AMD has advised Windows users this week to update their operating systems in order to receive a patch for a dangerous vulnerability in one of its CPU chipset drivers that can be exploited to dump system memory and steal sensitive information from AMD-powered computers.


Tracked as **CVE-2021-26333** and discovered by Kyriakos Economou, co-founder of security firm ZeroPeril, the vulnerability resides in the driver for  [AMD Platform Security Processor (PSP)](https://en.wikipedia.org/wiki/AMD_Platform_Security_Processor), which is AMD’s equivalent for Intel’s SGX technology.


Also known as a trusted execution environment (TEE), the AMD PSP creates secure enclaves inside AMD processors that allow the operating system to process sensitive information inside cryptographically secured memory.


In order to interact with PSP enclaves, the Windows OS uses a kernel driver named **amdsps.sys**.


But in a [report](https://zeroperil.co.uk/cve-2021-26333/) published on Wednesday, Economou said he found two issues in this driver that allows a non-admin user to dump the system memory and search for sensitive information handled by the OS.


“During our tests we managed to leak several gigabytes of uninitialized physical pages,” the ZerPeril co-founder said.



> The contents of those physical pages varied from kernel objects and arbitrary pool addresses that can be used to circumvent exploitation mitigations such as [KASLR](https://en.wikipedia.org/wiki/Address_space_layout_randomization), and even registry key mappings of *\Registry\Machine\SAM* containing [NTLM hashes](https://docs.microsoft.com/en-us/windows/win32/secauthn/microsoft-ntlm) of user authentication credentials that can be used in subsequent attack stages. For example, these can be used to steal credentials of a user with administrative privilege and/or be used in [pass-the-hash](https://www.sans.org/white-papers/33283/) style attacks to gain further access inside a network.
> 
> Kyriakos Economou, co-founder of security firm ZeroPeril


### Patches available via Windows Update


Economou said they successfully tested attacks on AMD Ryzen 2000- and 3000-series CPUs before reporting the issue to the vendor earlier this year in April.


On Tuesday, as Microsoft rolled out its monthly batch of security updates known as Patch Tuesday, AMD issued its own [advisory](https://www.amd.com/en/corporate/product-security/bulletin/amd-sb-1009) urging users to apply the updates as they also contained updates for its PSP chipset driver.


“AMD recommends updating to AMD PSP driver 5.17.0.0 through Windows Update or by updating to AMD Chipset Driver 3.08.17.735,” the company said this week.


The Santa Clara-based hardware vendor said the following AMD CPU products are affected and that users running these products will need to look into updating their systems as well.


* 6th Generation AMD FX APU with Radeon™ R7 Graphics
* AMD A10 APU with Radeon R6 Graphics
* AMD A8 APU with Radeon R6 Graphics
* AMD A6 APU with Radeon R5 Graphics
* AMD A4-Series APU with Radeon Graphics
* AMD Athlon™ X4 Processor
* AMD E1-Series APU with Radeon Graphics
* AMD Ryzen™ 1000 series Processor





#### Tags:
[[AMD]] [[APU]] [[GraphicsAMD]] [[Radeon]] [[Windows]] [[PSP]] [[co-founder]] [[The Record]]
