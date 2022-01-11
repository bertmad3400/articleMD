# KCodes NetUSB bug exposes millions of routers to RCE attacks
### A high-severity remote code execution flaw tracked as CVE-2021-45388 has been discovered in the KCodes NetUSB kernel module, used by millions of router devices from various vendors.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/kcodes-netusb-bug-exposes-millions-of-routers-to-rce-attacks/
+ Date: 2022-01-11T07:00:00-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/10/netgear-nighthawk.jpg)

![Netgear router](https://www.bleepstatic.com/content/hl-images/2022/01/10/netgear-nighthawk.jpg)


A high-severity remote code execution flaw tracked as CVE-2021-45388 has been discovered in the KCodes NetUSB kernel module, used by millions of router devices from various vendors.


Successfully exploiting this flaw would allow a remote threat actor to execute code in the kernel, and although some restrictions apply, the impact is broad and could be severe.


The vulnerability discovery comes from researchers at SentinelLabs who shared their technical report with Bleeping Computer before publication.


What is NetUSB and how it's targeted
------------------------------------


Some router manufacturers include USB ports on devices, allowing users to share printers and USB drives on the network.


NetUSB is a kernel module connectivity solution developed by KCodes, allowing remote devices in a network to interact with the USB devices directly plugged into a router.



![NetUSB operational diagram](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/netusb.jpg)**NetUSB operational diagram**  
*Source: KCodes*
SentinelOne discovered a vulnerable code segment in the kernel module that doesn't validate the size value of a kernel memory allocation call, resulting in an integer overflow.


The 'SoftwareBus\_fillBuf' function may then use this new region for a malicious out-of-bounds write with data from a network socket under the attacker's control.


Some limitations may make it difficult to exploit the vulnerability, as described below.


* The allocated object will always be in the kmalloc-32 slab of the kernel heap. As such, the structure must be less than 32 bytes in size to fit.
* The size supplied is only used as a maximum receive size and not a strict amount.
* The structure must be sprayable from a remote perspective.
* The structure must have something that can be overwritten that makes it useful as a target (e.g. a Type-Length-Value structure or a pointer).

However, the vulnerable NetUSB module has a sixteen-second timeout to receive a request, allowing more flexibility when exploiting a device.


"While these restrictions make it difficult to write an exploit for this vulnerability, we believe that it isn’t impossible and so those with Wi-Fi routers may need to look for firmware updates for their router," SentinelOne warned in [their report](http://www.sentinelone.com/labs/cve-2021-45388-netusb-rce-flaw-in-millions-of-end-user-routers).


Affected vendors and patching
-----------------------------


The router vendors that use vulnerable NetUSB modules are **Netgear**, **TP-Link**, **Tenda**, **EDiMAX**, **Dlink**, and **Western Digital**.


It is unclear which models are affected by CVE-2021-45388, but it's generally advisable to use actively supported products that receive regular security firmware updates.


Because the vulnerability affects so many vendors, Sentinel One alerted KCodes first, on September 9, 2021, and provided a PoC (proof of concept) script on October 4, 2021, to verify the patch released that day.


Vendors were contacted in November, and a firmware update was scheduled for December 20, 2021.


Netgear released a security update to patch CVE-2021-45388 on affected and supported products on December 14, 2021.


According to the [security advisory](https://kb.netgear.com/000064437/Security-Advisory-for-Pre-Authentication-Buffer-Overflow-on-Multiple-Products-PSV-2021-0278) published on December 20, 2021, the affected Netgear products are the following:


* **D7800** fixed in firmware version 1.0.1.68
* **R6400v2** fixed in firmware version 1.0.4.122
* **R6700v3** fixed in firmware version 1.0.4.122

The solution implemented by Netgear was to add a new size check to the 'supplied size' function, preventing the out-of-bounds write.



![Fix applied by Netgear](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/netgear_fix.jpg)**Fix applied by Netgear**  
*Source: SentinelLabs*
Bleeping Computer has contacted all affected vendors to request a comment on the timeline of releasing a firmware update, but we haven't received a response yet.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Netusb]] [[Kcodes]] [[Netgear]] [[Cve-2021-45388]] [[Usb]] [[Bleeping Computer]]
#### ipv4-adresses
1.0.1.68 1.0.4.122
#### CVE's
[[CVE-2021-45388]]

