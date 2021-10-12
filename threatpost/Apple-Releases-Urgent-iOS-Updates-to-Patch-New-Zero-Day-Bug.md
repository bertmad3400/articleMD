# Apple Releases Urgent iOS Updates to Patch New Zero-Day Bug
### The bug is under attack. Within hours of the patch release, a researcher published POC code, calling it a “great” flaw that can be used for jailbreaks and local privilege escalation. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175419)
+ Date: October 12, 2021  11:17 am
+ Author: Lisa Vaas


## Article:
![apple](https://media.threatpost.com/wp-content/uploads/sites/103/2020/07/01143018/Mac-Malware.jpg)
Apple on Monday rushed out a [security update](https://support.apple.com/en-us/HT212846) for iOS 15.0.2 and iPadOS 15.0.2 to fix a remote code-execution (RCE) zero-day vulnerability that’s being actively exploited.


Within hours, a security researcher had picked the bug apart and published both proof-of-concept code and an explanation of the vulnerability, meaning that now’s a really good time to update your iOS device.


A week and a half ago, Apple released iOS 15.0.1 to fix a [slew of performance glitches](https://www.zdnet.com/article/can-you-trust-ios-15-0-1/), but iOS 15.0.2 is the first security update for the new OS.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Monday’s patch addresses a memory-corruption zero day – tracked as CVE-2021-30883 – in IOMobileFrameBuffer, which is a kernel extension that acts as a [screen framebuffer](https://en.wikipedia.org/wiki/Framebuffer), allowing developers to control how the memory in a device uses the screen display.


“An application may be able to execute arbitrary code with kernel privileges. Apple is aware of a report that this issue may have been actively exploited,” the company said.


Attackers who get access to kernel privileges gain full control of an iOS device.


Apple typically doesn’t choose to hand weapons to attackers. True to form, the company kept potential attack blueprints close to its vest: It didn’t release technical details for either the vulnerability nor the attack(s) that have exploited it.


Not all are as cautious. Shortly after the patch was released, a security researcher named Saar Amar published both a [technical explanation and proof-of-concept exploit code](https://saaramar.github.io/IOMFB_integer_overflow_poc/). He said that he thought that the bug is “highly interesting because it’s accessible from the app sandbox (so it’s great for jailbreaks)”


Jailbreaking – exploiting flaws in a locked-down device in order to install software other than what the manufacturer had in mind or makes available – gives a device owner the ability to gain full access to the root of the operating system and to access all the features.


A ‘Great’ Bug
-------------


Besides being “great” for jailbreaks, the researcher also said that the vulnerability is “a good candidate for [local privilege escalation, or LPE] exploits in chains (WebContent, etc.).”


“Therefore, I decided to take a quick look, bindiff the patch, and identify the root cause of the bug,” the researcher explained. They were referring to BinDiff, a comparison tool for binary files that helps to quickly find differences and similarities in disassembled code. It’s used by security researchers and engineers to identify and isolate fixes for vulnerabilities in vendor-supplied patches and to analyze multiple versions of the same binary.


“After bindiffing and reversing, I saw that the bug is great, and I decided to write this short blogpost, which I hope you’ll find helpful,” the security researcher wrote. “I really want to publish my bindiff findings as close to the patch release as possible, so there will be no full exploit here; However, I did manage to build a really nice and stable POC that results in a great panic at the end,” they said, adding a smiley.


Monday’s zero-day is a kissing cousin to a critical memory-corruption flaw that [Apple patched in July.](https://threatpost.com/apple-patches-actively-exploited-zero-day-in-ios-macos/168177/) That bug, [CVE-2021-30807](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30807), was also actively exploited, also found in the IOMobileFrameBuffer extension in both iOS and macOS, and likewise used to take over systems.


Monday’s update, iOS 15.0.2, is available for iPhone 6s and later, iPad Pro (all models), iPad Air 2 and later, iPad 5th generation and later, iPad mini 4 and later, and iPod touch (7th generation).


Apple credited an anonymous researcher with the find.


The fix comes just weeks after Apple’s September release of [iOS 15](https://www.apple.com/ios/ios-15/features/), replete with its much-ballyhooed new security defenses. Specifically, the new operating system comes with a built-in two-factor authentication (2FA) code generator, on-device speech recognition and multiple anti-tracking security and privacy features. The speech recognition is meant to skirt the privacy concerns that have arisen around iPhone biometrics being sent off to the cloud to be processed (and sometimes [eavesdropped on](https://threatpost.com/amazon-auditors-listen-to-echo-recordings-report-says/143696/) by humans)


iOS 15 also included [patches](https://support.apple.com/en-ca/HT212814) for at least 22 security vulnerabilities, including some that exposed iPhone and iPad users to remote denial-of-service (DoS) and remote execution of arbitrary code with kernel privileges.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[iPad]] [[later,]] [[Monday’s]] [[iPhone]] [[ThreatPost]]
