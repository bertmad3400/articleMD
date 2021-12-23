# Apple fixes macOS security flaw behind Gatekeeper bypass
### Apple has addressed a macOS vulnerability that unsigned and unnotarized script-based apps could exploit to bypass all macOS security protection mechanisms even on fully patched systems.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/apple/apple-fixes-macos-security-flaw-behind-gatekeeper-bypass/
+ Date: 2021-12-23T17:09:32-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/02/10/Apple_red.jpg)

![Apple fixes macOS security flaw behind Gatekeeper bypass](https://www.bleepstatic.com/content/hl-images/2021/02/10/Apple_red.jpg)


Apple has addressed a macOS vulnerability that unsigned and unnotarized script-based apps could exploit to bypass all macOS security protection mechanisms even on fully patched systems.


If they circumvent [automated notarization security checks](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution) (which scans for malicious components and code-signing issues), the applications are allowed to launch by [Gatekeeper](https://support.apple.com/en-us/HT202491), a macOS security feature designed to verify if downloaded apps are notarized and developer-signed.


Once malicious script-based apps targeting the bypass flaw ([CVE-2021-30853](https://support.apple.com/en-mt/HT212804)) are launched on a target's system, they can be used by attackers to download and deploy second-stage malicious payloads.


Apple has addressed this vulnerability in [macOS 11.6](https://support.apple.com/en-mt/HT212804) through a security update released in September 2021 that adds improved checks.


Gatekeeper bypass with a shebang
--------------------------------


The CVE-2021-30853 Gatekeeper bypass bug was discovered and reported to Apple by Box Offensive Security Engineer [Gordon Long](https://twitter.com/ethicalhax).


He found that specially-crafted script-based applications downloaded from the Internet would launch without showing an alert even though automatically quarantined.


The "specially-crafted" part requires creating an app that uses a script starting with a shebang (!#) character but leaving the rest of the line empty, which tells the Unix shell to run the script without specifying a shell command interpreter.


This leads to a Gatekeeper bypass because the syspolicyd daemon automatically commonly invoked by the AppleSystemPolicy kernel extension to perform security checks (signing and notarization) no longer gets triggered for inspection when launching a script without specifying an interpreter.


Basically, if the script used a shebang (!#) but did not explicitly specify an interpreter, it would bypass Gatekeeper security checks.



[![Objective-See CVE-2021-30853 tweet](https://www.bleepstatic.com/images/news/u/1109292/2021/CVE-2021-30853_tweet.png)](https://twitter.com/objective_see/status/1473744130681425920)



"The syspolicyd daemon will perform various policy checks and ultimately prevent the execution of untrusted applications, such as those that are unsigned or unnotarized," [explained](https://objective-see.com/blog/blog_0x6A.html) security researcher Patrick Wardle.


"But, what if the AppleSystemPolicy kext decides that the syspolicyd daemon does not need to be invoked? Well then, the process is allowed! And if this decision is made incorrectly, well then, you have a lovely File Quarantine, Gatekeeper, and notarization bypass."


As revealed by Wardle, threat actors can exploit this flaw by tricking their targets into opening a malicious app that can also be camouflaged as a benign-looking PDF document.


Such malicious payloads can be delivered on targets' systems via many methods, including poisoned search results, fake updates, and trojaned applications downloaded from sites linking to pirated software.



![macOS infection vectors](https://www.bleepstatic.com/images/news/u/1109292/2021/macOS_infection_vectors.png)*Image: Patrick Wardle*
Similar bugs exploited by malware
---------------------------------


This is not the first macOS bug fixed by Apple that would enable threat actors to completely circumvent OS security mechanisms such as Gatekeeper and File Quarantine on fully patched Macs.


In April, Apple patched a [zero-day vulnerability exploited in the wild by Shlayer malware operators](https://www.bleepingcomputer.com/news/security/apple-fixes-macos-zero-day-bug-exploited-by-shlayer-malware/) to bypass macOS automated security checks and deploy additional payloads on compromised Macs.


The Shlayer threat actors began targeting macOS users with unsigned and unnotarized malware that exploited the zero-day bug (tracked as [CVE-2021-30657](https://support.apple.com/en-us/HT212325)) starting with January 2021, as the [Jamf Protect detection team](https://www.jamf.com/blog/shlayer-malware-abusing-gatekeeper-bypass-on-macos/) discovered.


[Microsoft also discovered a macOS vulnerability](https://www.bleepingcomputer.com/news/security/microsoft-shrootless-bug-lets-hackers-install-macos-rootkits/) in October, dubbed Shrootless and tracked as [CVE-2021-30892](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30892)), that could be used to bypass System Integrity Protection (SIP) and perform arbitrary operations, elevate privileges to root, and install rootkits on compromised devices.


"A malicious application may be able to modify protected parts of the file system," Apple said in a [security advisory](http://support.apple.com/en-us/HT212872) issued after patching the Shrootless bug.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Macos]] [[Unnotarized]] [[Script-based]] [[Apps]] [[Syspolicyd]] [[Wardle]] [[Malware]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-30853]] [[CVE-2021-30657]] [[CVE-2021-30892]]

