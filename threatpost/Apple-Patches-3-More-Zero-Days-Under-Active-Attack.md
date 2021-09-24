# Apple Patches 3 More Zero-Days Under Active Attack
### One of the bugs, which affects macOS as well as older versions of iPhones, could allow an attacker to execute arbitrary code with kernel privileges.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174988)
+ Date: September 24, 2021  7:29 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/11/06090222/apple-ios-vulnerability-bug.jpg)
Apple has patched three actively exploited zero-day security vulnerabilities in updates to iOS and macOS, one of which can allow an attacker to execute arbitrary code with kernel privileges.


Apple released two updates on Thursday: iOS 12.5.5, which patches three zero-days that affect older versions of iPhone and iPod devices, and Security Update 2021-006 Catalina for macOS Catalina, which patches one of same vulnerabilities, CVE-2021-30869, that also affects macOS.


The XNU kernel vulnerability — the discovery of which was attributed to Google researchers Erye Hernandez and Clemente Lecigne of Google Threat Analysis Group and Ian Beer of Google Project Zero — is a type-confusion issue that Apple addressed with “improved state handling,” according to [its advisory](https://support.apple.com/en-us/HT212825).


“A malicious application may be able to execute arbitrary code with kernel privileges,” the company said. “Apple is aware of reports that an exploit for this issue exists in the wild.”


The flaw also affects the WebKit browser engine, which is likely why [it caught the attention](https://twitter.com/ShaneHuntley/status/1441102086385455112?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1441102086385455112%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.theregister.com%2F2021%2F09%2F24%2Fapple_zero_day%2F) of the Google researchers. The issue affects macOS Catalina as well as iPhone 5s, iPhone 6, iPhone 6 Plus, iPad Air, iPad mini 2, iPad mini 3, and iPod touch (6th generation).


**Pegasus Zero-Day Patched for Older Devices**
----------------------------------------------


Another zero-day flaw patched in the iOS update also affects WebKit on the same older iOS devices. The issue tracked as CVE-2021-30858 is described by Apple as a use-after-free issue that the company addressed with improved memory management. It allows an attacker to process maliciously crafted web content that may lead to arbitrary code execution, according [to Apple’s advisory](https://support.apple.com/en-us/HT212824).


“Apple is aware of a report that this issue may have been actively exploited,” the company said.


A third bug patched in the iOS update — a zero-click exploit discovered by Citizen Lab — already [made headlines](https://threatpost.com/apple-emergency-fix-nso-zero-click-zero-day/169416/) earlier this month when Apple issued a series of emergency patches on Sept. 13 for it to cover the latest devices running iOS and macOS.


The vulnerability allows for an attacker to process a maliciously crafted PDF that may lead to arbitrary code execution. The fix issued Thursday for the integer-overflow bug “was addressed with improved input validation,” according to Apple, and covers older devices: iPhone 5s, iPhone 6, iPhone 6 Plus, iPad Air, iPad mini 2, iPad mini 3, and iPod touch (6th generation).


Citizen Lab detected the flaw — tracked by Apple as CVE-2021-30860, a flaw in CoreGraphics — targeting iMessaging in August. Researchers dubbed it ForcedEntry and alleged that it had been used to illegally spy on Bahraini activists with [NSO Group’s Pegasus spyware](https://threatpost.com/nso-group-data-pegasus/167897/).


**Keeping Up with 0-Days**
--------------------------


The latest Apple security updates come on the heels of [news earlier this week](https://threatpost.com/unpatched-apple-zero-day-code-execution/174915/) that it quietly slid out an incomplete patch for a zero-day vulnerability in its macOS Finder system — which hasn’t fixed the problem yet. It could allow remote attackers to trick users into running arbitrary commands.


Indeed Apple, like many other vendors, spends a lot of its time trying to keep up with security vulnerabilities—something at which it “does a great job,” noted Hank Schless, senior manager of security solutions at endpoint-to-cloud security firm Lookout.


“Even though Apple has been in the news a number of times over these zero-day vulnerabilities, software developers everywhere run into vulnerabilities in their code,” he observed in an email to Threatpost.


However, these patches are worth nothing and corporate data is at risk if people don’t update their mobile devices in particular, as soon as fixes for actively exploited flaws are available, Schless warned.


“People often ignore them until they’re forced to update,” he said. “This could be risky to an enterprise that allows its employees to access corporate resources from their mobile devices…[which is] just about every enterprise out there.”


***Rule #1 of Linux Security:****No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*


 




#### Tags:
[[iPhone]] [[iPad]] [[Linux]] [[zero-day]] [[Google]] [[iPod]] [[macOS]] [[said.]] [[ThreatPost]]
