# Free decryptor released for Atom Silo and LockFile ransomware
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/free-decryptor-released-for-atom-silo-and-lockfile-ransomware/)
+ Date: October 27, 2021
+ Author: Sergiu Gatlan


## Article:
![Free decryptor released for AtomSilo, LockFile ransomware victims](https://www.bleepstatic.com/content/hl-images/2021/10/27/Decyptor.jpg)


Avast has just released a decryption tool that will help AtomSilo and LockFile ransomware victims recover some of their files for free without having to pay a ransom.


Avast released another decryption tool earlier today [to help Babuk ransomware victims recover their files for free](https://www.bleepingcomputer.com/news/security/babuk-ransomware-decryptor-released-to-recover-files-for-free/).


As the Czech cybersecurity software firm explained, this decryptor may not be able to decrypt files with unknown, proprietary, or with no format at all.


"During the decryption process, the Avast AtomSilo decryptor relies on a known file format in order to verify that the file was successfully decrypted. For that reason, some files may not be decrypted," Avast's Threat Intelligence Team said.


The decryptor works for both ransomware strains because they are very similar, even though the groups deploying them on victims' networks use different attack tactics.


Avast Threat Labs said this ransomware decryptor was created in collaboration with RE - CERT malware analyst Jiří Vinopal, who found a [weakness in the AtomSilo ransomware](https://twitter.com/vinopaljiri/status/1449550289204391940) earlier this month.


**AtomSilo and LockFile victims can [download the decryption tool](https://files.avast.com/files/decryptor/avast_decryptor_atomsilo.exe) from Avast's servers and decrypt entire disk partitions using the instructions displayed within the decryptor's UI.**


BleepingComputer tested the tool and recovered files encrypted with an Atom Silo sample using Avast's free decryptor.



![Avast Atom Silo decryptor](https://www.bleepstatic.com/images/news/u/1109292/2021/Avast_Atom_Silo_decryptor.png)*Avast Atom Silo decryptor (BleepingComputer)*
The [LockFile](https://www.bleepingcomputer.com/tag/lockfile/) ransomware operation was first seen in July 2021 after [the gang was spotted taking over Windows domains](https://www.bleepingcomputer.com/news/security/microsoft-exchange-servers-being-hacked-by-new-lockfile-ransomware/) and encrypting devices after exploiting servers unpatched against the [ProxyShell](https://www.bleepingcomputer.com/tag/proxyshell/) and [PetitPotam vulnerabilities](https://www.bleepingcomputer.com/news/microsoft/new-petitpotam-attack-allows-take-over-of-windows-domains/).


When encrypting files, LockFile ransomware will append the .lockfile extension to the encrypted files' names and drop ransom notes named using the '[victim\_name]-LOCKFILE-README.hta' format.


Of particular interest is that LockFile's color scheme and ransom note layout are very similar to the LockBit ransomware. However, there does not appear to be any relation between the two groups.


Atom Silo is a newly spotted ransomware gang whose operators have recently targeted [Confluence Server and Data Center servers](https://www.bleepingcomputer.com/news/security/new-atom-silo-ransomware-targets-vulnerable-confluence-servers/) vulnerable against a now patched and actively exploited bug.


The ransomware used by Atom Silo is almost identical to LockFile, according to SophosLabs researchers.


However, Atom Silo operators use novel techniques that make it extremely difficult to investigate their attacks, including side-loading malicious dynamic-link libraries that disrupt endpoint protection solutions.




#### Tags:
[[ransomware]] [[decryptor]] [[LockFile]] [[AtomSilo]] [[Bleeping Computer]]
