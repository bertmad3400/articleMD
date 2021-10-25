# Popular NPM library hijacked to install password-stealers, miners
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/popular-npm-library-hijacked-to-install-password-stealers-miners/)
+ Date: October 23, 2021
+ Author: Lawrence Abrams


## Article:
![NPM supply-chain attack](https://www.bleepstatic.com/content/hl-images/2021/10/23/npm-supply-chain-attack.jpg)


Hackers hijacked the popular UA-Parser-JS NPM library, with millions of downloads a week, to infect Linux and Windows devices with cryptominers and password-stealing trojans in a supply-chain attack.


The UA-Parser-JS library is used to parse a browser's user agent to identify a visitor's browser, engine, OS, CPU, and Device type/model.






The library is immensely popular, with millions of downloads a week and over 24 million downloads this month so far. In addition, the library is used in over a thousand other projects, including those by Facebook, Microsoft, Amazon, Instagram, Google, Slack, Mozilla, Discord, Elastic, Intuit, Reddit, and [many more well-known companies](https://faisalman.github.io/ua-parser-js/).



![UA-Parser-JS downloaded millions of times per week](https://www.bleepstatic.com/images/news/security/attacks/n/npms/ua-parser-js/downloads-npm-stat.jpg)**UA-Parser-JS downloaded millions of times per week**  
*Source: NPM-stat.com*
UA-Parser-JS project hijacked to install malware
------------------------------------------------


On October 22nd, a threat actor published malicious versions of the UA-Parser-JS NPM library to install cryptominers and password-stealing trojans on Linux and Windows devices.


According to the developer, his NPM account was hijacked and used to deploy the three malicious versions of the library.


"I noticed something unusual when my email was suddenly flooded by spams from hundreds of websites (maybe so I don't realize something was up, luckily the effect is quite the contrary)," explained Faisal Salman, the developer of UA-Parser-JS, in a [bug report](https://github.com/faisalman/ua-parser-js/issues/536#issuecomment-949742904).


"I believe someone was hijacking my npm account and published some compromised packages (`0.7.29`, `0.8.0`, `1.0.0`) which will probably install malware as can be seen from the diff here: <https://app.renovatebot.com/package-diff?name=ua-parser-js&from=0.7.28&to=1.0.0>."


The affected versions and their patched counterparts are:


From copies of the malicious NPMs shared with BleepingComputer by Sonatype, we can better understand the attack.


When the compromised packages are installed on a user's device, a preinstall.js script will check the type of operating system used on the device and either launch a Linux shell script or a Windows batch file.



![preinstall.js script used to check operating system type](https://www.bleepstatic.com/images/news/security/attacks/n/npms/ua-parser-js/check-os.jpg)**preinstall.js script used to check operating system type**
If the package is on a Linux device, a preinstall.sh script will be executed to check if the user is located in Russia, Ukraine, Belarus, and Kazakhstan. If the device is not located in those countries, the script will download the **jsextension**[[VirusTotal](https://www.virustotal.com/gui/file/ea131cc5ccf6aa6544d6cb29cdb78130feed061d2097c6903215be1499464c2e/detection)] program from 159[.]148[.]186[.]228 and execute it.


The jsextension program is an XMRig Monero miner, which will use only 50% of the device's CPU to avoid being easily detected.



![Linux shell script to install the miner](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Linux shell script to install the miner**
For Windows devices, the batch file will also download the XMRig Monero cryptominer and save it as **jsextension.exe** [[VirusTotal](https://www.virustotal.com/gui/file/7f986cd3c946f274cdec73f80b84855a77bc2a3c765d68897fbc42835629a5d5)] and execute it. In addition, the batch file will download an sdd.dll file [[VirusTotal](https://www.virustotal.com/gui/file/2a3acdcd76575762b18c18c644a745125f55ce121f742d2aad962521bc7f25fd)] from citationsherbe[.]at and save it as create.dll.



![Windows batch file to install the cryptominer](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Windows batch file to install the cryptominer**
The downloaded DLL is a password-stealing trojan (possibly [DanaBot](https://twitter.com/_TheEmperors_/status/1451955840005586951)) that will attempt to steal the passwords stored on the device.


When the DLL is loaded using the `regsvr32.exe -s create.dll` command, it will attempt to steal passwords for a wide variety of programs, including FTP clients, VNC, messaging software, email clients, and browsers.


A list of targeted programs can be found in the table below.


In addition to stealing passwords from the above programs, the DLL will execute a PowerShell script to steal passwords from the Windows credential manager, as shown below.



![Stealing stored passwords from Windows](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Stealing stored passwords from Windows**
This attack appears to have been conducted by the same threat actor behind other malicious NPM libraries discovered this week.


Researchers from open-source security firm [Sonatype discovered three malicious NPM libraries](https://blog.sonatype.com/newly-found-npm-malware-mines-cryptocurrency-on-windows-linux-macos-devices) used to deploy cryptominers on Linux and Windows devices in an almost identical manner.


What should UA-Parser-JS users do?
----------------------------------


Due to the widespread impact of this supply-chain attack, it is strongly advised that all users of the UA-Parser-JS library check their projects for malicious software.


This includes checking for the existence of either **jsextension.exe** (Windows) or **jsextension** (Linux) and deleting them if they are found.


For Windows users, you should scan your device for a **create.dll** file and delete it immediately.


While only Windows was infected with a password-stealing Trojan, it is wise for Linux users to also assume their device was fully compromised.


Due to this, all infected Linux and Windows users should also change their passwords, keys, and refresh tokens, as they were likely compromised and sent to the threat actor.


While changing your passwords and access tokens will likely be a huge undertaking, by not doing so, the threat actor can compromise other accounts, including any projects you develop for further supply-chain attacks.




#### Tags:
[[Windows]] [[Linux]] [[UA-Parser-JS]] [[NPM]] [[password-stealing]] [[cryptominers]] [[supply-chain]] [[jsextension]] [[[VirusTotal]]] [[DLL]] [[Bleeping Computer]]
