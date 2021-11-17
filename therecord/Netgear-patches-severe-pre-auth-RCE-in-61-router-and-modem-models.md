# Netgear patches severe pre-auth RCE in 61 router and modem models
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/netgear-deals-with-its-fifth-wave-of-severe-rce-bugs-this-year/)
+ Date: November 17, 2021
+ Author: Catalin Cimpanu


## Article:
![Netgear patches severe pre-auth RCE in 61 router and modem models](https://therecord.media/wp-content/uploads/2021/11/netgear.jpg)

Networking equipment vendor Netgear has patched the fifth set of dangerous remote code execution bugs impacting its small office and small home (SOHO) routers this year.


Discovered by security firm GRIMM, the latest set of patches address a bug that can be exploited from within local networks to allow attackers to take full control of a vulnerable Netgear router.


According to GRIMM principal security researcher Adam Nichols, who discovered the issue in September, the vulnerability resides in the UPnP function of several Netgear routers.


Also known as [Universal Plug-and-Play](https://en.wikipedia.org/wiki/Universal_Plug_and_Play), this function is used by devices installed on a local network to change the router’s configurations in order to open ports to the public internet — such as gaming devices opening gaming ports or smart assistants opening ports to receive security updates.


Nichols said the GRIMM team discovered a vulnerability in the SUBSCRIBE/UNSUBSCRIBE feature of the UPnP function that allows devices to subscribe/unsubcribe and receive alerts when the router configuration has changed—in order to make sure their ports or settings remain configured on the device.


The GRIMM security researcher said there is a memory stack overflow bug in the code responsible for this feature that allows an attacker to send a malformed package that overflows the memory and then can run code on the device.


Since the UPnP service runs as root and the SUBSCRIBE/UNSUBSCRIBE is not protected by any authentication system, this bug can be easily abused to hijack Netgear routers in their entirety.


The faulty code was found in several Netgear models, according to a list made available by the GRIMM team. In total 61 Netgear models were found to have been impacted.


![Netgear-vulnerable-gear](https://www-therecord.recfut.com/wp-content/uploads/2021/11/Netgear-vulnerable-gear.png)Image: GRIMM
Nichols said that Netgear patched most of the devices last week, but only for models that were still under active firmware maintenance, with others remaining unpatched.


The list of Netgear models that received a fix is available in the official Netgear CVE-2021-34991 advisory [here](https://kb.netgear.com/000064361/Security-Advisory-for-Pre-Authentication-Buffer-Overflow-on-Multiple-Products-PSV-2021-0168). This includes SOHO routers, DSL modems, cable modems, and extenders.


In addition, Nichols also said that on some devices, a previous Netgear security fix had inadvertently blocked the possibility of exploiting their bug, but that the bug was still present in the firmware regardless.


### Netgear has had a tough 2021


Nichols’ findings are the fifth major set of remote code execution bugs that the US networking company patches this year. Similar remote takeover bugs were found in:


* [**March**](https://research.nccgroup.com/2021/03/08/technical-advisory-multiple-vulnerabilities-in-netgear-prosafe-plus-jgs516pe-gs116ev2-switches/)– by security firm NCC Group.
* [**June**](https://www.microsoft.com/security/blog/2021/06/30/microsoft-finds-new-netgear-firmware-vulnerabilities-that-could-lead-to-identity-theft-and-full-system-compromise/)– by Microsoft.
* [**September**](https://therecord.media/demons-cries-authentication-bypass-patched-in-netgear-switches/)– by Polish security researcher Gynvael Coldwind.
* [**September**](https://blog.grimm-co.com/2021/09/mama-always-told-me-not-to-trust.html) – by GRIMM (a different set of bugs).


The GRIMM team released proof-of-concept code to reproduce their vulnerability and exploit [on GitHub](https://github.com/grimm-co/NotQuite0DayFriday/tree/trunk/2021.11.16-netgear-upnp). An in-depth walkthrough of the bug’s technical aspects is also available on the [GRIMM blog](https://blog.grimm-co.com/2021/11/seamlessly-discovering-netgear.html).





#### Tags:
[[Netgear]] [[UPnP]] [[Nichols]] [[The Record]]
