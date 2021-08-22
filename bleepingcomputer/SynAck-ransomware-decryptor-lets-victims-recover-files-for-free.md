# SynAck ransomware decryptor lets victims recover files for free
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/synack-ransomware-decryptor-lets-victims-recover-files-for-free/)
+ Date: August 20, 2021
+ Author: Lawrence Abrams


## Article:
![decryptor](https://www.bleepstatic.com/content/hl-images/2021/01/29/key-large.jpg)


Emsisoft has released a decryptor for the SynAck Ransomware, allowing victims to decrypt their encrypted files for free.


The SynAck ransomware gang launched its operation in 2017 but rebranded as the El\_Cometa gang in 2021.



As part of this rebranding, the [threat actors released the master decryption keys](https://www.bleepingcomputer.com/news/security/synack-ransomware-releases-decryption-keys-after-el-cometa-rebrand/) and documentation for their encryption algorithm on their Tor data leak site.



![SynAck master decryption keys released by threat actors](https://www.bleepstatic.com/images/news/ransomware/s/synack/master-keys-released/decryption-keys.jpg)**SynAck master decryption keys released by threat actors**
SynAck decryptor released
-------------------------


Today, Emsisoft has released a [SynAck ransomware](https://www.emsisoft.com/ransomware-decryption-tools/synack) decryptor that works on all variants and allows victims to recover their files for free.




> 
> Works for both RSA and ECIES (secp192r1) variants. Thanks [@kaspersky](https://twitter.com/kaspersky?ref_src=twsrc%5Etfw) for the great article on the older variant, saved me lots of RE time.
> 
> 
> — Michael Gillespie (@demonslay335) [August 20, 2021](https://twitter.com/demonslay335/status/1428761855804256260?ref_src=twsrc%5Etfw)


After downloading the decryptor, simply run the program and browse to a ransom note. After selecting the ransom, press the **Start** button and the decryption key will be detected.



![Generating a SynAck decryption key from the ransom note](https://www.bleepstatic.com/images/news/ransomware/decryptors/s/synack/synack-decryptor.jpg)**Generating a SynAck decryption key from the ransom note**
After pressing the **OK**button, the decryptor will load your decryption key, and you can now begin decrypting files.


As you can see from the image below, we could decrypt a test file using the key extracted from the bundled ransom note.



![Decrypting a file using the SynAck decryptor](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Decrypting a file using the SynAck decryptor**
You can delete the leftover encrypted files after you have decrypted your files and determined that they are opening correctly.


For those who need help using the decryptor, please [read this page](https://www.emsisoft.com/ransomware-decryption-tools/howtos/emsisoft_howto_synack.pdf) first, and if that does not help, feel free to ask in our forums for further assistance.




#### Tags:
[[SynAck]] [[decryptor]] [[Bleeping Computer]]
