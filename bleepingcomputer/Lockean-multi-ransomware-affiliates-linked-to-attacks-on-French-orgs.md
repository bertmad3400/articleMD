# Lockean multi-ransomware affiliates linked to attacks on French orgs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/lockean-multi-ransomware-affiliates-linked-to-attacks-on-french-orgs/)
+ Date: November 4, 2021
+ Author: Ionut Ilascu


## Article:
![Ransomware affiliate](https://www.bleepstatic.com/content/hl-images/2021/11/04/ransomware-affiliate-header.jpg)


Details about the tools and tactics used by a ransomware affiliate group, now tracked as Lockean, have emerged today in a report from France’s Computer Emergency Response Team (CERT).


Over the past year and a half, the threat actor has compromised the networks of at least eight French companies, stealing data and deploying malware from multiple ransomware-as-a-service (RaaS) operations.


### Multi-RaaS affiliation


Lockean activity was first noticed in 2020 when the actor hit a French company in the manufacturing sector and deployed DoppelPaymer ransomware on the network.


Between June 2020 and March 2021, Lockean attacked at least seven more companies with various ransomware families: Maze, Egregor, ProLock, REvil.


![Activity of the Lockean ransomware affiliate](https://www.bleepstatic.com/images/news/u/1100723/2021/Ransomware/Lockean_Activity.png)


Among compromised businesses are transport company Gefco, the Ouest-France newspaper, and the pharmaceutical companies Fareva and Pierre Fabre.


Four additional companies, unnamed by CERT-FR, were identified as victims of Lockean from reports to ANSSI, France’s national cybersecurity agency, and two incidents described by private organizations Intrinsec and The DFIR Report.


![Lockean ransomware affiliations](https://www.bleepstatic.com/images/news/u/1100723/2021/Ransomware/LockeanRaaS_affiliations.png)


In most of the attacks described in the [report](https://www.cert.ssi.gouv.fr/cti/CERTFR-2021-CTI-009/), the threat actor gained initial access to the victim network through Qbot/QakBot, a banking trojan that changed its role to distribute other malware, including ransomware strains ProLock, Egregor, and DoppelPaymer.


Qbot was spread through emails from the now-defunct Emotet botnet as well as a less known malware distribution service tracked as TA551, a.k.a. Shathak, UNC2420, and Gold Cabin.


In at least one known instance, Lockean used the IcedID malware distribution service to get access to the network.


![Lockean initial access via Qbot/QakBot](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


For lateral movement, the threat actor used the Cobalt Strike penetration testing framework, and the freely available Adfind, BloodHound, and BITSadmin tools.


CERT-FR notes in the report that Lockean’s average cut of paid ransoms was 70%, the rest going to the RaaS maintainers.


To increase the profit, the actor adopted the double-extortion model and stole data from the victim (via the Rclone tool) before encrypting the machines.


Under the threat of a data leak, which carries larger privacy and legal implications, victims were more likely to pay a negotiated ransom.


From start to finish, a typical Lockean intrusion would look as follows:


![Lockean group - infection chain](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


While CERT-FR’s data on Lockean’s tactics, techniques, and procedures is based on eight incidents, the group is likely more active than that and hit a larger number of companies.


Looking at the indicators of compromise in the report, Valery Marchive of LegMagIT [found](https://twitter.com/ValeryMarchive/status/1455862532497973252) several IP addresses related to Conti ransomware, indicating Lockean’s affiliation to additional RaaS operations and targeting of businesses in other regions.


Lockean is the second ransomware affiliate identified this year. In August, the FBI shared information about [OnePercent](https://www.bleepingcomputer.com/news/security/fbi-onepercent-group-ransomware-targeted-us-orgs-since-nov-2020/), an actor that has been hitting organizations in the U.S. with various ransomware strains.


Like Lockean, OnePercent is affiliated with multiple RaaS operations (Maze, Egregor, REvil) and stole data before deploying the file-encryption routine.




#### Tags:
[[ransomware]] [[Lockean]] [[malware]] [[Egregor,]] [[Lockean’s]] [[RaaS]] [[Bleeping Computer]]
