# New DeadBolt ransomware targets QNAP devices, asks 50 BTC for master key
### A new DeadBolt ransomware group is encrypting QNAP NAS devices worldwide using what they claim is a zero-day vulnerability in the device's software.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/new-deadbolt-ransomware-targets-qnap-devices-asks-50-btc-for-master-key/
+ Date: 2022-01-25T19:28:37-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/25/Deadbolt_ransomware.jpg)

![DeadBolt ransomware](https://www.bleepstatic.com/content/hl-images/2022/01/25/Deadbolt_ransomware.jpg)


A new DeadBolt ransomware group is encrypting QNAP NAS devices worldwide using what they claim is a zero-day vulnerability in the device's software.


The attacks started today, January 25th, with QNAP devices suddenly finding their files encrypted and file names appended with a **.deadbolt**file extension.


Instead of creating ransom notes in each folder on the device, the QNAP device's login page is hijacked to display a screen stating, "WARNING: Your files have been locked by DeadBolt," as shown in the image below.



![Ransom note on hijacked QNAP login page](https://www.bleepstatic.com/images/news/ransomware/d/deadbolt/ransom-note-screen.jpg)**Ransom note on the hijacked QNAP login page**  
*Source: [Twitter](https://twitter.com/idobitom/status/1486065172598853635)*
This screen informs the victim that they should pay 0.03 bitcoins (approximately $1,100) to an enclosed Bitcoin address unique to each victim. After payment is made, the threat actors claim they will make a follow-up transaction to the same address that includes the decryption key.


This decryption key can then be entered into the screen to decrypt the device's files. At this time, there is no confirmation that paying a ransom will result in receiving a decryption key or that users will be able to decrypt files.


BleepingComputer is aware of at least fifteen victims of the new DeadBolt ransomware attack, with no specific region being targeted.


As with all ransomware attacks against QNAP devices, the DeadBolt attacks only affect devices accessible to the Internet.


As the threat actors claim the attack is conducted through a zero-day vulnerability, it is strongly advised that all QNAP users disconnect their devices from the Internet and place them behind a firewall.


With QNAP owners being targeted by ongoing attacks from two other ransomware families known as [Qlocker](https://www.bleepingcomputer.com/news/security/qlocker-ransomware-returns-to-target-qnap-nas-devices-worldwide/) and [eCh0raix](https://www.bleepingcomputer.com/news/security/ongoing-ech0raix-ransomware-campaign-targets-qnap-nas-devices/), all owners should follow [these steps](https://www.qnap.com/en/security-news/2022/take-immediate-actions-to-secure-qnap-nas) to prevent future attacks.


BleepingComputer has created a [DeadBolt ransomware support topic](https://www.bleepingcomputer.com/forums/t/767603/deadbolt-ransomware-support-topic-qnap-devices-deadbolt-extension/) that can be used to discuss the attacks and potentially receive help from other QNAP owners.


Attackers demand 50 bitcoin for master key
------------------------------------------


On the main ransom note screen, there is a link titled "important message for QNAP," that when clicked, will display a message from the DeadBolt gang specifically for QNAP.


On this screen, the DeadBolt ransomware gang is offering the full details of the alleged zero-day vulnerability if QNAP pays them 5 Bitcoins worth $184,000.


They are also willing to sell QNAP the master decryption key that can decrypt the files for all affected victims and the zero-day info for 50 bitcoins, or approximately $1.85 million.


"Make a bitcoin payment of 50 BTC to bc1qnju697uc83w5u3ykw7luujzupfyf82t6trlnd8," the threat actors wrote in a message to QNAP.


"You will receive a universal decryption master key (and instructions) that can be used to unlock all your clients their files. Additionally, we will also send you all details about the zero-day vulnerability to security@qnap.com."



![Message from threat actors for QNAP](https://www.bleepstatic.com/images/news/ransomware/d/deadbolt/master-key-note.jpg)**Message from threat actors for QNAP**  
*Source: [Twitter](https://twitter.com/news_wireless/status/1486045652652105733)*
The ransomware gang further states that there is no way to contact them other than through Bitcoin payments.


This method of communication is a very different approach than other ransomware attacks that usually provide some form of communication, whether through a dedicated Tor website, email, or messaging platforms.


BleepingComputer has contacted QNAP with questions about the DeadBolt attacks and will update the story with their response





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Qnap]] [[Deadbolt]] [[Ransomware]] [[Zero-day]] [[Bleepingcomputer]] [[Bleeping Computer]]
#### email-adresses
security@qnap.com

