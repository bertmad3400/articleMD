# Massive Zero-Day Hole Found in Palo Alto Security Appliances
### Researchers have a working exploit for the vulnerability (now patched), which allows for unauthenticated RCE and affects an estimated 70,000+ VPN/firewalls. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176170)
+ Date: November 10, 2021  12:00 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/10115608/vpn-e1636563380116.jpg)
Researchers have developed a working exploit to gain remote code execution (RCE) via a massive vulnerability in a security appliance from Palo Alto Networks (PAN), potentially leaving more than 70,000 vulnerable firewalls with their goods exposed to the internet.


The critical zero day, tracked as [CVE 2021-3064](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-3064) and scoring a CVSS rating of 9.8 out of 10 for vulnerability severity, is in PAN’s [GlobalProtect firewall](https://www.paloaltonetworks.com/products/globalprotect). It allows for unauthenticated RCE on multiple versions of PAN-OS 8.1 prior to 8.1.17, on both physical and virtual firewalls.


Randori researchers said in a [Wednesday post](https://security.paloaltonetworks.com/CVE-2021-3064) that if an attacker successfully exploits the weakness, they can gain a shell on the targeted system, access sensitive configuration data, extract credentials and more.


After that, attackers can dance across a targeted organization, they said: “Once an attacker has control over the firewall, they will have visibility into the internal network and can proceed to move laterally.”


Going by a Shodan search of internet-exposed devices, Randori believes there are “more than 70,000 vulnerable instances exposed on internet-facing assets.”


The Randori Attack Team found the zero day a year ago, developed a working exploit and used it against Randori customers (with authorization) over the past year. Below is the team’s video of the exploit:



Don’t Panic, But Do Patch
-------------------------


Randori has coordinated disclosure with PAN. On Wednesday, PAN published [an advisory](https://security.paloaltonetworks.com/CVE-2021-3064) and an update to patch CVE-2021-3064.


Randori’s also planning to release more technical details on Wednesday, “once the patch has had enough time to soak,” and will issue updates at [@RandoriAttack](https://twitter.com/Randoriattack) on Twitter, according to its writeup.


While Randori is setting aside 30 days before releasing yet more detailed technical information that it usually provides in its attack notes – a grace period for customers to patch or upgrade – it did give some higher-level details.


Vulnerability Chain Details
---------------------------


Randori said that CVE-2021-3064 is a buffer overflow that occurs while parsing user-supplied input into a fixed-length location on the stack. To get to the problematic code, attackers would have to use an HTTP smuggling technique, researchers explained. Otherwise, it’s not reachable externally.


HTTP request smuggling is a technique for interfering with the way a web site processes sequences of HTTP requests that are received from one or more users.


These kinds of vulnerabilities are often critical, as they allow an attacker to bypass security controls, gain unauthorized access to sensitive data and directly compromise other application users. A recent example was [a bug](https://threatpost.com/ibm-critical-remote-code-execution-flaw/164187/) that cropped up in February in Node.js, an open-source, cross-platform JavaScript runtime environment for developing server-side and networking applications that’s used in IBM Planning Analytics.


Exploitation of the buffer overflow done in conjunction with HTTP smuggling together yields RCE under the privileges of the affected component on the firewall device, according to Randori’s analysis. The HTTP smuggling wasn’t given a CVE identifier, as Palo Alto Networks doesn’t consider it a security boundary, they explained.


To exploit the bug, an attacker needs network access to the device on the GlobalProtect service port (default port 443).


“As the affected product is a VPN portal, this port is often accessible over the Internet,” researchers pointed out.


Virtual firewalls are particularly vulnerable, given that they lack Address Space Layout Randomization (ASLR), the researchers said. “On devices with ASLR enabled (which appears to be the case in most hardware devices), exploitation is difficult but possible. On virtualized devices (VM-series firewalls), exploitation is significantly easier due to lack of ASLR and Randori expects public exploits will surface.” When it comes to certain hard device versions with [MIPS-based](https://en.wikipedia.org/wiki/MIPS_architecture_processors) management plane CPUs, Randori researchers haven’t exploited the buffer overflow to achieve controlled code execution, they said, “due to their [big endian architecture](https://www.techtarget.com/searchnetworking/definition/big-endian-and-little-endian#:~:text=Big%2Dendian%20is%20an%20order,the%20sequence)%20is%20stored%20first.).” But they noted that “the overflow is reachable on these devices and can be exploited to limit availability of services.”


They referred to PAN’s [VM-Series](https://www.accyotta.com/palo-alto-networks/pa-vm) of virtualized firewalls, deployed in public and private cloud computing environments and powered by VMware, Cisco, Citrix, KVM, OpenStack, Amazon Web Services, Microsoft and Google as perimeter gateways, IPSec VPN termination points and segmentation gateways. PAN describes the firewalls as being designed to prevent threats from moving from workload to workload.


Randori said that the bug affects firewalls running the 8.1 series of PAN-OS with GlobalProtect enabled (specifically, as noted above, versions < 8.1.17). The company’s red-team researchers have proved exploitation of the vulnerability chain and attained RCE on both physical and virtual firewall products.


There’s no public exploit code available – yet – and there are both PAN’s patch and threat prevention signatures available to block exploitation, Randori said.


Exploit Code Sure to Follow
---------------------------


Randori noted that public exploit code will likely surface, given what tasty targets VPN devices are for malicious actors.


Randori CTO David “moose” Wolpoff has written for Threatpost, explaining why [he loves breaking into security appliances](https://threatpost.com/breaking-into-security-appliances/167584/) and VPNs: After all, they present one convenient lock for attackers to pick, and then presto, they can invade an enterprise.


The Colonial Pipeline ransomware attack is a case in point, Wolpoff recently wrote: As Colonial’s CEO told a Senate committee in June ([PDF](https://www.hsgac.senate.gov/imo/media/doc/Testimony-Blount-2021-06-08.pdf)), attackers were able to compromise the company through a legacy VPN account.


“The account lacked multi-factor authentication (MFA) and wasn’t in active use within the business,” Wolpoff noted. It’s “a scenario unlikely to be unique to the fuel pipeline,” he added.


How Palo Alto Customers Can Mitigate the Threat
-----------------------------------------------


Patching as soon as possible is of course the top recommendation, but Randori offered these mitigation options if that’s not doable:


The ‘Bigger Story’: Ethically Using a Zero Day
----------------------------------------------


Randori pointed out that Wolpoff has blogged about [why zero-days are essential to security](https://www.randori.com/blog/why-zero-days-are-essential-to-security/), and the Palo Alto Networks zero day is a prime example.


“As the threat from zero-days grows, more and more organizations are asking for realistic ways to prepare for and train against unknown threats, which translates to a need for ethical use of zero-days,” the researchers said in their writeup. “When a defender is unable to patch a flaw, they must rely on other controls. Real exploits let them validate those controls, and not simply in a contrived manner. Real exploits let customers scrimmage against the same class of threats they are already facing.”


***Cybersecurity for multi-cloud environments is notoriously challenging. OSquery and CloudQuery is a solid answer. Join Uptycs and Threatpost on Tues., Nov. 16 at 2 p.m. ET for “***[***An Intro to OSquery and CloudQuery***](https://bit.ly/3wf2vTP)***,” a LIVE, interactive conversation with Eric Kaiser, Uptycs’ senior security engineer, about how this open-source tool can help tame security across your organization’s entire campus.***


[***Register NOW***](https://bit.ly/3wf2vTP) ***for the LIVE event and submit questions ahead of time to Threatpost’s Becky Bracken at*** [***becky.bracken@threatpost.com***](mailto:becky.bracken@threatpost.com)***.***




#### Tags:
[[HTTP]] [[Palo]] [[firewalls]] [[VPN]] [[Wolpoff]] [[PAN’s]] [[GlobalProtect]] [[RCE]] [[ThreatPost]]
