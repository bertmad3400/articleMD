# Angry Conti ransomware affiliate leaks gang's attack playbook
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/angry-conti-ransomware-affiliate-leaks-gangs-attack-playbook/)
+ Date: August 5, 2021
+ Author: Lawrence Abrams


## Article:
![Angry face](https://www.bleepstatic.com/content/hl-images/2021/08/05/angry-face.jpg)


A disgruntled Conti affiliate has leaked the gang's training material when conducting attacks, including information about one of the ransomware's operators.


The Conti Ransomware operation is run as a ransomware-as-a-service (RaaS), where the core team manages the malware and Tor sites, while recruited affiliates perform network breaches and encrypt devices.


As part of this arrangement, the core team earns 20-30% of a ransom payment, while the affiliates earn the rest.


Today, a security researcher shared a forum post created by an angry Conti affiliate who publicly leaked information about the ransomware operation. This information includes the IP addresses for Cobalt Strike C2 servers and a 113 MB archive containing numerous tools and training material for conducting ransomware attacks.



![Forum post from disgruntled affiliate](https://www.bleepstatic.com/images/news/ransomware/c/conti/leaked-playbook/forum-post.jpg)**Forum post from disgruntled affiliate**
The affiliate said they posted the material as he was only paid $1,500 as part of an attack, while the rest of the team are making millions and promising big payouts after a victim pays a ransom.


"I merge you their ip-address of cobalt servers and type of training materials. 1500 $ yes, of course, they recruit suckers and divide the money among themselves, and the boys are fed with what they will let them know when the victim pays," the affiliate posted to a popular Russian-speaking hacking forum.


Attached to the above post are images of Cobalt Strike beacon configurations that contain the IP addresses for command and control servers used by the ransomware gang.


In a tweet by security researcher Pancak3, it is advised that everyone block those IP addresses to prevent attacks from the group.




> 
> go block these  
> 
> 162.244.80.235  
> 
> 85.93.88.165  
> 
> 185.141.63.120  
> 
> 82.118.21.1
> 
> 
> — pancak3 (@pancak3lullz) [August 5, 2021](https://twitter.com/pancak3lullz/status/1423324601346629635?ref_src=twsrc%5Etfw)


In a subsequent post, the affiliate shared an archive containing 111 MB of files, including hacking tools, manuals written in Russian, training material, and help documents that are allegedly provided to affiliates when performing Conti ransomware attacks.


A security researcher shared a screenshot of this extracted folder with BleepingComputer. We were told it contains a manual on deploying Cobalt Strike, mimikatz to dump NTLM hashes, and numerous other text files filled with various commands.



![Leaked Conti traning materials](https://www.bleepstatic.com/images/news/ransomware/c/conti/leaked-playbook/folder-listing.jpg)**Leaked Conti traning materials**
Advanced Intel's Vitali Kremez, who had already analyzed the archive, told BleepingCompter that the training material matches active Conti cases.


"We can confirm based on our active cases. This playbook matches the active cases for Conti as we see right now," Kremez told BleepingComputer in a conversation.


"By and large, it is the holy grail of the pentester operation behind the Conti ransomware "pentester" team from A-Z. The implications are huge and allow new pentester ransomware operators to level up their pentester skills for ransomware step by step."


"The leak also shows the maturity of their ransomware organization and how sophisticated, meticulous and experienced they are while targeting corporations worldwide."


"It also provides a plethora detection opportunities including the group focus on AnyDesk persistence and Atera security software agent persistence to survive detections."


This leak illustrates the vulnerability of ransomware-as-a-service operations, as a singly unhappy affiliate could lead to the exposure of carefully cultivated information and resources used in attacks.


Recently the United States government announced that its Rewards for Justice program is now accepting tips on foreign malicious cyberactivity against U.S. critical infrastructure, with a potential [$10 million reward for helpful information](https://www.bleepingcomputer.com/news/security/us-govt-offers-10-million-reward-for-tips-on-nation-state-hackers/).


Additionally, rewards through this program may be done anonymously in cryptocurrency, which could incentivize low-paid affiliates to turn on other cybercriminals.




#### Tags:
[[ransomware]] [[Conti]] [[IP]] [[attacks.]] [[pentester]] [[Bleeping Computer]]
