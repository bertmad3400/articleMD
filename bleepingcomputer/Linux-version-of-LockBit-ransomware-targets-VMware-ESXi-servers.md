# Linux version of LockBit ransomware targets VMware ESXi servers
### LockBit is the latest ransomware gang whose Linux encryptor has been discovered to be focusing on the encryption of VMware ESXi virtual machines.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/linux-version-of-lockbit-ransomware-targets-vmware-esxi-servers/
+ Date: 2022-01-26T18:40:10-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/07/27/Lockbit-logo.jpg)

![LockBit](https://www.bleepstatic.com/content/hl-images/2021/07/27/Lockbit-logo.jpg)


LockBit is the latest ransomware gang whose Linux encryptor has been discovered to be focusing on the encryption of VMware ESXi virtual machines.


The enterprise is increasingly moving to virtual machines to save computer resources, consolidate servers, and for easier backups.


Due to this, ransomware gangs have evolved their tactics to create Linux encryptors that specifically target the popular VMware vSphere and ESXi virtualization platforms over the past year.


While ESXi is not strictly Linux, it does share many of its characteristics, including the ability to run ELF64 Linux executables.


Lockbit targets VMware ESXi servers
-----------------------------------


In October, LockBit began promoting the new features of their Ransomware-as-a-Service operation on the RAMP hacking forums, including a new Linux encryptor that targets VMware ESXi virtual machines.


In a new report, Trend Micro researchers analyzed the ransomware gang's Linux encryptor and explained how it's used to target VMWare ESXi and vCenter installations.


Linux encryptors are nothing new, with BleepingComputer reporting on similar encryptors in the past from [HelloKitty](https://www.bleepingcomputer.com/news/security/linux-version-of-hellokitty-ransomware-targets-vmware-esxi-servers/), [BlackMatter](https://www.bleepingcomputer.com/news/security/linux-version-of-blackmatter-ransomware-targets-vmware-esxi-servers/), [REvil](https://www.bleepingcomputer.com/news/security/revil-ransomwares-new-linux-encryptor-targets-esxi-virtual-machines/), [AvosLocker](https://www.bleepingcomputer.com/news/security/linux-version-of-avoslocker-ransomware-targets-vmware-esxi-servers/), and the [Hive](https://www.bleepingcomputer.com/news/security/hive-ransomware-now-encrypts-linux-and-freebsd-systems/) ransomware operations.


Like other Linux encryptors, LockBits provides a command-line interface allowing affiliates to enable and disable various features to tailor their attacks.


These features include the ability to specify how large a file and how many bytes to encrypt, whether to stop running virtual machines, or wipe free space after, as shown by the image below.



![LockBit Linux encryptor command-line arguments](https://www.bleepstatic.com/images/news/ransomware/l/lockbit/linux-esxi-encryptor/command-line.jpg)**LockBit Linux encryptor command-line arguments**  
*Source: Trend Micro*
However, what makes the LockBit linux encryptor stand out is the wide use of both VMware ESXI and VMware vCenter command-line utilities to check what virtual machines are running and to shut them down cleanly so they are not corrupted while being encrypted.


The full list of commands [seen by Trend Micro](https://www.trendmicro.com/en_us/research/22/a/analysis-and-Impact-of-lockbit-ransomwares-first-linux-and-vmware-esxi-variant.html?utm_source=trendmicroresearch&utm_medium=smk&utm_campaign=0122_ImpactofLockbit) in LockBit's encryptor are listed below:




| Command | **Description** |
| vm-support --listvms  | Obtain a list of all registered and running VMs |
| esxcli vm process list  | Get a list of running VMs  |
| esxcli vm process kill --type   force --world-id  | Power off the VM from the list  |
| esxcli storage filesystem list  | Check the status of data storage  |
| /sbin/vmdumper %d suspend\_v  | Suspend VM  |
| vim-cmd hostsvc/enable\_ssh  | Enable SSH  |
| vim-cmd hostsvc/autostartmanager/enable\_autostart false  | Disable autostart  |
| vim-cmd hostsvc/hostsummary grep cpuModel  | Determine ESXi CPU model |

Trend Micro states that the encryptor uses AES to encrypt files and elliptic-curve cryptography (ECC) algorithms to encrypt the decryption keys.


With the widespread use of VMware ESXI in the enterprise, all network defenders and security professional should expect that every large ransomware operation has already developed a Linux variant.


By making this assumption, admins and security professionals can create appropriate defenses and plans to protect all devices in their networks, rather than just Windows devices.


This is especially true for the LockBit operation, which has become the most prominent ransomware operation since [REvil shut down](https://www.bleepingcomputer.com/news/security/revil-ransomware-shuts-down-again-after-tor-sites-were-hijacked/) and prides itself on its encryptors' speed and feature set.


It is also vital to remember that as much as we are watching ransomware gangs, they are also watching us back.


This means that they monitor researchers' and journalists' social feeds for the latest tactics, defenses, and vulnerabilities that they can then use against corporate targets.


Due to this, ransomware gangs are constantly evolving their encryptions and tactics to try and stay one step ahead of security and Windows admins.





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=HELLOKITTY]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=REvil]] [[action.malware.name=RTM]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=Oslo]] [[victim.country.name=Norway]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Linux]] [[Ransomware]] [[Encryptor]] [[Vmware]] [[Esxi]] [[Lockbit]] [[Encryptors]] [[Command-line]] [[Esxcli]] [[Vim-cmd]] [[Bleeping Computer]]

