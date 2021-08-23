# FBI: OnePercent Group Ransomware targeted US orgs since Nov 2020
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/fbi-onepercent-group-ransomware-targeted-us-orgs-since-nov-2020/)
+ Date: August 23, 2021
+ Author: Sergiu Gatlan


## Article:
![FBI: OnePercent Group Ransomware targeted US orgs since Nov 2020](https://www.bleepstatic.com/content/hl-images/2021/05/17/FBI.jpg)


The Federal Bureau of Investigation (FBI) has shared info about a threat actor known as OnePercent Group that has been actively targeting US organizations in ransomware attacks since at least November 2020.


The US federal law enforcement agency shared indicators of compromise, tactics, techniques, and procedures (TTP), and mitigation measures in a flash alert published on Monday.


"The FBI has learned of a cyber-criminal group who self identifies as the 'OnePercent Group' and who have used Cobalt Strike to perpetuate ransomware attacks against US companies since November 2020," the FBI [said](https://www.documentcloud.org/documents/21047946-onepercent-group-ransomware-bc-flash-alert).


"OnePercent Group actors encrypt the data and exfiltrate it from the victims’ systems. The actors contact the victims via telephone and email, threatening to release the stolen data through The Onion Router (TOR) network and clearnet, unless a ransom is paid in virtual currency."


Victims' networks breached via phishing
---------------------------------------


The threat actors use malicious phishing email attachments that drop IcedID banking trojan payload on targets' systems. After infecting them with the trojan, the attackers download and install Cobalt Strike on compromised endpoints for lateral movement throughout the victims' networks.


After maintaining access to their victims' networks for up to one month and exfiltrating files before deploying the ransomware payloads, OnePercent will encrypt files using a random eight-character extension (e.g., dZCqciA) and will add uniquely named ransom notes linking to the gang's .onion website.


Victims can use the Tor website to get more info on the demanded ransom, negotiate with the attackers, and get "technical support.'


Victims will be asked to pay the ransom in bitcoins in most cases, with a decryption key provided up to 48 hours after the payment is made.


Applications and services used by the OnePercent Group operators include AWS S3 cloud, IcedID, Cobalt Strike, Powershell, Rclone, Mimikatz, SharpKatz, BetterSafetyKatz, SharpSploit.


Victims threatened via phone calls
----------------------------------


According to the FBI, OnePercent Group threat actors will also reach out to their victims using spoofed phone numbers, threatening to leak the stolen data unless they're connected with a company negotiator.


"Once the ransomware is successfully deployed, the victim will start to receive phone calls through spoofed phone numbers with ransom demands and are provided a ProtonMail email address for further communication," the FBI added.


"The actors will persistently demand to speak with a victim company’s designated negotiator or otherwise threaten to publish the stolen data.


"When a victim company does not respond, the actors send subsequent threats to publish the victim company’s stolen data via the same ProtonMail email address."


While the FBI hasn't provided any information on OnePercent Group's past attacks, two of the command-and-control servers mentioned in FBI's IOC list (golddisco[.]top and june85[.]cyou) also shows up on [FireEye's report on the UNC2198 threat actor](https://www.fireeye.com/blog/threat-research/2021/02/melting-unc2198-icedid-to-ransomware-operations.html) who ICEDID to deploy Maze and Egregor ransomware.


The same IOCs were also mentioned in a [Team Cymru report from May 2021](https://team-cymru.com/blog/2021/05/19/tracking-bokbot-infrastructure/) on mapping active IcedID network infrastructure.




#### Tags:
[[OnePercent]] [[ransomware]] [[Bleeping Computer]]
