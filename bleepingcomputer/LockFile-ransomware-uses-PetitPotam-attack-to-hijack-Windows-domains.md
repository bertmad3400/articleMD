# LockFile ransomware uses PetitPotam attack to hijack Windows domains
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/lockfile-ransomware-uses-petitpotam-attack-to-hijack-windows-domains/)
+ Date: August 20, 2021
+ Author: Ionut Ilascu


## Article:
![New LockFile ransomware leverages PetitPotam NTLM relay attack to take over domain controllers](https://www.bleepstatic.com/content/hl-images/2021/07/07/Microsoft-Defender.jpg)


At least one ransomware threat actor has started to leverage the recently discovered [PetitPotam NTLM relay attack](https://www.bleepingcomputer.com/news/microsoft/new-petitpotam-attack-allows-take-over-of-windows-domains/) method to take over the Windows domain on various networks worldwide.


Behind the attacks appears to be a new ransomware gang called LockFile that was first seen in July, which shows some resemblance and references to other groups in the business.



### Exploiting PetitPotam for DC access


LockFile attacks have been recorded mostly in the U.S. and Asia, its victims including organizations in the following sectors: financial services, manufacturing, engineering, legal, business services, travel, and tourism.


Security researchers at Symantec, a division of Broadcom, said that the actor’s initial access on the network is through Microsoft Exchange servers but the exact method remains unknown at the moment.


Next, the attacker takes over the organization’s domain controller by leveraging the new PetitPotam method, which forces authentication to a remote NTLM relay under LockFile’s control.


Discovered by security researcher [Gilles Lionel](https://twitter.com/topotam77) in July, PetitPotam has a few variations that Microsoft kept trying to block. At this point, the [official mitigations](https://www.bleepingcomputer.com/news/security/microsoft-shares-mitigations-for-new-petitpotam-ntlm-relay-attack/) and [updates](https://www.bleepingcomputer.com/news/microsoft/windows-security-update-blocks-petitpotam-ntlm-relay-attacks/) do not completely [block the PetitPotam](https://www.bleepingcomputer.com/news/security/new-unofficial-windows-patch-fixes-more-petitpotam-attack-vectors/) attack vector.


LockFile threat actor seems to rely on publicly available [code to exploit the original PetitPotam](https://github.com/zcgonvh/EfsPotato) (tracked as CVE-2021-36942) variant.


Once the attackers successfully take over the domain controller, they effectively have control over the entire Windows domain and can run any command they wish.


### LockBit likeness


Symantec notes in a blog post today that the ransom note from LockFile ransomware is very similar to the one used by the LockBit ransomware group.



![Ransom note from LockFile ransomware ](https://www.bleepstatic.com/images/news/u/1100723/Ransomware/LockFile/LockFileRansomNote.png)**source: BleepingComputer**
Furthermore, it looks like the new gang also makes a not-so-subtle reference to the Conti gang in the contact email address they leave for the victim: *contact@contipauper[.]com*.


If we were to speculate about the choice for the email’s domain, we could say that LockFile looks like the project of the [disgruntled Conti affiliate that leaked](https://www.bleepingcomputer.com/news/security/angry-conti-ransomware-affiliate-leaks-gangs-attack-playbook/) the gang’s attack playbook.


### Gaps in the attack chain


Symantec analyzed LockFile’s attack chain and note that the hackers typically spend at least several days on the network before detonating the file-encrypting malware, typical for this kind of attacks.


The researchers say that when compromising the victim’s Exchange server, the attacker runs a PowerShell command that downloads a file from a remote location.


In the last stage of the attack, 20 to 30 minutes before deploying the ransomware, the threat actor proceeds to take over the domain controller by installing on the compromised Exchange server the PetitPotam exploit and two files:


* active\_desktop\_render.dll
* active\_desktop\_launcher.exe (legitimate KuGou Active Desktop launcher)


The legitimate KuGou Active Desktop launcher is abused to perform a DLL hijacking attack to load the malicious DLL to evade detection by security software.


The [researchers say](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/lockfile-ransomware-new-petitpotam-windows) that when loaded by the launcher, the DLL tries to load and decrypt a file called “desktop.ini” that contains shellcode. Symantec has not retrieved the file for analysis but says that a successful operation ends with running the shellcode.



“The encrypted shellcode, however, very likely activates the efspotato.exe file that exploits PetitPotam” - Symantec



The final step is to copy the LockFile ransomware payload on the local domain controller and push it across the network with the help of a script and executables that run on client hosts immediately after authentication to the server.


Symantec believes that LockFile is a new ransomware actor and that it could have a connection to other players in the business, either known in the community or retired.


LockFile is still active and has been seen as recently as today inside a victim network.




#### Tags:
[[LockFile]] [[PetitPotam]] [[ransomware]] [[Symantec]] [[DLL]] [[Bleeping Computer]]
