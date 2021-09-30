# RansomExx ransomware Linux encryptor may damage victims' files
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/ransomexx-ransomware-linux-encryptor-may-damage-victims-files/)
+ Date: September 30, 2021
+ Author: Lawrence Abrams


## Article:
![RansomEXX](https://www.bleepstatic.com/images/stock-photos/ransomware/ransomexx-header.jpg)


​Cybersecurity firm Profero has discovered that the RansomExx gang does not correctly lock Linux files during encryption, leading to potentially corrupted files.


In a new report by Profero, Senior Incident Responder Brenton Morris says the RansomEXX decryptor was failing on various files encrypted by the threat actor's Linux Vmware ESXI encryptor for one the victims who paid the ransom.


After reverse-engineering the RansomExx Linux encryptor, Profero discovered that the problematic decryption was caused by Linux files not being adequately locked while they were encrypted.


Without the file being locked, if the ransomware attempted to encrypt a Linux file simultaneously as another process wrote to it, the encrypted file would contain both encrypted data and unencrypted data appended after it, as shown below.



![Encrypted file with a mix of encrypted and unencrypted data](https://www.bleepstatic.com/images/news/ransomware/r/ransom.exx/linux-corrupted-files/corrupted-ransomexx-file.jpg)**Encrypted file with a mix of encrypted and unencrypted data**
"Some strains of Linux ransomware will attempt to acquire a file lock using *fcntl* while others will often not attempt to lock files for writing, and instead either knowingly choose to take the risk of corrupting the files or do so unknowingly due to lack of Linux programming experience," Morris told BleepingComputer.


"The Linux version of RansomEXX did not attempt to lock the file at all."


When RansomExx encrypts a file, it will append an RSA encrypted decryption key to the end of each encrypted file.


If a victim pays a ransom, the threat actor supplies a decryptor that can decrypt each file's encrypted decryption key and then use it to decrypt the file's contents.


However, as these problematic encrypted files had unencrypted data appended to the end of the file, the decryptor could not read the encrypted key properly and would fail to decrypt the file.


Fixed decryptor released
------------------------


To aid their clients and the greater cybersecurity community, Profero has released an [open-source RansomEXX decryptor](https://github.com/proferosec/RansomEXX-Tools) that can decrypt files encrypted with this file locking issue.



![Profero's RansomEXX decryptor](https://www.bleepstatic.com/images/news/ransomware/r/ransom.exx/linux-corrupted-files/ransomexx-decryptor.jpg)**Profero's RansomEXX decryptor**
Victims still need to have acquired a decryptor key from the threat actor, but they can now use a decryptor created by a cybersecurity firm rather than having to take the time to vet one provided by threat actors.


"Because the attackers provide paying victims with a decryption tool they must run to decrypt their files there is a risk that the decryption tool may be malicious. This requires affected victims to reverse engineer the provided decryption tool to ensure there is no hidden payload or malicious features, a time investment that can be problematic for some organizations during a ransomware incident," explains [Profero's blog post](https://medium.com/proferosec-osm/ransomexx-fixing-corrupted-ransom-8e379bcaf701).


You can find complete instructions and command-line usage for using the decryptor in Profero's post and on the decryptor's GitHub page.




#### Tags:
[[decryptor]] [[Linux]] [[Profero]] [[RansomEXX]] [[RansomExx]] [[ransomware]] [[Bleeping Computer]]
