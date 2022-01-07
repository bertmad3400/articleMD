# NoReboot attack fakes iOS phone shutdown to spy on you | ZDNet
### The PoC malware can be used to hijack microphone and camera functions.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/noreboot-attack-fakes-ios-phone-shutdown-to-spy-on-you/
+ Date: 2022-01-07 11:08:48
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/45d40582c44c17f70397ab585cadce33093fbb5b/2021/11/30/47400657-5820-4d86-a41e-a4f47687d4f6/stolen-iphone.png?width=770&height=578&fit=crop&auto=webp)

A new technique that fakes iPhone shutdowns to perform surveillance has been published by researchers. 


Dubbed "NoReboot," ZecOps' proof-of-concept (PoC) attack is described as a persistence method that can circumvent the normal practice of restarting a device to clear malicious activity from memory. 

Making its debut with [an analysis](https://blog.zecops.com/research/persistence-without-persistence-meet-the-ultimate-persistence-bug-noreboot/) and a public [GitHub](https://github.com/ZecOps/public/tree/master/fake_shutdown_POC) repository this week, ZecOps said that the NoReboot Trojan simulates a true shutdown while providing a cover for the malware to operate – which could include the covert hijacking of microphone and camera capabilities to spy on a handset owner.  

"The user cannot feel a difference between a real shutdown and a "fake shutdown," the researchers say. "There is no user interface or any button feedback until the user turns the phone back "on"."

The technique takes over the expected shutdown event by injecting code into three daemons: InCallService, SpringBoard, and backboardd.  

When an iPhone is turned off, there are physical indicators that this has been completed successfully, such as a ring or sound, vibration, and the Apple logo appearing onscreen – but by disabling "physical feedback," the malware could create the appearance of a shutdown while a live connection to an operator is maintained.  

![persistence-noreboot-3.png]()![persistence-noreboot-3.png](https://www.zdnet.com/a/img/resize/aceb43d65857171d5c50191ae2027706e1303d01/2022/01/07/9d18f772-535e-410b-ba73-3456380727ea/persistence-noreboot-3.png?width=470&fit=bounds&auto=webp)
 ZecOps
 "When you slide to power off, it is actually a system application /Applications/InCallService.app sending a shutdown signal to SpringBoard, which is a daemon that is responsible for the majority of the UI interaction," the researchers explained. "We managed to hijack the signal by hooking the Objective-C method -[FBSSystemService shutdownWithOptions:]. Now instead of sending a shutdown signal to SpringBoard, it will notify both SpringBoard and backboardd to trigger the code we injected into them."






The spinning wheel indicating a shutdown process can then be hijacked via backboardd and the SpringBoard function can both be forced to exit and blocked from restarting again. ZecOps said that by taking over SpringBoard, a target iPhone can "look and feel" like it is not turned on, which is the "perfect disguise for the purpose of mimicking a fake power off." 

Users, however, still have the option of a forced restart. This is where tampering with backboardd further comes in – by monitoring user input, including how long buttons are held, a reboot can be simulated just before a true restart takes place, such as by displaying the Apple logo early.  

"Stopping users from manually restarting an infected device by making them believe they have successfully done so is a notable malware persistence technique," Malwarebytes [commented](https://blog.malwarebytes.com/trojans/2022/01/new-iphone-malware-spies-via-camera-when-device-appears-off/). "On top of that, human deception is involved: Just when you thought it's gone, it still pretty much there." 

As the technique focuses on tricking users rather than vulnerabilities or bugs in the iOS platform, this is not something that can be fixed with a patch. ZecOps says that the NoReboot method impacts [all versions](https://twitter.com/ZecOps/status/1478779313436573700) of iOS and only hardware indicators could help in detecting this form of attack technique.  

A video demonstration can be found below. 





 window.ZdnetFunctions.logWithLabel('%c One Trust ', "IFrame loaded: iframe\_youtube with class optanon-category-3");
 

###  Previous and related coverage

* [Apple: Forcing app sideloading would turn iPhones into virus-prone 'pocket PCs'](https://www.zdnet.com/article/apple-forcing-app-sideloading-would-turn-iphones-into-virus-prone-pocket-pcs/)
* [Apple isn't happy about the amount of Mac malware out there](https://www.zdnet.com/article/apple-isnt-happy-about-the-amount-of-mac-malware-out-there/)
* [Apple just fixed a security flaw that allowed malware to take screenshots on Macs](https://www.zdnet.com/article/apple-just-fixed-a-security-flaw-that-allowed-malware-to-take-screenshots-on-macs/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0 



---





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Zecops]] [[Malware]] [[Backboardd]] [[Iphone]] [[Noreboot]] [[ZDNet]]

