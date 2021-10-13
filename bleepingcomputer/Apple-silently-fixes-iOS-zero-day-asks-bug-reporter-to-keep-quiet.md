# Apple silently fixes iOS zero-day, asks bug reporter to keep quiet
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/apple/apple-silently-fixes-ios-zero-day-asks-bug-reporter-to-keep-quiet/)
+ Date: October 13, 2021
+ Author: Sergiu Gatlan


## Article:
![Apple silently fixes iOS zero-day, asks bug reporter to keep quiet](https://www.bleepstatic.com/content/hl-images/2021/02/10/Apple_xray.jpg)


Apple has silently fixed a 'gamed' zero-day vulnerability with the release of iOS 15.0.2, on Monday, a security flaw that could let attackers gain access to sensitive user information.


The company addressed the bug [without acknowledging or crediting software developer Denis Tokarev](https://twitter.com/illusionofcha0s/status/1447985867734278147) for the discovery even though he reported the flaw seven months before iOS 15.0.2 was released.


Failures to credit bug reports
------------------------------


In July, Apple also silently patched an 'analyticsd' zero-day flaw with the release of 14.7 without crediting Tokarev in the security advisory, instead promising to acknowledge his report in security advisories for an upcoming update.


Since then, Apple published multiple security advisories (iOS 14.7.1, iOS 14.8, iOS 15.0, and iOS 15.0.1) addressing iOS vulnerabilities but, each time, they failed to credit his analyticsd bug report.


"Due to a processing issue, your credit will be included on the security advisories in an upcoming update. We apologize for the inconvenience," Apple told him when asked why the list of fixed iOS security bugs didn't include his zero-day.


Two days ago, [after iOS 15.0.2](https://www.bleepingcomputer.com/news/security/emergency-apple-ios-1502-update-fixes-zero-day-used-in-attacks/) was released, Tokarev emailed again about the lack of credit for the gamed and analyticsd flaws in the security advisories. Apple replied, asking him to treat the contents of their email exchange as confidential.


This wouldn't be the first time Apple's security team asked for confidentiality: the first time [happened in August](https://twitter.com/illusionofcha0s/status/1447985874306846721) when he was told the gamed zero-day would be fixed in a future security update and urged not to disclose the bug publicly.


"All things considered, they treat gamed vulnerability a bit better that analyticsd, at least they don't ignore me and lie to me this time," Tokarev told BleepingComputer.




> 
> Seems that they don't have a separate protocol on handling reports which were already disclosed. And if this message contains a legit excuse, they could save a tiny bit of reputation by making it public. But it's up to them, I won't disclose full message until I get credit. 2/3 [pic.twitter.com/iG6waUELtk](https://t.co/iG6waUELtk)
> 
> 
> — Denis Tokarev (@illusionofcha0s) [October 13, 2021](https://twitter.com/illusionofcha0s/status/1448269165417148418?ref_src=twsrc%5Etfw)


Other bug bounty hunters and security researchers have also reported having similar experiences when reporting vulnerabilities to Apple's product security team via the Apple Security Bounty Program.


Some said bugs reported to Apple were silently fixed, with the company failing to give them credit, just as it happened in this case.


Others weren't paid the amount listed on Apple's official bounty page [[1](http://twitter.com/VBarraquito/status/1438186052808757256?s=20), [2](https://twitter.com/VBarraquito/status/1438186052808757256?s=20)] or [haven't received any payment at all](https://medium.com/macoclock/apple-security-bounty-a-personal-experience-fe9a57a81943), while some [have been kept in the dark](http://www.imore.com/developer-feels-robbed-apples-security-bounty-program) for [months on end](https://twitter.com/theevilbit/status/1417935753775132676) with [no replies to their emails](https://theevilbit.github.io/posts/experiences_with_asb/).


Two zero-days left to (silently) patch
--------------------------------------


In total, Tokarev found four iOS zero-days and reported them to Apple between March 10 and May 4. In September, [he published proof-of-concept exploit code](https://www.bleepingcomputer.com/news/security/researcher-drops-three-ios-zero-days-that-apple-refused-to-fix/) and details on all iOS vulnerabilities after the company failed to credit him after patching the gamed zero-day in July.


If attackers would successfully exploit the four vulnerabilities on unpatched iOS devices (i.e., iPhones and iPads), they could gain access and harvest Apple ID emails, full names, Apple ID authentication tokens, installed apps info, WiFi info, and analytics logs (including medical and device  information).


The complete list of iOS zero-days reported by Tokarev includes:


* [Gamed 0-day](https://github.com/illusionofchaos/ios-gamed-0day) (fixed in iOS 15.0.2): Bug exploitable through user-installed apps from App Store and giving unauthorized access to sensitive data normally protected by a TCC prompt or the platform sandbox ($100,000 on the Apple Security Bounty Program page)


* [Nehelper Enumerate Installed Apps 0-day](https://github.com/illusionofchaos/ios-nehelper-enum-apps-0day) (iOS 15.0): Allows any user-installed app to determine whether any app is installed on the device given its bundle ID.


* [Nehelper Wifi Info 0-day](https://github.com/illusionofchaos/ios-nehelper-wifi-info-0day) (iOS 15.0): Makes it possible for any qualifying app (e.g., possessing location access authorization) to gain access to Wifi information without the required entitlement.


* [Analyticsd (fixed in iOS 14.7)](https://github.com/illusionofchaos/ios-analyticsd-pre14.7-exploit): Allows any user-installed app to access analytics logs.




"We saw your blog post regarding this issue and your other reports. We apologize for the delay in responding to you," Apple told Tokarev 24 hours after publishing the zero-days and the exploit code on his blog.


"We want to let you know that we are still investigating these issues and how we can address them to protect customers. Thank you again for taking the time to report these issues to us, we appreciate your assistance."


Apple has also fixed a second zero-day vulnerability in iOS 15.0.2 and iPadOS 15.0.2, actively exploited in the wild to target iPhones and iPads.


This bug, tracked as CVE-2021-30883, is a critical memory corruption flaw in the IOMobileFrameBuffer, allowing malicious applications to execute commands on vulnerable devices with kernel privileges.


*Apple has not replied to emails BleepingComputer sent since September 24, asking for an official statement and more details.*




#### Tags:
[[Tokarev]] [[zero-day]] [[zero-days]] [[(iOS]] [[0-day]] [[user-installed]] [[Bleeping Computer]]
