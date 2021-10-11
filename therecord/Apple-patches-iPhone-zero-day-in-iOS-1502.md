# Apple patches iPhone zero-day in iOS 15.0.2
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/apple-patches-iphone-zero-day-in-ios-15-0-2/)
+ Date: October 11, 2021
+ Author: Catalin Cimpanu


## Article:
![Apple patches iPhone zero-day in iOS 15.0.2](https://therecord.media/wp-content/uploads/2021/10/iphone-ios-apple.jpg)

Apple has released a security update on Monday for iPhone users to address a vulnerability in the iOS operating system that has been exploited in the wild.


Tracked as **CVE-2021-30883**, the zero-day resides in [IOMobileFramebuffer](https://iphonedev.wiki/index.php/IOMobileFramebuffer), a kernel extension that allows developers to control how a device’s memory handles the screen display—the screen [framebuffer](https://en.wikipedia.org/wiki/Framebuffer), to be more exact.


According to Apple, a malicious application may be able to execute arbitrary code with kernel privileges using this vulnerability. Gaining access to kernel privileges gives attackers full control over the iOS device.


Technical details about the vulnerability, or details about the attacks where the vulnerability has been used, are not available at the time of writing, as Apple usually likes to keep this information secret in order to prevent other threat actors from weaponizing the same bug before users had a chance to patch.


Today’s zero-day is eerily similar to another zero-day, CVE-2021-30807, which [Apple patched in July](https://therecord.media/apple-releases-fix-for-ios-and-macos-zero-day-13th-this-year/).


Users are advised to update to the latest i[OS 15.0.2 and iPad 15.0.2](https://support.apple.com/en-us/HT212846) to mitigate the issue.


Today’s CVE-2021-30883 represents the 17th zero-day that Apple has patched in its products this year.




| CVE | Patch date | Description |
| --- | --- | --- |
| [CVE-2021-1782](https://support.apple.com/en-us/HT212146) | February 1 | A zero-day impacting the macOS, iOS, iPadOS, watchOS, and tvOS kernels. |
| [CVE-2021-1870](https://support.apple.com/en-us/HT212146) | February 1 | WebKit zero-day impacting macOS, iOS, iPadOS, and watchOS |
| [CVE-2021-1871](https://support.apple.com/en-us/HT212146) | February 1 | WebKit zero-day impacting macOS, iOS, iPadOS, and watchOS |
| [CVE-2021-1879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-1879) | March 26 | WebKit bug impacting both old and new-gen iOS, iPadOS, and watchOS |
| [CVE-2021-30657](https://support.apple.com/en-us/HT212325) | April 26 | macOS Gatekeeper bypass abused by Shlayer malware |
| [CVE-2021-30661](https://therecord.media/apple-releases-fixes-for-three-webkit-zero-days-additional-patches-for-a-fourth/) | April 26 | WebKit zero-day impacting old and new-gen iOS, iPadOS, watchOS, and tvOS. |
| [CVE-2021-30663](https://therecord.media/apple-releases-fixes-for-three-webkit-zero-days-additional-patches-for-a-fourth/) | May 3 | WebKit zero-day impacting macOS, iOS, iPadOS, and watchOS |
| [CVE-2021-30665](https://therecord.media/apple-releases-fixes-for-three-webkit-zero-days-additional-patches-for-a-fourth/) | May 3 | WebKit zero-day impacting macOS, iOS, iPadOS, and watchOS |
| [CVE-2021-30666](https://therecord.media/apple-releases-fixes-for-three-webkit-zero-days-additional-patches-for-a-fourth/) | May 3 | WebKit zero-day impacting macOS, iOS, iPadOS, and watchOS |
| [CVE-2021-30713](https://therecord.media/apple-fixes-macos-zero-day-abused-by-xcsset-malware/) | May 24 | macOS TCC bypass abused by XCSSET malware |
| [CVE-2021-30761](https://support.apple.com/en-us/HT212548) | June 14 | WebKit zero-day impacting old-gen iOS devices |
| [CVE-2021-30762](https://support.apple.com/en-us/HT212548) | June 14 | WebKit zero-day impacting old-gen iOS devices |
| [CVE-2021-30807](https://support.apple.com/en-us/HT212623) | July 26 | IOMobileFramebuffer zero-day impacting iOS, iPadOS, and macOS |
| [CVE-2021-30858](https://support.apple.com/en-us/HT212807) | September 13 | WebKit zero-day impacting macOS, iOS, iPadOS, and watchOS |
| [CVE-2021-30860](https://support.apple.com/en-us/HT212807) | September 13 | Zero-day in the CoreGraphics component impacting macOS, iOS, iPadOS, and watchOS |
| [CVE-2021-30869](https://support.apple.com/en-us/HT212824) | September 23 | XNU kernel component zero-day impacting iOS and macOS |
| [CVE-2021-30883](https://support.apple.com/en-us/HT212846) | October 11 | IOMobileFramebuffer zero-day impacting iOS and iPadOS |





#### Tags:
[[zero-day]] [[iOS,]] [[iPadOS,]] [[macOS,]] [[3WebKit]] [[The Record]]
