# OceanLotus hackers turn to web archive files to deploy backdoors
### Vietnamese hackers of the APT32 group (Ocean Lotus) are now using Web Archive files (.mht and .mhtml) to deploy backdoors on their targets.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/oceanlotus-hackers-turn-to-web-archive-files-to-deploy-backdoors/
+ Date: 2022-01-12T10:20:43-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/03/25/Hacker.jpg)

![actor](https://www.bleepstatic.com/content/hl-images/2021/03/25/Hacker.jpg?rand=1021966306)


The OceanLotus group of state-sponsored hackers are now using the web archive file format (.MHT and .MHTML) to deploy backdoors to compromised systems.


The goal is to evade detection by antivirus solutions  tools which are more likely to catch commonly abused document formats and stop the victim from opening them on Microsoft Office.


Also tracked as APT32 and SeaLotus, the hackers have shown a tendency in the past to try out [less common methods](https://www.bleepingcomputer.com/news/security/oceanlotus-apt-uses-steganography-to-load-backdoors/) for deploying malware.


A report from Netskope Threat Labs shared with Bleeping Computer in advance notes that OceanLotus' campaign using web archive files is still active, although the targeting scope is narrow and despite the command and control (C2) server being disrupted.


From trusty RARs to Word macros
-------------------------------


The attack chain starts with a RAR compression of a 35-65MB large web archive file containing a malicious Word document.



![RAR file dropped as the first step of the attack](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/rar.jpg)**RAR file dropped as the first step of the attack**  
*Source: Netskope*
To bypass Microsoft Office protection, the actors have set the ZoneID property in the file's metadata to "2", making it appear as if it was downloaded from a trustworthy source.



![Editing ZoneID to bypass MS Office protection](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/zone-id.jpg)**Setting ZoneID value to bypass MS Office protection**  
*Source: Netskope*
When opening the web archive file with Microsoft Word, the infected document prompts the victim to "Enable Content", which opens the way to executing malicious VBA macro code.



![Decoded VBA code used in APT32 docs](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Decoded VBA code used in APT32 docs**  
*Source: Netskope*
The script performs the following tasks on the infected machine:


1. Drops the payload to "C:\ProgramData\Microsoft\User Account Pictures\guest.bmp";
2. Copies the payload to "C:\ProgramData\Microsoft Outlook Sync\guest.bmp";
3. Creates and display a decoy document named "Document.doc";
4. Rename the payload from "guest.bmp" to "background.dll";
5. Executes the DLL by calling either "SaveProfile" or "OpenProfile" export functions

After the payload is executed, the VBA code deletes the original Word file and opens the decoy document which serves the victim a bogus error.


Backdoor uses Glitch hosting service
------------------------------------


The payload dropped in the system is a 64-bit DLL that executes every 10 minutes thanks to a scheduled task impersonating a WinRAR update check.



![Fake process carrying the payload injection](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Fake process carrying the payload injection**  
*Source: Netskope*
The backdoor is injected into the rundll32.exe process running indefinitely in the system memory to evade detection, Netskope notes in its [technical report](http://www.netskope.com/blog/abusing-microsoft-office-using-malicious-web-archive-files).



![Payload injected and unpacked into memory](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Payload injected and unpacked into memory**  
*Source: Netskope*
The malware collects network adapter information, computer name, username, enumerates system directories and files, checks the list of running processes.


Once that basic data is gathered, the backdoor compiles everything into a single packages and encrypts the content before it's sent to the C2 server.


This server is hosted on Glitch, a cloud hosting and web development collaboration service that is frequently [abused for malicious purposes](https://www.bleepingcomputer.com/news/security/glitch-service-abused-to-host-short-lived-phishing-sites/).



![Backdoor communicating with a Glitch-hosted C2](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Backdoor communicating with a Glitch-hosted C2**  
*Source: Netskope*
By using a legitimate cloud hosting service for C2 communication, the actors further reduce the chances of being detected even when network traffic monitoring tools are deployed.


Although Glitch took down the C2 URLs identified and reported by Netskope researchers, it's unlikely that this will stop APT32 from creating new ones using different accounts.


For the complete list of the indicators of compromise from this campaign, you may check [this GitHub repository](https://github.com/netskopeoss/NetskopeThreatLabsIOCs/tree/main/MHTGlitch/IOCs).





## Tags:

#### Threatactor:
[[threatactor.name=APT3]] [[threatactor.name=APT32]] [[threatactor.name=APT32]] [[threatactor.name=APT32]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Netskope]] [[Microsoft]] [[Apt32]] [[Vba]] [[C2]] [[Bleeping Computer]]

