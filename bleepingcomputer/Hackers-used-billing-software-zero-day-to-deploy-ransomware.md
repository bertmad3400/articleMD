# Hackers used billing software zero-day to deploy ransomware
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/hackers-used-billing-software-zero-day-to-deploy-ransomware/)
+ Date: October 25, 2021
+ Author: Sergiu Gatlan


## Article:
![Hackers used billing software zero-day to deploy ransomware](https://www.bleepstatic.com/content/posts/2021/10/25/BillQuick.jpg)


An unknown ransomware group is exploiting a critical SQL injection bug found in the BillQuick Web Suite time and billing solution to deploy ransomware on their targets' networks in ongoing attacks.


BQE Software, the company behind BillQuick, claims to have a 400,000 strong user base worldwide.


The vulnerability, tracked as [CVE-2021-42258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42258), can be triggered extremely easily via login requests with invalid characters (a single quote) in the username field, according to security researchers with the Huntress ThreatOps team.


This actively exploited vulnerability was patched on [October 7](http://billquick.net/download/Support_Download/BQWS2021Upgrade/WebSuite2021LogFile_9_1.pdf) after Huntress Labs notified BQE Software of the bug.


However, the researchers also found eight other BillQuick zero-day vulnerabilities (i.e., [CVE-2021-42344](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42344), [CVE-2021-42345](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42345), [CVE-2021-42346](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42456), [CVE-2021-42571](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42571), [CVE-2021-42572](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42572), [CVE-2021-42573](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42573), [CVE-2021-42741](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42741), [CVE-2021-42742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42742)) also usable for initial access/code execution and ripe for abuse since they're still waiting for a patch.


Unpatched BillQuick server used to hack engineering company
-----------------------------------------------------------


"Our team was able to successfully recreate this SQL injection-based attack and can confirm that hackers can use this to access customers' BillQuick data and run malicious commands on their on-premises Windows servers," [Huntress Labs said](https://www.huntress.com/blog/threat-advisory-hackers-are-exploiting-a-vulnerability-in-popular-billing-software-to-deploy-ransomware).


"We have been in close contact with the BQE team to notify them of this vulnerability, assess the code changes implemented in WebSuite 2021 version 22.0.9.1 and work to address multiple security concerns we raised over their BillQuick and Core offerings (more to come on these when patches are available)."


According to the researchers, since the attacks have begun, a U.S. engineering company already had its systems encrypted after a vulnerable BillQuick server was hacked and used as the initial point of access to its network.


"The actor we observed did not align with any known/large threat actor of which we are aware. It's my personal opinion this was a smaller actor and/or group based on their behavior during exploitation and post-exploitation," Huntress Labs security researcher Caleb Stewart told BleepingComputer.


"However, based on the issues we've identified/disclosed, I would expect further exploitation by others moving forward is likely. We observed the activity over Columbus Day weekend (08-10 October 2021)."


Active since at least May 2020
------------------------------


The ransomware gang behind these attacks is unknown, and its operators haven't dropped ransom notes on encrypted systems to make it easier to identify them or ask their victims to pay ransom in exchange for decryptors.


Also, it's not clear if the ransomware is used as a decoy to cover up other malicious activity, such as data theft, or if the victims are expected to know to email the threat actor from the extension appended to encrypted files.


BleepingComputer found that the ransomware deployed by this group has been in use since at least May 2020 and it heavily borrows code from other AutoIT-based ransomware families.


Once deployed on target systems, it will add the *pusheken91@bk.ru* extension to all encrypted files but, as mentioned above, BleepingComputer has not seen it drop a ransom note during any known attacks.



![Encrypted files](https://www.bleepstatic.com/images/news/u/1109292/2021/Encrypted%20files.jpg)*Image: [Michael Gillespie](http://twitterr.com/demonslay335)*
The attackers are likely using this approach because the appended extension itself hints at what email the victims have to use to ask for details on how to recover their data.


In August, [the FBI and CISA warned organizations](https://www.bleepingcomputer.com/news/security/fbi-cisa-ransomware-attack-risk-increases-on-holidays-weekends/) not to let down their defenses against ransomware attacks during weekends or holidays in a joint cybersecurity advisory.


The two federal government agencies said they "observed an increase in highly impactful ransomware attacks occurring on holidays and weekends—when offices are normally closed—in the United States, as recently as the Fourth of July holiday in 2021."




#### Tags:
[[ransomware]] [[BillQuick]] [[BQE]] [[Bleeping Computer]]
