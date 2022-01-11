# MacOS Bug Could Let Creeps Snoop On You
### The flaw could allow attackers to bypass Privacy preferences, giving  apps with no right to access files, microphones or cameras the ability to  record you or grab screenshots.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177551
+ Date: 2022-01-11T20:35:47+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/11152615/spying-ga59576ef6_1280-e1641932787367.jpeg)

Microsoft on Monday released details about a bug in macOS that Apple fixed last month – named “powerdir” – that could let attackers hijack apps, install their own nasty apps, use the microphone to eavesdrop or grab screenshots of whatever’s displayed on your screen.


The vulnerability allows malicious apps to bypass Privacy preferences. Specifically, it could allow an attacker to bypass the operating system’s [Transparency, Consent, and Control](https://support.apple.com/guide/security/controlling-app-access-to-files-secddd1d86a6/web) (TCC) technology, thereby gaining unauthorized access to a user’s protected data, the Microsoft 365 Defender Research Team said in its [advisory](https://www.microsoft.com/security/blog/2022/01/10/new-macos-vulnerability-powerdir-could-lead-to-unauthorized-user-data-access/).


Introduced in 2012 in macOS Mountain Lion, TCC helps users to configure their apps’ privacy settings by requiring that all apps get user consent before accessing files in Documents, Downloads, Desktop, iCloud Drive, calendar and network volumes, as well as before the apps are allowed to access the device’s camera, microphone or location.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Apple released a fix for the vulnerability – identified as [CVE-2021-30970](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30970) – in macOS Big Sur and macOS Monterey, as [part of](https://threatpost.com/apple-ios-updates-iphone-13-jailbreak-exploit/177051/) its Dec. 13, 2021 [security updates](https://support.apple.com/en-us/HT212978). At the time, as is typical, Apple didn’t give much detail, merely stating that the flaw was a logic issue that could allow a malicious to bypass Privacy preferences: a flaw that it addressed with improved state management.


The Bug Trips Up TCC
--------------------


TCC stores the consent history of app requests. The feature prevents unauthorized code execution by restricting full disk access to only those apps with full disk access – at least, that’s the way it’s supposed to work.


But Microsoft researchers discovered that it’s possible to programmatically change a target user’s home directory and to plant a fake TCC database, which stores the consent history of app requests.


“If exploited on unpatched systems, this vulnerability could allow a malicious actor to potentially orchestrate an attack based on the user’s protected personal data,” they explained in Monday’s advisory. “For example, the attacker could hijack an app installed on the device – or install their own malicious app – and access the microphone to record private conversations or capture screenshots of sensitive information displayed on the user’s screen.”


Typically, users manage TCC under System Preferences in macOS (System Preferences > Security & Privacy > Privacy).


As Microsoft explained, when an app requests access to protected user data, one of two things can happen:


1. If the app and the type of request have a record in the TCC databases, then a flag in the database entry dictates whether to allow or deny the request … automatically and without any user interaction.
2. If the app and the type of request do not have a record in the TCC databases, then a prompt is presented to the user, who decides whether to grant or deny access. The said decision is backed into the databases so that succeeding similar requests will now fall under the first scenario.


If an attacker gets full disk access to the TCC databases, Microsoft explained that the world’s then their app oyster: “They could edit it to grant arbitrary permissions to any app they choose, including their own malicious app. The affected user would also not be prompted to allow or deny the said permissions, thus allowing the app to run with configurations they may not have known or consented to.”


Prior TCC Trespasses
--------------------


This isn’t the first time that TCC databases have shown themselves to be susceptible to bypass. Microsoft listed this trio of past vulnerabilities:


* **Time Machine mounts** ([CVE-2020-9771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9771)): macOS offers a built-in backup and restore solution called [Time Machine](https://support.apple.com/en-us/HT201250). It was discovered that Time Machine backups could be mounted (using the *apfs\_mount* utility) with the “*noowners*” flag. Since these backups contain the *TCC.db* files, an attacker could mount those backups and determine the device’s TCC policy without having full disk access.
* **Environment variable poisoning** ([CVE-2020-9934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9934)): It was discovered that the user’s *tccd* could build the path to the *TCC.db* file by expanding *$HOME/Library/Application Support/com.apple.TCC/TCC.db*. Since the user could manipulate the *$HOME* environment variable (as introduced to *tccd* by *launchd*), an attacker could plant a chosen *TCC.db* file in an arbitrary path, poison the *$HOME* environment variable, and make *TCC.db* consume that file instead.
* **Bundle conclusion issue** ([CVE-2021-30713](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30713)): [First disclosed by Jamf](https://www.jamf.com/blog/zero-day-tcc-bypass-discovered-in-xcsset-malware/) in a blog post about the XCSSET malware family, this bug abused how macOS was deducing app bundle information. For example, suppose an attacker knows of a specific app that commonly has microphone access. In that case, they could plant their application code in the target app’s bundle and “inherit” its TCC capabilities.


Apple has responded to those vulnerabilities with two changes: It protected the system-wide *TCC.db* via [System Integrity Protection](https://developer.apple.com/documentation/security/disabling_and_enabling_system_integrity_protection) (SIP), a macOS feature that prevents unauthorized code execution, and it enforced a TCC policy that only apps with full disk access can access the *TCC.db* files.


“Note, though, that this policy was also subsequently abused as some apps required such access to function properly (for example, the SSH daemon, [sshd](https://man7.org/linux/man-pages/man8/sshd.8.html)),” Microsoft researchers noted.


Apple has since patched these vulnerabilities, but Microsoft said that its research shows that “the potential bypass to *TCC.db* can still occur.”


Microsoft’s very predictable, inarguable advice: “We encourage macOS users to apply these security updates as soon as possible.”


*Image courtesy of [Pixabay](https://pixabay.com/photos/spying-eyes-strange-weird-4250251/).*


**Password** **Reset:** **[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):** Fortify 2022 with a password security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the *new* password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken. **[Register & Stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)** – sponsored by Specops Software.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=CALENDAR]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=XCSSET]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Tcc]] [[Microsoft]] [[Macos]] [[Apps]] [[Tcc.db]] [[ThreatPost]]
#### CVE's
[[CVE-2021-30970]] [[CVE-2020-9771]] [[CVE-2020-9934]] [[CVE-2021-30713]]

