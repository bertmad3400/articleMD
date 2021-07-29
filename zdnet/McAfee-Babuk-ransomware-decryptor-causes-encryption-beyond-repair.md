# McAfee: Babuk ransomware decryptor causes encryption 'beyond repair'
### Babuk announced earlier this year that it would be targeting Linux/UNIX and ESXi or VMware systems with ransomware.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/mcafee-babuk-ransomware-decryptor-causes-encryption-beyond-repair/)
+ Date: July 29, 2021 -- 10:30 GMT (11:30 BST)
+ Author: Jonathan Greig


## Article:
Unknown

[A new report](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/babuk-biting-off-more-than-they-could-chew-by-aiming-to-encrypt-vm-and-nix-systems/) from McAfee Advanced Threat Research spotlights the Babuk ransomware gang, which recently announced it would be developing a cross-platform binary [aimed at Linux/UNIX and ESXi or VMware systems](https://www.zdnet.com/article/ransomware-gangs-are-abusing-vmware-esxi-exploits-to-encrypt-virtual-hard-disks/). 

McAfee's Thibault Seret and Northwave's Noël Keijzer [wrote](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-moving-to-vm-nix-systems.pdf) that many core backend systems in companies are running on these *nix operating systems and Babuk wasted little time in infecting high-profile victims despite numerous problems with the binary. Researchers noted that they saw some ransomware gangs experimenting with writing their binaries in the cross-platform language Golang (Go).

"It seems that Babuk has adopted live beta testing on its victims when it comes to its Golang binary and decryptor development. We have seen several victims' machines encrypted beyond repair due to either a faulty binary or a faulty decryptor," Seret and Keijzer said.  

"Even if a victim gave in to the demands and was forced to pay the ransom, they still could not get their files back. We strongly hope that the bad coding also affects Babuk's relationship with its affiliates. The affiliates are the ones performing the actual compromise and are now faced with a victim that cannot get their data back even if they pay. This essentially changes the crime dynamic from extortion to destruction which, from a criminal's point of view, is much less profitable."

The typical Babuk attack features three distinct phases: initial access, network propagation and action on objectives. 

Babuk also operated a ransomware-as-a-service model [before shutting down in April](https://therecord.media/babuk-gang-says-it-will-stop-ransomware-attacks-after-dc-police-incident/). Northwave investigated a Babuk attack that was perpetrated through the [CVE-2021-27065 vulnerability](https://www.zdnet.com/article/microsoft-exchange-zero-day-attacks-30000-servers-hit-already-says-report/) also being exploited by the [HAFNIUM](https://www.zdnet.com/article/hafniums-china-chopper-a-slick-and-tiny-web-shell-for-creating-server-backdoors/) threat actor. 

Once access is gained, the threat actor placed a Cobalt Strike backdoor on the system, according to the report. Cobalt Strike is generally used by attackers for repeat access and Northwave found multiple backdoors on "several key systems within the network." 






Through a custom version of zer0dump, the attacker was able to gain domain administrator credentials and used Mimikatz to get access to credentials.

"During later stages of the attack the threat actor opted to create a new local administrator account on some of the systems as a means of additional persistence. Lateral movement between Windows systems was achieved using RDP," the report said. 

"For connections to Linux systems the attacker made use of SSH (using Putty). Moving files to Linux systems was done using WinSCP from Windows systems. While tools used on Windows systems were downloaded from the internet. The threat actor made use of the "temp.sh" and "wdfiles.ru" file hosting websites to host most of his tools. Other tools were downloaded directly from GitHub or the websites of their respective developers."

The attacker also used DFind, NetScan and LAN Search Pro to search through the environment and exfiltrate data before rolling out the ransomware. 

Once compressed data was exfiltrated to both Mega and Google Drive, the attacker destroyed the victim's backups and moved on to the victim's ESXi hosts to deploy a precompiled ransomware binary.

That binary encrypts all of a victim's virtual machines, but according to McAfee's analysis, it was "very poorly implemented and contained several different design flaws that resulted in the irreversible corruption of data."

At the end of April, Babuk's operators decided to change things up following the widely covered [ransomware attack on the DC Police Department](https://www.techrepublic.com/article/ransomware-attack-hits-washington-d-c-police-department/). 

After trying and failing to extort the police department, the leaders of the group said they would no longer encrypt systems and instead focus on data exfiltration. They also pledged to make their ransomware an open-source project by publishing the code.

![babuk.jpg]()![babuk.jpg](https://www.zdnet.com/a/hub/i/r/2021/07/29/bd0caf48-25ee-4bf0-b132-bc559f4234f1/resize/470xauto/136d0f35a0f777993a467830d659c6fc/babuk.jpg)A recent message from Babuk.


 McAfee
 "The threat actor indicated that it would focus on publishing data from victims that were unresponsive to its ransom demands. Furthermore, the threat actor indicated that it would host and publish data for other groups. As such the Babuk threat actor seems to be moving towards a data management position," the report said. 

"Given the poor design of its ransomware, a fair number of victims should be saved from completely losing their data when being attacked by Babuk. As mentioned in the previous sections, Northwave has seen threat actors slowly move from a scheme extorting victims by encrypting their data towards a double-extortion scheme where the threat actors both encrypt the victim's data and exfiltrate it as well. It is interesting to see threat actors now moving towards a scheme where their sole source of pressure to extort victims is the exfiltration of sensitive data."

The Babuk team began leaking data, first [releasing source code for the Cyberpunk 2077 game](https://www.databreaches.net/babuk-re-organizes-as-payload-bin-offers-its-first-leak/) in May. But after that, the gang went dark again according to the report. 

The study also discusses the Babuk decryptor, which Seret and Keijzer said has a limit in the maximum number of bytes that will decrypt, "which is strange."

"Overall, the decryptor is poor as it only checks for the extension '.babyk' which will miss any files the victim may have renamed in an attempt to recover them. Also, the decryptor checks if the file is more than 32 bytes in length as the last 32 bytes are combined later with other hardcoded values to get the final key," the study said. 

"This is bad design as those 32 bytes could be trash, instead of the key, as the customer could make things, etc. It does not operate efficiently by checking the paths that are checked in the malware, instead it analyzes everything." 

Seret and Keijzer go on to explain that the Babuk ransomware caused significant damage because it was operating faulty ransomware that led to a decryption process that fails in some instances, causing "irrecoverable damage."

"We suspect that this poor design of the ransomware was the reason that the threat actor decided to move towards a data management position," Seret and Keijzer added. 

"Ultimately, the difficulties faced by the Babuk developers in creating ESXi ransomware may have led to a change in business model, from encryption to data theft and extortion."

McAfee Advanced Threat Research warned that Babuk was posting recruitment memos asking for individuals with pentest skills. They urge defenders to watch for penetration testing tools like winPEAS, Bloodhound and SharpHound, or hacking frameworks such as CobaltStrike, Metasploit, Empire or Covenant.





#### Tags:
[[Babuk]] [[ransomware]] [[Seret]] [[Keijzer]] [[McAfee]] [[Northwave]] [[said.]] [[ESXi]] [[decryptor]] [[Windows]] [[ZDNet]]
