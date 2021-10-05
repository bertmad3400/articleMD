# New Python ransomware targets virtual machines, ESXi hypervisors to encrypt disks
### By targeting ESXi, encryption was achieved in less than three hours on a corporate network.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/new-python-ransomware-targets-virtual-machines-esxi-hypervisor-to-encrypt-disks/)
+ Date: October 5, 2021
+ Author: Charlie Osborne


## Article:
Unknown

A new strain of Python-based malware has been used in a "sniper" campaign to achieve encryption on a corporate system in less than three hours.


The attack, one of the fastest recorded by [Sophos researchers](https://news.sophos.com/en-us/2021/10/05/python-ransomware-script-targets-esxi-server-for-encryption/), was achieved by operators who "precision-targeted the ESXi platform" in order to encrypt the virtual machines of the victim. 

On Tuesday, Sophos said the malware, a new variant written in Python, was deployed ten minutes after threat actors managed to break into a TeamViewer account belonging to the victim organization.  

TeamViewer is a control and access platform that can be used by the general public and businesses alike to manage and control PCs and mobile devices remotely.  

As the software was installed on a machine used by an individual who also owned domain administrator access credentials, it took only ten minutes -- from 12.30 am to 12.40 am on a Sunday -- for attackers to find a vulnerable ESXi server suitable for the next stage of the assault.  

VMware ESXi is an enterprise-grade, bare-metal hypervisor used by vSphere, a system designed to manage both containers and virtual machines (VMs).  

The researchers say the ESXi server was likely vulnerable to exploit due to an active shell, and this led to the installation of Bitvise, SSH software used -- at least, legitimately -- for Windows server administration tasks.  






In this case, the threat actors utilized Bitvise to tap into ESXi and the virtual disk files used by active VMs.  

"ESXi servers have a built-in SSH service called the ESXi Shell that administrators can enable, but is normally disabled by default," Sophos says. "This organization's IT staff was accustomed to using the ESXi Shell to manage the server, and had enabled and disabled the shell multiple times in the month prior to the attack. However, the last time they enabled the shell, they failed to disable it afterwards." 

Three hours in, and the cyberattackers were able to deploy their Python ransomware and encrypt the virtual hard drives.  

The script used to hijack the company's VM setup was only 6kb in length but contained variables including different sets of encryption keys, email addresses, and options for customizing the suffix used to encrypt files in a ransomware-based attack.  

The malware created a map of the drive, inventoried the VM names, and then powered each virtual machine off. Once they were all disabled, full database encryption began. OpenSSL was then weaponized to encrypt them all quickly by issuing a command to a log of each VM's name on the hypervisor.  

Once encryption is complete, the reconnaissance files were overwritten with the word f*ck and were then deleted.   

Big game ransomware groups including DarkSide -- responsible for the [Colonial Pipeline](https://www.zdnet.com/article/colonial-pipeline-ransomware-attack-everything-you-need-to-know/) attack -- and REvil are known to use this technique. Sophos says the sheer speed of this case, however, should remind IT administrators that security standards need to be maintained on VM platforms as well as standard corporate networks.  

"Python is a coding language not commonly used for ransomware," commented Andrew Brandt, principal researcher at Sophos. "However, Python is pre-installed on Linux-based systems such as ESXi, and this makes Python-based attacks possible on such systems. ESXi servers represent an attractive target for ransomware threat actors because they can attack multiple virtual machines at once, where each of the virtual machines could be running business-critical applications or services." 

###  Previous and related coverage

* [This is the perfect ransomware victim, according to cybercriminals](https://www.zdnet.com/article/this-is-the-perfect-ransomware-victim-according-to-cybercriminals/)  

* [Ransomware gangs are complaining that other crooks are stealing their ransoms](https://www.zdnet.com/article/these-ransomware-crooks-are-complaining-they-are-getting-ripped-off-by-other-ransomware-crooks/)  

* [What is ransomware? Everything you need to know about one of the biggest menaces on the web](https://www.zdnet.com/article/ransomware-an-executive-guide-to-one-of-the-biggest-menaces-on-the-web/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[ESXi]] [[Sophos]] [[ransomware]] [[VM]] [[ZDNet]]
