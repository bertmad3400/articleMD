# ‘Tropic Trooper’ Reemerges to Target Transportation Outfits
### Analysts warn that the attack group, now known as 'Earth Centaur,' is honing its attacks to go after transportation and government agencies.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177106
+ Date: 2021-12-16T19:16:06+00:00
+ Author: Becky Bracken


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/16141318/centaur-e1639682011813.jpeg)

They’ve been an active threat group since 2011, but a recent uptick in activity from Earth Centaur – previously known as Tropic Trooper – aimed specifically at transportation and government agencies is setting off alarm bells among experts.


Trend Micro researchers have been tracking [Tropic Trooper’s resurgence](https://www.trendmicro.com/en_us/research/21/l/collecting-in-the-dark-tropic-trooper-targets-transportation-and-government-organizations.html), which began in July 2020 and has recently included troubling attempts to breach sensitive transportation-related data like flight schedules and financial planning documents.


The analysts were able to attribute the new Earth Centaur activity to Tropic Trooper after finding similar code in configuration decoding, they reported.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“Currently, we have not discovered substantial damage to these victims as caused by the threat group,” Trend Micro’s analysts explained. “However, we believe that it will continue collecting internal information from the compromised victims and that it is simply waiting for an opportunity to use this data.”


**Earth Centaur’s Tricks**
--------------------------


The group’s hallmark tactics, techniques and procedures (TTPs) include savvy [red teamwork](https://threatpost.com/ta551-tactics-sliver-red-teaming/175651/), the researchers noted. Earth Centaur is proficient at bypassing security and lingering undetected, the report added.


“Depending on the target, it uses backdoors with different protocols, and it can also use the reverse proxy to bypass the monitoring of network security systems. The usage of the open-source frameworks also allows the group to develop new backdoor variants efficiently. ”


Typically, the threat group breaches the target systems through a vulnerable Exchange or Internet Information Services (IIS) server, followed by dropping backdoors like ChiserClient and SmileSvr, the report said. Trend Micro detailed the intrusion stages in the chart shown below.


From there, a custom version of Gh0st RAT sets out to gather data from active sessions on the host, according to the researchers. After that’s done, the attackers move through the compromised organization’s intranet and exfiltrate valuable data.


Trend Micro said Earth Centaur used PowerShell to download Rclone, an [exfiltration tool](https://threatpost.com/darkwatchman-rat-evolution-fileless-malware/177091/) that copies data to multiple clouds.


“Based on previous experience, Rclone has frequently been used in ransomware attacks to exfiltrate stolen data,” the report added. “However, it seems that currently, it is not only used in ransomware attacks but also in [advanced persistent threat, or APT] attacks.”


[Credential](https://threatpost.com/twitch-leak-emails-passwords/175390/) dumping was another common tactic Trend Micro saw with the Tropic Troopers transportation campaign.


“We also observed that the group used multiple legitimate tools to dump credentials on compromised machines,” the report added. “It made good use of these tools to achieve its goal and keep its operation hidden and unobstructive.”


Tropic Trooper/Earth Centaur has also developed its own, bespoke tool for cleaning up its tracks that deletes event logs on the targeted computer.


Tropic Trooper “uses backdoors with different protocols, which are deployed depending on the victim,” Trend Micro’s researchers found. “It also has the capability to develop customized tools to evade security monitoring in different environments, and it exploits vulnerable websites and uses them as C&C servers. ”


The rise of the threat actor’s interest in the transportation and government sector coincides with the November passage of the [Infrastructure Deal](https://www.whitehouse.gov/briefing-room/statements-releases/2021/11/06/fact-sheet-the-bipartisan-infrastructure-deal/), which promises gargantuan investments across the transportation sector, including $39 billion to modernize transit, $89.9 billion for public transit, $25 billion for airports, $66 billion in rail funding and much more.


Billions in cash are about to flood the transportation sector by way of the government, and Earth Centaur appears perfectly poised to cash in.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]] [[threatactor.name=Tropic Trooper]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=gh0st RAT]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Backdoors]] [[ThreatPost]]

