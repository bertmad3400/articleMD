# Fortress Home Security Open to Remote Disarmament
### A pair of unpatched security vulnerabilities can allow unauthenticated cyberattackers to turn off window, door and motion-sensor monitoring.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169069)
+ Date: August 31, 2021  4:35 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/31151918/fortress-scaled-e1630437615681.jpg)
A pair of vulnerabilities in the Fortress S03 WiFi Home Security System could allow cyberattackers to remotely disarm the system, leaving homes open to unlawful entry.


The Fortress platform [is a consumer-grade](https://www.fortresssecuritystore.com/home-wifi-security-system-s03.html) home security system that allows users to mix and match various sensors, [IP cameras](https://threatpost.com/fbi-warn-home-security-devices-swatting/162678/) and accessories, connecting them via Wi-Fi to create a personalized security system. RF fobs are used for system control, arming and disarming monitors on doors, windows and motion detectors.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


According to Rapid7 researcher Arvind Vishwakarma, who discovered the bugs, the “vulnerabilities could result in unauthorized access to control or modify system behavior, and access to unencrypted information in storage or in transit.”


Both bugs remain unpatched.


**Disarming Home Security Systems**
-----------------------------------


The first vulnerability, tracked as CVE-2021-39276, is due to an insecure cloud API deployment, he said in a Tuesday post. Unauthenticated users can trivially exploit it to retrieve a secret that can then be used to alter the system’s functionality remotely. To disarm an alarm system, attackers can send a specially crafted unauthenticated POST to the API.


“If a malicious actor knows a user’s email address, they can use it to query the cloud-based API to return an International Mobile Equipment Identity (IMEI) number, which appears to also serve as the device’s serial number,” Vishwakarma said. “With a device IMEI number and the user’s email address, it is then possible for a malicious actor to make changes to the system, including disarming its alarm.”


According to Rapid7, it’s important to note that the effort to exploit this may be too much for random, opportunistic home invaders, but in a stalker/restraining order type of situation where the person already knows the target and is in possession of an email address, the urgency to mitigate the problem increases, given the potential for physical violence.


“The likelihood of exploitation of these issues is pretty low,” Tod Beardsley, director of research at Rapid7, told Threatpost. “An opportunistic home invader is not likely to be a cybersecurity expert, after all. However, I am concerned about a scenario where the attacker already knows the victim well, or at least, well enough to know their email address, which is all that is really required to disable these devices from over the internet using CVE-2021-39276.”


**An RF Weakness**
------------------


The second issue, tracked as CVE-2021-39277, involves the RF signals used to communicate between the key fobs, door/window contact sensors and the Fortress Console, which are sent in the 433 MHz band. Specifically, anyone within RF signal range could capture and replay RF signals to alter systems behavior, resulting in disarmament.


“When a radio-controlled device has not properly implemented encryption or rotating key protections, this can allow an attacker to capture command-and-control signals over the air and then replay those radio signals in order to perform a function on an associated device,” according to Vishwakarma.


In a proof-of-concept exploit, researchers used a software-defined-radio (SDR) device to capture normal operations of the device’s “arm” and “disarm” commands. Then, replaying the captured RF signal communication command would arm and disarm the system without further user interaction.


An exploit requires an attacker to be within physical range, staking out the property and waiting for the victim to use an RF-controlled device on the system – no prior knowledge of the victim is necessary.


To exploit the RF weakness, “the attacker would need to be both reasonably conversant in SDR in order to capture and replay the signals, and be within reasonable radio range,” Beardsley told Threatpost. “What that range is would depend on the sensitivity of the gear being used, but typically this sort of eavesdropping requires line of sight and pretty close proximity – across the street or so.”


**How to Protect Against Fortress Home Security Attacks**
---------------------------------------------------------


As mentioned, there is, unfortunately, no firmware update available for either vulnerability. The vendor closed the ticket that Rapid7 opened on the bugs without comment, and didn’t respond to researchers’ follow-ups.


“In the past, we’ve seen that vendors that are unresponsive prior to disclosure tend to respond after disclosure, and tend to address these issues pretty quickly,” Beardsley said. “I’m hopeful that’ll be the case with this issue.”


There is, however, a workaround for the first issue. Because an attack requires the system’s email address, “we suggest registering the device with a secret, one-time use email address, that can function as a sort of weak password,” Beardsley told Threatpost. “Absent an authentication update from the vendor, I feel like this is an okay workaround.”


For CVE-2021-39277, there’s “very little a user can do to mitigate the effects of the RF replay issues absent a firmware update to enforce cryptographic controls on RF signals,” according to the post. Rapid7 advised that users could avoid using key fobs and other RF devices linked to Fortress to avoid an attack.


This is just the latest vulnerabilities to be found in internet of things (IoT) devices, pointing out a continuing need for security by design on the part of hardware vendors.


“A proper cloud infrastructure can greatly benefit IoT security by enabling automatic updates and insulating users from many local security threats, but it can also magnify the impact of vendor programming errors,” Craig Young, principal security researcher at Tripwire, said via email. “Whereas a vulnerability within an individual device is generally exploited by a nearby attacker, vulnerabilities within a vendor infrastructure can expose all users at once.”


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[address,]] [[system,]] [[Rapid7]] [[Threatpost.]] [[Beardsley]] [[ThreatPost]]
