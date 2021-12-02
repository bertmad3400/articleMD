# Nine WiFi routers used by millions were vulnerable to 226 flaws
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/nine-wifi-routers-used-by-millions-were-vulnerable-to-226-flaws/)
+ Date: December 2, 2021
+ Author: Bill Toulas


## Article:
![router](https://www.bleepstatic.com/content/hl-images/2021/11/19/modem_router.jpg?rand=459340730)


Security researchers analyzed nine popular WiFi routers and found a total of 226 potential vulnerabilities in them, even when running the latest firmware.


The tested routers are made by Asus, AVM, D-Link, Netgear, Edimax, TP-Link, Synology, and Linksys, and are used by millions of people.


The front-runners in terms of the number of vulnerabilities are the TP-Link Archer AX6000, having 32 flaws, and the Synology RT-2600ac, which has 30 security bugs.



![High-severity flaws affecting TP-Link Archer AX6000](https://www.bleepstatic.com/images/news/u/1220909/Tables/TP-Link.jpg)**High-severity flaws affecting TP-Link Archer AX6000**  
*Source: IoT Inspector*
The testing process
-------------------


Researchers at IoT Inspector carried out the security tests in collaboration with CHIP magazine, focusing on models used mainly by small firms and home users.


"For Chip’s router evaluation, vendors provided them with current models, which were upgrade to the latest firmware version," Florian Lukavsky, CTO & Founder at IoT Inspector, told BleepingComputer via email.


"The firmware versions were automatically analyzed by IoT Inspector and checked for more than 5,000 CVEs and other security issues."


Their findings showed that many of the routers were still vulnerable to publicly disclosed vulnerabilities, even when using the latest firmware, as illustrated in the table below.



![Router models and flaws categorized as per their severity](https://www.bleepstatic.com/images/news/security/translated-table.jpg)**Router models and flaws categorized as per their severity**  
*Source: IT Inspector  

Left column translated by BleepingComputer*
While not all flaws carried the same risk, the team found some common problems that affected most of the tested models:


* Outdated Linux kernel in the firmware
* Outdated multimedia and VPN functions
* Over-reliance on older versions of BusyBox
* Use of weak default passwords like "admin"
* Presence of hardcoded credentials in plain text form


Jan Wendenburg, the CEO of IoT Inspector, noted that one of the most important ways of securing a router is to change the default password when you first configure the device.


"Changing passwords on first use and enabling the automatic update function must be standard practice on all IoT devices, whether the device is used at home or in a corporate network." [explained](http://www.iot-inspector.com/blog/router-security-check-2021/) Wendenburg.


"The greatest danger, besides vulnerabilities introduced by manufacturers, is using an IoT device according to the motto 'plug, play and forget'."


Extracting an encryption key
----------------------------


The researchers didn't publish many technical details about their findings, except for one case concerning the [extraction of the encryption key](https://www.iot-inspector.com/blog/extracting-decryption-keys-dlink/) for D-Link router firmware images.


The team found a way to gain local privileges on a D-Link DIR-X1560 and get shell access via the physical UART debug interface.


Next, they dumped the whole filesystem using built-in BusyBox commands and then located the binary responsible for the decryption routine.


By analyzing the corresponding variables and functions, the researchers eventually extracted the AES key used for the firmware encryption.



![Deriving the AES key on CyberChef](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Deriving the AES key on CyberChef**  
*Source: IoT Inspector*
Using that key, a threat actor can send malicious firmware image updates to pass verification checks on the device, potentially planting malware on the router.


Such problems can be solved with full-disk encryption that secures locally stored images, but this practice is not common.


Manufacturers responded quickly
-------------------------------


All of the affected manufacturers responded to the researchers' findings and released firmware patches.


CHIP's author [Jörg Geiger](https://www.iot-inspector.com/wp-content/uploads/2021/11/Chip-IoT-Inspector-Router-Sicherheit-Test.pdf) commented that the router vendors addressed most of the security flaws identified by the working group, but not all of them.


The researchers have told Bleeping Computer that the unpatched flaws are mostly lower importance vulnerabilities. However, they clarified that no follow-up tests were done to confirm that the security updates fixed the reported issues.


The vendor responses to CHIP (translated) were the following:


* **Asus**: Asus examined every single point of the analysis and presented us with a detailed answer. Asus has patched the outdated BusyBox version, and there are also updates for “curl” and the web server. The pointed out that password problems were temp files that the process removes when it is terminated. They do not pose a risk.
* **D-Link**: D-Link thanked us briefly for the information and published a firmware update that fixes the problems mentioned.
* **Edimax**: Edimax doesn't seem to have invested too much time in checking the problems, but at the end there was a firmware update that fixed some of the gaps.
* **Linksys**: Linksys has taken a position on all issues classified as "high" and "medium". Default passwords will be avoided in the future; there is a firmware update for the remaining problems.
* **Netgear**: At Netgear they worked hard and took a close look at all problems. Netgear sees some of the "high" issues as less of a problem. There are updates for DNSmasq and iPerf, other reported problems should be observed first.
* **Synology**: Synology is addressing the issues we mentioned with a major update to the Linux kernel. BusyBox and PHP will be updated to new versions and Synology will soon be cleaning up the certificates. Incidentally, not only the routers benefit from this, but also other Synology devices.
* **TP-Link**: With updates from BusyBox, CURL and DNSmasq, TP-Link eliminates many problems. There is no new kernel, but they plan more than 50 fixes for the operating system


If you are using any of the models mentioned in the report, you are advised to apply the available security updates, enable "automatic updates", and change the default password to one that is unique and strong.


Additionally, you should disable remote access, UPnP (Universal Plug and Play), and the WPS (WiFi Protected Setup) functions if you're not actively using them.


Bleeping Computer has contacted all of the affected manufacturers requesting a comment on the above, and we will update this piece as soon as we receive their response.




#### Tags:
[[IoT]] [[Synology]] [[BusyBox]] [[TP-Link]] [[D-Link]] [[problems.]] [[Bleeping Computer]]
