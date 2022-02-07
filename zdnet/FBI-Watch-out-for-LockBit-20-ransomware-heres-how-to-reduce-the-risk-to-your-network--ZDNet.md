# FBI: Watch out for LockBit 2.0 ransomware, here's how to reduce the risk to your network | ZDNet
### Turn on multi-factor authentication and use strong passwords, warns FBI.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/fbi-watch-out-for-lockbit-2-0-ransomware-heres-how-to-reduce-the-risk-to-your-network/
+ Date: 2022-02-07 13:01:25
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/13ae50dad19fad76a55ec6b4fa192d06429898b4/2021/09/27/11cf4ae8-38a8-4caa-8a94-b2652ec8bc61/fbi-decision-to-withhold-kaseya-ransomware.jpg?width=770&height=578&fit=crop&auto=webp)

The Federal Bureau of Investigations (FBI) has published a fresh warning about LockBit 2.0. recommending that companies enable multi-factor authentication (MFA) and use strong, unique passwords for all admin and high-value accounts to thwart the strain of ransomware that is used by one of [the busiest attack groups on the internet today](https://www.zdnet.com/article/ransomware-these-four-rising-threats-could-be-the-next-major-cybersecurity-risk-facing-your-business/).

MFA is vital to protecting against compromised user and admin passwords, but Microsoft has found that [78% of organizations using Azure Active Directory don't enable MFA](https://www.zdnet.com/article/strong-authentication-protects-against-phishing-so-why-arent-more-people-using-it/).  


LockBit 2.0 targets Windows PCs [and now Linux servers too](https://www.zdnet.com/article/this-sneaky-ransomware-is-now-targeting-linux-servers-too/) via bugs in VMWare's ESXi virtual machines, and has [hit tech consulting and services giant Accenture](https://www.zdnet.com/article/this-ransomware-has-returned-with-new-techniques-to-make-attacks-more-effective/) [and France's Ministry of Justice](https://www.zdnet.com/article/french-officials-investigating-lockbit-claim-of-ransomware-attack/) among others.

**SEE:** [**Cybersecurity: Let's get tactical**](https://www.zdnet.com/topic/cybersecurity-lets-get-tactical/#link=%7B%22linkText%22:%22Cybersecurity:%20Let's%20get%20tactical%20(ZDNet%20special%20report)%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/topic/cybersecurity-lets-get-tactical/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D%23link=%7B%22role%22:%22standard%22,%22href%22:%22https://www.zdnet.com/topic/cybersecurity-lets-get-tactical/%23link=%7B%22linkText%22:%22Cybersecurity:%20Let's%20get%20tactical%20(ZDNet%20special%20report)%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/topic/cybersecurity-lets-get-tactical/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D%22,%22target%22:%22%22,%22absolute%22:%22%22,%22linkText%22:%22%3Cstrong%3ECybersecurity:%20Let's%20get%20tactical%20(ZDNet%20special%20report%3C/strong%3E%22%7D) **(ZDNet special report)**

LockBit's operators use any method available to compromise a network, as long as it works. These include, but are not limited to, [buying access to an already compromised network from "access brokers](https://www.zdnet.com/article/log4j-flaw-now-state-backed-hackers-are-using-bug-as-part-of-attacks-warns-microsoft/)", exploiting unpatched software bugs, and even paying for insider access, as well as using exploits for previously unknown zero-day flaws, [according to the FBI's report](https://www.ic3.gov/Media/News/2022/220204.pdf). 

The group's techniques continue to evolve. The FBI says LockBit's operators have started advertising for insiders at a target company to help them establish initial access into the network. Insiders were promised a cut of the proceeds from a successful attack. A month earlier it began automatically encrypting devices across Windows domains by abusing group policies in Active Directory.   

After compromising a network, LockBit uses penetration-testing tools like Mimikatz to escalate privileges and use multiple tools to exfiltrate data (to threaten victims with a leak if they don't pay) before encrypting files. LockBit always leaves a ransom note with instructions for how to obtain the decryption key.   






Like other Russia-based ransomware operations, LockBit 2.0 determines the system and user language settings and excludes an organisation from attack if the languages are one of 13 Eastern European languages. The FBI lists the language codes in LockBit 2.0 as at February 2022 – such as 2092 for Azeri/Cyrillic and 1067 for Armenian – that cause it not to activate. 

"If an Eastern European language is detected, the program exits without infection," the FBI notes. 

Lockbit 2.0 identifies and collects an infected device's hostname, host configuration, domain information, local drive configuration, remote shares, and mounted external storage devices.

It then attempts to encrypt data saved to any local or remote device but skips files associated with core system functions, according to the FBI. After this, it deletes itself from the disk and creates persistence at startup.  

Besides requiring strong, unique passwords and MFA for webmail, VPNs and accounts for critical systems, the FBI also recommends a series of mitigations, including keeping operating systems and software up to date and removing unnecessary access to administrative shares. It also recommends using a host-based firewall and enabling "protected files" in Windows, referring to [Microsoft's controlled folder access](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-controlled-folders?view=o365-worldwide).   

It also recommends that companies segment their networks, investigate any abnormal activity, implement time-based access for accounts set at the admin level and higher, disable command-line and scripting activities and permissions, and – of course maintain – offline backups of data.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Mimikatz]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Armenia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.country.name=France]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Lockbit]] [[Windows]] [[ZDNet]]

