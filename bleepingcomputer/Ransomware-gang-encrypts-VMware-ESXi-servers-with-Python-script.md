# Ransomware gang encrypts VMware ESXi servers with Python script
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/ransomware-gang-encrypts-vmware-esxi-servers-with-python-script/)
+ Date: October 5, 2021
+ Author: Sergiu Gatlan


## Article:
![Ransomware gang encrypts VMware ESXi servers with Python script](https://www.bleepstatic.com/content/hl-images/2021/09/22/VMware-headpic.jpg)


Operators of an unknown ransomware gang are using a Python script to encrypt virtual machines hosted on VMware ESXi servers.


While the Python programming language is not commonly used in ransomware development, it is a logical choice for ESXi systems, seeing that such Linux-based servers come with Python installed by default.


As Sophos researchers recently discovered while investigating a ransomware incident, a Python ransomware script was used to encrypt a victim's virtual machines running on a vulnerable ESXi hypervisor within three hours of the initial breach.


"A recently-concluded investigation into a ransomware attack revealed that the attackers executed a custom Python script on the target's virtual machine hypervisor to encrypt all the virtual disks, taking the organization's VMs offline," SophosLabs Principal Researcher Andrew Brandt said.


"In what was one of the quickest attacks Sophos has investigated, from the time of the initial compromise until the deployment of the ransomware script, the attackers only spent just over three hours on the target's network before encrypting the virtual disks in a VMware ESXi server."


VMs encrypted using a 6kb script
--------------------------------


In the middle of the night, the attackers breached the victim's network over the weekend by logging into a TeamViewer account running on a device with a domain admin logged on.


Once in, they started searching the network for additional targets using Advanced IP Scanner and logged onto an ESXi server via the built-in SSH ESXi Shell service, which was accidentally left toggled on by the IT staff (even though it's disabled by default.)


The ransomware operators then executed a 6kb Python script to encrypt all virtual machines' virtual disk and VM settings files.


The script, partially recovered while investigating the incident, allows the ransomware operators to use multiple encryption keys and email addresses and customize the file suffix for the encrypted files.


It works by shutting down the virtual machines, overwriting the original files stored on the datastore volumes, then deleting them to block recovery attempts and leaving the encrypted files behind.


"Administrators who operate ESXi or other hypervisors on their networks should follow security best practices, avoiding password reuse, and using complex, difficult to brute-force passwords of adequate length," Brandt recommended.


"Wherever possible, enable the use of multi-factor authentication and enforce the use of MFA for accounts with high permissions, such as domain administrators."


VMware also [provides advice on securing ESXi servers](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-E9B71B85-FBA3-447C-8A60-DEE2AE1A405A.html) by limiting the risk of unauthorized access and the attack surface on the hypervisor itself.


VMware ESXi servers under attack
--------------------------------


Attacking ESXi servers is a highly disruptive tactic for ransomware groups since most of them run multiple virtual machines simultaneously, with business-critical services and apps deployed on many of them.


Multiple ransomware gangs, including Darkside, RansomExx, and Babuk Locker, have [exploited VMWare ESXi pre-auth RCE bugs](https://twitter.com/GossiTheDog/status/1324896051128635392) to encrypt virtual hard disks used as centralized enterprise storage space.


This is not the first incident where Python-based malicious tools have been used to target Internet-exposed VMware servers.


In June, researchers spotted the multi-platform Python-based [FreakOut](https://www.bleepingcomputer.com/news/security/freakout-malware-exploits-critical-bugs-to-infect-linux-hosts/)malware targeting Windows and Linux devices upgraded to worm[its way onto VMware vCenter servers](https://www.bleepingcomputer.com/news/security/freakout-malware-worms-its-way-into-vulnerable-vmware-servers/) unpatched against a critical RCE bug in all default installs.


FreakOut is an obfuscated Python script designed to evade detection with the help of a polymorphic engine and a user-mode rootkit that hides malicious files dropped on infected systems.


Linux versions of [HelloKitty](https://www.bleepingcomputer.com/news/security/linux-version-of-hellokitty-ransomware-targets-vmware-esxi-servers/) and [BlackMatter](https://www.bleepingcomputer.com/news/security/linux-version-of-blackmatter-ransomware-targets-vmware-esxi-servers/) ransomware were also spotted in the wild in July and August, both of them targeting targets VMware's ESXi virtual machine platform.


To make things even worse, with VMware ESXi being one of the most if not the most popular enterprise virtual machine platforms, almost every enterprise-targeting ransomware gang has started developing their encryptors designed to specifically target ESXi virtual machines.




#### Tags:
[[ESXi]] [[ransomware]] [[VMware]] [[hypervisor]] [[Bleeping Computer]]
