# Netgear SOHO Security Bug Allows RCE, Corporate Attacks
### The issue lies in a parental-control function that’s always enabled by default, even if users don’t configure for child security.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174921)
+ Date: September 22, 2021  3:41 pm
+ Author: Tara Seals


## Article:
A high-severity security bug affecting several Netgear small office/home office (SOHO) routers could allow remote code execution (RCE) via a man-in-the-middle (MiTM) attack.


The bug (CVE-2021-40847) exists in a third-party component that Netgear includes in its firmware, called Circle – it handles the parental controls for the devices, according to researchers at Grimm who discovered the flaw. It rates 8.1 out of 10 on the CVSS 3.0 vulnerability-severity scale.


“Since this code is run as root on the affected routers, exploiting it to obtain RCE is just as damaging as a RCE vulnerability found in the core Netgear firmware,” they said in [an advisory](https://blog.grimm-co.com/2021/09/mama-always-told-me-not-to-trust.html) released Tuesday.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Specifically, the issue lives in the Circle update daemon. Researchers explained that the updating process is insecure, making it possible for attackers to spoof the update server and inject their own bits and bytes into the process.


It should be noted that a prerequisite for exploitation is having the ability to sniff and send network traffic to and from a target router, the advisory said – meaning that adversaries would need to be attached to the same network as the appliance. That can be achieved by compromising a connected device such as a mobile phone or computer prior to initiating the RCE effort.


**Man-in-the-Middle to RCE**
----------------------------


Periodically, the daemon polls a file hosted on an update server via the internet to see if there’s anything new for it to download to the device. That file includes versions, checksums and sizes for the firmware, database and platform components. Circle compares the latest iterations of those things with what’s on the device; if something’s outdated, it will initiate an update.


In a proof-of-concept (PoC) exploit, Grimm initiated an attack using a fake DNS server, configured to respond to Circle’s requests from the router.


“If the router receives the malicious DNS response before the legitimate one, the router will connect to the MitM server instead of Netgear’s update server,” according to the advisory. “While the PoC uses a DNS-spoofing attack, any type of MitM attack could also exploit this vulnerability.”


From there, attackers can serve up a malicious database update that triggers RCE, which can be created by downloading and modifying a legitimate Netgear database update, researchers said.


“This daemon connects to Circle and Netgear to obtain version information and updates to the daemon and its filtering database,” researchers explained. “However, database updates from Netgear are unsigned and downloaded via HTTP. As such, an attacker with the ability to perform a MitM attack on the device can respond to Circle update requests with a specially crafted, compressed database file, the extraction of which gives the attacker the ability to overwrite executable files with attacker-controlled code.”


Notably, the Circle daemon is enabled to run by default, even if users haven’t configured the router to use the parental control features, researchers warned.


“While it doesn’t fix the underlying issue … simply disabling the vulnerable code when Circle is not in use would have prevented exploitation on most devices,” they noted.


**Real-World Attack Scenarios**
-------------------------------


The overwriting capability mentioned above comes from the fact that database updates are extracted to the same folder as the firmware binaries, they said, allowing the latter to be replaced. Unfortunately, those binaries have root privileges, opening the door for dangerous attacks.


“Since the executable files that can be overwritten by this vulnerability are run as root, the highest privileged user in Linux environments, the code executed on behalf of the attacker will be run as root as well,” researchers said.


They added, “With root access on a router, an attacker can read and modify all traffic that is passed through the router. For example, if an employee connects to a corporate network via a compromised router, the router could MitM the connection and read any unencrypted data sent between the user’s device and devices on the corporate network.”


A compromised router could also be used to pivot to more secure environments, Grimm warned.


In one scenario, “the attacker performs some initial reconnaissance to determine the ISP that employees of the target corporation use; the attacker compromises this ISP via some other means (phishing, exploit, etc.); from within the ISP, the attacker will be able to compromise any routers vulnerable to the Circle Parental Control Service vulnerability,” according to the analysis.


Then, using an exploit for a separate vulnerability, such as the recent [PrintNightmare bug,](https://threatpost.com/microsoft-emergency-patch-printnightmare/167578/) the attacker can compromise attached PCs, move laterally into corporate networks, exfiltrate corporate data or launch further attacks like ransomware.


“While this attack chain requires separate exploits, which may be blocked or detected, it does provide an alternative to directly attacking the corporate network which is much harder and more likely to be detected,” researchers noted.


Organizations should pay attention to security for their at-home users, they added.


“As a result of COVID-19 precautions, the number of people working remotely has increased significantly,” the researchers said. “While companies have taken steps to facilitate remote work, employees are usually responsible for managing their own internet connections. In most cases, this takes the form of purchasing or renting a SOHO router or modem. These devices typically aren’t on the radar of corporate security teams, unlike their enterprise-grade brethren.”


**Affected Netgear Devices and Versions**
-----------------------------------------


The below devices and versions are vulnerable; Grimm noted that older versions of all of these likely are as well:


To mitigate the risks to corporate environments posed by vulnerable SOHO routers, users should update their router firmware to the latest versions, which contain patches for CVE-2021-40847. Details can be [found here](https://kb.netgear.com/000064039/Security-Advisory-for-Remote-Code-Execution-on-Some-Routers-PSV-2021-0204).


***Rule #1 of Linux Security:****No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*




#### Tags:
[[Netgear]] [[Linux]] [[RCE]] [[MitM]] [[“While]] [[router,]] [[said.]] [[ThreatPost]]
