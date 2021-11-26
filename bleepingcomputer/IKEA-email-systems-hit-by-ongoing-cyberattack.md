# IKEA email systems hit by ongoing cyberattack
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/ikea-email-systems-hit-by-ongoing-cyberattack/)
+ Date: November 26, 2021
+ Author: Lawrence Abrams


## Article:
![IKEA](https://www.bleepstatic.com/content/hl-images/2021/11/26/IKEA_headpic.jpg)


IKEA is battling an ongoing cyberattack where threat actors are targeting employees in internal phishing attacks using stolen reply-chain emails.


A reply-chain email attack is when threat actors steal legitimate corporate email and then reply to them with links to malicious documents that install malware on recipients' devices.


As the reply-chain emails are legitimate emails from a company and are commonly sent from compromised email accounts and internal servers, recipients' will trust the email and be more likely to open the malicious documents.


IKEA dealing with an ongoing attack
-----------------------------------


In internal emails seen by BleepingComputer, IKEA is warning employees of an ongoing reply-chain phishing cyber-attack targeting internal mailboxes. These emails are also being sent from other compromised IKEA organizations and business partners.


"There is an ongoing cyber-attack that is targeting Inter IKEA mailboxes. Other IKEA organisations, suppliers, and business partners are compromised by the same attack and are further spreading malicious emails to persons in Inter IKEA," explained an internal email sent to IKEA employees and seen by BleepingComputer.


"This means that the attack can come via email from someone that you work with, from any external organisation, and as a reply to an already ongoing conversations. It is therefore difficult to detect, for which we ask you to be extra cautious."


IKEA IT teams warn employees that the reply-chain emails contain links with seven digits at the end and shared an example email, as shown below. In addition, employees are told not to open the emails, regardless of who sent them, and to report them to the IT department immediately.


Recipients are also told to tell the sender of the emails via Microsoft Teams chat to report the emails.



![Example phishing email sent to IKEA employees](https://www.bleepstatic.com/images/news/security/attacks/i/ikea-phishing-internal-server/ikea-internal-email-phishing.jpg)**Example phishing email sent to IKEA employees**
Threat actors have recently begun to [compromise internal Microsoft Exchange servers](https://www.bleepingcomputer.com/news/security/microsoft-exchange-servers-hacked-in-internal-reply-chain-attacks/) using the ProxyShell and ProxyLogin vulnerabilities to perform phishing attacks.


Once they gain access to a server, they use the internal Microsoft Exchange servers to perform reply-chain attacks against employees using stolen corporate emails.


As the emails are being sent from internal compromised servers and existing email chains, there is a higher level of trust that the emails are not malicious.


While IKEA has not responded to our emails about the attack and has not disclosed to employees whether internal servers were compromised, it appears that they are suffering from a similar attack.


Attack used to spread Emotet or Qbot trojan
-------------------------------------------


From the URLs shared in the redacted phishing email above, BleepingComputer has been able to identify the attack targeting IKEA.


When visiting these URLs, a browser will be redirected to a download called 'charts.zip' that contains a malicious Excel document. This attachment tells recipients to click the 'Enable Content' or 'Enable Editing' buttons to properly view it, as shown below.



![Excel attachment used in the phishing campaign](https://www.bleepstatic.com/images/news/security/attacks/i/ikea-phishing-internal-server/phishing-attachment.jpg)**Excel attachment used in the phishing campaign**
Once those buttons are clicked, malicious macros will be executed that download files named 'besta.ocx,' 'bestb.ocx,' and 'bestc.ocx' from a remote site and save them to the C:\Datop folder.


These OCX files are renamed DLLs and are executed using the regsvr32.exe command to install the malware payload.


Campaigns using this method [have been seen](https://twitter.com/Max_Mal_/status/1463909174279090185) installing the Qbot trojan (aka QakBot and Quakbot) and possibly Emotet based on a [VirusTotal submission](http://www.virustotal.com/gui/file/6558c29ec98005ea4100943c7ceddc2131b9ae15a88b3bf8850e36ec8d9f3473/detection) found by BleepingComputer.


The Qbot and Emotet trojans both lead to further network compromise and ultimately the deployment of ransomware on a breached network.


Due to the severity of these infections and the likely compromise of their Microsoft Exchange servers, IKEA is treating this security incident as a significant cyberattack that could potentially lead to a far more disruptive attack.




#### Tags:
[[IKEA]] [[emails]] [[phishing]] [[reply-chain]] [[Microsoft]] [[emails.]] [[Emotet]] [[Qbot]] [[Bleeping Computer]]
