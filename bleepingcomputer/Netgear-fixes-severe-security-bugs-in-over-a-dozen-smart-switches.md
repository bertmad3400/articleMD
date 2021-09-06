# Netgear fixes severe security bugs in over a dozen smart switches
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/netgear-fixes-severe-security-bugs-in-over-a-dozen-smart-switches/)
+ Date: September 6, 2021
+ Author: Ionut Ilascu


## Article:
![Netgear fixes severe vulnerabilities in smart switches](https://www.bleepstatic.com/content/hl-images/2021/09/06/Netgear.jpg)


Netgear has released firmware updates for more than a dozen of its smart switches used on corporate networks to address high-severity vulnerabilities.


The company fixed three security flaw that affect 20 Netgear products, mostly smart switches. Technical details and proof-of-concept (PoC) exploit code for two of the bugs are publicly available.



### Affected Netgear devices


An advisory from Netgear on Friday informs that a new firmware version is available for some of its switches impacted by three security vulnerabilities that received severity scores between 7.4 and 8.8 on a scale of 10.


Netgear identifies the bugs as PSV-2021-0140, PSV-2021-0144, PSV-2021-0145, as tracking numbers have yet to be assigned. Many of the affected products are smart switches, some of them with cloud management capabilities that allows configuring and monitoring them over the web.


* GC108P (latest firmware version: 1.0.8.2)
* GC108PP (latest firmware version: 1.0.8.2)
* GS108Tv3 (latest firmware version: 7.0.7.2)
* GS110TPP (latest firmware version: 7.0.7.2)
* GS110TPv3 (latest firmware version: 7.0.7.2)
* GS110TUP (latest firmware version: 1.0.5.3)
* GS308T (latest firmware version: 1.0.3.2)
* GS310TP (latest firmware version: 1.0.3.2)
* GS710TUP (latest firmware version: 1.0.5.3)
* GS716TP (latest firmware version: 1.0.4.2)
* GS716TPP (latest firmware version: 1.0.4.2)
* GS724TPP (latest firmware version: 2.0.6.3)
* GS724TPv2 (latest firmware version: 2.0.6.3)
* GS728TPPv2 (latest firmware version: 6.0.8.2)
* GS728TPv2 (latest firmware version: 6.0.8.2)
* GS750E (latest firmware version: 1.0.1.10)
* GS752TPP (latest firmware version: 6.0.8.2)
* GS752TPv2 (latest firmware version: 6.0.8.2)
* MS510TXM (latest firmware version: 1.0.4.2)
* MS510TXUP (latest firmware version: 1.0.4.2)


Netgear’s [advisory](https://kb.netgear.com/000063978/Security-Advisory-for-Multiple-Vulnerabilities-on-Some-Smart-Switches-PSV-2021-0140-PSV-2021-0144-PSV-2021-0145) leaves out any technical details about the bugs but “strongly recommends that you download the latest firmware as soon as possible.”


### Exploiting the bugs


Security researcher [Gynvael Coldwind](https://twitter.com/gynvael), who found and reported the vulnerabilities, today explained two of the issues and provided demo exploit code for them.


Coldwind says in his [security report](https://gynvael.coldwind.pl/?lang=en&id=740) that one of the flaws is an authentication bypass that could, under certain conditions, allow an attacker to take control of a vulnerable device.


A prerequisite for exploiting this bug is that the Netgear Smart Control Center (SCC) feature be active. Default configurations have it turned off.


Netgear calculated a severity score of 8.8 (AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) for this vulnerability, noting that an attacker should be on the local network (Attack Vector: Adjacent) to be able to exploit it.


The researcher disagrees and marks the severity of this vulnerability as critical at 9.8. He argues that the specifications for version 3.1 of the Common Vulnerability Scoring System [notes](https://www.first.org/cvss/specification-document#:~:text=network%20should%20be%20used%20even%20if%20the%20attacker%20is%20required%20to%20be%20on%20the%20same%20intranet%20to%20exploit%20the%20vulnerable%20system%20(e.g.%2C%20the%20attacker%20can%20only%20exploit%20the%20vulnerability%20from%20inside%20a%20corporate%20network).) that the Attack Vector: Network (over the internet) should be used even for the intranet attacks:



“Network should be used even if the attacker is required to be on the same intranet to exploit the vulnerable system (e.g., the attacker can only exploit the vulnerability from inside a corporate network).”



However, a remote attacker would need the help of a user on the network (e.g. access a website with malicious code executed through the web browser to target the vulnerable switch) to exploit the flaw. This drops the severity security score to 8.8.


The second vulnerability that [Coldwind detailed](https://gynvael.coldwind.pl/?id=741) today is what he defines as an “authentication hijacking (for lack of a better term).” The description accounts for an attack where a threat actor would need the same IP address as an admin to “hijack the session bootstrapping information.”


As a result, the attacker would have full admin access to the device web user interface, giving them complete control over the device.


Talking to BleepingComputer, the researcher says that this flaw is “more interesting than dangerous” because of the need to hijack an admin’s local IP address.




#### Tags:
[[(latest]] [[version:]] [[Netgear]] [[Bleeping Computer]]
