# Apple Patches Critical iOS Bugs; One Under Attack
### Researchers found that one critical flaw in question is exploitable from the browser, allowing watering-hole attacks.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175803)
+ Date: October 27, 2021  12:14 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/27115334/apple-with-bandaid-e1635350026287.jpeg)
Apple lovers who haven’t yet updated to [iOS 15](https://www.macworld.com/article/357166/ios-15-update-right-away-or-wait.html), you may want to pop into Settings to freshen up your iPhone now: Apple has released several critical security updates that might light a fire under your britches.


On Monday and Tuesday, Apple released iOS 14.8.1, iPadOS 14.8.1, watchOS 8.1 and tvOS 15.1, patching 24 CVEs in total.


[Apple’s security page](https://support.apple.com/en-us/HT212868) has all the details about the CVEs, which include multiple issues in iOS components that, if exploited, could lead to arbitrary code execution, sometimes with kernel privileges that would let an attacker get to the heart of the operating system.


Critical, Easily/Already Exploited Bug
--------------------------------------


In one case – a memory-corruption issue in IOMobileFrameBuffer for Apple TV – the computing giant said that it’s “aware of a report that this issue may have been actively exploited” — which other researchers confirmed.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


This one is particularly worrisome, given that researchers already found that the flaw is exploitable from the browser, making it “perfect for one-click & waterholing mobile attacks,” mobile security firm ZecOps said earlier this month.



In a [watering-hole attack,](https://threatpost.com/watering-holes-asian-ethnic-flash-update-decoy/154323/) a threat actor infects with malware the websites that could attract a target, in hopes that somebody will eventually drop in and get infected.


Understandably, Apple keeps a lid on details that might help more attackers do damage. What we do know is that this bug could allow an application to execute arbitrary code with kernel privileges.


Malwarebyte Labs has a nice [rundown](https://blog.malwarebytes.com/exploits-and-vulnerabilities/2021/10/update-now-apple-patches-bugs-in-ios-and-ipados/) on other security-related bugs that stand out in the two dozen CVEs Apple addressed this week.


Why Did Apple Let iOS 14 Users Stay Put?
----------------------------------------


Earlier this year, [Apple announced](https://www.apple.com/ios/ios-15/features/) that it was giving users a choice: They could update to iOS 15 as soon as it’s released, or stay on iOS 14 but still get important security updates until they’re ready to upgrade.


Why the choice? Some [suggested](https://www.intego.com/mac-security-blog/why-doesnt-apple-want-people-to-upgrade-to-ios-15/) it might have to do with an “urban legend” about Apple slowing down older phones on purpose in order to prod people into upgrading.


Maybe that’s just an oft-circulated conspiracy theory, but it’s rooted in legal comeuppance, at least with regards to battery life: Apple admitted to slowing down phones in 2017 as a way to prevent old batteries from randomly shutting devices off. In November of last year, the company was [fined $113 million](https://www.washingtonpost.com/technology/2020/11/18/apple-fine-battery/) to settle an investigation into what was known as the iPhone “batterygate.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[it’s]] [[ThreatPost]]
