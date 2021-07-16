# Linux Variant of HelloKitty Ransomware Targets VMware ESXi Servers
### HelloKitty joins the growing list of ransomware bigwigs going after the juicy target of VMware ESXi, where one hit gets scads of VMs.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167883)
+ Date: July 16, 2021  5:10 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/16162559/hellokitty-e1626467172148.jpeg)
For the first time, researchers have publicly spotted a Linux encryptor used by the HelloKitty ransomware gang: the outfit behind the February [attack on videogame developer CD Projekt Red](https://threatpost.com/cyberpunk-2077-publisher-hack-ransomware/163775/).


On Wednesday, [MalwareHunterTeam](https://twitter.com/malwrhunterteam) disclosed its discovery of numerous Linux ELF-64 versions of the HelloKitty ransomware targeting VMware ESXi servers and virtual machines (VMs) running on them.



> 
> Seems no one mentioned yet, so let me do it: the Linux version of HelloKitty ransomware was already using esxcli at least in early March for stopping VMs…[@VK\_Intel](https://twitter.com/VK_Intel?ref_src=twsrc%5Etfw) [@demonslay335](https://twitter.com/demonslay335?ref_src=twsrc%5Etfw) [pic.twitter.com/atSv0OO7YL](https://t.co/atSv0OO7YL)
> 
> 
> — MalwareHunterTeam (@malwrhunterteam) [July 14, 2021](https://twitter.com/malwrhunterteam/status/1415403132230803460?ref_src=twsrc%5Etfw)
> 
> 




The fact that HelloKitty uses a Linux encryptor [isn’t a lightbulb moment](https://twitter.com/aboutdfir/status/1415532608428158977), but this is the first sample that researchers have observed.


ESXi isn’t strictly Linux, as it has its own, custom kernel. But it’s similar, including in its ability to run ELF-64 Linux executables. Executable and Linkable Format (ELF-64) is a standard file format for executable files within Linux and UNIX-like operating systems.


Attackers Love ESXi
-------------------


VMware ESXi, formerly known as ESX, is a bare-metal hypervisor that installs easily onto servers and partitions them into multiple VMs. While that makes it easy for multiple VMs to share the same hard-drive storage, it sets systems up to be one-stop shopping spots for attacks, since attackers can encrypt the centralized virtual hard drives used to store data from across VMs.


That’s how AT&T Cybersecurity’s [Alien Labs](https://cybersecurity.att.com/blogs/labs-research/revils-new-linux-version) explained it earlier in the month, when the REvil ransomware threat actors came up with a [Linux variant](https://threatpost.com/linux-variant-ransomware-vmwares-nas/167511/) that likewise targeted VMware ESXi, as well as its network-attached storage (NAS) devices.


The motivation behind producing these variants of widespread ransomware malware isn’t Linux, per se. Rather, it’s that ESXi servers are such a valuable target, according to Dirk Schrader, global vice president of security research at change-management software provider New Net Technologies (NNT). Schrader told Threatpost on Friday that on top of the attraction of ESXi servers as a target, “going that extra mile to add Linux as the origin of many virtualization platforms to [malware’s] functionality” has the welcome side effect of enabling attacks on any Linux machine.


“A single EXSi 7 server can host up to 1024 VMs, in theory, but for the attacker, it is the combination of number of VMs and their importance that makes each ESXi server a worthy target,” Schrader explained. “Attacking and encrypting a device that runs 30 or so critical services for an organization is promising to yield results (ransom paid).”


MalwareHunterTeam shared samples of the HelloKitty Linux variant with [BleepingComputer](https://www.bleepingcomputer.com/news/security/linux-version-of-hellokitty-ransomware-targets-vmware-esxi-servers/), which published technical details including strings referencing ESXi and the ransomware’s attempts to shut down running VMs. As you can see in the multiple “kill” checks in the replicated sample below, the ransomware is using ESXi’s “esxcli” command-line management tool to list the running VMs on the server and attempt to shut them down – first with a soft kill, then a hard kill, then a forced kill.



> First try kill VM:%ld ID:%d %s  
> 
> esxcli vm process kill -t=soft -w=%d  
> 
> Check kill VM:%ld ID:%d  
> 
> esxcli vm process kill -t=hard -w=%d  
> 
> Unable to find  
> 
> Killed VM:%ld ID:%d  
> 
> still running VM:%ld ID:%d try force  
> 
> esxcli vm process kill -t=force -w=%d  
> 
> Check VM:%ld ID: %d manual !!!  
> 
> .README\_TO\_RESTORE  
> 
> Find ESXi:%s  
> 
> esxcli vm process list  
> 
> World ID:  
> 
> Process ID:  
> 
> Running VM:%ld ID:%d %s  
> 
> Total VM run on host: %ld
> 
> 


So Many Linux Encryptors
------------------------


The days when Linux, Unix and other Unix-like computer operating systems weren’t typically targeted by malware authors are long gone. It might well have been the case that attackers used to prefer bedeviling Windows systems, given that Windows instances are far more widespare than Linux instances. As well, Linux instances are generally well-protected against vulnerabilities, thanks to a tight-knit user base that delivers fast security updates.


Andrew Barratt, managing principal of solutions and investigations at cybersecurity advisory firm Coalfire, told Theatpost on Friday that we said goodbye to the days when malware didn’t target Linux “a long time ago,” but that change was typically server-side and hence not particularly visible to the public.


“With the rise of Mac OS on the desktop and its underlying infrastructure being based on BSD – everyone’s favourite ‘hard nix’ – there has been a correlation in *nix based malware as attackers target the Apple end user,” Barratt said in an email, *nix being shorthand for any Unix, Linux or other Unix-like systems. “Looking at it as Windows vs. Linux is too short a view. Realistically attackers cast a broad net against platforms: yes, Windows/Linux/ESXi – but also application platforms – Magento being a common one targeted due to its prevalence in e-commerce. What this really starts to show us, is the absolute need for full stack application security from line of business applications right the way down to the bare metal.”


At this point, besides the HelloKitty and REvil variants, the list of ransomware operators that have introduced Linux encryptors to target ESXi VMs also includes [Babuk](https://twitter.com/fwosar/status/1382111802398498819), [RansomExx](https://threatpost.com/linux-variant-ransomware-vmwares-nas/167511/)/[Defray 777](https://threatpost.com/defray-ransomware-seen-targeting-education-healthcare-industry/127656/), [PYSA](https://threatpost.com/pysa-ransomware-education-feds-warn/164832/)/Mespinoza, [GoGoogle](https://www.techradar.com/news/revil-ransomware-group-deploys-linux-encryptor-against-vmware-virtual-machines), and the [now-defunct](https://threatpost.com/darksides-servers-shutdown/166187/) DarkSide.


Defensive Tactics
-----------------


Sean Nikkel, senior cyber threat intel analyst at digital risk protection provider Digital Shadows, opined that the tricky part about defending against attacks like these, which are already against a variety of software and hardware, means “having a good baseline on what your assets are,”


Nikkel told Threatpost on Friday that that includes “how they’re patched, how they’re secured, what other dependencies they have, and who’s got access to them. It’s a laundry list of tasks to stay secured, but organizations must handle most or all of these best practices, addressing the low-hanging fruit, which is the favorite avenue of attack for threats. Otherwise, they may end up in the crosshairs of yet another ransomware attack.”


NNT’s Schrader advised that for ESXi shops, the best defense is to have tight monitoring to alert about any change happening to the ESXi, its filesystem and configuration settings. “It should be hardened anyway,” he commented.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Linux]] [[ESXi]] [[VMs]] [[ransomware]] [[VM]] [[HelloKitty]] [[esxcli]] [[malware]] [[Schrader]] [[vm]] [[ThreatPost]]
