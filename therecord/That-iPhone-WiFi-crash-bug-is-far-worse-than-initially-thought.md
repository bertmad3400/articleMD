# That iPhone WiFi crash bug is far worse than initially thought
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/that-iphone-wifi-crash-bug-is-far-worse-than-initially-thought/)
+ Date: July 18, 2021
+ Author: Catalin Cimpanu


## Article:
![That iPhone WiFi crash bug is far worse than initially thought](https://therecord.media/wp-content/uploads/2021/07/WiFi.jpg)

An innocuous iPhone bug that could crash the WiFi service has turned out to be far worse than initially thought after mobile security firm ZecOps showed on Friday how the bug could be abused for remote code execution attacks.


Discovered last month by Danish security researcher [Carl Schou](https://twitter.com/vm_call), the bug could crash any up-to-date iPhone that connected to an access point or WiFi network with a name of **%p%s%s%s%s%n**.





Since WiFi network names are written on disk in certain files, every time the iPhone tried to connect to a WiFi network, iOS would read those files and crash and reboot in a loop.


Initially, the bug was considered a pretty big deal before iOS experts discovered that disabling WiFi and resetting iOS network settings would clear those local files of the problematic network name and allow users to use their WiFi feature again.


**Settings > General > Reset > Reset Network Settings**


At the heart of the problem was the **“%**” character in the WiFi network name, which in Objective-C —the main programming language of iOS— is also used to declare variable names or commands.


In [new research](https://blog.zecops.com/research/meet-wifidemon-ios-wifi-rce-0-day-vulnerability-and-a-zero-click-vulnerability-that-was-silently-patched/) published on Friday, security firm ZecOps said that they found a new string pattern that, when added to WiFi network names, could have far worse consequences than just crashing an iPhone’s WiFi service.


By adding “**%@**” to a network name, ZecOps said that a malicious threat actor could abuse the crash-pattern loop in the WiFi service to execute custom code in what could be described as a [use-after-free vulnerability](https://cwe.mitre.org/data/definitions/416.html).


Since iOS automatically connects users to the closest WiFi network, ZecOps said the bug could be exploited in zero-click scenarios just by creating a malicious WiFi network name and then waiting for nearby users to connect to it when close enough.


### WiFiDemon RCE already fixed in current iOS version


ZecOps said that while the original crash bug discovered last month impacted all iOS 14.x versions, the remote code execution (RCE) variant they found last week only worked for iPhones and iPads running iOS versions from 14.0 and up to 14.4.


The San Francisco-based security firm said the bug was mysteriously [patched in January 2021](https://support.apple.com/en-us/HT212146) with the release of iOS 14.4 but without much fanfare from the Apple security team.


As a result of their findings, ZecOps is now advising iPhone and iPad users to update their devices to the latest iOS version in order to prevent threat actors from exploiting this issue —which they nicknamed **WiFiDemon**— to run malicious code on out-of-date devices.


Older iOS releases prior to iOS 14.x are not vulnerable to WiFiDemon RCE or crash attacks, researchers said.








#### Tags:
[[WiFi]] [[ZecOps]] [[iPhone]] [[WiFiDemon]] [[RCE]] [[The Record]]
