# Security team finds Crimea manifesto buried in VBA Rat using double attack vectors
### The Malwarebytes report said a new threat actor may be targeting Russian and pro-Russian individuals.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/security-team-finds-crimea-manifesto-buried-in-vba-rat-using-double-attack-vectors/)
+ Date: July 29, 2021 -- 21:28 GMT (22:28 BST)
+ Author: Jonathan Greig


## Article:
Unknown

Hossein Jazi and Malwarebytes' Threat Intelligence team [released a report](https://blog.malwarebytes.com/threat-intelligence/2021/07/crimea-manifesto-deploys-vba-rat-using-double-attack-vectors/) on Thursday highlighting a new threat actor potentially targeting Russian and pro-Russian individuals.

The attackers included a manifesto about Crimea, indicating the attack may have been politically motivated. The attacks feature a suspicious document named "Manifest.docx" that uniquely downloads and executes double attack vectors: remote template injection and [CVE-2021-26411](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26411), an Internet Explorer exploit. 

"Both techniques have been loaded by malicious documents using the template injection technique. The first template contains a url to download a remote template that has an embedded full-featured VBA Rat. This Rat has several different capabilities including downloading, uploading and executing files," Jazi said. 

"The second template is a an exploit for CVE-2021-26411 which executes a shell-code to deploy the same VBA Rat. The VBA Rat is not obfuscated but still has used some interesting techniques for shell-code injection."

Jazi attributed the attack to the [ongoing conflict between Russian and Ukraine](https://www.cnet.com/news/russian-hackers-reportedly-hit-ukrainian-gas-firm-at-heart-of-trump-impeachment/), part of which centers on Crimea. The report notes that cyberattacks on both sides [have been increasing](https://www.cnet.com/news/us-charges-russian-hackers-over-3-of-worlds-biggest-cyberattacks/). 

But Jazi does note that the manifesto and Crimea information may be used as a false flag by the threat actors. 

Malwarebytes' Threat Intelligence team discovered the "Манифест.docx" ("Manifest.docx") on July 21, finding that it downloads and executes the two templates: one is macro-enabled and the other is an html object that contains an Internet Explorer exploit.






The analysts found that the exploitation of CVE-2021-26411 resembled an attack launched by the [Lazarus APT](https://www.zdnet.com/article/lazarus-state-hacking-group-now-hides-payloads-in-bmp-image-files/). 

According to the report, the attackers combined social engineering and the exploit in order to increase their chances of infecting victims. 

Malwarebytes was not able to attribute the attack to a specific actor, but said that a decoy document was displayed to victims that contained a statement from a group associating with a figure named Andrey Sergeevich Portyko, who allegedly opposes Russian President Vladimir Putin's policies on the Crimean Peninsula. 

Jazi explained that the decoy document is loaded after the remote templates are loaded. The document is in Russian but is also translated into English. 

The attack also features a VBA Rat that collects victim's info, identifies the AV product running on victim's machine, executes shell-codes, deletes files, uploads and downloads files while also reading disk and file systems information.

Jazi noted that instead of using well known API calls for shell code execution which can easily get flagged by AV products, the threat actor used the distinctive EnumWindows to execute its shell-code.





#### Tags:
[[Jazi]] [[VBA]] [[Malwarebytes]] [[ZDNet]]
