# REVil ransomware devs added a backdoor to cheat affiliates
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/revil-ransomware-devs-added-a-backdoor-to-cheat-affiliates/)
+ Date: September 23, 2021
+ Author: Ionut Ilascu


## Article:
![REvil ransomware admins pose as non-paying victims to trick affiliates](https://www.bleepstatic.com/content/hl-images/2020/06/02/REvil1.jpg)


Cybercriminals are slowly realizing that the REvil ransomware operators may have been hijacking ransom negotiations, to cut affiliates out of payments.


By using a cryptographic scheme that allowed them to decrypt any systems locked by REvil ransomware, the operators left their partners out of the deal and stole the entire ransom.


Conversations about this practice started a while ago on underground forums, in posts from collaborators of the gang, and have been confirmed recently by security researchers and by malware developers.


REvil ransomware, also known as Sodinokibi, emerged in the first half of 2019 and built a reputation as a [successor of the GandCrab](https://www.bleepingcomputer.com/news/security/shared-code-links-sodinokibi-to-gandcrab-minus-the-fun-and-games/) ransomware-as-a-service (RaaS) operation.


The RaaS cybercriminal business model involves a developer, who creates the ransomware malware and sets up the infrastructure, and affiliates recruited to breach and encrypt victims. The proceedings are divided between the two parties with affiliates taking the larger cut (typically 70-80%). 


Promoted by veterans of underground forums, the REvil gang developed a [highly lucrative](https://www.bleepingcomputer.com/news/security/a-look-inside-the-highly-profitable-sodinokibi-ransomware-business/) private operation that accepted only experienced network hackers.


### REvil name goes down the drain


If the REvil operation started as an “honest” cybercriminal endeavor, it soon switched to scamming affiliates out of the promised 70% share of a ransom from paying victims.


[Yelisey Boguslavskiy](https://twitter.com/y_advintel), head of research at Advanced Intel, told BleepingComputer that since at least 2020 various actors on underground forums claimed that the RaaS operators were taking over negotiations with victims in secret chats, unbeknownst to affiliates.


The rumor became more frequent after the sudden [shut down of DarkSide](https://www.bleepingcomputer.com/news/security/darkside-ransomware-servers-reportedly-seized-operation-shuts-down/) ransomware and [Avaddon’s exit](https://www.bleepingcomputer.com/news/security/avaddon-ransomware-shuts-down-and-releases-decryption-keys/) by releasing the decryption keys for their victims.


The conversations involved individuals that played a role in REvil ransomware attacks, such as partners that provided network access, penetration-testing services, VPN specialists, and potential affiliates.


[Boguslavskiy](https://twitter.com/y_advintel) says that REvil admins have been opening a second chat, identical to the one used by their affiliate to negotiate a ransom with the victim.


When talks reached a critical point, REvil would take over by posing as the victim quitting the negotiations without paying the ransom, Boguslavskiy explained to BleepingComputer.


The gang would continue the talks with the victim and obtain the full ransom with the affiliate being none the wiser.


Recently, these claims got more substance as an underground malware reverse engineer provided evidence of REvil’s double-dipping practices. They talk of a “cryptobackdoor” in the REvil samples that RaaS operators gave affiliates to deploy on victim networks.


The author’s revelation comes after cybersecurity company Bitdefender released a [universal REvil decryption tool](https://www.bleepingcomputer.com/news/security/free-revil-ransomware-master-decrypter-released-for-past-victims/) that works for all victims encrypted up to July 13, 2021.



![REvil called out for using secondary decryption to cheat affiliates](https://www.bleepstatic.com/images/news/u/1100723/Ransomware/Sodinokibi%20(REvil)/REvilCryptoBackdoor.jpg)source: [Advanced Intel](https://www.advintel.io/)
Public key in the image above:


What the author of the above post is saying is that affiliates were not the only ones that could decrypt the systems they locked with the REvil ransomware sample they received.


REvil operators had a master key they could use to restore encrypted files.


### Researcher revealed the trick in July


[Fabian Wosar](https://twitter.com/fwosar), “ransomware slayer” par excellence and chief technology officer at Emsisoft, in early July provided a clear explanation for how REvil’s cryptographic scheme worked.


GandCrab’s successor uses in their malware four sets of public-private keys responsible for the encryption and decryption tasks:


1. An operator/master pair that has the public part hardcoded in all REvil samples
2. A campaign pair, whose public part is stored in the configuration file of the malware as a PK value
3. A system-specific pair - generated upon encrypting the machine, with the private part encrypted using both the public master and campaign keys
4. A key pair generated for each encrypted file



“The private file key and public system key are then used as inputs for ECDH using Curve25519 in order to generate the Salsa20 key (called a shared secret) that is being used to actually encrypt the file content,” [Wosar explains](https://twitter.com/fwosar/status/1411281336065794049).



The system private key is essential to unlocking a machine because it is the only one required to decrypt individual files. Recovering it is possible with either the master private key - available only to REvil operators, or the campaign key that affiliates have.


Wosar notes that the master private key is REvil’s insurance against rogue affiliates, allowing them to decrypt any victim. This is also what Bitdefender used for their [REvil decryption tool](https://download.bitdefender.com/am/malware_removal/BDREvilDecryptor.exe) and likely what helped [Kaseya victims recover files](https://www.bleepingcomputer.com/news/security/kaseya-obtains-universal-decryptor-for-revil-ransomware-victims/) for free.


To access the REvil payment portal, the ransomware threat actor requires a blob of data present in the ransom note. That string of apparently nonsensical characters includes various data about the machine, campaign, version of the malware used, and the system private key.



![Info present in REvil key blob for payment portal](https://www.bleepstatic.com/images/news/u/1100723/Ransomware/Sodinokibi%20(REvil)/REvilDataBlob.jpg)source: [Fabian Wosar](https://twitter.com/fwosar/status/1411297199879823366)
Keeping an ace up their sleeve that gives ransomware operators total control over decrypting any system locked by their malware is a practice seen with other, newer ransomware groups.


Boguslavskiy says that the DarkSide ransomware gang was rumored to run their operation in the same way.


After [rebranding as BlackMatter](https://www.bleepingcomputer.com/news/security/darkside-ransomware-gang-returns-as-new-blackmatter-operation/), the actor was open about this practice, letting everybody know that they reserved their right to take over the negotiations at any point, without explaining.


Reverse engineer and Advanced Intelligence CEO Vitali Kremez told BleepingComputer that the latest REvil samples, which emerged when the gang restarted operations, no longer have the master key that enabled the decryption of any system locked with REvil ransomware.




#### Tags:
[[REvil]] [[ransomware]] [[malware]] [[RaaS]] [[victims.]] [[Boguslavskiy]] [[REvil’s]] [[Wosar]] [[Bleeping Computer]]
