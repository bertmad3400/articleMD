# New Tomiris backdoor likely developed by SolarWinds hackers
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-tomiris-backdoor-likely-developed-by-solarwinds-hackers/)
+ Date: September 29, 2021
+ Author: Sergiu Gatlan


## Article:
![New Tomiris backdoor likely developed by SolarWinds hackers](https://www.bleepstatic.com/content/hl-images/2021/08/25/silhouette_headpic.jpg)


Kaspersky security researchers have discovered a new backdoor likely developed by the Nobelium hacking group behind last year's SolarWinds supply chain attack.


This comes on the heels of another report published by Microsoft two days ago [detailing FoggyWeb](https://www.bleepingcomputer.com/news/security/microsoft-nobelium-uses-custom-malware-to-backdoor-windows-domains/), a "passive and highly targeted" backdoor developed and used by the same group to exfiltrate sensitive information from compromised AD FS servers remotely.


The new malware found by Kaspersky, dubbed **Tomiris**, was first spotted in June even though the first samples were deployed in the wild in February 2021, one month before the "sophisticated second-stage backdoor" [Sunshuttle](https://www.bleepingcomputer.com/news/security/fireeye-finds-new-malware-likely-linked-to-solarwinds-hackers/) was found by FireEye and linked to Nobelium.


Tomiris was discovered while investigating a series of DNS hijacking attacks targeting several government zones of a CIS member state between December 2020 and January 2021, which allowed the threat actors to redirect traffic from government mail servers to machines under their control


Their victims were redirected to webmail login pages that helped the attackers to steal their email credentials and, in some cases, prompted them to install a malicious software update that instead downloaded the previously unknown Tomiris backdoor.


"During these time frames, the authoritative DNS servers for the zones above were switched to attacker-controlled resolvers. These hijacks were for the most part relatively brief and appear to have primarily targeted the mail servers of the affected organizations," Kaspersky [said](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/).


"We do not know how the threat actor was able to achieve this, but we assume they somehow obtained credentials to the control panel of the registrar used by the victims."



![Malicious webmail login page used to delive Tomiris](https://www.bleepstatic.com/images/news/u/1109292/2021/Malicious%20webmail%20login%20page%20used%20to%20delive%20Tomiris.png)*Image: Kaspersky*
Links to Nobelium-made Sunshuttle malware
-----------------------------------------


Once deployed on a system, Tomiris will repeatedly query a command-and-control server for further malicious payloads to run on the compromised device, allowing its operators to establish a foothold in the victim's network.


Another variant can collect and exfiltrate documents out of compromised systems, automatically uploading recent files matching extensions of interest, including .doc, .docx, .pdf, .rar, and more.


Kaspersky found many similarities between the two backdoors (e.g., both developed in Go, persistence through scheduled tasks, same encoding scheme for C2 comms, automated sleep triggers to reduce network noise).


They also spotted the Kazuar backdoor who shares features with the Sunburst malware used in the SolarWinds attack on the same network as Tomiris.


Despite this, the researchers did not conclusively link the new backdoor to the Russian-backed Nobelium state hackers because of the possibility of a false flag attack designed to mislead malware researchers.


"While it is possible that other APTs were aware of the existence of this tool at this time, we feel it is unlikely they would try to imitate it before it was even disclosed," Kaspersky added.


"A much likelier (but yet unconfirmed) hypothesis is that Sunshuttle's authors started developing Tomiris around December 2020 when the SolarWinds operation was discovered, as a replacement for their burned toolset."



![Tomiris Sunshuttle Kazuar connection](https://www.bleepstatic.com/images/news/u/1109292/2021/Tomiris_Sunshuttle_connection_.png)*Image: Kapersky*
Who is Nobelium?
----------------


[Nobelium](https://www.bleepingcomputer.com/news/security/microsoft-russian-svr-hackers-target-govt-agencies-from-24-countries/), the hacking group that carried out the [SolarWinds supply-chain attack](https://www.bleepingcomputer.com/news/security/the-solarwinds-cyberattack-the-hack-the-victims-and-what-we-know/) that led to the compromise of multiple US federal agencies, is the hacking division of the Russian Foreign Intelligence Service (SVR), also tracked as APT29, The Dukes, or Cozy Bear.


In April 2021, the United States government [formally blamed the SVR division](https://www.bleepingcomputer.com/news/security/us-government-confirms-russian-svr-behind-the-solarwinds-hack/) for coordinating the SolarWinds "broad-scope cyber espionage campaign."


Cybersecurity outfit Volexity also [linked the attacks to the same hacking group's operators](https://www.volexity.com/blog/2021/05/27/suspected-apt29-operation-launches-election-fraud-themed-phishing-campaigns/) based on tactics they used in previous incidents going back to 2018.


In May, Microsoft researchers [revealed four more malware families](https://www.bleepingcomputer.com/news/security/microsoft-russian-hackers-used-4-new-malware-in-usaid-phishing/) used by Nobelium in other attacks: a malware downloader known as 'BoomBox,' a shellcode downloader and launcher known as 'VaporRage,' a malicious HTML attachment dubbed 'EnvyScout,' and a loader named 'NativeZone.'


In March, they detailed [three other Nobelium malware strains](https://www.bleepingcomputer.com/news/security/microsoft-reveals-3-new-malware-strains-used-by-solarwinds-hackers/) used for maintaining persistence on compromised networks: a command-and-control backdoor dubbed 'GoldMax,' an HTTP tracer tool tracked as 'GoldFinder,' a persistence tool and malware dropper named 'Sibot.'




#### Tags:
[[malware]] [[Kaspersky]] [[SolarWinds]] [[Tomiris]] [[Sunshuttle]] [[Bleeping Computer]]
