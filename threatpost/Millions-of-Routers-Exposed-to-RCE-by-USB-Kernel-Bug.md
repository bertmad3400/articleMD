# Millions of Routers Exposed to RCE by USB Kernel Bug
### The high-severity RCE flaw is in the KCodes NetUSB kernel module, used by popular routers from Netgear, TP-Link, DLink, Western Digital, et al.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177506
+ Date: 2022-01-11T12:00:04+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/04/01165141/Kernel-e1617310316383.jpg)

Millions of popular end-user routers are at risk of remote code execution (RCE) due to a high-severity flaw in the KCodes NetUSB kernel module.


The [module](http://kcodes.com/product/usb_01.html) enables remote devices to connect to routers over IP and access any USB devices (such as printers, speakers, webcams, flash drives and other peripherals) that are plugged into them. This is made possible using the proprietary NetUSB protocol and a Linux kernel driver that launches a server, which makes the USB devices available via the network. For remote users, it’s as if the USB devices are physically plugged into their local systems.


According to a Tuesday [writeup](https://www.sentinelone.com/labs/cve-2021-45388-netusb-rce-flaw-in-millions-of-end-user-routers) from SentinelOne vulnerability researcher Max Van Amerongen, attackers could remotely exploit the vulnerability to execute code in the kernel via a pre-authentication buffer overflow security vulnerability, allowing device takeover.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

NetUSB is licensed to a slew of popular router vendors, including:


* Netgear
* TP-Link
* Tenda
* EDiMAX
* DLink
* Western Digital


Fortunately, SentinelOne hasn’t yet spotted evidence of the flaw having been exploited in the wild.


‘Who Doesn’t Love a Remote Kernel Bug?’
---------------------------------------


As is his wont, Van Amerongen found the bug while poking around at a target of the Pwn2Own hacking contests: the aforementioned Netgear router, R6700v3. The device appeared in the 2019 Pwn2Own conference as well as being named as a target in [Pwn2Own Austin 2021](https://www.techtarget.com/searchsecurity/news/252509184/Routers-NAS-and-phones-hacked-in-Pwn2Own-competition).


He came across the NetUSB kernel module while sifting through various paths through various binaries, where he saw something fishy: “As it turned out, this module was listening on TCP port 20005 on the IP 0.0.0.0,” Van Amerongen explained. “Provided there were no firewall rules in place to block it, that would mean it was listening on the WAN as well as the LAN. Who wouldn’t love a remote kernel bug?”


He does love to pop kernels: In November, Van Amerongen wrote up a bug (CVE-2021-43267) that he discovered in a Transparent Inter Process Communication (TIPC) message type that allows Linux nodes to send cryptographic keys to each other. The critical heap-overflow security vulnerability in the Linux kernel could have allowed [local exploitation and RCE](https://threatpost.com/critical-linux-kernel-bug/176000/), leading to full system compromise.


This isn’t the first time a worrisome NetUSB vulnerability has been discovered, either. In 2015, there was another [kernel stack buffer overflow](https://sec-consult.com/vulnerability-lab/advisory/kernel-stack-buffer-overflow-in-kcodes-netusb/) in KCodes NetUSB. That [discovery](https://threatpost.com/details-surface-on-unpatched-kcodes-netusb-bug/112910/) led to a “very helpful exploit” that helped to quickly verify the more recent vulnerability, Van Amerongen recounted.


The Communication Handshake
---------------------------


The USB connection process starts with a handshake between the PC and router that initializes communication: a handshake that SentinelOne depicted in the graphic below.


What comes next after the handshake is a command-parsing while-loop, which contains the following code:


“SoftwareBus\_fillBuf acts in a similar way to recv by taking both a buffer and its size, filling the buffer with data read from the socket,” Van Amerongen wrote.


The Bug
-------


The vulnerable chunk of code in the kernel module is triggered when the command 0x805f reaches the following code in the function SoftwareBus\_dispatchNormalEPMsgOut:


“Four bytes are fetched from the remote PC,” the researcher continued. “The number 0x11 is added to it and then used as a size value in kmalloc. Since this supplied size isn’t validated, the addition of the 0x11 can result in an integer overflow. For example, a size of 0xffffffff would result in 0x10 after 0x11 has been added to it.”


This allocated region is then used and written to through both dereferencing and through the SoftwareBus\_fillBuf function, he continued, as shown below.


“Looking at the final call to SoftwareBus\_fillBuf, the supplied size is used as a maximum value to read from the remote socket,” Van Amerongen said. “From the previous example, the size 0xffffffff would be used here (not the overflown value) as the size sent to recv.”


Along with its report, SentinelOne sent a suggested mitigation strategy, shown below. This integer overflow check should be performed before allocating memory with user supplied sizes, the firm noted:


<pre>  

if(user\_supplied\_size + 0x11 < 0x11) return;  

</pre>


Exploitability
--------------


There are a number of factors that play into the feasibility of exploiting this bug, according to the analysis:


**Size that can be allocated:** The minimum size that can be allocated is 0x0, and the maximum is 0x10. “That means that the allocated object will always be in the kmalloc-32 slab of the kernel heap,” Van Amerongen noted.


**The amount of control over the overflow itself:** The attacker controls the data being received over the socket, but is the size negotiable? “Since a size of 0xffffffff is not realistically exploitable on a 32-bit system, it’s necessary to take a look at how SoftwareBus\_fillBuf actually works,” the  researcher explained. “Underneath this function is the standard socket recv function. That means that the size supplied is only used as a maximum receive size and not a strict amount, like memcpy.”


**Ease of laying out the kernel heap for the overflow:** “Many exploits require the use of heap holes in order to make sure that the vulnerable heap structure will be placed before the object that will be overwritten,” Van Amerongen added. “In the case of this kernel module, there’s a timeout of 16 seconds on the socket for receiving data, meaning the struct can be overflown up to 16 seconds after it is allocated. This removes the need to create a heap hole.”


**Constraints regarding which target structures could be overwritten:**


* The structure must be less than 32 bytes in size in order to fit into kmalloc-32
* The structure must be sprayable from a remote perspective
* The structure must have something that can be overwritten that makes it useful as a target (e.g. a Type-Length-Value structure or a pointer)


**Too Big to Ignore**
---------------------


Bottom line: It’s not a trivial task to write an exploit for this vulnerability, but SentinelOne doesn’t think it’s impossible, and it’s too critical to ignore. “This vulnerability affects millions of devices around the world and in some instances may be completely remotely accessible,” Van Amerongen stressed.


Given that the vulnerability is in a third-party component licensed to various router vendors, that means the only fix is a firmware update rolling out from each specific vendor – if it’s even available.


SentinelLabs began the disclosure process on Sept. 9, and the patch was sent to all vendors on Oct. 4. On Dec. 14, Netgear had released fixed firmware for its R6700v3 device (version 1.0.4.122). And on Dec. 20, Netgear released an [advisory](https://kb.netgear.com/000064437/Security-Advisory-for-Pre-Authentication-Buffer-Overflow-on-Multiple-Products-PSV-2021-0278) about the flaw, with patches for D7800 models (firmware version 1.0.1.68) and R6400v2 routers (fixed in firmware version 1.0.4.122).


All of the other vendors affected by the NetUSB bug are aware of the vulnerability and have either fixed it or in the process of fixing it, according to SentinelOne. However, if a router is end-of-life, that update may never come.


Long story short: Router owners should be on the lookout for a firmware update, Van Amerongen concluded. If none’s forthcoming, the mitigation listed above is the way to go.


“While we are not going to release any exploits for it, there is a chance that one may become public in the future despite the rather significant complexity involved in developing one,” he said. “We recommend that all users follow the remediation information above in order to reduce any potential risk.”


***Password** **Reset:** **[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):** Fortify 2022 with a password-security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken. **[Register & stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)** – sponsored by Specops Software.*





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Epic]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Amerongen]] [[Netusb]] [[Sentinelone]] [[Usb]] [[Netgear]] [[0x11]] [[Linux]] [[Pwn2own]] [[0xffffffff]] [[Softwarebus_fillbuf]] [[ThreatPost]]
#### ipv4-adresses
0.0.0.0 1.0.4.122 1.0.1.68
#### CVE's
[[CVE-2021-43267]]

