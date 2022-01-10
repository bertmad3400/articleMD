# Microsoft: powerdir bug gives access to protected macOS user data
### Microsoft says threat actors could use a macOS vulnerability to bypass Transparency, Consent, and Control (TCC) technology to access users' protected data.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-powerdir-bug-gives-access-to-protected-macos-user-data/
+ Date: 2022-01-10T12:39:58-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/09/05/Microsoft.jpg)

![Microsoft: powerdir bug](https://www.bleepstatic.com/content/hl-images/2021/09/05/Microsoft.jpg)


Microsoft says threat actors could use a macOS vulnerability to bypass Transparency, Consent, and Control (TCC) technology to access users' protected data.


The Microsoft 365 Defender Research Team has reported the vulnerability dubbed **powerdir** (tracked as [CVE-2021-30970](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30970)) to Apple on July 15, 2021, via the Microsoft Security Vulnerability Research (MSVR).


TCC is security tech designed to block apps from accessing sensitive user data by allowing macOS users to configure privacy settings for the apps installed on their systems and devices connected to their Macs, including cameras and microphones.


While Apple has restricted TCC access only to apps with full disk access and set up features to automatically block unauthorized code execution, Microsoft security researchers found that attackers could plant a second, specially crafted TCC database that would allow them to access protected user info.


"We discovered that it is possible to programmatically change a target user’s home directory and plant a fake TCC database, which stores the consent history of app requests," [said](https://www.microsoft.com/security/blog/2022/01/10/new-macos-vulnerability-powerdir-could-lead-to-unauthorized-user-data-access/) Jonathan Bar Or, a principal security researcher at Microsoft.


"If exploited on unpatched systems, this vulnerability could allow a malicious actor to potentially orchestrate an attack based on the user’s protected personal data.


"For example, the attacker could hijack an app installed on the device—or install their own malicious app—and access the microphone to record private conversations or capture screenshots of sensitive information displayed on the user’s screen."


Apple has also patched other TCC bypasses reported since 2020, including:


* ***Time Machine mounts** ([CVE-2020-9771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9771)): macOS offers a built-in backup and restore solution called [Time Machine](https://support.apple.com/en-us/HT201250). It was discovered that Time Machine backups could be mounted (using the apfs\_mount utility) with the “noowners” flag. Since these backups contain the TCC.db files, an attacker could mount those backups and determine the device’s TCC policy without having full disk access.*
* ***Environment variable poisoning** ([CVE-2020-9934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9934)): It was discovered that the user’s tccd could build the path to the TCC.db file by expanding $HOME/Library/Application Support/com.apple.TCC/TCC.db. Since the user could manipulate the $HOME environment variable (as introduced to tccd by launchd), an attacker could plant a chosen TCC.db file in an arbitrary path, poison the $HOME environment variable, and make TCC.db consume that file instead.*
* ***Bundle conclusion issue** ([CVE-2021-30713](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30713)): [First disclosed by Jamf](https://www.jamf.com/blog/zero-day-tcc-bypass-discovered-in-xcsset-malware/) in a blog post about the XCSSET malware family, this bug abused how macOS was deducing app bundle information. For example, suppose an attacker knows of a specific app that commonly has microphone access. In that case, they could plant their application code in the target app’s bundle and “inherit” its TCC capabilities.*


![powerdir PoC exploit](https://www.bleepstatic.com/images/news/u/1109292/2022/powerdir_poc.png)*powerdir PoC exploit (Microsoft)*
Apple has fixed the vulnerability in security updates released last month, on December 13, 2021. "A malicious application may be able to bypass Privacy preferences," the company explained in the [security advisory](https://support.apple.com/en-us/HT212978).


Apple addressed the logic issue behind the powerdir security flaw bug with improved state management.


"During this research, we had to update our proof-of-concept (POC) exploit because the initial version no longer worked on the latest macOS version, Monterey," Jonathan Bar Or added.


"This shows that even as macOS or other operating systems and applications become more hardened with each release, software vendors like Apple, security researchers, and the larger security community, need to continuously work together to identify and fix vulnerabilities before attackers can take advantage of them."


Microsoft has previously reported finding a [security flaw dubbed Shrootless](https://www.bleepingcomputer.com/news/security/microsoft-shrootless-bug-lets-hackers-install-macos-rootkits/) that would allow an attacker to bypass System Integrity Protection (SIP) and perform arbitrary operations, elevate privileges to root, and install rootkits on vulnerable devices.


The company's researchers also discovered [new variants of macOS WizardUpdate malware](https://www.bleepingcomputer.com/news/security/microsoft-wizardupdate-mac-malware-adds-new-evasion-tactics/) (aka UpdateAgent or Vigram), updated with new evasion and persistence tactics.


Last year, in June, Redmond revealed [critical firmware bugs in some NETGEAR router models](https://www.bleepingcomputer.com/news/security/microsoft-finds-netgear-router-bugs-enabling-corporate-breaches/) that hackers could use to breach and move laterally within enterprise networks.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=route]] [[action.malware.name=Tor]] [[action.malware.name=XCSSET]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Macos]] [[Tcc]] [[Microsoft]] [[Tcc.db]] [[Powerdir]] [[Apps]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-30970]] [[CVE-2020-9771]] [[CVE-2020-9934]] [[CVE-2021-30713]]

