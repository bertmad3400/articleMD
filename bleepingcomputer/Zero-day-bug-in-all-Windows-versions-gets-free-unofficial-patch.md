# Zero-day bug in all Windows versions gets free unofficial patch
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/zero-day-bug-in-all-windows-versions-gets-free-unofficial-patch/)
+ Date: November 12, 2021
+ Author: Sergiu Gatlan


## Article:
![Zero-day bug in all Windows versions gets free unofficial patch](https://www.bleepstatic.com/content/hl-images/2021/07/09/Windows.jpg)


A free and unofficial patch is now available for a zero-day local privilege escalation vulnerability in the Windows User Profile Service that lets attackers gain SYSTEM privileges under certain conditions.


The bug, tracked as [CVE-2021-34484](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34484), was incompletely patched by Microsoft during the August Patch Tuesday. The company only addressed the impact of the proof-of-concept (PoC) provided by security researcher Abdelhamid Naceri who reported the issue.


Naceri later discovered that threat actors could still bypass the Microsoft patch to elevate privileges to gain SYSTEM privileges if certain conditions are met, getting an elevated command prompt while the User Account Control (UAC) prompt is displayed.


CERT/CC vulnerability analyst [Will Dormann](https://twitter.com/wdormann) tested the [CVE-2021-34484 bypass PoC exploit](https://twitter.com/KLINIX5/status/1451558296872173577) and found that, while it worked, it would not always create the elevated command prompt. However, in BleepingComputer's tests, it launched an elevated command prompt immediately, as shown below.


Luckily, the exploit requires attackers to know and log in with other users' credentials for exploiting the vulnerability, which means that it will likely not be as widely abused as other LPE bugs (including [PrintNightmare](https://www.bleepingcomputer.com/tag/printnightmare/)).


The bad news is that it impacts fully-updated devices running all Windows versions, including Windows 10, Windows 11, and Windows Server 2022.


Additionally, the researcher told BleepingComputer threat actors will only need another domain account to deploy the exploits in attacks, so it's definitely something admins should be concerned about.


After [BleepingComputer's report on the CVE-2021-34484 bypass](https://www.bleepingcomputer.com/news/security/all-windows-versions-impacted-by-new-lpe-zero-day-vulnerability/), Microsoft told us that they are aware of the issue and "will take appropriate action to keep customers protected."



![Exploit launching an elevated command prompt behind UAC prompt](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/CVE-2021-34484/elevated-command-prompt.jpg)*Exploit launching an elevated command prompt behind UAC prompt (BleepingComputer)*
Free patch available until Microsoft addresses the bug
------------------------------------------------------


While Microsoft is still working on a security update to address this zero-day flaw, the [0patch micropatching service](https://0patch.com/) has [released Thursday a free unofficial patch](https://twitter.com/0patch/status/1458545386243727361) (known as a micropatch).


0patch developed the micropatch using the info provided by Naceri in his write-up and PoC for the Windows User Profile Service 0day LPE.


You can apply this free patch to block attacks using the CVE-2021-34484 bypass on the following Windows versions:


1. **Windows 10 v21H1 (32 & 64 bit)** updated with October or November 2021 Updates
2. **Windows 10 v20H2 (32 & 64 bit)**updated with October or November 2021 Updates
3. **Windows 10 v2004 (32 & 64 bit)**updated with October or November 2021 Updates
4. **Windows 10 v1909 (32 & 64 bit)**updated with October or November 2021 Updates
5. **Windows Server 2019 64 bit** updated with October or November 2021 Updates


"While this vulnerability already has its CVE ID (CVE-2021-33742), we're considering it to be without an official vendor fix and therefore a 0day," 0patch co-founder Mitja Kolsek [explained](https://blog.0patch.com/2021/11/micropatching-incompletely-patched.html). "Micropatches for this vulnerability will be free until Microsoft has issued an official fix."


To install this unofficial patch on your system, you will first need to [register a 0patch account](https://central.0patch.com/) and then install the [0patch agent](https://0patch.com/).


Once you launch the agent, the micropatch is applied automatically (if there is no custom patching enterprise policy in place blocking it), without the need to reboot the device.


While this issue in theory also impacts older Windows versions, Kolsek said that "the vulnerable code is different there, making the window for winning the race condition extremely narrow and probably unexploitable."


A video demo of the CVE-2021-33742 micropatch in action is embedded below.





#### Tags:
[[Windows]] [[Microsoft]] [[0patch]] [[bit)]] [[Naceri]] [[CVE-2021-34484]] [[BleepingComputer]] [[micropatch]] [[Bleeping Computer]]
