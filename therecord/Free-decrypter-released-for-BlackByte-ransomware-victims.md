# Free decrypter released for BlackByte ransomware victims
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/free-decrypter-released-for-blackbyte-ransomware-victims/)
+ Date: October 18, 2021
+ Author: Catalin Cimpanu


## Article:
![Free decrypter released for BlackByte ransomware victims](https://therecord.media/wp-content/uploads/2021/10/uncloked-decrypt-encryption-lock.jpg)

Cybersecurity firm Trustwave has released on Friday a free utility that victims of the BlackByte ransomware can use to decrypt and restore their files without paying the ransom demand.


Made available [on GitHub](https://github.com/SpiderLabs/BlackByteDecryptor), the decrypter exploits a design flaw in the ransomware’s encryption routine.


In a [two](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)–[part](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-2-code-obfuscation-analysis/) technical analysis, Trustwave researchers said they discovered that the BlackByte encryption routine began after the group downloaded a fake image file named “forest.png” on all of its victims’ computers.


According to researchers, this file contained a “raw” cryptographic key that the ransomware would use to derive keys to encrypt the victim’s files and then generate an access key to grant the victim access to a dark web portal where they could negotiate and pay the attacker’s ransom.


![BlackByte-encryption-scheme](https://www-therecord.recfut.com/wp-content/uploads/2021/10/BlackByte-encryption-scheme.png)Image: Trustwave
Trustwave researchers said this process was rather simplistic compared to the more complex and more secure encryption routines used by other gangs.


The decrypter they released on Friday automates the process of reading the raw key from the forest.png file, and then computing the decryption key needed to recover and restore the victim’s files.


A default “forest.png” file is included with the decrypter, but victims are advised to replace this file with the one found on their own systems.


### BlackByte gang responds to researchers


The release of the decrypter did not go unnoticed by the ransomware gang. On Monday, the group posted a message on their dark web portal, trying to scare victims from using the decrypter.


Their response is valid and warns companies about using the decrypter with the wrong key (forest.png file), which would result in victims corrupting their files.



> We would not recommend you to use that. because we do not use only 1 key. if you will use the wrong decryption for your system you may break everything, and you wont be able to restore your system again.we just want to warn you, if you do decide to use that, its at your own risk. 
> 
> BlackByte gang


![BlackByte](https://www-therecord.recfut.com/wp-content/uploads/2021/10/BlackByte.png)Image: The Record
But while the decrypter will help past victims, its release also means that the BlackByte gang also learned of the flaw in its encryption routine and will most likely fix it — something that has [happened before](https://www.zdnet.com/article/free-decrypter-released-for-avaddon-ransomware-victims-aaand-its-gone/) with other decrypters released to the general public without taking down the ransomware gang’s operations.


However, the fact that researchers found such a major flaw in the BlackByte ransomware encryption routine is not a surprise since this is a relatively new group, bound to have many bugs in its code.


First spotted three weeks ago, at the end of September, the gang has had limited activity and its dark web leak site, where the group lists victims who refused to pay the ransom demand, only lists eight entries so far.








#### Tags:
[[BlackByte]] [[ransomware]] [[decrypter]] [[Trustwave]] [[The Record]]
