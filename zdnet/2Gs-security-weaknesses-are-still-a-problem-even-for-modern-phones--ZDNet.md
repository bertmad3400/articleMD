# 2G's security weaknesses are still a problem, even for modern phones | ZDNet
### EFF urges Apple to follow Google and give smartphone users the option to dodge 2G.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/2gs-security-weaknesses-are-still-a-problem-even-for-modern-phones/
+ Date: 2022-01-17 11:10:32
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/2b7cef157d5879210d71e1b73b799895d1086dc6/2021/09/21/9ace91bb-15e2-4b5f-90dc-a721785f2af9/shutterstock-129038348.jpg?width=770&height=578&fit=crop&auto=webp)

Google recently added an option to switch off insecure 2G connectivity in Android smartphone modems, a move that has been welcomed by digital civil liberties group the Electronic Frontier Foundation (EFF).

It applauded Google for adding the new setting in Android 12 and has now called on Apple to implement the feature, too. 


2G is an early digital cellular network standard that emerged in the early 1990s, when Nokia still ruled mobile. As EFF notes, 2G was developed when standards bodies didn't account for threats like rogue cell towers or the need for strong encryption. 

**SEE: [Best cheap 5G phone 2022: No need to pay flagship prices for quality devices](https://www.zdnet.com/article/best-cheap-5g-phones/)**

"There are two main problems with 2G. First, it uses weak encryption between the tower and device that can be cracked in real time by an attacker to intercept calls or text messages. In fact, the attacker can do this passively without ever transmitting a single packet," [EFF notes](https://www.eff.org/deeplinks/2022/01/victory-google-releases-disable-2g-feature-new-android-smartphones). 

"The second problem with 2G is that there is no authentication of the tower to the phone, which means that anyone can seamlessly impersonate a real 2G tower and a phone using the 2G protocol will never be the wiser."

Also known as IMSI – international mobile subscriber identity – catchers, the ability to spoof base stations has been used by law enforcement and others worldwide to intercept mobile phone traffic and location data by forcing devices with 2G modems to connect to the 2G surveillance devices. While newer standards like 3G, 4G and 5G are [designed to protect against this attack](https://www.zdnet.com/article/stingray-spying-5g-will-protect-you-against-surveillance-attacks-say-standards-setters/), newer ISMI catchers can be used in so-called [downgrade attacks](https://www.zdnet.com/article/stingray-security-flaw-cell-networks-phone-tracking-surveillance/) since mobile modems still support 2G. 






"This makes every user vulnerable – from journalists and activists to medical professionals, government officials, and even law enforcement," the EFF warns.

The new setting to disable 2G is available on newer Android phones. On the Google Pixel it can be changed via Settings > Network & Internet > SIMs > Allow 2G, where there is an option to disable 2G. However, 2G is enabled by default to support emergency calls, so users must manually toggle it off. 

The new setting may not be available on older Android device and is only available on newer Samsung phones under a different setting. 

[Via Ars Technica](https://arstechnica.com/gadgets/2022/01/eff-praises-androids-new-2g-kill-switch-wants-apple-to-follow-suit/), Google introduced the 2G disable option in Android 12, but since it implemented it in the radio hardware abstraction layer (HAL), it's only available in Android devices that implemented that version of the radio HAL. HALs sit between Android and the hardware driver and don't get updated frequently. 

Google explains in [Android 12 release notes](https://source.android.com/setup/start/android-12-release#2g-toggle) that the toggle to disable 2G is part of Radio 1.6 HAL and that, while the toggle is enabled by default, carriers can disable the feature at runtime. 

"Device manufacturers must ensure that all networks are available during emergency calling," Google adds. 

While operators in North America, South Korea, Japan and Taiwan have already turned off 2G networks, many networks in Europe will support 2G through to 2025 and in some cases even after switching off 3G, [according to cellular IoT firm EMnify](https://www.emnify.com/blog/global-2g-phase-out).   

EFF is calling on Google, Apple and Samsung to improve availability of options to disable 2G at the user's end. 

"We are very pleased with the steps that Google has taken here to protect users from vulnerabilities in 2G, and though there is a lot more work to be done, this will ensure that many people can finally receive a basic level of protection," EFF says. 

"We strongly encourage Google, Apple, and Samsung to invest more resources into radio security so they can better protect smartphone owners."





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Healthcare]]

#### Location:
[[victim.country.name=Japan]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=South Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[2g]] [[Google]] [[Android]] [[Samsung]] [[ZDNet]]

