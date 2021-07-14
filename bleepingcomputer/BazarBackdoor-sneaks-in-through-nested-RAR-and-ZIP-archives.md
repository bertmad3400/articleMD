# BazarBackdoor sneaks in through nested RAR and ZIP archives
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/bazarbackdoor-sneaks-in-through-nested-rar-and-zip-archives/)
+ Date: July 14, 2021
+ Author: Ionut Ilascu


## Article:
![Trickbot's BazarBacdoor delivered via the multi-compression method](https://www.bleepstatic.com/content/hl-images/2020/10/12/trojan-horse-chip.jpg)


Security researchers caught a new phishing campaign that tried to deliver the BazarBackdoor malware by using the multi-compression technique and masking it as an image file.


The multi-compression or nested archive method is not new but gained in popularity recently as it can trick email security gateways into mislabeling malicious attachments as clean.



It consists of placing an archive within another. Researchers at Cofense say that this method can bypass some secure email gateways (SEGs), which can have a limit to how deep they check a compressed file.


The new BazarBackdoor campaign deployed earlier this month and lured enterprise recipients with an “Environmental Day” theme, officially celebrated on June 5.


![Malspam delivering BazarBackdoor](https://www.bleepstatic.com/images/news/u/1100723/Malware/Trickbot/BazarBackdoorLure_Cofense.png)


Both attached nested ZIP and RAR archives in the attachment contained a JavaScript file that ultimately delivered Trickbot’s BazarBackdoor malware, a stealthy backdoor typically used on corporate targets to provide remote access to the threat actor.


Cofense analyzed the recent malspam campaign and found that the role of the highly obfuscated JavaScript file was to download a payload with an image extension.


![ZIP and RAR nested archives with BazarBackdoor payload](https://www.bleepstatic.com/images/news/u/1100723/Malware/Trickbot/BazarBackdoorJS_Cofense.jpg)


Cofense [explains](https://cofense.com/blog/nested-files-evade-segs/) that “nesting of various archive types is purposeful by the threat actor as it has the chance of hitting the SEG’s decompression limit or fails because of an unknown archive type.”


Obfuscated files can also pose problems to an SEG if there are several layers of encryption for the payload, increasing the chances of the malicious file passing undetected.


“Once executed, the obfuscated JavaScript would download a [BazarBackdoor] payload with a .png extension via an HTTP GET connection,” Cofense says, adding that the payload is an executable with the wrong extension.


Once deployed on a victim computer, BazarBackdoor may download and execute the Cobalt Strike, a legitimate toolkit designed for post-exploitation exercises, to spread laterally in the environment.


After gaining access to high-value systems on the network, threat actors can launch ransomware attacks, steal sensitive information, or sell the access to other cybercriminals.


Earlier this year, security researchers discovered a [BazarBackdoor variant written in the Nim](https://www.bleepingcomputer.com/news/security/trickbots-bazarbackdoor-malware-is-now-coded-in-nim-to-evade-antivirus/) programming language, showing the effort Trickbot developer goes to keep the malware undetected and relevant to cybercriminal activities.




#### Tags:
[[BazarBackdoor]] [[Cofense]] [[malware]] [[JavaScript]] [[Bleeping Computer]]
