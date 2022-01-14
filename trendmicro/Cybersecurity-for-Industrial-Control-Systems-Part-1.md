# Cybersecurity for Industrial Control Systems: Part 1
### In this two-part series, we look into various cybersecurity threats that affected industrial control systems (ICS) endpoints.

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/22/a/cybersecurity-industrial-control-systems-ics-part-1.html
+ Date: 2022-01-15
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/cybersecurity-for-industrial-control-systems-part-1/Threats-Affecting-ICS-Endpoints.jpg)





The ever-changing technological landscape has made it possible for the business process on the IT side of an enterprise to be interconnected with the physical process on the OT side. While this advancement has improved visibility, speed, and efficiency, it has exposed industrial control systems (ICSs) to threats affecting IT networks for years.


Our expert team extensively looked into reported specific malware families in ICS endpoints to validate ICS security and establish a global baseline for examining threats that put these systems at risk. By doing so, this can help identify the choice of malware and unveil the attackers’ motivation, skill levels as well as gather insights about the affected network’s ecosystem and cybersecurity hygiene.


An overview of the IT/OT network and ICS endpoints


IT/OT network pertains to the convergence of the IT and OT network—a connection of the business process on the IT side with the physical process on the OT side. The IT/OT network enables data exchange and the monitoring and control of the operations from the IT network.


On the other hand, ICS endpoints are used in the design, development, monitoring, and control of industrial processes. These have specific software to perform important functions. Examples of these software applications are:


* Industrial automation suites, such as Siemens’ Totally Integrated Automation, Kepware’s KEPServerEX, and Rockwell Automation’s FactoryTalk.
* Engineering Workstation (EWS), which is used in the programming of an industrial process or workflow. This includes:
	+ Control systems such as Mitsubishi Electric’s MELSEC GX Works or Phoenix Contact’s Nanonavigator
	+ HMI (Human Machine Interface) such as MELSEC GT Works or Schneider’s GP-PRO EX
	+ Robot programming software such as ABB Robotstudio
	+ Design software such as Solidworks
	+ Historian software such as Honeywell’s Uniformance
	+ Supervisory Control and Data Acquisition (SCADA) such as Siemens’ Simatic WinCC SCADA
	+ Field device management and configuration such as PACTware and Honeywell’s EZconfig
	+ Converters for serial to USB connections such as Moxa’s Uport


ICS data through the looking glass


We analyzed data from ICS endpoints that are part of the IT/OT network, not including ICS endpoints from air-gapped systems or those without an internet connection. These endpoints can be found in different IT/OT network levels, except the process and control levels. Moreover, the ICS endpoints we identified were running Windows operating systems.






![ICS endpoints, highlighted, as shown in a Purdue model architecture](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/cybersecurity-for-industrial-control-systems-part-1/diagram-ics-endpoints.png)





*Figure 1. ICS endpoints, highlighted, as shown in a Purdue model architecture*


We filtered out obvious test machines, endpoints used by penetration testers, and endpoints from universities to ensure that our data came from real ICSs and that the malware detection data was not skewed by penetration testers, researchers, and student machines.


Additionally, we determined ICS endpoints using various indicators like file names, file paths, and processes reported to the [Trend Micro Smart Protection Network](/en_us/business/technologies/smart-protection-network.html). We processed the relevant data in compliance with our Data Collection Disclosure policy, maintaining customer anonymity throughout the process.


After extensively evaluating the data gathered, we discovered various malware threats that continue to pose a cybersecurity risk to ICS endpoints, including the age-old legacy malware as well as ransomware.


Post-intrusion ransomware






![Breakdown of ransomware that affected industrial control systems](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/cybersecurity-for-industrial-control-systems-part-1/diagram-ransomware-breakdown.png)




*Figure 1. Breakdown of ransomware that affected industrial control systems*


We discovered that there was a significant rise in ransomware activity affecting ICSS. This was mostly due to increased Nefilim, Ryuk, LockBit, and Sodinokibi attacks from September to December of that year. When combined, these ransomware make up over 50% of the attacks affecting ICSs.






![Per country breakdown of organization-related ransomware detections for industrial control systems](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/cybersecurity-for-industrial-control-systems-part-1/diagram-ransomware-breakdown-per-country.png)




*Figure 2. Per country breakdown of organization-related ransomware detections for industrial control systems*


Additionally, we discovered that the US had the most number of organization-related incidents affecting ICSs. India, Spain, and Taiwan came in second. However, Vietnam, Spain, and Mexico would be the top three countries if we took the percentage of organizations running industrial control systems that had ransomware affecting their systems.


Coinmakers






![Breakdown of coinminers affecting industrial control systems](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/cybersecurity-for-industrial-control-systems-part-1/diagram-coinminers-breakdown.png)




*Figure 3. Breakdown of coinminers affecting industrial control systems*


Apart from ransomware, coinminers also greatly affected ICS endpoints that we analyzed. These are malicious software aiming to abuse computer resources to mining cryptocurrencies.


MALXMR is the top coinminer that affected the most ICSs. WORM\_COINMINER and TOOLMXR also affected a total of 30.8% ICSs that year.






![MALXMR distribution per country and organization](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/cybersecurity-for-industrial-control-systems-part-1/diagram-malxmr-breakdown.png)




*Figure 4. MALXMR distribution per country and organization*


The most affected country by MALXR was India. However, note that this doesn’t mean that the country was specifically targeted by MALXR gangs. It just suggests that India had the most infections as a lot of computers running ICS software are vulnerable to EternalBlue, which exploits SMBv1 vulnerabilities.


Conficker






![OS distribution of ICS endpoints with Conficker detections](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/cybersecurity-for-industrial-control-systems-part-1/diagram-distribution-of-ics-endpoints.png)




*Figure 5. OS distribution of ICS endpoints with Conficker detections*


Similar to what we found on [Security in the Era of Industry 4.0: Dealing With Threats to Smart Manufacturing Environments](https://www.trendmicro.com/vinfo/us/security/news/internet-of-things/security-in-the-era-of-industry-4-dealing-with-threats-to-smart-manufacturing-environments?_ga=2.209525010.1874680133.1621125958-1328426616.1593403903), we still saw Conficker or Downad as a persistent threat for ICS endpoints.


We discovered that Window 10 and 7 OSs were the most affected2. However, they were not affected using MS08-067, one of the most common propagation techniques used to spread Confickers. This means that these infections were propagated using either removable drivers or dictionary attacks on ADMIN$ share.






![Location of Conficker detections based on file path](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/cybersecurity-for-industrial-control-systems-part-1/diagram-location-conflicker-detection.png)




*Figure 6. Location of Conficker detections based on file path*


At least 85% of the Conficker detections were detected from removable drives. Additionally, at least 12% % of the detections were found only on the Windows system directory.


Legacy Malware






![Breakdown of legacy malware detected in ICS endpoints](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/cybersecurity-for-industrial-control-systems-part-1/diagram-legacy-malware-breakdown.png)




We also detected old worm malware primarily propagated via network shares or removable USB drives. SALITY affected 1.5% of ICSs, while RAMNIT and AUTORUN infected 1.3% and 1% of ICSs, respectively. Some of these worms were rampant in 2013 and 2014 but have since been prevented as security policies have disabled autorun.


However, file transfer via USB thumb drives allows for their continued propagation. Moreover, creating system backups or cold standby terminals without performing a security scan allow these worms’ continuous spread.


[In part two of this blog entry](/en_us/research/22/a/cybersecurity-for-industrial-control-systems-part-2.html), well discuss malware detection in the top 10 countries as well as some useful insights and recommendations to make your ICSs more robust and resilient to mitigate such threats.








## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conficker]] [[action.malware.name=Conti]] [[action.malware.name=Miner-C]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=REvil]] [[action.malware.name=REvil]] [[action.malware.name=Ryuk]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Manufacturing]] [[victim.industry.name=Manufacturing]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.country.name=Vietnam]] [[victim.continent.name=Asia]] [[victim.country.name=Spain]] [[victim.continent.name=Europe]] [[victim.country.name=Mexico]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ics]] [[Icss]] [[Ransomware]] [[Malware]] [[It/ot]] [[Conficker]] [[Usb]] [[Trend Micro]]

