# Unpatched Apple Zero-Day in macOS Finder Allows Code Execution
### All a user needs to do is click on an email attachment, and boom — the code is silently executed without the victim knowing. It affects Big Sur and prior versions of macOS.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174915)
+ Date: September 22, 2021  1:22 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/22125219/Big-Sur-e1632329554949.jpg)
A zero-day security vulnerability in Apple’s macOS Finder system could allow remote attackers to trick users into running arbitrary commands, according to researchers – and a silent patch hasn’t fixed it.


For those not in the Apple camp, the macOS Finder is the default file manager and GUI front-end used on all Macintosh operating systems. It’s the first thing users see upon booting, and it governs the launching of other applications and the overall user management of files, disks and network volumes. It’s the overlord application for everything else on the Mac, in other words.


According to an SSD Secure Disclosure advisory this week, the vulnerability exists in the way macOS Finder handles .Inetloc files. Inetloc files are Apple-specific, and function as [shortcuts to internet locations](https://fileinfo.com/extension/inetloc), such as an RSS feed or a telnet location; or they can be used to open documents locally on someone’s Mac within a browser using the “file://” format (in place of http://). It’s the latter function that’s at issue with the zero day, researchers said.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In an exploit scenario for the bug, the .Inetloc files can be specially crafted to contain embedded commands. The crafted files can then be attached to (or linked in) malicious emails, researchers added – and if users are socially engineered into clicking on them, those commands embedded inside automatically execute in stealth mode, with no alert or prompt given to victims.


“A vulnerability in the way macOS processes .Inetloc files causes it to run commands embedded inside, the commands it runs can be local to the macOS allowing the execution of arbitrary commands by the user without any warning/prompts,” according to [the advisory](https://ssd-disclosure.com/ssd-advisory-macos-finder-rce/).


It’s a simple exploitation scenario – as demoed in an SSD video included in the alert.


Independent security researcher Park Minchan reported the vulnerability to SSD, noting that the bug affects macOS Big Sur edition and all those prior it. In response, Apple chose not to issue a CVE, and silently patched the issue – except the fix was botched, researchers said.


“The vendor has notified us that file:// [function] has been silently patched,” the advisory explained. However, researchers added that the bug can still be exploited by using a mangled value, like FiLe:// in the file’s execution routine.


“Newer versions of macOS (from Big Sur) have blocked the file:// prefix…however they did case-matching causing File:// or fIle:// to bypass the check,” they explained.


“We…have not received any response from them since the report has been made,” according to the advisory. “As far as we know, at the moment, the vulnerability has not been patched.”


There’s no word on whether it’s been exploited in the wild, and Apple did not immediately return a request for comment.


The computing giant has had its share of zero days this year. In May, it [patched a critical bug](https://threatpost.com/apple-patches-zero-day-flaw-in-macos-that-allows-for-sneaky-screenshots/166428/) in macOS that could be exploited to take screenshots of someone’s computer and capture images of their activity within applications or on video conferences without that person knowing. In July, [it patched](https://threatpost.com/apple-patches-actively-exploited-zero-day-in-ios-macos/168177/) an actively exploited zero-day flaw in both its iOS and macOS platforms that could allow attackers to take over an affected system. And earlier this month, it [rushed an emergency patch](https://threatpost.com/apple-emergency-fix-nso-zero-click-zero-day/169416/) for the “ForcedEntry” zero-click zero-day, which was being exploited by NSO Group to install spyware.


***Rule #1 of Linux Security:****No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*




#### Tags:
[[macOS]] [[Linux]] [[It’s]] [[.Inetloc]] [[ThreatPost]]
