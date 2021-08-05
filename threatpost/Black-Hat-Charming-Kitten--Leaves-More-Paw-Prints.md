# Black Hat: Charming Kitten  Leaves More Paw Prints
### IBM X-Force detailed the custom-made “LittleLooter” data stealer and 4+ hours of ITG18 operator training videos revealed by an opsec goof. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168394)
+ Date: August 5, 2021  10:16 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/05101414/kitten-e1628172869531.jpeg)
LAS VEGAS – The suspected Iranian threat group that IBM Security X-Force calls ITG18 and which overlaps with the group known as [Charming Kitten](https://threatpost.com/apt-ta453-siphons-intel-mideast/167715/) keeps leaving a trail of paw prints.


The latest: a custom Android backdoor dubbed “LittleLooter” – used exclusively by the threat actor, as far as researchers have been able to determine – that IBM Security X-Force detailed for the first time at Black Hat USA 2021.


On Wednesday, in a [session](https://www.blackhat.com/us-21/briefings/schedule/?fbclid=IwAR3-iLWAf2qsujXq22Jo3i7ORW8iuNXG6hD7SDCKvW2g6_6C-iCtV46TrGE#the-kitten-that-charmed-me-the--lives-of-a-nation-state-attacker-23066) titled “The Kitten that Charmed Me: The 9 Lives of a Nation State Attacker,” X-Force researchers Allison Wikoff and Richard Emerson said you just have to laugh about all the errors the group keeps making. “If that is not amusing, I do not know what is,” Wikoff said. “And God, I love my job with things like this happening.”



LittleLooter
------------


Most recently, “things like this” included X-Force’s discovery of a file named “WhatsApp.apk” (md5: a04c2c3388da643ef67504ef8c6907fb) on infrastructure associated with ITG18 operations.


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/05094452/LittleLooter-e1628171108175.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/05094452/LittleLooter-e1628171108175.jpg)


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/05094822/LittleLooter.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/05094822/LittleLooter.png)


X-Force determined that “WhatsApp.apk” was Android malware that the researchers dubbed “LittleLooter” based on its information-stealing capabilities.


For command-and-control (C2) communication, LittleLooter attempts to establish communication to the C2 server via HTTP POST requests and responses. X-Force says that the C2 server masquerades as a U.S. flower shop that’s been active since July 2020. The communication between the malware and the C2 server is compressed via GZIP, AES encrypted and BASE64 encoded. The AES key and initialization vector (IV) are hardcoded into this sample: KEY: 3544c085656c997, IV: 4fcff6864c594343.


LittleLooter is “functionally rich,” researchers said, providing ITG18 operators the ability to pull off this long list of stunts on an infected Android device:


“The LittleLooter sample X-Force analyzed had the version number ‘5’, as well as an update capability if LittleLooter detected it was running a previous version,” [Wikoff detailed in a post](https://securityintelligence.com/posts/itg18-operational-security-errors-plague-iranian-threat-group/) on Wednesday. “The tool updates itself by downloading a zip file from a URL on the C2 server: ‘http[:]//[C2server]/updates/update\_[class name].zip’ and replacing the old ‘classes.dex’ file with the newer version from the zip file.”


LittleLooter is a modified version of Android malware reported by third-party researchers several years ago and “has likely been in use by ITG18 for years prior to our association with this threat group,” she said.


X-Force expects ITG18 operations to persist despite all the publicity the threat actor has gotten due to its lousy opsec and stolen data, she continued, which speaks to the group’s ability to just keep doing what it’s been doing for so long. “X-Force researchers have high confidence that ITG18 activity will continue regardless of public reporting due to their broad objectives and continued success of their operations,” Wikoff wrote. Her [post](https://securityintelligence.com/posts/itg18-operational-security-errors-plague-iranian-threat-group/) includes indicators to identify potential malicious activity on networks and mobile devices.


Hitting the Jackpot With Discovery of Training Videos
-----------------------------------------------------


Before the discovery of LittleLooter, “things like this” began with X-Force’s discovery of the group’s [training videos in May 2020](https://securityintelligence.com/posts/new-research-exposes-iranian-threat-group-operations/). Routine information gathering on the group led to discovery of an open file directory. That directory included files uploaded over the course of a week before the threat actor took them down.


It was a gold mine: The open directory included not only exfiltrated victim data but over 4 hours of training videos for new ITG18 operators. Hearing about those training videos was probably “what you’re all here for,” Wikoff surmised. As she and Emerson noted in a [July blog post](https://securityintelligence.com/posts/new-research-exposes-iranian-threat-group-operations/), it’s rare to get a behind-the-scenes look at how threat operators behave behind the keyboard, and “even rarer still are there recordings the operator self-produced showing their operations.”


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/05094114/Research_Genesis-e1628170890289.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/05094114/Research_Genesis-e1628170890289.jpg)


But that’s exactly what X-Force uncovered: OPSEC failures on the part of an ITG18 operator that provided “a unique behind-the-scenes look into their methods, and potentially, their legwork for a broader operation that is likely underway.”


The fact that Charming Kitten is so efficient at training newbies might mean a few things, Wikoff suggested during the session: It could be that the group has a large staff, and/or it could be that they have a good amount of worker turnover.


A Busy and Not-so-Charming Kitten
---------------------------------


What we do know: it’s a highly active adversary, with associated groups having [targeted genetic, neurology and oncology](https://threatpost.com/charming-kitten-pounces-on-researchers/165129/) professionals; [medical researchers](https://threatpost.com/charming-kitten-pounces-on-researchers/165129/); [Mid-East scholars](https://threatpost.com/apt-ta453-siphons-intel-mideast/167715/); and ex-President Trump’s 2020 [re-election campaign](https://threatpost.com/trump-biden-campaign-apt-phishing-emails/156319/). They’re notoriously ever-evolving: In October 2019, researchers reported that the actor had added [new spearphishing techniques](https://threatpost.com/iran-linked-charming-kitten-touts-new-spearphishing-tactics/149109/) to its arsenal in what appeared to be a ramp-up of operations. Security researchers who tracked the [earlier phase of the campaign](https://threatpost.com/charming-kitten-iranian-2fa/139979/) in October 2018 saw attacks tailored to elude two-factor authentication (2FA) in order to compromise email accounts and to monitor communications.


Between August 2020 and May 2021, X-Force has also observed ITG18 successfully compromising multiple victims aligned with the Iranian reformist movement, “Probably to monitor group activity around the Iranian presidential election in June,” Wikoff hypothesized.


Due to a basic misconfiguration by suspected ITG18 associates, IBM discovered a server with more than 40 gigabytes of data on the adversary’s operations.


iTG18’s training videos were made with a tool called Bandicam: a legit, free screen recorder for Windows. The group also uses [Zimbra](https://threatpost.com/zimbra-server-bugs-email-plundering/168188/), a popular, legitimate email and collaboration tool that’s at the heart of communications in over 200,000 businesses, over a thousand government and financial institutions. Every day, Zimbra is used by hundreds of millions of workers to exchange emails containing sensitive information.


That makes sense, given the group’s objectives: espionage and surveillance, likely in support of Iranian government objectives. They go after Iranian and what IBM X-Force enumerated as “near-abroad” dissidents, journalists and academics, along with reformist political party members; COVID researchers; and nuclear and financial regulators.


The group frequently leases virtual private servers and registers its own domains. Wikoff said that group operators might be given their own, virtual private server to run operations on, “soup to nuts,” replete with lists of potential targets.


The group’s TTPs include phishing via email, social media and SMS; credential harvesting; leveraging compromised accounts; and masquerading as legitimate organizations and individuals. Over the years, they’ve persistently exfiltrated all that data out of Google and Yahoo accounts.


Even Adversaries Stumble With CAPTCHAs
--------------------------------------


Google and Yahoo are unsurprising targets, but Charming Kitten isn’t fussy: The group gobbles up anything. “What we found interesting is that there’s no account too trivial to test credentials for,” Wikoff said, citing food delivery accounts – e.g., DoorDash – as one of many examples. “You name it. If they had a credential for it, they logged in and looked around,” she explained.


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/05094339/enduring-operations-e1628171032432.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/05094339/enduring-operations-e1628171032432.jpg)


X-Force researchers also had “a nice chuckle” when they saw ITG18 operators stumbling over CAPTCHAs. “We all know how fun those are,” Wikoff said. “To humanize [the operators], we all struggle. We saw him hung up on traffic lights: It took 45 seconds. It’s a nice reminder that threat actors are human, too.”


X-Force found a combination of victim-exfiltrated data and tools to get it on the same server.


As far as validating credentials goes, it’s “extremely time-consuming,” Wikoff surmised. The group must have “a considerable amount of manpower” behind them to pull it off, she said. The recordings show it all as a manual cut-and-paste slog. The training videos show that the operators stick harvested credentials into Notepad: an easy format for cutting and pasting. Then, they switch between copying a user name, pasting it into Gmail or Yahoo, then switching back to Notepad to do the same with passcodes.


But while it sounds like a slog, the operators whip through with alacrity that surprised Wikoff and Emerson. “It blows both our minds, how quickly the adversary can get into these accounts and set them up for exfiltrating and monitoring,” Wikoff said. Practice makes perfect, though, she remarked: “It just speaks to how long these adversaries have been doing this.”


The training videos also showed the operators modifying Zimbra collaboration accounts, changing the settings to “less secure access.” Then, they flipped back to the compromised accounts’ inboxes and, when they intercepted the “did you make this setting change?” alert, they said yup, that was me. The operators next added the compromised email accounts to Zimbra, copying and pasting the email addresses in as account names. They also changed syncing from every 15 minute to 1 minute so they could intercept sensitive data closer to real time.


Tracking shows that the group has, over time, exfiltrated at least 2 Terabytes since Fall 2018. The data has included personal information, location details, audio, video, photos, chat logs and SMS messages, and search histories. It’s also compromised social media on top of email accounts.


It’s No Laughing Matter: Use MFA or Else
----------------------------------------


There’s a bucket-load of schadenfreude to be enjoyed when it comes to adversaries faulty opsec, but this is a serious matter, Wikoff and Emerson stressed. In spite of ITG18 ‘s continued errors, it’s conducting a big, and often successful, operation that’s going after personal webmail and social media accounts.


The two researchers also emphasized the need to train employees. “In case of IPG18, personal resources are targeted, and employees’ personal computing habits can impact the security of the company,” Wikoff said. That means they’re going after all our info: where we go on vacation, our voice recordings, our conversations with other people. It’s all “ripe for social engineering opportunities,” she said – or for blackmail.


Emerson noted that the group tends to first go after targets’ contact lists when first getting access to compromised accounts. “They’re always looking for the next hotpoint, the next person to go after: often people who are related,” he noted.


All the more reason to keep pounding home the importance of multifactor authentication (MFA), Wikoff said. “We’ll say it til we’re blue in the face: … vendors have got to emphasize putting MFA on everything. We see this across the board. We can’t drive this point home enough … to put it lightly.


“ITG18 is a very serious, prolific group that runs cyberespionage and surveillance. Off of email accounts, cell phones. They have hardly changed their tactics” over the years,” she said.


The researchers said that IBM contacted law enforcement about the plethora of compromised accounts that they uncovered. So far, they haven’t detected any reaction from ITG18 in response to the light that IBM’s shed on the group’s opsec glitches: One reason why X-Force feels OK about sprinkling publicity glitter on it all, they said.


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[Wikoff]] [[X-Force]] [[ITG18]] [[said.]] [[LittleLooter]] [[group’s]] [[it’s]] [[Android]] [[C2]] [[that’s]] [[ThreatPost]]
