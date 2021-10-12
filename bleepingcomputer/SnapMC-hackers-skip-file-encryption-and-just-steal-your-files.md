# SnapMC hackers skip file encryption and just steal your files
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/snapmc-hackers-skip-file-encryption-and-just-steal-your-files/)
+ Date: October 12, 2021
+ Author: Bill Toulas


## Article:
![hacker remote access](https://www.bleepstatic.com/content/hl-images/2021/02/08/hacker-accessing-remotely.jpg?rand=1830552086)


A new actor tracked as SnapMC has emerged in the cybercrime space, performing the typical data-stealing extortion that underpins ransomware operations, but without doing the file encryption part.


File encryption is considered a core component of ransomware attacks, as it's the very element that brings operational disruption to the victim.


Data exfiltration for purposes of double extortion came later as an additional form of leverage against a victim, but always took a back seat to the mayhem caused by an encrypted network


Soon, [ransomware actors realized](https://www.bleepingcomputer.com/news/security/babuk-quits-ransomware-encryption-focuses-on-data-theft-extortion/) the power of this approach as many companies could restore the corrupted files from backups, but couldn’t possibly revert the file-stealing event and its consequences.


Researchers at NCC Group have been tracking a new adversary which they call SnapMC, named after the rapid strike approach the group follows, who enter networks, steal files, and deliver extortion emails in under 30 minutes.


Targeting known vulnerabilities
-------------------------------


The SnapMC gang uses the Acunetix vulnerability scanner to find a range of flaws in a target’s VPN and web server apps, and then successfully exploits them to breach the corporate network.


The most exploited flaws observed in the actor’s initial access efforts include the [PrintNightmare LPE](https://github.com/calebstewart/CVE-2021-1675), remote code execution in [Telerik UI for ASPX.NET](https://github.com/noperator/CVE-2019-18935), and also various SQL injection opportunities.


The actors use SQL database exportation scripts to steal the data, while the CSV files are compressed with the 7zip archive utility prior to exfiltration. Once everything is neatly packed, the MinIO client is used for sending the data back to the attacker.


Considering that SnapMC leverages known vulnerabilities that have already been patched, updating your software tools would be a good way to defend against this rising threat


As [NCC Group](https://research.nccgroup.com/2021/10/11/snapmc-skips-ransomware-steals-data/) points out in its report, even if an organization uses a vulnerable version of Telerik, putting it behind a well-configured Web Application Firewall would render any exploitation efforts futile.


Paying is risky
---------------


In data exfiltration extortion attacks, meeting the threat actor's demands by paying a ransomware, guarantees nothing. On the contrary, it could give the hackers an incentive to attempt further extortion in the future.


It is also possible that even if a victim pays a ransom, their data may end up sold on criminal marketplaces or hacker forums as an additional way of generating revenue for the attackers.


Ransomware negotiation firm Coveware, strongly advises its clients [never to pay a ransom](https://www.bleepingcomputer.com/news/security/scam-psa-ransomware-gangs-dont-always-delete-stolen-data-when-paid/) to prevent stolen files from being leaked to the public.


During negotiation cases in the past, victims have paid a ransom and their data was stll leaked or no proof of deletion was ever provided.


* Sodinokibi: Victims that paid were re-extorted weeks later with threats to post the same data set.
* Netwalker: Data posted of companies that had paid for it not to be leaked
* Mespinoza: Data posted of companies that had paid for it not to be leaked
* Conti: Fake files are shown as proof of deletion


Due to this, victims should automatically assume that their data has been shared with other threat actors and that it will be used or leaked in the future, regardless of whether they paid a ransom.




#### Tags:
[[SnapMC]] [[ransomware]] [[Bleeping Computer]]
