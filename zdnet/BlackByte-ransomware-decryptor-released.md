# BlackByte ransomware decryptor released
### The "odd" malware avoids systems based on Russian and ex-USSR languages.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/blackbyte-ransomware-decryptor-released/)
+ Date: October 18, 2021
+ Author: Charlie Osborne


## Article:
Unknown

A new form of malware found in a recent IT incident appears to have been inspired by other strains known to reap their operators huge financial rewards -- but is likely the work of amateurs. 


Dubbed BlackByte and discovered by Trustwave, the Windows-based ransomware is considered "odd" due to some of the design and function decisions made by its creators.  

In a set of technical advisories published last week ([1](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/),[2](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-2-code-obfuscation-analysis/)), the cybersecurity firm says the malware only targets systems that are not based on Russian or ex-USSR languages -- a common trend in ransomware believed to be of Russian origin. 

BlackByte has also taken advantage of what has become known as [double-extortion](https://www.zdnet.com/article/black-hat-enterprise-players-face-one-two-punch-extortion-tactics-in-ransomware-attacks/) in this space: not only does malware encrypt and lock up systems, but victims are also then faced with the threat of confidential information being leaked or sold online.  

Modern ransomware operators, including Maze, ReEvil, Conti, and Babuk, run leak websites on the Dark Web for this purpose. BlackByte, too, has launched a website, but according to the researchers, the threat of data exfiltration and leaks is groundless -- as the ransomware does not appear to have this functionality in the first place. 

As a result, more victims may pay up after infection, even if there is no actual risk of information becoming public.  

BlackByte's encryption process also reveals that unskilled threat actors may be at work. The malware downloads and executes the same key to encrypt files in AES, rather than unique keys for each session, such as those usually employed by sophisticated ransomware operators.  






If the key cannot be downloaded from its HTTP server -- hidden in a file called forest.PNG -- the ransomware program simply crashes. An RSA key is used once, to encrypt the 'raw' key to show a ransom note.  

"To decrypt a file, one only needs the raw key to be downloaded from the host," Trustwave says. "As long as the .PNG file it downloaded remains the same, we can use the same key to decrypt the encrypted files." 

Aside from this odd encryption process, the malware utilizes a JavaScript launcher designed to decrypt the main .NET DLL payload.  

The ransomware is executed into memory and a victim ID is assigned using the vulnerable PC's processor ID and volume serial number, which are then hashed and pinged to the malware's command-and-control (C2) server. Any process which could prevent file encryption is terminated, and the SetThreadExecutionState API is used to stop the machine from entering a sleep state.  

In addition, volume shadow copies are wiped, Windows restore points are deleted, and network discovery is enabled. BlackByte also has worm-like capabilities similar to those employed by Ryuk and it will try to propagate itself across available networks.  

Trustwave has made a BlackByte decryptor available for download [at GitHub](https://github.com/SpiderLabs/BlackByteDecryptor). 

###  Previous and related coverage

* [New Python ransomware targets virtual machines, ESXi hypervisors to encrypt disks](https://www.zdnet.com/article/new-python-ransomware-targets-virtual-machines-esxi-hypervisor-to-encrypt-disks/)
* [$5.2 billion in BTC transactions tied to top 10 ransomware variants: US Treasury](https://www.zdnet.com/article/5-2-billion-in-btc-transactions-tied-to-top-10-ransomware-variants-us-treasury/)
* [This is the perfect ransomware victim, according to cybercriminals](https://www.zdnet.com/article/this-is-the-perfect-ransomware-victim-according-to-cybercriminals/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[ransomware]] [[malware]] [[BlackByte]] [[ZDNet]]
