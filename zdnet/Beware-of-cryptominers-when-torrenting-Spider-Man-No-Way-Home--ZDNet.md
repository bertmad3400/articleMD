# Beware of cryptominers when torrenting 'Spider-Man: No Way Home' | ZDNet
### A cybersecurity company found a Monero miner attached to a torrent of the popular Marvel film.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/beware-of-cryptominers-when-downloading-spider-man-no-way-home-torrents/
+ Date: 2021-12-23 15:15:23
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/3c323966e832ebd47773236ac50608975f112bf9/2021/12/23/41a432ad-fb8b-474b-ae62-e6b5086f57ef/shutterstock-1171760575.jpg?width=770&height=578&fit=crop&auto=webp)

Cybersecurity firm ReasonLabs is warning eager fans of "Spider-Man: No Way Home" to beware of cryptominers if they decide to torrent the film instead of heading to theaters for it. 

In a new report, the ReasonLabs research team says it found Monero miners attached to Russian torrent files of the new film, which brought in more than [$750 million worldwide](https://www.boxofficemojo.com/title/tt10872600/credits/) since it debuted last week. 

The miner adds exclusions to Windows Defender, creates persistence, and spawns a watchdog process to maintain its activity, according to ReasonLabs. 

"The malware is not signed and written in .net, and as of this date, it is not present in Virus Total. The malware tries to stay away from examining eyes, by using 'legitimate' names for the files and processes that it creates. We recommend taking extra caution when downloading content of any kind from non-official sources -- whether it's a document in an email from an unknown sender, a cracked program from a fishy download portal, or a file from a torrent download," the team explained. 

"One easy precaution you can take is to always check that the file extension matches the file you are expecting e.g. in this case, a movie file should end with '.mp4', not '.exe'. Try to gather information about the file, and always think twice before double-clicking on it. To make sure you see the real file extension, open a folder, go to 'View' and check 'File name extensions.' This will make sure you see the full file type." 

The researchers added that although the malware does not compromise personal information, cryptominers cause other kinds of damage.

The added electricity will cost victims of the malware and the researchers noted that the miner runs for long periods, slowing down your device while requiring high CPU usage. 






When asked how they discovered the cryptominer, the ReasonLabs team told ZDNet that they have amassed a large malware database over the years that allows them to research their origins, flag them, and cross check with other databases such as [Virus Total](https://www.virustotal.com/). 

One of their users downloaded this "Spider-Man: No Way Home" file and it got flagged within their database as a new threat.

They do not know how many times the file has been downloaded but noted that it has been around for some time. 

"The Spiderman malware is actually a new 'edition' of a previously known malware that was disguised as various popular apps in the past such as 'windows updater,' 'discord app,' and now the Spiderman movie. This suggests that it's been downloaded a lot. No one else has identified this 'edition' of the malware," the team said. 

BreachQuest CTO Jake Williams said threat actors have used torrents as a distribution mechanism for malware long before cryptominers were a thing. 

"I remember seeing a wave of threat actors compromising victims with screen savers celebrating Whitney Houston's career in the wake of her passing. Given that cryptominers are the easiest way for threat actors to cash out, it's not surprising that threat actors will use these as their malware payload of choice," Williams explained. 

Digital Shadows' Sean Nikkel noted that there are likely lots of Gen Xers and Millennials who remember the days of downloading random files from strangers across Kazaa and Limewire in search of rare or free MP3 or video files and ending up with a Trojan or similar nastiness. 

The tactic, he said, carried into the torrent world. In addition to malware being attached to popular movies or shows, this same thing occurs with popular applications like those from Adobe, Microsoft, or specialized music programs like Ableton or Fruity Loops, which are themselves often pirated. 

"Sometimes the key generators themselves were malicious or the application's executable. There have been plenty of office workers looking to cut corners or use programs they're familiar with on their work computer. These users run the risk of downloading 'free' versions or versions hosted on bad sites and end up getting burned," Nikkel said. 

Bugcrowd CTO Casey Ellis explained that from the threat actor's perspective, using a delivery system where users are less likely to reach out for "technical support" if something seems off or even admit to peers or family that their computer might be acting strange, gives them an increased chance of their malware executing in the first and, once it does, a lower risk of it being discovered and removed. 

ReasonLabs said it is still researching the origins of the miner but noted that they are constantly seeing miners deployed as common programs, files of interest, popular apps, current events etc. 

"Miners got very popular in the past years because it's easy money and attackers are trying to gain as many victims as possible -- by any way possible, including fooling users to download files that are not what they seem," ReasonLabs told ZDNet. 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Miner-C]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Entertainment]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Malware]] [[Reasonlabs]] [[Cryptominers]] [[ZDNet]]

