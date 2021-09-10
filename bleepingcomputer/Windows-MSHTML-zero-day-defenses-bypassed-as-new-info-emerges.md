# Windows MSHTML zero-day defenses bypassed as new info emerges
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-mshtml-zero-day-defenses-bypassed-as-new-info-emerges/)
+ Date: September 9, 2021
+ Author: Lawrence Abrams


## Article:
![Microsoft](https://www.bleepstatic.com/content/hl-images/2021/03/18/microsoft-fire.jpg)


New details have emerged about the recent Windows CVE-2021-40444 zero-day vulnerability, how it is being exploited in attacks, and the threat actor's ultimate goal of taking over corporate networks.


This Internet Explorer MSHTML remote code execution vulnerability, tracked as CVE-2021-40444, was [disclosed by Microsoft on Tuesday](https://www.bleepingcomputer.com/news/security/microsoft-shares-temp-fix-for-ongoing-office-365-zero-day-attacks/) but with few details as it has not been patched yet.


The only information shared by Microsoft was that the vulnerability uses malicious ActiveX controls to exploit Office 365 and Office 2019 on Windows 10 to download and install malware on an affected computer.


Since then, researchers have found the malicious Word documents used in the attacks and have learned new information about how the vulnerability is exploited.


Why the CVE-2021-40444 zero-day is so critical
----------------------------------------------


Since the release of this vulnerability, security researchers have taken to Twitter to warn how dangerous it is even though Microsoft Office's 'Protected View' feature will block the exploit.


When Office opens a document it checks if it is tagged with a "[Mark of the Web](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/)" (MoTW), which means it originated from the Internet.


If this tag exists, Microsoft will open the document in read-only mode, effectively blocking the exploit unless a user clicks on the 'Enable Editing' buttons.



![Word document opened in Protected View](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/CVE-2021-40444/protected-view-maldoc.jpg)**Word document opened in Protected View**
As the "Protected View" feature mitigates the exploit, we reached out to [Will Dormann](https://twitter.com/wdormann), a vulnerability analyst for CERT/CC, to learn why security researchers are so concerned about this vulnerability.


Dormann told BleepingComputer that even if the user is initially protected via Office's 'Protected View' feature, history has shown that many users ignore this warning and click on the 'Enable Editing' button anyway.


Dormann also warns that there are numerous ways for a document not to receive the MoTW flag, effectively negating this defense.



> 
> "If the document is in a container that is processed by something that is not MotW-aware, then the fact that the container was downloaded from the Internet will be moot. For example, if 7Zip opens an archive that came from the Internet, the extracted contents will have no indication that it came from the Internet. So no MotW, no Protected View."
> 
> 
> "Similarly, if the document is in a container like an ISO file, a Windows user can simply double-click on the ISO to open it. But Windows doesn't treat the contents as having come from the Internet. So again, no MotW, no Protected View."
> 
> 
> "This attack is more dangerous than macros because any organization that has chosen to disable or otherwise limit Macro execution will still be open to arbitrary code execution simply as the result of opening an Office document." - Will Dormann
> 
> 
> 


To make matters even worse, Dormann discovered that you could use this vulnerability in RTF files, which do not benefit from Office's Protected View security feature.




> 
> Inspired by [@buffaloverflow](https://twitter.com/buffaloverflow?ref_src=twsrc%5Etfw), I tested out the RTF attack vector. And it works quite nicely.  
> 
> WHERE IS YOUR PROTECTED MODE NOW? [pic.twitter.com/qf021VYO2R](https://t.co/qf021VYO2R)
> 
> 
> — Will Dormann (@wdormann) [September 9, 2021](https://twitter.com/wdormann/status/1435951560006189060?ref_src=twsrc%5Etfw)


Microsoft has also [shared mitigations](http://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40444) to prevent ActiveX controls from running in Internet Explorer, effectively blocking the current attacks.


However, security researcher Kevin Beaumont has already [discovered a way](https://twitter.com/GossiTheDog/status/1435570418623070210) to bypass Microsoft's current mitigations to exploit this vulnerability.


With these bypasses and additional use cases, CVE-2021-40444 has become even more severe than initially thought.


How CVE-2021-40444 is currently used in attacks
-----------------------------------------------


While we do not have the actual phishing emails used in the attacks, Beaumont has analyzed the malicious Word document to understand better how the exploit works.




> 
> Looks like this has been in the wild for a week or more. Uses the daft as F feature that allows Word to load a template from internet, that spawns IE and then trusts JS and ActiveX controls, then uses ../.. (yes it's 1999) to spawn .cpl file <https://t.co/mOvaN9YLj6> [pic.twitter.com/xLf2jVWyY5](https://t.co/xLf2jVWyY5)
> 
> 
> — Kevin Beaumont (@GossiTheDog) [September 8, 2021](https://twitter.com/GossiTheDog/status/1435562870331293706?ref_src=twsrc%5Etfw)


One of the known malicious Word attachments used in the attacks is named 'A Letter before court 4.docx' [[VirusTotal](https://www.virustotal.com/gui/file/938545f7bbe40738908a95da8cdeabb2a11ce2ca36b0f6a74deda9378d380a52/relations%20-%20A%20Letter%20before%20court%204.docx)] and claims to be a letter from an attorney.


Since the file was downloaded from the Internet, it will be tagged with the 'Mark of the Web' and opened in Protected View, as shown below.



![Malicious Word document for the CVE-2021-40444 exploit](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/CVE-2021-40444/malicious-word-document.jpg)**Malicious Word document for the CVE-2021-40444 exploit**
Once a user clicks on the 'Enable Editing' button, the exploit will open an URL using the 'mhtml' protocol to a 'side.html' [[VirusTotal](https://www.virustotal.com/gui/file/d0fd7acc38b3105facd6995344242f28e45f5384c0fdf2ec93ea24bfbc1dc9e6)] file hosted at a remote site, which is loaded as a Word template.


As 'mhtml' URLs are registered to Internet Explorer, the browser will be started to load the HTML, and its obfuscated JavaScript code will exploit the CVE-2021-40444 vulnerability by creating a malicious ActiveX control.



![Obfuscated JavaScript in side.html file](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Obfuscated JavaScript in side.html file**
This ActiveX control will download a ministry.cab [[VirusTotal](https://www.virustotal.com/gui/file/1fb13a158aff3d258b8f62fe211fabeed03f0763b2acadbccad9e8e39969ea00)] file from a remote site, extract a championship.inf [[VirusTotal](https://www.virustotal.com/gui/file/bd4b9f4b79f8a9eedc12abe3919cecb041c61022485b87b3a5cdfd1891e30670)] file (actually a DLL), and execute it as a Control Panel 'CPL' file, as illustrated in the image below from a [Trend Micro report](https://www.trendmicro.com/en_us/research/21/i/remote-code-execution-zero-day--cve-2021-40444--hits-windows--tr.html).



![Executing the championship.inf files as a CPL file](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Executing the championship.inf files as a CPL file**
TrendMicro states that the ultimate payload is installing a Cobalt Strike beacon, which would allow the threat actor to gain remote access to the device.


Once the attacker gains remote access to victims' computers, they can use it to spread laterally throughout the network and install further malware, steal files, or deploy ransomware.


Due to the severity of this vulnerability, it is strongly advised that users only open attachments unless they come from a trusted source.


While Microsoft's Patch Tuesday is next week, it is unclear if Microsoft will have enough time to fix the bug and adequately test it by then.




#### Tags:
[[Microsoft]] [[CVE-2021-40444]] [[ActiveX]] [[Dormann]] [[Windows]] [[vulnerability,]] [[[VirusTotal]]] [[Internet.]] [[Bleeping Computer]]
