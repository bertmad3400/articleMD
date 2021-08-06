# Linux version of BlackMatter ransomware targets VMware ESXi servers
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/linux-version-of-blackmatter-ransomware-targets-vmware-esxi-servers/)
+ Date: August 5, 2021
+ Author: Lawrence Abrams


## Article:
![BlackMatter ransomware](https://www.bleepstatic.com/content/hl-images/2021/08/05/BlackMatter_ransomware.jpg)


​The BlackMatter gang has joined the ranks of ransomware operations to develop a Linux encryptor that targets VMware's ESXi virtual machine platform.


The enterprise is increasingly moving to virtual machines for their servers for better resource management and disaster recovery.


With VMware ESXi being the most popular virtual machine platform, almost every enterprise-targeting ransomware operation has begun to release encryptors that specifically target its virtual machines.


BlackMatter targets VMware ESXi
-------------------------------


Yesterday, security researcher [MalwareHunterTeam](https://twitter.com/malwrhunterteam) found a Linux ELF64 encryptor [[VirusTotal](https://www.virustotal.com/gui/file/6a7b7147fea63d77368c73cef205eb75d16ef209a246b05698358a28fd16e502/detection)] for the [BlackMatter ransomware gang](https://www.bleepingcomputer.com/news/security/blackmatter-ransomware-gang-rises-from-the-ashes-of-darkside-revil/) that specifically targets VMware ESXi servers based on its functionality.


BlackMatter is a relatively new ransomware operation that started last month and is believed to be a [rebrand of DarkSide](https://www.bleepingcomputer.com/news/security/darkside-ransomware-gang-returns-as-new-blackmatter-operation/). After researchers found samples, it was determined that the encryption routines used by the ransomware were the same custom and unique ones used by DarkSide.


DarkSide shut down after [attacking and shutting down Colonial Pipeline](https://www.bleepingcomputer.com/news/security/largest-us-pipeline-shuts-down-operations-after-ransomware-attack/) and then feeling the total pressure of international enforcement and the US government.


From the sample BlackMatter's Linux encryptor shared with BleepingComputer, it is clear that it was designed solely to target VMWare ESXi servers.


Advanced Intel's [Vitali Kremez](https://twitter.com/VK_Intel) [reverse engineered the sample](https://twitter.com/VK_Intel/status/1423188690126266370) and told BleepingComputer that the threat actors created an 'esxi\_utils' library that is used to perform various operations on VMware ESXi servers


Kremez told us that each function would execute a different command using the esxcli command-line management tool, such as listing VMs, stopping the firewall, stopping a VM, and more.


For example, stop\_firewall() function will execute the following command:


While the stop\_vm() will execute the following esxcli command:


All ransomware that targets ESXi servers attempts to shut down virtual machines before encrypting the drives. This is done to prevent data from being corrupted while it is encrypted.


Once all the VMs are shut down, it will encrypt files that match specific file extensions based on the configuration included with the ransomware.


Targeting ESXi servers is very efficient when conducting ransomware attacks, as it allows the threat actors to encrypt numerous servers at once with a single command.


As more businesses move to this type of platform for their servers, we will continue to see ransomware developers focus primarily on Windows machines but also create a dedicated Linux encrypted targeting ESXi.


Emsisoft CTO Fabian Wosar told BleepingComputer that other ransomware operations, such as [REvil](https://www.bleepingcomputer.com/news/security/revil-ransomwares-new-linux-encryptor-targets-esxi-virtual-machines/), [HelloKitty](https://www.bleepingcomputer.com/news/security/linux-version-of-hellokitty-ransomware-targets-vmware-esxi-servers/), Babuk, [RansomExx/Defray](https://www.bleepingcomputer.com/news/security/ransomexx-ransomware-also-encrypts-linux-systems/), Mespinoza, GoGoogle, have also created Linux encryptors for this purpose.




#### Tags:
[[ransomware]] [[ESXi]] [[BlackMatter]] [[Linux]] [[VMware]] [[encryptor]] [[Bleeping Computer]]
