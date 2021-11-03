# CERT-France: Lockean ransomware group behind attacks on French companies
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/cert-france-lockean-ransomware-group-behind-attacks-on-french-companies/)
+ Date: November 3, 2021
+ Author: Catalin Cimpanu


## Article:
![CERT-France: Lockean ransomware group behind attacks on French companies](https://therecord.media/wp-content/uploads/2021/11/hacker-keyboard-computer-cybercrime.jpg)

French cybersecurity officials have identified today for the first time a ransomware “affiliate group” that is responsible for a long list of attacks against French companies over the past two years.


Identified as **Lockean**, the group’s activities and modus operandi were detailed today in a [comprehensive report](https://www.cert.ssi.gouv.fr/cti/CERTFR-2021-CTI-009/) published by France’s Computer Emergency Response Team (CERT-FR), a division of ANSSI, the country’s national cybersecurity agency.


According to French officials, the group has been active since June 2020 and “has a propensity to target French entities,” having been linked to attacks on at least seven French companies, such as transportation logistics firm **Gefco**, pharmaceutical groups **Fareva**and **Pierre Fabre**, and local newspaper **Ouest-France**.


### Lockean operators used different ransomware strains


CERT-FR officials said the group would typically rent access to corporate networks that had been previously infected via Emotet phishing emails, where they would deploy the QakBot malware and later the CobaltStrike post-exploitation framework.


Lockean operators would then use tools like [AdFind](https://attack.mitre.org/software/S0552/), [BITSAdmin](https://attack.mitre.org/software/S0190/), and [BloodHound](https://attack.mitre.org/software/S0521/) to move laterally inside a network in order to expand their access and control over a company’s systems.


The group would then use the [RClone](https://rclone.org/) utility to copy sensitive files from the victim network and then deploy a file-encrypting ransomware strain.


![Lockean-chain](https://www-therecord.recfut.com/wp-content/uploads/2021/11/Lockean-chain.png)Image: CERT-FR
![Lockean-post-exploitation](https://www-therecord.recfut.com/wp-content/uploads/2021/11/Lockean-post-exploitation.png)Image: CERT-FR
According to CERT-FR officials, who investigated several of these intrusions, the Lockean group used different ransomware strains across the years, such as DoppelPaymer, Maze, Egregor, REvil (Sodinokibi), and ProLock.


![Lockean-RaaS](https://www-therecord.recfut.com/wp-content/uploads/2021/11/Lockean-RaaS.png)Image: CERT-FR
![Lockean-victims](https://www-therecord.recfut.com/wp-content/uploads/2021/11/Lockean-victims.png)Image: CERT-FR
### Second ransomware affiliate group identified


Because Lockean used different ransomware strains, officials believe the group is what security researchers call a “**ransomware affiliate**,” a term that refers to criminal groups who sign up on Ransomware-as-a-Service (RaaS) platforms.


Through these platforms, affiliates gain access to ready-to-deploy ransomware strains, which they deploy on hacked networks, splitting successful ransom payments with the ransomware’s creators.


If victims refused to pay, data from these companies would be published on so-called “leak sites” operated by the RaaS platforms, where victims would often be listed in order to ramp up public pressure on the hacked companies.


Lockean is now the second ransomware affiliate group that has been publicly identified by law enforcement agencies after the [FBI exposed the OnePercent group in August](https://therecord.media/fbi-sends-its-first-ever-alert-about-a-ransomware-affiliate/).





#### Tags:
[[ransomware]] [[CERT-FR]] [[Lockean]] [[Image:]] [[The Record]]
