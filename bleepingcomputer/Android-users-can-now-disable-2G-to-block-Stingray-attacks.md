# Android users can now disable 2G to block Stingray attacks
### Google has finally rolled out an option on Android allowing users to disable 2G connections, which come with a host of privacy and security problems exploited by cell-site simulators.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/android-users-can-now-disable-2g-to-block-stingray-attacks/
+ Date: 2022-01-13T16:56:28-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/08/23/Cell-towers.jpg)

![cell tower](https://www.bleepstatic.com/content/hl-images/2021/08/23/Cell-towers.jpg?rand=715443774)


Google has finally rolled out an option on Android allowing users to disable 2G connections, which come with a host of privacy and security problems exploited by cell-site simulators.


The addition of the option was spotted by EFF (Electronic Frontier Foundation), which calls the development [a victory](https://www.eff.org/deeplinks/2022/01/victory-google-releases-disable-2g-feature-new-android-smartphones) for privacy protection.


Caught by “stingrays”
---------------------


A cell-site simulator, also known as “stingray” or IMSI Catcher, is a device that masquerades as a cell tower, forcing cell phones in their range to connect to it.


This connection enables the operators of these Stingrays to perform man-in-the-middle attacks and intercept sensitive personal information such as: 


* Device IMSI (international mobile subscriber identity)
* Call metadata like dialed number and duration
* SMS and voice call content
* Data usage and web browsing history


![Stingray intercepting people communications](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/stingray.jpg)**Stingray intercepting people communications**  
*Source: EFF*
Unfortunately, this method of data interception has been repeatedly and [indiscriminately deployed](https://www.bleepingcomputer.com/news/government/stingray-devices-may-interfere-with-911-emergency-calls/) by [law enforcement authorities](https://thebristolcable.org/2016/10/imsi/) during peaceful protests in otherwise democratic countries where strict data protection laws apply.


Moreover, documented cases of private deployment of “stingrays” have also been [abundant in recent years](https://www.bleepingcomputer.com/news/security/surveillance-firm-pays-1-million-fine-after-spy-van-scandal/), so the abuse of communication network vulnerabilities is widespread.


Most of these vulnerabilities have been addressed in 4G, but the simulated base stations have a way to downgrade nearby device connections to 2G, essentially laying the ground for exploiting old flaws.


Having a way to prevent this on the user end is a significant development, and while stopping 2G connections isn’t dealing with the entire spectrum of security problems, it certainly is a good start.


Disabling 2G on Android
-----------------------


While Google has given Android users the option not to allow 2G cellular connections on their device, the setting is turned on by default.


If you want to turn it off, you can go to ‘**Settings → Network & Internet → SIMs → Allow 2G**’. Depending on your device maker and the Android skin used, the path to access that setting may be different.



![Android option to disable 2G](https://www.bleepstatic.com/images/news/u/1220909/devices/allow-option.png)**Android option to disable 2G**  
*Source: EFF*
Note that this setting has only been made available on Android 12 for now. Bleeping Computer has tested Android 11 and Android 10, but the option is not yet available.


We have asked Google to clarify if there's a hardware requirement too for this new option to work, and they told us that the modem needs to support the 1.6 Radio HAL, which is available only on newer devices.


Also, it’s important to clarify that 2G remains active as a backup for emergency calls no matter what position the toggle is set to, so there’s no way to disable it completely.


Finally, Apple hasn’t given iPhone users a choice to lock their devices to 4G/5G connectivity only, but now that Google has taken that step, it’s likely the competition follows.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Android]] [[2g]] [[Google]] [[Bleeping Computer]]

