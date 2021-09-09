# Fortinet warns customers after hackers leak passwords for 87,000 VPNs
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/fortinet-warns-customers-after-hackers-leak-passwords-for-87000-vpns/)
+ Date: September 9, 2021
+ Author: Catalin Cimpanu


## Article:
![Fortinet warns customers after hackers leak passwords for 87,000 VPNs](https://therecord.media/wp-content/uploads/2021/09/FortiGate.png)

Networking equipment vendor Fortinet has notified customers today that a cybercriminal gang has assembled a collection of access credentials for more than 87,000 FortiGate SSL-VPN devices.


“This incident is related to an old vulnerability resolved in May 2019,” the company said in a [blog post](https://www.fortinet.com/blog/psirt-blogs/malicious-actor-discloses-fortigate-ssl-vpn-credentials) following an inquiry from *The Record* sent on Tuesday, when a small portion of this larger list was published on a private cybercrime forum hosted on the dark web, and later on the website of a ransomware gang, [known to have close affiliations with the same forum](https://www.mcafee.com/blogs/enterprise/mcafee-enterprise-atr/how-groove-gang-is-shaking-up-the-ransomware-as-a-service-market-to-empower-affiliates/).


![forum-post](https://www-therecord.recfut.com/wp-content/uploads/2021/09/forum-post.jpg)Image: The Record [supplied by source]
![Groove-post](https://www-therecord.recfut.com/wp-content/uploads/2021/09/Groove-post.png)Image: The Record
“These credentials were obtained from systems that remained unpatched against [FG-IR-18-384](https://www.fortiguard.com/psirt/FG-IR-18-384) / [CVE-2018-13379](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-13379) at the time of the actor’s scan,” Fortinet said.


Sources familiar with the existence of this collection told *The Record* the list had been compiled more than a year ago and had been sold in private circles to different threat actors, including groups who carried out ransomware attacks.


While it would be illegal to grab Fortinet credentials and check if they were still valid, as this would amount to a CFAA violation, *The Record* was able to find two security researchers who tested the credentials from the sample leaked on the dark web hacking forum earlier this week.


The researchers, who publicly admit to being “[gray hats](https://en.wikipedia.org/wiki/Grey_hat)” but still did not want their names included in this article for legal reasons, said that from a list of 502,677 credentials, belonging to more than 12,800 Fortinet VPNs, the vast majority (varying from 80% to 90%, depending on scan) did not work anymore, or the login screen was protected by a two-factor authentication system.


This would explain why this small sample from a larger 87,000 collection would be leaked from professional data traders and their closed circles into the public domain.


![Fortinet-sample](https://www-therecord.recfut.com/wp-content/uploads/2021/09/Fortinet-sample-1024x333.png)Image: The Record
In the meantime, Fortinet is recommending that companies who use Fortinet SSL-VPN devices apply the patch for CVE-2018-13379, released back in May 2019, and rotate passwords for all device accounts after they install the patch.


In its blog post earlier today, the company pointed out that it had warned its customers five different times about this issue until now — in May 2019, August 2019, July 2020, April 2021, and again in June 2021.


While there are many reasons for delaying a patch, running crucial devices such as a FortiGate SSL-VPN system unpatched for two years has no excuse and amounts to derelict of duty on the part of some system administrators, especially after several cybersecurity agencies warned that Fortinet devices were among the favorite entry points for obth ransomware gangs and cyber-espionage groups alike.


A list of the IP addresses for the 12,800+ Fortinet SSL-VPN devices shared as part of the smaller sample leaked on the dark web earlier this week is [available on GitHub](https://gist.github.com/crypto-cypher/f216d6fa4816ffa93c5270b001dc4bdc), stripped of any credentials, which would allow Fortinet device owners to test if their systems were included on this leak.


*The Record has not named the hacking forum and ransomware gang who leaked this information because we are aware that the group had tried to use the leak to create awareness for their “services” and drive new users to their sites. Some of the group’s members gleefully rejoiced earlier when their leak was covered by several news outlets earlier this week and their names were mentioned.* 





#### Tags:
[[Fortinet]] [[SSL-VPN]] [[ransomware]] [[Image:]] [[The Record]]
