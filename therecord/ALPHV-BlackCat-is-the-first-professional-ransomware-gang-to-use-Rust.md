# ALPHV (BlackCat) is the first professional ransomware gang to use Rust
### Security researchers have discovered this week the first professional ransomware strain that was coded in the Rust programming language and was deployed against companies in real-world attacks.

## Information:
+ Source: The Record
+ Link: https://therecord.media/alphv-blackcat-is-the-first-professional-ransomware-gang-to-use-rust/
+ Date: 2021-12-09T16:31:11+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2021/12/BlackCat.jpg)

* A new Ransomware-as-a-Service named ALPHV is currently being advertised on two underground forums.
* ALPHV, also known as BlackCat, is the first professional ransomware group to use Rust.
* The ransomware has made less than 10 victims so far.


**Security researchers have discovered this week the first professional ransomware strain that was coded in the Rust programming language and was deployed against companies in real-world attacks.**


Discovered by security researchers from Recorded Future and MalwareHunterTeam, the ransomware is named **ALPHV**(or **BlackCat**).


The ransomware is technically the third ransomware strain written in Rust after a [proof-of-concept strain](https://github.com/cdong1012/Rust-Ransomware) was released on GitHub in 2020 and an experimental and now-defunct strain named [BadBeeTeam](https://id-ransomware.blogspot.com/2020/09/badbeeteam-ransomware.html) was also seen later in the same year.


But while they were first, ALPHV (BlackCat) is the first one to be created and deployed in the wild by what looks to be a professional cybercrime cartel.


### ALPHV (BlackCat) is advertised on underground forums


In a [threat actor profile](https://support.recordedfuture.com/hc/en-us/articles/4412359150739?__hstc=156209188.d25ee89468395607cc54536ba1fc910f.1639069247099.1639069247099.1639069247099.1&__hssc=156209188.1.1639069247099&__hsfp=2041467688) published today, Recorded Future analysts said they believe the ALPHV (BlackCat) author was previously involved with the infamous REvil ransomware cartel in some sort of capacity.


Following REvil’s model, since early December, this individual—also going by the name of ALPHV—has been advertising a Ransomware-as-a-Service (RaaS) of the same name on two underground cybercrime forums (XSS and Exploit), inviting others to join and launch attacks against large companies to extract ransom payments they can then divide. Those who apply, known as “affiliates,” receive a version of the ALPHV (BlackCat) ransomware they can use in attacks.


Among the features they advertise is the ability to encrypt data on Windows, Linux, and VMWare eSXI systems, and the ability for “affiliates” to earn between 80% and 90% of the final ransom, depending on the total sum they extract from victims.


![](https://therecord.media/wp-content/uploads/2021/12/BlackCat-forum-1.png)Image: Recorded Future
At the time of writing, the ALPHV (BlackCat) gang appears to be in its early stages of operations and [MalwareHunterTeam](https://twitter.com/malwrhunterteam) has told *The Record* that only a handful of victims have been identified so far.


The BlackCat gang’s preferred initial entry vector is currently unknown, but once they breach a network, they search and steal sensitive files and then encrypt local systems.


In tune with the tactics of most major ransomware operations today, the group also engages in double-extortion, where they use the stolen data to put pressure on victims to pay, threatening to leak the stolen data if they don’t.


![BlackCat-ransom](https://therecord.media/wp-content/uploads/2021/12/BlackCat-ransom.png)BlackCat/ALPHV ransom note (Image: MalwareHunterTeam)
Right now, the group seems to be operating multiple leak sites, with each of these hosting the data of one or two victims, with ALPHV (BlackCat) creating a new one to use in new attacks. A screenshot of one of these sites is below.


A theory is that these leak sites are currently being hosted by the ALPHV (BlackCat) affiliates themselves, which explains the different leak URLs.


![BlackCat-leak-site](https://therecord.media/wp-content/uploads/2021/12/BlackCat-leak-site-1024x411.png)BlackCat (ALPHV) leak site (Image: The Record)
### Malware world slowly moving to Rust


While there have been some other tentative attempts at creating ransomware in Rust last year, BlackCat is the first one that is an actual threat and which companies need to be wary of.


In a [tweet](https://twitter.com/demonslay335/status/1468735840033677318) yesterday, Michael Gillespie, a malware analyst at Emsisoft and the author of tens of ransomware decryption utilities, has described BlackCat as “very sophisticated.”


However, BlackCat is not the only professional malware operation to move to Rust, considered a much secure programming language compared to C and C++.


Other cybercrime groups, such as the operators of [BuerLoader](https://www.proofpoint.com/us/blog/threat-insight/new-variant-buer-loader-written-rust) and [FickerStealer](https://www.cyberark.com/resources/threat-research-blog/fickerstealer-a-new-rust-player-in-the-market), have also made the first steps in 2021 towards deploying Rust versions of their tools.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=REvil]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Alphv]] [[(blackcat)]] [[Blackcat]] [[Cybercrime]] [[The Record]]

