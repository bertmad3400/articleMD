# Stealthier version of Mekotio banking trojan spotted in the wild
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/stealthier-version-of-mekotio-banking-trojan-spotted-in-the-wild/)
+ Date: November 3, 2021
+ Author: Bill Toulas


## Article:
![malware](https://www.bleepstatic.com/content/hl-images/2021/04/16/malware-phishing-header.jpg)


A new version of a banking trojan known as Mekotio is being deployed in the wild, with malware analysts reporting that it's using a new, stealthier infection flow.


The last notable activity of Mekotio dates back to [the summer of 2020](https://www.bleepingcomputer.com/news/security/mekotio-banking-trojan-imitates-update-alerts-to-steal-bitcoin/) when the trojan's operators deployed it in a campaign targeting Latin American countries.


The targeting scope appears to be the same in recent attacks, with Spanish being the language of choice for the phishing emails that start the infection chain.


A new attack flow
-----------------


The infection begins with a phishing email bundling a ZIP attachment containing an obfuscated batch script that fetches and executes a PowerShell script.


Once the PowerShell script gets launched, it will download a second ZIP archive after some basic location and anti-analysis checks.


If the checks confirm the victim is in Latin America and the malware isn't running on a virtual machine, the second ZIP, which contains the Mekotio payload in DLL form, is extracted.



![New attack flow diagram](https://www.bleepstatic.com/images/news/u/1220909/Security/attack%20flow.jpg)**New Mekotio attack flow diagram**  
*Source: CheckPoint*
Multi-step attack flows like the one above may appear unnecessarily complicated, but they're needed to evade detection and successfully deploy the final payload.


One of the advantages of modular attacks is the added ability to make subtle changes that render previous detection methods useless.


This is precisely the case in Mekotio's development, as the trojan's code has largely remained unchanged, with its authors mostly tweaking things instead of adding new capabilities.



![Phishing email used in recent Mekotio campaign](https://www.bleepstatic.com/images/news/u/1220909/Security/phishing%20email.jpg)**Phishing email used in recent Mekotio campaign**  
*Source: CheckPoint*
Same old code in new wrapping
-----------------------------


The three novel elements that make the latest Mekotio version harder to detect are the following:


* A stealthier batch file with at least two layers of obfuscation
* New file-less PowerShell script that runs directly in memory
* Use of Themida v3 for packing the final DLL payload


[CheckPoint reports](https://research.checkpoint.com/2021/mekotio-banker-returns-with-improved-stealth-and-ancient-encryption/) seeing approximately 100 attacks in the past three months deploying cipher substitution techniques, which albeit simple, help Mekotio go undetected by most AV products.


The second layer of obfuscation is slicing the PowerShell commands into parts saved in different environment variables and then concatenating the values during execution.



![Second layer of obfuscation on the PowerShell script](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Second layer of obfuscation on the PowerShell script**  
*Source: CheckPoint*
The trojan's primary goal remains to steal people's e-banking credentials and online account passwords.


Some past Mekotio variants could also hijack cryptocurrency payments and direct them to actor-controlled wallets, but recent versions have removed this functionality.


CheckPoint says the new campaign was launched right after the Spanish Civil Guard arrested 16 people in Mexico, linked with local Mekotio distribution.


However, the core Mekotio crew appears to be based in Brazil, and it's assumed that they are Mekotio's creators who are now selling it to other cybercriminals.


ESET [characterized this particular trojan as "chaotic"](https://www.welivesecurity.com/2020/08/13/mekotio-these-arent-the-security-updates-youre-looking-for/) last year due to the concurrent development that resulted in the simultaneous circulation of different variants.


That activity has now waned, and the most recent campaign uses the variant analyzed by CheckPoint.




#### Tags:
[[Mekotio]] [[PowerShell]] [[Bleeping Computer]]
