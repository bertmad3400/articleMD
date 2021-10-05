# IP Surveillance Bugs in Axis Gear Allow RCE, Data Theft
### Three security vulnerabilities in Axis video products could open up the door to a bevy of different cyberattacks on businesses.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175350)
+ Date: October 5, 2021  5:09 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/05163647/video-communications.jpg)
Three vulnerabilities in the IP video-surveillance systems created by Axis Communications could allow arbitrary code execution, among other attacks.


That’s according to Nozomi Networks Labs, whose researchers examined the company’s Axis Companion Recorder, a compact network video recorder (NVR) that stores IP surveillance video coming from attached cameras (it can support up to eight at one time).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


They found that the three bugs (CVE-2021-31986, CVE-2021-31987, CVE-2021-31988) turn out to affect all Axis devices that run the company’s embedded Axis OS.


The bugs are as follows:


“All attacks require that a victim, while logged into the device, visits a specifically crafted webpage or clicks on a malicious link,” Nozomi researchers told Threatpost. “There are several ways this could happen (phishing, watering holes, etc.) which we do not delve into in this analysis. But it does not take a great deal of expertise, as some of these attacks are well-known types of attacks.”


**CVE-2021-31986: Heap-based Buffer Overflow**
----------------------------------------------


The first vulnerability is in the read callback function, according to Nozomi, which is called by the “libcurl” function to read data in order to upload or post data to a server or peer.


“Notably, the read callback function was noticed failing to verify that no more than ‘size’ multiplied by ‘nitems’ number of bytes are copied in the libcurl destination buffer (on our device, 64 KB),” according to a writeup, [posted on Tuesday](https://www.nozominetworks.com/blog/new-axis-os-security-research-aided-by-transparent-design/). “Among the copied bytes, the read callback function copies in the libcurl destination buffer the ‘to,’ ‘from,’ ‘subject’ and ‘body’ HTTP parameters of the request to the endpoint.”


This request is normally a GET request that’s limited to less than 10,000 characters: too few to trigger the overflow. However, researchers discovered that they could also send POST requests to the endpoint, which are not restricted by any limit at all.


In addition, the requests don’t have any protections against cross-site request forgery (CSRF) attacks, researchers added, which paves the way for exploitation without authentication.


As a result, an external remote attacker with a successful social-engineering approach is able to trigger memory corruption on the device and possibly execute arbitrary code.


“The first vulnerability relies on a user downloading malicious code to the Axis recorder by just visiting a specifically crafted page while logged in to the Companion application,” Nozomi researchers told Threatpost. “This could open a range of attacks, such as taking over the camera operations, offloading data, or operating other malicious software against the network.”


**CVE-2021-31987: Improper Recipient Validation**
-------------------------------------------------


The other two vulnerabilities rely on test features in the Axis OS that are used for network communication using the standard protocols HTTP, SMTP and TCP.


The second vulnerability specifically arises because of failings in certain blocklist-based security checks, which are used to make sure that HTTP, email and TCP recipients can’t access adjacent network services that are exposed via a local web server.


These “blocklist-based security checks to impede interactions with localhost-exposed network services…could be circumvented with known bypasses or were incomplete,” according to the writeup. “[We] confirmed the feasibility of sending requests to localhost-exposed services.”


To exploit the bug, a user need only click on a malicious link or again visit a specific webpage while logged in. An external remote attacker can then interact with internal-only services running on the device, obtaining access to restricted information, researchers told Threatpost.


“Once you can access network services on the localhost, you are directly interacting with internal software that, as such, was not designed to be robust and secure in the same way as [an] externally reachable one,” they said. “Many things could be possible, from the immediate unauthorized access of confidential internal information, to the execution of exploits against internal unprotected services, to further compromising the system.”


How this would manifest to the company being attacked could vary depending on the attacker’s intent, they added: “There are a range of possibilities and threats.”


**CVE-2021-31988: SMTP Header Injection**
-----------------------------------------


The third vulnerability allows SMTP header injection within emails and messaging, thanks to an absence of input validation functions, according to Nozomi.


“As with many other network video recorders, Axis products allow users to set up notifications in case of events, such as motion detection or system malfunctioning,” Nozomi researchers explained to Threatpost. “Although simple features, if not adequately protected they also can be leveraged to gain access to the device.”


SMTP header injection allows attackers to inject additional headers with arbitrary values into emails, through which they could send copies of emails to third parties, spread malware, deliver phishing attacks, alter the content of emails, disclose information and more.


In this case, the issue is located in the SMTP test functionality, the firm noted.


“Again, by convincing a victim-user to visit a specifically crafted web page while logged into the Companion Recorder web application, an external remote attacker can trick the device into sending malicious emails to other users with arbitrary SMTP header values,” researchers explained to Threatpost.


**IoT Insecurity Bonanza**
--------------------------


Connected camera ecosystems and other internet-of-things gear are often in the crosshairs of both vulnerability hunters and attackers.


The flaws are endemic and tend to have widespread affects: In June, for instance, Nozomi researchers [found that](https://threatpost.com/millions-connected-cameras-eavesdropping/166950/) millions of connected security and home cameras contained a critical software vulnerability that can allow remote attackers to tap into video feeds. The critical bug had been introduced via a supply-chain component from ThroughTek that’s used by several original equipment manufacturers (OEMs) of security cameras – along with makers of IoT devices like baby- and pet-monitoring cameras and robotic and battery devices.


Perhaps it’s no wonder that the first half of 2021 [saw 1.5 billion attacks](https://threatpost.com/iot-attacks-doubling/169224/) on smart devices, with attackers looking to steal data, mine cryptocurrency or build botnets. That represented a more than 100 percent growth in IoT cyberattacks, according to a Kaspersky analysis of its telemetry.


The best way to stay protected is, of course, to patch.


**How to Protect Your Environment from Axis Attacks**
-----------------------------------------------------


Axis is in the process of [releasing patches](https://help.axis.com/axis-os#upcoming-current-releases) for all affected devices, it said, which could add up to millions of vulnerable endpoints, given Axis’ role as a [market leader](https://www.sptnews.ca/axis-leader-in-network-and-security-cameras-nabs-top-spot-in-video-encoders-also-study-2636/). The updates are as follows:


***CVE-2021-31986 and CVE-2021-31988:***


***CVE-2021-31987:***


“Axis devices not included in these tracks and still under support will receive a patch according to their planned maintenance & release schedule,” the analysis noted.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





#### Tags:
[[SMTP]] [[Nozomi]] [[Threatpost.]] [[device,]] [[attacks,]] [[emails]] [[IoT]] [[ThreatPost]]
