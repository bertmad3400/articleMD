# Researcher dumps three iOS zero-days after Apple failed to fix issues for months
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/researcher-dumps-three-ios-zero-days-after-apple-failed-to-fix-issues-for-months/)
+ Date: September 24, 2021
+ Author: Catalin Cimpanu


## Article:
![Researcher dumps three iOS zero-days after Apple failed to fix issues for months](https://therecord.media/wp-content/uploads/2021/09/iPhone-iOS.png)

A security researcher has published on Thursday details about three iOS zero-day vulnerabilities, claiming that Apple has failed to patch the issues, which they first reported to the company earlier this year.


Going by the pseudonym of Illusion of Chaos, the researcher has published their [findings](https://habr.com/ru/post/579714/) on Russian blogging platform Habr and has released proof-of-concept code for each vulnerability on GitHub.


This includes:


A vulnerability in the Gamed daemon that can grant access to user data such as AppleID emails, names, auth token, and grant file system access. PoC [here](https://github.com/illusionofchaos/ios-gamed-0day).


A vulnerability in the nehelper daemon that can be used from within an app to learn what other apps are installed on a device. PoC [here](https://github.com/illusionofchaos/ios-nehelper-enum-apps-0day).


An additional vulnerability in the nehelper daemon can also be used from within an app to gain access to a device’s WiFi information. PoC [here](https://github.com/illusionofchaos/ios-nehelper-wifi-info-0day).


The researcher said the vulnerabilities are still exploitable in iOS 15, released earlier this week.


The researcher also published proof of concept code for [a fourth issue](https://github.com/illusionofchaos/ios-analyticsd-pre14.7-exploit), affecting the iOS Analyticsd daemon. This was also part of the initial four bugs he reported to Apple in April but was the only issue patched by the OS maker in iOS 14.7 in July.


An Apple spokesperson did not return a request for comment, but several security researchers told *The Record* that Apple might not have prioritized the three issues as they could not lead to “code execution.”



> I want to share my frustrating experience participating in Apple Security Bounty program. I’ve reported four 0-day vulnerabilities this year between March 10 and May 4, as of now three of them are still present in the latest iOS version (15.0) and one was fixed in 14.7, but Apple decided to cover it up and not list it on the [security content page](https://support.apple.com/en-us/HT212601). When I confronted them, they apologized, assured me it happened due to a processing issue and promised to list it on the security content page of the next update. There were three releases since then and they broke their promise each time.
> 
> Illusion of Chaos on Habr


The researcher cited similar experiences from other researchers, all of which reported issues to Apple’s bug bounty program, only to be ignored, have bug bounties reduced and payments delayed for their work [[1](https://medium.com/macoclock/apple-security-bounty-a-personal-experience-fe9a57a81943https://medium.com/macoclock/apple-security-bounty-a-personal-experience-fe9a57a81943), [2](https://thezerohack.com/apple-vulnerability-bug-bountyhttps://thezerohack.com/apple-vulnerability-bug-bounty), [3](https://thezerohack.com/apple-vulnerability-bug-bountyhttps://theevilbit.github.io/posts/experiences_with_asb/), [4](https://gigazine.net/gsc_news/en/20200701-apple-security-bounty-program-tcchttps://theevilbit.github.io/posts/experiences_with_asb/)].











Illusion of Chaos actions come after another researcher, disheartened with Apple’s bug bounty program, also decided to release an [iOS lock screen bypass](https://therecord.media/researcher-discloses-iphone-lock-screen-bypass-on-ios-15-launch-day/) on the iOS 15 launch day, on Monday.


A [Washington Post article](https://www.washingtonpost.com/technology/2021/09/09/apple-bug-bounty/) published two weeks ago contained similar accusations from other researchers about how the company’s security team was leaving bug reports unsolved for months, shipping incomplete fixes, low-balling monetary rewards, or banning researchers from their program when they complained.





#### Tags:
[[PoC]] [[here.]] [[The Record]]
