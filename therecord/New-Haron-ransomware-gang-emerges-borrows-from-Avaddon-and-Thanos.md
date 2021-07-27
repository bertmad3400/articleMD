# New Haron ransomware gang emerges, borrows from Avaddon and Thanos
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/new-haron-ransomware-gang-emerges-borrowing-from-avaddon-and-thanos/)
+ Date: July 27, 2021
+ Author: Catalin Cimpanu


## Article:
![New Haron ransomware gang emerges, borrows from Avaddon and Thanos](https://therecord.media/wp-content/uploads/2021/07/Haron.png)

Malware analysts from South Korean security firm S2W Labs have discovered a new ransomware operation that launched in the cybercrime ecosystem this month that heavily borrows from past ransomware operations such as [Thanos](https://www.recordedfuture.com/thanos-ransomware-builder/?__hstc=156209188.49c3da4ebdae6b0fac01d83f5c784449.1627408877939.1627408877939.1627408877939.1&__hssc=156209188.1.1627408877939&__hsfp=3914057893) and the [now-defunct Avaddon](https://therecord.media/avaddon-ransomware-operation-shuts-down-and-releases-decryption-keys/).


Named **Haron**, the [first samples](https://www.virustotal.com/gui/file/6e6b78a1df17d6718daa857827a2a364b7627d9bfd6672406ad72b276014209c/detection) linked to this gang have been spotted earlier this month.


Just like the vast majority of ransomware operations today, the Haron gang goes after enterprise targets in order to maximize its profits and also runs a “leak site” where it threatens to publish data stolen from companies who refuse to pay for decrypting their files.


But while Haron uses the same tactics used by more advanced ransomware families, S2W researchers say that under the hood, Haron is more of an amateurish Frankenstein, being built around code copied from other ransomware gangs.


These similarities include:


* Using a [leaked builder](https://github.com/Hacker-Data/Thanos-Ransomware-Builder) for the old Thanos ransomware to create the final Haron ransomware binary.
* The website where victims are told to go negotiate and pay the ransom (the “payment site”) is nearly similar to the one run by the former Avaddon gang.
* The leak site is also almost identical to Avaddon’s site.
* The Haron gang’s ransom note contains large portions of text copy-pasted from the Avaddon note.
* The Haron web server also contained icons and images that were previously found on the official Avaddon site.


![Haron-Avaddon-comparissons](https://www-therecord.recfut.com/wp-content/uploads/2021/07/Haron-Avaddon-comparissons-760x1024.png)Image: S2W Labs
All of these suggest that the Haron gang had direct access to some parts of Avaddon’s operation.


However, it is unclear how this happened. It is unclear if the Haron gang purchased these items from the Avaddon gang directly or if they hired one of Avaddon’s former members, most likely the person responsible for the gang’s web-facing applications, such as Avaddon’s payment and leak sites.


But as [S2W researchers point out](https://medium.com/s2wlab/quick-analysis-of-haron-ransomware-feat-avaddon-and-thanos-1ebb70f64dc4), while the Haron gang had incorporated Avaddon’s web-based systems into its operations, they did not have access to the Avaddon ransomware source code.


Written in C++, the original Avaddon ransomware was an advanced ransomware strain, something superior to the C# codebase of the Thanos strain, also used by the Prometheus ransomware group.








#### Tags:
[[ransomware]] [[Haron]] [[Avaddon]] [[Avaddon’s]] [[S2W]] [[Thanos]] [[The Record]]
