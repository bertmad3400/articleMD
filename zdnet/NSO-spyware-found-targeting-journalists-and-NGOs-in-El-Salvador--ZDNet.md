# NSO spyware found targeting journalists and NGOs in El Salvador | ZDNet
### Citizen Lab and Access Now find hacking was taking place while journalists were reporting on issues surrounding President Bukele.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/nso-spyware-found-targeting-journalists-and-ngos-in-el-salvador/
+ Date: 2022-01-13 03:42:40
+ Author: Chris Duckett


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/deedf28be02f5d029f3fbfc2b12e7fef354e14c1/2020/12/21/4865e211-37a1-4556-83f9-86f3e885a96f/nso-group.jpg?width=770&height=578&fit=crop&auto=webp)

![nso-group.jpg](https://www.zdnet.com/a/img/resize/6a5e784ff186274193b5f644e2635dc5f05b1400/2020/12/21/4865e211-37a1-4556-83f9-86f3e885a96f/nso-group.jpg?fit=bounds&auto=webp)
 NSO
 The University of Toronto's Citizen Lab along with Access Now have found the Pegasus spyware developed by the [now-sanctioned NSO Group](https://www.zdnet.com/article/commerce-dept-sanctions-nso-group-positive-technologies-and-more-for-selling-spyware-and-hacking-tools/) was used to target journalists and non-government organisations operating in El Salvador. 

In total, the investigation found 35 individuals were targeted across 37 devices, with Citizen Lab having a high degree of confidence that data was exfiltrated from devices belonging to 16 targets. 

"In several cases, Pegasus apparently exfiltrated multiple gigabytes of data successfully from target phones using their mobile data connections," Citizen Lab said in a [blog post](https://citizenlab.ca/2022/01/project-torogoz-extensive-hacking-media-civil-society-el-salvador-pegasus-spyware/). 

"We observed extensive targeting using zero-click exploits, however we also identified specific instances in which targets were sent one-click infection links via SMS message." 

One of the zero-click exploits was the [same iMessage Kismet exploit sold by NSO Group](https://www.zdnet.com/article/zero-click-ios-zero-day-found-deployed-against-al-jazeera-employees/) to target Al Jazeera employees, which was patched in iOS 14, and the other was ForcedEntry, which led to Apple notifying users they could have been the target of state-sponsored hacking. Many of the Salvadorian targets received such notifications, Citizen Lab said. 

"The Kismet exploit has not yet been publicly captured and analyzed, but appeared to involve the use of JPEG attachments, as well as iMessage's IMTranscoderAgent process invoking a WebKit instance," Citizen Lab said.

"Additionally, we recovered a copy of the ForcedEntry exploit from one of the phones. The exploit appears to have been fired at a phone with iOS 14.8.1, which is not vulnerable to ForcedEntry. The exploit does not appear to have run on the phone. 






"It is unclear why the exploit was fired at a non-vulnerable iOS version, though it is possible that NSO operators cannot always determine the precise iOS version used by the target before firing an exploit." 

**See also: [NSO spyware used to hack Polish politicians, Khashoggi's wife, others](/article/nso-spyware-used-to-hack-polish-politicians-wife-of-khashoggi-un-war-crimes-investigator-and-more/)** 

Apple is currently [suing NSO Group](https://www.zdnet.com/article/apple-sues-nso-group-over-pegasus-spyware/) over its use of Pegasus and seeking a permanent injunction that bans NSO Group from using any Apple software, services, or devices. 

Citizen Lab stopped short of pointing the finger at the El Salvador government and President Nayib Bukele, but said there was a "range of circumstantial evidence pointing to a strong El Salvador government nexus". 

Backing up this claim, Citizen Lab said the targets were working on sensitive domestic issues surrounding the government, such as *El Faro* [reporting](https://elfaro.net/en/202009/el_salvador/24785/Bukele-Has-Been-Negotiating-with-MS-13-for-a-Reduction-in-Homicides-and-Electoral-Support.htm) Bukele's administration was negotiating with leaders of gang MS-13 to reduce homicides in the country, prison privileges. and "long-term pledges tied to the results of congressional elections in 2021". 

Citizen Lab also said the operator had a "near-total focus of infections" within the country. 

"Through our ongoing Internet scanning and DNS cache probing, we identified a Pegasus operator focusing almost exclusively within El Salvador," Citizen Lab said. 

"We first observed this operator in early 2020, though the domain names associated with the operator appear to have been registered as early as November 2019." 

Citizen Lab said if Pegasus was sold into El Salvador, it was done despite warning signs that abuse would have take place including: An autocratic-leaning President with a fascination with digital technology; a long history of harassment of independent media and journalists; a climate of insecurity and human rights abuses; poorly regulated police, intelligence, and private security firms; and a lengthy history of corruption, organized crime, state violence, and authoritarianism. 

For its part, *El Faro* [reported](https://elfaro.net/en/202201/el_salvador/25936/22-Members-of-El-Faro-Bugged-with-Spyware-Pegasus.htm) two-thirds of its staff were hit, which included journalists, administration staff, and board members. 

"When the hacks occurred, the journalists were working on investigations, for example, into the Bukele administration's negotiation with gangs, the theft of pandemic-related food relief by the director of prisons and his mother, the Bukele brothers' secret negotiations related to the implementation of bitcoin, the financial holdings of officials in the current government, the government pandemic response, or a profile of President Nayib Bukele," the outlet said. 

During 2021, El Salvador [adopted bitcoin as legal tender](https://www.zdnet.com/article/el-salvador-makes-bitcoin-legal-tender-as-president-looks-to-volcanos-to-mine-crypto/), and Bukele said in November he wanted to create a [Volcano-powered Bitcoin City](https://www.zdnet.com/article/volcano-powered-bitcoin-city-could-be-bond-villainy-or-the-state-of-play-in-2021/). 

### Related Coverage

* [Apple sues NSO Group over Pegasus spyware](/article/apple-sues-nso-group-over-pegasus-spyware/)
* [Israeli govt pledges greater oversight of cyber-exports after NSO tools hacked US officials](/article/israeli-govt-pledges-greater-oversight-of-cyber-exports-after-nso-tools-used-to-spy-on-us-officials/)
* [CEO-designate of Pegasus spyware's NSO Group resigns after US sanctions](/article/new-ceo-designate-of-pegasus-spyware-maker-nso-group-resigns-after-us-sanctions/)
* [Apple releases update fixing NSO spyware vulnerability affecting Macs, iPhones, iPads and Watches](/article/apple-releases-update-fixing-nso-spyware-vulnerability-affecting-macs-iphones-ipads-and-watches/)
* [Commerce Dept sanctions NSO Group, Positive Technologies and more for selling spyware and hacking tools](/article/commerce-dept-sanctions-nso-group-positive-technologies-and-more-for-selling-spyware-and-hacking-tools/)
* [Citizen Lab researcher disputes claims from NSO Group after UK court finds UAE ruler used Pegasus to hack ex-wife, lawyers](/article/citizen-lab-researcher-disputes-claims-from-nso-group-after-uk-court-finds-uae-ruler-used-pegasus-to-hack-ex-wife-lawyers/)





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Ruler]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Education]]

#### Location:
[[victim.country.name=Israel]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=El Salvador]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Nso]] [[Bukele]] [[Spyware]] [[Forcedentry]] [[ZDNet]]

