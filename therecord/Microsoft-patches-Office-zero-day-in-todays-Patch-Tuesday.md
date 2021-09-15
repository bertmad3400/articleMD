# Microsoft patches Office zero-day in today’s Patch Tuesday
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/microsoft-patches-office-zero-day-in-todays-patch-tuesday/)
+ Date: September 14, 2021
+ Author: Catalin Cimpanu


## Article:
![Microsoft patches Office zero-day in today’s Patch Tuesday](https://therecord.media/wp-content/uploads/2021/09/Patch-Tuesday.jpg)

Microsoft has released patches today for a zero-day vulnerability in one of the Windows components that was abused in the wild for attacks using weaponized Office documents.


[First disclosed last week](https://therecord.media/microsoft-warns-of-new-ie-zero-day-exploited-in-targeted-office-attacks/), when Microsoft warned of the attacks and published basic mitigations, the OS maker has released official fixes as today, part of its monthly [Patch Tuesday security updates](https://rawcdn.githack.com/campuscodi/Microsoft-Patch-Tuesday-Security-Reports/b433082c2156fbeb6f7c7d2d2720f3ecbc207b83/Reports/MSRC_CVEs2021-Sep.html).


Tracked as [CVE-2021-40444](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-40444), patches have been made available for Windows versions as far back as Windows 7 and Windows Server 2008.


The bug resides in the Microsoft MHTML component, also known as Trident, the old Internet Explorer browser engine. Microsoft said it discovered instances where a threat actor had created malicious Office files that used the MHTML component to load web-based content inside the documents, such as a malicious ActiveX control, which exploited CVE-2021-40444 to run code on the underlying Windows OS.


A successful attack allowed threat actors to gain control over a user’s OS, Microsoft said last week.


While no technical details were revealed last week, security researchers and malware developers quickly figured out what the issue was and published proof-of-concept code to exploit the bug was eventually on both GitHub and underground hacking forums, and the code has already been weaponized and integrated as part of [attacks](https://twitter.com/alex_lanstein/status/1437565704778223618) spotted this week.


 
Fortunately, today’s Office zero-day patch also comes just in time, as several security researchers discovered last week ways to bypass Microsoft’s temporary mitigation solutions [[1](https://twitter.com/GossiTheDog/status/1435570418623070210), [2](https://twitter.com/wdormann/status/1435951560006189060)], meaning that Windows users were fully exposed to these attacks without any kind of protection.


However, if the patches hold up remains to be seen. Several security researchers have publicly stated that the bug is buried deep enough in core Office behavior that attackers could easily find new ways to abuse this issue, creating another scenario similar to Microsoft’s PrintNightmare never-ending patching conundrum.


#### The September 2021 Patch Tuesday also fixes 85 other bugs


But besides fixes for CVE-2021, Microsoft has also released other security updates today, with patches for 85 other bugs, 48 of which are Edge/Chromium-related issues.


Of these, the most important appears to be [CVE-2021-36968](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-36968), an elevation of privilege in the Windows DNS service, for which details have been publicly shared on the internet.


“According to Microsoft, it is not being exploited in the wild,” said Allan Liska, threat intelligence analyst at Recorded Future. “It is labelled Important by Microsoft and, interestingly, only impacts Windows 7 and Windows Server 2008.”


Other issues to keep an eye on, and reasons to apply today’s patches as soon as possible, are [CVE-2021-36965](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-36965) and [CVE-2021-26435](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-26435), Liska said.





#### Tags:
[[Windows]] [[Microsoft]] [[The Record]]
