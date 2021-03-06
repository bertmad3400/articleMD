# New MoonBounce UEFI bootkit can't be removed by replacing the hard drive
### Security researchers from Kaspersky said on Thursday that they had discovered a novel bootkit that can infect a computer's UEFI firmware.

## Information:
+ Source: The Record
+ Link: https://therecord.media/new-moonbounce-uefi-bootkit-cant-be-removed-by-replacing-the-hard-drive/
+ Date: 2022-01-21T18:47:08+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2022/01/moon-night-sky-cloud.jpg)

Security researchers from Kaspersky said on Thursday that they had discovered a novel bootkit that can infect a computer’s UEFI firmware.


What makes [MoonBounce](https://securelist.com/moonbounce-the-dark-side-of-uefi-firmware/105468/)—the name they gave the bootkit—special is the fact that the malware doesn’t burrow and hide inside a section of the hard drive named ESP (EFI System Partition), where some UEFI code typically resides, but instead it infects the SPI flaws memory that is found on the motherboard.


This means that, unlike similar bootkits, defenders can’t reinstall the operating system and replace the hard drive, as the bootkit will continue to remain on the infected device until the SPI memory is re-flashed (a very complex process) or the motherboard is replaced.


According to Kaspersky, MoonBounce marks the third UEFI bootkit they have seen so far that can infect and live inside the SPI memory, following previous cases such as [LoJax](https://www.welivesecurity.com/2018/09/27/lojax-first-uefi-rootkit-found-wild-courtesy-sednit-group/) and [MosaicRegressor](https://securelist.com/mosaicregressor/98849/).


Furthermore, MoonBounce’s discovery also comes after researchers have also found additional UEFI bootkits in recent months, such as [ESPectre](https://www.welivesecurity.com/2021/10/05/uefi-threats-moving-esp-introducing-especter-bootkit/), [FinSpy’s UEFI bootki](https://securelist.com/finspy-unseen-findings/104322/)t, and [others](https://securelist.com/apt-trends-report-q3-2021/104708/), which has led the Kaspersky team to conclude that what was once considered unachievable following the rollout of the UEFI standard has gradually become the norm.


### MoonBounce linked to China’s APT41


As for MoonBounce itself, the researchers said that the bootkit had been used as a way to maintain access to an infected host and deploy second-stage malware to carry out various operations.


Researchers said they found MoonBounce deployed only once—on the network of a transportation services company—and that based on the other malware deployed on the infected network, they believe the bootkit is the work of APT41, a cyber-espionage group believed to work on behalf of the Chinese government.


Evidence to this stands the fact that both MoonBounce and the malware found on the victim’s network were often seen communicating with the same server infrastructure, from where they most likely received instructions from APT31.


The only detail that remained a mystery to the Kaspersky team was how the bootkit was installed in the first place.


“As a safety measure against this attack and similar ones, it is recommended to update the UEFI firmware regularly and verify that BootGuard, where applicable, is enabled. Likewise, enabling Trust Platform Modules, in case a corresponding hardware is supported on the machine, is also advisable,” the Kaspersky team said.





## Tags:

#### Threatactor:
[[threatactor.name=APT3]] [[threatactor.name=APT41]] [[threatactor.name=ZIRCONIUM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=FinFisher]] [[action.malware.name=LoJax]] [[action.malware.name=Net]] [[action.malware.name=Reg]]

#### Industry:
[[victim.industry.name=Transportation]]

#### Location:
[[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Bootkit]] [[Uefi]] [[Moonbounce]] [[Kaspersky]] [[Malware]] [[Spi]] [[The Record]]

