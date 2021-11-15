# New Moses Staff group targets Israeli organizations in destructive attacks
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/new-moses-staff-group-targets-israeli-organizations-in-destructive-attacks/)
+ Date: November 15, 2021
+ Author: Catalin Cimpanu


## Article:
![New Moses Staff group targets Israeli organizations in destructive attacks](https://therecord.media/wp-content/uploads/2021/11/Moses-Staff.png)

A new hacking group named **Moses Staff** has attacked Israeli organizations, breached their networks, encrypted their data, but has then refused to negotiate ransom payments, in what security researchers are describing as politically-motivated destructive attacks.


First spotted in [early October 2021](https://twitter.com/campuscodi/status/1450455259202166799), the group is the third entity of its kind that has exclusively attacked Israeli organizations in recent months, after the [Pay2Key](https://attack.mitre.org/software/S0556/) and [Black Shadow](https://www.timesofisrael.com/black-shadow-hackers-leak-medical-records-of-290000-israeli-patients/) groups.


But according to a [report](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/) published today by Israeli security firm Check Point, Moses Staff behaves differently from the previous two.


Instead of trying to hide their attacks and subsequent data leaks as failed ransomware negotiations, Moses Staff openly admits that their intrusions are politically motivated.


According to a message posted on a website the group operates on the dark web, Moses Staff openly admits to targeting the Israeli Zionist regime in support of the occupied Palestine territories.


As a result, the group often encrypted and then leaked a victim’s data without even attempting to engage in a ransom negotiation process.


According to Check Point researchers, who have got a chance to investigate the group’s past attacks, Moses Staff operates using the following patterns:


* The group breaches victims’ networks by exploiting old vulnerabilities that have been left unpatched.
* Past intrusions have been linked to unpatched Microsoft Exchange servers.
* Once they breach a system, the group use tools like PsExec, WMIC, and Powershell to move deeper inside the victim’s network.
* The group then steals sensitive information from the victim’s network before encrypting its data.
* Moses Staff typically deploys the open-source [DiskCryptor](https://github.com/DavidXanatos/DiskCryptor) library to perform volume encryption and lock the victims’ computers with a bootloader that won’t allow the machines to boot without the correct password. Even if a correct password is provided, the data is still encrypted once the system boots.
* Check Point said that both the boot password and the encryption key could be recovered in certain circumstances.
* The hackers also operate a Telegram channel and Twitter account where they announce new victims they add to their leak site.


Check Point researchers declined to attribute the group to any specific country, lacking any concrete evidence; however, they did point out that some samples of the group’s malware had been submitted to the VirusTotal web malware scanner from Palestine IP addresses months before Moses Staff’s first attack.


So far, Moses Staff has listed 16 victims on their leak site. At the time of writing, the group is still active, having announced the Unit 8200 leak this past Saturday and a leak of a 3D image map of Israel allegedly obtained from the Israeli government itself on Sunday.


![Moses-Staff-website](https://www-therecord.recfut.com/wp-content/uploads/2021/11/Moses-Staff-website-1024x700.png)Image: The Record



#### Tags:
[[victim’s]] [[The Record]]
