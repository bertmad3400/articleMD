# Apple Issues Urgent iPhone Updates; None for Pegasus Zero-Day
### Update now: The ream of bugs includes some remotely exploitable code execution flaws. Still to come: a fix for what makes iPhones easy prey for Pegasus spyware. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168040)
+ Date: July 22, 2021  12:18 pm
+ Author: Lisa Vaas


## Article:
iPhone users, drop what you’re doing and update now: Apple has issued a warning about a ream of code-execution vulnerabilities – some of which are remotely exploitable – and experts are emphatically recommending an ASAP update to version 14.7 of iOS and iPadOS.


Unfortunately, you aren’t getting a fix for the flaw that makes your iPhones easy prey for Pegasus spyware. As headlines have focused on all week, a zero-click zero-day in Apple’s iMessage feature is being [exploited by NSO Group’s](https://threatpost.com/nso-group-data-pegasus/167897/) notorious Pegasus mobile spyware: A spyware blitz enabled by a bug that has [given the security community pause](https://threatpost.com/nso-pegasus-spyware-bans-apple-accountability/167965/) about the security of Apple’s closed ecosystem.


The patches address a total of 40 vulnerabilities, 37 of which are in iPhones. The most severe of the flaws could allow for arbitrary code execution with kernel or root privileges. See below for a full list of the vulnerabilities and their details.



Besides fixing other, non-Pegasus-associated vulnerabilities in iOS and iPadOS, Wednesday’s [security updates](https://support.apple.com/en-us/HT201222) also squashed bugs in macOS Big Sur 11.5 and in macOS Catalina.


Fortunately, as of now, there are no reports of these vulnerabilities being exploited in the wild. But as noted by MS-ISAC, the Multi-State Information Sharing and Analysis Center, the risk to large and medium-sized government and business entities is rated high. The flaws are rated medium-risk for small business or government entities, while the risk to home users is considered low.


WebKit: The Little Engine That Could…Blow Up
--------------------------------------------


With regards to the security updates in iOS 14.7 and iPad 14.7, four of them are in WebKit, the engine that powers Apple’s Safari browser. All four could lead to arbitrary code execution. Exploitation would require a user to download maliciously crafted web content.


The vulnerabilities – CVE-2021-30758, CVE-2021-30795, CVE-2027-30797 and CVE-2021-30799 – are due to type confusion, use-after-free and memory-corruption issues in WebKit.


IOS 14.7 also fixes a known issue – CVE-2021-30800 – where joining a malicious Wi-Fi network may result in a denial of service or arbitrary code execution.


A Basket of 40 Bad (But Now Fixed) Apples
-----------------------------------------


Below are details of all 40 vulnerabilities in Apple macOS/iOS:


Update Now
----------


On Wednesday, MS-ISAC urged Apple users to apply appropriate patches to vulnerable systems “immediately after appropriate testing.”


It’s easy: Go to Settings > General > Software Update and follow the prompts.


In an advisory email, MS-ISAC offered these recommendations:


Apple released the iOS 14.7 update on Monday, but the company kept the crucial, now-released list of security-fix details that typically come with iOS upgrades close to the vest. As is its wont, the company held back details in order to protect customers, giving them a chance to update before hanging out dirty laundry for attackers to grab.


Meanwhile, the update for iPadOS is now out: iPadOS 14.7 was released along with the security details yesterday, on Wednesday.


Time to Examine iPhone’s Reputation for Security
------------------------------------------------


Oliver Tavakoli, CTO at the AI cybersecurity company Vectra, noted that Apple’s marketing on security and privacy – “which is backed up by actions they have actually taken” – has resulted in adoption of iPhones by activists, politicians and journalists “at a rate which substantially exceeds adoption within the public at large.”


Is the same true for terrorists and criminals – NSO Group’s purported targets? It’s “up for debate,” Tavakoli told Threatpost on Thursday. Regardless, the proliferation of iPhones by those belonging to groups historically targeted with spyware force us to shine a spotlight on the question of whether Apple’s security can bear the weight of protecting those people.


“Given that NSO’s customers want the ability to monitor Apple devices, it’s pretty clear that NSO is expending substantial effort on exploits for the iOS platform,” he said.


Not to be too hard on Apple: Software will always have flaws, particularly with ever more functionality added to a platform. But Tavakoli feels that “zero-click exploits that can be carried out by perfect strangers (rather than someone on your contact list who has previously been compromised)” are “in a class by themselves.”


Apple shouldn’t just patch the iMessage vulnerability “with a sense of urgency,” he said. The company “should also provide mechanisms which reduce the attack surface available to people not on your contact list.”


Dirk Schrader with New Net Technologies agreed: “No device, and no operating system, is 100 percent error-free,” he observed to Threatpost on Thursday. Case in point is the latest Wi-Fi bug for iPhones: That type of bug that can fetch top dollar on exploit markets, most particularly for iOS vulnerabilities.


“Especially for companies alike to NSO, it is vital to keep a list of exploitable bugs, and the grey market for these bugs is huge, with amounts north of $1 million paid for exploitable bugs identified in iOS,” Schrader said.


Bug-bounty programs can help, but they won’t shut down that grey market and its huge payouts, he continued. That makes fixing the iMessage bug crucial: “Fixing these bugs is not easy,” Schrader noted. “NSO will certainly not reveal the details, providing a responsible disclosure about one of its key revenue generating assets. In order to reinstate that claim of being the most secure device, it will be crucial for Apple to find and fix the bug as fast as possible and to report the details about.”


Sean Wright, principal application security engineer at Immersive Labs, called the iMessage flaw “unexpected,” given Apple’s reputation for security. The company is aware of it being used by Pegasus spyware, although Apple has said that there’s only limited danger to individuals. But that doesn’t mean that, as with any vulnerability, it won’t lead to a wider likelihood of risk.


“The concern is that it shines a light on the application and criminal elements discover how to exploit it at greater scale,” Wright told Threatpost. “This puts the onus on Apple to patch as soon as possible.


“Some have also criticized what they perceive to be a lack of transparency from the company on the problem,” Wright continued. “With devices such as this being central to the lives of so many, those who set the tone for the technology sector are typically held to high standards so people can take action and effectively protect themselves.”


072221 12:51 UPDATE: Added comments from Sean Wright.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[7]] [[NSO]] [[iPhones]] [[spyware]] [[iPadOS]] [[iMessage]] [[Threatpost]] [[macOS]] [[MS-ISAC]] [[WebKit]] [[ThreatPost]]
