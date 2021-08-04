# Security researchers warn of TCP/IP stack flaws in operational technology devices
### Researchers at Forescout disclose INFRA:HALT, a set of 14 security vulnerabilities in TCP/IP stacks commonly used in industrial infrastructure - and organisations are urged to apply the updates.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/security-researchers-warn-of-tcpip-stack-flaws-in-operational-technology-devices/)
+ Date: August 4, 2021 -- 13:54 GMT (14:54 BST)
+ Author: Danny Palmer


## Article:
Unknown

Security vulnerabilities in the communications protocols used by industrial control systems could allow cyber attackers to tamper with or disrupt services, as well access data on the network. 

Dubbed [INFRA:HALT](https://www.forescout.com/research-labs/infra-halt/), the set of 14 security vulnerabilities have been detailed by cybersecurity researchers at Forescout Research Labs and JFrog Security Research, who warn that if left unchecked, the flaws could allow remote code execution, denial of service or even information leaks.

All the vulnerabilities relate to TCP/IP stacks - communications protocols commonly used in connected devices - in NicheStack, used throughout operational technology (OT) and industrial infrastructure.  

Some of the newly uncovered vulnerabilities are more than 20 years old, a common problem in operational technology, which still often runs on protocols developed and produced years ago. Over 200 vendors, including Siemens, use the NicheStack libraries and [users are advised to apply the security patches.](https://www.hcc-embedded.com/support/security-advisories)  

Forescout has [detailed each of the vulnerabilities in a blog post](https://www.forescout.com/blog/new-critical-operational-technology-vulnerabilities-found-on-nichestack/) - they're related to malformed packet processes which allow an attacker to send instructions to read or write on parts of the memory it shouldn't. That can crash the device and disrupt networks, as well as allowing attackers to craft shell code to perform malicious actions, including take control of the device. 

The disclosure of the newly discovered vulnerabilities is the continuation of [Project Memoria](https://www.zdnet.com/article/these-new-vulnerabilities-millions-of-iot-devives-at-risk-so-patch-now/), Forescout's research initiative [examining vulnerabilities in TCP/IP stacks](https://www.zdnet.com/article/this-old-security-vulnerability-left-millions-of-internet-of-things-devices-vulnerable-to-attacks/) and how to mitigate them. The INFRA:HALT vulnerabilities were uncovered because of the ongoing research.  

All versions of NicheStack before version 4.3, including NicheLite, are affected by the vulnerabilities, which have been disclosed to HCC Embedded, which acquired NicheStack in 2016.  






****SEE:**[**Sensor'd enterprise: IoT, ML, and big data**](https://www.zdnet.com/topic/sensord-enterprise-iot-ml-and-big-data/) **(ZDNet special report) |**[**Download the report as a PDF**](https://www.techrepublic.com/resource-library/whitepapers/special-report-iot-and-the-sensor-d-enterprise-free-pdf/?ftag=CMG-01-10aaa1b) **(TechRepublic)****

The full extent of vulnerable OT devices is uncertain, but researchers were able to identify over 6,400 vulnerable devices by using Shodan, the Internet of Things search engine. 

"When you're dealing with operational technology crashing devices and crashing systems is something that can have various serious consequences. There are also remote code execution possibilities  in these, vulnerabilities which would allow the attacker to take control of a device, and not just crash it but make it behave in a way that it's not intended to or use it to pivot within the network," Daniel dos Santos, research manager at Forescout research labs told ZDNet 

For remote code execution, attackers would need to have detailed knowledge of the systems, but crashing the device is a blunt instrument that's easier to use and that could significant consequences, especially if the devices help control or monitor critical infrastructure.  

Forescout and JFrog Security Research contacted HCC Embedded to disclose the vulnerabilities, as well as contacting CERT as part of the coordinated vulnerability disclosure process. HCC Embedded confirmed that Forescout contacted them about the vulnerabilities and [that patches have been released to mitigate them](https://www.hcc-embedded.com/support/security-advisories).  

"We have been fixing these vulnerabilities over the last six months or so and we have released fixes for every customer who maintains their software," Dave Hughes, CEO of HCC Embedded told ZDNet, adding that if environments are properly configured, it's unlikely that attackers could plant code or take control of devices. 

"These are real vulnerabilities, they are weaknesses in the stack. However, most of them are extremely dependent on how you use the software and how you integrate it as to whether you can experience these things. 

"If they've got a security department that understands DNS poisoning and things like that then they will not be vulnerable at all because they've configured things in a safe way," Hughes said.  

Researchers also contacted Coordination agencies including the [CERT](https://www.kb.cert.org/vuls/) Coordination Center, [BSI](https://www.bsi.bund.de/EN/Home/home_node.html) (the German Federal Cyber Security Authority), and [ICS-CERT](https://us-cert.cisa.gov/) (the Industrial Control Systems Cyber Emergency Response Team) about the vulnerabilities. Siemens [has also issued an advisory about the vulnerabilities](https://cert-portal.siemens.com/productcert/pdf/ssa-789208.pdf) – although only four of the vulnerabilities affect Siemens products.  

To help protect operational technology from any kind of cyber attacks, researchers at Forescout recommend that network segmentation is put in place, so operational technology which doesn't need to be exposed to the internet can't be remotely discovered – and technology which doesn't need to be connected to the internet at all is on a separate, air-gapped network. 

Forescout has released an [open-source script](https://github.com/Forescout/project-memoria-detector) to detect devices running NicheStack to help provide visibility onto networks – and help protect them.  

**MORE ON CYBERSECURITY**

* [**The key to stopping cyberattacks? Understanding your own systems before the hackers strike**](https://www.zdnet.com/article/the-key-to-stopping-cyberattacks-understanding-your-own-systems-before-the-hackers-strike/)
* **[Manufacturing is becoming a major target for ransomware attacks](https://www.zdnet.com/article/manufacturing-is-becoming-a-major-target-for-ransomware-attacks/)**
* [**Colonial Pipeline hack exposes cracks in US energy defense against cyberattacks**](https://www.cnet.com/tech/services-and-software/colonial-pipeline-hack-exposes-cracks-in-us-energy-defense-against-cyberattacks/)
* [**Ransomware gangs are taking aim at 'soft target' industrial control systems**](https://www.zdnet.com/article/ransomware-gangs-are-taking-aim-at-soft-target-industrial-control-systems/)
* **[MITRE announces first evaluations of cybersecurity tools for industrial control systems](https://www.zdnet.com/article/mitre-announces-first-evaluations-of-industrial-control-systems/)**





#### Tags:
[[Forescout]] [[NicheStack]] [[HCC]] [[them.]] [[vulnerabilities,]] [[ZDNet]]
