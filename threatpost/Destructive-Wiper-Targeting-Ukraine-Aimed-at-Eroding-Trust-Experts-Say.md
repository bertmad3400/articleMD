# Destructive Wiper Targeting Ukraine Aimed at Eroding Trust, Experts Say
### Disruptive malware attacks on Ukrainian organizations (posing as ransomware attacks) are very likely part of Russia’s wider effort to undermine Ukraine’s sovereignty, according to analysts.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177768
+ Date: 2022-01-19T20:55:28+00:00
+ Author: Becky Bracken


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2018/05/10063440/Wiper_Fire_Destruction.jpg)

[Russia is positioned for a hot-war attack on Ukraine](https://www.nbcnews.com/news/world/blinken-ukraine-russia-attack-short-notice-invasion-fears-mount-rcna12691) that the Biden administration warned could come “at any point” — but the country is already suffering an attack of a different kind. A sweeping malware campaign remains ongoing, which experts agree is intended to permanently disrupt organizations across the country and paint Ukraine as a failed state.


The cyberattacks represent a coordinated destructive malware operation which has already impacted dozens of systems across the country, according to an alert from the Microsoft Threat Intelligence Center (MCTIC) this week.


The [cyberattacks on organizations across Ukraine](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/) started on Jan. 13, according to MCTIC, and based on the team’s assessment, the malware is a Master Boot Record (MBR) [wiper](https://threatpost.com/secrets-of-the-wiper-inside-the-worlds-most-destructive-malware/131836/). The destructor, which Microsoft has named WhisperGate, has already been used against government systems, non-profit organizations and IT companies in Ukraine, the report warned.


[![Password Management Webinar](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/12124026/specops_300x250_watch.jpg)](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)


The perpetrators are taking pains to make the attacks look like a ransomware attack, even providing a ransom note. However, the reality is that “the ransomware note is a ruse and…the malware destructs MBR and the contents of the files it targets,” according to MCTIC. It added, “MSTIC assesses that the malware…is intended to be destructive and designed to render targeted devices inoperable rather than to obtain a ransom.”


The team expects to find additional victims of the attack as part of its continuing investigation.


“We do not know the current stage of this attacker’s operational cycle or how many other victim organizations may exist in Ukraine or other geographic locations,” the MSTIC alert added. “However, it is unlikely these impacted systems represent the full scope of impact as other organizations are reporting.”


**Attacks Similar to NotPetya, WannaCry**
-----------------------------------------


Overwriting the MBR — typically a “nuclear” option ([as seen in](https://threatpost.com/shamoon-new-wiper-attack/139881/) the 2012 Saudi Aramco Shamoon attack) — is atypical for cybercriminal ransomware. As such, experts surmised that government-backed actors are most likely behind the hacks, which are similar to previous [NotPetya attacks](https://threatpost.com/doj-charges-6-sandworm-apt-members-in-notpetya-cyberattacks/160304/) on Ukraine.


Raj Samani, Trellix fellow and chief scientist, said there are also additional similarities between this latest round of attacks and the [WannaCry campaign](https://threatpost.com/the-wannacry-security-legacy-and-whats-to-come/144607/), which he described having a similar “pseudo-ransomware nature.”


“We have identified threat indicators targeting a range of industries, including government, financial services, transportation and utilities,” Samani explained. “We have to acknowledge that such actions, in conjunction with the inability to pay, infers a destructive campaign, or indeed one intended to spread fear and hysteria.”


Saumitra Das, CTO and founder of Blue Hexagon, agreed that this type of destructive malware doesn’t offer a cash payoff for the everyday cybercrook, which supports the state-backed actor theory.


“The tactics used in this attack seem to focus on disruption rather than moneymaking,” Das explained to Threatpost. “Wiping the MBR, causing systems to go down, is not beneficial to criminal gangs out to make a quick buck — but it’s very effective for nation states as a provocation or tool used for larger aims. Usually, malware that extorts based on disruption does not usually make the system inoperable but merely throttles it.”


Silas Cutler, threat analyst at Stairwell, told Threatpost that the phony ransomware amount demanded in the attacks is ridiculously low by industry standards, further indicating that the attacks were never about the cash.


“The ransom demand shared in its original format by Microsoft is different from current ransomware trends in that the sum is a tenth of what sophisticated groups would demand; and, they offer limited ways to communicate with the attackers,” Cutler said. “It’s unclear at this time why the ransom demand is so low. It’s possible the actor chose an arbitrarily low amount in hopes that some organizations may attempt to pay in a panic to recover before reporting and guidance about the malware was made public.”


**Russia’s Hybrid War Against Ukraine?**
----------------------------------------


As for which nation-state may be behind the effort, Microsoft doesn’t attribute WhisperGate to any specific country. Others are not as circumspect.


“While not currently attributed to any known actor group or country of origin, Russia is generally considered the primary suspect,” Cutler said. “The reported use of destructive malware, using ransomware as a cover, is a tactic that’s been previously observed in Russian attacks against Ukrainian organizations such as in the [Ukraine blackout](https://threatpost.com/notpetya-linked-to-industroyer-attack-on-ukraine-energy-grid/138287/) and NotPetya attacks in 2015 to 2017.”


Scheherazade Rehman, Professor of International Affairs at George Washington University, explained to Threatpost that this show of cyberwarfare fits into the larger “hybrid war” being waged by the Russian government against Ukraine.


“Russia wants the rest of the world to see that they are planning significant military activity in Ukraine and their tactics involve an attack on all fronts: 100,000 troops and military equipment build-up on the border, planting insurgents to stage a ‘false-flag’ operation, and cyber-attacks on Kyiv’s government computer systems,” Dr. Rehman told Threatpost.


She added this step toward “dismantling the Ukrainian infrastructure” is part of the Russian narrative that Ukraine is an illegitimate, failed state.


“Although not definitive, the cyberattacks are almost certainly from Russia,” Rehman said. “It was a two-prong attack and the largest in four years.”


The first prong, she said, was last week’s breach of more than 70 [Ukrainian government sites](https://threatpost.com/be-afraid-massive-cyberattack-downs-ukrainian-govt-sites/177659/) that posted a defacement message in Ukrainian, Russian and Polish:


*“Ukrainians! … All information about you has become public. Be afraid and expect worse. It’s your past, present and future.”*


The note included other messaging suggesting Ukraine is an illegitimate nation, she said.


This round of fake ransomware attacks appears to the second prong of the attack, Rehman added.


“These cyberattacks are a larger part of the Russian escalation and intent,” she said. “Inoperable government agencies would further assist in the Russian objective of showing Ukraine as not being a legitimate sovereign state and undermining Ukraine’s ability to fight back on all fronts. These cyberattacks are not only intended to intimidate Ukrainians but destabilize and undermine their confidence in their public sector, and erode trust in their own government.”


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=njRAT]] [[action.malware.name=NotPetya]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Shamoon]] [[action.malware.name=Tor]] [[action.malware.name=WannaCry]] [[action.malware.name=Wiper]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Mining]] [[victim.industry.name=Public]]

#### Location:
[[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.country.name=Ukraine]] [[victim.continent.name=Europe]] [[victim.city.name=Kyiv]] [[victim.country.name=Ukraine]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Malware]] [[Ransomware]] [[Cyberattacks]] [[Microsoft]] [[Threatpost]] [[Rehman]] [[Mbr]] [[“we]] [[Notpetya]] [[“the]] [[ThreatPost]]

