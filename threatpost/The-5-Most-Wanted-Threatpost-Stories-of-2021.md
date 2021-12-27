# The 5 Most-Wanted Threatpost Stories of 2021
### A look back at what was hot with readers in this second year of the pandemic.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177278
+ Date: 2021-12-27T18:57:24+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/27135554/2021-e1640631400644.jpg)

As 2021 draws to a close, and the COVID-19 pandemic drags on, it’s time to take stock of what resonated with our 1 million+ monthly visitors this year, with an eye to summing up some hot trends (gleaned from looking at the most-read stories on the Threatpost site).


While 2020 was all about work-from-home security, COVID-19-themed social engineering and gaming (all driven by social changes during Year One of the pandemic), 2021 saw a distinctive shift in interest. Data insecurity, code-repository malware, major zero-day vulnerabilities and fresh ransomware tactics dominated the most-read list – perhaps indicating that people are keenly focused on cybercrime innovation as the “new normal” for how we work becomes more settled in.


***Jump to section:***


1. [Data Leakapalooza](#Experian_Leak)
2. [Major Zero-Day Vulnerabilities](#Zero_Day)
3. [Code Repository Malware](#Supply_Chain)
4. [Ransomware Innovations](#Ransomware_Variants)
5. [Gaming Attacks](#Gaming_Security)
6. [Bonus! Zodiac Killer Cipher Cracked](#Zodiac_Killer)


**1. The Most-Read Story of 2021: Experian Leaks Everyone’s Credit Scores**
---------------------------------------------------------------------------


There were obviously some huge news stories that dominated headlines during the year: Log4Shell; Colonial Pipeline; Kaseya; ProxyLogon/ProxyShell; SolarWinds. But judging from article traffic, readers were most interested in…the Experian data exposure.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In April, Bill Demirkapi, a sophomore student at the Rochester Institute of Technology, discovered that the credit scores of almost every American [were exposed](https://threatpost.com/experian-api-leaks-american-credit-scores/165731/) through an API tool used by the Experian credit bureau, which he said was left open on a lender site without even basic security protections.[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/04/29144158/Experian-300x160.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/04/29144158/Experian.jpg)


The tool, called the Experian Connect API, allows lenders to automate FICO-score queries. Demirkapi said he was able to build a command-line tool that let him automate lookups for any credit score for nearly anyone, even after entering all zeros in the fields for date of birth, which he named, “Bill’s Cool Credit Score Lookup Utility.”


In addition to raw credit scores, the college student said that he was able to use the API connection to get “risk factors” from Experian that explained potential flaws in a person’s credit history, such as “too many consumer-finance company accounts.”


Experian, for its part, fixed the problem – and refuted concerns from the security community that the issue could be systemic.


Experian wasn’t the only household name that drew in readers for data insecurity: LinkedIn data going up for sale on the Dark Web was another very hot story this year.


### **LinkedIn Data Scraping**


After 500 million LinkedIn members were affected in a data-scraping incident in April, [it happened again](https://threatpost.com/data-700m-linkedin-users-cyber-underground/167362/) in June. A posting with 700 million LinkedIn records for sale appeared on popular cyberattacker destination RaidForums, by a hacker calling himself “GOD User TomLiner.” The advertisement included a sample of 1 million records as “proof.”


Privacy Sharks examined the free sample and saw that the records include full names, gender, email addresses, phone numbers and industry information. It’s unclear what the origin of the data is – but the scraping of public profiles is a likely source. According to LinkedIn, no breach of its networks occurred.


Even so, the security ramifications were significant, researchers said, in terms of the cache enabling brute-force cracking of account passwords, email and telephone scams, phishing attempts, identity theft and finally, the data could be a social-engineering goldmine. Sure, attackers could simply visit public profiles to target someone, but having so many records in one place could make it possible to automate targeted attacks using information about users’ jobs and gender, among other details.


**2. Major Zero-Day Bugs**
--------------------------


OK, this one’s a perennial topic of fascination, but 2021 had some doozies, starting with Log4Shell.


### **Log4Shell Threatens Basically All Web Servers in Existence**


The Log4Shell vulnerability is [an easily exploited flaw](https://threatpost.com/zero-day-in-ubiquitous-apache-log4j-tool-under-active-attack/176937/) in the ubiquitous Java logging library Apache Log4j could allow unauthenticated remote code execution (RCE) and complete server takeover — and it’s still being actively exploited in the wild.[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/21151757/Logs-300x200.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/21151757/Logs-e1640117899602.png)


The flaw (CVE-2021-44228) first turned up on sites that cater to users of the world’s favorite game, Minecraft. Apache rushed a patch but within a day or two, attacks became rampant as threat actors tried to exploit the new bug. From there, news of additional exploitation vectors, a second bug, various kinds of real-world attacks and the sheer enormity of the threat surface (the logging library is basically everywhere) dominated reader interest in December.


### **NSO Group’s Zero-Click Zero Day for Apple**


In September, a [zero-click zero-day](https://threatpost.com/apple-emergency-fix-nso-zero-click-zero-day/169416/) dubbed ForcedEntry be researchers was found, affecting all things Apple: iPhones, iPads, Macs and Watches. It turns out that it was being exploited by NSO Group to install the infamous Pegasus spyware.


Apple pushed out an emergency fix, but Citizen Lab had already observed the NSO Group targeting never-before-seen, zero-click exploit targeting iMessage to illegally spy on Bahraini activists.


The ForcedEntry exploit was particularly notable in that it was successfully deployed against the latest iOS versions – 14.4 & 14.6 – blowing past Apple’s new BlastDoor sandboxing feature to install spyware on the iPhones of the Bahraini activists.


### **Giant Zero-Day Hole in Palo Alto Security Appliances**


Another zero-day item that garnered big reader interest was [the news](https://threatpost.com/massive-zero-day-hole-found-in-palo-alto-security-appliances/176170/) that researchers from Randori developed a working exploit to gain remote code execution (RCE) on Palo Alto Networks’ GlobalProtect firewall, via the critical bug CVE 2021-3064.


Randori researchers said that if an attacker successfully exploits the weakness, they can gain a shell on the targeted system, access sensitive configuration data, extract credentials and more. And after that, attackers can dance across a targeted organization, they said: “Once an attacker has control over the firewall, they will have visibility into the internal network and can proceed to move laterally.”


Palo Alto Networks patched the bug on the day of disclosure.


### **The Great Google Memory Bug Zero-Day**


In March, Google [hurried out a fix](https://threatpost.com/google-mac-windows-chrome-zero-day/164759/) for a vulnerability in its Chrome browser that was under active attack. If exploited, the flaw could allow remote code-execution and denial-of-service attacks on affected systems. Readers flocked to the coverage of the issue.


The flaw is a use-after-free vulnerability, and specifically exists in Blink, the browser engine for Chrome developed as part of the Chromium project. Browser engines convert HTML documents and other web page resources into the visual representations viewable to end users.


“By persuading a victim to visit a specially crafted website, a remote attacker could exploit this vulnerability to execute arbitrary code or cause a denial-of-service condition on the system,” according to IBM X-Force’s report on the bug.


### **Dell Kernel-Privilege Bugs**


Earlier this year, five high-severity security bugs that remained hidden for 12 years [were found](https://threatpost.com/dell-kernel-privilege-bugs/165843/) to exist in all Dell PCs, tablets and notebooks shipped since 2009. They allow the ability to bypass security products, execute code and pivot to other parts of the network for lateral movement, according to SentinelLabs.


The flaws lurked in Dell’s firmware update driver, impacting potentially hundreds of millions of Dell desktops, laptops, notebooks and tablets, researchers said.


The multiple local privilege-escalation (LPE) bugs exist in the firmware update driver version 2.3 (dbutil\_2\_3.sys) module, which has been in use since 2009. The driver component handles Dell firmware updates via the Dell BIOS Utility, and it comes pre-installed on most Dell machines running Windows.


3. Code Repositories and the Software Supply Chain
--------------------------------------------------


The software supply chain is anchored by open-source code repositories – centralized locations where developers can upload software packages for use by developers in building various applications, services and other projects. They include GitHub, as well as more specialized repositories like the Node.js package manager (npm) code repository for Java; RubyGems for the Ruby programming language; Python Package Index (PyPI) for Python; and others.


These package managers represent a supply-chain threat given that anyone can upload code to them, which can in turn be unwittingly used as building blocks in various applications. Any applications corrupted by malicious code can attack the programs’ users.


To boot, a single malicious package can be baked into multiple different projects – infecting them with cryptominers, info-stealers and more, and making remediation a complex process.[![](https://media.threatpost.com/wp-content/uploads/sites/103/2018/09/27155850/threatlist-python-300x168.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2018/09/27155850/threatlist-python.png)


Cybercriminals have swarmed to this attack surface, and readers in 2021 loved to hear about their exploits.


For instance, in December, a [series of 17 malicious packages](https://threatpost.com/malicious-npm-code-packages-discord/176886/) in npm were found; they were all built to target Discord, the virtual meeting platform used by 350 million users that enables communication via voice calls, video calls, text messaging and files. The coal was to steal Discord tokens, which can be used to take over accounts.


Also this month, three malicious packages hosted in the PyPI code repository [were uncovered](https://threatpost.com/malicious-pypi-code-packages/176971/), which collectively have more than 12,000 downloads – and presumably slithered into installations in various applications. The packages included one trojan for establishing a backdoor on victims’ machines, and two info-stealers.


Researchers also discovered last week that there were 17,000 unpatched Log4j Java packages in the Maven Central ecosystem, leaving massive supply-chain risk on the table from [Log4Shell exploits](https://threatpost.com/new-log4shell-attack-vector-local-hosts/177128/). It will likely take “years” for it to be fixed across the ecosystem, [according](https://threatpost.com/java-supply-chain-log4j-bug/177211/) to Google’s security team.


Using malicious packages as a cyberattack vector was a common theme earlier in the year too. Here’s a rundown of other recent discoveries:


* In January, other Discord-stealing malware [was discovered](https://threatpost.com/discord-stealing-malware-npm-packages/163265/) in three npm packages. One, “an0n-chat-lib” had no legitimate “twin” package, but the other two made use of brandjacking and typosquatting to lure developers into thinking they’re legitimate. The “discord-fix” malicious component is named to be similar to the legitimate “discord-XP,” an XP framework for Discord bots. The “sonatype” package meanwhile made use of pure brandjacking.
* In March, researchers [spotted](https://threatpost.com/malicious-code-bombs-amazon-lyft-slack-zillow/164455/) malicious packages targeting internal applications for Amazon, Lyft, Slack and Zillow (among others) inside the npm public code repository – all of which exfiltrated sensitive information.
* That March attack was based on research from security researcher Alex Birsan, who found that it’s possible to [inject malicious code](https://threatpost.com/supply-chain-hack-paypal-microsoft-apple/163814/) into common tools for installing dependencies in developer projects. Such projects typically use public repositories from sites like GitHub. The malicious code then can use these dependencies to propagate malware through a targeted company’s internal applications and systems. The novel supply-chain attack was (ethically) used to  breached the systems of more than 35 technology players, including Microsoft, Apple, PayPal, Shopify, Netflix, Tesla and Uber, by exploiting public, open-source developer tools.
* In June, a group of cryptominers was found [to have infiltrated](https://threatpost.com/cryptominers-python-supply-chain/167135/) the PyPI. Researchers found six different malicious packages hiding there, which had a collective 5,000 downloads.
* In July, a credentials-stealing package that uses legitimate password-recovery tools in Google’s Chrome web browser [was found lurking in](https://threatpost.com/npm-package-steals-chrome-passwords/168004/)npm. Researchers caught the malware filching credentials from Chrome on Windows systems. The password-stealer is multifunctional: It also listens for incoming commands from the attacker’s command-and-control (C2) server and can upload files, record from a victim’s screen and camera, and execute shell commands.


**4. Interesting Ransomware Variants**
--------------------------------------


The ransomware epidemic matured in 2021, with the actual malware used to lock up files progressing beyond simply slapping an extension on targeted folders. Readers flocked to malware analysis stories covering advancements in ransomware strains, including the following Top 3 discoveries.


### **HelloKitty’s Linux Variant Targets VMs**


In June, for the first time, researchers [publicly spotted](https://threatpost.com/linux-variant-of-hellokitty-ransomware-targets-vmware-esxi-servers/167883/) a Linux encryptor – being used by the HelloKitty ransomware gang.


HelloKitty, the same group behind the [February attack](https://threatpost.com/cyberpunk-2077-publisher-hack-ransomware/163775/) on videogame developer CD Projekt Red, has developed numerous Linux ELF-64 versions of its ransomware, which it used to target VMware ESXi servers and virtual machines (VMs) running on them.[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/16162559/hellokitty-300x169.jpeg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/16162559/hellokitty-e1626467172148.jpeg)


VMware ESXi, formerly known as ESX, is a bare-metal hypervisor that installs easily onto servers and partitions them into multiple VMs. While that makes it easy for multiple VMs to share the same hard-drive storage, it sets systems up to be one-stop shopping spots for attacks, since attackers can encrypt the centralized virtual hard drives used to store data from across VMs.


Dirk Schrader of New Net Technologies (NNT) told Threatpost that on top of the attraction of ESXi servers as a target, “going that extra mile to add Linux as the origin of many virtualization platforms to [malware’s] functionality” has the welcome side effect of enabling attacks on any Linux machine.


### **MosesStaff: No Decryption Available**


A politically motivated group known as MosesStaff [was seen in November](https://threatpost.com/mosesstaff-locks-targets-ransom-decryption/176366/) paralyzing Israeli entities with no financial goal – and no intention of handing over decryption keys. Instead, it was using ransomware in politically motivated, destructive attacks at Israeli targets, looking to inflict the most damage possible.


MosesStaff encrypts networks and steals information, with no intention of demanding a ransom or rectifying the damage. The group also maintains an active social-media presence, pushing provocative messages and videos across its channels, and making its intentions known.


### **Epsilon Red Targets Exchange Servers**


Threat actors in June [were seen deploying](https://threatpost.com/exchange-servers-epsilon-red-ransomware/166640/) new ransomware on the back of a set of PowerShell scripts developed for exploiting flaws in unpatched Exchange Servers.


The Epsilon Red ransomware – a reference to an obscure enemy character in the X-Men Marvel comics, a super soldier of Russian origin armed with four mechanical tentacles – was discovered after an attack on a U.S.-based company in the hospitality sector.


Researchers said the ransomware was different in the way it spreads its hooks into a corporate network. While the malware itself is a “bare-bones” 64-bit Windows executable programmed in the Go programming language, its delivery system relies on a series of PowerShell scripts that “prepared the attacked machines for the final ransomware payload and ultimately delivered and initiated it,” they wrote.


**5. Gaming Security**
----------------------


For the second year in a row, gaming security was on the radar for readers in 2021, possibly because cybercriminals continue to target this area as result of the global COVID-19 pandemic driving higher volumes of play. In a recent survey by Kaspersky, nearly 61 percent reported suffering foul play such as ID theft, scams or the hack of in-game valuables. Some of the most popular articles are recapped below.


### **Steam Used to Host Malware**


In June, the appropriately named SteamHide malware [emerged](https://threatpost.com/steam-gaming-delivering-malware/166784/), which disguises itself inside profile images on the gaming platform Steam.[![](https://media.threatpost.com/wp-content/uploads/sites/103/2018/08/01084854/Steam-logo-300x169.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2018/08/01084854/Steam-logo.jpg)


The Steam platform merely serves as a vehicle which hosts the malicious file, according to research from G Data: “The heavy lifting in the shape of downloading, unpacking and executing a malicious payload fetched by the loader is handled by an external component, which accesses the malicious profile image on one Steam profile. This external payload can be distributed via crafted emails to compromised websites.”


The steganography technique is obviously not new — but Steam profiles being used as attacker-controlled hosting sites, is – and readers’ ears perked up in a big way when we posted the story.


### **Twitch Source-Code Leak**


In October, an anonymous user posted a link to a 125GB torrent on 4chan, containing all of Twitch’s source code, comments going back to its inception, user-payout information and more.


The attacker [claimed to have ransacked](https://threatpost.com/twitch-source-code-leaked/175359/) the live gameplay-streaming platform for everything it’s got;  Twitch confirmed the breach not long after.


The threat actor rationalized gutting the service by saying that the Twitch community needs to have the wind knocked out of its lungs. They called the leak a means to “foster more disruption and competition in the online-video streaming space,” because “their community is a disgusting toxic cesspool.”


### **Steam-Stealing Discord Scams**


In November, a scam started making the rounds on Discord, through which cybercriminals could harvest Steam account information and make off with any value the account contained.


Gamer-aimed Discord scams are just about everywhere. But researchers [flagged a new approach](https://threatpost.com/free-discord-nitro-offer-steam-credentials/176011/) as noteworthy because it crossed over between Discord and the Stream gaming platform, with crooks offering a purported free subscription to Nitro (a Discord add-on that enables avatars, custom emoji, profile badges, bigger uploads, server boosts and so on), in exchange for “linking” the two accounts.[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/04113440/nitro-fake-discord-website-600x324-1-300x162.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/04113440/nitro-fake-discord-website-600x324-1.png)


The target is first served a malicious direct message on Discord with the fake offer. “Just link your Steam account and enjoy,” the message said, which included a link to purportedly do just that. The malicious link takes users to a spoofed Discord page with a button that reads, “Get Nitro.” Once a victim clicks on the button, the site appears to serve a Steam pop-up ad, but researchers explained the ad is still part of the same malicious site.


The gambit is intended to fool users into thinking they’re being taken to the Steam platform to enter in their login information — in reality, the crooks are poised to harvest the credentials.


### **Sony PlayStation3 Bans**


In June, a reported breach of a Sony folder containing the serial ID numbers for every PlayStation3 console out there [appeared to](https://threatpost.com/ps3-players-ban-attacks-gaming/167303/) have led to users being inexplicably banned from the platform.


Sony reportedly left a folder with every PS3 console ID online unsecured, and it was discovered and reported by a Spanish YouTuber with the handle “The WizWiki” in mid-April. In June, players on PlayStation Network message boards began complaining that they couldn’t sign on.


Users mused that threat actors started using the stolen PS3 console IDs for malicious purposes, causing the legitimate players to get banned. But Sony didn’t confirm a connection between the PS3 ID breach and player reports of being locked out of the platform.


**Bonus Item: Zodiac Killer Cipher – Revealed!!**
-------------------------------------------------


One of the quirky stories that made it into the Top 10 most-read Threatpost stories for 2021 concerned the cracking of the Zodiac’s serial killer’s 340 cipher, which couldn’t be solved for 50 years.  

In December 2020, the code [was cracked](https://threatpost.com/cryptologists-zodiac-killer-340-cipher/162353/) by a team of mathematicians.


The Zodiac serial killer is believed to have murdered at least five people — and likely more — in and around the Northern California area in the late 1960s and early 1970s. The still-unnamed murderer sent a series of four coded messages to local newspaper outlets, bragging about his crimes and containing cryptic icons, which earned him the moniker “Zodiac.”[![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/12/17122725/Zodiac-300x200.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2020/12/17122725/Zodiac-e1608226062664.jpg)


The first cipher was quickly decoded. But the second, the 340 Cipher, named after its 340 characters, was trickier to figure out. Australian-based mathematician Sam Blake calculated that there were 650,000 possible ways to read the code, and Jarl Van Eycke, whose day job is as a warehouse operator in Belgium, wrote a code-breaking software to tackle decryption. Soon, their unique algorithmic approach paid off. The message, officially recognized by the FBI as correct, reads:


“I HOPE YOU ARE HAVING LOTS OF FUN IN TRYING TO CATCH ME THAT WASNT ME ON THE TV SHOW WHICH BRINGS UP A POINT ABOUT ME I AM NOT AFRAID OF THE GAS CHAMBER BECAUSE IT WILL SEND ME TO PARADICE ALL THE SOONER BECAUSE I NOW HAVE ENOUGH SLAVES TO WORK FOR ME WHERE EVERYONE ELSE HAS NOTHING WHEN THEY REACH PARADICE SO THEY ARE AFRAID OF DEATH I AM NOT AFRAID BECAUSE I KNOW THAT MY NEW LIFE IS LIFE WILL BE AN EASY ONE IN PARADICE DEATH.”


While the name of the elusive serial killer remains hidden, the breakthrough represents a triumph for cryptology and the basic building blocks of cybersecurity — access control and segmentation.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=Inception]]

#### Action:
[[action.malware.name=Anchor]] [[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=HELLOKITTY]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Education]] [[victim.industry.name=Finance]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Information]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Bahrain]] [[victim.continent.name=Asia]] [[victim.country.name=Israel]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Belgium]] [[victim.continent.name=Europe]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Ransomware]] [[Malware]] [[Experian]] [[Linkedin]] [[Linux]] [[Threatpost]] [[Zero-day]] [[Log4shell]] [[Google]] [[Npm]] [[ThreatPost]]
#### CVE's
[[CVE-2021-44228]]

