# iPhone WiFi bug morphs into zero-click hacking, but there's a fix
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/apple/iphone-wifi-bug-morphs-into-zero-click-hacking-but-theres-a-fix/)
+ Date: July 19, 2021
+ Author: Ionut Ilascu


## Article:
![iPhones vulnerable to WiFiDemon printf format string bug](https://www.bleepstatic.com/content/hl-images/2019/04/08/wifi-jamming.jpg)


Security researchers investigating a bug that crashed the Wifi service on iPhones found that it could be exploited for remote code execution without user interaction.


When [initially disclosed](https://www.bleepingcomputer.com/news/security/iphone-bug-breaks-wifi-when-you-join-hotspot-with-unusual-name/), the bug could disable an iPhone’s WiFi connection after trying to connect to a network with a name (SSID) that included a special character.


Security researcher Carl Schou found the vulnerability after making his iPhone join a network with the SSID “%p%s%s%s%s%n,” resulting in the device losing its WiFi connection capability:



![iPhone WiFi loop crashing](https://www.bleepstatic.com/images/news/u/1100723/2021/CarlSchouWiFi.jpg)source: [Carl Schou](https://twitter.com/vm_call/status/1405937492642123782)
Different variations of the string led to crashing the WiFi service and sending it into a restart loop. Tests from done by BleepingComputer and security researchers shows that the vulnerability discovered by Schou is exploitable in iOS 14.6 when connecting to a maliciously crafted SSID.


Fixing the bug was as simple as resetting network settings to remove the names of all WiFi networks, including the mischievous one, from the lists of known SSIDs it could join.


### Bug worse than thought


However, researchers at mobile security startup ZecOps found that there is more to this bug than the initially reported WiFi denial-of-service (DoS) condition.


In a blog post last week, the researchers note that the bug can be triggered as a zero-click (no user interaction) and has potential for remote code execution.


ZecOps says that issue is similar to a format-strings bug, where the computer sees the input value as a formatting character, not a character. They dubbed this attack WiFiDemon.


“However, this bug is slightly different from the “traditional” printf format string bugs because it uses [NSString stringWithFormat:] which was implemented by Apple, and Apple removed the support for %n for security reasons,” ZecOps explains.


While trying to find another way to exploit the vulnerability, the researchers used “%@,” which is a format specifier for printing and formatting objects in Objective-C, the programming language for iOS software.



“A potential exploit opportunity is if we can find an object that has been released on the stack, in that case, we can find a spray method to control the content of that memory and then use %@ to treat it as an Objective-C object, like a typical Use-After-Free that could lead to code execution”- [ZecOps](https://blog.zecops.com/research/meet-wifidemon-ios-wifi-rce-0-day-vulnerability-and-a-zero-click-vulnerability-that-was-silently-patched/)



The researchers were successful when simply adding “%@” to the name of a SSID. One scenario that can lead to running code on the target device is to create a malicious WiFi network and wait for the victim to connect.


If the WiFi connection is enabled and the auto-join feature turned on, which is the default state, one scenario is to create a malicious WiFi network and wait for the target to connect.


On earlier iOS versions, even if the victim does not join the malicious network, the WiFi service crashes and restarts in a loop immediately after reading the malcrafted SSID name, the researchers write in their report.


If the bug is exploited locally, it could help an attacker build a partial sandbox so they could jailbreak the device.


ZecOps did not find evidence of WiFiDemon attacks in the wild but believes that some threat actors may have also discovered the bug and might exploit it.


The researchers say that the vulnerability that Schou discovered is exploitable in iOS 14.6 when connecting to a maliciously crafted SSID.


Furthermore, the zero-click part making WiFiDemon dangerous works on iOS 14 through 14.4, since Apple patched the bug silently with the security updates released in January.




#### Tags:
[[WiFi]] [[SSID]] [[ZecOps]] [[Schou]] [[WiFiDemon]] [[Bleeping Computer]]
