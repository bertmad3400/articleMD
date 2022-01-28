# QNAP users still struggling with Deadbolt ransomware after forced firmware updates | ZDNet
### Censys said about 4,000 devices are still infected with Deadbolt ransomware.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/decryptor-released-for-deadbolt-ransomware-affecting-qnap-nas-devices/
+ Date: 2022-01-28 21:56:35
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/db36dda02b827ca75e0bbc2dbaa81c4dcb37ab25/2020/04/30/a0f407e5-4a1f-46e3-886e-4811e3ab755e/ransomware.jpg?width=770&height=578&fit=crop&auto=webp)

QNAP Network Attached Storage (NAS) device users are still struggling to address a range of issues connected to the Deadbolt ransomware, which began [infecting devices earlier this week](https://www.zdnet.com/article/qnap-warns-nas-users-of-deadbolt-ransomware-urges-customers-to-update/?ftag=COS-05-10aaa0g&taid=61f44ecd669f060001f1ed64&utm_campaign=trueAnthem%3A+Trending+Content&utm_medium=trueAnthem&utm_source=twitter). 

On Tuesday, QNAP NAS users flocked to [Reddit](https://www.reddit.com/r/qnap/comments/scm0zv/deadbolt_ransomware_attack_against_qnaps/) and [QNAP forums](https://forum.qnap.com/viewtopic.php?f=45&t=164797&start=30) to report ransomware infections. Censys [reported](https://censys.io/blog/the-qnapping-of-qnap-devices/) that of the [130,000 QNAP NAS devices](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.tls.certificates.leaf_data.issuer_dn%3A+%22CN%3DQNAP+NAS%22), 4,988 services "exhibited the [telltale signs](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=100&virtual_hosts=INCLUDE&q=services.http.response.html_title%3A+%22ALL+YOUR+FILES+HAVE+BEEN+LOCKED+BY+DEADBOLT.%22) of this specific piece of ransomware."

On Friday afternoon, Censys updated its report, telling ZDNet that overnight, the number of exposed and ransomware infected devices went down by 1,061 to 3,927. 

![qmap-hosts.png](https://www.zdnet.com/a/img/resize/fc9203ea44b964461d18b592bc24242867a862ba/2022/01/28/d4bc9630-6495-4826-a261-13542d71df59/qmap-hosts.png?width=370&fit=bounds&auto=webp)![qmap-hosts.png](https://www.zdnet.com/a/img/resize/fc9203ea44b964461d18b592bc24242867a862ba/2022/01/28/d4bc9630-6495-4826-a261-13542d71df59/qmap-hosts.png?width=370&fit=bounds&auto=webp)
 Censys
 "Why this went down could be for any number of reasons, we're still investigating to see if we can pinpoint the reasoning behind this," a Censys spokesperson said, theorizing that the decrease could be attributed to a forced update from QNAP. 

On Wednesday, QNAP initially [urged](https://www.qnap.com/en/security-news/2022/take-immediate-actions-to-stop-your-nas-from-exposing-to-the-internet-and-update-qts-to-the-latest-available-version-fight-against-ransomware-together) users to [update to the latest version of QTS](https://www.qnap.com/en/security-advisory/qsa-21-57), the Linux based operating system developed by the Taiwanese company to run on their devices.

But MalwareBytes [said](https://blog.malwarebytes.com/ransomware/2022/01/qnap-update-stops-deadbolt-ransomware-annoys-some-users-starts-debate/) QNAP pushed out an automatic, forced update with firmware on Thursday containing the latest security updates.

"Later that day, QNAP took more drastic action and force-updated the firmware for all customers' NAS devices to version 5.0.0.1891, the latest universal firmware which has been available since December 23rd, 2021," MalwareBytes explained.






"As you might expect after a forced update, a number of unexpected side-effects arose, making users that were affected by these problems unhappy. Some users reported losing their devices' ISCSI connections (ISCSI is a networking standard for linking data storage facilities), and some adapters were apparently left disabled by the update. The firmware update removed the ransomware executable and the ransom screen used to initiate decryption, which apparently caused some victims who had paid the ransom to be unable to proceed with decrypting the files after the update."

QNAP [responded](https://www.reddit.com/r/qnap/comments/sdz7e5/you_want_to_know_why_your_qnap_updated_last_night/huhlp5t/) to the controversy over the forced update on Reddit. A company representative explained why they decided to force the update, noting that it had been urging users to update their systems since January 7.

"In QTS there was a message in control panel/auto-update that 'QTS/QuTS hero will enable recommended version update soon to protect nas from deadbolt.' But I think a lot of people did not see that message. We are trying to increase protection against deadbolt. If recommended update is enabled under auto-update, then as soon as we have a security patch, it can be applied right away," the company spokesperson said. 

"Back in the time of [Qlocker](https://www.bleepingcomputer.com/news/security/qlocker-ransomware-returns-to-target-qnap-nas-devices-worldwide/), many people got infected after we had patched the vulnerability. In fact, that whole outbreak was after the patch was released. But many people don't apply a security patch on the same day or even the same week it is released. And that makes it much harder to stop a ransomware campaign. We will work on patches/security enhancements against deadbolt and we hope they get applied right away. I know there are arguments both ways as to whether or not we should do this. It is a hard decision to make. But it is because of deadbolt and our desire to stop this attack as soon as possible that we did this."

The message drew several furious responses from people who said the forced update caused [a number of downstream issues](https://www.reddit.com/r/qnap/comments/sdz7e5/comment/huij1yj/?utm_source=share&utm_medium=web2x&context=3). Others said it was [concerning the company had a backdoor](https://www.reddit.com/r/qnap/comments/sdz7e5/comment/hui27t3/?utm_source=share&utm_medium=web2x&context=3) into their systems while some said the forced update [did little to actually address](https://www.reddit.com/r/qnap/comments/sdz7e5/comment/hui22mm/?utm_source=share&utm_medium=web2x&context=3) the issues of people who had already been infected with Deadbolt. 

Recorded Future ransomware expert Allan Liska said this kind of specialty ransomware is very hard to defend against and commended QNAP for releasing a detailed guide to securing the appliance earlier this month. 

"It is difficult to defend against because the device is controlled by the manufacturer. Unless you are a company with the resources to enable compensating controls, you are largely at the mercy of the vendor," Liska said. 

"For most IoT devices, this doesn't matter too much. If someone launches a ransomware attack against my lightbulbs, I can just reset and go on with my life. But when those IoT devices hold all of your data it is a very different matter."

Decryptor issues
----------------

Security company Emsisoft [released](https://www.emsisoft.com/ransomware-decryption-tools/deadbolt) its own version of a decryptor after several victims reported having issues with the decryptor they received after paying a ransom. Some users even said they never got a decryptor after paying the ransom while others said the decryptor malfunctioned. 

Unfortunately, Emsisoft's decryptor requires users to have already paid the ransom and received the decryption keys from the Deadbolt ransomware operators. 

Deadbolt's ransom note says victims need to pay 0.03 BTC (equivalent to USD 1,100) to unlock their hacked device and that it "is not a personal] attack." 

Liska said ransomware groups are notorious for providing poor decryption software and noted that it is not uncommon for incident response teams to take the key given by the ransomware group and ignore the decryption code.

"The reason for Emsisoft to release a decryptor is to make sure victims have something they know will work once they get the key," Liska explained.

Liska slammed the people behind the attack, questioning their insistence that the attack wasn't "personal."

"It is a personal attack. People often have their digital lives stored on these devices. Whether it is photos, work, the book they have been writing, or the program they have been developing this stuff is important to them and the attackers just took that away from them," Liska added. 

"The attacker can dress it up as 'poor vendor security' all they want, but it is just a sign they are shitty people that have no regard for their fellow human beings."





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Derusbi]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Rover]] [[action.malware.name=Tor]] [[action.malware.name=UPPERCUT]]

#### Location:
[[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Qnap]] [[Decryptor]] [[Liska]] [[Deadbolt]] [[Censys]] [[Deadbolt]] [[Nas]] [[Emsisoft]] [[ZDNet]]

