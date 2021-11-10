# North Korean hackers target the South's think tanks through blog posts
### Responsibility for new attacks has been laid at the feet of the Kimsuky threat group.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/north-korean-hackers-target-the-souths-think-tanks-through-blog-posts/)
+ Date: November 10, 2021
+ Author: Charlie Osborne


## Article:
Unknown

A North Korean hacking group has been attacking think tanks in the South through malware-laden blog posts. 


In a new campaign, tracked since June 2021, the state-sponsored advanced persistent threat (APT) group has been attempting to plant surveillance and theft-based malware on victim machines. 

On Wednesday, researchers from Cisco Talos said the [Kimsuky APT](https://blog.talosintelligence.com/), also known as Thallium or Black Banshee, is responsible for the wave of attacks, in which malicious Blogspot content is being used to lure "South Korea-based think tanks whose research focuses on political, diplomatic, and military topics pertaining to North Korea, China, Russia, and the US." 

Specifically, geopolitical and aerospace organizations appear to be on the APT's radar.  

Kimsuky has been active since at least 2012. The US Cybersecurity and Infrastructure Security Agency (CISA) issued [an advisory](https://us-cert.cisa.gov/sites/default/files/publications/TLP-WHITE_AA20-301A_North_Korean_APT_Focus_Kimsuky.pdf) (.PDF) on the APT in 2020, noting that the state-sponsored group is tasked by the North Korean government with "global intelligence gathering." Past victims have been located in South Korea, Japan, and the United States. 

[AhnLab says](https://asec.ahnlab.com/en/24443/) that compensation forms, questionnaires, and research documents attached to emails have been used in the past as phishing lures, and in the campaign detected by Talos, malicious Microsoft Office documents are still a primary attack vector. 

Typically, malicious VBA macros are included in the documents, and when triggered, will download the payloads from Blogspot.  






According to the team, the blogposts deliver three types of malicious content based on the [Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)/Brave Prince malware family: initial beacons, file stealers, and implant deployment scripts -- the latter of which is designed to infect endpoints and launch further malware components, including a keylogger, information stealer, and a file injector module for website login credential theft. 

While some APTs will try to steal whatever content they can from an infected machine, Kimsuky has adopted a different approach. The threat actors will, instead, scan for files of particular interest to them.  

This includes content related to North Korea, denuclearization, the relationships between the US, China, and Russia, as well as rocket designs, aviation fuel research, fluid mechanics, and material science.  

"The attackers knew exactly which files they were looking for," Talos commented. "This indicates that the attackers have a deep understanding of their targets' endpoints, likely obtained from previous compromises."

The researchers informed Google of their findings and the malicious blog content has since been removed. However, this is unlikely to stop Kimsuky's activities.   

"Kimsuky is a highly motivated threat actor targeting a number of entities in South Korea," the researchers say. "This group has been relentlessly creating new infection chains to deliver different types of malware to their victims. Such targeted attacks can result in the leak of restricted research, unauthorized access for espionage, and even destructive attacks against target organizations." 

###  Previous and related coverage

* [Cyberattackers are now quietly selling off their victim's internet bandwidth](https://www.zdnet.com/article/cyberattackers-are-now-quietly-selling-off-their-victims-internet-bandwidth/)
* [Turla hacking group launches new backdoor in attacks against US, Afghanistan](https://www.zdnet.com/article/turla-hacking-group-launches-new-backdoor-in-attacks-against-us-afghanistan/)
* [Cisco researchers spotlight Solarmarker malware](https://www.zdnet.com/article/cisco-researchers-spotlight-solarmarker-malware/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[malware]] [[Kimsuky]] [[Korea,]] [[ZDNet]]
