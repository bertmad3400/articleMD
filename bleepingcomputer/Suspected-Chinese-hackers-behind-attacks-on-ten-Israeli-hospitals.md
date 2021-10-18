# Suspected Chinese hackers behind attacks on ten Israeli hospitals
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/suspected-chinese-hackers-behind-attacks-on-ten-israeli-hospitals/)
+ Date: October 18, 2021
+ Author: Bill Toulas


## Article:
![hospital ward](https://www.bleepstatic.com/content/hl-images/2021/10/18/hospital_ward.jpg?rand=2137062659)


A joint announcement from the Ministry of Health and the National Cyber Directorate in Israel describes a spike in ransomware attacks over the weekend that targeted the systems of nine health institutes in the country.


In the [joint announcement](http://www.gov.il/he/departments/news/17102021), the Israeli government states that the attempts resulted in no damage to the hospitals and the medical organizations, thanks to national-level coordination and the quick and decisive response of the local IT teams.


The two authorities had carried out numerous defensive activities in the health sector to identify open vulnerabilities and secure them before the weekend arrived, mostly in response to [a Wednesday attack](http://hy.health.gov.il/eng/?CategoryID=23&ArticleID=891) on the Hillel Yaffe Medical Center. 


As it seems, though, these efforts weren't enough to secure the exposed endpoints, and some healthcare organizations were still breached over the weekend.


Fingers point to Chinese hackers
--------------------------------


According to [local media reports](https://www.ynetnews.com/business/article/hy5mghyby), the attack is attributed to a Chinese group of actors using the 'DeepBlueMagic' ransomware strain, which first appeared in the wild [in August this year](https://heimdalsecurity.com/blog/deepbluemagic-new-ransomware-discovered/).


DeepBlueMagin is known to disable security solutions that usually detect and block file encryption attempts, allowing for successful attacks.


Testing the IOCs shared by the authorities, BleepingComputer determined that the threat actors are using the 'BestCrypt' hard drive encryption tool to encrypt devices.



![BestCrypt used for the encryption of the files](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/bestcrypt.png)BestCrypt used for the encryption of the files
Israel's National Cyber Directorate has [released indicators of compromise](http://www.gov.il/he/departments/publications/reports/alert_1389) (IOCs) in the form of file hashes that have been seen in related attacks.


The agency suggests that Israeli organizations perform the following steps:


1. Review the IOCs in the CSV file and check if they have been observed in their environment.
2. Perform an active scan of all systems and include the file hashes in the organization's AV/EDR solutions.
3. Make sure all VPN and email servers are upgraded to the latest version to resolve any vulnerabilities that threat actors can use to gain access to internal networks.
4. If servers are not up to date, update them and perform password resets for all users.
5. Increase monitoring for unusual events in the corporate networks.
6. Report any breaches or unusual activity to the Israeli Israel National Cyber Directorate.


Hille Yaffe still struggling
----------------------------


In the meantime, the Hillel Yaffe Medical Center in the north of Tel Aviv is still struggling with restoring its systems, and the staff is using "pen a paper" to admit patients and circulate exams for the sixth day now.


Reuven Eliyahu, the cybersecurity chief in the Health Ministry, [has confirmed](https://www.timesofisrael.com/top-cyber-official-hospital-attack-purely-financial-likely-by-chinese-group/) that the mid-week attack was carried out by Chinese hackers in a statement today and described the actors' motives as "purely financial."


Even though there's hope that the Hillel Yaffe Medical Center will return to normal operations in a few days, there are fears that some medical records will be [unrecoverable](https://www.timesofisrael.com/officials-said-to-fear-some-medical-records-lost-forever-in-hospital-cyberattack/).


This is because the ransomware actors reportedly accessed the backup system, wiping all copies stored there for emergency cases like cyberattacks.


As for the ransom payment, the Hillel Yaffa center is a government-owned hospital, and as such, it won't even negotiate with hackers.




#### Tags:
[[Yaffe]] [[ransomware]] [[Bleeping Computer]]
