# Apple fixes doorLock bug that can disable iPhones and iPads
### Apple has released security updates to address a persistent denial of service (DoS) dubbed doorLock that would altogether disable iPhones and iPads running HomeKit on iOS 14.7 and later.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/apple-fixes-doorlock-bug-that-can-disable-iphones-and-ipads/
+ Date: 2022-01-12T16:45:03-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/01/09/Apple_logo.jpg)

![Apple fixes doorLock bug that can disable iPhones and iPads](https://www.bleepstatic.com/content/hl-images/2021/01/09/Apple_logo.jpg)


Apple has released security updates to address a persistent denial of service (DoS) dubbed doorLock that would altogether disable iPhones and iPads running HomeKit on iOS 14.7 and later.


HomeKit is an Apple protocol and framework that allow iOS and iPadOS users to discover and control smart home appliances on their network.


As the company explained in a [security advisory](https://support.apple.com/en-us/HT213043) issued today, [the doorLock vulnerability](https://www.bleepingcomputer.com/news/security/apple-ios-vulnerable-to-homekit-doorlock-denial-of-service-bug/) tracked as [CVE-2022-22588](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22588) will crash affected iOS and iPadOS devices when processing maliciously crafted HomeKit accessory names.


Apple has addressed this severe resource exhaustion issue in iOS 15.2.1 and iPadOS 15.2.1 by adding improved input validation which no longer allows attackers to disable vulnerable devices.


Devices that received security updates today include iPhone 6s and later, iPad Pro (all models), iPad Air 2 and later, iPad 5th generation and later, iPad mini 4 and later, and iPod touch (7th generation).


"Four months ago I discovered and reported a serious denial of service bug in iOS that still remains in the latest release. It persists through reboots and can trigger after restores under certain conditions," Trevor Spiniolas, the programmer and "beginning security researcher" who spotted and reported the bug.


"All the requirements are default settings. When someone sets up their iOS device, everything is already in order for the bug to work. If they accept a malicious home invitation from there, their device stops working."



Fix delayed since August
------------------------


According to Spiniolas, Apple has known about doorLock since August 2021, 2021, but pushed the security update multiple times despite repeatedly promising to fix it.


"I believe this bug is being handled inappropriately as it poses a serious risk to users and many months have passed without a comprehensive fix," Spinolas said.


"The public should be aware of this vulnerability and how to prevent it from being exploited, rather than being kept in the dark."


The researcher says attackers would have to change the name of a HomeKit device to large strings of up to 500,000 characters and trick the target into accepting a Home invitation.


Once the target joins the attacker's HomeKit network, their device becomes unresponsive and eventually crashes.


The only way to recover from such an attack would be to factory reset the disabled device, given that it will once again crash after restarting and signing back into the iCloud account linked to the HomeKit device.


Zero-day patches also delayed
-----------------------------


In September, software developer Denis Tokarev also [dropped proof-of-concept exploit code for three iOS zero-day flaws](https://www.bleepingcomputer.com/news/security/researcher-drops-three-ios-zero-days-that-apple-refused-to-fix/) on GitHub after Apple delayed patching and failed to credit him when patching a fourth in July.


One month later, with the release of iOS 15.0.2, Apple fixed one of the 'gamed' zero-day vulnerabilities reported by Tokarev.


However, Apple didn't acknowledge or credit him for the discovery and also [asked him to keep quiet](https://www.bleepingcomputer.com/news/apple/apple-silently-fixes-ios-zero-day-asks-bug-reporter-to-keep-quiet/) and not disclose to others that the company failed to give him credit for the bug.


Other security researchers and bug bounty hunters have also gone through similar experiences saying that [they have been kept in the dark](http://www.imore.com/developer-feels-robbed-apples-security-bounty-program) for [months on end](https://twitter.com/theevilbit/status/1417935753775132676) with Apple [refusing to reply to their messages](https://theevilbit.github.io/posts/experiences_with_asb/).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Denis]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]] [[victim.industry.name=Manufacturing]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Homekit]] [[Ipad]] [[Doorlock]] [[Ipados]] [[Bleeping Computer]]
#### CVE's
[[CVE-2022-22588]]

