# DazzleSpy: Pro-democracy org hijacked to become macOS spyware distributor | ZDNet
### A Safari exploit was being served through a watering hole attack.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/dazzlespy-pro-democracy-org-hijacked-to-become-macos-spyware-distributor/
+ Date: 2022-01-26 11:41:09
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/ed6402dbd0ddd1722c4bdfc62a956991a62e60d0/2021/06/23/a770b6fe-2aac-41d5-adc6-6d4bd356db60/code-development.jpg?width=770&height=578&fit=crop&auto=webp)

Researchers have uncovered a new strain of macOS malware in targeted attacks against visitors to a Hong Kong pro-democracy radio station website. 


The website was used to facilitate a watering hole attack and to serve a Safari browser exploit to visitors, leading to the deployment and execution of spyware on victim machines. 

Dubbed [DazzleSpy by ESET](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/) researchers, the malware is a backdoor for conducting surveillance on an infected Mac.  

ESET's investigation follows past research conducted by Google's [Threat Analysis Group](https://blog.google/threat-analysis-group/analyzing-watering-hole-campaign-using-macos-exploits/) (TAG) security team. On November 11, 2021, TAG said watering hole attacks had been spotted on a media outlet and pro-democracy political website targeting Hong Kong residents.  

This attack utilized an XNU privilege escalation vulnerability in macOS Catalina, leading to the execution of the backdoor malware.  

Now tracked as [CVE-2021-30869](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30869), the type confusion zero-day flaw has now been patched by Apple.  

"Based on our findings, we believe this threat actor to be a well-resourced group, likely state-backed, with access to their own software engineering team based on the quality of the payload code," Google TAG said.  






ESET has now provided a breakdown of additional attack vectors used and the exploit itself.  

The legitimate pro-democracy online radio station D100 was compromised to serve the payload via an iframe between September 30 and November 4, 2021. In addition, fake 'liberate Hong Kong' websites also delivered the malware. 

"Both distribution methods have something in common: they attract visitors from Hong Kong with pro-democracy sympathies," ESET says. "It seems that they were the primary target of this threat." 

The attack chain begins by running a script that checks what version of macOS is installed. JavaScript containing exploit code, mac.js, is deployed to trigger the WebKit [engine flaw](https://github.com/wangtielei/Slides/blob/main/mosec21.pdf). (While technical details are scant, the researchers confirmed that Apple's patch now resolves [CVE-2021-30869](https://nvd.nist.gov/vuln/detail/CVE-2019-8526).) 

It appears the exploit is used to obtain memory read and write access, with object address leaks and the ability to create fake JavaScript objects being the overall goal. The next step requires a Mach-O executable to be loaded into memory and to achieve code execution through a local privilege escalation weakness, allowing it to run as root and execute the next payload.  

In ESET's sample, the payload differs from TAG's findings. The new DazzleSpy macOS malware has a range of capabilities including collecting macOS data such as hardware UUIDs and serial numbers, extracting Wi-FI SSIDs, downloading user files on the infected machine, enumerating files in Desktop, Downloads, and Documents folders, launching remote sessions, and executing shell commands.

ESET says that the malware will also see if it is possible to take advantage of [CVE-2019-8526](https://nvd.nist.gov/vuln/detail/CVE-2019-8526), a critical vulnerability fixed in macOS Mojave 10.14.4. If the macOS version is below 10.14.4, keychain information is stolen. 

Once it has connected to a C2, secure communication appears to be a high priority.  

"In practice, the same self-signed certificate is used for both the CA and the C&C server," the researchers say. "The technique protects the malware's communications from potential eavesdropping by refusing to send data if end-to-end encryption is not possible." 

The cybersecurity researchers also say that the watering hole attack used has similarities with the deployment of the LightSpy implant. Kaspersky [said in 2020](https://securelist.com/ios-exploit-chain-deploys-lightspy-malware/96407/) that the malware appeared on websites aimed at residents of Hong Kong. The cybersecurity firm temporarily named the advanced persistent threat (APT) group believed to be responsible as TwoSail Junk.    

Trend Micro has also [published research](https://documents.trendmicro.com/assets/Tech-Brief-Operation-Poisoned-News-Hong-Kong-Users-Targeted-with-Mobile-Malware-via-Local-News-Links.pdf) (.PDF) on the threat actor's mobile activities.  

"We cannot confirm at this point whether both campaigns are from the same group," ESET noted.  

###  Previous and related coverage

* [Chinese APT deploys MoonBounce implant in UEFI firmware](https://www.zdnet.com/article/chinese-apt-deploy-moonbounce-malware-in-uefi-firmware/)
* [Researchers break down WhisperGate wiper malware used in Ukraine website defacement](https://www.zdnet.com/article/researchers-break-down-whispergate-wiper-malware-used-in-ukraine-website-defacement/)
* [Ransomware in 2022: We're all screwed](https://www.zdnet.com/article/ransomware-in-2022-were-all-screwed/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0 



---





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=Wiper]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Ukraine]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Malware]] [[Macos]] [[Eset]] [[Pro-democracy]] [[Website]] [[ZDNet]]
#### CVE's
[[CVE-2021-30869]] [[CVE-2019-8526]]

