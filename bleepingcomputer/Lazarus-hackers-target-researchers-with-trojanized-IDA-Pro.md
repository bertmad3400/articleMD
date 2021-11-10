# Lazarus hackers target researchers with trojanized IDA Pro
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/lazarus-hackers-target-researchers-with-trojanized-ida-pro/)
+ Date: November 10, 2021
+ Author: Lawrence Abrams


## Article:
![North Korea](https://www.bleepstatic.com/content/hl-images/2021/10/26/north_korean_flag.jpg)


A North Korean state-sponsored hacking group known as Lazarus is again trying to hack security researchers, this time with a trojanized pirated version of the popular IDA Pro reverse engineering application.


IDA Pro is an application that converts an executable into assembly language, allowing security researchers and programmers to analyze how a program works and discover potential bugs.


Security researchers commonly use IDA to analyze legitimate software for vulnerabilities and malware to determine what malicious behavior it performs.


However, as IDA Pro is an expensive application, some researchers download a pirated cracked version instead of purchasing it.


As with any pirated software, there is always the risk of it being tampered modified to include malicious executables, which is precisely what ESET researcher [Anton Cherepanov](https://twitter.com/cherepanov74) discovered in a pirated version of IDA Pro distributed by the Lazarus hacking group.


Trojanized IDA Pro targets security researchers
-----------------------------------------------


Today, [ESET tweeted](http://twitter.com/ESETresearch/status/1458438155149922312) about a malicious version of IDA Pro 7.5 discovered by [Cherepanov](https://twitter.com/cherepanov74) that is being distributed online to target security researchers.


This IDA installer has been modified to include two malicious DLLs named **idahelp.dll** and **win\_fw.dll** that will be executed when the program is installed.



![Malicious DLLs added to pirated IDA Pro](https://www.bleepstatic.com/images/news/security/attacks/l/lazarus/fake-ida-pro/dir-list.jpg)**Malicious DLLs added to pirated IDA Pro**  
*Source: ESET*
The win\_fw.dll file will create a new task in the Windows Task Scheduler that launches the idahelper.dll program.



![New SRCheck scheduled task created by win_fw.dll](https://www.bleepstatic.com/images/news/security/attacks/l/lazarus/fake-ida-pro/lazarus-task-scheduler.jpg)**New SRCheck scheduled task created by win\_fw.dll**  
*Source: ESET*
The idahelper.dll will then connect to the devguardmap[.]org site and download payloads believed to be the NukeSped remote access trojan. The installed RAT will allow the threat actors to gain access to the security researcher's device to steal files, take screenshots, log keystrokes, or execute further commands.


"Based on the domain and trojanized application, we attribute this malware to known Lazarus activity, previously reported by Google's Threat Analysis Group and Microsoft," ESET tweeted regarding connection to Lazarus.


Cherepanov told BleepingComputer that while he does not know how the installer is being distributed, it was discovered recently and appears to have been distributed since Q1 2020


Lazarus has a history of targeting researchers
----------------------------------------------


The Lazarus hacking group, also [known as Zinc by Microsoft](https://www.bleepingcomputer.com/news/security/microsoft-dprk-hackers-likely-hit-researchers-with-chrome-exploit/), has a long history of targeting security researchers with backdoors and remote access trojans.


In January, Google disclosed that [Lazarus conducted a social media campaign](https://www.bleepingcomputer.com/news/security/north-korean-hackers-are-targeting-security-researchers-with-malware-0-days/) to create fake personas pretending to be vulnerability researchers.



![Fake online security researcher personas](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Fake online security researcher personas**
Using these personas, the hacking group would contact other security researchers about potential collaboration in vulnerability research.


After establishing contact with a researcher, the hackers would send Visual Studio projects related to an alleged 'vulnerability,' which contained a malicious hidden DLL named 'vcxproj.suo.'


When the researcher attempted to build the project, a pre-build event would execute the DLL, which acted as a custom backdoor installed on the researcher's device.


Other [Lazarus attacks also used an Internet Explorer zero-day](https://www.bleepingcomputer.com/news/security/hacking-group-also-used-an-ie-zero-day-against-security-researchers/) to deploy malware on security researcher's devices when they visited links sent by the attackers.



![Exploiting the Lazarus zero-day in Internet Explorer](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Exploiting the Lazarus zero-day in Internet Explorer**
While it was never determined what the ultimate goal was for these attacks, it was likely to steal undisclosed security vulnerabilities and exploits that the hacking group could use in their own attacks.




#### Tags:
[[ESET]] [[malware]] [[Cherepanov]] [[Bleeping Computer]]
