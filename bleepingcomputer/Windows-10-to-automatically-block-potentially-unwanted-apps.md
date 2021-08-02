# Windows 10 to automatically block potentially unwanted apps
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-10-to-automatically-block-potentially-unwanted-apps/)
+ Date: August 2, 2021
+ Author: Lawrence Abrams


## Article:
![Microsoft Defender](https://www.bleepstatic.com/content/hl-images/2021/05/26/Microsoft--Defender.jpg)


Microsoft Defender and Microsoft Edge on Windows 10 will automatically block potentially unwanted applications (PUAs) by default starting this month.


Starting with the Windows 10 2004, the May 2020 update, Microsoft added a new 'Potentially unwanted app blocking' setting in Windows security that causes Microsoft Defender to block these types of applications.



Since its release, this feature has been disabled by default, but starting this month, Microsoft will begin to block PUAs when detected on a computer automatically.


"Starting in early August 2021 we'll begin turning it on by default to make it easier for you to keep your systems performing at their best," Microsoft announced in a short [support bulletin](https://support.microsoft.com/en-us/windows/potentially-unwanted-apps-will-be-blocked-by-default-b9f53cb9-7f1e-40bb-8c6b-a17e0ab6289e) today.


Windows 10 users who do not wish to block PUAs by default can turn the feature off by opening the **Windows Security**setting screen, clicking on **App & browser control**, and selecting **Reputation-based protection settings**.


At the Reputation-based protection settings screen, you can disable the '**Potentially unwanted app blocking**' setting.



![Windows Security Potentially unwanted app blocking setting](https://www.bleepstatic.com/images/news/Microsoft/Windows-10/w/windows-defender/pua-detection/new-setting.jpg)**Windows Security Potentially unwanted app blocking setting**
The 'Block Apps' option will enable Microsoft Defender's built-in PUA scanning and blocking feature. The 'Block downloads' will control whether the 'Block potentially unwanted apps' setting is enabled in the new Microsoft Edge browser. When enabled, SmartScreen will block PUAs and PUPs as they are downloaded.


This cchange to automatic blocking is beneficial for all users of Microsoft Defender as BleepingComputer has found over the years that programs marked as PUAs or PUPs should be classified as malware as they perform malicious behavior on a computer.


However, due to legal concerns, many companies do not block them automatically or ignore them.


With Microsoft automatically blocking PUAs, it could encourage the security industry to do a better job at blocking these unwanted applications.


What are potentially unwanted applications?
-------------------------------------------


Potentially unwanted applications, otherwise known as PUAs or PUPs, are not quite malware but pretty close.


They are usually created by legitimate legal entities who skirt the boundaries of what would be considered "respectable" software, and in most cases, perform unwanted behavior on a computer.


These programs range from browser extensions, adware, programs that send usage data without permission, Windows system cleaners and antivirus programs that use false positives, and programs that do not provide promised functionality.


Microsoft's [criteria for designating a program](https://docs.microsoft.com/en-us/windows/security/threat-protection/intelligence/criteria) as a potentially unwanted application is listed below:



> 
> * **Advertising software:** Software that displays advertisements or promotions, or prompts you to complete surveys for other products or services in software other than itself. This includes software that inserts advertisements to webpages.
> 
> 
> * **Torrent software (Enterprise only):** Software that is used to create or download torrents or other files specifically used with peer-to-peer file-sharing technologies.
> 
> 
> * **Cryptomining software:** Software that uses your device resources to mine cryptocurrencies.
> 
> 
> * **Bundling software:** Software that offers to install other software that is not developed by the same entity or not required for the software to run. Also, software that offers to install other software that qualifies as PUA based on the criteria outlined in this document.
> 
> 
> * **Marketing software:** Software that monitors and transmits the activities of users to applications or services other than itself for marketing research.
> 
> 
> * **Evasion software:** Software that actively tries to evade detection by security products, including software that behaves differently in the presence of security products.
> 
> 
> * **Poor industry reputation:** Software that trusted security providers detect with their security products. The security industry is dedicated to protecting customers and improving their experiences. Microsoft and other organizations in the security industry continuously exchange knowledge about files we have analyzed to provide users with the best possible protection.
> 
> 
> 


Unfortunately, some legitimate software may be lumped in with these criteria and detected by Microsoft Defender's PUA blocking feature.


For example, crypto mining applications and torrent software commonly have legitimate purposes but may now be detected by Microsoft Defender and removed.


In those, cases it is advised that you [create exclusions in Microsoft Defender](https://www.bleepingcomputer.com/news/microsoft/how-to-exclude-files-and-folders-from-windows-defender-scans/) to prevent those files from being quarantined rather than disabling the entire feature.




#### Tags:
[[Microsoft]] [[Windows]] [[PUAs]] [[software:]] [[feature.]] [[Bleeping Computer]]
