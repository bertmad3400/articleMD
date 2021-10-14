# New Yanluowang ransomware used in targeted enterprise attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-yanluowang-ransomware-used-in-targeted-enterprise-attacks/)
+ Date: October 14, 2021
+ Author: Sergiu Gatlan


## Article:
![New Yanluowang ransomware used in targeted enterprise attacks](https://www.bleepstatic.com/content/hl-images/2021/10/13/Yanluowang_ransomware.jpg)


A new and still under development ransomware strain is being used in highly targeted attacks against enterprise entities as Broadcom's Symantec Threat Hunter Team discovered.


The malware, dubbed Yanluowang ransomware (after a Chinese deity [Yanluo Wang](https://en.wikipedia.org/wiki/Yanluo_Wang), one of the ten kings of hell) based on the extension it adds to encrypted files on compromised systems.


It was recently spotted while investigating an incident involving a high-profile organization after detecting suspicious activity involving the legitimate AdFind command line Active Directory query tool.


[AdFind](https://attack.mitre.org/software/S0552/) is commonly used by ransomware operators for reconnaisance tasks including gaining access to information needed for lateral movement through their victims' networks.


Victims warned not to ask for help
----------------------------------


Within days of the researchers spotting the suspicious AdFind use, the attackers also attempted to deploy their Yanluowang ransomware payloads across the breached organization's systems.


Before being deployed on compromised devices, the ransomware operators launch a malicious tool designed to carry out the following actions:


* Creates a .txt file with the number of remote machines to check in the command line
* Uses Windows Management Instrumentation (WMI) to get a list of processes running on the remote machines listed in the .txt file
* Logs all the processes and remote machine names to processes.txt


Once deployed, Yanluowang will stop hypervisor virtual machines, end all processes harvested by the precursor tool (including SQL and Veeam), encrypts files and appends the .yanluowang extension.


On encrypted systems, Yanluowang also drops a ransom note named README.txt that warns its victims not to reach out to law enforcement or ask ransomware negotiation firms for help.



![Yanluowang ransom note](https://www.bleepstatic.com/images/news/u/1109292/2021/Yanluowang_ransom_note.png)*Yanluowang ransom note (Broadcom Symantec Threat Hunter Team)*
Threats of DDoS attacks
-----------------------


"If the attackers' rules are broken the ransomware operators say they will conduct distributed denial of service (DDoS) attacks against the victim, as well as make 'calls to employees and business partners'," the Broadcom researchers added.


"The criminals also threaten to repeat the attack "in a few weeks" and delete the victim’s data," a common tactic used by most ransomware gangs to pressure their victims into paying the ransom.


Indicators of compromise including malware hashes can be found at the end of [Symantec Threat Hunter Team's report](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/yanluowang-targeted-ransomware).


Even though under development, the Yanluowang is still dangerous malware given that ransomware is one of the biggest threats organizations are facing worldwide.


The White House National Security Council facilitates this week a series of meetings between senior officials from over 30 countries in a [virtual international counter-ransomware event](https://www.bleepingcomputer.com/news/security/russia-and-china-left-out-of-global-anti-ransomware-meetings/) to join US efforts to crack down on ransomware cybercrime groups.


After the ransomware attacks on Colonial Pipeline and JBS this summer, Deputy National Security Advisor Anne Neuberger also told U.S. businesses [to take ransomware seriously](https://www.bleepingcomputer.com/news/security/white-house-urges-businesses-to-take-ransomware-crime-seriously/).




#### Tags:
[[ransomware]] [[Yanluowang]] [[Symantec]] [[AdFind]] [[Bleeping Computer]]
