# Palo Alto Networks patches zero-day affecting firewalls using GlobalProtect Portal VPN
### The issue affects multiple versions of PAN-OS 8.1 prior to 8.1.17 and Randori said it found numerous vulnerable instances exposed on internet-facing assets, in excess of 70,000 assets.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/palo-alto-networks-patches-zero-day-affecting-firewalls-using-globalprotect-portal-vpn/)
+ Date: November 10, 2021
+ Author: Jonathan Greig


## Article:
Unknown

Researchers with cybersecurity firm Randori have [discovered](https://www.randori.com/blog/cve-2021-3064/) a remote code execution vulnerability in Palo Alto Networks firewalls using the GlobalProtect Portal VPN. 


The zero-day -- which has a severity rating of 9.8 -- [allows](https://vital.wistia.com/medias/ht539sderu) for unauthenticated, remote code execution on vulnerable installations of the product. 

The issue affects multiple versions of PAN-OS 8.1 prior to 8.1.17, and Randori said it found numerous vulnerable instances exposed on internet-facing assets, in excess of 70,000 assets. It is used by a number of Fortune 500 companies and other global enterprises.

Palo Alto has released an update that patches CVE-2021-3064 after being notified about the issue in September. 

Aaron Portnoy, principal scientist at Randori, told *ZDNet* that the original catalyst for their research into Palo Alto Networks firewalls was identifying its presence on customer perimeters.

"Once an attacker has control over the firewall, they will have visibility into the internal network and can proceed to move laterally. Randori believes the best way to identify potential points of attack is to assess the attack surface. We then devoted resources into assessing the attack surface of the firewall itself in a lab environment. This process allowed us to identify the components an attacker would have to exploit in order to compromise the device," Portnoy explained.

"As is the case with many closed-source products, simply setting up an environment in which to develop an exploit is challenging. Complex products such as PAN firewalls include protections that make this process difficult regardless of the vulnerability. We have found the overall security posture of the affected devices to be on par with other vendors in the space." 






Portnoy said that exploitation is difficult but possible on devices with ASLR enabled, which appears to be the case in most hardware devices. 

"On virtualized devices (VM-series firewalls), exploitation is significantly easier due to lack of ASLR, and Randori expects public exploits will surface," Portnoy said. 

According to Portnoy, in October 2020, his team was tasked with researching vulnerabilities with the GlobalProtect Portal VPN. By November 2020, his team discovered CVE-2021-3064, began authorized exploitation of Randori customers, and successfully landed it at one of their customers -- over the internet -- not just in a lab.

The exploit gains root privileges -- complete control over the device -- and can execute arbitrary code. Portnoy said his team was able to gain a shell on the affected target, access sensitive configuration data, extract credentials and more while moving laterally from there and gaining visibility into the internal network. 

Randori exploited Palo Alto Networks PA-5220, including PAN-OS 8.1.16 and PAN-OS 8.1.15.

"The vulnerability chain consists of a method for bypassing validations made by an external web server (HTTP smuggling) and a stack-based buffer overflow. Exploitation of the vulnerability chain has been proven and allows for remote code execution on both physical and virtual firewall products. Publicly available exploit code does not exist at this time," Randori said.

"VPN devices are attractive targets for malicious actors, and exploitation of PA-VM virtual devices, in particular, is made easier due to their lack of Address Space Layout Randomization (ASLR). CVE-2021-3064 is a buffer overflow that occurs while parsing user-supplied input into a fixed-length location on the stack. The problematic code is not reachable externally without utilizing an HTTP smuggling technique. The exploitation of these together yields remote code execution as a low privileged user on the firewall device."

Randori noted that in order to exploit the vulnerability, the attacker must have network access to the device on the global protect service port (default port 443). As the affected product is a VPN portal, they added that this port is often accessible over the internet. 

In addition to the patch, Randori suggested affected organizations look through the available Threat Prevention signatures 91820 and 91855 that Palo Alto Networks made available. They can be enabled to thwart exploitation while organizations plan for the software upgrade. For those that do not use the VPN capability as part of the firewall, Randori recommended disabling the VPN functionality.

Portnoy and Randori touted the situation as an example of the ethical use of zero-days to protect companies from the kind of threats they face from nation-state actors. Portnoy estimates that the vulnerability would be worth several hundred thousand dollars on the black market.





#### Tags:
[[Portnoy]] [[Palo]] [[firewalls]] [[PAN-OS]] [[VPN]] [[ZDNet]]
