# FBI: Cuba ransomware group hit 49 critical infrastructure organizations | ZDNet
### The FBI claimed the group has made at least $43.9 million in ransom payments.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/fbi-cuba-ransomware-hit-49-critical-infrastructure-organizations/
+ Date: 2021-12-03 22:42:04
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/db6e8e885ac2ba67171e631c838e8c946b163e98/2021/02/02/9a9177ed-a0cf-4c13-8082-23535179348a/cuba-ransomware-leak-site.png?width=770&height=578&fit=crop&auto=webp)

The FBI has [released a new notice](https://www.ic3.gov/Media/News/2021/211203-2.pdf) about the Cuba ransomware, explaining that the group has attacked "49 entities in five critical infrastructure sectors" and made at least $43.9 million in ransom payments.

In a notice sent out on Friday, the FBI said the group is targeting enterprises in the financial, government, healthcare, manufacturing, and information technology sectors while using the Hancitor malware to gain entry to Windows systems. 

"Cuba ransomware is distributed through Hancitor malware, a loader known for dropping or executing stealers, such as Remote Access Trojans (RATs) and other types of ransomware, onto victims' networks," the notice explained, noting that the encrypted files have the ".cuba" extension. 

"Hancitor malware actors use phishing emails, Microsoft Exchange vulnerabilities, compromised credentials, or legitimate Remote Desktop Protocol (RDP) tools to gain initial access to a victim's network. Subsequently, Cuba ransomware actors use legitimate Windows services -- such as PowerShell, PsExec, and other unspecified services -- and then leverage Windows Admin privileges to execute their ransomware and other processes remotely." 

The eye-popping ransom payments were dwarfed by the amount of money the group has demanded from victims, which the FBI pegged at $74 million. 

Once a victim is compromised, the ransomware installs and executes a CobaltStrike beacon while two executable files are downloaded. The two files allow attackers to acquire passwords and "write to the compromised system's temporary (TMP) file."

"Once the TMP file is uploaded, the 'krots.exe' file is deleted and the TMP file is executed in the compromised network. The TMP file includes Application Programming Interface (API) calls related to memory injection that, once executed, deletes itself from the system. Upon deletion of the TMP file, the compromised network begins communicating with a reported malware repository located at Montenegro-based Uniform Resource Locator (URL) teoresp.com," the FBI explained. 






"Further, Cuba ransomware actors use MimiKatz malware to steal credentials, and then use RDP to log into the compromised network host with a specific user account. Once an RDP connection is complete, the Cuba ransomware actors use the CobaltStrike server to communicate with the compromised user account. One of the initial PowerShell script functions allocates memory space to run a base64-encoded payload. Once this payload is loaded into memory, it can be used to reach the remote command-and-control (C2) server and then deploy the next stage of files for the ransomware. The remote C2 server is located at the malicious URL kurvalarva.com."

The FBI included other attack information as well as a sample ransom note and email the attackers typically include. 

Ransomware experts were somewhat surprised by the amount of money the group made considering their level of activity relative to other more prominent ransomware groups. 

Emsisoft threat analyst Brett Callow said the report illustrated how lucrative the ransomware industry is considering the Cuba ransomware group is not in their top ten list in terms of activity. 

[His data](https://twitter.com/BrettCallow/status/1466844637688041479) shows 105 Cuba ransomware submissions this year compared to 653 for the Conti ransomware group. 

"This really highlights how much money there is to be made from ransomware. Cuba is a relatively small player and if they made $49 million, other outfits will have made considerably more," Callow told ZDNet. "And this, of course, is why ransomware is such a difficult problem to deal with. The massive rewards mean people consider the risks worthwhile."

[Since January](https://www.zdnet.com/article/heres-a-list-of-all-the-ransomware-gangs-who-will-steal-and-leak-your-data-if-you-dont-pay/), the group has operated a leak site, becoming one of the many ransomware groups that threatens to release stolen data if victims do not pay. 

The McAfee Advanced Threat Research Team released a [detailed report](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf) on the group in April, noting many of the same things the FBI found in their analysis. McAfee researchers also found that while the group had been around for years, it only recently began extorting victims with its leak site. 

The group typically targets companies in the US, South America and Europe. McAfee said that the group has sold stolen data in some instances. 

"Cuba ransomware is an older ransomware that has been active for the past few years. The actors behind it recently switched to leaking the stolen data to increase its impact and revenue, much like we have seen recently with other major ransomware campaigns," the McAfee report explained.

"In our analysis, we observed that the attackers had access to the network before the infection and were able to collect specific information in order to orchestrate the attack and have the greatest impact. The attackers operate using a set of PowerShell scripts that enables them to move laterally. The ransom note mentions that the data was exfiltrated before being encrypted."

The group made waves in February when they attacked payment processor Automatic Funds Transfer Services, forcing multiple US states to send out breach notification letters. First reported by [Bleeping Computer](https://www.bleepingcomputer.com/news/security/us-cities-disclose-data-breaches-after-vendors-ransomware-attack/), the attack involved the theft of "financial documents, correspondence with bank employees, account movements, balance sheets and tax documents." The incident also caused significant damage to the company's services for weeks. 

Multiple states were concerned because they used the company for a variety of services that gave them access to people's names, addresses, phone numbers, license plate numbers, VIN numbers, credit card information, paper checks and other billing details, according to Bleeping Computer. The state of [California](https://www.dmv.ca.gov/portal/security-breach-at-address-verification-company-may-compromise-dmv-information/) and [multiple](https://content.govdelivery.com/accounts/WALYNNWOOD/bulletins/2c24c24) [cities](http://monroewa.gov/CivicAlerts.aspx?AID=3766) in [Washington](https://thescoop.seattle.gov/2021/02/18/thid-party-vendor-incident/) state were affected and sent out breach notification letters.

Allan Liska, a ransomware expert with Recorded Future, said the FBI report also showed the observability problem with the ransomware landscape. 

"There were 28 victims published to the Cuba extortion site, but the FBI knew about at least 49 victims. We only knew about 1/2 of their victims," Liska said.

"Despite the small number of victims, the FBI claiming they made at least $43.9 million shows that ransomware continues to be extremely profitable for these threat actors. Their targets tended to be medium sized organizations and were spread around the world. I think it shows there is a lot we don't know."





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Cuba]] [[action.malware.name=Hancitor]] [[action.malware.name=Mimikatz]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=PsExec]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Accomodation]] [[victim.industry.name=Finance]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Manufacturing]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.continent.name=Europe]] [[victim.country.name=Montenegro]] [[victim.continent.name=Europe]] [[victim.city.name=Washington, D.C.]] [[victim.country.name=Navassa Island]] [[victim.continent.name=North and Central America]] [[victim.country.name=Cuba]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Ransomware]] [[Malware]] [[Tmp]] [[Mcafee]] [[Windows]] [[Powershell]] [[ZDNet]]

