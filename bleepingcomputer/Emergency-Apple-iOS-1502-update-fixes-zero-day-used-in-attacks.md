# Emergency Apple iOS 15.0.2 update fixes zero-day used in attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/emergency-apple-ios-1502-update-fixes-zero-day-used-in-attacks/)
+ Date: October 11, 2021
+ Author: Lawrence Abrams


## Article:
![Apple vulnerability](https://www.bleepstatic.com/content/hl-images/2021/02/10/Apple_logo.jpg)


Apple has released iOS 15.0.2 and iPadOS 15.0.2 to fix a zero-day vulnerability that is actively exploited in the wild in attacks targeting Phones and iPads.


This vulnerability, tracked as CVE-2021-30883, is a critical memory corruption bug allowing an application to execute commands on vulnerable devices with kernel privileges.


As kernel privileges allow the application to execute any command on the device, threat actors could potentially use it to steal data or install further malware.


While Apple has not provided any details on how this vulnerability was used in attacks, they state that there are reports of it being actively used in attacks.


"Apple is aware of a report that this issue may have been actively exploited," the company said in a [security advisory](https://support.apple.com/en-us/HT212846) published earlier today.


Apple purposely keeps vulnerability reports vague to make sure the update is applied to as many devices as possible before other threat actors can learn the details or reverse engineer the patch to create their own exploits.


The list of impacted devices is quite extensive, affecting older and newer models, including iPhone 6s and later, iPad Pro (all models), iPad Air 2 and later, iPad 5th generation and later, iPad mini 4 and later, and iPod touch (7th eneration).


While it is possible that the vulnerability is used in targeted attacks and is not widely used, it is strongly advised to install the update as soon as possible due to its severity.


Zero-days gone wild
-------------------


Besides today's zero-day, Apple has fixed what feels like a never-ending stream of zero-day vulnerabilities used in attacks against iPhone, iPads, and macOS devices:


* [two zero-days earlier this month](https://www.bleepingcomputer.com/news/apple/apple-fixes-ios-zero-day-used-to-deploy-nso-iphone-spyware/), one of them used also used to install Pegasus spyware on iPhones,
* the [FORCEDENTRY exploit](https://www.bleepingcomputer.com/news/apple/new-zero-click-iphone-exploit-used-to-deploy-nso-spyware/) disclosed in August (previously tracked by Amnesty Tech as Megalodon),
* [three iOS zero-days](https://support.apple.com/en-us/HT212146) (CVE-2021-1870, CVE-2021-1871, CVE-2021-1872) in February, exploited in the wild and reported by anonymous researchers,
* an [iOS zero-day](https://www.bleepingcomputer.com/news/security/apple-fixes-a-ios-zero-day-vulnerability-actively-used-in-attacks/) (CVE-2021-1879) in March that may have also been actively exploited,
* one zero-day [in iOS (CVE-2021-30661) and one in macOS (CVE-2021-30657)](https://www.bleepingcomputer.com/news/security/apple-fixes-macos-zero-day-bug-exploited-by-shlayer-malware/) in April, exploited by Shlayer malware,
* [three other iOS zero-days](https://www.bleepingcomputer.com/news/apple/apple-fixes-2-ios-zero-day-vulnerabilities-actively-used-in-attacks/) (CVE-2021-30663, CVE-2021-30665, and CVE-2021-30666) in May, bugs allowing for arbitrary remote code execution (RCE) simply by visiting malicious websites,
* [a macOS zero-day (CVE-2021-30713)](https://www.bleepingcomputer.com/news/security/apple-fixes-three-zero-days-one-abused-by-xcsset-macos-malware/) in May, which was abused by the XCSSET malware to bypass Apple's TCC privacy protection,
* [two iOS zero-day bugs (CVE-2021-30761 and CVE-2021-30762)](https://www.bleepingcomputer.com/news/security/apple-fixes-ninth-zero-day-bug-exploited-in-the-wild-this-year/) in June that "may have been actively exploited" to hack into older iPhone, iPad, and iPod devices.


Last month, a researcher [publicly disclosed exploits for three zero-day vulnerabilities](https://www.bleepingcomputer.com/news/security/researcher-drops-three-ios-zero-days-that-apple-refused-to-fix/) after Apple delayed patching and failed to credit the person who reported them.




#### Tags:
[[zero-day]] [[later,]] [[iPad]] [[macOS]] [[zero-days]] [[Bleeping Computer]]
