# Chinese APT deploys MoonBounce implant in UEFI firmware | ZDNet
### The highly targeted attack reveals a new level of sophistication in attacks against UEFI firmware.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/chinese-apt-deploy-moonbounce-malware-in-uefi-firmware/
+ Date: 2022-01-21 10:18:00
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/a5423c1a8b673ba79d137e9d683b3b9bcc81fb6a/2021/06/29/1b445116-bb3a-42ac-a646-e43829d1a46d/extracting-water-from-the-moon.jpg?width=770&height=578&fit=crop&auto=webp)

Security researchers have unveiled MoonBounce, a custom UEFI firmware implant used in targeted attacks. 


The implant is believed to be the work of APT41, a Chinese-speaking sophisticated hacking group also known as Winnti or Double Dragon. 

On January 20, [Kaspersky researchers](https://securelist.com/moonbounce-the-dark-side-of-uefi-firmware/105468/) said that at the end of last year, the team uncovered a case of Unified Extensible Firmware Interface (UEFI) compromise caused by the modification of one component in the firmware – a core element called SPI flash, located on the motherboard. 

"Due to its emplacement on SPI flash which is located on the motherboard instead of the hard disk, the implant is capable of persisting in the system across disk formatting or replacement," the team noted. 

Not only did the tweak to the firmware result in persistence at a level that is extremely difficult to remove, the team says that the firmware image was "modified by attackers in a way that allowed them to intercept the original execution flow of the machine's boot sequence and introduce a sophisticated infection chain." 

The developer of the MoonBounce UEFI rootkit is said to have a deep and thorough understanding of how UEFI systems work. 

"The source of the infection starts with a set of hooks that intercept the execution of several functions in the EFI Boot Services Table, namely AllocatePool, CreateEventEx and ExitBootServices," the researchers explained. "Those hooks are used to divert the flow of these functions to malicious shellcode that is appended by the attackers to the CORE\_DXE image, which in turn sets up additional hooks in subsequent components of the boot chain, namely the Windows loader." 






"This multistage chain of hooks facilitates the propagation of malicious code from the CORE\_DXE image to other boot components during system startup, allowing the introduction of a malicious driver to the memory address space of the Windows kernel." 

Kaspersky says that this single patch turned the UEFI firmware "into a highly stealthy and persistent storage for malware in the system" -- and one which was made more difficult to detect as there was no need to add new drivers or make further changes.  

In addition, the infection chain operates in memory-only, and so there are no traces on the hard drive of the fileless attack.  

Kaspersky has not been able to obtain a sample of the payload yet, nor has the team discovered how the initial infection took place – although it is presumed that the infection was achieved remotely.  

However, non-UEFI implants were found on the targeted network, including ScrambleCross/SideWalk malware, which communicated with the same infrastructure the attackers used. It was through the analysis of this activity that likely attribution has been possible.  

To the best of Kaspersky's knowledge, APT41 is the advanced persistent threat (APT) group behind the intrusion. The Chinese-speaking APT is a state-sponsored outfit believed to be responsible for widespread attacks against the IT sector, social media companies, telecoms, non-profits, and healthcare.  

In terms of the victim organization in this case, Kaspersky mentioned a target that "corresponds to an organization in control of several enterprises dealing with transport technology." 

In September 2020, the US Department of Justice (DoJ) [filed charges](https://www.zdnet.com/article/us-charges-five-hackers-part-of-chinese-state-sponsored-group-apt41/) against five suspected members of APT41. 

"We can now say that UEFI threats are gradually becoming a norm," Kaspersky says. "With this in mind, vendors are taking more precautions to mitigate attacks like MoonBounce, for example by enabling Secure Boot by default. We assess that, in this ongoing arms race, attacks against UEFI will continue to proliferate, with attackers evolving and finding ways to exploit and bypass current security measures." 

###  Previous and related coverage

* [Indian Patchwork hacking group infects itself with remote access Trojan](https://www.zdnet.com/article/indian-patchwork-hacking-group-infect-themselves-with-remote-access-trojan/)
* [Donot Team APT will strike gov't, military targets for years - until they succeed](https://www.zdnet.com/article/donot-team-apt-will-strike-govt-targets-for-years-until-they-succeed/)
* [SnatchCrypto campaign plants backdoors in crypto startups, DeFi, blockchain networks](https://www.zdnet.com/article/snatchcrypto-campaign-plants-backdoors-in-crypto-exchanges-defi-blockchain-networks/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Threatactor:
[[threatactor.name=APT41]] [[threatactor.name=Patchwork]] [[threatactor.name=RTM]] [[threatactor.name=Winnti Group]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=RTM]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Healthcare]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Uefi]] [[Kaspersky]] [[Moonbounce]] [[Apt41]] [[ZDNet]]

