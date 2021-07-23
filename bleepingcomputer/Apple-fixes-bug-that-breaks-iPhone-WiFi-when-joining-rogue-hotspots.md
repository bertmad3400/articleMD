# Apple fixes bug that breaks iPhone WiFi when joining rogue hotspots
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/apple-fixes-bug-that-breaks-iphone-wifi-when-joining-rogue-hotspots/)
+ Date: July 23, 2021
+ Author: Sergiu Gatlan


## Article:
![Apple fixes bug that breaks iPhone WiFi when joining rogue hotspots](https://www.bleepstatic.com/content/hl-images/2021/06/15/Apple-iPhone-headpic.jpg)


Apple has rolled out security updates to address dozens of iOS and macOS vulnerabilities, including a severe iOS bug dubbed WiFiDemon that could lead to denial of service or arbitrary code execution.


The vulnerability, tracked as **CVE-2021-30800**and a zero-day bug when security researcher Carl Schou [publicly disclosed it](https://twitter.com/vm_call/status/1405937492642123782), was fixed by Apple with the release of iOS 14.7 earlier this week.


Successful exploitation would make it possible to [break an iPhone's Wi-Fi functionality](https://www.bleepingcomputer.com/news/security/iphone-bug-breaks-wifi-when-you-join-hotspot-with-unusual-name/) on joining hotspots with SSIDs containing the "%" character (i.e., %p%s%s%s%s%n).


Once triggered on a vulnerable iPhone, iPad, or iPod, the bug would render it unable to establish Wi-Fi connections, even after rebooting or renaming the Wi-Fi hotspot.


Fixing the Wi-Fi breaking issue requires resetting network settings to remove the names of all Wi-Fi networks, including the rogue ones, from the lists of known SSIDs.


Zero-click RCE risks on older iOS versions
------------------------------------------


As ZecOps later found, threat actors could also execute arbitrary code without user interaction when unpatched devices joined a rogue Wi-Fi hotspot with a maliciously crafted SSID containing the "%@" character (i.e., DDDD%x%x%x%@)


Luckily, as mobile security startup ZecOps [revealed](http://on%20iOS%2014.4), the zero-click remote code execution component of WiFiDemon was only present starting with iOS 14.0 and was silently addressed by Apple with the release of iOS 14.4.


Attackers could exploit this bug by planting malicious Wi-Fi hotspots in popular and highly circulated areas to attack iPhone devices configured to auto-join new Wi-Fi networks.


If you don't want to or cannot immediately update your iOS device to iOS 14.7 to secure it from WiFiDemon attacks, you are advised to disable the Wi-Fi Auto-Join feature by choosing '*Never*' on the *Settings> Wi-Fi>Auto-Join Hotspot* option.


The bug impacts iPhone 6s and later, all iPad Pro models, iPad Air 2 and later, iPad 5th generation and later, iPad mini 4 and later, and iPod touch (7th generation), as Apple revealed in a [security advisory](https://support.apple.com/en-us/HT212601) published earlier this week.



![iPhone unable to join Wi-Fi networks](https://www.bleepstatic.com/images/news/u/1109292/2021/iOS-bad-SSID.webp)*Wi-Fi functionality disabled after joining a "%p%s%s%s%s%n" SSID*
Apple patches stream of zero-days
---------------------------------


Since March, Apple has been busy released security updates to address a seemingly endless wave of zero-day bugs—nine of them in total—most of them also exploited in the wild.


Last month, the company [fixed two iOS zero-day bugs (CVE-2021-30761 and CVE-2021-30762)](https://www.bleepingcomputer.com/news/security/apple-fixes-ninth-zero-day-bug-exploited-in-the-wild-this-year/) that "may have been actively exploited" to hack into older iPhone, iPad, and iPod devices.


Apple [patched a macOS zero-day (CVE-2021-30713)](https://www.bleepingcomputer.com/news/security/apple-fixes-three-zero-days-one-abused-by-xcsset-macos-malware/) in May, a vulnerability abused by the XCSSET malware to bypass Apple's TCC protections designed to safeguard users' privacy.


The same month, Apple also fixed [three other zero-days](https://www.bleepingcomputer.com/news/apple/apple-fixes-2-ios-zero-day-vulnerabilities-actively-used-in-attacks/) (CVE-2021-30663, CVE-2021-30665, and CVE-2021-30666), bugs allowing for arbitrary remote code execution (RCE) on vulnerable devices simply by visiting malicious websites.


The company addressed one more [iOS zero-day](https://www.bleepingcomputer.com/news/security/apple-fixes-a-ios-zero-day-vulnerability-actively-used-in-attacks/) (CVE-2021-1879) in March and zero-days [in iOS (CVE-2021-30661) and macOS (CVE-2021-30657)](https://www.bleepingcomputer.com/news/security/apple-fixes-macos-zero-day-bug-exploited-by-shlayer-malware/) in April.


The Shlayer macOS malware [exploited the latter](https://www.bleepingcomputer.com/news/security/apple-fixes-macos-zero-day-bug-exploited-by-shlayer-malware/) to bypass Apple's File Quarantine, Gatekeeper, and Notarization security checks and deliver second-stage malicious payloads on compromised Macs.




#### Tags:
[[Wi-Fi]] [[iPad]] [[zero-day]] [[iPhone]] [[macOS]] [[WiFiDemon]] [[iPod]] [[zero-days]] [[Bleeping Computer]]
