# QNAP force-installs update after DeadBolt ransomware hits 3,600 devices
### QNAP force-updated customer's Network Attached Storage (NAS) devices with firmware containing the latest security updates to protect against the DeadBolt ransomware, which has already encrypted over 3,600 devices.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/qnap-force-installs-update-after-deadbolt-ransomware-hits-3-600-devices/
+ Date: 2022-01-28T01:30:00-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/25/Deadbolt__ransomware.jpg)

![DeadBolt ransomware](https://www.bleepstatic.com/content/hl-images/2022/01/25/Deadbolt__ransomware.jpg)


QNAP force-updated customer's Network Attached Storage (NAS) devices with firmware containing the latest security updates to protect against the DeadBolt ransomware, which has already encrypted over 3,600 devices.


On Tuesday, BleepingComputer reported on a [new ransomware operation named DeadBolt](https://www.bleepingcomputer.com/news/security/new-deadbolt-ransomware-targets-qnap-devices-asks-50-btc-for-master-key/) that was encrypting Internet-exposed QNAP NAS devices worldwide.


The threat actor claims to be using a zero-day vulnerability to hack QNAP devices and encrypt files using the DeadBolt ransomware, which appends the **.deadbolt**extension to file names.


The ransomware will also replace the regular HTML login page with a ransom note demanding 0.03 bitcoins, worth approximately $1,100, to receive a decryption key and recover data.



![DeadBolt ransom screen on a QNAP NAS device](https://www.bleepstatic.com/images/news/ransomware/d/deadbolt/ransom-note-screen.jpg)**DeadBolt ransom screen on a QNAP NAS device**
The DeadBolt ransomware gang is also trying to sell the full details of the alleged zero-day vulnerability to QNAP for 5 Bitcoins, worth $185,000.


They are also willing to sell QNAP the master decryption key that can decrypt all affected victims and provide information on the alleged zero-day for 50 bitcoins, or approximately $1.85 million.


While it is unlikely that QNAP will give into the extortion demand, numerous users in our [DeadBolt support forum topic](https://www.bleepingcomputer.com/forums/t/767603/deadbolt-ransomware-support-topic-qnap-devices-deadbolt-extension/) have reported successfully paying the ransomware to recover their files.


QNAP force-updates firmware on NAS devices
------------------------------------------


The next day, [QNAP began warning customers](https://www.bleepingcomputer.com/news/security/qnap-warns-of-new-deadbolt-ransomware-encrypting-nas-devices/) to secure their Internet-exposed NAS devices against DeadBolt by updating to the latest QTS software version, disabling UPnP, and disabling port forwarding.


Later that night, QNAP took more drastic action and force-updated the firmware for all customers' NAS devices to [version 5.0.0.1891](https://www.qnap.com/en-us/release-notes/qts/5.0.0.1891/20211221), the latest universal firmware released on December 23rd, 2021.


This update also included numerous security fixes, but almost all of them are related to Samba, which is unlikely associated with this attack.


QNAP owners and IT admins told BleepingComputer that QNAP forced this firmware update on devices even if automatic updates were disabled.


However, this update did not go off without a hitch, as some owners found that their iSCSI connections to the devices no longer worked after the update. 


"Just thought I would give everyone a heads-up. A couple of our QNAPS lost ISCSI connection last night. After a day of tinkering and pulling our hair out we finally found it was because of the update. It has not done it for all of the QNAPs we manage but we finally found the resolution," a QNAP owner [said on Reddit](https://www.reddit.com/r/qnap/comments/se0ko3/qnap_iscsi_failed_after_update_fix/).


"In "Storage & Snapshots > ISCSI & Fiber Channel" right-click on your Alias (IQN) select "Modify > Network Portal" and select the adapter you utilize for ISCSI."


Other users who had purchased the decryption key, and were in the process of decrypting, found that the firmware update also removed the ransomware executable and ransom screen used to initiate decryption. This prevented them from continuing the decryption process once the device finished updating.


"It usually asks me if I want to update, but now it didn't ask me. I was just standing idle while the decryption was in progress and then I heard a beep from the NAS, and when I looked in the menu, it was asking me if I want to restart now for the update to finalize," an upset owner posted in BleepingComputer's [DeadBolt support topic](https://www.bleepingcomputer.com/forums/t/767603/deadbolt-ransomware-support-topic-qnap-devices-deadbolt-extension/?p=5313748).


"I pressed NO but it ignored me and started to close down all the apps in order to restart."


In response to numerous complaints about QNAP forcing a firmware update, a QNAP support representative replied, stating it was to protect users from the ongoing DeadBolt ransomware attacks.



> 
> "We are trying to increase protection against deadbolt. If recommended update is enabled under auto-update, then as soon as we have a security patch, it can be applied right away.
> 
> 
> Back in the time of Qlocker, many people got infected after we had patched the vulnerability. In fact, that whole outbreak was after the patch was released. But many people don't apply a security patch on the same day or even the same week it is released. And that makes it much harder to stop a ransomware campaign. We will work on patches/security enhancements against deadbolt and we hope they get applied right away.
> 
> 
> I know there are arguments both ways as to whether or not we should do this. It is a hard decision to make. But it is because of deadbolt and our desire to stop this attack as soon as possible that we did this." - [QNAP support rep](https://www.reddit.com/r/qnap/comments/sdsf02/comment/huhfmjc/?utm_source=share&utm_medium=web2x&context=3).
> 
> 
> 


What is unclear is why a forced update to the latest firmware would protect a device from the DeadBolt ransomware when QNAP initially said that reducing devices' exposure on the Internet would mitigate the attacks.


One possibility is that an older vulnerability in QTS is being abused to breach QNAP devices and install DeadBolt and that upgrading to this firmware patches the vulnerabilities.


Forced updates come too late
----------------------------


Unfortunately, QNAP's move may have come too late as CronUP security researcher and Curated Intel member [Germán Fernández](http://twitter.com/1ZRR4H?ref_src=twsrc%5Etfw)discovered that DeadBolt had already encrypted thousands of QNAP devices.



> 
> Curated Intel member, [@1ZRR4H](https://twitter.com/1ZRR4H?ref_src=twsrc%5Etfw), observed QNAP ransomware events being reported via IoT search engines, including Shodan and Censys.  
>   
> 
> Shodan (1160 events): <https://t.co/qpaCTuICAf>  
>   
> 
> Censys (3687 events): <https://t.co/uZKLQprSDE>  
>   
> 
> Tip: use country tags to search by country. [pic.twitter.com/2IXpCNpBvV](https://t.co/2IXpCNpBvV)
> 
> 
> — Curated Intelligence (@CuratedIntel) [January 27, 2022](https://twitter.com/CuratedIntel/status/1486832416039788544?ref_src=twsrc%5Etfw)


Internet device search engine [Shodan reports](https://beta.shodan.io/search?query=html%3A%22All+your+files+have+been+locked+by+DeadBolt%22) that 1,160 QNAP NAS devices are encrypted by DeadBolt. Censys, though, paints a far grimmer picture, [finding 3,687 devices](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=100&virtual_hosts=EXCLUDE&q=services.http.response.body%3A+%22All+your+files+have+been+locked+by+DeadBolt%22) already encrypted at the time of this writing.


Both Shodan and Censys show that the top countries affected by this attack are the United States, France, Taiwan, the United Kingdom, and Italy.


To make matters worse, QNAP NAS owners are already targeted by other ransomware operations named [Qlocker](https://www.bleepingcomputer.com/news/security/qlocker-ransomware-returns-to-target-qnap-nas-devices-worldwide/) and [eCh0raix](https://www.bleepingcomputer.com/news/security/ongoing-ech0raix-ransomware-campaign-targets-qnap-nas-devices/), who constantly scan for new devices to encrypt.


BleepingComputer has asked QNAP further questions about the forced update and DeadBolt attacks.





## Tags:

#### Action:
[[action.malware.name=4H RAT]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=France]] [[victim.continent.name=Europe]] [[victim.country.name=United Kingdom]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Qnap]] [[Deadbolt]] [[Ransomware]] [[Nas]] [[Bleepingcomputer]] [[Deadbolt]] [[Shodan]] [[Censys]] [[Zero-day]] [[Iscsi]] [[Bleeping Computer]]
#### urls
https://t.co/qpaCTuICAf https://t.co/uZKLQprSDE

