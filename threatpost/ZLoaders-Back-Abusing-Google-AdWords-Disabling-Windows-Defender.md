# ZLoader’s Back, Abusing Google AdWords, Disabling Windows Defender
### The well-known banking trojan retools for stealth with a whole new attack routine, including using ads for Microsoft TeamViewer and Zoom to lure victims in.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169448)
+ Date: September 14, 2021  1:21 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/14124501/Letter-Z-e1631638050739.jpg)
A targeted campaign delivering the ZLoader banking trojan is spreading via Google AdWords, and is using a mechanism to disable all Windows Defender modules on victim machines, researchers have found.


That’s according to SentinelLabs, which said that to lower the rates of detection, the infection chain for the campaign also includes the use of a signed dropper, plus a backdoored version of the Windows utility wextract.exe to embed the ZLoader payload itself.


ZLoader has been around a while, one of many malware forks rising from the ashes of the Zeus banking trojan after its source code was [published nearly 10 years ago](https://threatpost.com/zeus-source-code-leaked-051011/75217/).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“[It] is a typical banking trojan which implements web injection to steal cookies, passwords and any sensitive information,” SentinelLabs analysts noted in a [Monday posting](https://www.sentinelone.com/labs/hide-and-seek-new-zloader-infection-chain-comes-with-improved-stealth-and-evasion-mechanisms/) on the new campaign. “It attacks users of financial institutions all over the world and has also been used to deliver ransomware families like Egregor and Ryuk. It also provides backdoor capabilities and acts as a generic loader to deliver other forms of malware.”


**Stealthy ZLoader Infection Chain Starts With Google AdWords**
---------------------------------------------------------------


To target victims, the malware is spread from a fake Google advertisement (published through Google AdWords) for various software, researchers found – an indirect alternative to social-engineering tactics like spear-phishing emails. The lures include Discord, Java plugins, Microsoft’s TeamViewer and Zoom.


Thus, when someone Googles, say, “Team Viewer download,” an advertisement shown by Google will redirect the person to a fake TeamViewer site under the attacker’s control, according to SentinelLabs. From there, the user can be tricked into downloading a fake installer in a signed MSI format, with a signing timestamp of Aug. 23.


“It appears that the cybercriminals managed to obtain a valid certificate issued by Flyintellect Inc., a Software company in Brampton, Canada,” researchers explained. “The company was registered on 29 June 2021, suggesting that the threat actor possibly registered the company for the purpose of obtaining those certificates.”


**Disabling Windows Defender**
------------------------------


The signed .MSI file is of course not an installer for legitimate software at all, but is rather the first-stage dropper for the malware.


Once downloaded, it runs an installation wizard that creates the following directory: *C:\Program Files (x86)\Sun Technology Network\Oracle Java SE*, and drops a .BAT file appropriately called “setup.bat.”


After that, the built-in Windows cmd.exe function is used to execute that file, which in turn downloads a second-stage dropper that then initiates yet a third stage of infection by executing a script called “updatescript.bat.”


This third-stage script performs most of the Defender-killing dirty work.


“The third stage dropper contains most of the logic to impair the defenses of the machine,” researchers explained. “At first, it disables all the Windows Defender modules through the PowerShell cmdlet Set-MpPreference. It then adds exclusions, such as regsvr32, *.exe, *.dll, with the cmdlet Add-MpPreference to hide all the components of the malware from Windows Defender.”


At this point, it downloads a fourth stage dropper from the URL “hxxps://pornofilmspremium.com/tim[dot]exe,” which is saved as “tim.exe” and executed through the legitimate Windows explorer.exe function.


“This allows the attacker to break the parent/child correlation often used by endpoint detection and response (EDRs) for detection,” researchers explained.


They added that the tim.exe binary is actually a backdoored version of the legitimate Windows utility wextract.exe, containing additional code for creating a new malicious batch file with the name “tim.bat.”


“The tim.bat file is a very short script that downloads the final ZLoader DLL payload with the name tim.dll,” they noted. This final payload is executed using the legitimate Windows function known as regsvr32, which allows the attackers to proxy the execution of the DLL through a signed binary by Microsoft.


The intensive use of legitimate Windows utilities and functions serves to help the malware avoid defenses and hide itself, researchers noted.


**More Defense Evasion**
------------------------


Tim.bat has one more trick up its sleeve: It downloads another script, called “nsudo.bat,” which performs multiple operations with the goal of elevating privileges on the system and impairing defenses:


**The Tim Botnet**
------------------


As some of the malicious file names suggest, the cybercriminal’s infrastructure includes the Tim botnet, according to the analysis. The botnet’s structure involves at least 350 different web domains.


“Some domains implement the gate.php component, which is a fingerprint of the ZLoader botnet,” researchers explained. “We noticed during our investigation that all the domains were registered from April to Aug 2021, and they switched to the new IP (195.24.66[dot]70) on the 26th of August.”


This is the first time the researchers have observed this particular attack chain in a ZLoader campaign, which for now is targeting customers of Australian and German banking institutions. If this campaign is successful, a stealthier attack routine could show up in other places, they said.


“The attack chain…shows how the complexity of the attack has grown in order to reach a higher level of stealthiness,” researchers concluded. “The first stage dropper has been changed from the classic malicious document to a stealthy, signed MSI payload. It uses backdoored binaries and a series of [living off the land utilities] to impair defenses and proxy the execution of their payloads.”


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[Windows]] [[ZLoader]] [[Google]] [[“The]] [[malware]] [[explained.]] [[backdoored]] [[ThreatPost]]
