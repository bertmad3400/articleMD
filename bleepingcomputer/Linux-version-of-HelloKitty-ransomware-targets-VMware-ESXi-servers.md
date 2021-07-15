# Linux version of HelloKitty ransomware targets VMware ESXi servers
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/linux-version-of-hellokitty-ransomware-targets-vmware-esxi-servers/)
+ Date: July 15, 2021
+ Author: Lawrence Abrams


## Article:
![HelloKitty](https://www.bleepstatic.com/content/hl-images/2021/02/09/HelloKitty.jpg)


​The ransomware gang behind the highly publicized attack on CD Projekt Red uses a Linux variant that targets VMware's ESXi virtual machine platform for maximum damage.


As the enterprise increasingly moves to virtual machines for easier backup and resource management, ransomware gangs are evolving their tactics to create Linux encryptors that target these servers.



VMware ESXi is one of the most popular enterprise virtual machine platforms. Over the past year, there has been an increasing number of ransomware gangs releasing Linux encryptors targeting this platform.


While ESXi is not strictly Linux as it uses its own customer kernel, it does share many similar characteristics, including the ability to run ELF64 Linux executables.


HelloKitty moves to ESXi
------------------------


Yesterday, security researcher [MalwareHunterTeam](https://twitter.com/malwrhunterteam) found numerous Linux ELF64 versions of the HelloKitty ransomware targeting ESXi servers and the virtual machines running on them.


It has been known that HelloKitty utilizes a Linux encryptor, but this is the first sample that researchers have publicly spotted.




> 
> Seems no one mentioned yet, so let me do it: the Linux version of HelloKitty ransomware was already using esxcli at least in early March for stopping VMs...[@VK\_Intel](https://twitter.com/VK_Intel?ref_src=twsrc%5Etfw) [@demonslay335](https://twitter.com/demonslay335?ref_src=twsrc%5Etfw) [pic.twitter.com/atSv0OO7YL](https://t.co/atSv0OO7YL)
> 
> 
> — MalwareHunterTeam (@malwrhunterteam) [July 14, 2021](https://twitter.com/malwrhunterteam/status/1415403132230803460?ref_src=twsrc%5Etfw)


MalwareHunterTeam shared samples of the ransomware with BleepingComputer, and you can clearly see strings referencing ESXi and the ransomware's attempts to shut down running virtual machines.


From the debug messages, we can see that the ransomware uses ESXi's `esxcli` command-line management tool to list the running virtual machines on the server and then shut them down.


Ransomware gangs targeting ESXi servers will shut down virtual machines before encrypting files to prevent the files from being locked and to avoid data corruption.




> 
> Some Darkside affiliates have a tendency to forget to stop all the ESXi daemons before kicking off the encryption. The result is that sometimes encrypted data can be interlaced with unencrypted data or that the footer containing the file key is partially overwritten. Same result.
> 
> 
> — Fabian Wosar (@fwosar) [April 14, 2021](https://twitter.com/fwosar/status/1382303492002435073?ref_src=twsrc%5Etfw)


When shutting down the virtual machines, the ransomware will first try a graceful shutdown using the 'soft' command:


If there are still VMs running, it will try an immediate shutdown of virtual machines using the 'hard' command:


Finally, if virtual machines are still running, the malware will use the 'force' command to shut down any running VMs forcefully.


After the virtual machines are shut down, the ransomware will begin encrypting **.vmdk**(virtual hard disk), **.vmsd** (metadata and snapshot information), and **.vmsn** (contains the active state of the VM) files.


This method is very efficient as it allows a ransomware gang to encrypt many virtual machines with a single command.


Last month, MalwareHunterTeam also found a [Linux version of the REvil ransomware](https://www.bleepingcomputer.com/news/security/revil-ransomwares-new-linux-encryptor-targets-esxi-virtual-machines/) that targets ESXi servers and used the esxcli command as part of the encryption process.


Emsisoft CTO Fabian Wosar told BleepingComputer at the time that other ransomware operations, such as Babuk, RansomExx/Defray, Mespinoza, GoGoogle, and the now-defunct DarkSide, have also created Linux encryptors to target ESXi virtual machines.


"The reason why most ransomware groups implemented a Linux-based version of their ransomware is to target ESXi specifically," said Wosar.


A bit about HelloKitty
----------------------


HelloKity has been in operation since November 2020, when a victim [first posted](https://www.bleepingcomputer.com/forums/t/750580/hellokitty-ransomware-crypt-read-me-unlocktxt-support-topic/) about the ransomware in our forums.


Since then, the threat actors have not been particular actively compared to other human-operated ransomware operations.


Their most well-known attack has been against [CD Projekt Red](https://www.bleepingcomputer.com/news/security/cd-projekt-red-gaming-studio-hit-by-ransomware-attack/), where the threat actors encrypted devices and claim to have stolen source code for Cyberpunk 2077, Witcher 3, Gwent, and more.


The threat actors later claimed that someone had [purchased the files stolen from CD Projekt Red](https://www.bleepingcomputer.com/news/security/cd-projekts-stolen-source-code-allegedly-sold-by-ransomware-gang/).


This ransomware, or its variants, has been used under different names such as DeathRansom and [Fivehands](https://www.bleepingcomputer.com/news/security/new-ransomware-group-uses-sonicwall-zero-day-to-breach-networks/).




#### Tags:
[[ransomware]] [[ESXi]] [[Linux]] [[HelloKitty]] [[MalwareHunterTeam]] [[Projekt]] [[encryptors]] [[esxcli]] [[VMs]] [[Wosar]] [[Bleeping Computer]]
