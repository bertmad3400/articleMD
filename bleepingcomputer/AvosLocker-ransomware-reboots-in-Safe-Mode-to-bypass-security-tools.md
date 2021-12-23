# AvosLocker ransomware reboots in Safe Mode to bypass security tools
### Recent AvosLocker ransomware attacks are characterized by a focus on disabling endpoint security solutions that stand in the way of threat actors.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/avoslocker-ransomware-reboots-in-safe-mode-to-bypass-security-tools/
+ Date: 2021-12-23T12:47:14-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/23/AvosLocker_ransomware.jpg)

![avos-locker](https://www.bleepstatic.com/content/hl-images/2021/12/23/AvosLocker_ransomware.jpg?rand=1730526537)


In recent attacks, the AvosLocker ransomware gang has started focusing on disabling endpoint security solutions that stand in their way by rebooting compromised systems into Windows Safe Mode.


This tactic makes it easier to encrypt victims' files since most security solutions will be automatically disabled after Windows devices boot in Safe Mode.


And their new approach appears to be quite effective since the number of attacks attributed to the particular group is rising.


Encrypting in 'Safe Mode'
-------------------------


AvosLocker operators leverage PDQ Deploy, a legitimate deployment tool for automating patch management, to drop several Windows batch scripts onto the target machine, which helps them to lay the ground for the attack, according to [a report from SophosLabs Principal Researcher Andrew Brandt](https://news.sophos.com/en-us/2021/12/22/avos-locker-remotely-accesses-boxes-even-running-in-safe-mode/).


These scripts modify or delete Registry keys that belong to specific endpoint security tools, including Windows Defender and products from Kaspersky, Carbon Black, Trend Micro, Symantec, Bitdefender, and Cylance.



![One of the batch script files used by Avos Locker](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/bat_file.png)*One of the batch script files used by AvosLocker (Sophos)*
The scripts also create a new user account on the compromised machine, naming it 'newadmin' and adding it to the Administrators user group.


Next, they configure that account to automatically log in when the system reboots into Safe Mode with Networking and disable "legal notice" dialog registry keys that could hamper the automatic login.


Finally, the scripts execute a reboot command which puts the machine into Safe Mode. Once it's up again, the ransomware payload is run from a Domain Controller location.


If the automated payload execution process fails, the actor can assume manual control of the procedure using the AnyDesk remote access tool.


"The penultimate step in the infection process is the creation of a 'RunOnce' key in the Registry that executes the ransomware payload, filelessly, from where the attackers have placed it on the Domain Controller," explains Brandt.


"This is a similar behavior to what we've seen IcedID and other ransomware do as a method of executing malware payloads without letting the files ever touch the filesystem of the infected computer."



![Entire operation of the dropped batch scripts](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/batch_operation.png)*Batch scripts being dropped (Sophos)*
Safe Mode used to easily bypass endpoint security
-------------------------------------------------


This same Safe Mode execution method was previously used by other ransomware groups, including [REvil](https://www.bleepingcomputer.com/news/security/revil-ransomware-has-a-new-windows-safe-mode-encryption-mode/) (with [auto-login](https://www.bleepingcomputer.com/news/security/revil-ransomware-now-changes-password-to-auto-login-in-safe-mode/) too), [BlackMatter](https://www.bleepingcomputer.com/news/security/blackmatter-ransomware-gang-rises-from-the-ashes-of-darkside-revil/), and [Snatch](https://www.bleepingcomputer.com/news/security/snatch-ransomware-reboots-to-windows-safe-mode-to-bypass-av-tools/), so this is clearly a security gap that needs to be addressed.


The whole idea behind putting the machine in Safe Mode is to disable any running security tools since most endpoint protection solutions don't run in that mode.


Thanks to this simple yet effective trick, even adequately protected machines can be rendered defenseless against ransomware execution chains.


To avoid arbitrary reboot commands from manifesting on your machines, ensure that your security tools can detect and prevent the addition of suspicious Registry keys.


This capability could interfere with legitimate Registry access, but it is well worth the additional trouble for admins.


As Sophos underlines in its report, no alert should be treated as "low priority," as a small and seemingly innocuous thing could be a pivotal link to a ransomware execution chain.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Carbon]] [[action.malware.name=IcedID]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Reg]] [[action.malware.name=REvil]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=Oslo]] [[victim.country.name=Norway]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Windows]] [[Avoslocker]] [[Bleeping Computer]]

