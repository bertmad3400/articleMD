# Comcast RF Attack Leveraged Remotes for Surveillance
### IoT vulnerabilities turned the remote into a listening device, researchers found, which impacted 18 million Xfinity customers.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169133)
+ Date: September 2, 2021  7:03 am
+ Author: Becky Bracken


## Article:
More details about a now-patched vulnerability in Comcast’s XR11 voice remotes have emerged, which would have made it easy for a threat actor to intercept radio frequency (RF) communications between the remote and the set-top box, effectively turning the remote into a surveillance device.


The XR11 remotes are some of the most common around, with more than 18 million scattered across homes in the U.S. A man-in-the-middle attack conducted by researchers at Guardicore, [dubbed](https://www.guardicore.com/blog/wareztheremote-turning-remotes-into-listening-devices/) “WarezTheRemote,” allowed the team to listen in on conversations from up to 65 feet away.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The flaw [was disclosed](https://threatpost.com/comcast-tv-remote-homes-snooping/159899/) in October and has since been mitigated by Comcast, but researchers at AT&T Cybersecurity [recently broke down](https://cybersecurity.att.com/blogs/security-essentials/hackers-leverage-rf-to-compromise-smart-tv-remotes) more details on the bug. It also highlights the stakes in deploying armies of seemingly benign internet-of-everything (IoT) devices without basic security to protect them from being weaponized and abused by cybercriminals.


**WarezTheRemote Vulnerability**
--------------------------------


Voice-controlled remotes like the XR11 are handy because they allow a user to push a button and just tell the TV what to do. To make it even easier to use, the old-school infrared control has been swapped out for RF controls, so users don’t have to have the device within line of sight of the set-top box to switch the channel.![Comcast remote hack](https://media.threatpost.com/wp-content/uploads/sites/103/2020/10/06153627/comcast-remote-224x300.png)


“The combination of recording capabilities with RF-based communication led us to believe that the XR11 can be of particular interest to an attacker: RF enables contact with the remote from afar, which makes for a larger attack surface than a remote control would otherwise have, and the recording capability makes it a high-value target,” the Guardicore researchers wrote.


The analysts then reverse-engineered the remote firmware and found that only incoming RF packets were encrypted, leaving the responses to the requests exposed.


**RF Comms Encryption Bug**
---------------------------


“This means that if an attacker within RF range had responded to outgoing (encrypted) requests from the remote in plaintext, the remote would have accepted the spurious responses,” Guardicore’s report explained. “Because of this bug, if an attacker had guessed the contents of a request from the remote, they could have easily formulated a malicious response to that request.”


That means an attacker could trick the remote into thinking they were the set-top box to update the device’s firmware, they explained, which the device is set up to automatically look for every 24 hours.


![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/02063603/remote-attack-diagram.png)


“As this attack literally flashes the remote’s firmware, we decided to name it WarezTheRemote,” the team said. “We implemented a full proof-of-concept of a malicious firmware upgrade using this method.”


Once inside the firmware, the team found the code that controls the device’s recorder.


“In normal circumstances, all communication between the remote and the box is initiated by the remote – this is a common power-saving strategy for low-energy devices, since it enables them to power off whenever they are not used,” the report said. “This means that we can’t directly send a ‘start recording’ command to the remote from the outside – we can only do it in response to a query from the remote.”


To work around that challenge, they updated the firmware to send out a query every minute, rather than every 24 hours, they explained. During the test, Guardicore was able to record for 10-minute intervals, they said.


The ability to start and stop recording would help attackers preserve battery power over an extended period, the analysts pointed out.


Ultimately, they were able to record conversations from up to 65 feet away the report said.


“We didn’t push this to the limit, but we were easily able to push firmware to the remote around 65 feet away from outside the apartment it was in,” they wrote. “This is the alarming part – it conjures up the famous ‘van parked outside’ scene in every espionage film in recent memory.”


**More Details**
----------------


The details of how Guardicore managed to achieve the attack were laid out further recently, AT&T noted, explaining that the remote communicates with the cable box via encrypted, short-range radio signals — which makes intercepting them all but impossible if both devices – the cable box and the remote – are working properly.


“Using a different form of attack – not described in the paper, but likely to be an [SQL injection](https://cybersecurity.att.com/blogs/security-essentials/what-is-web-application-security) over Wi-Fi – they were able to trigger a crash in the cable box,” according to AT&T’s writeup/ “During the period that the box was down, the remote was vulnerable.”


The researchers could then invoke the aforementioned network node that mimicked the cable box the remote was supposed to be communicating with. And of course, besides a quick redundancy check, the remote didn’t check the firmware being loaded at all.


“The hackers took advantage of this process and created a script that would attempt to slip a modified packet into the update stream,” according to AT&T. “This packet did not actually include the recording command, but rather told the remote to change its update checks from once every 24 hours to once per minute. Then, they uploaded the code needed to start recording voices in small packets, so they would not be detected.”


In the end, the TV remote automatically recorded voices around it, and then sent these to the researchers via an encrypted file.


The attack, “it should be said, is scary,” according to AT&T, though researchers acknowledged that an in-the-wild attack would be unlikely.


**Independent Researchers Driving RF Security Improvements**
------------------------------------------------------------


Comcast has made all the necessary mitigations and Guardicore reported there are no currently vulnerable devices but pointed out that up until remediation was pushed out, every one of these remotes was open to this kind of attack.


“Besides leaving out the batteries, there was no effective way to mitigate it, either,” the report added.


Similarly, [RF vulnerabilities](https://threatpost.com/fortress-home-security-remote-disarmament/169069/) exposed this week in the Fortress S03 WiFi Home Security System could allow cybercriminals to remotely disarm the alarm system remain unpatched.


And just last month a [flaw in ThroughTek’s Kalay network](https://threatpost.com/bug-iot-millions-devices-attackers-eavesdrop/168729/), connected to 83 million devices like baby monitors and security cameras left them open to breach and eavesdropping by threat actors.


While the security community grapples with these types of revelations, Jake Williams from BreachQuest said its independent researchers like Guardicore that are educating users and pushing IoT device manufacturers to prioritize security.


“Consumers need to realize that everything that has a microphone can potentially be turned into a listening device,” he told Threatpost by email. “When Amazon released the Echo, many researchers screamed ‘the sky is falling’ but of course those worst fears never came to pass. This has likely led to some complacency among the public.”


But Williams added those security community concerns drove Amazon to take security seriously.


“Amazon expended significant resources on privacy and security that most producing devices with microphones device have not,” Williams said. “As we’ve seen with IP-based security cameras before, much of this hardware is a race to the bottom. This research from Guardicore highlights why independent security research is so important for consumers.”


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Guardicore]] [[said.]] [[XR11]] [[remotes]] [[“This]] [[set-top]] [[firmware,]] [[ThreatPost]]
