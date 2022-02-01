# State-sponsored Iranian hackers attack Turkish government, private organizations | ZDNet
### MuddyWater is impersonating the Turkish Health and Interior Ministries to sink its claws into victim networks.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/state-sponsored-iranian-hackers-attack-turkish-govt-organizations/
+ Date: 2022-02-01 10:17:45
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/8f786d318672a408c41fc69b083c60f3d9df00fe/2022/01/17/e0e7d48d-443e-4c48-be8d-bf0c83859c7c/phishing.jpg?width=770&height=578&fit=crop&auto=webp)

A state-sponsored Iranian hacking group has pivoted to attacks against high-profile targets in Turkey. 


This week, cybersecurity researchers from Cisco Talos said that MuddyWater, an advanced persistent threat (APT) group with ties to Iran's Ministry of Intelligence and Security (MOIS), has been linked to campaigns against private organizations in Turkey alongside the country's government. 

Active since at least 2017, MuddyWater, also known as Mercury or Static Kitten, has been tied to attacks against organizations in the US, Israel, Europe, and the Middle East in the past.  

Earlier this year, US Cyber Command [linked the APT](https://www.cybercom.mil/Media/News/Article/2897570/iranian-intel-cyber-suite-of-malware-uses-open-source-tools/) to the Iranian government, saying that MuddyWater is one of many groups "conducting Iranian intelligence activities." 

"MuddyWater is a subordinate element within the MOIS," US Cyber Command says. "According to the Congressional Research Service, the MOIS "conducts domestic surveillance to identify regime opponents. It also surveils anti-regime activists abroad through its network of agents placed in Iran's embassies."" 

According to [Talos researchers](https://blog.talosintelligence.com/2022/01/iranian-apt-muddywater-targets-turkey.html) Asheer Malhotra and Vitor Ventura, the latest MuddyWater campaign, dating back from November 2021, is utilizing malicious PDFs and Microsoft Office documents as an initial attack vector.  

Phishing emails containing these malicious attachments are spoofed to appear to be from the Turkish Health and Interior Ministries. Targets included the Scientific And Technological Research Council of Turkey (Tubitak). 






The malicious documents contained embedded VBA macros designed to trigger a PowerShell script, leading to the execution of a downloader for executing arbitrary code, the creation of a registry key for persistence, and the use of Living Off the Land Binaries (LOLBins) to hijack the machine.  

Once inside a target system, MuddyWater tends to focus on three aims: conducting cyberespionage for state interests; stealing intellectual property with a high economic value, and deploying ransomware to deliberately disrupt a victim organization's operators or to "destroy evidence of their intrusions," according to Talos.  

However, the researchers were not able to secure the final payload in this campaign due to verification checks on the operator's command-and-control (C2) server. 

The APT has also adopted canary tokens to keep track of their intrusions. Canary tokens are digital "canaries" that warn that a file has been opened – and while often used by defenders to detect and [monitor potential breaches](https://www.fortinet.com/resources/cyberglossary/what-is-canary-in-cybersecurity), cyberattackers can also use them to track successful infections.  

"Tracking tokens may also be used as another means of anti-analysis: timing checks," Talos says. "A reasonable timing check on the duration between the token requests and the request to download a payload can indicate automated analysis. [...] Tracking tokens can also be a method to detect the blocking of the payload server. If they keep receiving requests to the token but not to the payload server, that is an indication of their payload server being blocked, and by whom." 

An advisory issued by Trakya and the Turkey National Cyber Incident Response Center (USOM) warning of an APT-level attack listed IPs and an email address that were also uncovered in the Talos analysis of this campaign.  

###  Previous and related coverage

* [Donot Team APT will strike gov't, military targets for years - until they succeed](https://www.zdnet.com/article/donot-team-apt-will-strike-govt-targets-for-years-until-they-succeed/)
* [New advanced hacking group targets governments, engineers worldwide](https://www.zdnet.com/article/new-advanced-hacking-group-targets-governments-engineers-worldwide/)
* [Chinese APT deploys MoonBounce implant in UEFI firmware](https://www.zdnet.com/article/chinese-apt-deploy-moonbounce-malware-in-uefi-firmware/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Threatactor:
[[threatactor.name=MuddyWater]] [[threatactor.name=MuddyWater]] [[threatactor.name=MuddyWater]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.country.name=Israel]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Turkey]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Talos]] [[Muddywater]] [[ZDNet]]

