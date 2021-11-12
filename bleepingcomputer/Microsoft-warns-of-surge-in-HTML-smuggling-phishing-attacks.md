# Microsoft warns of surge in HTML smuggling phishing attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-surge-in-html-smuggling-phishing-attacks/)
+ Date: November 12, 2021
+ Author: Bill Toulas


## Article:
![javascript](https://www.bleepstatic.com/content/hl-images/2021/11/12/javascript.jpg?rand=1127599119)


Microsoft has seen a surge in malware campaigns using HTML smuggling to distribute banking malware and remote access trojans (RAT).


While HTML smuggling is not a new technique, Microsoft is seeing it increasingly used by threat actors to evade detection, including the [Nobelium hacking group](https://www.bleepingcomputer.com/news/security/microsoft-russian-svr-hackers-target-govt-agencies-from-24-countries/) behind the SolarWinds attacks.


How HTML smuggling works
------------------------


HTML smuggling is a technique used in phishing campaigns that use HTML5 and JavaScript to hide malicious payloads in encoded strings in an HTML attachment or webpage. These strings are then decoded by a browser when a user opens the attachment or clicks a link.


For example, a phishing HTML attachment could include a harmless link to a known website, thus not being seen as malicious. However, when a user clicks on the link, JavaScript will decode an included encrypted or encoded string and convert it into a malicious attachment that is downloaded instead, as shown in the code below.



![A basic example of HTML smuggling](https://www.bleepstatic.com/images/news/security/html-smuggling-example.jpg)**A basic example of HTML smuggling**  
*Source: Microsoft*
Since the malicious payload is encoded initially, it looks harmless to security software and is not detected as malicious. Furthermore, as JavaScript assembles the payload on the target system, it bypasses any firewalls and security defenses that would usually catch the malicious file at the perimeter.



![HTML smuggling malware drop process](https://www.bleepstatic.com/images/news/u/1220909/Security/diagram(1).jpg)**HTML smuggling malware drop process**  
*Source: Microsoft*
Deployment cases
----------------


[Microsoft researchers](https://www.microsoft.com/security/blog/2021/11/11/html-smuggling-surges-highly-evasive-loader-technique-increasingly-used-in-banking-malware-targeted-attacks/) have seen this technique used in Mekotio campaigns that deliver banking trojans and also in highly-targeted NOBELIUM attacks.


HTML smuggling campaigns are also used to drop the AsyncRAT or NJRAT remote access trojans, or the TrickBot trojan used to breach networks and deploy ransomware.


The attacks usually start with a phishing email containing an HTML link in the body of the message or a malicious HTML file as an attachment.


If either is clicked, a ZIP file is dropped using HTML smuggling. This archive contains a JavaScript file downloader that fetches additional files from a command and control server (C2) to install on the victim's device.


In some cases, the created archives are password-protected for additional detection evasion against endpoint security controls. However, the password to open it is provided in the original HTML attachment, so the victim must enter it manually.



![Password provided in the email or HTML attachment](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Password provided in the email or HTML attachment**  
*Source: Microsoft*
Once the script is launched, a base64-encoded PowerShell command is executed that downloads and installs the TrickBot trojan or other malware.


A 2020 report from [Menlo Security](https://secureteam.co.uk/articles/information-assurance/what-is-html-smuggling/) also mentions the Duri malware group as one of the actors who actively uses HTML smuggling for payload distribution, but the technique was first seen in the wild since at least 2018.


Microsoft first warned about a sudden uptick in this activity in [July 2021](https://twitter.com/MsftSecIntel/status/1418706916922986504), urging admins to raise their defenses against it.


How to defend against HTML smuggling
------------------------------------


Microsoft suggests admins use behavior rules to check for commonly characteristics of HTML smuggling, including:


* An attached ZIP file contains JavaScript
* An attachment is password-protected
* An HTML file contains a suspicious script code
* An HTML file decodes a Base64 code or obfuscates a JavaScript


For endpoints, admins should block or audit activity associated with HTML smuggling, including:


* Block JavaScript or VBScript from launching downloaded executable content
* Block execution of potentially obfuscated scripts
* Block executable files from running unless they meet a prevalence, age, or trusted list criterion


In addition to the above, users may prevent automatic JavaScript code execution by associating .js and .jse files with a text editor like Notepad.


Ultimately, the best defense is to train users not to open files downloaded via links in emails and attachments. All files downloaded from an email should be treated with caution and checked carefully before being opened.


Furthermore, if an attachment or email link downloads an attachment ending with a .js extension (JavaScript), it should never be opened and automatically be deleted.


Unfortunately, Windows disables the showing of file extensions by default, leading to extensions not being seen in many cases. This is why it is [always suggested](https://www.bleepingcomputer.com/news/microsoft/hiding-windows-file-extensions-is-a-security-risk-enable-now/) that users enable the viewing of file extensions to prevent the opening of malicious files.




#### Tags:
[[HTML]] [[Microsoft]] [[JavaScript]] [[malware]] [[phishing]] [[admins]] [[Bleeping Computer]]
