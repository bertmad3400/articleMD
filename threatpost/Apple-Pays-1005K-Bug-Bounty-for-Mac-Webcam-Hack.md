# Apple Pays $100.5K Bug Bounty for Mac Webcam Hack
### The researcher found that he could gain unauthorized camera access via a shared iCloud document that could also hack every website you've ever visited.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178114
+ Date: 2022-01-31T18:18:41+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2020/04/06125323/webcam.jpeg)

A researcher who showed Apple how its webcams can be hijacked via a universal cross-site scripting bug (UXSS) Safari bug has been awarded what is [reportedly](https://appleinsider.com/articles/22/01/25/apple-pays-record-100500-to-student-who-found-mac-webcam-hack) a record $100,500 bug bounty. The bug could be used by an adversary as part of an attack to gain full access to every website ever visited by the victim.


The bug-finder is Ryan Pickren, founder of proof-of-concept sharing platform [BugPoC](https://bugpoc.com/) and a former Amazon Web Services security engineer. This isn’t the first time he’s found bugs that let him hoodwink Apple’s cameras: In 2020, he [discovered](https://threatpost.com/apple-safari-flaws-webcam-access/154476/) vulnerabilities in the Safari browser that could be used to snoop on iPhones, iPads and Mac computers using their microphones and cameras, just by convincing a target to click one malicious link.




This time around, [according to Pickren](https://www.ryanpickren.com/safari-uxss), he found a series of flaws – in Safari 15 and iCloud Sharing – that could again lead to unauthorized camera access, which would again allow an attack to be launched from a malicious site.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


But his more recent find is worse: It could also enable a shared iCloud document to “hack every website you’ve ever visited,” he said, and could steal permissions to use multimedia – in other words, the microphone, camera and screensharing.


Pickren reported that the same hack could result in an attacker gaining full access to a device’s entire filesystem, y exploiting Safari’s webarchive files, which are the files Safari creates as an alternative to HTML when it saves a website locally.


Pickren submitted the bugs to Apple last July. The iPhone-maker patched the issues earlier this month and subsequently awarded the $100,500 [bug bounty](https://threatpost.com/apples-bug-bounty-opens-1m-payout/151334/) to Pickren.


The Bugs
--------


The [issues](https://support.apple.com/en-us/HT212869) are found in ShareBear, a behind-the-scenes iCloud file-sharing app that prompts users when they try to open a shared document for the first time – and only the first time. Since users aren’t presented with the display again once they’ve accepted the prompt to open the file, Pickren found that anyone who has access to the file can alter the file’s content after that occurs.


“ShareBear will then download and update the file on the victim’s machine without any user interaction or notification,” Pickren [explained](https://www.ryanpickren.com/safari-uxss) in his technical write-up. “In essence, the victim has given the attacker permission to plant a polymorphic file onto their machine and the permission to remotely launch it at any moment.”


These three steps are involved in using ShareBear to download and open a webarchive file:


1. Trick the victim into giving permission to plant the polymorphic file;
2. Turn an image file with a .PNG format – he gave the example of puppies.png – into an executable binary (“evil.dmg) after a user has agreed to open it and then to open it;
3. The binary triggers an exploit chain that leverages other flaws discovered in Safari in order to take over the machine’s microphone or webcam, or even to steal local files.


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/31123626/Staging-the-Attack-e1643650600392.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/31123626/Staging-the-Attack-e1643650600392.jpg)[![](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/31123732/Mount-Disk-Image.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/31123732/Mount-Disk-Image.jpg)


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/31123814/Launch-URL-file.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/31123814/Launch-URL-file.jpg)


Stages of ShareBear attack. Source: Ryan Pickren.


Pickren identified four zero-day bugs, the following of which have received CVE tracking numbers:


* **[CVE-2021-30861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30861):** A logic issue in Webkit, rated at 5.5 in criticality, that Apple addressed with improved state management in [macOS Monterey 12.0.1](https://support.apple.com/en-us/HT212869). The bug could allow a malicious application to bypass checks done by [Gatekeeper](https://en.wikipedia.org/wiki/Gatekeeper_(macOS)): a macOS security feature that attempts to reduce the likelihood of inadvertently executing malware by enforcing code signing and verifying downloaded applications before allowing them to run.
* **[CVE-2021-30975](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30975):** An issue in macOS Monterey’s Script Editor with a base criticality score of High – 8.6 – that may allow a malicious [OSAX scripting addition](https://www.oreilly.com/library/view/applescript-the-definitive/0596005571/ch04s07.html) to bypass Gatekeeper checks and circumvent sandbox restrictions. Apple addressed the issue by disabling execution of JavaScript when viewing a scripting dictionary.


“This project was an interesting exploration of how a design flaw in one application can enable a variety of other, unrelated, bugs to become more dangerous,” Pickren concluded. “It was also a great example of how even with macOS Gatekeeper enabled, an attacker can still achieve a lot of mischief by tricking approved apps into doing malicious things.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Accomodation]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Pickren]] [[Macos]] [[Website]] [[Icloud]] [[Sharebear]] [[ThreatPost]]
#### CVE's
[[CVE-2021-30861]] [[CVE-2021-30975]]

