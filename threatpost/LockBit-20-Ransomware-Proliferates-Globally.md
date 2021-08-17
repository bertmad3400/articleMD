# LockBit 2.0 Ransomware Proliferates Globally
### Fresh attacks target companies’ employees, promising millions of dollars in exchange for valid account credentials for initial access.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168746)
+ Date: August 17, 2021  12:44 pm
+ Author: Tara Seals


## Article:
The LockBit ransomware-as-a-service (RaaS) gang has ramped up its targeted attacks, researchers said, with attempts against organizations in Chile, Italy, Taiwan and the U.K. using version 2.0 of its malware.


Attacks in July and August have employed LockBit 2.0, according to a Trend Micro analysis [released on Monday](https://www.trendmicro.com/en_us/research/21/h/lockbit-resurfaces-with-version-2-0-ransomware-detections-in-chi.html), featuring a souped-up encryption method.


“In contrast to LockBit’s attacks and features in 2019, this version includes automatic encryption of devices across Windows domains by abusing Active Directory (AD) group policies, prompting the group behind it to claim that it’s one of the fastest ransomware variants in the market today,” according to the report. “LockBit 2.0 prides itself on having one of the fastest and most efficient encryption methods in today’s ransomware threat landscape. Our analysis shows that while it uses a multithreaded approach in encryption, it also only partially encrypts the files, as only 4 KB of data are encrypted per file.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The attacks also feature an effort to recruit insider threats from within targeted companies, Trend Micro noted. The last step of the malware’s infection routine is to change the wallpaper on victim machines to what’s effectively an advertisement, with information on how organization insiders can be part of the “affiliate recruitment,” with guaranteed payouts of millions of dollars and anonymity in exchange for credentials and access, according to the report.


The fresh spate of attacks are employing the tactic “seemingly to remove middlemen (of other threat actor groups) and to enable faster attacks by providing valid credentials and access to corporate networks,” according to the researchers.


LockBit, it should be noted, recently made headlines as [the culprit behind](https://threatpost.com/accenture-lockbit-ransomware-attack/168594/) the Accenture cyberattack.


**LockBit 2.0 Infection Routine**
---------------------------------


For initial access to a targeted corporate network, the LockBit gang recruits affiliates and helpers as mentioned, who perform the actual intrusion on targets, usually via valid remote desktop protocol (RDP) account credentials. To help the cause, LockBit’s creators provide their partners with a handy [StealBit trojan](https://www.sophos.com/en-us/threat-center/threat-analyses/viruses-and-spyware/OSX~StealBit-A/detailed-analysis.aspx) variant, which is a tool for establishing access and automatically exfiltrating data.


The report pointed out that once in a system, LockBit 2.0 uses a panoply of tools to case the joint, as it were. A network scanner takes stock of the network structure and identifies target domain controllers. It also uses multiple batch files for various purposes, including terminating security tools, enabling RDP connections, clearing Windows Event logs, and making sure that crucial processes, such as Microsoft Exchange, MySQL and QuickBooks, are unavailable. It also stops Microsoft Exchange and disables other related services.


But that’s not all: “LockBit 2.0 also abuses legitimate tools such as Process Hacker and PC Hunter to terminate processes and services in the victim system.”


After this first stage, it’s time for lateral movement.


“Once in the domain controller, the ransomware creates new group policies and sends them to every device on the network,” Trend Micro researchers explained. “These policies disable Windows Defender, and distribute and execute the ransomware binary to each Windows machine.”


This main ransomware module goes on to append the “.lockbit” suffix to every encrypted file. Then, it drops a ransom note into every encrypted directory threatening [double extortion](https://threatpost.com/double-extortion-ransomware-attacks-spike/154818/); i.e., the note warns victims that files are encrypted and may be publicly published if they don’t pay up.


The final step for LockBit 2.0 is changing the victims’ desktop wallpapers into the aforementioned recruitment ad, which also includes instructions on how victims can pay the ransom.


**LockBit’s Continued Evolution**
---------------------------------


Trend Micro has been tracking LockBit over time, and noted that its operators initially worked with the Maze ransomware group, which shut down last October.


Maze was a pioneer in the double-extortion tactic, first emerging in November 2019. It went on to make waves with big strikes such as the [one against Cognizant](https://threatpost.com/maze-ransomware-cognizant/154957/). In summer 2020, it formed a cybercrime “cartel” – joining forces with various ransomware strains (including Egregor) and [sharing code, ideas and resources](https://threatpost.com/maze-ransomware-ragnar-locker-virtual-machine/159350/).


“After [Maze’s shutdown](https://threatpost.com/revil-video-game-hit-revenue/160743/), the LockBit group went on with its own leak site, which led to the development of LockBit,” researchers explained. “The previous version showed characteristics of ready-made ransomware using the double extortion techniques of encrypting files, stealing data and leaking the stolen data when the ransom was not paid.”


Now, LockBit 2.0 shows influences from Ryuk and Egregor, perhaps due to shared code DNA. Two notable examples flagged by Trend Micro are:


“We…assume that this group will continue to make a scene for a long time, especially since it’s currently recruiting affiliates and insiders, making it more capable of infecting many companies and industries,” Trend Micro researchers concluded. “It would also be wise to assume and prepare for upgrades and further developments in LockBit 2.0, especially now that many companies are aware of its capabilities and how it works.”


**How to Protect Organizations from Ransomware**
------------------------------------------------


The [Center of Internet Security](https://www.cisecurity.org/controls/) and the [National Institute of Standards and Technology](https://www.nist.gov/cyberframework) recommend the following best practices for preventing LockBit 2.0 and other malware infections:


![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/17123237/Best-Practices.png)


 




#### Tags:
[[LockBit]] [[ransomware]] [[Windows]] [[LockBit’s]] [[it’s]] [[ThreatPost]]
