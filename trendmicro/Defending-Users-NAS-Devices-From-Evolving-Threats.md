# Defending Users’ NAS Devices From Evolving Threats
### In our latest research, we analyze the threats targeting well-known brands of network-attached storage (NAS) devices. 

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/22/a/defending-users-NAS-devices-from-evolving-threats.html
+ Date: 2022-01-20
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-users-nas-devices-from-evolving-threats/cover-defending-users-nas-from-evolving-threats.jpg)





Threats to the internet of things (IoT) continue to evolve as users and businesses grow increasingly reliant on these tools for constant connectivity, access to information and data, and workflow continuity. Cybercriminals have taken notice of this dependence and now regularly update their known tools and routines to include network-attached storage (NAS) devices to their list of targets, knowing full well that users rely on these devices for storing and backing up files in both modern homes and businesses. More importantly, cybercriminals are aware that these tools hold valuable information and have only minimal security measures.


In our latest research paper, **“[Backing Your Backup: Defending NAS Devices Against Evolving Threats](https://www.trendmicro.com/vinfo/us/security/news/internet-of-things/reinforcing-nas-security-against-pivoting-threats),”** we studied the current infrastructure, environment, threats, and recommendations for defending systems against current threats targeting NAS devices. To emphasize the importance of mitigating the risks of malware infection and targeted attacks on NAS devices, we analyzed the technical details of two malware families that potentially included NAS devices in their existing business models, the [REvil](https://www.trendmicro.com/vinfo/tmr/?/us/security/news/cybercrime-and-digital-threats/ransomware-double-extortion-and-beyond-revil-clop-and-conti) ransomware and [StealthWorker](https://www.trendmicro.com/en_us/research/21/l/the-evolution-of-iot-linux-malware-based-on-mitre-att&ck-ttps.html) botnets.  




REvil


While the disappearance of REvil (aka Sodinokibi) in mid-2021 is filled with uncertainty, security researchers have [found](https://twitter.com/malwrhunterteam/status/1409577829289934851) a Linux version of the REvil ransomware that they have dubbed as Revix. After analyzing the samples, we found four different versions of the malware, all of which rely on an embedded JavaScript Observed Notation (JSON)-based configuration to set parameters before encrypting files. 






![fig1-defending-users-NAS-devices-from-evolving-threats](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-users-nas-devices-from-evolving-threats/figure1-defending-nas-devices-from-evolving-threats.png)
Figure 1. Revix’s JSON-based configuration





While some parameters are ignored by the ransomware, these are most important ones that we observed:


* **pk:** A 64-byte key
* **nbody:** The ransomware note text-encoded in base64
* **nname:** The ransomware note name
* **ext**: The extension added to encrypted files


After compromising the system, the malicious actors execute it manually on a NAS device to encrypt files and create a ransom note with a unique key per victim.  








![fig2-defending-users-NAS-devices-from-evolving-threats](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-users-nas-devices-from-evolving-threats/figure2-defending-nas-devices-from-evolving-threats.png)
Figure 2. Revix encrypting a QNAP NAS device




![fig3-defending-users-NAS-devices-from-evolving-threats](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-users-nas-devices-from-evolving-threats/figure3-defending-nas-devices-from-evolving-threats_.png)
Figure 3. Revix ransom note 




While the differences between the versions are minor, the group advertised the capability of encrypting NAS devices as early as May 2021 in underground forums. Given the vulnerability of NAS devices that are directly connected to the internet, we can expect a new wave of ransomware attacks affecting these gadgets in the future.


StealthWorker


In 2021, security researchers [found](https://blog.malwarebytes.com/threat-analysis/2019/02/new-golang-brute-forcer-discoveredamid-) brute-force attacks launched from the StealthWorker botnet on Synology NAS devices. We found multiple samples for this botnet and confirmed that newer versions are capable of brute-forcing and compromising servers running on several products and systems such as WooCommerce and WordPress. This botnet is also designed to generally attack any web server using HTTP authentication and other NAS devices like QNAP. Valid credentials found during compromise are then uploaded to the command-and-control (C&C) server, usually at port 5028/TCP.






![fig4-defending-users-NAS-devices-from-evolving-threats](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-users-nas-devices-from-evolving-threats/figure4-defending-nas-devices-from-evolving-threats.png)
Figure 4. StealthWorker brute-force function targeting QNAP devices




![fig5-defending-users-NAS-devices-from-evolving-threats](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-users-nas-devices-from-evolving-threats/figure5-defending-nas-devices-from-evolving-threats.png)
Figure 5. Infected Linux device connected to a C&C server




How to protect NAS devices


Without proper security implemented in NAS devices, users and businesses will continue to be targeted since these tools can be used as entry points for information theft, malware infection, and the disruption of operations, among others. Here are some best practices to protect your systems against threats that leverage the gaps in your NAS devices:


* Avoid connecting a NAS device directly to the internet.
* Regularly change the credentials for accessing an NAS device. Never use the preset default credentials that come with the device as these are well-known to malicious actors.
* Enable two-factor authentication (2FA) for additional security.
* Regularly check NAS manufacturers’ online security guides, such as Synology’s recommended [best practices](https://kb.synology.com/en-us/DSM/tutorial/How_to_add_extra_security_to_your_Synology_NAS) and QNAP’s recently released [suggestions](https://www.qnap.com/en/security-news/2022/take-immediate-actions-to-secure-qnap-nas) on how to help defend their devices against additional exposure on the internet.


To find more technical details, threats, insights, and recommendations in protecting your NAS device, download our research **“[Backing Your Backup: Defending NAS Devices Against Evolving Threats](https://www.trendmicro.com/vinfo/us/security/news/internet-of-things/reinforcing-nas-security-against-pivoting-threats).”**  










## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=REvil]] [[action.malware.name=REvil]] [[action.malware.name=REvil]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Nas]] [[Ransomware]] [[Malware]] [[Revil]] [[Stealthworker]] [[Revix]] [[Qnap]] [[Botnet]] [[Trend Micro]]

