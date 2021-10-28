# Android spyware spreading as antivirus software in Japan
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/android-spyware-spreading-as-antivirus-software-in-japan/)
+ Date: October 28, 2021
+ Author: Bill Toulas


## Article:
![Japanese flag](https://www.bleepstatic.com/content/hl-images/2021/10/28/japan.jpg?rand=540441458)


A new variant of the Android info-stealer called FakeCop has been spotted by Japanese security researchers, who warn that the distribution of the malicious APK is picking up pace.


First spotted by Japanese security researcher [Yusuke Osumi](https://twitter.com/ozuma5119) last week, the malware is being distributed in phishing campaigns impersonating KDDI.


Furthermore, the malware is only detected by 22 out of 62 AV engines on VirusTotal, showing a concerted effort by the threat actor to remain hidden.




> 
> [#Phishing](https://twitter.com/hashtag/Phishing?src=hash&ref_src=twsrc%5Etfw) [#malware](https://twitter.com/hashtag/malware?src=hash&ref_src=twsrc%5Etfw) [#android](https://twitter.com/hashtag/android?src=hash&ref_src=twsrc%5Etfw)  
> 
> Brand: au KDDI あんしんセキュリティ  
> 
> VT: <https://t.co/CFbRa6KkYX><https://t.co/fWcZ1cKWJy>  
>   
> 
> hxxp://zuwnkmkrjh[.]duckdns[.]org/AU.apk  
> 
> C2 hxxp://210902[.]top/  
> 
> 45.116.13[.]12 (AS4785 xTOM, JP)  
> 
> → websocket://172.247.35[.]189:6666/  
> 
> (AS21859 ZenLayer) [pic.twitter.com/nCsq31Dccw](https://t.co/nCsq31Dccw)
> 
> 
> — Osumi, Yusuke (@ozuma5119) [October 19, 2021](https://twitter.com/ozuma5119/status/1450467756302905359?ref_src=twsrc%5Etfw)


Masked as a popular security tool
---------------------------------


In a new report by cybersecurity firm Cyble, researchers have dubbed the malware 'FakeCop' and state it is masquerading as 'Anshin Security,' a popular antivirus product in Japan.


After analyzing the malware, the researchers state that the new spyware variant has the following capabilities:


* Collect SMSs, contacts, accounts information, and apps list
* Modify or delete SMSs in the device database
* Collect device hardware information (IMEI)
* Send SMSs without the user’s knowledge


The spyware asks the user to grant numerous sensitive permissions to perform this functionality, as shown below.



![Permissions requested by FakeCop](https://www.bleepstatic.com/images/news/u/1220909/Security/permissions.png)**Permissions requested by FakeCop**  
*Source: Cyble*
When users are met with such requests by AV software, they are more likely to grant them because security software commonly needs higher privileges to scan and remove detected threats.


Attempts to evade detection
---------------------------


The malware authors are also using a custom packer to hide the actual behavior of their app while also thwarting static detection.


The malicious code is Bitwise XOR encrypted and stored inside a file in the assets folder, and it can only be unpacked if invoked by a specific app subclass.


Additionally, FakeCop actively scans the device app list, and if any antivirus apps are found, it pushes a notification to the user asking them to uninstall them.


The hardcoded AV solutions that malware will prompt users to remove include Anshin Security, McAfee Security, and the Docomo Anshin Scan.



![Code checking for the presence of AV tools](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/checking%20packages.png)**Code checking for the presence of AV tools**  
*Source: Cyble*
As for how FakeCop reaches the victims, Cyble’s OSINT research revealed two channels of distribution, one via SMS with malicious links and one relying on phishing emails.


The 'duckdns.org' free dynamic DNS used as the delivery mechanism has been [previously used](https://japanlife--guide-com.translate.goog/en/phishing-scam-alerts-via-phone-messages-in-japan-duckdns-org/?_x_tr_sl=vi&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui,sc) for distributing Medusa and Flubot, so it's possible that the current campaign ties to the same operators.


As a general rule, avoid clicking on URL links that arrive via unsolicited SMS and email, and refrain from installing APK files from outside the Google Play Store.


Additionally, periodically check and confirm that Google Play Protect is active on your device, and always scrutinize permission requests when installing a new app.




#### Tags:
[[malware]] [[FakeCop]] [[Security,]] [[Bleeping Computer]]
