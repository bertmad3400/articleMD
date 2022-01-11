# FIN7 Mailing Malicious USB Sticks to Drop Ransomware
### The FBI warned that attackers are impersonating Health & Human Services and/or Amazon to mail BadUSB-poisoned USB devices to targets in transportation, insurance & defense.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177541
+ Date: 2022-01-11T17:06:11+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/11114826/usb-santa-e1641919763991.jpeg)

Ransomware gangs are mailing malicious USB drives, posing as the U.S. Department of Health and Human Services (HHS) and/or Amazon to target the transportation, insurance, and defense industries for ransomware infection, the FBI warned on Friday.


In a security alert sent to organizations, the FBI said that [FIN7](https://threatpost.com/fin7-security-pros-ransomware-attacks/175681/) – aka Carbanak or Navigator Group, the infamous, financially motivated cybercrime gang behind the Carbanak backdoor malware – is the guilty party.


FIN7 has been around since at least 2015. Initially, the gang made its reputation by maintaining persistent access at target companies with its custom backdoor malware, and for targeting point-of-sale (PoS) systems with skimmer software. It often targeted [casual-dining restaurants](https://threatpost.com/chilis-doesnt-leave-data-breach-on-the-back-burner/131955/), casinos and hotels. But in 2020, FIN7 [got into](https://threatpost.com/fin7s-liquor-lure-law-firm-backdoor/168086/) the ransomware/data exfiltration game, with its activities involving [REvil](https://threatpost.com/revil-servers-offline-governments/175675/) or [Ryuk](https://threatpost.com/ryuk-ransomware-worming-self-propagation/164412/) as the payload.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The FBI said that over the past several months, FIN7 has mailed the malicious USB devices to US companies, in hopes that somebody would plug in the drives, infect systems with malware and thus set them up for future ransomware attacks.


“Since August 2021, the FBI has received reports of several packages containing these USB devices, sent to US businesses in the transportation, insurance, and defense industries,” the Bureau [said](https://therecord.media/fbi-fin7-hackers-target-us-companies-with-badusb-devices-to-install-ransomware/) in the security alert.


Snail-mailed BadUSB Infection
-----------------------------


“The packages were sent using the United States Postal Service and United Parcel Service,” the FBI added.


The attackers gussied up the packages, disguising them as either pandemic-related or as goodies from Amazon, the bureau said: “There are two variations of packages – those imitating HHS are often accompanied by letters referencing COVID-19 guidelines enclosed with a USB; and those imitating Amazon arrived in a decorative gift box containing a fraudulent thank you letter, counterfeit gift card, and a USB.”


Either way, the packages contained LilyGO-branded USB devices.


If targets fall for all the tinsel and flimflam and plug in the USB thumb drives, the FBI says that the devices execute a [BadUSB attack](https://threatpost.com/badusb-vulnerabilities-live-in-ics-gear-too/111142/). BadUSB attacks exploit an [inherent vulnerability](https://www.manageengine.com/data-security/security-threats/bad-usb.html) in USB firmware that enables bad actors to reprogram a USB device so it can act as a human interface device – i.e., as a malicious USB keyboard preloaded with automatically executed keystrokes. After reprogramming, the USB can be used to discreetly execute commands or run malicious programs on a victim’s computer.


Neither BadUSB attacks nor FIN7’s use of them are new. In 2020, the Trustwave SpiderLabs cybersecurity research team initially [discovered](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/would-you-exchange-your-security-for-a-gift-card/) these USB thumb drive attacks being sent to some of its customers, with the malicious devices similarly contained within packages impersonating Amazon and HHS. This latest attack is a carbon copy of the 2020 attack, when the FBI siilarly issued a public alert that named FIN7 as the culprit.


How to Beat Back Bad USB Sticks
-------------------------------


You’d think that the sure way to ward off attacks ushered in by evil USB-wielding sticks sprinkled through hallways, parking lots or via snail-mail would be drop-dead simple: i.e., don’t plug them in. Human nature being what it is, though, [study](https://threatpost.com/never-trust-a-found-usb-drive-black-hat-demo-shows-why/119653/) after study has shown that curiosity or altruism (“I’ll find out whose this is so I can return it!”) killed the cat and triggered system takeover.


Still, you have to at least try to talk people out of their USB curiosity and/or good manners. Karl Sigler, Trustwave SpiderLabs senior security research manager, told Threatpost on Monday that ongoing security awareness training “should include this type of attack and warn against connecting any strange device to your computer.”


End-point protection software can also help prevent these attacks, and it cuts the curious cat clean out of the picture, he said.


“These attacks are triggered by a USB stick emulating a USB keyboard, so an end-point protection software that can monitor access to command shells should take care of most issues,” Sigler said via email.


For critical systems that don’t require USB accessories, physical and software-based USB port blockers may also help prevent this attack, Sigler added.


For its part, the [ACA Group](https://www.acaglobal.com/) has coined the term CAPs to refer to the standard hygiene that all organizations should actively monitor to prevent a ransomware attack. CAPs refers to Configuration, Access, and Patching, with employee awareness and education again being considered critical as well. CAPs refer to:


**Configuration management** – Reduce the number of entry points an attacker could use to gain access to your system. Many attacks are successful because there are misconfigurations on security devices, cloud configurations and so forth.


**Access** – Reduce the number of internal access points for an attacker who has entered your system.


**Patching –** Reduce the chances of an attack happening via an unknown or entry point, a foundation in fixing and security vulnerabilities and other bugs.


*Image courtesy of* [*crazydavepromo.co.uk*](https://crazydavepromo.co.uk)*.* *[Licensing details](https://creativecommons.org/licenses/by-sa/4.0/).*


**Password** **Reset:** **[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):** Fortify 2022 with a password security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the *new* password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken. **[Register & Stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)** – sponsored by Specops Software.





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]] [[threatactor.name=Carbanak]] [[threatactor.name=FIN7]] [[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Carbanak]] [[action.malware.name=Carbon]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=REvil]] [[action.malware.name=RTM]] [[action.malware.name=Ryuk]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Accomodation]] [[victim.industry.name=Education]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Usb]] [[Fin7]] [[Badusb]] [[Ransomware]] [[Malware]] [[Sigler]] [[Threatpost]] [[ThreatPost]]

