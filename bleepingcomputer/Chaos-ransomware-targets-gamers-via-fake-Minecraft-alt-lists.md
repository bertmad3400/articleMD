# Chaos ransomware targets gamers via fake Minecraft alt lists
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/chaos-ransomware-targets-gamers-via-fake-minecraft-alt-lists/)
+ Date: October 30, 2021
+ Author: Bill Toulas


## Article:
![Minecraft villains](https://www.bleepstatic.com/content/hl-images/2021/10/29/minecraft-villains.jpg)


The Chaos Ransomware gang encrypts gamers' Windows devices through fake Minecraft alt lists promoted on gaming forums.


Minecraft is a massively popular sandbox video game currently played by over 140 million people, and according to Nintendo sales numbers, it's a top-seller title in Japan.


Masked as an 'alt list' text file
---------------------------------


According to researchers at [FortiGuard](https://www.fortinet.com/blog/threat-research/chaos-ransomware-variant-in-fake-minecraft-alt-list-brings-destruction), a recently discovered variant of the Chaos ransomware is being tentatively distributed in Japan, encrypting the files of Minecraft players and dropping ransom notes.


The lure used by the threat actors are 'alt list' text files that supposedly contain stolen Minecraft account credentials, but in reality, is Chaos ransomware executable.


Minecraft players who want to troll or grief other players without the risk of their accounts being banned will sometimes use 'alt' lists to find stolen accounts that they can use for bannable offenses.


Due to their popularity, alt lists are always in demand and are commonly shared for free or through automated account generators that supply the community with "spare" accounts.



![Alt list txt offered for free download](https://www.bleepstatic.com/images/news/u/1220909/ransomware/image%20(2).png)**Alt list txt offered for free download**
The Chaos Ransomware
--------------------


When encrypting victims, the Chaos ransomware will append four random characters or digits as the extension to encrypted files.


The ransomware will also drop a ransom note named 'ReadMe.txt,' where the threat actors demand 2,000 yen (~$17.56) in pre-paid cards.



![Ransom note dropped by Chaos](https://www.bleepstatic.com/images/news/u/1220909/ransomware/ransom.png)**Ransom note dropped by Chaos actors**  
*Source: FortiGuard*
A destructive infection
-----------------------


This particular variant of the Chaos Ransomware is configured to search the infected systems for different file types smaller than 2ΜΒ and encrypts them.


However, if the file is larger than 2MB is will inject random bytes into the files, making them unrecoverable even if a ransom is paid.


Due to the destructive nature of the attack, those who pay the ransom can only recover smaller files.


The reason for this functionality is unclear, and it could be caused by poor coding, incorrect configuration, or to damage gamers' files purposely.


In this particular campaign, the threat actors are promoting text files to create a false sense of security while swapping them out in the end with executables.


Users should be suspicious of and not execute any files they download from the Internet unless they trust the site and have scanned it with a tool like VirusTotal.




#### Tags:
[[Minecraft]] [[ransomware]] [[Ransomware]] [[Bleeping Computer]]
