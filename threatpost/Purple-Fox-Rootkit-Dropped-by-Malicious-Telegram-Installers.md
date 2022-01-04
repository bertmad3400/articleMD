# Purple Fox Rootkit Dropped by Malicious Telegram Installers
### Multiple malicious installers were delivering the same Purple Fox rootkit version using the same attack chain, possibly distributed via email or phishing sites.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177330
+ Date: 2022-01-04T17:12:12+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2020/07/06105231/purple-fox.jpg)

A malicious Telegram instant-messaging app installer scurries past a slew of antivirus (AV) engines to deliver Purple Fox malware, evading detection by separating the attack into bite-sized morsels that fly under the radar.


In a Monday [report](https://blog.minerva-labs.com/malicious-telegram-installer-drops-purple-fox-rootkit), Minerva Labs said that the attack evades detection by AV products from the likes of Avira, ESET, Kaspersky, McAfee, Panda, Trend Micro, Symantec and many more.


“We have often observed threat actors using legitimate software for dropping malicious files,” analysts wrote. “This time however is different. This threat actor was able to leave most parts of the attack under the radar by separating the attack into several small files, most of which had very low detection rates by AV engines, with the final stage leading to Purple Fox [rootkit infection](https://threatpost.com/microsoft-exploits-purple-fox-ek/157157/).”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The malicious installer, bearing the familiar Telegram icon of a white paper plane, is actually a compiled AutoIt script called “Telegram Desktop.exe.” The installer creates a new folder named “TextInputh” under C:\Users\Username\AppData\Local\Temp\. It drops two files into the folder: an actual Telegram installer (which isn’t executed), and a malicious downloader, TextInputh.exe.


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/04103420/Malicious-installer-150x150.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/04103420/Malicious-installer.jpg)


The malicious downloader, TextInputh.exe, creates a new folder named “1640618495” under the C:\Users\Public\Videos\ directory. In the next stage of the attack, the executable contacts a command-and-control (C2) server – a C2 that was already down at the time of investigation – and downloads two files to the new folder: a legitimate 7z archiver and a RAR archive (1.rar).


The 1.rar archive contains the payload and the configuration files, as shown in the image below. The 7z program unpacks everything onto the ProgramData folder.


TextInputh.exe then performs these actions on infected machines:


* Copies 360.tct with “360.dll” name, rundll3222.exe and svchost.txt to the ProgramData folder
* Executes ojbk.exe with the “ojbk.exe -a” command line
* Deletes 1.rar and 7zz.exe and exits the process


Next, a registry key is created for persistence, a DLL (rundll3222.dll) disables Microsoft’s [User Account Control](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works) (UAC) malware-inhibiting security control, the payload (svchost.txt) is executed, and these five additional files are dropped onto the infected system:


1. Calldriver.exe
2. Driver.sys
3. dll.dll
4. kill.bat
5. speedmem2.hg


UAC is a Windows security feature designed to prevent changes to an operating system by unauthorized users, applications or malware. Bypassing UAC is a key function that’s regularly [coded into](https://threatpost.com/chrome-deliver-malware-as-legit-win-10-app/175884/) [malware](https://threatpost.com/trickbot-switches-to-a-new-windows-10-uac-bypass-to-evade-detection/152477/). With UAC out of the picture, any programs that run on an infected system – including viruses and malware – are free to gain administrator privileges.


Small Files Cluster-Block 360 AV
--------------------------------


The five files that fly under the radar “work together to shut down and block the initiation of 360 AV processes from the kernel space, thus allowing the next stage attack tools (Purple Fox rootkit, in our case) to run without being detected,” according to Minerva Labs’ writeup.


“The beauty of this attack is that every stage is separated to a different file which are useless without the entire file set,” according to the report. “This helps the attacker protect his files from AV detection.”


After blocking 360 AV, the malware then gathers the following list of system information, checks to see if a long list of security tools are running, and, finally, sends all the information to a hardcoded C2 address.


1. Hostname
2. CPU – by retrieving a value of HKLM\HARDWARE\DESCRIPTION\System\CentralProcessor\0\ ~MHz registry key
3. Memory status
4. Drive Type
5. Processor Type – by calling GetNativeSystemInfo and checking the value of wProcessorArchitecture.


The Latest Bite from the Rabid Purple Fox
-----------------------------------------


Purple Fox, which first appeared in 2018, is a malware campaign that up until March required user interaction or some kind of third-party tool to infect Windows machines. Last spring, the attackers behind the campaign skipped over that crutch by empowering the malware with the [ability to brute force](https://threatpost.com/purple-fox-malware-windows-worm/164993/) its way into victims’ systems on its own, according to research from [Guardicore Labs](https://www.guardicore.com/labs/purple-fox-rootkit-now-propagates-as-a-worm/). At the same time, Purple Fox was outfitted with a rootkit that allowed it to burrow in, evade detection and establish persistence.


Minerva Labs said that it found a large number of malicious installers delivering the same Purple Fox rootkit version using the same attack chain. It’s not entirely clear how it’s being distributed, though analysts believe that some were delivered via email, while others were presumably downloaded from phishing sites.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Crutch]] [[action.malware.name=Miner-C]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Systeminfo]] [[action.malware.name=Systeminfo]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Malware]] [[Rootkit]] [[Textinputh.exe]] [[Uac]] [[ThreatPost]]

