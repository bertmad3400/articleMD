# BlackByte ransomware decryptor released to recover files for free
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/blackbyte-ransomware-decryptor-released-to-recover-files-for-free/)
+ Date: October 19, 2021
+ Author: Lawrence Abrams


## Article:
![Free decryptor](https://www.bleepstatic.com/content/hl-images/2021/02/07/brighter-key.jpg)


A free decryptor for the BlackByte ransomware has been released, allowing past victims to recover their files for free.


When executed, most ransomware will generate a unique encryption key per file or a single key per machine known as sessions keys used to encrypt a victim's device.


These keys are then encrypted with a public RSA key and appended to the end of an encrypted file or a ransom note. This encrypted key can now only be decrypted by the associated private decryption key known only to the ransomware operation.


This makes it so threat actors can decrypt the encrypted keys when a victim pays a ransom.


BlackByte reused encryption keys
--------------------------------


In a [report by Trustwave](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/),  researchers explain that the ransomware was downloading a file called 'forest.png' from a remote site under their control. While this file is named to appear as an image file, it actually contains the AES encryption key used to encrypt a device.


As BlackByte uses AES symmetrical encryption, the same key is used for both the encryption and decryption of files.


While BlackByte also encrypts this downloaded AES encryption key and appends it to the ransom note, Trustwave discovered that the ransomware gang was reusing the same forest.png file for multiple victims.


As the same 'raw' encryption key was being reused, Trustwave could use that key to build a decryptor that recovers a victim's files for free.


However, there are always drawbacks when releasing free decryptors like this as it alerts the ransomware gangs of the bugs in their programs and quickly fixed.


Trustwave's report and decryptor did not go unnoticed by the ransomware gang, who warned that they have used more than one key and that utilizing the decryptor with the wrong key would corrupt a victim's files.



> 
> "we have seen in some places that there is a decryption for our ransom. we would not recommend you to use that. because we do not use only 1 key. if you will use the wrong decryption for your system you may break everything, and you wont be able to restore your system again.we just want to warn you, if you do decide to use that, its at your own risk." - BlackByte.
> 
> 
> 



![BlackByte's response to Trustwave's decryptor](https://www.bleepstatic.com/images/news/ransomware/b/blackbyte/decryptor/blackbyte-blog.jpg)**BlackByte's response to Trustwave's decryptor**
If you are a BlackByte victim and want to use Trustwave's decryptor, you will need to download the [source code from Github](https://github.com/SpiderLabs/BlackByteDecryptor) and compile it yourself.


While Trustwave has included a default 'forest.png' file that will be used to extract the decryption key, it may be possible that BlackByte rotated the encryption keys downloaded in that file.


Due to this, it is strongly advised that you backup files before attempting to decrypt them.


Furthermore, if you have a 'forest.png' file on an encrypted device, you should use that file rather than the one bundled with Trustwave's decryptor.


Who is BlackByte?
-----------------


BlackByte is a ransomware operation that slowly started targeting corporate victims worldwide [in early July 2021](https://www.bleepingcomputer.com/forums/t/755181/blackbyte-ransomware-blackbyte-support-topic/).


First reports of the ransomware showed up about a week later in the [BleepingComputer forums](https://www.bleepingcomputer.com/forums/t/755181/blackbyte-ransomware-blackbyte-support-topic/) after victims sought help in decrypting their files.



![BlackByte ransom note](https://www.bleepstatic.com/images/news/ransomware/b/blackbyte/decryptor/blackbyte-ransom-note.jpg)**BlackByte ransom note**
Written in C#, BlackByte will attempt to terminate numerous security, mail server, and database processes to successfully encrypt a device.


The ransomware will also attempt to disable Microsoft Defender on target devices before attempting encryption.


While BlackByte is not as active as other ransomware operations, they have successfully conducted many attacks worldwide and should not be ignored.




#### Tags:
[[BlackByte]] [[ransomware]] [[Trustwave]] [[decryptor]] [[device.]] [[files.]] [[Bleeping Computer]]
