# Netgear Smart Switches Open to Complete Takeover
### The Demon’s Cries, Draconian Fear and Seventh Inferno security bugs are high-severity entryways to corporate networks.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169259)
+ Date: September 7, 2021  4:39 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/07162353/Flames-Devil-Horror-Horns-Demon-5863702-e1631046247502.jpg)
Three severe Netgear vulnerabilities, codenamed Demon’s Cries, Draconian Fear and Seventh Inferno by the researcher that found them, affect 20 of the company’s managed smart switches and could allow an attacker to take them over.


The bugs were [patched](https://kb.netgear.com/000063978/Security-Advisory-for-Multiple-Vulnerabilities-on-Some-Smart-Switches-PSV-2021-0140-PSV-2021-0144-PSV-2021-0145) on Friday with zero technical details made available, but the researcher has now released more details on the first two. Details on the third, Seventh Inferno, will be published after Sept. 13, he said. Netgear tracks the bugs as PSV-2021-0140, PSV-2021-0144 and PSV-2021-0145, but CVEs are pending for all three.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


If exploited, the gear could allow cyberattackers to gain administrative privileges and completely take over the device, gaining the ability to disrupt corporate communications as well as to pivot to move laterally throughout an enterprise network.


**Demon’s Cries Takeover Bug**
------------------------------


The Demon’s Cries bug carries a CVSS severity-rating score of 8.8, making it high severity.


According to the researcher, who goes by “Gynvael Coldwind,” an exploit would allow an authentication bypass, resulting in the attacker accessing an admin’s password and achieving full compromise of the device.


The researcher said that the issue exists within the Netgear Switch Discovery Protocol (NSDP), which is implemented by the sqfs/bin/sccd daemon (hence the flaw’s name).


“The protocol itself is UDP-based and each datagram consists of a 32-byte header, followed by a Type/Length/Value chain, with each TLV consisting of a four-byte header (two bytes Type, two bytes Length), followed by the Value bytes,” Coldwind explained in his posting, [issued Monday](https://gynvael.coldwind.pl/?id=740).


By analyzing Netgear administration tools, Coldwind uncovered that any “set” commands (used to define and determine the values of the system environment) require a password-authentication TLV to be first in the datagram.


“However, the sccd daemon on this device DOES NOT enforce this, i.e. the type 10 TLV can be omitted from the chain and in such case neither the password verification takes place, nor does it seem to be required by any of the ‘set’ TLV handlers,” explained Coldwind.


As an example of how this can be exploited, he noted that a “set” command that changes the password on an account to the one specified in the value portion of the header can be sent – and accepted.


“Sending just this one TLV is enough to change the admin password on the device without knowing the previous password,” he said.


Caveats: An attacker needs to already have a foothold on the same corporate network as the target device in order to exploit the vulnerable system. And, to be pwned, a switch must have Netgear’s Smart Control Center (SCC Control) enabled (which it is by default).


**Draconian Fear Full-Device Compromise**
-----------------------------------------


The second bug carries a 7.4 CVSS rating, making it also high-severity. It’s only exploitable if the attack occurs while an admin is in the process of logging in.


“An attacker with the same IP as a logging-in admin to hijack the session bootstrapping information, giving the attacker full admin access to the device web UI and resulting in a full compromise of the device,” according to Coldwind’s Draconian Fear writeup, [also issued](https://gynvael.coldwind.pl/?id=741) on Monday.


The bug exists because in Netgear’s web UI authentication logic, the browser first sends the login information using the “set.cgi” function, and then polls “get.cgi” to get the session ID. However, Coldwind found that get.cgi doesn’t adequately verify if the polling party is actually the same as the party that sent in the login information, because there’s no session cookie that links the set.cgi and get.cgi requests together.


Thus, to exploit the issue, an attacker on the same IP as the admin can just flood the get.cgi function with requests and snatch the session information when it appears, according to the researcher, who added that the window between get.cgi requests on the browser is one second.


“The obvious limiting factor here is the requirement for the attacker to either have the same IP as the admin (foothold on the same machine with limited privileges, same source NAT IP, etc.) or being able to spoof the IP with various low-level network shenanigans, as well winning a race condition with a one-second window (pretty easy actually),” Coldwind said. “[That one second] allows an attacker to send multiple requests effectively greatly increasing the odds of getting the session information before admin’s browser gets it (in my tests the [proof-of-concept exploit] wins the race nine out of 10 times).”


**Which Netgear Smart Switches Are Affected?**
----------------------------------------------


Coldwind verified the vulnerabilities on the Netgear GS110TPV3 Smart Managed Pro Switch (and others) using firmware version 7.0.6.3 and below. However, the vendor issued an extensive list of affected models [in its advisory](https://kb.netgear.com/000063978/Security-Advisory-for-Multiple-Vulnerabilities-on-Some-Smart-Switches-PSV-2021-0140-PSV-2021-0144-PSV-2021-0145):


Firmware fixes are available for all affected products:


**Netgear Authentication Problems Persist**
-------------------------------------------


Netgear gear has had a bevy of authentication flaws in the past, especially when it comes to the vendor’s routers.


For instance, three firmware flaws in the DGN-2200v1 series router [were disclosed](https://threatpost.com/netgear-authentication-bypass-router-takeover/167469/) in July. They can enable authentication bypass to take over devices and access stored credentials using a side-channel attack.


And last year, researchers [discovered](https://threatpost.com/netgear-zero-day-takeover-routers/156744/) an unpatched zero-day vulnerability in firmware that put [79 Netgear device models](https://www.bleepingcomputer.com/news/security/79-netgear-router-models-risk-full-takeover-due-to-unpatched-bug/) at risk for full takeover. Moreover, the company chose to leave 45 of those models [unpatched](https://threatpost.com/netgear-wont-patch-45-router-models-vulnerable-to-serious-flaw/157977/) because they were outdated or had reached their end of life.


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[Netgear]] [[TLV]] [[Coldwind]] [[IP]] [[get.cgi]] [[Demon’s]] [[said.]] [[ThreatPost]]
