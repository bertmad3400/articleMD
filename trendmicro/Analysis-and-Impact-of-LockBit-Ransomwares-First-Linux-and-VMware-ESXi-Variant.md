# Analysis and Impact of LockBit Ransomware’s First Linux and VMware ESXi Variant
### LockBit ransomware's operators announced the release of its first Linux and ESXi variant in October. With samples also spotted in the wild, we discuss the impact and analysis of this variant.

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/22/a/analysis-and-Impact-of-lockbit-ransomwares-first-linux-and-vmware-esxi-variant.html
+ Date: 2022-01-24
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/analysis-and-impact-of-lockbit-ransomwares-first-linux-and-vmware-esxi-variant/analysis_and%20mpact_of_lockbit_ransomwares_first_linux_and_vmware_esxi_variant.jpg)





In our monitoring of the LockBit [ransomware](https://www.trendmicro.com/vinfo/us/security/definition/ransomware)’s intrusion set, we found an announcement for LockBit Linux-ESXi Locker version 1.0 on October 2021 in the underground forum "RAMP," where potential affiliates can find it. This signifies the LockBit ransomware group’s efforts to expand its targets to Linux hosts. Since October, we have been seeing samples of this variant in the wild.


This variant could have a big impact on victim organizations because of how ESXi, VMware’s hypervisor helps in managing servers.


Analysis of the variant


Lockbit Linux-ESXi Locker version 1.0 uses a combination of Advanced Encryption Standard (AES) and elliptic-curve cryptography (ECC) algorithms for data encryption. From our analysis, we can see that this version of LockBit can accept parameters, as detailed in Figure 1.






![Figure 1. Parameters accepted by the Linux-ESXi version of LockBit](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/analysis-and-impact-of-lockbit-ransomwares-first-linux-and-vmware-esxi-variant/fig%201Parameters%20accepted%20by%20the%20Linux-ESXi%20version%20of%20LockBit.jpg)
Figure 1. Parameters accepted by the Linux-ESXi version of LockBit





This version of the ransomware has logging capabilities and can log the following information:


* Processor information
* Volumes in the system
* Virtual machines (VMs) for skipping
* Total files
* Total VMs
* Encrypted files
* Encrypted VMs
* Total encrypted size
* Time spent for encryption


This variant also contains commands necessary for encrypting VM images hosted on ESXi servers, as listed in Table 1.




| Command | **Description** |
| vm-support --listvms  | Obtain a list of all registered and running VMs |
| esxcli vm process list  | Get a list of running VMs  |
| esxcli vm process kill --type   force --world-id  | Power off the VM from the list  |
| esxcli storage filesystem list  | Check the status of data storage  |
| /sbin/vmdumper %d suspend\_v  | Suspend VM  |
| vim-cmd hostsvc/enable\_ssh  | Enable SSH  |
| vim-cmd hostsvc/autostartmanager/enable\_autostart false  | Disable autostart  |
| vim-cmd hostsvc/hostsummary grep cpuModel  | Determine ESXi CPU model |


Table 1. Commands for encrypting VM images hosted on ESXi servers


The ransom note is typical of LockBit attacks. It advertises the speed of [LockBit 2.0](https://www.trendmicro.com/en_us/research/21/h/lockbit-resurfaces-with-version-2-0-ransomware-detections-in-chi.html), lists down the leak sites where the LockBit group threatens to publish stolen information, and ends with a recruitment ad for potential insiders enticing them with “millions of dollars” in exchange for access to valuable company data.






![Figure 2 LockBit ransom note](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/analysis-and-impact-of-lockbit-ransomwares-first-linux-and-vmware-esxi-variant/fig%202%20A%20ransom%20note%20of%20the%20Linux-ESXi%20version%20of%20LockBit%20a.jpg)




![Figure 2 LockBit ransom note](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/analysis-and-impact-of-lockbit-ransomwares-first-linux-and-vmware-esxi-variant/fig%202%20A%20ransom%20note%20of%20the%20Linux-ESXi%20version%20of%20LockBit%20b.jpg)
Figure 2. A ransom note of the Linux-ESXi version of LockBit




LockBit's operators typically threaten to publish data they stole from their victims on their leak site once their targeted organizations have failed to comply with their ransom demands.






![Figure 3. A screenshot of LockBit 2.0’s leak site](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/analysis-and-impact-of-lockbit-ransomwares-first-linux-and-vmware-esxi-variant/LockBit%20leak%20blog.jpg)
Figure 3. A screenshot of LockBit 2.0’s leak site




Impact of the variant


The release of this variant is in line with how [modern ransomware](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/modern-ransomwares-double-extortion-tactics-and-how-to-protect-enterprises-against-them) groups have been shifting their efforts to target and encrypt Linux hosts such as ESXi servers. An ESXi server typically hosts multiple VMs, which in turn hold important data or services for an organization. The successful encryption by ransomware of ESXi servers could therefore have a large impact on targeted companies. This trend was spearheaded by ransomware families like [REvil](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-revil) and [DarkSide](/en_us/research/21/e/what-we-know-about-darkside-ransomware-and-the-us-pipeline-attac.html).


Recommendations


ESXi offers organizations an easier way to manage their servers. But ransomware operators are also mirroring the transition of organizations to platforms such as ESXi. This development adds LockBit to the list of ransomware families capable of targeting Linux hosts in general and the ESXi platform in particular.


While Linux versions are typically harder to detect, implementing security best practices can still help organizations minimize the possibility of a successful attack. In the case of LockBit, keeping systems up to date can prevent intrusions. This is because LockBit has been known to use access credentials stolen from vulnerable servers and sold in the cybercriminal underground. VMware also provides recommendations for [enhancing the security](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-E9B71B85-FBA3-447C-8A60-DEE2AE1A405A.html) of ESXi.


Organizations should also consider the following steps to mitigate ransomware threats:


* Deploy cross-layered detection and response solutions. Find solutions that can anticipate and respond to ransomware activities, techniques, and movements before the threat culminates. [Trend Micro Vision One™️](https://www.trendmicro.com/en_us/business/products/detection-response.html), for example, helps detect and block ransomware components to stop attacks before they can affect an enterprise.
* Create a playbook for attack prevention and recovery. Both an incident response (IR) [playbook](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final) and IR [frameworks](https://www.cynet.com/incident-response/incident-response-sans-the-6-steps-in-depth/) help organizations plan for different attacks.
* Conduct attack simulations. Expose employees to [realistic cyberattack simulations](https://www.nytimes.com/2021/06/03/us/politics/ransomware-cybersecurity-infrastructure.html) that can help decision-makers, security personnel, and IR teams identify and prepare for potential security gaps and attacks.






**Indicators of compromise (IOCs)**


SHA256


* f3a1576837ed56bcf79ff486aadf36e78d624853e9409ec1823a6f46fd0143ea
* 67df6effa1d1d0690c0a7580598f6d05057c99014fcbfe9c225faae59b9a3224
* ee3e03f4510a1a325a06a17060a89da7ae5f9b805e4fe3a8c78327b9ecae84df


YARA rule**:**  





> rule Linux\_Lockbit\_Jan2022 {
> 
> 
>    meta:
> 
> 
>       description = "Detects a Linux version of Lockbit ransomware"
> 
> 
>       author = "TrendMicro Research"
> 
> 
>       date = "2022-01-24"
> 
> 
>       hash1 = "038ff8b2fef16f8ee9d70e6c219c5f380afe1a21761791e8cbda21fa4d09fdb4"
> 
> 
>      strings:
> 
> 
>         $xor\_string\_1 = "LockBit Linux/ESXi locker V:" xor(0x01-0xff)
> 
> 
>         $xor\_string\_2 = "LockBit 2.0 the world's fastest ransomware since 2019" xor(0x01-0xff)
> 
> 
>         $xor\_string\_3 = "Tox ID LockBitSupp" xor(0x01-0xff)
> 
> 
>     condition:
> 
> 
>       uint16(0) == 0x457f and filesize < 300KB and
> 
> 
>       filesize > 200KB and any of them
> 
> 
>  
> 
> 
> }
> 
> 
> 








## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=Expand]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=REvil]] [[action.malware.name=RTM]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Lockbit]] [[Ransomware]] [[Esxi]] [[Vms]] [[Linux-esxi]] [[Linux]] [[Vm]] [[Esxcli]] [[Vim-cmd]] [[Trend Micro]]
#### SHA256-hash
f3a1576837ed56bcf79ff486aadf36e78d624853e9409ec1823a6f46fd0143ea 67df6effa1d1d0690c0a7580598f6d05057c99014fcbfe9c225faae59b9a3224 ee3e03f4510a1a325a06a17060a89da7ae5f9b805e4fe3a8c78327b9ecae84df 038ff8b2fef16f8ee9d70e6c219c5f380afe1a21761791e8cbda21fa4d09fdb4

