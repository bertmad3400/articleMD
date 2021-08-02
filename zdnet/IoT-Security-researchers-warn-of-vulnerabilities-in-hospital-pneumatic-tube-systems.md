# IoT: Security researchers warn of vulnerabilities in hospital pneumatic tube systems
### PwnedPiper vulnerabilities affect pneumatic tube system (PTS) stations used throughout thousands of hospitial networks - and attackers could use them to crash systems, deliver ransomware and steal data, warn security researchers, so patch now.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/iot-security-researchers-warn-of-vulnerabilities-in-hospital-pneumatic-tube-systems/)
+ Date: August 2, 2021 -- 11:20 GMT (12:20 BST)
+ Author: Danny Palmer


## Article:
Unknown

Security researchers have detailed vulnerabilities in the system controlling the pneumatic tube networks used in thousands of hospitals around the world, which could allow hackers to disrupt the services or potentially launch ransomware attacks.

The series of vulnerabilities have been discovered in Nexus Control Panel, which powers current models of Translogic's pneumatic tube system (PTS) stations by Swisslog Healthcare. The tubes allow staff to send patient test samples and medication around the hospital and are a key part of providing care to patients. 


Dubbed PwnedPiper, the nine security vulnerabilities [have been detailed by cybersecurity researchers at Armis](https://www.armis.com/research/pwnedpiper) ahead of a [presentation on the findings at Black Hat USA](https://www.blackhat.com/us-21/briefings/schedule/index.html#a-hole-in-the-tube-uncovering-vulnerabilities-in-critical-infrastructure-of-healthcare-facilities-23546).  

**SEE:**[**Cybersecurity: Let's get tactical**](https://www.zdnet.com/topic/cybersecurity-lets-get-tactical/)**(ZDNet/TechRepublic special feature) |**[**Download the free PDF version**](https://www.techrepublic.com/resource-library/whitepapers/cybersecurity-let-s-get-tactical-free-pdf/?ftag=CMG-01-10aaa1b)**(TechRepublic)**

They include hard-coded passwords, a privilege escalation vulnerability, memory corruption bugs that can lead to remote-code-execution and denial of service and a design flaw in which firmware upgrades on the Nexus Control Panel are unencrypted and don't require any cryptographic signature, which could allow an attacker to gain unauthenticated remote-code execution privileges by initiating a firmware update procedure while also maintaining persistence on the device.

"It was surprisingly easy to find these vulnerabilities; too easy, I would say. Although this device has a crucial function in hospitals for the critical infrastructure, the type of vulnerabilities that we found are similar to stuff that you would find on an average IoT device," Ben Seri, VP of research at Armis, told ZDNet.  

To get to a Nexus Control Panel, an attacker would need some access to the network via a [phishing attack](https://www.zdnet.com/article/what-is-phishing-how-to-protect-yourself-from-scam-emails-and-more/) or [breached remote desktop credentials](https://www.zdnet.com/article/big-jump-in-rdp-attacks-as-hackers-target-staff-working-from-home/). 






According to Armis, the infrastructure is used in more than 3,000 hospitals worldwide, including 2,300 in the United States. 

Researchers warn that by exploiting vulnerabilities in these systems, attackers could gain control over the tube network.

It could also provide attackers with the ability to exploit the escalation of privileges enabled by the vulnerabilities to gain access to other sections of the network to the extent they could launch a [ransomware attack](https://www.zdnet.com/article/ransomware-an-executive-guide-to-one-of-the-biggest-menaces-on-the-web/) against the hospital network.

"It wasn't difficult to find vulnerabilities here. It's just the system that is hidden in plain sight. You don't think about it and, normally, you don't connect it being related to any critical functions – it's a lack of knowledge of this area which leads to vulnerabilities," said Seri. 

The vulnerabilities have been disclosed to Swisslog and security updates are available to close them and protect networks – healthcare organisations using Translogic's PTS are urged to apply them.  

"I think the lesson to be learned here is that this is the story of IoT in a way. Many applications have moved over the years from analogue systems to digital systems and eventually to be connected to the network and then later to the internet," said Seri. 

"From the hospital's point of view, this is just another reason to go ahead and [apply network segmentation](https://www.zdnet.com/article/cybersecurity-do-these-ten-things-to-keep-your-networks-secure-from-hackers-hospitals-told/) in the most effective way possible," he added.  

**SEE:** [**Ransomware: Now gangs are using virtual machines to disguise their attacks**](https://www.zdnet.com/article/ransomware-cyber-criminals-are-using-virtual-machines-to-hide-attacks-from-being-detected/)

It's also recommended that hospitals apply access controls across the network, [such as multi-factor authentication](https://www.zdnet.com/article/multi-factor-authentication-use-it-for-all-the-people-that-access-your-network-all-the-time/), so that users can't gain access to networks and systems they don't have permission to use in order to prevent intruders from exploiting this ability. 

"Understanding that patient care depends not only on medical devices, but also on the operational infrastructure of a hospital is an important milestone to securing healthcare environments," said Seri. 

Swisslog confirmed that Armis had contacted them about the vulnerabilities and that software updates and mitigations are now available to fix the vulnerabilities and prevent them potentially being exploited on hospital networks.  

"Swisslog Healthcare has already begun rolling out these solutions and will continue to work with its customers and affected facilities. Our commitment to security as an organizational priority has prepared us to address these types of issues with efficiency and transparency," a spokesperson said.  

### **MORE ON CYBERSECURITY**

* [**Cyber criminals targeting hospitals are 'playing with lives' and must be stopped, report warns**](https://www.zdnet.com/article/cyber-criminals-targeting-hospitals-are-playing-with-lives-and-must-be-stopped-report-warns/)
* [**This old security vulnerability left millions of Internet of Things devices vulnerable to attacks**](https://www.zdnet.com/article/this-old-security-vulnerability-left-millions-of-internet-of-things-devices-vulnerable-to-attacks/)
* [**Universal Health Services slammed by massive cyberattack**](https://www.cnet.com/tech/services-and-software/universal-health-services-slammed-by-massive-cyberattack/)
* [**Hospitals are leaving millions of sensitive medical images exposed online**](https://www.zdnet.com/article/hospitals-are-leaving-millions-of-sensitive-medical-images-exposed-online/)
* [**Ransomware: How the NHS learned the lessons of WannaCry to protect hospitals from attack**](https://www.zdnet.com/article/ransomware-how-the-nhs-learned-the-lessons-of-wannacry-to-protect-hospitals-from-attack/)





#### Tags:
[[Swisslog]] [[Seri.]] [[ZDNet]]
