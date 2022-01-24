# Dark Souls 3 Servers Shut Down Due to Critical RCE Bug
### The bug can allow attackers to remotely execute code on gamers’ computers. The devs temporarily deactivated PvP servers across multiple affected versions.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177896
+ Date: 2022-01-24T20:26:32+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/24124837/AdobeStock_314561521-1-1-scaled-e1643046545478.jpeg)

There’s a dangerous remote-code execution (RCE) bug in the Dark Souls video game that could let attackers brick the PCs of online players.


The flaw could allow attackers to do pretty much anything: As Kaspersky researchers [explained](https://www.kaspersky.com/blog/dark-souls-dangerous-vulnerability/43436/) on Monday, the bug “allows an attacker to execute almost any program on the victim’s computer, so they’re able to steal confidential data or execute any program they wish” – that includes installing malware, letting them access sensitive information or enabling them to rip off resources for [cryptocurrency mining](https://threatpost.com/bogus-cryptomining-apps-google-play/168785/).


The main problem is with Dark Souls III, but the remote code-execution (RCE) vulnerability also affects earlier games in the Dark Soul series, leading the developers to temporarily turn off player-versus-player (PvP) servers across Dark Souls Remastered, Dark Souls II and Dark Souls III. PvP refers to players being able to interact and duel with each other.


This same bug is [reportedly](https://www.reddit.com/r/Eldenring/comments/s9wai2/it_is_now_possible_for_dark_souls_3_invaders_to/) an issue in the Elden Ring game.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

On Sunday, the developers said that the bug is only relevant for PC users and that Xbox and PlayStation consoles are unaffected.



> 
> PvP servers for Dark Souls 3, Dark Souls 2, and Dark Souls: Remastered have been temporarily deactivated to allow the team to investigate recent reports of an issue with online services.   
> Servers for Dark Souls: PtDE will join them shortly.
> 
> 
> We apologize for this inconvenience.
> 
> 
> — Dark Souls (@DarkSoulsGame) [January 23, 2022](https://twitter.com/DarkSoulsGame/status/1485210967009071108?ref_src=twsrc%5Etfw)
> 
> 



The danger was brought to light on Saturday, when game fan SkeleMann [urged players](https://twitter.com/SkeleMann/status/1484802130850549760?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1484802130850549760%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.dexerto.com%2Fgaming%2Fdark-souls-3-players-risk-having-their-pc-bricked-if-they-play-online-1746144%2F) to steer clear of playing Dark Souls 3 online. “On PC there is a new, very serious exploit plaguing Dark Souls 3 which can cause lasting damage to your computer,” SkeleMann explained. “This could brick your PC, let your login information be shared or execute programs in the background, like a trojan horse.”


There’s a demonstration of the exploit in the [Twitch stream](https://www.twitch.tv/videos/1271478221?t=80m20s) of a player named The\_Grim\_Sleeper. In that stream, an unknown party launched a PowerShell script on the streamer’s computer that used the Windows Narrator engine to read out critical notes about the gameplay.


Whoever’s behind the attack apparently had benign intentions: According to a [screenshotted post](https://cdn.discordapp.com/attachments/524597731121954816/934488192575500318/unknown.png) on the [SpeedSouls’ Discord](https://discord.com/channels/81303778900316160/524597731121954816) – a group focused on speedrunning, or playing video games as fast as possible – they were just trying to bring attention to the problem after having not heard back from the game’s developers about the vulnerability. Since they hadn’t heard back, they decided to hijack a popular streamer during a streaming session.



> 
> like a Trojan Horse. And more nasty stuff.
> 
> 
> It's highly suggested to NOT PLAY ONLINE DARK SOULS 3 in it's current state. Avoid any online activity from Ds3.
> 
> 
> In addition, if you haven't already everybody and their mother can recommend the Blue Sentinel mod<https://t.co/lposZRzbr1>
> 
> 
> — SkeleMann (@SkeleMann) [January 22, 2022](https://twitter.com/SkeleMann/status/1484802130850549760?ref_src=twsrc%5Etfw)
> 
> 



That doesn’t mean that the bug won’t be abused at some point, Kaspersky pointed out. “For example, the creator of the exploit has already [shared information about the vulnerability](https://www.reddit.com/r/darksouls3/comments/s9sd3w/new_remote_code_execution_vulnerability_discovered/) with the developers of the Blue Sentinel plugin, a mod for Dark Souls designed to counteract cheats,” they wrote. “And one can only guess who else could get this information.


“Also, once demonstrated, other hackers may try to replicate the exploit and use it to cause real harm to players,” researchers continued. “There are various possible scenarios here: attackers can use it to steal passwords from game accounts or crypto-wallets, install good old ransomware, hidden miners and much more.”


How Gaming Brings Risk to Corporate Networks
--------------------------------------------


Saryu Nayyar, CEO and founder of Gurucul, noted that this attack points to the risk of remote workers using home networks and personal devices to access corporate resources.


“As we connect our gaming systems to the same network as resources that attach to the corporate network, the infection can easily spread from home to a much bigger operation,” she noted.


That’s why it’s critical for security teams to understand how users are accessing network resources and to incorporate that information into an assessment of the risks and the severity associated with attack campaigns, she added. “This is where identity, and specifically access analytics, incorporated into next-generation [security information and event management or SIEM] can narrow down indicators of compromise and determine malicious behaviors hiding as authorized user activity.”


RCE vulnerabilities are nothing new, but they’re dangerous when no one knows they exist, noted Jorge Orchilles, CTO of SCYTHE.


“We see threat actors use RCEs all the time, especially when the vulnerabilities do not have a patch available,” he told Threatpost on Monday.


Companies affected by these types of vulnerabilities “need to take immediate action to protect their customers by releasing patches,” he stressed. “Meanwhile, gamers affected should monitor their systems for abnormal activity such as crypto-miners.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Miner-C]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Skelemann]] [[ThreatPost]]
#### urls
modhttps://t.co/lposZRzbr1

