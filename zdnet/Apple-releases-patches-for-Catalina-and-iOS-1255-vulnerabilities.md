# Apple releases patches for Catalina and iOS 12.5.5 vulnerabilities
### One of the vulnerabilities was discovered by Citizen Lab and another was found by the Google Threat Analysis team.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/apple-releases-patches-for-catalina-and-ios-12-5-5-vulnerabilities/)
+ Date: September 23, 2021
+ Author: Jonathan Greig


## Article:
Unknown

Apple [released](https://support.apple.com/en-us/HT212824) security updates for three vulnerabilities in both macOS Catalina and iOS 12.5.5 that are currently being exploited in the wild. 

[CVE-2021-30869](https://support.apple.com/en-us/HT212825) is an XNU vulnerability found in macOS, iPhone 5s, iPhone 6, iPhone 6 Plus, iPad Air, iPad mini 2, iPad mini 3, and iPod touch that allows malicious applications to execute arbitrary code with kernel privileges.

Apple said there are reports that an exploit for the vulnerability exists and said it was addressed "with improved state handling," noting that it was [discovered](https://twitter.com/ShaneHuntley/status/1441102086385455112) by Google Threat Analysis Group members Erye Hernandez and Clément Lecigne as well as Ian Beer of Google Project Zero.

CVE-2021-30860 was discovered by Citizen Lab and may be [connected](https://www.zdnet.com/article/apple-releases-update-fixing-nso-spyware-vulnerability-affecting-macs-iphones-ipads-and-watches/) to the [NSO Pegasus spyware](https://www.zdnet.com/article/nso-groups-pegasus-spyware-used-against-journalists-political-activists-worldwide-report/) that was used to break into Apple devices. The vulnerability affects iPhone 5s, iPhone 6, iPhone 6 Plus, iPad Air, iPad mini 2, iPad mini 3, and iPod touch (6th generation).

There was significant outrage when Citizen Lab [released](https://citizenlab.ca/2021/09/forcedentry-nso-group-imessage-zero-click-exploit-captured-in-the-wild/) multiple reports this year showing how NSO Pegasus spyware [gave](https://www.zdnet.com/article/fbi-launches-investigation-into-pegasus-spyware-vendor-over-us-intelligence-gathering-hacks/) certain nation-states and criminal actors full access to Apple devices. CVE-2021-30860, as Citizen Lab described in their latest report, relates to how threat actors could use the processing of a maliciously crafted PDF to execute arbitrary code.

Apple admitted in the release that it has been actively exploited and said it was addressed "with improved input validation."

The third vulnerability -- CVE-2021-30858 -- affects the same devices as the first two and was submitted anonymously. Apple explained that the vulnerability relates to how processing maliciously crafted web content can lead to arbitrary code execution. Like the others, Apple said it was aware that it may have been actively exploited. 






Apple said they solved the issue with "improved memory management."





#### Tags:
[[iPhone]] [[iPad]] [[ZDNet]]
