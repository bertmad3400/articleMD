# CISA releases advisory on Conti ransomware, notes increase in attacks after more than 400 incidents
### CISA did a deep dive on the Conti ransomware, providing information for those protecting organizations.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/cisa-releases-advisory-on-conti-ransomware-notes-increase-in-attacks-after-more-than-400-incidents/)
+ Date: September 23, 2021
+ Author: Jonathan Greig


## Article:
Unknown

CISA sent out an [advisory](https://us-cert.cisa.gov/ncas/alerts/aa21-265a) on Wednesday centered around the Conti ransomware, providing detailed information for the cybersecurity community about the ransomware group and its affiliates.  

Both CISA and the FBI said they have seen more than 400 attacks involving Conti's ransomware targeting US organizations as well as international enterprises. The FBI has [previously implicated](https://www.zdnet.com/article/fbi-identifies-16-conti-ransomware-attacks-striking-us-healthcare-first-responders/) Conti in attacks on at least 290 organizations in the US. CISA offered a technical breakdown on how the ransomware group's operators typically function and what steps organizations can take to mitigate potential attacks. 

CISA noted that while Conti operates a ransomware-as-a-service model, they do so a bit differently than others. Instead of paying affiliates a cut of the earnings that come from ransoms, the group pays the deployers of the ransomware a wage, according to CISA. 

Rob Joyce, director of cybersecurity at NSA, [said](https://www.cisa.gov/news/2021/09/22/cisa-fbi-and-nsa-release-conti-ransomware-advisory-help-organizations-reduce-risk) the cybercriminals now running the Conti ransomware-as-a-service have historically targeted critical infrastructure, such as the Defense Industrial Base (DIB). He added that the advisory highlights actions organizations can take right now to counter the threat.

"NSA works closely with our partners, providing critical intelligence and enabling operations to counter ransomware activities. We highly recommend using the mitigations outlined in this advisory to protect against Conti malware and mitigate your risk against any ransomware attack," Joyce said. 

On [Twitter](https://twitter.com/NSA_CSDirector/status/1440729546576125957), Joyce said Conti attacks are increasing and he urged organizations to use MFA, segment their networks and explore using a patch management system to keep networks updated. 

CISA explained that Conti actors typically use a variety of methods and tools to infiltrate systems, including spearphishing campaigns, remote monitoring and management software and remote desktop software.






The spearphishing campaigns seen by CISA used tailored emails that contain malicious attachments or links. 

Stolen or weak Remote Desktop Protocol (RDP) credentials, phone calls, fake software promoted via search engine optimization, other malware distribution networks like ZLoader and common vulnerabilities in external assets were all cited as tools Conti actors have used during ransomware attacks. 

"Malicious Word attachments often contain embedded scripts that can be used to download or drop other malware -- such as TrickBot and IcedID, and/or Cobalt Strike -- to assist with lateral movement and later stages of the attack life cycle with the eventual goal of deploying Conti ransomware," CISA explained. 

"In the execution phase, actors run a getuid payload before using a more aggressive payload to reduce the risk of triggering antivirus engines. CISA and FBI have observed Conti actors using Router Scan, a penetration testing tool, to maliciously scan for and brute force routers, cameras, and network-attached storage devices with web interfaces. Additionally, actors use Kerberos attacks to attempt to get the Admin hash to conduct brute force attacks." 

The operators of Conti's ransomware also have been seen using remote monitoring and management software as well as remote desktop software as backdoors to maintain persistence in a victim's network. 

CISA explained that sometimes the ransomware group and its affiliates use tools that are already on a victim's network or add tools like Windows Sysinternals and Mimikatz to "obtain users' hashes and clear-text credentials, which enable the actors to escalate privileges within a domain and perform other post-exploitation and lateral movement tasks."

The TrickBot malware is also used in some cases as a way to carry out other post-exploitation tasks.

The advisory noted that "artifacts from a recently leaked threat actor 'playbook,' identify IP addresses Conti actors have used for their malicious activity." The playbook also shows that Conti operators aim to exploit vulnerabilities in unpatched assets like the 2017 Microsoft Windows Server Message Block 1.0 server vulnerabilities, the "[PrintNightmare](https://www.zdnet.com/article/ransomware-now-attackers-are-exploiting-windows-printnightmare-vulnerabilities/)" vulnerability and the "Zerologon" vulnerability. 

"CISA and FBI have observed Conti actors using different Cobalt Strike server IP addresses unique to different victims. Conti actors often use the open-source Rclone command line program for data exfiltration," the advisory said. 

"After the actors steal and encrypt the victim's sensitive data, they employ a double extortion technique in which they demand the victim pay a ransom for the release of the encrypted data and threaten the victim with public release of the data if the ransom is not paid."

As Joyce said, CISA, the FBI and NSA suggested organizations segment their networks, filter traffic, scan for vulnerabilities and stay up-to-date with all patches. They added that unnecessary applications and apply controls should be removed, endpoint and detection response tools should be implemented and access should be limited across networks. 

Conti made a name for itself after [attacking hundreds of healthcare institutions](https://www.zdnet.com/article/fbi-identifies-16-conti-ransomware-attacks-striking-us-healthcare-first-responders/) -- including a debilitating ransomware attack on Ireland's Health Service Executive on May 14 -- as well as [schools](https://www.zdnet.com/article/conti-ryuk-joins-the-ranks-of-ransomware-gangs-operating-data-leak-sites/) like the University of Utah and other government organizations like the city government of [Tulsa, Oklahoma](https://www.zdnet.com/article/tulsa-warns-residents-that-police-citations-and-reports-leaked-to-dark-web-after-conti-ransomware-attack/) and [the Scottish Environment Protection Agency](https://www.zdnet.com/article/hackers-publish-thousands-of-files-after-government-agency-refuses-to-pay-ransom/).

Allan Liska, ransomware expert and member of the computer security incident response team at Recorded Future, said much of what was in the advisory was well-known in the information security community. But he noted that experts are not the target audience of the advisory. 

"There are a lot of security people who will find this very useful because the tools used by Conti are used by other ransomware groups. For example, rclone is mentioned in the report. I see rclone used by many ransomware groups but rarely by legitimate employees of an organization, so looking for rclone hashes on endpoints could be useful," Liska said. 

"I also think a lot of people didn't know that Conti has infected organizations through phone calls. That may be a new threat model for a lot of organizations and one that they have to consider how to defend against. Overall, while it is not a groundbreaking report, it is nice to have so many of Conti's TTP in a single location rather than combing through 15 different ZDNet articles to find them."





#### Tags:
[[Conti]] [[ransomware]] [[CISA]] [[malware]] [[said.]] [[rclone]] [[ZDNet]]
