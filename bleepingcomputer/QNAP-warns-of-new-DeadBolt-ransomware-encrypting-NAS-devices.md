# QNAP warns of new DeadBolt ransomware encrypting NAS devices
### QNAP is warning customers again to secure their Internet-exposed Network Attached Storage (NAS) devices to defend against ongoing and widespread attacks targeting their data with the new DeadBolt ransomware strain.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/qnap-warns-of-new-deadbolt-ransomware-encrypting-nas-devices/
+ Date: 2022-01-26T04:34:33-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/04/29/QNAP-headpic.jpg)

![QNAP ](https://www.bleepstatic.com/content/hl-images/2021/04/29/QNAP-headpic.jpg)


QNAP is warning customers again to secure their Internet-exposed Network Attached Storage (NAS) devices to defend against ongoing and widespread attacks targeting their data with the new DeadBolt ransomware strain.


"DeadBolt has been widely targeting all NAS exposed to the Internet without any protection and encrypting users’ data for Bitcoin ransom," [the company said](https://www.qnap.com/en/security-news/2022/take-immediate-actions-to-stop-your-nas-from-exposing-to-the-internet-and-fight-against-ransomware-together) in a statement issued today.


"Your NAS is exposed to the Internet and at high risk if there shows 'The System Administration service can be directly accessible from an external IP address via the following protocols: HTTP' on the dashboard."


All QNAP users are urged to "immediately update QTS to the latest available version" to block incoming DeadBolt ransomware attacks.


The NAS maker also advises customers to immediately disable Port Forwarding on their router and the UPnP function of the QNAP NAS using the following steps:


* **Disable the Port Forwarding function of the router:** Go to the management interface of your router, check the Virtual Server, NAT, or Port Forwarding settings, and disable the port forwarding setting of NAS management service port (port 8080 and 433 by default).
* **Disable the UPnP function of the QNAP NAS:** Go to myQNAPcloud on the QTS menu, click the "Auto Router Configuration," and unselect "Enable UPnP Port forwarding."

You can also use this [detailed step-by-step guide](https://www.qnap.com/en/security-advisory/nas-201911-01) to toggle off SSH and Telnet connections, change the system port number and device passwords, and enable IP and account access protection.


There is also a [DeadBolt ransomware support topic](https://www.bleepingcomputer.com/forums/t/767603/deadbolt-ransomware-support-topic-qnap-devices-deadbolt-extension/) on BleepingComputer's forum with more info on the attacks and with help from other QNAP users.


New DeadBolt ransomware surfaces
--------------------------------


As BleepingComputer reported yesterday, the [DeadBolt ransomware group started attacking QNAP users](https://www.bleepingcomputer.com/news/security/new-deadbolt-ransomware-targets-qnap-devices-asks-50-btc-for-master-key/) on January 25th, encrypting files on compromised NAS devices and appending a .deadbolt file extension.


The attackers are not dropping ransom notes on encrypted devices but, instead, they are hijacking the login pages to display warning screens saying "WARNING: Your files have been locked by DeadBolt."


The ransom screen asks the victims to pay 0.03 bitcoins (roughly $1,100) to a unique Bitcoin address generated for each victim, claiming that the decryption key will be sent to the same blockchain address in the OP\_RETURN field once the payment goes through.


At the moment, there are no confirmations that the threat actors will actually deliver on their promise to send a working decryption key after paying the ransom.



![DeadBolt ransom note and instructions](https://www.bleepstatic.com/images/news/u/1109292/2022/DeadBolt%20ransom%20note%20and%20instructions.jpg)*DeadBolt ransom note and instructions (BleepingComputer)*
These ongoing DeadBolt ransomware attacks only impact exposed NAS devices and, given that the attackers also claim to use a zero-day bug, it's advised to disconnect them from the Internet just as QNAP recommended in today's warning.


The DeadBolt gang is also [asking QNAP to pay 50 bitcoins](https://www.bleepstatic.com/images/news/ransomware/d/deadbolt/master-key-note.jpg) (around $1.85 million) for the zero-day and a master decryption key to decrypt files for all affected victims.


Today's warning is the third one QNAP issued to alert customers of ransomware attacks targeting their Internet-exposed NAS devices in the last 12 months.


They were previously warned of [eCh0raix ransomware](https://www.bleepingcomputer.com/news/security/qnap-warns-of-ech0raix-ransomware-attacks-roon-server-zero-day/) attacks in May and [AgeLocker ransomware](https://www.bleepingcomputer.com/news/security/qnap-warns-of-agelocker-ransomware-attacks-on-nas-devices/) attacks in April.


The company also [urged all QNAP NAS users to secure NAS devices exposed to Internet access](https://www.bleepingcomputer.com/news/security/qnap-warns-of-ransomware-targeting-internet-exposed-nas-devices/) on January 7th, at the same time alerting them of active ransomware and brute-force attacks.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Nas]] [[Qnap]] [[Ransomware]] [[Deadbolt]] [[Upnp]] [[Bleeping Computer]]

