# Now Iran's state-backed hackers are turning to ransomware
### Iranian ransomware attacks are being launched in waves every six to eight weeks on average.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/now-irans-state-backed-hackers-are-turning-to-ransomware/)
+ Date: November 17, 2021
+ Author: Liam Tung


## Article:
Unknown

Microsoft has detailed the activities of six Iranian hacker groups that are behind waves of ransomware attacks that have arrived every six to eight weeks since September 2020. 

Russia is often seen as the home of the biggest cyber-criminal ransomware threats, but state-sponsored [attackers from North Korea](https://www.zdnet.com/article/on-the-three-year-anniversary-of-wannacry-us-exposes-new-north-korean-malware/) and Iran have also shown a growing interest in ransomware. 


Microsoft said Iranian hacking groups are using ransomware to either collect funds or disrupt their targets, and are "patient and persistent" while engaging with their targets – although they will use aggressive brute-force attacks.

**SEE:** [**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/#link=%7B%22role%22:%22standard%22,%22href%22:%22http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22%3Cstrong%3EA%20winning%20strategy%20for%20cybersecurity%3C/strong%3E%22%7D) **(ZDNet special report)**

The most consistent of the six Iranian threat groups is one Microsoft tracks as Phosphorus (others call it APT35). Microsoft has been playing cat and mouse with the group [for the past two years](https://www.zdnet.com/article/microsoft-these-iranian-attackers-are-targeting-high-profile-conference-attendees/). While initially [known for cyber espionage](https://www.zdnet.com/article/microsoft-takes-control-of-99-domains-operated-by-iranian-state-hackers/), Microsoft details the group's strategies for deploying ransomware on targeted networks, often using Microsoft's Windows disk-encryption tool BitLocker to encrypt victim files. 

Other cybersecurity firms last year [detected a rise in ransomware from Iranian state-backed hackers](https://www.zdnet.com/article/iranian-state-hacker-group-linked-to-ransomware-deployments/) using known Microsoft Exchange vulnerabilities to install persistent web shells on email servers and Thanos ransomware.    

According to Microsoft, Phosphorus was also targeting unpatched on-premise Exchange servers and Fortinet's FortiOS SSL VPN in order to deploy ransomware.






In the second half of 2021, the group started scanning for the four Exchange flaws known as ProxyShell that were initially [exploited as zero days by Beijing-backed hackers.](https://www.zdnet.com/article/uk-white-house-blames-china-for-microsoft-exchange-server-hack/)

Microsoft released patches for CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, and CVE-2021-27065 in April. ProxyLogon was one of several exploits that made up ProxyShell. 

An [account by security specialist DFIR Report](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/#link=%7B%22linkText%22:%22DFIR%20Report's%20account%20of%20the%20same%20group's%20activity%22,%22target%22:%22_blank%22,%22href%22:%22https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D) notes Phosphorus used BitLocker on servers and DiskCryptor on PCs. Their activity stood out because it didn't rely on ransomware-as-a-service offerings that are popular among cyber criminals and didn't create custom encryptors. 

"After compromising the initial server (through vulnerable VPN or Exchange Server), the actors moved laterally to a different system on the victim network to gain access to higher value resources," [the Microsoft Threat Intelligence Center (MSTIC) notes in a blogpost](http://v). 

"From there, they deployed a script to encrypt the drives on multiple systems. Victims were instructed to reach out to a specific Telegram page to pay for the decryption key."

The group also tries to steal credentials by sending "interview requests" to targeted individuals through emails that contain tracking links to confirm whether the user has opened the file. Once a response is received from the target user, the attackers send a link to a list of interview questions and then a link to a fake Google Meeting, which would steal login details.

**SEE:** [**Ransomware: It's a 'golden era' for cyber criminals - and it could get worse before it gets better**](https://www.zdnet.com/article/ransomware-its-a-golden-era-for-cyber-criminals-and-it-could-get-worse-before-it-gets-better/)

Other groups mentioned in Microsoft's report included an emerging Iranian hacking group that recently [targeted Israel and US organizations in the Persian Gulf with password-spraying attacks](https://www.zdnet.com/article/microsoft-warns-over-password-attacks-against-250-office-365-customers/). 

Microsoft highlights that the adoption of ransomware aided the Iranian hackers' efforts in espionage, disruption and destruction, and to support physical operations. Their arsenal of attacks included ransomware, disk wipers, mobile malware, phishing, password-spray attacks, mass exploitation of vulnerabilities, and supply chain attacks.        





#### Tags:
[[Microsoft]] [[ransomware]] [[ransomware.]] [[ZDNet]]
