# A Microsoft Defender Glitch Allowed Hackers Evade AV Detections
### Microsoft has now fixed the Defender glitch that even existed in the Windows 10 21H1 and 21H2. Windows 11 remained unaffected by this glitch.

## Information:
+ Source: Latest Hacking News
+ Link: https://latesthackingnews.com/2022/01/21/microsoft-defender-glitch-allowed-hackers-to-evade-av-detection/
+ Date: 2022-01-21
+ Author: Abeerah Hashim


## Article:
![Article Image](https://latesthackingnews.com/wp-content/uploads/2020/09/Microsoft-Windows-Defender.jpeg)
 Security researchers have highlighted a serious technical glitch in Microsoft Defender antimalware program. Briefly, Microsoft Defender exposed the AV exclusion to anyone, allowing potential adversaries to exploit/deploy malware while evading detections.

 Researcher Points Out A Microsoft Defender Glitch
-------------------------------------------------

 Security researcher Antonio Cocomazzi from SentinelOne recently discovered a Microsoft Defender glitch that existed for years.

 Sharing about it in a tweet, the researcher mentioned how Defender exposed details of antivirus exclusions.

 
>  Windows Defender AV allows Everyone to read the configured exclusions on the system 🤦
> 
>  reg query "HKLMSOFTWAREMicrosoftWindows DefenderExclusions" /s [pic.twitter.com/dpTFwMVRje](https://t.co/dpTFwMVRje)
> 
>  — Antonio Cocomazzi (@splinter\_code) [January 12, 2022](https://twitter.com/splinter_code/status/1481073265380581381?ref_src=twsrc%5Etfw)
> 
> 

  Consequently, this would allow an attacker to plant malware in excluded folders to escape [Microsoft Defender](https://latesthackingnews.com/2021/03/24/microsoft-defender-now-addresses-exchange-server-vulnerabilities-automatically/) detection.

 According to another researcher, the glitch existed for at least 8 years.

 
>  Noticed that almost 8 years ago when I started in Tech Support. Always told myself that if I was some kind of malware dev I would just lookup the WD exclusions and make sure to drop my payload in an excluded folder and/or name it the same as an excluded filename or extension…
> 
>  — Aura (@SecurityAura) [January 12, 2022](https://twitter.com/SecurityAura/status/1481107646082072577?ref_src=twsrc%5Etfw)
> 
> 

  In Windows 10, these exclusions were even possible to view via the GUI.

 This security vulnerability is particularly important for corporate users. While exploiting the vulnerability requires local access, it isn’t difficult for an attacker who has already infiltrated the network. Accessing the exclusion list was possible for any user privilege, thus increasing the severity of the matter.

 Microsoft Fixed The Matter
--------------------------

 The researchers observed that the glitch affected the latest Windows 10 21H1 and Windows 10 21H2 alongside the previous Windows versions. However, it didn’t affect Windows 11.

 
>  Is that Windows 11? 
> 
>  I've tested clean installs of Windows 10 21H1 and 21H2, and Get-MpPreference is protected while the reg keys are not.
> 
>  In Windows 11, all methods are protected from standard users :)
> 
>  — Nathan McNulty (@NathanMcNulty) [January 12, 2022](https://twitter.com/NathanMcNulty/status/1481373102973997062?ref_src=twsrc%5Etfw)
> 
> 

  The most obvious fix for this glitch is to update to the latest Windows 11. Nonetheless, since this isn’t possible for many existing Windows 10 users due to the hardware requirements for the upgrade, Microsoft has fortunately addressed the matter in Windows 10 too.

 According to another researcher, the [tech giant](https://latesthackingnews.com/2021/03/22/tech-giant-acer-suffered-revil-ransomware-attack-attackers-demand-50m/) has fixed the glitch “in PrivescCheck”.

 
>  There is now a check for this in PrivescCheck (available through the "-Extended" mode).  
> Thanks [@splinter\_code](https://twitter.com/splinter_code?ref_src=twsrc%5Etfw) ! 🙏 <https://t.co/hMCwa03AlY>
> 
>  — Clément Labro (@itm4n) [January 13, 2022](https://twitter.com/itm4n/status/1481716083539288072?ref_src=twsrc%5Etfw)
> 
> 

  So now, Windows 10 users do have a patch for this issue. It now requires all users to vigilantly monitor their systems and networks for security. Users should also review their AV exclusion lists to be sure about the exclusions. As the researcher [Nathan McNulty](https://twitter.com/NathanMcNulty) highlighted,

 
>  Finally, for those configuring Defender AV on servers, be aware that there are automatic exclusions that get enabled when specific roles or features are installed
> 
>  They do not cover non-default install locations, and you should review the list here:<https://t.co/StYXMmfs8T>
> 
>  — Nathan McNulty (@NathanMcNulty) [January 12, 2022](https://twitter.com/NathanMcNulty/status/1481136160936132609?ref_src=twsrc%5Etfw)
> 
> 

  Let us know your thoughts in the comments.

   


## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Malware]] [[Mcnulty]] [[Latest Hacking News]]
#### urls
https://t.co/hMCwa03AlY https://t.co/StYXMmfs8T

