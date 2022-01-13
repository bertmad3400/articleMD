# BlueNoroff hackers steal crypto using fake MetaMask extension
### The North Korean threat actor group known as 'BlueNoroff' has been spotted targeting cryptocurrency startups with malicious documents and fake MetaMask browser extensions.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/bluenoroff-hackers-steal-crypto-using-fake-metamask-extension/
+ Date: 2022-01-13T15:14:32-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/05/24/NorthKoreaCrypto.jpg)

![North Korea and cryptocurrency](https://www.bleepstatic.com/content/hl-images/2021/05/24/NorthKoreaCrypto.jpg)


The North Korean threat actor group known as 'BlueNoroff' has been spotted targeting cryptocurrency startups with malicious documents and fake MetaMask browser extensions.


The motive of this group is [purely financial](https://www.bleepingcomputer.com/news/security/north-korean-hackers-behind-wannacry-and-sony-hack-sanctioned-by-usa/), but its sophistication in carrying out objectives has previously led researchers to conclude that this is [a sub-group of the North Korean Lazarus gang](https://www.bleepingcomputer.com/news/security/north-korean-apt-lazarus-targets-russian-entities-with-keymarble-backdoor/).


Although BlueNoroff has been active for several years, its structure and operation have been shrouded by mystery.


A report by Kaspersky attempts to shed some light by using intelligence collected during the most recent activity observed, dating back to November 2021.


Targets
-------


The latest attacks are focused on cryptocurrency startups located in the US, Russia, China, India, the UK, Ukraine, Poland, Czech Republic, UAE, Singapore, Estonia, Vietnam, Malta, Germany, and Hong Kong.



![Victim map on the latest campaign](Victim%20map%20on%20the%20latest%20campaign)**Victim map on the latest campaign**  
*Source: Kaspersky*
The threat actors attempt to infiltrate the communications of these firms and map the interactions between the employees to derive potential social engineering pathways.


In some cases, they do this by compromising the LinkedIn account of an employee and sharing a link to download a macro-laced document right on the platform.


BlueNoroff uses these real discussions to name laced documents accordingly and send them to the target employee at the right time.



![Email used in latest BlueNoroff campaigns](https://www.bleepstatic.com/images/news/u/1220909/Phishing/email-example.jpg)**Email used in latest BlueNoroff campaigns**  

Source: Kaspersky
To track their campaign, they include an icon from a third-party tracking service (Sendgrid) to get a notification when the victim opens the sent document.


The company names and logos impersonated by BlueNoroff are shown below:



![Logos and firms used for social engineering attacks](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Logos and firms used for social engineering attacks**  
*Source: Kaspersky*
As Kaspersky points out, these companies may not have been compromised, and Sendgrid may not know (was notified) that North Korean APTs are abusing them.


Infection chains
----------------


The first infection chain uses documents that feature VBS scripts, which exploit an old remote template injection vulnerability (CVE-2017-0199).



![First infection chain](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**First infection chain**  
*Source: Kaspersky*
The second infection chain relies on sending an archive that contains a shortcut file and a password-protected document (Excel, Word, or PDF).



![Second infection chain](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Second infection chain**  
*Source: Kaspersky*
The LNK file that supposedly contains the password to open the document initiates a series of scripts that fetches the next-stage payload.


Eventually, in both cases, a backdoor with the following functionalities is dropped onto the infected machine:


* Directory/File manipulation
* Process manipulation
* Registry manipulation
* Executing commands
* Updating configuration
* Stealing stored data from Chrome, Putty, and WinSCP

Fake MetaMask steal crypto from victims
---------------------------------------


BlueNoroff steals user credentials that can be used for lateral movement and deeper network infiltration, while they also collect configuration files relevant to cryptocurrency software.


"In some cases where the attackers realized they had found a prominent target, they carefully monitored the user for weeks or months," reads [Kaspersky’s report](https://securelist.com/the-bluenoroff-cryptocurrency-hunt-is-still-on/105488/).


"They collected keystrokes and monitored the user’s daily operations while planning a strategy for financial theft."


The main trick employed to steal the cryptocurrency assets is to replace the core components of wallet management browser extensions with tampered versions that are dropped on local memory.



![Tampered component on the laced Metamask plugin](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Tampered component on the laced Metamask plugin**  
*Source: Kaspersky*
Kaspersky notes that tampering with the Metamask Chrome extension requires a thorough analysis of 170,000 lines of code, indicative of the skills and determination of BlueNoroff.


Victims can only detect the extension is fake by switching the browser to Developer mode and seeing the extension source pointing to a local directory rather than the online store.



![Extension showing a local folder as an installation source](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Extension showing a local folder as an installation source**  
*Source: Kaspersky*
When the target uses a hardware wallet, the actors wait for transactions and hijack the amounts by changing the recipient's address.


Because they have only one chance before the victim realizes the infection, the actors also change the transaction amount to the maximum possible, draining the assets in one move.


Clues for attribution
---------------------


On the aspect of attribution, Kaspersky researchers report seeing overlaps and similarities between PowerShell scripts and backdoors used in the latest and past campaigns.



![Code similarities between different backdoors](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Code similarities between different backdoors**  
*Source: Kaspersky*
Moreover, the C2 address acquisition scheme is similar to the 2016 attacks, using a hardcoded DWORD value to resolve an IP address via XORing.


Finally, the metadata on the Windows shortcut files dropped as part of the second infection chain contain Korean characters.





## Tags:

#### Threatactor:
[[threatactor.name=APT38]] [[threatactor.name=Lazarus Group]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.city.name=Singapore]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.country.name=Vietnam]] [[victim.continent.name=Asia]] [[victim.country.name=Czech Republic]] [[victim.continent.name=Europe]] [[victim.country.name=Estonia]] [[victim.continent.name=Europe]] [[victim.country.name=Germany]] [[victim.continent.name=Europe]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=Malta]] [[victim.continent.name=Europe]] [[victim.country.name=Poland]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.country.name=Ukraine]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Kaspersky]] [[Bluenoroff]] [[Bleeping Computer]]
#### CVE's
[[CVE-2017-0199]]

