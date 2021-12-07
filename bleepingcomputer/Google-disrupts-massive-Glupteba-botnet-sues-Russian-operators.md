# Google disrupts massive Glupteba botnet, sues Russian operators
### Google has taken action to disrupt the Glupteba botnet that now controls more than 1 million Windows PCs around the world, growing by thousands of new infected devices each day.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/google-disrupts-massive-glupteba-botnet-sues-russian-operators/
+ Date: 2021-12-07T11:57:23-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/07/Glupteba.jpg)

![Google disrupts massive Glupteba botnet, sues Russian operators](https://www.bleepstatic.com/content/hl-images/2021/12/07/Glupteba.jpg)


Google has taken action to disrupt the Glupteba botnet that now controls more than 1 million Windows PCs around the world, growing by thousands of new infected devices each day.


[Glupteba](https://www.bleepingcomputer.com/tag/glupteba/) is a blockchain-enabled and modular malware that targets Windows devices worldwide [since at least 2011](https://www.bleepingcomputer.com/news/security/glupteba-malware-uses-bitcoin-blockchain-to-update-c2-domains/), including the US, India, Brazil, and countries from Southeast Asia.


Threat actors behind this malware strain are mainly distributing payloads onto targets' devices camouflaged as "free, downloadable software, videos, or movies" through pay-per-install (PPI) networks and malvertising pushed using traffic purchased from traffic distribution systems (TDS) via Google’s advertising platform.


After infecting a host, it can mine for cryptocurrency and steal user credentials and cookies, as well as deploy proxies on Windows systems and IoT devices which later get sold as 'residential proxies' to other cybercriminals.


As part of Google's concerted effort to disrupt the botnet, the company took over Glupteba's key command and control (C2) infrastructure which uses a Bitcoin blockchain backup mechanism to add resilience if the main C2 servers stop responding.


"We believe this action will have a significant impact on Glupteba's operations," [said](https://blog.google/threat-analysis-group/disrupting-glupteba-operation/) Google Threat Analysis Group's Shane Huntley and Luca Nagy today.


"However, the operators of Glupteba are likely to attempt to regain control of the botnet using a backup command and control mechanism that uses data encoded on the Bitcoin blockchain."



> 
> Glupteba disruption over last year:  
> 
> 63M Google Docs 1,183 Google Accounts, 908 Cloud Projects, and 870 Google Ads accounts. 3.5M users were warned via Safe Browsing.  
>   
> 
> TAG also partnered with CloudFlare and others take down servers.
> 
> 
> — Shane Huntley (@ShaneHuntley) [December 7, 2021](https://twitter.com/ShaneHuntley/status/1468234069184028690?ref_src=twsrc%5Etfw)


Legal action towards botnet disruption
--------------------------------------


Google also filed a temporary restraining order and [a complaint](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/1_Complaint.pdf) in the Southern District of New York against two Russian defendants (Dmitry Starovikov and Alexander Filippov) and 15 other unknown individuals.


The complaint claims the 17 defendants were the ones operating and coordinating Glupteba attacks with the end goal of stealing user accounts and credit card info, selling ad placement and proxy access on infected devices, and mining for cryptocurrency in computer fraud and abuse, trademark infringement, and other schemes.


Among the online services offered by Glupteba botnet's operators, Google mentioned "selling access to virtual machines loaded with stolen credentials (dont[.]farm), proxy access (awmproxy), and selling credit card numbers (extracard) to be used for other malicious activities such as serving malicious ads and payment fraud on Google Ads."


"Unfortunately, Glupteba’s use of blockchain technology as a resiliency mechanism is notable here and is becoming a more common practice among cyber crime organizations," Google's Vice President for Security Royal Hansen and General Counsel Halimah DeLaine Prado [added](https://blog.google/technology/safety-security/new-action-combat-cyber-crime/).


"The decentralized nature of blockchain allows the botnet to recover more quickly from disruptions, making them that much harder to shutdown. We are working closely with industry and government as we combat this type of behavior, so that even if Glupteba returns, the internet will be better protected against it."


On Monday, Microsoft also [seized dozens of malicious sites used by the Nickel China-based hacking group](https://www.bleepingcomputer.com/news/microsoft/microsoft-seizes-sites-used-by-apt15-chinese-state-hackers/) (aka KE3CHANG, APT15, Vixen Panda, Royal APT, and Playful Dragon) to target servers belonging to government orgs, diplomatic entities, and non-governmental organizations (NGOs) in the US and 28 other countries worldwide.





## Tags:

#### Threatactor:
[[threatactor.name=APT1]] [[threatactor.name=Ke3chang]] [[threatactor.name=Ke3chang]] [[threatactor.name=Ke3chang]] [[threatactor.name=Ke3chang]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Agriculture]] [[victim.industry.name=Entertainment]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.continent.name=Asia]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Brazil]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Google]] [[Glupteba]] [[Botnet]] [[Blockchain]] [[Windows]] [[Bleeping Computer]]

