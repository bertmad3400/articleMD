# Cybersecurity warning: Realtek flaw exposes dozens of brands to supply chain attacks
### New attacks on IoT devices highlight weakness in the software supply chain.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/realtek-hardware-bugs-expose-dozens-of-brands-to-supply-chain-cyber-attack/)
+ Date: August 26, 2021 -- 10:05 GMT (11:05 BST)
+ Author: Liam Tung


## Article:
Unknown

A recently disclosed flaw in chipsets from Taiwanese semiconductor company Realtek is being targeted by a botnet based on the old IoT malware, Mirai.

German security firm IoT Inspector reports that the Realtek bug, tracked as CVE-2021-35395, [affects over 200 wi-fi and router products from 65 vendors](https://www.iot-inspector.com/blog/advisory-multiple-issues-realtek-sdk-iot-supply-chain/), including Asus, Belkin, China Mobile, Compal, D-Link, LG, Logitec, Netgear, ZTE, and Zyxel. 

The flaw is located in a Realtek software developer kit (SDK) and is currently under attack from a group using a [variant of the IoT malware, Mirai](https://www.zdnet.com/article/mirai-botnet-attack-against-krebsonsecurity-cost-device-owners-300000/), which is designed to function on devices with budget processors and little memory.  

Should an attack be successful, it would give the attacker full control of the wi-fi module and root access to the device's operating system.  


The attacks highlight vulnerabilities in the software supply chain that US president Joe Biden hopes to patch up with [billions of dollars promised this week by Microsoft and Google](https://www.zdnet.com/article/tech-giants-make-cybersecurity-commitments-after-white-house-meeting/). This follows recent [cyberattacks on US critical infrastructure](https://www.zdnet.com/article/microsoft-solarwinds-attack-took-more-than-1000-engineers-to-create/), which have compromised top US cybersecurity firms and classical critical infrastructure providers, such as east coast fuel distributor Colonial Pipeline.

While Mirai poses some threat to information stored on devices such as routers, the greater damage is caused by high-powered distributed denial of service (DDoS) attacks on websites using compromised devices. In 2016, Mirai was used to launch the world's biggest DDoS attack on Dyn -- a domain name service (DNS) provider that matches website names with numerical internet addresses. Oracle [acquired the firm shortly after the Mirai attack.](https://www.zdnet.com/article/oracle-acquires-dns-provider-dyn-to-take-on-amazons-lead-in-the-cloud/) 

Researchers at IoT Inspector found a bug within the Realtek RTL819xD module that allows hackers to gain "complete access to the device, installed operating systems and other network devices". The firm identified multiple vulnerabilities within the SDK.  






Realtek has released a patch, but device brands (OEMs) need to distribute them to end-users on devices that, for the most part, lack a user interface, and therefore can't be used to communicate that a patch is available. Vendors need to analyse their firmware to check for the presence of the vulnerability. 

"Manufacturers using vulnerable Wi-Fi modules are strongly encouraged to check their devices and provide security patches to their users," warned Florian Lukavsky, managing director of IoT Inspector.   

The attacker generally needs to be on the same wi-fi network as the vulnerable device, but IoT Inspector noted that faulty ISP configurations can expose vulnerable devices directly to the internet. 

[Per security firm Recorded Future](https://therecord.media/hundreds-of-thousands-of-realtek-based-devices-under-attack-from-iot-botnet/), IoT security firm SAM said that attackers were observed remotely exploiting [CVE-2021-35395 over the web on August 18](https://securingsam.com/realtek-vulnerabilities-weaponized/).

IoT Inspector notes that Realtek's poor software development practices and lack of testing allowed "dozens of critical security issues to remain untouched in Realtek's codebase for more than a decade".





#### Tags:
[[Realtek]] [[IoT]] [[wi-fi]] [[Mirai]] [[ZDNet]]
