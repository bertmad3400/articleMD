# Arrests were made, but the Mekotio Trojan lives on
### Law enforcement cut off tails, but not the head of the cybercriminal operation.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/arrests-were-made-but-the-mekotio-trojan-lives-on/)
+ Date: November 3, 2021
+ Author: Charlie Osborne


## Article:
Unknown

Despite the arrest of individuals connected with the spread of the Mekotio banking Trojan, the malware continues to be used in new attacks. 


On Wednesday, Check Point Research (CPR) [published an analysis](https://blog.checkpoint.com/) on Mekotio, a modular banking Remote Access Trojan (RAT) that targets victims in Brazil, Chile, Mexico, Spain, and Peru -- and is now back with new tactics for avoiding detection. 

In October, law enforcement [made 16 arrests](http://www.interior.gob.es/prensa/noticias/-/asset_publisher/GHU8Ap6ztgsg/content/id/13552853) in relation to Mekotio and the Grandoreiro Trojans across Spain. The suspects allegedly sent thousands of phishing emails to distribute the Trojan, then used to steal banking and financial service credentials.  

Local media reports suggest that 276,470 euros were stolen, but transfer attempts -- thankfully, blocked -- worth 3,500,000 euros were made.  

CPR researchers Arie Olshtein and Abedalla Hadra say that the arrests only managed to disrupt distribution across Spain, and as the group likely collaborated with other criminal outfits, the malware continues to spread.  

Once the Spanish Civil Guard announced the arrests, Mekotio's developers, suspected of being located in Brazil, rapidly rehashed their malware with new features designed to avoid detection.  

Mekotio's infection vector has stayed the same, in which phishing emails either contain links to or have a malicious .ZIP archive attached that contains the payload. However, an analysis of over 100 attacks taking place in recent months has revealed the use of a simple obfuscation method and a substitution cipher to circumvent detection by antivirus products.  






In addition, the developers have included a batch file redesigned with multiple layers of obfuscation, a new PowerShell script that runs in memory to perform malicious actions, and the use of Themida -- a legitimate application to prevent cracking or reverse engineering -- to protect the final Trojan payload.  

Once installed on a vulnerable machine, Mekotio will attempt to exfiltrate access credentials for banks and financial services and will transfer them to a command-and-control (C2) server controlled by its operators.  

"One of the characteristics of those bankers, such as Mekotio, is the modular attack which gives the attackers the ability to change only a small part of the whole in order to avoid detection," the researchers say. "CPR sees a lot of old malicious code used for a long time, and yet the attacks manage to stay under the radar of AVs and EDR solutions by changing packers or obfuscation techniques such as a substitution cipher." 

###  Previous and related coverage

* [Meet Janeleiro: a new banking Trojan striking company, government targets](https://www.zdnet.com/article/meet-janeleiro-a-new-banking-trojan-striking-corporate-targets/)
* [Bizarro banking Trojan surges across Europe](https://www.zdnet.com/article/bizarro-banking-trojan-surges-across-europe/)
* [Banking Trojan evolves from distribution through porn to phishing schemes](https://www.zdnet.com/article/banking-trojan-evolves-from-distribution-through-porn-to-sophisticated-phishing-schemes/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Mekotio]] [[malware]] [[phishing]] [[ZDNet]]
