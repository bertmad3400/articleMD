# Kaseya warns of phishing campaign pushing fake security updates
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/kaseya-warns-of-phishing-campaign-pushing-fake-security-updates/)
+ Date: July 9, 2021
+ Author: Sergiu Gatlan


## Article:
![Kaseya warns of phishing campaign pushing fake security updates](https://www.bleepstatic.com/content/hl-images/2021/07/05/Kaseya-headpic.jpg)


Kaseya has warned customers that an ongoing phishing campaign attempts to breach their networks by spamming emails bundling malicious attachments and embedded links posing as legitimate VSA security updates.


"Spammers are using the news about the Kaseya Incident to send out fake email notifications that appear to be Kaseya updates. These are phishing emails that may contain malicious links and/or attachments," the company [said](https://helpdesk.kaseya.com/hc/en-gb/articles/4403440684689) in an alert issued on Thursday evening.



**"Do not click on any links or download any attachments** claiming to be a Kaseya advisory. Moving forward, Kaseya email updates **will not contain any links or attachments**."


Attackers try to backdoor recipients' systems
---------------------------------------------


While the company did not provide additional details regarding these attacks, the warning perfectly lines up with another series of malspam emails targeting Kaseya customers with Cobalt Strike payloads.


As BleepingComputer first reported, Malwarebytes Threat Intelligence researchers have recently discovered a [series of phishing attacks](https://www.bleepingcomputer.com/news/security/fake-kaseya-vsa-security-update-backdoors-networks-with-cobalt-strike/) trying to take advantage of the ongoing Kaseya ransomware crisis.


"A malspam campaign is taking advantage of Kaseya VSA ransomware attack to drop CobaltStrike," Malwarebytes researchers said.


"It contains an attachment named 'SecurityUpdates.exe' as well as a link pretending to be security update from Microsoft to patch Kaseya vulnerability!"



![Kaseya phishing email sample (Malwarebytes)](https://www.bleepstatic.com/images/news/u/1109292/2021/Kaseya%20phishing.png)*Kaseya phishing email sample (Malwarebytes)*
The attackers' end goal is to deploy Cobal Strike beacons on the recipients' devices to backdoor them and steal sensitive info or deliver more malware payloads.


Once the targets run the malicious attachment or download and execute the fake Microsoft update on their devices, the attackers gain persistent remote access to the now compromised systems.


In June, following the Colonial Pipeline attack, [threat actors also used fake systems updates](https://www.bleepingcomputer.com/news/security/phishing-uses-colonial-pipeline-ransomware-lures-to-infect-victims/) claiming to help block ransomware infections.


These two campaigns highlight that cybercriminals behind phishing attacks keep up with the latest news to push lures relevant to recent events to boost their campaigns' success rates.


Given that Kaseya has so far [failed to deploy a fix for the VSA zero-day exploited by REvil](https://helpdesk.kaseya.com/hc/en-gb/articles/4403440684689), some of its customers might fall for this campaign's tricks in their effort to protect their networks from attacks.


Light at the end of the tunnel
------------------------------


The [highly-publicized REvil ransomware attack](https://www.bleepingcomputer.com/news/security/revil-ransomware-hits-1-000-plus-companies-in-msp-supply-chain-attack/) that hit Kaseya and [approximately 1,500 of their direct customers and downstream businesses](https://www.bleepingcomputer.com/news/security/kaseya-roughly-1-500-businesses-hit-by-revil-ransomware-attack/) makes for a perfect lure theme.


After the attack was disclosed, CISA and the FBI have [shared guidance](https://www.bleepingcomputer.com/news/security/cisa-fbi-share-guidance-for-victims-of-kaseya-ransomware-attack/) on how to deal with the attack's aftermath, and the White House National Security Council [is urging victims](https://www.whitehouse.gov/briefing-room/statements-releases/2021/07/04/statement-by-deputy-national-security-advisor-for-cyber-and-emerging-technology-anne-neuberger-on-reporting-kaseya-compromises/) to follow the guidance issued by Kaseya and report incidents to the FBI.


However, despite the attack's massive reach, which has led to some calling the largest ransomware attack ever, multiple victims told BleepingComputer that their backups were not affected, and they are [restoring systems rather than paying a ransom.](https://www.bleepingcomputer.com/news/security/revil-victims-are-refusing-to-pay-after-flawed-kaseya-ransomware-attack/)


Victims who do ultimately pay REvil's ransoms will likely only do so because their backups failed or they had no backups, to begin with.




#### Tags:
[[Kaseya]] [[phishing]] [[ransomware]] [[emails]] [[VSA]] [[Malwarebytes]] [[REvil]] [[Bleeping Computer]]
