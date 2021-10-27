# Malicious NPM libraries install ransomware, password stealer
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/malicious-npm-libraries-install-ransomware-password-stealer/)
+ Date: October 27, 2021
+ Author: Lawrence Abrams


## Article:
![NPM](https://www.bleepstatic.com/content/hl-images/2021/10/23/npm-supply-chain-attack.jpg)


Malicious NPM packages pretending to be Roblox libraries are delivering ransomware and password-stealing trojans on unsuspecting users.


The two NPM packages are named **noblox.js-proxy** and **noblox.js-proxies**, and use typo-squatting to pretend to be the legitimate Roblox API wrapper called [noblox.js-proxied](https://www.npmjs.com/package/noblox.js-proxied) by changing a single letter in the library's name.



![Malicious noblox.js-proxies NPM](https://www.bleepstatic.com/images/news/ransomware/m/monster-npm/noblox-proxies.jpg)**Malicious noblox.js-proxies NPM** 
In a [new report](http://blog.sonatype.com/fake-npm-roblox-api-package-installs-ransomware-spooky-surprise) by open source security firm [Sonatype](https://www.sonatype.com) with further analysis by BleepingComputer, these malicious NPMs are infecting victims with an MBRLocker ransomware that impersonates the [notorious GoldenEye ransomware](https://www.bleepingcomputer.com/news/security/petya-ransomware-returns-with-goldeneye-version-continuing-james-bond-theme/), trollware, and a password stealing trojan.


Both of the malicious NPM libraries have since been taken down and are no longer available.


A mess of malicious activity
----------------------------


After the malicious NPM libraries are added to a project and launched, the library will execute a postinstall.js script. This script is normally used to execute legitimate commands after a library is installed, but in this case, it starts a chain of malicious activity on victims' computers.


As you can see below, the postinstall.js script is heavily obfuscated to prevent analysis by security researchers and software.



![Obfuscated postinstall.js script](https://www.bleepstatic.com/images/news/ransomware/m/monster-npm/postinstall-script.jpg)**Obfuscated postinstall.js script**
When executed, the script will launch the heavily obfuscated batch file called 'nobox.bat,' shown below.



![Obfuscated noblox.bat batch file](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Obfuscated noblox.bat batch file**
This batch file was decoded by Sonatype security researcher Juan Aguirre and will download a variety of malware from Discord and launches them with the help of the [fodhelper.exe UAC bypass](https://pentestlab.blog/2017/06/07/uac-bypass-fodhelper/)


The files downloaded by the noblox.bat batch file are listed below in the order they are installed, along with their VirusTotal links and a description of their actions.


* [exclude.bat](https://www.virustotal.com/gui/file/0419582ea749cef904856dd1165cbefe041f822dd3ac9a6a1e925afba30fe591) - Adds a Microsoft Defender exclusion not to scan files under the C:\ drive.
* [legion.exe](https://www.virustotal.com/gui/file/a81b7477c70f728a0c3ca14d0cdfd608a0101cf599d31619163cb0be2a152b78/details) - Deploys a [password-stealing trojan](https://www.virustotal.com/gui/file/f4fb42c8312a6002a8783e2a1ab4571eb89e92cd192b1a21e8c4582205c37312) that steals browser history, cookies, saved passwords, and attempts to record video via the built-in webcam.
* [000.exe](https://www.virustotal.com/gui/file/4a900b344ef765a66f98cf39ac06273d565ca0f5d19f7ea4ca183786155d4a47) - Trollware that modifies the current user's name to 'UR NEXT,' plays videos, changes a user's password, and attempts to lock them out of their system.
* [tunamor.exe](https://www.virustotal.com/gui/file/78972cdde1a038f249b481ea2c4b172cc258aa294440333e9c46dcb3fbed5815) - Installs an MBRLocker called 'Monster Ransomware,' which impersonates the [GoldenEye ransomware](https://www.bleepingcomputer.com/news/security/petya-ransomware-returns-with-goldeneye-version-continuing-james-bond-theme/).


The Monster ransomware MBRLocker
--------------------------------


Of particular interest is the 'tunamor.exe' executable, which installs an MBRLocker calling itself 'Monster Ransomware.'


When executed, the ransomware will perform a forced restart of the computer and then display a fake CHKDSK of the system. During this process, the ransomware is allegedly encrypting the disks on the computer.



![Fake CHKDSK while drives are encrypted](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Fake CHKDSK while drives are encrypted**  
*Source: BleepingComputer*
When finished, it will reboot the computer and display a skull and crossbones lock screen originally found in the Petya/ GoldenEye ransomware families.



![Monster ransomware lock screen](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Monster ransomware lock screen**  
*Source: BleepingComputer*
After pressing enter, the victim is shown a screen stating that their hard disks are encrypted and that they must visit the http://monste3rxfp2f7g3i.onion/ Tor site, which is now down, to pay a ransom.



![Monster ransomware ransom demand](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Monster ransomware ransom demand**  
*Source: BleepingComputer*
BleepingComputer discovered the '*qVwaofRW5NbLa8gj*' string, which is accepted as a valid key to decrypt the computer. However, while the key is accepted and the ransomware states it is decrypting the computer, Windows will fail to start afterward.



![Windows unable to start after entering key](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Windows unable to start after entering key**  
*Source: BleepingComputer*
It is unclear if an additional string must be added to that key to decrypt the hard disk's drive correctly or if this program is simply a wiper designed to destroy systems.


This ransomware does not appear to be widespread and is only known to be distributed via these NPM packages.


Based on the activity of the 000.exe trollware and the strange behavior of the Monster ransomware, it is likely that these packages are designed to destroy a system rather than generate a ransom demand.


Malicious NPMs used in supply-chain attacks, such as this one, are becoming more common.


[Sonatype recently discovered three malicious NPM libraries](https://blog.sonatype.com/newly-found-npm-malware-mines-cryptocurrency-on-windows-linux-macos-devices) used to deploy cryptominers on Linux and Windows devices.


Last Friday, the very popular [UA-Parser-JS NPM library was hijacked](https://www.bleepingcomputer.com/news/security/popular-npm-library-hijacked-to-install-password-stealers-miners/) to infect users with miners and password stealing trojans.


IOCS
----




#### Tags:
[[ransomware]] [[NPM]] [[BleepingComputer]] [[MBRLocker]] [[Sonatype]] [[postinstall.js]] [[Windows]] [[Bleeping Computer]]
