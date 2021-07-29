# Hackers used never-before-seen wiper in recent attack on Iranian train system: report
### SentinelOne analysts were able to recreate the July 9 attack and identify the threat actor behind it.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/hackers-used-never-before-seen-wiper-in-recent-attack-on-iranian-train-system-report/)
+ Date: July 29, 2021 -- 11:00 GMT (12:00 BST)
+ Author: Jonathan Greig


## Article:
Unknown

Researchers with cybersecurity company SentinelOne reconstructed the recent cyberattack on Iran's train system [in a new report](https://labs.sentinelone.com/meteorexpress-mysterious-wiper-paralyzes-iranian-trains-with-epic-troll), uncovering a new threat actor -- which they named 'MeteorExpresss' -- and a never-before-seen wiper.

On July 9, [local](http://www.jahannews.com/news/769316/%D8%A7%D8%AD%D8%AA%D9%85%D8%A7%D9%84-%D8%AD%D9%85%D9%84%D9%87-%D8%B3%D8%A7%DB%8C%D8%A8%D8%B1%DB%8C-%D8%B4%D8%B1%DA%A9%D8%AA-%D8%B1%D8%A7%D9%87-%D8%A2%D9%87%D9%86-%DA%A9%D8%B4%D9%88%D8%B1%DB%8C) [news outlets](https://baamardom.ir/185583/%D8%AD%D9%85%D9%84%D9%87-%D8%B3%D8%A7%DB%8C%D8%A8%D8%B1%DB%8C-%D8%A8%D9%87-%D8%B3%DB%8C%D8%B3%D8%AA%D9%85-%D9%87%D8%A7%DB%8C-%D8%B4%D8%B1%DA%A9%D8%AA-%D8%B1%D8%A7%D9%87-%D8%A2%D9%87%D9%86/) began [reporting on a cyberattack](https://twitter.com/IranIntl_En/status/1413574416953401344/photo/1) targeting the Iranian train system, with [hackers defacing display screens](https://twitter.com/IranIntl_En/status/1413574416953401344) in train stations by asking passengers to call '64411', the phone number of Iranian Supreme Leader Khamenei's office. 

Train services were disrupted and just one day later, hackers took down the website of Iran's transport ministry. [According to Reuters](https://www.reuters.com/world/middle-east/iran-transport-ministry-hit-by-second-apparent-cyberattack-days-2021-07-10/), the ministry's portal and sub-portal sites went down after the attack targeted computers at the Ministry of Roads and Urban Development.

![e54gcklxiamirfq.jpg]()![e54gcklxiamirfq.jpg](https://www.zdnet.com/a/hub/i/r/2021/07/29/4da5c962-a045-48c2-b219-0f861fb43f32/resize/470xauto/29d65d76413aa553467683ed4b1f2230/e54gcklxiamirfq.jpg)Hackers took over screens in Iranian train stations on July 9 and put up the phone number 64411-- the number to Iran's Supreme Leader's Office. 


 Fars News
 In his examination, SentinelOne principal threat analyst Juan Andres Guerrero-Saade explained that the people behind the attack called the never-before-seen wiper 'Meteor' and developed it in the last three years. 

"At this time, we have not been able to tie this activity to a previously identified threat group nor to additional attacks," Guerrero-Saade said, adding that they were able to reconstruct the attack thanks to security researcher Anton Cherepanov and an Iranian antivirus company.  

"Despite a lack of specific indicators of compromise, we were able to recover most of the attack components described in the post along with additional components they had missed. Behind this outlandish tale of stopped trains and glib trolls, we found the fingerprints of an unfamiliar attacker."

Guerrero-Saade said the early analysis of Padvish security researchers was key to SentinelOne's reconstruction alongside "a recovered attacker artifact that included a longer list of component names."






"The attackers abused Group Policy to distribute a cab file to conduct their attack. The overall toolkit consists of a combination of batch files orchestrating different components dropped from RAR archives," Guerrero-Saade explained. 

"The archives decompressed with an attacker supplied copy of Rar.exe coupled with the password 'hackemall'. The wiper components are split by functionality: Meteor encrypts the filesystem based on an encrypted configuration, nti.exe corrupts the MBR, and mssetup.exe locks the system."

SentinelOne found that the majority of the attack was "orchestrated via a set of batch files nested alongside their respective components and chained together in successive execution." 

The batch file copies the initial components via a CAB file in a network share within the Iranian railways network, according to the report. From there, the batch file uses its own copy of WinRAR to decompress additional components from three additional archives that use a Pokemon-themed password, "hackemall" which was also referenced elsewhere during the attack. 

"At this point the execution begins to bifurcate into other scripts. The first one is 'cache.bat', which focuses on clearing obstacles and preparing the ground for subsequent elements with the use of Powershell," Guerrero-Saade said. 

"'cache.bat' performs three main functions. First, it will disconnect the infected device from the network. Then it checks to see if Kaspersky antivirus is installed on the machine, in which case it'll exit. Finally, 'cache.bat' will create Windows Defender exclusions for all of its components, effectively clearing the way for a successful infection without impediments." 

The report explained that this specific script was instructive in rebuilding the attack chain because it includes a list of the attack components that gave researchers specific things to search for. 

Two batch files are deployed that make the machine unbootable and clean up the event logs. After a number of other actions, update.bat will then call 'msrun.bat,' which passes "the Meteor wiper executable as a parameter." 

Another batch file -- msrun.bat -- moves in a screen locker and the encrypted configuration for the Meteor wiper, Guerrero-Saade explained. A scheduled task is created by the script called 'mstask' that is then set to execute the Meteor wiper at five minutes to midnight.

"There's a strange level of fragmentation to the overall toolkit. Batch files spawn other batch files, different rar archives contain intermingled executables, and even the intended action is separated into three payloads: Meteor wipes the filesystem, mssetup.exe locks the user out, and nti.exe presumably corrupts the MBR," Guerrero-Saade wrote.  

"The main payload of this convoluted attack chain is an executable dropped under 'env.exe' or 'msapp.exe'. Internally, the coders refer to it as 'Meteor'. While this particular instance of Meteor suffers from a crippling OPSEC failure (the inclusion of verbose debug strings presumably intended for internal testing), it's an externally configurable wiper with an extensive set of features."

The Meteor wiper, according to the report, is supplied with a single argument, an encrypted JSON configuration file 'msconf.conf.'

Meteor wipes files as it moves from the encrypted config, deletes shadow copies and takes a machine out of a domain to complicate remediation. These only scratched the surface of what Meteor is capable of, according to the report. 

Although not used in the attack on the Iranian train station, the wiper is able to change passwords for all users, disable screensavers, process termination based on a list of target processes, install a screen locker, disable recovery mode, change boot policy error handling, create schedule tasks, log off local sessions, delete shadow copies, change lock screen images and execute demands. 

Guerrero-Saade noted that the developers of the wiper created multiple ways for the wiper to accomplish each of these tasks

"However, the operators clearly made a major mistake in compiling a binary with a wealth of debug strings meant for internal testing. The latter is an indication that despite whatever advanced practices the developers have in their arsenal, they lack a robust deployment pipeline that ensures such mistakes do not happen. Moreover, note that this sample was compiled six months before its deployment and the mistake was not caught," the report found. 

"Secondly, the code is a bizarre amalgam of custom code that wraps open-source components (cpp-httplib v0.2) and practically ancient abused software (FSProLabs' Lock My PC 4). While that might suggest that the Meteor wiper was built to be disposable, or meant for a single operation, that's juxtaposed with an externally configurable design that allows efficient reuse for different operations." 

When SentinelOne researchers did a deeper dive into Meteor, they found that the redundancies were evidence that the wiper was created by multiple developers who added different components. 

The report added that the "externally configurable nature of the wiper" shows that it wasn't created for this particular operation. They have yet to see any other attacks or variants of the Meteor wiper in the wild. 

Researchers were not able to attribute the attack to a specific threat actor but explained that the attacker is an "intermediate level player whose different operational components sharply oscillate from clunky and rudimentary to slick and well-developed." 

"On the one hand, we have a new externally-configurable wiper packed full of interesting capabilities, involving a mature development process, and redundant means to accomplish their goals. Even their batch scripts include extensive error checking, a feature seldom encountered with deployment scripts. Their attack is designed to cripple the victim's systems, leaving no recourse to simple remediation via domain administration or recovery of shadow copies," Guerrero-Saade wrote. 

"On the other hand, we see an adversary that doesn't yet have a handle on their deployment pipeline, using a sample of their malware that contains extensive debug features and burning functionality irrelevant to this particular operation." 

Guerrero-Saade goes on to say that SentinelOne "cannot yet make out the shape of this adversary across the fog" and theorizes that it is "an unscrupulous mercenary group" or state-backed actors with a variety of motives. 

Although they were unable to attribute the attack, they noted that the attackers appeared to be familiar with the general setup of Iran's railway system and the Veeam backup used by the target, implying the threat actors spent time in the system before launching an attack. 

At the time of the attack, Iranian officials did not confirm if there was a ransom demand or who they believed was behind the attack, [Reuters reported](https://www.reuters.com/world/middle-east/iran-transport-ministry-hit-by-second-apparent-cyberattack-days-2021-07-10/). 

[The Times of Israel noted](https://www.timesofisrael.com/hack-causes-chaos-on-iran-trains-posts-supreme-leaders-number-for-complaints/) that following the infamous [Stuxnet attack](https://www.zdnet.com/article/infographic-how-stuxnet-supervirus-works/) in 2010, Iran [disconnected significant parts](https://www.zdnet.com/pictures/the-worlds-most-famous-and-dangerous-apt-state-developed-malware/3/) of its infrastructure from the internet. 





#### Tags:
[[Guerrero-Saade]] [[SentinelOne]] [["The]] [[attack.]] [[attack,]] [[ZDNet]]
