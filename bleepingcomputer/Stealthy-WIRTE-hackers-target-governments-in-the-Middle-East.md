# Stealthy WIRTE hackers target governments in the Middle East
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/stealthy-wirte-hackers-target-governments-in-the-middle-east/)
+ Date: November 29, 2021
+ Author: Bill Toulas


## Article:
![middle_east](https://www.bleepstatic.com/content/hl-images/2021/11/29/middle_east.jpg?rand=973175068)


A stealthy hacking group named WIRTE has been linked to a government-targeting campaign conducting attacks since at least 2019 using malicious Excel 4.0 macros.


The primary targeting scope includes high-profile public and private entities in the Middle East, but researchers also observed targets in other regions.


Kaspersky analyzed the campaign, toolset, and methods, and concluded with low confidence that WIRTE has pro-Palestinian motives and is suspected to be part of the '[Gaza Cybergang](https://www.bleepingcomputer.com/tag/gaza-cybergang/)'.


However, compared to other affiliated hacking groups, WIRTE has better OpSec and more stealthy techniques, and they can avoid detection for long periods.


Tricky dropper execution flow
-----------------------------


WIRTE's phishing emails include Excel documents that execute malicious macros to download and install malware payloads on recipients' devices


While the main focus of WIRTE's attacks government and diplomatic entities, Kaspersky has seen these attacks targeting a wide variety of industries throughout the Middle East and other regions.


"Our telemetry indicates that the threat actor has targeted a variety of verticals, including diplomatic and financial institutions, government, law firms, military organizations, and technology companies," explained Kaspersky's [report](http://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044/).


"The affected entities are located in Armenia, Cyprus, Egypt, Jordan, Lebanon, Palestine, Syria, and Turkey."


The malicious documents are tailored to raise the interest of the targeted victim, and use logos and themes that mimic brands, authorities, or the targeted organization.



![Phishing documents sent to victims](https://www.bleepstatic.com/images/news/u/1220909/Phishing/document.jpg)**Phishing documents sent to victims**  
*Source: Kaspersky*
The Excel dropper first runs a series of formulas in a hidden column, which hides the "enable editing" request from the original file and unhides a secondary spreadsheet that contains the decoy.


The dropper then runs formulas from a third spreadsheet with hidden columns, which perform the following three anti-sandbox checks:


1. Get the name of the environment
2. Check if a mouse is present
3. Check if the host computer can play sounds


If all the checks are passed, the macro writes a VBS script that writes an embedded PowerShell snippet and two registry keys for persistence.



![Adding the two registry keys](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/adding_registry%20keys.png)**Adding the two registry keys**  
*Source: Kaspersky*
The macro then continues by writing a PowerShell with VB code onto %ProgramData%. This snippet is the ‘LitePower’ stager that will download payloads and receive commands from the C2.


The commands observed by Kaspersky during the various monitored/analyzed intrusions are the following: 


* List local disk drives
* Get list of installed AV software
* Check if current user is admin
* Get OS architecture
* Check for the existence of backdoor services
* Check for registry keys added for COM hijacking
* List all installed hotfixes
* Get screenshot and save to %AppData% until the next POST request


Obscured command and control
----------------------------


The actors have placed their C2 domains behind Cloudflare to hide the actual IP addresses, but Kaspersky was able to identify some of them and found that they are hosted in Ukraine and Estonia.


Many of these domains date back to at least December 2019, indicative of WIRTE's ability to evade detection, analysis, and report for extensive periods.



![Mapped WIRTE C2 infrastructure](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Mapped WIRTE C2 infrastructure**  
*Source: Kaspersky*
The most recent intrusions use TCP/443 over HTTPS in C2 communication, but they also use TCP ports 2096 and 2087, as mentioned in [a 2019 report by Lab52](https://lab52.io/blog/wirte-group-attacking-the-middle-east/).


Another similarity with the older campaign is the sleep function on the script, which still ranges between 60 and 100 seconds.



![Sleep function on the script](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Sleep function on the script**  
*Source: Kaspersky*
WIRTE has now been seen tentatively expanding its targeting scope to financial institutes and large private organizations, which could be the result of experimentation or a gradual change in focus.


Kaspersky warns that even though the TTPs used by these actors are simple and rather ordinary, they are still very effective against the group's targets.




#### Tags:
[[Kaspersky]] [[WIRTE]] [[C2]] [[Bleeping Computer]]
