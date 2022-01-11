# Microsoft: This macOS bug could bypass controls and access private user data | ZDNet
### A Microsoft researcher found a new way to bypass Apple's macOS system for protecting app access to user data.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/microsoft-this-macos-bug-could-bypass-controls-and-access-private-user-data/
+ Date: 2022-01-11 15:24:00
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/c3965a5c519ab39c06baf67724d35f4e52a5263f/2021/12/15/b6821fa2-f1a5-4e6d-a839-63172b59646d/shutterstock-1122656969.jpg?width=770&height=578&fit=crop&auto=webp)

Microsoft has detailed how malware on macOS can bypass privacy preferences enforced by Apple's macOS system called Transparency, Consent, and Control (TCC) for controlling apps' access to sensitive user data. 

The 'powerdir' bug, which [Apple fixed in its December 13 update for macOS](https://support.apple.com/en-us/HT212978) up to Monterey, lets an attacker bypass TCC to gain access to a user's protected data. 


The bug was discovered by Microsoft security researcher Jonathan Bar Or. Microsoft is interested in macOS security because Defender for Endpoint can be used in an enterprise to protect non-Windows devices.

Microsoft's 365 Defender Research Team [noted in a blog post](https://www.microsoft.com/security/blog/2022/01/10/new-macos-vulnerability-powerdir-could-lead-to-unauthorized-user-data-access/) that Apple introduced a feature to protect TCC that "prevents unauthorized code execution and enforced a policy that restricts access to TCC to only apps with full disk access."

However, Or discovered that it is "possible to programmatically change a target user's home directory and plant a fake TCC database, which stores the consent history of app requests."

"If exploited on unpatched systems, this vulnerability could allow a malicious actor to potentially orchestrate an attack based on the user's protected personal data," Microsoft said. 

An attacker could hijack an already installed app or install their own malicious app to access the microphone to record private conversations or capture screenshots of sensitive information displayed on the user's screen, Microsoft explained. 






TCC appeared in 2012 in OS X Mountain Lion and is behind the system notifications users see when giving or denying 'consent' for specific applications to access private data, which includes access to the device's camera, microphone, location, and access to the user's calendar or iCloud account. 

Apple doesn't detail TCC directly in its security manual, however, [via security firm Sentinal One](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/), TCC's purpose is [described in a section](https://manuals.info.apple.com/MANUALS/1000/MA1902/en_US/apple-platform-security-guide.pdf) of the manual detailing how macOS and iOS protect app access to user data. Users can manage these privacy protections in macOS within the Security & Privacy section of System Preferences.

"Apple devices help prevent apps from accessing a user's personal information without permission using various technologies including Data Vault. In Settings in iOS and iPadOS, or System Preferences in macOS, users can see which apps they have permitted to access certain information as well as grant or revoke any future access," Apple explains. 

Microsoft's TCC bypass flaw offers a new way to bypass protections Apple has added to previously discovered TCC bypasses, including [CVE-2020-9771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9771), [CVE-2020-9934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9934), and [CVE-2021-30713](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30713). 

To protect TCC from these bypass flaws, Apple introduced a feature that prevents unauthorized code execution and enforced a policy that restricts access to TCC to only apps with full disk access. Those fixes protected TCC.db (database) files from being incorrectly accessed through, for example. Time Machine backups or alternative file paths.  

Microsoft bypass Apple's TCC protections worked by planting a fake TCC.db file and changing the Home directory using a specific 'superuser' sudo command in the Directory Services command-line utility.

"While requiring root access, we discovered that this works only if the app is granted with the TCC policy kTCCServiceSystemPolicySysAdminFiles, which the local or user-specific TCC.db maintains," explains Microsoft.  

"That is weaker than having full disk access, but we managed to bypass that restriction with the [dsexport](https://www.unix.com/man-page/osx/1/dsexport/) and [dsimport](https://www.unix.com/man-page/osx/1/dsimport/) utilities."

Microsoft's proof of concept demonstrated that attackers could change the settings on any application, potentially allowing them to enable microphone and camera access on any app — hence the bug's name "Powerdir". 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=CALENDAR]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Peru]] [[victim.continent.name=South America]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Tcc]] [[Microsoft]] [[Macos]] [[Apps]] [[Tcc.db]] [[ZDNet]]
#### CVE's
[[CVE-2020-9771]] [[CVE-2020-9934]] [[CVE-2021-30713]]

