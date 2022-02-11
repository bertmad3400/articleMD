# Microsoft fixes Defender flaw letting hackers bypass antivirus scans
### Microsoft has recently addressed a weakness in the Microsoft Defender Antivirus on Windows that allowed attackers to plant and execute malicious payloads without triggering Defender's malware detection engine.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-defender-flaw-letting-hackers-bypass-antivirus-scans/
+ Date: 2022-02-10T19:20:20-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/02/10/0_Microsoft-Defender.jpg)

![Microsoft Defender](https://www.bleepstatic.com/content/hl-images/2022/02/10/0_Microsoft-Defender.jpg)


Microsoft has recently addressed a weakness in the Microsoft Defender Antivirus on Windows that allowed attackers to plant and execute malicious payloads without triggering Defender's malware detection engine.


This security flaw [[1](https://twitter.com/splinter_code/status/1481073265380581381), [2](https://twitter.com/overtsecrecy/status/1389985293994975232)] affected the [latest Windows 10 versions](https://twitter.com/NathanMcNulty/status/1481133301767098369), and threat attackers could abuse it [since at least 2014](https://twitter.com/SecurityAura/status/1481107646082072577).


As BleepingComputer [previously reported](https://www.bleepingcomputer.com/news/security/microsoft-defender-weakness-lets-hackers-bypass-malware-detection/), the flaw resulted from lax security settings for the "HKLM\Software\Microsoft\Windows Defender\Exclusions" Registry key. This key contains the list of locations (files, folders, extensions, or processes) excluded from Microsoft Defender scanning.


Exploiting the weakness was possible because the Registry key was accessible by the 'Everyone' group, as shown in the image below.



![Exclusions Registry key accessible by the Everyone group](https://www.bleepstatic.com/images/news/Microsoft/w/windows-defender-atp/exclusions-permissions-change/old-exclusions-permissions.jpg)**Exclusions Registry key accessible by the Everyone group**  
*Source: BleepingComputer*
This made it possible for local users (regardless of their permissions) to access it via the command line by querying the Windows Registry.



![Accessing Defender exclusions](https://www.bleepstatic.com/images/news/u/1100723/2022/WinDefenderExclusions.jpg)*Accessing Defender exclusions (BleepingComputer)*
Security expert Nathan McNulty [also warned](https://twitter.com/NathanMcNulty/status/1481133301767098369) that users could also grab the list of exclusions from registry trees with entries storing Group Policy settings, which is much more sensitive info as it provides exclusions for multiple computers on a Windows domain.


After finding out what folders were added to the antivirus exclusion list, attackers could deliver and execute malware from an excluded folder on a compromised Windows system without having to fear that its malicious payload will be detected and neutralized.


By exploiting this weakness, BleepingComputer could execute a sample of Conti ransomware from an excluded folder and encrypt a Windows system without any warnings or signs of detection from Microsoft Defender.


Security weakness addressed silently by Microsoft
-------------------------------------------------


This is no longer be possible given Microsoft has now addressed the weakness via a silent update, as [spotted](https://twitter.com/SecGuru_OTX/status/1491708672027901955) by Dutch security expert SecGuru\_OTX on Thursday.


SentinelOne threat researcher Antonio Cocomazzi [confirmed](https://twitter.com/splinter_code/status/1491777485457039363) that the flaw can no longer be used on Windows 10 20H2 systems after installing the February 2022 Patch Tuesday Windows updates.


Some users are seeing the new permission change after installing the February 2022 Patch Tuesday Windows updates.


On the other hand, Will Dormann, a vulnerability analyst for CERT/CC, [noted that he received the permissions change](https://twitter.com/wdormann/status/1491808676193214467) without installing any updates, indicating that the change could be added by both Windows updates and Microsoft Defender security intelligence updates.


As BleepingComputer was also able to confirm today, the permissions on Windows advanced security settings for Defender exclusions have indeed been updated, with the 'Everyone' group removed from the Registry key's permissions.



![New permissions for the Exclusions Registry key](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**New permissions for the Exclusions Registry key**  
*Source: BleepingComputer*
On Windows 10 systems where this change has already rolled out, users are now required to have admin privileges to be able to access the list of exclusions via the command line or when adding them using the Windows Security settings screen.



![Access to Defender exclusions now blocked](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)*Access to Defender exclusions now blocked (BleepingComputer)*
The change rolled out since our previous report, but, at the moment, only Microsoft knows how it was pushed to affected Windows 10 systems (via Windows updates, Defender intelligence updates, or other means).


A Microsoft spokesperson was not available for comment when contacted by BleepingComputer earlier today.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Bleepingcomputer]] [[Bleeping Computer]]

