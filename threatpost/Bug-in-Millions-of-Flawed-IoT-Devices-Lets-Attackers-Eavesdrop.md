# Bug in Millions of Flawed IoT Devices Lets Attackers Eavesdrop
### A remote attacker could exploit a critical vulnerability to eavesdrop on live audio & video or take control. The bug is in ThroughTek’s Kalay network, used in 83m devices.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168729)
+ Date: August 17, 2021  12:20 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/17115556/baby-monitor-iot-hacking-01-blog-e1629215769747.jpeg)
Security researchers have discovered a critical flaw that affects tens of millions of internet-of-things (IoT) devices – one that exposes live video and audio streams to eavesdropping threat actors and which could enable attackers to take over control of devices, including security webcams and connected baby monitors.


The flaw, tracked as [CVE-2021-28372](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28372) and [FEYE-2021-0020](https://github.com/fireeye/Vulnerability-Disclosures/blob/master/FEYE-2021-0020/FEYE-2021-0020.md) and assigned a critical CVSS3.1 base score of 9.6, was found in devices connected via [ThroughTek’s Kalay IoT cloud platform](https://www.throughtek.com/overview/).


The [alarm was sounded](https://www.fireeye.com/blog/threat-research/2021/08/mandiant-discloses-critical-vulnerability-affecting-iot-devices.html) on Tuesday by Mandiant, in coordination with the Cybersecurity and Infrastructure Security Agency (CISA) and ThroughTek. Mandiant’s Red Team discovered the vulnerability in late 2020.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“CVE-2021-28372 poses a huge risk to an end user’s security and privacy and should be mitigated appropriately,” according to Mandiant’s post. “Unprotected devices, such as IoT cameras, can be compromised remotely with access to a UID and further attacks are possible depending on the functionality exposed by a device.”


The world has already been inundated with tales of what can happen when these kind of devices are misconfigured or riddled with vulnerabilities, and this just adds to the growing pile of scary headlines. For example, in February, a vulnerability affecting multiple baby monitors was found to [expose hundreds of thousands of live devices](https://threatpost.com/baby-monitors-unauthorized-viewing/163982/), potentially allowing someone to drop in and view a camera’s video stream.


As Mandiant explained, the flaw would enable adversaries “to remotely compromise victim IoT devices, resulting in the ability to listen to live audio, watch real time video data, and compromise device credentials for further attacks based on exposed device functionality. These further attacks could include actions that would allow an adversary to remotely control affected devices.”


In a Tuesday post, researchers Jake Valletta, Erik Barzdukas and Dillon Franke – who discovered the bug – explained that it’s impossible to compile a comprehensive list of companies and products affected, given how the Kalay protocol is integrated by manufacturers and resellers before devices reach consumers. Though they couldn’t come up with a definitive list of affected companies and products that implement the Kalay platform, they strongly advised users of IoT devices “to keep device software and applications up to date and use complex, unique passwords for any accounts associated with these devices.”


Mandiant also recommends that device owners avoid connecting to affected devices from untrusted networks, such as public Wi-Fi: a recommendation that’s already part of wireless best practices, as the National Security Agency (NSA) [recently advised](https://threatpost.com/nsa-warns-public-networks-are-hacker-hotbeds/168268/) in a public service announcement ([PDF](https://media.defense.gov/2021/Jul/29/2002815141/-1/-1/0/CSI_SECURING_WIRELESS_DEVICES_IN_PUBLIC.PDF)).


Kalay: A Newly Unappealing Handshake
------------------------------------


According to ThroughTek, “Kalay” is an indigenous [Dawu](http://www.china.org.cn/english/13602.htm#:~:text=The%20Dawu%20language%20is%20used,was%20a%20non%2DTibetan%20language.) word that means “handshake,” “symbolizing the universal link in an interconnected world.”


ThroughTek implements that handshake – the Kalay protocol – as a software development kit (SDK). The Kalay SDK provides a plug-and-play network to easily connect smart devices with corresponding mobile apps.


The researchers provided an illustration that gives an example of how it works: The figure below shows a typical device registration process and client connection on the Kalay network. In this example, a user remotely accesses their home network’s Kalay-enabled camera on a mobile app from a remote network: for example, a user would view their home camera’s feed while in a coffee shop or on a mobile phone network


How Many Devices Are Affected? Impossible to Say
------------------------------------------------


To get a high-level view of the scope of potentially affected products and companies, researchers pointed to ThroughTek’s advertising, which boasts of supporting upwards of 83 million active devices and more than 1.1 billion monthly connections on the platform. ThroughTek also supports 250 systems-on-a-chip (SOCs): the microchips that contain all the necessary electronic circuits and parts for small consumer electronic devices, such as smartphones or wearable computers.


Mandiant said that affected Kalay products include IoT camera manufacturers, smart baby monitors, and Digital Video Recorder (DVR) products.


Researchers noted that this ThroughTek bug is worse than the critical Nozomi Networks vulnerability disclosed in May: a bug that was already quite severe in that it [laid open millions of connected cameras](https://threatpost.com/millions-connected-cameras-eavesdropping/166950/), leaving them prey to having remote attackers get at camera feeds. But besides eavesdropping, this latest Kalay vulnerability means that devices could be remotely controlled by people who have no business tinkering with other people’s baby monitors, webcams or other IoT gadgets, Mandiant said.


“This latest vulnerability allows attackers to communicate with devices remotely,” researchers explained. “As a result, further attacks could include actions that would allow an adversary to remotely control affected devices and could potentially lead to remote code execution.”


How the Bug Works
-----------------


Mandiant determined that the problem lies in the device registration process, which requires only a device’s 20-byte, uniquely assigned identifier – which they refer to as a UID – to access the network. Mandiant’s testing showed that, typically, the UID is provided by a Kalay-enabled client, such as a mobile app, from a web API hosted by the company that markets and sells a given device.


In order to exploit the vulnerability, an attacker would need both deep knowledge of the Kalay protocol and the ability to generate and send messages. They’d also have to get their hands on those Kalay UIDs, which they could wriggle away via “social engineering or other vulnerabilities in APIs or services that return Kalay UIDs,” the researchers said. As an alternative, Mandiant also investigated brute forcing ThroughTek UIDs, but researchers said that it sucked up too much time and resources.


After they get their hands on the UIDs, an attacker could take over the associated, affected devices. With some knowledge of the Kalay protocol, they’d be able to re-register the UID, overwriting the existing Kalay device on the Kalay servers. Then, whenever the legitimate owner tries to access the device, the UID will be directed to the attacker, in effect leading to hijacking of the connection.


As Mandiant director Jake Valletta told [Wired](https://www.wired.com/story/kalay-iot-bug-video-feeds/), the legitimate device owner would experience a few seconds of lag, but that’s the only difference that would be apparent from their perspective.


After that, the attacker can continue with the connection process in order to steal the device owner’s username and password. The figure below shows what happens when both a victimized device and a malicious device with the same UID exist on the network: Namely, the malicious registration overwrites the existing registration and force the legitimate device’s connections to be re-routed to the attacker’s device.


After that, a threat actor can remotely connect to the victimized device, access audio/visual data and execute remote procedure calls (RPC), Mandiant said. Due to vulnerabilities in the device-implemented RPC interface, this can then lead to “fully remote and complete device compromise,” researchers described. Their enumeration of what makes this possible: “Mandiant observed that the binaries on IoT devices processing Kalay data typically ran as the privileged user root and lacked common binary protections such as Address Space Layout Randomization (“ASLR”), Platform Independent Execution (“PIE”), stack canaries, and NX bits.”


The figure below shows a hypothetical attack using the captured Kalay credentials to stage yet another attack by abusing the vulnerabilities in the Kalay RPC interface:


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/17114402/Screen-Shot-2021-08-17-at-11.43.08-AM-e1629215096109.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/17114402/Screen-Shot-2021-08-17-at-11.43.08-AM-e1629215096109.png)


Mandiant isn’t releasing public exploit code, but it did provide the video below, which demonstrates a proof of concept for CVE-2021-28372.


How to Address the Bug
----------------------


Mandiant “strongly recommends” that companies using the Kalay platform follow the following guidance from ThroughTek and Mandiant:


Mandiant thanked ThroughTek and CISA for their cooperation and support with releasing the advisory and for their “commitment to securing IoT devices globally.”


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Kalay]] [[Mandiant]] [[IoT]] [[ThroughTek]] [[devices,]] [[UID]] [[Mandiant’s]] [[example,]] [[said.]] [[that,]] [[ThreatPost]]
