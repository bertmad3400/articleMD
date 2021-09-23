# Apple fixes another zero-day used to deploy NSO iPhone spyware
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/apple/apple-fixes-another-zero-day-used-to-deploy-nso-iphone-spyware/)
+ Date: September 23, 2021
+ Author: Sergiu Gatlan


## Article:
![Apple fixes another zero-day used to deploy NSO iPhone spyware](https://www.bleepstatic.com/content/hl-images/2021/08/25/Apple-glitch.jpg)


Apple has released security updates to fix three zero-day vulnerabilities exploited in the wild by attackers to hack into iPhones and Macs running older iOS and macOS versions.


Based on the info shared by Apple in today's security advisories [[1](https://support.apple.com/en-us/HT212824), [2](https://support.apple.com/en-us/HT212825)] at least one of the bugs (reported by The Citizen Lab) was likely used to deploy NSO Pegasus spyware on hacked devices.


The three security flaws are tracked as CVE-2021-30860 (in the CoreGraphics framework), CVE-2021-30858 (in the WebKit browser engine), and CVE-2021-30869 (in the XNU operating system kernel), and they were reported by Citizen Lab, Google, and anonymous security researchers.


Successful exploitation of any of these bugs leads to arbitrary code execution on compromised devices, with kernel privileges if the abused zero-day is the one found in XNU.


"Apple is aware of a report that this issue may have been actively exploited," Apple said when describing the three zero-day vulnerabilities.


The complete list of impacted devices includes:


* iPhone 5s, iPhone 6, iPhone 6 Plus, iPad Air, iPad mini 2, iPad mini 3, and iPod touch (6th generation) running iOS 12.5.5
* and Macs with Security Update 2021-006 Catalina.




> 
> 0day privilege escalation for macOS Catalina discovered in the wild by [@eryeh](https://twitter.com/eryeh?ref_src=twsrc%5Etfw) <https://t.co/yvCWPo45fL>  
>   
> 
> We saw this used in conjunction with a N-day remote code execution targeting webkit.  
>   
> 
> Thanks to Apple for getting patch out so quickly.
> 
> 
> — Shane Huntley (@ShaneHuntley) [September 23, 2021](https://twitter.com/ShaneHuntley/status/1441102086385455112?ref_src=twsrc%5Etfw)




Long stream of zero-days exploited in the wild
----------------------------------------------


Besides today's three zero-days, Apple had to deal with what looks like an unending stream of zero-day bugs used in attacks targeting iOS and macOS devices:


* [two zero-days earlier this month](https://www.bleepingcomputer.com/news/apple/apple-fixes-ios-zero-day-used-to-deploy-nso-iphone-spyware/), one of them used also used to install Pegasus spyware on iPhones,
* the [FORCEDENTRY exploit](https://www.bleepingcomputer.com/news/apple/new-zero-click-iphone-exploit-used-to-deploy-nso-spyware/) disclosed in August (previously tracked by Amnesty Tech as Megalodon),
* [three iOS zero-days](https://support.apple.com/en-us/HT212146) (CVE-2021-1870, CVE-2021-1871, CVE-2021-1872) in February, exploited in the wild and reported by anonymous researchers,
* an [iOS zero-day](https://www.bleepingcomputer.com/news/security/apple-fixes-a-ios-zero-day-vulnerability-actively-used-in-attacks/) (CVE-2021-1879) in March that may have also been actively exploited,
* one zero-day [in iOS (CVE-2021-30661) and one in macOS (CVE-2021-30657)](https://www.bleepingcomputer.com/news/security/apple-fixes-macos-zero-day-bug-exploited-by-shlayer-malware/) in April, exploited by Shlayer malware,
* [three other iOS zero-days](https://www.bleepingcomputer.com/news/apple/apple-fixes-2-ios-zero-day-vulnerabilities-actively-used-in-attacks/) (CVE-2021-30663, CVE-2021-30665, and CVE-2021-30666) in May, bugs allowing for arbitrary remote code execution (RCE) simply by visiting malicious websites,
* [a macOS zero-day (CVE-2021-30713)](https://www.bleepingcomputer.com/news/security/apple-fixes-three-zero-days-one-abused-by-xcsset-macos-malware/) in May, which was abused by the XCSSET malware to bypass Apple's TCC privacy protection,
* [two iOS zero-day bugs (CVE-2021-30761 and CVE-2021-30762)](https://www.bleepingcomputer.com/news/security/apple-fixes-ninth-zero-day-bug-exploited-in-the-wild-this-year/) in June that "may have been actively exploited" to hack into older iPhone, iPad, and iPod devices.




#### Tags:
[[zero-day]] [[macOS]] [[zero-days]] [[(in]] [[iPhone]] [[iPad]] [[Bleeping Computer]]
