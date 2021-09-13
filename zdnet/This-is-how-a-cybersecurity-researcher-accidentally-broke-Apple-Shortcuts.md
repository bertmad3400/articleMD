# This is how a cybersecurity researcher accidentally broke Apple Shortcuts
### Detectify explains how investigating CloudKit resulted in Shortcuts disruption for users back in March.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-is-how-a-cybersecurity-researcher-accidentally-broke-apple-shortcuts/)
+ Date: September 13, 2021 -- 14:19 GMT (15:19 BST)
+ Author: Charlie Osborne


## Article:
Unknown

A Detectify researcher has explained how an investigation into Apple CloudKit led to the accidental downtime of Shortcuts functionality for users. 


In March, [Apple](https://www.zdnet.com/topic/apple/) users began to report error messages when they attempted to open shared shortcuts. As noted [by 9to5Mac](https://9to5mac.com/2021/03/24/icloud-shortcut-sharing-broken/), this bizarre issue was of particular concern to content creators who shared shortcuts with their followers via iCloud, who suddenly found their links were broken.  

Reports began to surface on March 24, and a day later, the iPad and iPhone maker [told MacStories](https://twitter.com/viticci/status/1374925965239914496) editor-in-chief Federico Viticci that the company was "working to restore previously shared shortcuts as quickly as possible." 

According to Detectify Knowledge Advisor and bug bounty hunter Frans Rosén, the root cause of the issue was a misconfiguration flaw he accidentally stumbled upon -- and triggered -- in Apple CloudKit. 

On Monday, Rosén [published details](https://labs.detectify.com/2021/09/13/hacking-cloudkit-how-i-accidentally-deleted-your-apple-shortcuts/) on the situation, in which he was examining the security of Apple services. Rosén's exploration began in February and in particular, he wanted to investigate the [CloudKit framework](https://developer.apple.com/documentation/cloudkit), a platform for creating containers suitable for data storage in the Apple ecosystem.  

Rosén says that he noticed that many of Apple's own applications stored information in databases based on CloudKit and so he was "curious" to know if any specific apps' data could be modified by obtaining access to their public CloudKit containers.

The researcher found that various APIs were being used to connect to CloudKit. According to Rosén, there are three scopes in the containers: Private (information is only accessed by you), Shared (shareable between users), and Public (accessible to anyone). Zones are also set with varying permission levels.  






Rosén began testing these permissions and found several vulnerabilities in CloudKit relating to iCrowd+, Apple News, and Shortcuts which permitted him to tamper with content, including stock entries.  

The most prominent and public issue, found in Shortcuts during March, "caused all Shortcut sharing links to break, and it was quickly noticed amongst Apple users, media reporters, and especially Shortcuts fans," Detectify said.

According to Rosén, he had previously tested different ways to delete public zones and permission was always denied -- however, in the Shortcuts CloudKit database, the researcher was surprisingly able to create zones and was also given an "OK" message in an attempt to delete a default zone. 

This was caused by a misconfiguration on Apple's part.  

"All of them were gone," the researcher said. "I now realized that the deletion did somehow work, but that the \_defaultZone never disappeared. When I tried sharing a new shortcut it also did not work, at least not to begin with, most likely due to the record types also being deleted."

At this point, Rosén reached out to Apple's security team, who asked him to stop testing immediately. Apple Security then set to work resolving the issue, restoring Shortcuts functionality and patching the problem in the process by refining its security controls and removing the options to both create new and delete existing public zones.

It should be noted that the break did not allow the researcher access to any user or sensitive data.

While accidental, and causing not only panic for the researcher but also unintentional downtime for users, Rosén was awarded a $28,000 bug bounty for his discovery via the Apple Security Bounty program. 

"Approaching CloudKit for bugs turned out to be a lot of fun, a bit scary, and a really good example of what a real deep-dive into one technology can result in when hunting bugs," Rosén commented. "The Apple Security team was incredibly helpful and professional throughout the process of reporting these issues."

The vulnerabilities in iCrowd+ and Apple News also earned him bounties of $12,000 and $24,000.

"We would like to thank this researcher for working side by side with us to keep our users and their data safe," an Apple spokesperson told ZDNet. "He immediately reported his actions so that we were able to quickly fix the issues documented and restore functionality after the researcher unintentionally disrupted the ability to use iCloud sharing links for Shortcuts."

###  Previous and related coverage

* [Epic Games appeals decision made in antitrust lawsuit against Apple](https://www.zdnet.com/article/epic-games-appeals-decision-made-in-antitrust-lawsuit-against-apple/)  

* [US judge rules Apple can't block in-app purchasing](https://www.zdnet.com/article/us-judge-rules-apple-cant-block-in-app-purchasing/)  

* [Apple confirms four new iPhones, and a nasty surprise for iPhone 12 owners](https://www.zdnet.com/article/apple-confirms-four-new-iphones-and-a-nasty-surprise-for-iphone-12-owners/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[CloudKit]] [[Rosén]] [[Detectify]] [[Rosén,]] [[ZDNet]]
