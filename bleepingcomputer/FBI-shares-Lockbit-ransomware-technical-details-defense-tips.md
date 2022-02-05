# FBI shares Lockbit ransomware technical details, defense tips
### The Federal Bureau of Investigation (FBI) has released technical details and indicators of compromise associated with Lockbit ransomware attacks in a new flash alert published this Friday.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/fbi-shares-lockbit-ransomware-technical-details-defense-tips/
+ Date: 2022-02-05T10:00:00-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/07/27/Lockbit-1.jpg)

![LockBit ](https://www.bleepstatic.com/content/hl-images/2021/07/27/Lockbit-1.jpg)


The Federal Bureau of Investigation (FBI) has released technical details and indicators of compromise associated with LockBit ransomware attacks in a new flash alert published this Friday.


It also provided information to help organizations block this adversary's attempts to breach their networks and asked victims to urgently report such incidents to their local FBI Cyber Squad.


The [LockBit ransomware](https://www.bleepingcomputer.com/tag/LockBit/) gang has been very active since September 2019 when it launched as a ransomware-as-a-service (RaaS), with gang representatives promoting the operation, providing support on Russian-language hacking forums, and recruiting threat actors to breach and encrypt networks.


Two years later, in June 2021, LockBit announced [the LockBit 2.0 RaaS](https://twitter.com/Intel_by_KELA/status/1406905385580118017?s=20) on their data leak site after ransomware actors were banned from posting on cybercrime forums [[1](https://www.bleepingcomputer.com/news/security/ransomware-ads-now-also-banned-on-exploit-cybercrime-forum/), [2](https://www.bleepingcomputer.com/news/security/popular-russian-hacking-forum-xss-bans-all-ransomware-topics/)].


With the relaunch, the ransomware gang redesigned Tor sites and overhauled the malware, adding more advanced features, including the [automatic encryption of devices across Windows domains](https://www.bleepingcomputer.com/news/security/lockbit-ransomware-now-encrypts-windows-domains-using-group-policies/) via Active Directory group policies.


The gang is now also [trying to remove the intermediaries](https://www.bleepingcomputer.com/news/security/lockbit-ransomware-recruiting-insiders-to-breach-corporate-networks/) by recruiting insiders to provide them with access to corporate networks via Virtual Private Network (VPN) and Remote Desktop Protocol (RDP).


In January, it was discovered that [LockBit also added a Linux encryptor](https://www.bleepingcomputer.com/news/security/linux-version-of-lockbit-ransomware-targets-vmware-esxi-servers/) targeting VMware ESXi servers to its toolkit.


Among the technical details on how LockBit ransomware works, the FBI also revealed that the malware comes with a hidden debug window that can be activated during the infection process using the SHIFT + F1 keyboard shortcut.


Once it shows up, it can be used to view real-time information on the encryption process and trach the status of user data destruction.



![LockBit ransomware status window](https://www.bleepstatic.com/images/news/u/1109292/2022/Lockbit_ransomware_status_Window.jpg)*LockBit ransomware status window (FBI)*
This week's advisory follows an alert issued by the Australian cybersecurity agency in August 2021 [warning of quickly escalating LockBit ransomware attacks](https://www.bleepingcomputer.com/news/security/australian-govt-warns-of-escalating-lockbit-ransomware-attacks/).


Days later, Accenture, a Fortune 500 company and one of the world's largest IT services and consulting firms, [confirmed to BleepingComputer that it was breached](https://www.bleepingcomputer.com/news/security/accenture-confirms-hack-after-lockbit-ransomware-data-leak-threats/) after LockBit threatened to leak data stolen from its network and asked for a $50 million ransom.


Two months later, Accenture also disclosed a data breach in October SEC filings after "extraction of proprietary information" during the August attack.


Companies asked to report LockBit ransomware attacks
----------------------------------------------------


While the FBI didn't say what prompted this flash alert, it did ask admins and cybersecurity professionals to share information on LockBit attacks targeting their companies' networks.


"The FBI is seeking any information that can be shared, [including] boundary logs showing communication to and from foreign IP addresses, a sample ransom note, communications with the threat actors, Bitcoin wallet information, the decryptor file, and/or a benign sample of an encrypted file," the federal agency [said](https://www.ic3.gov/Media/News/2022/220204.pdf).


"The FBI encourages recipients of this document to report information concerning suspicious or criminal activity to their local FBI field office.


"By reporting any related information to FBI Cyber Squads, you are assisting in sharing information that allows the FBI to track malicious actors and coordinate with private industry and the United States Government to prevent future intrusions and attacks."


How to defend your network
--------------------------


The FBI also provides mitigations that would help defenders guard their networks against LockBit ransomware attack attempts:


* Require all accounts with password logins (e.g., service account, admin accounts, and domain admin accounts) to have strong, unique passwords
* Require multi-factor authentication for all services to the extent possible
* Keep all operating systems and software up to date
* Remove unnecessary access to administrative shares
* Use a host-based firewall to only allow connections to administrative shares via server message block (SMB) from a limited set of administrator machines
* Enable protected files in the Windows Operating System to prevent unauthorized changes to critical files.

Admins can also hinder ransomware operators' network discovery efforts by taking these measures:


* Segment networks to prevent the spread of ransomware
* Identify, detect, and investigate abnormal activity and potential traversal of the indicated ransomware with a networking monitoring tool
* Implement time-based access for accounts set at the admin level and higher
* Disable command-line and scripting activities and permissions
* Maintain offline backups of data, and regularly maintain backup and restoration
* Ensure all backup data is encrypted, immutable, and covers the entire organization’s data infrastructure

Paying ransoms is frowned upon, but ...
---------------------------------------


The FBI also added that it does not encourage paying ransoms and advises companies against it since it's not guaranteed that paying will protect them from future attacks or data leaks.


Moreover, giving into ransomware gangs' demands further finances their operations and motivates them to target more victims. It also incentivizes other cybercrime groups to join them in conducting illegal activities.


Despite this, the FBI acknowledged that a ransomware attack's fallout might force companies to consider paying ransoms to protect shareholders, customers, or employees. The law enforcement agency strongly recommends reporting such incidents to a [local FBI field office](https://www.fbi.gov/contact-us/field-offices).


Even after paying a ransom, the FBI still urges to promptly report ransomware incidents as it will provide critical info that would allow law enforcement to prevent future attacks by tracking ransomware attackers and holding them accountable for their actions.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Ransomware]] [[Lockbit]] [[Bleeping Computer]]

