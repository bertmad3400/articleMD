# NUCLEUS:13 TCP security bugs impact critical healthcare devices
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/nucleus-13-tcp-security-bugs-impact-critical-healthcare-devices/)
+ Date: November 9, 2021
+ Author: Ionut Ilascu


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/11/09/NUCLEUS_13.jpg)


Researchers today published details about a suite of 13 vulnerabilities in the Nucleus real-time operating system (RTOS) from Siemens that powers devices used in the medical, industrial, automotive, and aerospace sectors.


Dubbed NUCLEUS:13, the set of flaws affect the Nucleus TCP/IP stack and could be leveraged to obtain remote code execution on vulnerable devices, create a denial-of-service condition, or obtain info that could lead to damaging consequences.


The NUCLEUS:13 vulnerabilities were discovered by researchers at cybersecurity company Forescout and Medigate, a firm that focuses on the security of devices for healthcare providers.


The research is the last part of a larger initiative from Forescout called Project Memoria, which brought together industry peers, universities and research institutes to analyze the security of multiple TCP/IP stacks.


Project Memoria lasted for 18 months and lead to the discovery of 78 vulnerabilities in 14 TCP/IP stacks, presented in studies published  as [AMNESIA:33](https://www.forescout.com/research-labs/amnesia33/), [NUMBER:JACK](https://www.forescout.com/blog/numberjack-forescout-research-labs-finds-nine-isn-generation-vulnerabilities-affecting-tcpip-stacks/), [NAME:WRECK](https://www.bleepingcomputer.com/news/security/name-wreck-dns-vulnerabilities-affect-over-100-million-devices/), and [INFRA:HALT](https://www.bleepingcomputer.com/news/security/infra-halt-security-bugs-impact-critical-industrial-control-devices/).


Another research that aligns with Project Memoria’s goal is [Ripple20](https://www.bleepingcomputer.com/news/security/ripple20-vulnerabilities-affect-iot-devices-across-all-industries/) from security research group JSOF, which uncovered 19 flaws in the proprietary TCP/IP stack from Treck.


### Three remote code execution bugs


A dozen of the NUCLEUS:13 flaws received medium and high severity ratings, the one standing out being [CVE-2021-31886](https://nvd.nist.gov/vuln/detail/CVE-2021-31886), a critical bug affecting the FTP server component that could allow attackers to take control of the vulnerable device.


In a report published today, Forescout notes that the issue is due to the FTP server’s improper validation of the length of the “USER” command. This leads to stack-based buffer overflows that could result in DoS and remote code execution (RCE) conditions.


![NUCLEUS:13 vulnerabilities in the Nucleus TCP/IP stack](https://www.bleepstatic.com/images/news/u/1100723/2021/Vulnerabilities/NUCLEUS13_bugs.jpg)


As seen in the image above, two other high-severity vulnerabilities ([CVE-2021-31887](https://nvd.nist.gov/vuln/detail/CVE-2021-31887) and [CVE-2021-31888](https://nvd.nist.gov/vuln/detail/CVE-2021-31888)) have a potential RCE impact, and both affect the FTP server component.


Forescout note in a blog post announcing a suite of vulnerabilities that the Nucleus RTOS “is deployed in more than 3 billion devices” in healthcare and critical systems.


Based on the company’s visibility, over 5,000 devices are running a vulnerable version of the Nucleus RTOS, most of them in the healthcare sector.


![Devices affected by NUCLEUS:13 vulnerabilities in the Nucleus TCP/IP stack](https://www.bleepstatic.com/images/news/u/1100723/2021/Vulnerabilities/NUCLEUS13_vuln-devices.jpg)


To show how serious NUCLEUS:13 is, Forescout described two hacking scenarios. One targeted a hospital’s building automation to crash a controller that automatically switched on a fan and lights when someone entered a patient’s room.


In the second scenario, the target was a presence sensor part of the railway infrastructure, which detects when a train arrives at the station and controls how long it stops.


By crashing the controller with any of the DoS bugs in the NUCLEUS:13 suite, an attacker could cause the train to run past the station and potentially collide with another train or objects on the track.


Forescout researcher Stanislav Dashevskyi demonstrated the NUCLEUS:13 attacks in the video below



### Mitigating NUCLEUS:13 issues


Siemens has released updates that fix the NUCLEUS:13 vulnerabilities in Nucleus ReadyStart versions 3 (update to v2017.02.4 or later) and 4 (update to v4.1.1 or later version).


An advisory from the U.S. Cybersecurity and Infrastructure Security Agency (CISA) today provides the following general mitigation action:


* Minimize network exposure for all control system devices and/or systems, and ensure that they are not accessible from the Internet.
* Locate control system networks and remote devices behind firewalls, and isolate them from the business network.
* When remote access is required, use secure methods, such as Virtual Private Networks (VPNs), recognizing VPNs may have vulnerabilities and should be updated to the most current version available. Also recognize VPN is only as secure as its connected devices.
* Forescout’s open-source Project Memoria Detector tool can help vendors identify products affected by the NUCLEUS:13 set of vulnerabilities as well as issues uncovered by previous TCP/IP research from the company.


For organizations where patching is not possible at the moment due to the critical nature of the affected devices, Forescout provides the following mitigation strategy:


* Discover and inventory devices running Nucleus using Project Memoria Detector, which uses active fingerprinting to find systems running Nucleus
* Enforce segmentation controls and proper network hygiene; restrict external communication paths and isolate or contain vulnerable devices in zones as a mitigating control if they cannot be patched or until they can be patched
* Monitor progressive patches released by affected device vendors and devise a remediation plan for your vulnerable asset inventory, balancing business risk and business continuity requirements
* Monitor all network traffic for malicious packets that try to exploit known vulnerabilities or possible 0-days. Anomalous and malformed traffic should be blocked, or at least alert its presence to network operators




#### Tags:
[[NUCLEUS:13]] [[Forescout]] [[TCP/IP]] [[FTP]] [[Bleeping Computer]]
