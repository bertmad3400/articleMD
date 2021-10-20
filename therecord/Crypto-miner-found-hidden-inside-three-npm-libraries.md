# Crypto-miner found hidden inside three npm libraries
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/crypto-miner-found-hidden-inside-three-npm-libraries/)
+ Date: October 20, 2021
+ Author: Catalin Cimpanu


## Article:
![Crypto-miner found hidden inside three npm libraries](https://therecord.media/wp-content/uploads/2021/03/JavaScript.jpg)

DevOps security firm Sonatype has uncovered crypto-mining malware hidden inside three JavaScript libraries uploaded on the official npm package repository.


The three files, disguised as user-agent string parsers, would detect the user’s operating system and then run a BAT or Shell script, based on the victim’s platform.


“These scripts then download an externally-hosted EXE or a Linux ELF, and execute the binary with arguments specifying the mining pool to use, the wallet to mine cryptocurrency for, and the number of CPU threads to utilize,” said Sonatype security researcher Ali ElShakankiry, who discovered the campaign.


This [campaign’s specifics](https://blog.sonatype.com/newly-found-npm-malware-mines-cryptocurrency-on-windows-linux-macos-devices) include:


* The names of the three npm packages were: [klow](https://www.npmjs.com/package/klow), [klown](https://www.npmjs.com/package/klown), [okhsa](https://www.npmjs.com/package/okhsa).
* The packages were live only for a day, on October 15.
* None of the three libraries were downloaded more than 150 times, individually.
* The final payloads (cryptominers) could run on [Windows](https://www.virustotal.com/gui/file/7f986cd3c946f274cdec73f80b84855a77bc2a3c765d68897fbc42835629a5d5) or [Linux](https://www.virustotal.com/gui/file/ea131cc5ccf6aa6544d6cb29cdb78130feed061d2097c6903215be1499464c2e) platforms.
* All three packages were uploaded from the same account.


The number of malicious packages uploaded on the npm repository has been rising, but this is actually a good thing rather than a negative aspect, as this is the byproduct of companies like Snyk and Sonatype constantly monitoring new uploads and package updates for malicious code and catching miscreants before they do more damage and before packages are downloaded thousands of times in real-world projects.





#### Tags:
[[Sonatype]] [[npm]] [[The Record]]
