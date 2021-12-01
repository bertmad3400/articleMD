# Microsoft Defender scares admins with Emotet false positives
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-scares-admins-with-emotet-false-positives/)
+ Date: November 30, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft Defender scares admins with Emotet false positives](https://www.bleepstatic.com/content/hl-images/2021/05/26/Microsoft-Defender.jpg)


Microsoft Defender for Endpoint is currently blocking Office documents from being opened and some executables from launching due to a false positive tagging the files as potentially bundling an Emotet malware payload.


Windows system admins are reporting [[1](https://twitter.com/ChrisBarnesInfo/status/1465759131218984964), [2](https://twitter.com/lunderquist2/status/1465805631370182660), [3](https://www.reddit.com/r/sysadmin/comments/r5y8wv/msdefender_detect_emotet_in_microsoft_excel/), [4](https://twitter.com/search?q=PowEmotet&src=typed_query&f=live), [5](https://www.reddit.com/search/?q=PowEmotet)] that this is happening since updating Microsoft's enterprise endpoint security platform (previously known as Microsoft Defender ATP) definitions to version 1.353.1874.0.


When triggered, Defender for Endpoint will block the file from opening and throw an error mentioning suspicious activity linked to [Win32/PowEmotet.SB](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Behavior:Win32/PowEmotet.SB&ThreatID=2147805329) or [Win32/PowEmotet.SC](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Behavior:Win32/PowEmotet.SC).


"We're seeing issues with definition update 1.353.1874.0 detecting printing as Win32/PowEmotet.SB this afternoon," one admin [said](https://twitter.com/SydeEyeDotCom/status/1465800720821727235).


"We are seeing this detected for Excel, any Office app using MSIP.ExecutionHost.exe ( AIP Sensitivity Client ) and splwow64.exe," another [added](https://www.reddit.com/r/sysadmin/comments/r5y8wv/msdefender_detect_emotet_in_microsoft_excel/hmpyalf/).


A third one [confirmed the issues](https://www.reddit.com/r/sysadmin/comments/r5y8wv/msdefender_detect_emotet_in_microsoft_excel/hmpz0jv/) with today's definition updates: "We're seeing the same behavior specifically with v.1.353.1874.0 of the definitions, which was released today, & included a definition for Behavior:Win32/PowEmotet.SB & Behavior:Win32/PowEmotet.SC."



![Emotet false positive in Microsoft Defender](https://www.bleepstatic.com/images/news/u/1109292/2021/Microsoft_Defender_Emotet_false_positive.png)*Emotet false positive in Microsoft Defender (BleepingComputer)*
While Microsoft hasn't yet shared any info on what causes this, the most likely reason is that the company has increased the sensitivity for detecting Emotet-like behavior in updates released today, which makes Defender's generic behavioral detection engine too sensitive prone to false positives.


The change was likely prompted by the [recent revival of the Emotet botnet](https://www.bleepingcomputer.com/news/security/emotet-malware-is-back-and-rebuilding-its-botnet-via-trickbot/) from two weeks ago, after Emotet research group [Cryptolaemus](https://twitter.com/Cryptolaemus1/status/1460302706954981385), [GData](https://cyber.wtf/2021/11/15/guess-whos-back/), and [Advanced Intel](https://twitter.com/VK_Intel/status/1460308855129313281) began seeing TrickBot dropping Emotet loaders on infected devices.


Even though this is almost surely not the real thing, the timing is definitely unfortunate with Emotet coming back and most Windows admins already on their toes.


As some of them have reported, they [almost took their data centers offline](https://www.reddit.com/r/sysadmin/comments/r5y8wv/msdefender_detect_emotet_in_microsoft_excel/hmpru0o/) to stop a possible Emotet infection from spreading before realizing that what they were seeing were likely false positives.


Since October 2020, Windows admins had to deal with other Defender for Endpoint including one that [showed network devices infected with Cobalt Strike](https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-atp-scars-admins-with-false-cobalt-strike-alerts/) and another that [marked Chrome updates as PHP backdoors](https://www.bleepingcomputer.com/news/security/microsoft-defender-atp-detects-chrome-updates-as-php-backdoors/).


BleepingComputer has reached out to Microsoft for more information and to confirm that this behavioral detection issue triggers a false positive but has not heard back.




#### Tags:
[[Emotet]] [[Microsoft]] [[Windows]] [[admins]] [["We]] [[Bleeping Computer]]
