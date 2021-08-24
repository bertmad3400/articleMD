# FBI sends its first-ever alert about a ‘ransomware affiliate’
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/fbi-sends-its-first-ever-alert-about-a-ransomware-affiliate/)
+ Date: August 23, 2021
+ Author: Catalin Cimpanu


## Article:
![FBI sends its first-ever alert about a ‘ransomware affiliate’](https://therecord.media/wp-content/uploads/2021/08/FBI-flash-OnePercent.jpg)

The US Federal Bureau of Investigations has published today its first-ever public advisory detailing the modus operandi of a “ransomware affiliate.”


A relatively new term, a ransomware affiliate refers to a person or group who rents access to Ransomware-as-a-Service (RaaS) platforms, orchestrates intrusions into corporate networks, encrypt files with the “rented ransomware,” and then earn a commission from successful extortions.


Going by the name of **OnePercent Group**, the FBI said today this threat actor has been active since at least November 2020.


Per the FBI report [[PDF](https://www.ic3.gov/Media/News/2021/210823.pdf)], historically, the group has primarily relied on the following tactics for its attacks:


* Used phishing email campaigns to infect victims with the IcedID trojan.
* Used the IcedID trojan to deploy additional payloads on infected networks.
* Used the Cobalt Strike penetration testing framework to move laterally across a victim’s network.
* Used RClone to exfiltrate sensitive data from a victim’s servers.
* Encrypted data and demanded a ransom.
* Phoned or emailed victims to threaten to sell their stolen data on the dark web if they didn’t pay on time.


### How the OnePercent Group got its name


The FBI said the group gained its name thanks to its well-structured extortion technique, which would go through different stages:


1. After gaining access to a victim network, the OnePercent Group would leave a ransom note stating the data has been encrypted and exfiltrated to a remote server.
2. If the victim didn’t follow the instructions in the ransom note and contact the gang, the group would follow up with threats to leak their data. These threats would be made via email or telephone ([a known technique](https://www.zdnet.com/article/ransomware-gangs-are-now-cold-calling-victims-if-they-restore-from-backups-without-paying/)).
3. If victims didn’t pay fast enough, the group would **leak 1%** of the stolen data as a warning for the victim — hence their name.
4. If victims still didn’t want to pay, the group would threaten to sell a victim’s data in [a section of the REvil leak site dedicated to data auctions](https://www.zdnet.com/article/revil-ransomware-gang-launches-auction-site-to-sell-stolen-data/).


### OnePercent is a known REvil, Maze, and Egregor affiliate


While the FBI did not specifically name the group as a ransomware affiliate, sources in the cybersecurity industry have told *The Record* that OnePercent had a long-standing collaboration with the creators and operators of the REvil (Sodinokibi) ransomware and have also worked with the Maze and Egregor operations.


“The attribution was clear,” Bill Siegel, founder and CEO of security firm Coveware, told *The Record*. “Victims that did not pay ended up on The REvil Happy Blog.”


![REvil-leak-site](https://www-therecord.recfut.com/wp-content/uploads/2021/08/REvil-leak-site.png)Image: Catalin Cimpanu
In addition, domain names included in the FBI advisory and which have been used by the OnePercent Group in the past to host their IcedID trojan have also been linked to [ransomware attacks that deployed the Maze and Egregor strains](https://www.fireeye.com/blog/threat-research/2021/02/melting-unc2198-icedid-to-ransomware-operations.html), per a FireEye report where the group appears to be tracked as UNC2198.


All in all, the FBI security advisory published today is an important step in clarifying how the cybercrime ecosystem actually works.


While security firms and news outlets often call and ransomware attacks and gangs by the ransomware strain they deployed, the reality is that almost all of these attacks are typically carried out by third parties who rent access to a RaaS—and not the ransomware creators themselves.


These “affiliate” groups often jump from one RaaS platform to another and will often deploy a ransomware strain that’s known to be able to bypass security solutions installed inside a specific corporate network, known to work faster, or the strain from a RaaS platform with the better commissions at a given point in time.


While the FBI did not say if the OnePercent group is still active today, the chances are that they still are, even if the REvil, Maze, and Egregor RaaS platforms have all shut down over the past few months.





#### Tags:
[[ransomware]] [[OnePercent]] [[didn’t]] [[Egregor]] [[IcedID]] [[victim’s]] [[REvil]] [[RaaS]] [[The Record]]
