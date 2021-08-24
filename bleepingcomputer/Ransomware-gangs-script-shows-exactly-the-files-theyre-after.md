# Ransomware gang's script shows exactly the files they're after
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/ransomware-gangs-script-shows-exactly-the-files-theyre-after/)
+ Date: August 24, 2021
+ Author: Lawrence Abrams


## Article:
![Data](https://www.bleepstatic.com/content/hl-images/2021/08/24/database-header.jpg)


A PowerShell script used by the Pysa ransomware operation gives us a sneak peek at the types of data they attempt to steal during a cyberattack.


When ransomware gangs compromise a network, they usually start with limited access to a single device.


They then use various tools and exploits to steal other credentials used on the Windows domain or gain elevated privileges on different devices.


Once they gain access to a Windows domain controller, they search for and steal data on the network before encrypting devices.


The threat actors use this stolen data in two ways.


The first is to generate a ransom demand based on company revenue and whether they have insurance policies. The second is to scare the victims into paying a ransom because the gang will leak the data.


Searching for valuable data
---------------------------


Yesterday, [MalwareHunterTeam](https://twitter.com/malwrhunterteam) shared a PowerShell script with BleepingComputer used by the Pysa ransomware operation to search for and exfiltrate data from a server.


This script is designed to scan each drive for data folders whose names match certain strings on a device. If a folder matches the search criteria, the script will upload the folder's files to a remote drop server under the threat actor's control.


Of particular interest are the 123 keywords that the script searches for, which give us a glimpse into what the ransomware gang considers valuable.


As we would expect, the script seeks out files related to the companies financials or personal information, such as audit, banking information, login credentials, tax forms, student information, social security numbers, and SEC filings.


However, it also looks for more intriguing keywords that could be particularly harmful to a company if leaked, such as folders containing the words 'crime', 'investigation', 'fraud', 'bureau', 'federal', 'hidden', 'secret', 'illegal', and 'terror.'


The full list of 123 keywords targeted by the threat actors' script is listed in the table below.


It does not make sense to change your folder names, so they do not include these strings, as the threat actors will likely perform manual sweeps of data.


However, knowing what types of data a ransom gang is searching for gives you a better indication of how ransomware gangs will attempt to extort their victims.


Pysa is not the only one searching for particular files after breaching a network.


Earlier this month, an angry Conti affiliate leaked the training material for the ransomware operation.


This [training material told affiliates to immediately search for data](https://www.bleepingcomputer.com/news/security/conti-ransomware-prioritizes-revenue-and-cyberinsurance-data-theft/) containing the following keywords after they gained control of a Windows domain controller.


Once again, this illustrates how vital data theft is to a ransomware attack and how important it is to safeguard it adequately.




#### Tags:
[[ransomware]] [[Pysa]] [[Windows]] [[information,]] [[Bleeping Computer]]
