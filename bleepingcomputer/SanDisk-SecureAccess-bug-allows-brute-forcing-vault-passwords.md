# SanDisk SecureAccess bug allows brute forcing vault passwords
### Western Digital has fixed a security vulnerability that enabled attackers to brute force SanDisk SecureAccess passwords and access the users' protected files.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/sandisk-secureaccess-bug-allows-brute-forcing-vault-passwords/
+ Date: 2021-12-09T08:40:09-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/09/Western_Digital.jpg)

![SanDisk SecureAccess bug allows brute forcing vault passwordsSanDisk SecureAccess bug allows brute forcing vault passwords](https://www.bleepstatic.com/content/hl-images/2021/12/09/Western_Digital.jpg)


Western Digital has fixed a security vulnerability that enabled attackers to brute force SanDisk SecureAccess passwords and access the users' protected files.


SanDisk SecureAccess (now rebranded to [SanDisk PrivateAccess](https://kb.sandisk.com/app/answers/detail/a_id/21996)) allows storing and protecting sensitive files on SanDisk USB flash drives.


"SanDisk SecureAccess 3.02 was using a one-way cryptographic hash with a predictable salt making it vulnerable to dictionary attacks by a malicious user," Western Digital explained in a security advisory issued Wednesday.


"The software also made use of a password hash with insufficient computational effort that would allow an attacker to brute force user passwords leading to unauthorized access to user data."


The flaw ([CVE-2021-36750](https://nvd.nist.gov/vuln/detail/cve-2021-36750)) stemming from the key derivation function issues presented above has been addressed with the release of SanDisk PrivateAccess Version 6.3.5, which now uses PBKDF2-SHA256 together with a randomly generated salt.


How to upgrade to PrivateAccess Vault
-------------------------------------


You can find detailed information [here](https://kb.sandisk.com/app/answers/detail/a_id/23775) on upgrading your installation and migrating the SecureAccess Vault to the new PrivateAccess Vault.


This requires updating the iXpand Drive mobile app and the Windows and macOS Desktop to the latest released versions.


"We urge our customers to install this software update immediately to keep their vaults secure," Western Digital [added](https://www.westerndigital.com/support/product-security/wdc-21014-sandisk-secureaccess-software-update).


"As with any upgrade, it is best to back up your data before installing the upgrade. Back up your data using the built-in Backup function in the Tools menu."



![PrivateAccess Vault](https://www.bleepstatic.com/images/news/u/1109292/2021/PrivateAccess_Vault.png)*Image: Western Digital*
In related news, Western Digital confirmed a [speed crippling SN550 SSD flash change](https://www.bleepingcomputer.com/news/hardware/western-digital-confirms-speed-crippling-sn550-ssd-flash-change/) in August (with writing speed decreases of up to 50%) after replacing the NAND flash memory in the WD Blue SN550, one of its most popular M.2 NVMe SSD models.


While it failed to alert customers of the change, the company said that, in the future, it would also introduce new model numbers when making hardware changes impacting its' products' performance.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Sandisk]] [[Secureaccess]] [[Privateaccess]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-36750]]

