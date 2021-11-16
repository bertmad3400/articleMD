# MosesStaff Locks Up Targets, with No Ransom Demand, No Decryption
### A politically motivated group is paralyzing Israeli entities with no financial goal — and no intention of handing over decryption keys.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176366)
+ Date: November 16, 2021  1:29 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/16132506/moses-e1637087120137.jpg)
The MosesStaff hacking group is aiming politically motivated, destructive attacks at Israeli targets, looking to inflict the most damage possible, researchers warned.


Unlike other anti-Zionist hacktivists like [the Pay2Key](https://research.checkpoint.com/2020/pay2key-the-plot-thickens/) and BlackShadow gangs, which look to extort their victims and cause embarrassment, MosesStaff encrypts networks and steals information, with no intention of demanding a ransom or rectifying the damage. That’s according to Check Point Research (CPR), which began observing MosesStaff activity in September.


The group also maintains an active social-media presence, pushing provocative messages and videos across its channels, and making its intentions known.


“In the language of the attackers, their purpose is to ‘fight against the resistance and expose the crimes of the Zionists in the occupied territories,'” researchers explained in a [Monday post](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/). “There is no ransom demand and no decryption option; their motives are purely political.”


**Known Vulnerabilities**
-------------------------


MosesStaff (named after the Staff of Moses mentioned in the Book of Exodus, which was used to part the Red Sea for fleeing Israelites, among other things) is exploiting known vulnerabilities in Microsoft Exchange Server to achieve initial compromise, CPR noted. Then, to carry out its attacks, the opens an obfuscated, password-protected webshell.


Using this access, the threat actors go on to deploy several additional tools, according to the analysis:


The next step is to collect information on the machines in the network, including domain name, machine names and administrator credentials. CPR said this list is later used to compile a custom, environment-specific malware called PyDCrypt — a precursor to the main payload, which, it turns out, uses a flawed encryption mechanism.


**MosesStaff’s Custom Malware Scheme**
--------------------------------------


PyDCrypt, which is written in Python, uses the list information to move laterally throughout the network, replicating itself inside the network using available tools like PowerShell, PSExec or WMIC, and installing PSExec, the batch scripts and the main encryption payload on each machine.


The main encryption payload is another custom malware called DCSrv, according to the writeup. It masquerades as the legitimate svchost.exe process and is singly focused on encrypting all computer volumes; and, it features a tri-part execution flow: Driver installation, volume encryption and boot loader installation.


The first action is to create two services named DCUMSrv and DCDrv. The former provides persistence across startups. DCDrv meanwhile runs the supplied filter driver DCDrv.sys, which in turn deploys the encryption.


“When the malware finishes installing the driver, it performs a reboot after a few minutes to make the driver operational,” CPR analysts explained. “On the second run, the malware waits for the exact time given in the configuration before it detonates its encryption mechanism. This is yet another proof that the payloads are targeted and created per victim.”


This core encryption mechanism is based on the DiskCryptor open-source library, “to perform volume encryption and lock the victims’ computers with a bootloader that won’t allow the machines to boot without the correct password.”


**Breakable Encryption**
------------------------


The good news is that decrypting victim systems is possible, CPR found.


“The most notorious ransomware gangs ([e.g. Conti, REvil, Lockbit etc](https://threatpost.com/conti-ransomware-backups/175114/).), almost without exception, always ensure that their encryption system is well-designed and unassailable,” researchers said. “For whatever reasons, including non-financial motivation, lack of experience with ransomware or amateur coding skills, the MosesStaff group didn’t make as much of an effort.”


And indeed, CPR uncovered two options to potentially reverse the encryption, as detailed in the posting:


From there, it’s possible to plug these extracted keys into the boot login screen, unlocking the computer and restoring access to the operating system.


“They made an outright mistake when they put together their own encryption scheme, which is honestly a surprise in today’s landscape where every two-bit cybercriminal seems to know at least the basics of how to put together functioning ransomware,” according to CPR.


That said, “the disks remain encrypted and the DiskCryptor boot loader is active on every restart,” according to CPR. “This can be solved by creating a simple program that initiates proper IOCTL to the DiskCryptor driver, and eventually, removes it from the system.”


**Attribution**
---------------


When it comes to attribution, hard evidence is slim as to who’s behind MosesStaff. CPR researchers did see one of the tools used in the attack, OICe.exe, being submitted to VirusTotal from Palestine a few months before the attacks started.


“Although this is not a strong indication, it might betray the attackers’ origins; sometimes they test the tools in public services like VirusTotal to make sure they are stealthy enough,” researchers explained.


The other potential indicator involves the graphics used on the group’s website, moses-staff[.]se. According to the metadata of the images, these were all created in the time zone GMT+3, which is the time zone for Israel and Palestine.


To keep themselves protected, patching systems is a good place to start for organizations, CPR noted.


“MosesStaff has a specific modus operandi of exploiting vulnerabilities in public-facing servers, then using a combination of unique tools and living-off-the-land maneuvers to leave the targeted network encrypted, with encryption used solely for destruction purposes,” said CPR researchers. “The vulnerabilities exploited in the group’s attacks are not zero days, and therefore all potential victims can protect themselves by immediately patching all publicly-facing systems.”


***TOMORROW!! Want to win back control of the flimsy passwords standing between your network and the next cyberattack? Join Darren James, head of internal IT at Specops, and Roger Grimes, data-driven defense evangelist at KnowBe4, to find out how during a free, LIVE Threatpost event,*** [***“Password Reset: Claiming Control of Credentials to Stop Attacks,”***](https://bit.ly/3bBMX30) ***on Wed., Nov. 17 at 2 p.m. ET. Sponsored by Specops.***


[***Register NOW***](https://bit.ly/3bBMX30)***for the LIVE event!***




#### Tags:
[[CPR]] [[MosesStaff]] [[malware]] [[DiskCryptor]] [[ThreatPost]]
