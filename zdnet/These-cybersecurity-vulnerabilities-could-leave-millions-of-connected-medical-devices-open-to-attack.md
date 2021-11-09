# These cybersecurity vulnerabilities could leave millions of connected medical devices open to attack
### Cybersecurity researchers at Forescout detail Nucleus:13, a set of vulnerabilities in TCP/IP stacks that could allow attackers to launch denial of service attacks and interfere with devices.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/these-cybersecurity-vulnerabilities-could-leave-millions-of-connected-medical-devices-open-to-attack/)
+ Date: November 9, 2021
+ Author: Danny Palmer


## Article:
Unknown

Critical vulnerabilities in millions of connected devices used in hospital networks could allow attackers to disrupt medical equipment and patient monitors, as well as [Internet of Things devices](https://www.zdnet.com/article/what-is-the-internet-of-things-everything-you-need-to-know-about-the-iot-right-now/) that control systems and equipment throughout facilities, such as lighting and ventilation systems.


The vulnerable TCP/IP stacks – communications protocols commonly used in connected devices – are also deployed in other industries, including the industrial sector and the automotive industry. 

[The 13 newly disclosed vulnerabilities](https://www.forescout.com/blog/new-critical-vulnerabilities-found-on-nucleus-tcp-ip-stack/) in Nucleus Net TCP/IP stacks have been detailed by cybersecurity researchers at Forescout and Medigate. Dubbed Nucleus:13, the findings represent the final part of Project Memoria, [a](https://www.zdnet.com/article/this-old-security-vulnerability-left-millions-of-internet-of-things-devices-vulnerable-to-attacks/)[n initiative examining vulnerabilities in TCP/IP stacks used in connected devices and how to mitigate them](https://www.zdnet.com/article/this-old-security-vulnerability-left-millions-of-internet-of-things-devices-vulnerable-to-attacks/).

**SEE:**[**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/)**(ZDNet special report)**

The vulnerabilities could be present in millions of devices based around Nucleus TCP/IP stacks and could allow attackers to engage in remote code execution, denial of service attacks and even leak data – although researchers can't say for certain if they've actively been exploited by cyber criminals.

Now owned by Siemens, the Nucleus TCP/IP stack was originally released in 1993 and is still widely used in critical safety devices, particularly in hospitals and the healthcare industry where they're used in anaesthesia machines, patient monitors and other devices, as well as for building automation systems controlling lighting and ventilation.

Of the three critical vulnerabilities identified by researchers, CVE-2021-31886 poses the greatest threat, with a [Common Vulnerability Scoring System](https://www.zdnet.com/article/the-25-most-dangerous-software-vulnerabilities-to-watch-out-for/) (CVSS) score of 10 out of 10. It's a vulnerability in (File Transfer Protocol) FTP servers that doesn't properly validate the length of user commands, leading to stack-based buffer overflows that can be abused for denial-of-service and remote code execution.






The remaining two critical vulnerabilities both have a CVSS score of 9.9. CVE-2021-31887 is a vulnerability in FTP servers that doesn't properly validate the length of PWD or XPWD FTP server commands, while CVE-2021-31888 is a vulnerability that occurs when the FTP server doesn't properly validate the length of MKD or XMKD FTP commands. Both can result in stack-based buffer overflows, allowing attackers to begin denial-of-service attacks or remotely launch code.

Because the stacks are so common, they are easy to identify and target. It's also possible to find some of the connected devices on [IoT search engine Shodan](https://www.zdnet.com/article/shodan-the-iot-search-engine-which-shows-us-sleeping-kids-and-how-we-throw-away-our-privacy/) – and if they are publicly facing the internet, it's possible to launch remote attacks. This is why researchers decided to examine them specifically.

"We found some promotional material for the stack that mentions using this for medical applications," Daniel dos Santos, research manager at Forescout Research Labs, told ZDNet. "Then when you look at some of the data promoting medical devices, they mention the use of the stack directly." 

Attackers would need to jump through a number of steps, detailed extensively in the paper, to fully exploit the vulnerabilities. But, as long as they exist, that potential is there – along with the potential for disruption. In hospitals, not only could this affect machines used for patient care, systems in the building such as alarms, lighting and ventilation could be affected.

Organisations are recommended to apply the [available security patches released by Siemens](https://cert-portal.siemens.com/productcert/pdf/ssa-044112.pdf) in order to mitigate the threat. 

"All vulnerabilities that are being disclosed on Nov 9th have been fixed in the corresponding latest fix releases of active Nucleus version lines," a Siemens spokesperson told ZDNet. 

Researchers also suggest that networks should be segmented in order to limit the exposure of any devices or software that could contain vulnerabilities, but can't be patched.

"Make sure that you know your network, so even if devices are not patched and you know that probabilities exist, you can still live with a network configuration that lets you sleep at night," said dos Santos.


"The main thing is network segmentation and being able to know and to make sure that devices that are potentially vulnerable and maybe can't be patched are contained, and can only talk to other devices they're allowed to."

****SEE:****[****Sensor'd enterprise: IoT, ML, and big data****](https://www.zdnet.com/topic/sensord-enterprise-iot-ml-and-big-data/)****(ZDNet special report)****

Nucleus:13 represents the final part of Forescout's Project Memoria, which has [worked to uncover and, when possible, help to patch security vulnerabilities in devices](https://www.zdnet.com/article/security-researchers-warn-of-tcpip-stack-flaws-in-operational-technology-devices/), which in some cases are decades old – designed at a time far before the rise of the Internet of Things was even predicted.

"Many of these pieces of software are 20, 30 or even more years old. Unfortunately, that means that they were designed in a different age for different requirements and they're just not up to date with security nowadays," said dos Santos.

"Many of these vulnerabilities are kind of predictable in the sense that they're repeated over and over again over different pieces of software," he added.

The aim of the year-long project has been to showcase the vulnerabilities in older devices and to push for connected devices to be built with IoT security in mind – and to prevent the same old vulnerabilities causing problems moving forward, particularly as the use of IoT devices continues to grow.

"The expanded adoption of these types of technology by every type of organization, and their deep integration into critical business operations, will only increase their value for attackers over the long term," warns the report.

### **MORE ON CYBERSECURITY**

* [**IoT: Security researchers warn of vulnerabilities in hospital pneumatic tube systems**](https://www.zdnet.com/article/iot-security-researchers-warn-of-vulnerabilities-in-hospital-pneumatic-tube-systems/)
* [**Critical IoT security camera vulnerability allows attackers to remotely watch live video - and gain access to networks**](https://www.zdnet.com/article/critical-iot-security-camera-vulnerability-allows-attackers-to-remotely-watch-live-video-and-gain-access-to-networks/)
* **[**This old security vulnerability left millions of Internet of Things devices vulnerable to attacks**](https://www.zdnet.com/article/this-old-security-vulnerability-left-millions-of-internet-of-things-devices-vulnerable-to-attacks/)**
* [**Security researchers warn of TCP/IP stack flaws in operational technology devices**](https://www.zdnet.com/article/security-researchers-warn-of-tcpip-stack-flaws-in-operational-technology-devices/)
* [**The IoT is getting a lot bigger, but security is still getting left behind**](https://www.zdnet.com/article/the-iot-is-getting-a-lot-bigger-but-security-is-still-getting-left-behind/)





#### Tags:
[[TCP/IP]] [[FTP]] [[IoT]] [[devices,]] [[Forescout]] [[ZDNet]]
