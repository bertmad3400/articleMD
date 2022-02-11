# Hacking group 'ModifiedElephant' evaded discovery for a decade
### Threat analysts have linked a decade of activity to an APT (advanced persistent threat) actor called 'ModifiedElephant', who has managed to remain elusive to all threat intelligence firms since 2012.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/hacking-group-modifiedelephant-evaded-discovery-for-a-decade/
+ Date: 2022-02-10 20:02:17+00:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/04/elephant.jpg)

![APT actor 'ModifiedElephant' remained in the shadow for a decade](https://www.bleepstatic.com/content/hl-images/2022/01/04/elephant.jpg?rand=1529398727)


For a decade, an advanced persistent threat (APT) actor tracked as ModifiedElephant has been using tactics that allowed it to operate in utmost secrecy, without cybersecurity companies connecting the dots between attacks.


This particular group of hackers employs readily-available trojans through spear-phishing, and has been targeting human rights activists, free speech defenders, academics, and lawyers in India since 2012.


The malicious emails push keyloggers and remote access trojans like NetWire and DarkComet, and even Android malware.


Researchers at SentinelLabs in a report today detail the tactics of ModifiedElephant explaining how recently published evidence helped them attribute previously "orphan" attacks.


The most reliable evidence is overlapping infrastructure observed in multiple campaigns between 2013 and 2019, as well as consistency in the malware deployed.



![ModifiedElephant C2 infrastructure](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/timeline(4).jpg)**ModifiedElephant C2 infrastructure** *(SentinelLabs)*
Past campaigns
--------------


ModifiedElephant has relied on spear-phishing emails with malicious attachments for over a decade now, but their techniques have evolved throughout that time.


Below is an overview of their past operations highlighting some evolution milestones:


* 2013 – actor uses email attachments with [fake double extensions](https://web.archive.org/web/20210226131047/https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2013/NS-Unveiling-an-Indian-Cyberattack-Infrastructure_FINAL_Web.pdf) (file.pdf.exe) to drop malware
* 2015 – group moves to password-protected RAR attachments containing legitimate lure documents that overlay the signs of malware execution
* 2019 – ModifiedElephant starts hosting malware-dropping sites and [abuses cloud hosting services](http://www.amnesty.org/en/latest/research/2020/06/india-human-rights-defenders-targeted-by-a-coordinated-spyware-operation/), switching from fake documents to malicious links
* 2020 – attackers use large-size RAR files (300 MB) to evade detection by skipping scans

On multiple occasions, the attached documents leveraged known exploits for malware execution, including CVE-2012-0158, CVE-2013-3906, CVE-2014-1761, and CVE-2015-1641.


As for the lures used in these campaigns, they were all politically related and often highly tailored for the target.



![Sample email sent by ModifiedElephant](https://www.bleepstatic.com/images/news/u/1220909/Phishing/email(2).jpg)**Sample email sent by ModifiedElephant** *(SentinelLabs)*
"The phishing emails take many approaches to gain the appearance of legitimacy," [explains SentinelLabs in the report](https://www.sentinelone.com/labs/modifiedelephant-apt-and-a-decade-of-fabricating-evidence/)



"This includes fake body content with a forwarding history containing long lists of recipients, original email recipient lists with many seemingly fake accounts, or simply resending their malware multiple times using new emails or lure documents."



Attacker's toolkit
------------------


ModifiedElephant hasn't been observed using any custom backdoors throughout its operational record, so the particular group doesn't appear to be very sophisticated.


The primary malware deployed on the campaigns are NetWire and DarkComet, two remote access trojans that are publicly available and widely used by lower-tier cybercriminals.


The Visual Basic keylogger used by ModifiedElephant has remained the same since 2012, and it's been freely available on hacking forums all these years. SentinelLabs comments on the antiquity of the tool, highlighting that it doesn't even work on modern OS versions anymore.


The Android malware is also a commodity trojan, delivered to victims in the form of an APK, tricking them into installing it themselves by posing as a news app or a safe messaging tool.


A state actor?
--------------


The SentinelLabs report makes several correlations between the timing of specific ModifiedElephant attacks and the arrest of targets that followed shortly after.


This coincidence, combined with the targeting scope, which aligns with the interests of the Indian state, constructs a very probable hypothesis that the hackers are sponsored by circles of India's official administration.


Freedom of speech activists and academics aren't targeted for financial purposes, so these attacks always have an underlying political nuance.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Circles]] [[action.malware.name=DarkComet]] [[action.malware.name=Net]] [[action.malware.name=NETWIRE]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Modifiedelephant]] [[Malware]] [[Emails]] [[Sentinellabs]] [[Bleeping Computer]]
#### CVE's
[[CVE-2012-0158]] [[CVE-2013-3906]] [[CVE-2014-1761]] [[CVE-2015-1641]]

