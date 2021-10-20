# Political-themed actor using old MS Office flaw to drop multiple RATs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/political-themed-actor-using-old-ms-office-flaw-to-drop-multiple-rats/)
+ Date: October 20, 2021
+ Author: Bill Toulas


## Article:
![Hacker](https://www.bleepstatic.com/content/hl-images/2021/04/16/computer-hacker.jpg)


A novel threat actor with unclear motivesis running a crimeware campaign delivering multiple Windows and Android RATs (remote access tools) through the exploitation of CVE-2017-11882.


This [four-years-old Microsoft Office Equation Editor bug](https://www.bleepingcomputer.com/news/security/office-equation-editor-security-bug-runs-malicious-code-without-user-interaction/) was addressed in the November 2017 patch, but it appears that it's still available for leverage, especially in India and Afghanistan where the targets of this campaign are based.


The threat actor was spotted by researchers at [Cisco Talos](https://blog.talosintelligence.com/2021/10/crimeware-targets-afghanistan-india.html), who didn’t find any strong links to a particular nation, apart from a Pakistani IT front company named “Bunse Technologies”.


The actor has registered multiple domains that feature political themes such as diplomatic and humanitarian efforts and uses them to deliver malware payloads to the victims.


A worm-style threat
-------------------


The infection begins with the victim downloading a laced RTF (rich text document) file from one of the aforementioned websites, and if it’s opened on a vulnerable MS Office version, arbitrary code execution is triggered.


At first, a loader executable establishes its presence on the system by creating a Startup entry and compiles hard-coded C# code into an executable.



![On the fly compilation from source code](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/code%20compilation.png)**"On the fly" compilation from source code**  

Source: Cisco
The resulting binary is a custom file enumerator module that discovers all document files on the infected endpoint and sends a list with the file names and paths to the C2.


Finally, a file infector is also compiled which infects otherwise benign files such as DOCXs and EXEs, serving as a worm for the actors.



![DOCX file infector](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/docx_infector.png)**DOCX file infector module in action**  

Source: Cisco
This way, the infection can spread throughout a network as other users open the tampered files.


The payloads that are used in the monitored campaign are the following:


* Browser credential stealer for Brave, Google Chrome, Opera, Opera GX, Microsoft Edge, YandexBrowser, and Mozilla Firefox.
* DcRAT, featuring remote shells, keylogging, file, and process management.
* QuasarRAT, featuring credential stealing, arbitrary command execution, remote shell, and file management.
* AndroRAT, for Android smartphone targeting.


Moderate attribution confidence
-------------------------------


At the time of writing this, the site for Bunse Technologies has been taken down, but BleepingComputer was able to an associated Twitter account.



![Bunse Technologies account on Twitter](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Bunse Technologies account on Twitter**
The CEO of the firm promotes himself as a penetration tester and ethical hacker, and posts nationalistic anti-India and pro-Taliban content on his personal Facebook account.


Talos was able to find GitHub repositories belonging to the person, and one of them contained the DcRat source code. As such, the attribution to the particular individual is moderately confident.



![GitHub repository](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Actor's GitHub repository**  

Source: Cisco
Although the actor is generally using commodity malware in this campaign, the appearance of custom downloaders and file infectors is a sign that they are looking to shift away from using detectable tools.


Organizations in Afghanistan and India should remain vigilant against threats of this kind, which can spread rapidly and stealthily inside their networks.




#### Tags:
[[Source:]] [[Bleeping Computer]]
