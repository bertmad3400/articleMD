# ‘Demon’s Cries’ authentication bypass patched in Netgear switches
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/demons-cries-authentication-bypass-patched-in-netgear-switches/)
+ Date: September 6, 2021
+ Author: Catalin Cimpanu


## Article:
![‘Demon’s Cries’ authentication bypass patched in Netgear switches](https://therecord.media/wp-content/uploads/2021/09/devil.png)

Networking equipment vendor Netgear has patched three vulnerabilities in several of its smart switches that can allow threat actors to bypass authentication and take over devices.


Codenamed **Demon’s Cries**, **Draconian Fear**, and **Seventh Inferno**, the vulnerabilities were discovered and reported to Netgear by a Polish security researcher going by the pseudonym of Gynvael Coldwind.


* Netgear released [patches](https://kb.netgear.com/000063978/Security-Advisory-for-Multiple-Vulnerabilities-on-Some-Smart-Switches-PSV-2021-0140-PSV-2021-0144-PSV-2021-0145) last week on September 3.
* The researcher published detailed write-ups for the first two bugs, [Demon’s Cries](https://gynvael.coldwind.pl/?id=740) and [Draconian Fear](https://gynvael.coldwind.pl/?id=741).
* Coldwind said technical details about the Seventh Inferno bug would be published next Monday, on September 13.


Of the three vulnerabilities, the first, known as Demon’s Cries, is considered the most severe, with a severity rating of 9.8 out of a maximum of 10, on the CVSSv3 scale.


As Coldwind explained today, the vulnerability can be used to change to bypass initial authentication and change the admin account password for affected Netgear switches.


Not all switches are vulnerable, as the bug resides in the device’s web-based administration panel, known as SCC Control (NETGEAR Smart Control Center), which is disabled by default.


However, if the web UI is enabled, Coldwind says the bug can result in “a full compromise of the device.”


The Polish researcher said he initially tested the bug on a Netgear GS110TPV3 Smart Managed Pro Switch, but the US company confirmed that both Demon’s Cries and Draconian Fear impact a much larger list of devices.


**Affected Netgear models:**


* GC108P
* GC108PP
* GS108Tv3
* GS110TPP
* GS110TPv3
* GS110TUP
* GS308T
* GS310TP
* GS710TUP
* GS716TP
* GS716TPP
* GS724TPP
* GS724TPv2
* GS728TPPv2
* GS728TPv2
* GS750E
* GS752TPP
* GS752TPv2
* MS510TXM
* MS510TXUP


On the other hand, the Draconian Fear vulnerability, while also an authentication bypass, is considered less severe. Coldwind said this bug could only be exploited to hijack logged-in admin sessions, but the attack needs to be carried out from the admin’s IP address.


The researcher released proof-of-concept code for both bugs.





#### Tags:
[[Netgear]] [[Demon’s]] [[Coldwind]] [[The Record]]
