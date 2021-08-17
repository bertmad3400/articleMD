# Critical bug impacting millions of IoT devices lets hackers spy on you
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/critical-bug-impacting-millions-of-iot-devices-lets-hackers-spy-on-you/)
+ Date: August 17, 2021
+ Author: Ionut Ilascu


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/08/17/Kalay01.jpg)


Security researchers are sounding the alarm on a critical vulnerability affecting tens of millions of devices worldwide connected via ThroughTek’s Kalay IoT cloud platform.


The security issue impacts products from various manufacturers providing video and surveillance solutions as well as home automation IoT systems that use the Kalay network for easy connectin and communication with a corresponding app.


A remote attacker could leverage the bug to gain access to the live audio and video streams, or to take control of the vulnerable device.


### Hijacking device connections


Researchers at Mandiant’s Red Team discovered the vulnerability at the end of 2020 and worked with the U.S. Cybersecurity and Infrastructure Security Agency and ThroughTek to coordinate the disclosure and create mitigation options.


Tracked as CVE-2021-28372, the issue is a device impersonation vulnerability that received a severity score of 9.6 out of 10. It affects the Kalay protocol that is implemented as a software development kit (SDK) that is built into mobile and desktop applications.


Mandiant’s Jake Valletta, Erik Barzdukas, and Dillon Franke looked at ThroughTek’s Kalay protocol and found that registering a device on the Kalay network required only the device’s unique identifier (UID).


Following this lead, the researchers discovered that a Kalay client, such as a mobile app, usually receives the UID from a web API hosted by the vendor of the IoT device.


![Device registration on ThroughTek's Kalay network](https://www.bleepstatic.com/images/news/u/1100723/2021/Vulnerabilities/KalayDeviceReg.gif)


An attacker with the UID of a target system could register on the Kalay network a device they control and receive all client connection attempts.


This would allow them to obtain the login credentials that provide remote access to the victim device audio-video data.


![Impersonating a device on ThroughTek's Kalay network](https://www.bleepstatic.com/images/news/u/1100723/2021/Vulnerabilities/KalayDeviceImpersonation.gif)


The researchers say that this type of access combined with vulnerabilities in device-implemented RPC (remote procedure call) interface can lead to complete device compromise.



“Mandiant observed that the binaries on IoT devices processing Kalay data typically ran as the privileged user root and lacked common binary protections such as Address Space Layout Randomization (“ASLR”), Platform Independent Execution (“PIE”), stack canaries, and NX bits” - [Mandiant](https://www.fireeye.com/blog/threat-research/2021/08/mandiant-discloses-critical-vulnerability-affecting-iot-devices.html)



During their research of this vulnerability, Mandiant researchers were able to develop a functional implementation of the Kalay protocol, which allowed them to discover devices, register them, connect to remote clients, authenticate, and process audio and video data.


They also created proof-of-concept (PoC) exploit code that allowed them to impersonate a device on the Kalay network. A video showing the feat is available below:



By the latest data from ThroughTek, its Kalay platform has more than 83 million active devices and manages over 1 billion connections every month.


### Mitigation options for devs and owners


In a [security advisory](https://www.throughtek.com/please-update-the-sdk-version-to-minimize-the-risk-of-sensitive-information-being-accessed-by-unauthorized-third-party/) published on July 20 for another critical vulnerability in its SDK ([CVE-2021-32934](https://us-cert.cisa.gov/ics/advisories/icsa-21-166-01)), and updated on August 13, ThroughTek provides guidance that customers can follow to mitigate the risks associated with CVE-2021-28372:


* If using ThroughTek SDK v3.1.10 and above, please enable AuthKey and DTLS (Datagram Transport Layer Security) to protect data in transit;
* If using ThroughTek SDK the older versions before v3.1.10, please upgrade library to v3.3.1.0 or v3.4.2.0 and enable AuthKey and DTLS.


Mandiant also recommends reviewing security controls defined on APIs or other services that can return Kalay UIDs.


The researchers note that an attacker exploiting the device impersonation vulnerability would need to be knowledgeable of the Kalay protocol and how messages are being generated and delivered.


Obtaining the UIDs is also a task that requires some effort from the attacker (social engineering, exploiting other vulnerabilities).


What owners of affected devices can do to mitigate the risk is keep their device software and applications updated to the latest version and define complex, unique login passwords.


Furthermore, they should avoid connecting to IoT devices from an untrusted network (e.g. public WiFi).


Because the Kalay platform is used by devices from a large number of manufacturers, it is difficult to create a list with the affected brands.




#### Tags:
[[Kalay]] [[IoT]] [[ThroughTek]] [[Mandiant]] [[SDK]] [[Bleeping Computer]]
