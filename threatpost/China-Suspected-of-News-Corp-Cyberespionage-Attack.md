# China Suspected of News Corp Cyberespionage Attack
### Attackers infiltrated the media giant’s network using BEC, while Microsoft moved to stop such attacks by blocking VBA macros in 5 Windows apps. Included: more ways to help stop BEC.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178277
+ Date: 2022-02-08T14:14:59+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/02/08091000/China-cyberespionage-scaled-e1644329424934.jpg)

The Chinese hackers responsible for an attack on media giant News Corp last month likely were seeking intelligence to serve China’s interests in a cyberespionage incident that shows the persistent vulnerability of corporate networks to email-based attacks, security professionals said.


[Reports](https://www.theguardian.com/media/2022/feb/04/new-corp-hack-murdoch-media-firm-believes-hackers-links-china) on Monday revealed that a Jan. 20 incident at Rupert Murdoch’s media giant involved an attack on journalists’ email accounts that gave the intruders access to sensitive data. The breach – limited to several individuals working for outlets including News UK, the Wall Street Journal and the New York Post – has raised concerns over the safety of confidential sources working with journalists affected by the incident.


In an email to staff, News Corp cited a “foreign government” as responsible for the “persistent nation-state attack” and confirmed that “some data” was stolen, according to published reports. The media giant enlisted the help of cybersecurity firm [Mandiant](https://www.mandiant.com/) to investigate the incident, which the firm said is likely the work of a China-sponsored actor.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“Mandiant assesses that those behind this activity have a China nexus, and we believe they are likely involved in espionage activities to collect intelligence to benefit China’s interests,” said David Wong, vice president of consulting at Mandiant, in an emailed statement to Threatpost.


**Targeting Journalists for Cyberespionage**
--------------------------------------------


Indeed, while China typically targets “military and intellectual property” in its state-sponsored attacks, journalists also are “fairly high on their radar for espionage” due to their work with sources – confidential and otherwise, as noted by one cybersecurity professional.


“Journalists can have access to sources and intelligence about adversaries and other opponents of the Chinese regime, both foreign and domestic, or can be researching stories that could generate negative publicity for the Chinese government,” Mike McLellan, director of intelligence for cyber threat intelligence firm [Secureworks Counter Threat Unit](https://www.secureworks.com/about/counter-threat-unit), wrote in an email to Threatpost on Monday.


Paul Farrington, chief product officer for security firm  [Glasswall](https://glasswallsolutions.com/), agreed that it’s “common for politically motivated cybercriminals to mine reporters’ materials for intelligence,” given their frequent conversations with confidential sources that have access to information about current and future geopolitical events.


Moreover, China has previously shown an interest in attacking journalists, making this latest attack “entirely consistent with past Chinese state-sponsored behavior,” concurred Dave Merkel, CEO of cybersecurity firm [Expel](http://www.expel.io/).


He cited [a previous attack](https://threatpost.com/inside-targeted-attack-new-york-times-013113/77477/) on the New York Times by China in 2013 as a precedent for the nation’s targeting of journalists. Moreover, the threat actors’ use of business email compromise (BEC) to pull off the attack “makes sense” and also is consistent with nation-state actors, Merkel observed.


“When it comes to cyberattacks, nation state actors will only be as advanced as they have to – why burn expensive zero days if you don’t need to?” he said.


**Preventing BEC Attacks**
--------------------------


In fact, Merkel said the No. 1 source of attacks against Expel customers is BEC. “There’s no reason to think Chinese state-sponsored groups wouldn’t use the same tactics against their targets if those tactics work – and news organizations are definitely targets,” he said.


Indeed, BEC is a major threat that typically involves human error. The way it works is that an employee at a company receives an email with a malicious link or document and takes an action that can install malware on their computers. This can result in consequences from local data theft to giving threat actors access to the corporate network to advanced attack vectors such as ransomware.


Microsoft unveiled a timely yet unrelated step this week that could help mitigate the impact of, or even prevent, future BEC attacks: Namely, the company will soon begin blocking, by default, VBA macros obtained from the internet in five Office apps, as the company [revealed in a blog post](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805) Monday.


“For macros in files obtained from the internet, users will no longer be able to enable content with a click of a button,” Microsoft Principal Program Manager Kellie Eickmeyer wrote. “A message bar will appear for users notifying them with a button to learn more.”


This default setting “is more secure and is expected to keep more users safe including home users and information workers in managed organizations,” she added. Indeed, sending documents loaded with macros that immediately install malware on people’s computers with one click is a popular tactic of email-based attacks.


The new default setting will apply to Microsoft Office on devices running Windows for Access, Excel, PowerPoint, Visio and Word. Microsoft will roll out the change first in a preview version of Office 2023, starting with its Current Channel update channel in early April 2022.


Later, the change will be available in the other update channels, such as Current Channel, Monthly Enterprise Channel, and Semi-Annual Enterprise Channel. In the future Microsoft also will change the Office default setting for VBA macros in Office LTSC, Office 2021, Office 2019, Office 2016 and Office 2013, Eickmeyer added.


This move may make it more difficult to slip malware past corporate employees using BEC tactics. However, as one security professional noted, companies still must remain vigilant and take an “all hands on deck” approach to both threat mitigation and response, given the evolving nature and increased occurrence of cyber-attacks that organizations face.


“As the threat environment continues to change, proper and continuous diligence is required to ensure all cyber defensive tools and techniques are employed to protect your most precious data assets,” observed Tom Garrubba, vice president at risk-management firm [Shared Assessments](https://u7061146.ct.sendgrid.net/ls/click?upn=4tNED-2FM8iDZJQyQ53jATUY-2Flf1YfJi8Jl6Pa8fYnwMooXA0t7nRcGwuHZmhL1VNFMgZ7_ZRLSPEhX0sWy6v6-2FW4BoBGwvynWnvEEKCCoI2tE2RSv7Ap1BbaYTRGgOsmBtH3N8QKMiyASu9uND9imXoTFn2Ec5EmRJ9V9NBrK7aLIAhF6196NdmcyMkxC1VH7FuP-2B9MgrfUoUGWizcYBWkO7YHK-2FSUvJvNf4hmd993Dye56pyq89HFwWZoHTuzoXanpznaaoSlcLfzlPiOUFNRXQsUtdLW6-2BFIvjy5oI3kpt8fOysQ-2BJJ7pNAMDmmGf2nc2TWwK5J4rfFBha96XAcFn5Tdh8idS0UjuT6a1Fel8Ug5x5WkloyV8fxoFRJXaTFLqD0L0IDktPIPckEiewFCmD6TiVprT0ERdmp5-2BqTF3UZ3I98-3D)**,** in an email to Threatpost. “Continuous intelligence, monitoring, and dialogue with critical partners and suppliers should be ongoing to ensure ‘all is ready’ in the event recovery is needed, and that additional support is available in the event something were to occur.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.city.name=Dili]] [[victim.country.name=East Timor]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Cybersecurity]] [[Threatpost]] [[State-sponsored]] [[Merkel]] [[Malware]] [[ThreatPost]]

