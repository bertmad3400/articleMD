# Apple fixes iOS zero-day used to deploy NSO iPhone spyware
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/apple/apple-fixes-ios-zero-day-used-to-deploy-nso-iphone-spyware/)
+ Date: September 13, 2021
+ Author: Lawrence Abrams


## Article:
![Apple](https://www.bleepstatic.com/content/hl-images/2021/07/27/Apple.jpg)


Apple has released security updates to fix two zero-day vulnerabilities that have been seen exploited in the wild to attack iPhones and Macs. One is known to be used to install the Pegasus spyware on iPhones.


The vulnerabilities are tracked as CVE-2021-30860 and CVE-2021-30858, and both allow maliciously crafted documents to execute commands when opened on vulnerable devices.


The CVE-2021-30860 CoreGraphics vulnerability is an integer overflow bug discovered by [Citizen Lab](https://citizenlab.ca/) that allows threat actors to create malicious PDF documents that execute commands when opened in iOS and macOS.


CVE-2021-30858 is a WebKit use after free vulnerability allowing hackers to create maliciously crafted web page that execute commands when visiting them on iPhones and macOS.  Apple states that this vulnerability was disclosed anonymously.


"Apple is aware of a report that this issue may have been actively exploited," the company said in [security advisories](https://support.apple.com/en-us/HT201222) published today regarding both vulnerabilities.


While Apple did not release any further information on how the vulnerabilities were used in attacks, [Citizen Lab has confirmed](https://citizenlab.ca/2021/09/forcedentry-nso-group-imessage-zero-click-exploit-captured-in-the-wild/) that CVE-2021-30860 is a zero-day zero-click iMessage exploit named 'FORCEDENTRY.'


The FORCEDENTRY exploit was discovered to be used to bypass the [iOS BlastDoor](http://googleprojectzero.blogspot.com/2021/01/a-look-at-imessage-in-ios-14.html) security feature [to deploy the NSO Pegasus spyware](https://www.bleepingcomputer.com/news/apple/new-zero-click-iphone-exploit-used-to-deploy-nso-spyware/) on devices belonging to Bahraini activists.


BleepingComputer has contacted Citizen Lab with further questions about the attacks but has not heard back at this time.


Apple zero-days run rampant in 2021
-----------------------------------


It has been a very busy year for Apple with what seems like an unending streaming of zero-day vulnerabilities used in targeted attacks against iOS and Mac devices.


* The [FORCEDENTRY exploit](https://www.bleepingcomputer.com/news/apple/new-zero-click-iphone-exploit-used-to-deploy-nso-spyware/) disclosed in August (previously tracked by Amnesty Tech as Megalodon),
* [three iOS zero-days](https://support.apple.com/en-us/HT212146) (CVE-2021-1870, CVE-2021-1871, CVE-2021-1872) in February, exploited in the wild and reported by anonymous researchers,
* an [iOS zero-day](https://www.bleepingcomputer.com/news/security/apple-fixes-a-ios-zero-day-vulnerability-actively-used-in-attacks/) (CVE-2021-1879) in March that may have also been actively exploited,
* one zero-day [in iOS (CVE-2021-30661) and one in macOS (CVE-2021-30657)](https://www.bleepingcomputer.com/news/security/apple-fixes-macos-zero-day-bug-exploited-by-shlayer-malware/) in April, exploited by Shlayer malware,
* [three other iOS zero-days](https://www.bleepingcomputer.com/news/apple/apple-fixes-2-ios-zero-day-vulnerabilities-actively-used-in-attacks/) (CVE-2021-30663, CVE-2021-30665, and CVE-2021-30666) in May, bugs allowing for arbitrary remote code execution (RCE) simply by visiting malicious websites,
* [a macOS zero-day (CVE-2021-30713)](https://www.bleepingcomputer.com/news/security/apple-fixes-three-zero-days-one-abused-by-xcsset-macos-malware/) in May, which was abused by the XCSSET malware to bypass Apple's TCC privacy protections.
* [two iOS zero-day bugs (CVE-2021-30761 and CVE-2021-30762)](https://www.bleepingcomputer.com/news/security/apple-fixes-ninth-zero-day-bug-exploited-in-the-wild-this-year/) in June that "may have been actively exploited" to hack into older iPhone, iPad, and iPod devices.


Project Zero also disclosed [11 zero-day vulnerabilities](https://www.bleepingcomputer.com/news/security/hacking-group-used-11-zero-days-to-attack-windows-ios-android-users/) this year that were used in attacks targeting Windows, iOS , and Android devices.


*Update 9/13/21: Added confirmed from Citizen Labs that this update fixes the FORCEDENTRY vulnerability.*




#### Tags:
[[zero-day]] [[devices.]] [[CVE-2021-30860]] [[FORCEDENTRY]] [[zero-days]] [[Bleeping Computer]]
