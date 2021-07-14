# Detonating Ransomware on My Own Computer (Don’t Try This at Home)
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/detonating-ransomware-on-my-own-computer-don-t-try-this-at-home/)
+ Date: July 14, 2021
+ Author: Acronis


## Article:
![Ransomware](https://www.bleepstatic.com/content/hl-images/2020/11/03/Ransomware.jpg)


*This article was written by [Topher Tebow](https://twitter.com/TopherTebow), a senior cybersecurity researcher at [Acronis](https://acronis.com/?utm_source=securityboulevard&utm_medium=referral&utm_campaign=fy21-q2-securityboulevard-sp) with a focus on malware tracking and analysis.*


Headlines of [ransomware attacks](https://www.acronis.com/en-us/solutions/business/ransomware-protection/?utm_source=bleepingcomputer&utm_medium=referral&utm_campaign=fy21-q2-bleepingcomputer-sp) seem to be a daily occurrence, announcing new levels of danger and confusion to the already complicated business of protecting data. One such threat is Conti, which is often used to target healthcare organizations and retailers.


How it behaves can tell us lot about a modern ransomware attack – so I recently detonated Conti ransomware in a controlled environment to demonstrate the importance of proper cyber protection.


Preparing the attack
--------------------


I used three virtual machines in this attack to simulate different scenarios. The first machine was a clean install of Windows with no protection in place. This machine shows the capabilities of the ransomware. The other two machines had either ransomware protection in place to remediate the attack, or URL filtering to prevent the malicious payload from being installed.


Process Monitor and Process Explorer from the SysInternals Suite helped me keep an eye on the [ransomware](https://www.acronis.com/en-us/products/cyber-protect/?utm_source=bleepingcomputer&utm_medium=referral&utm_campaign=fy21-q2-bleepingcomputer-sp) activity throughout the attack. Naturally there are normal processes, but also processes spun up by the ransomware, as well as registry changes.


As the attack vector, I created a fake malicious email based on a tax-related invoice to mimic a common phishing lure. The email was based on a real email, so it looked legitimate. After a quick update to the email settings, it even showed the company name as the sender. I used official logos and colors, but replaced the invoice details with a download link to ensure someone who might be expecting such an email would interact with the one I crafted instead of just viewing it.


The link used a trusted file sharing service to download an “invoice” with an embedded Visual Basic script that downloads and runs the ransomware automatically.


Normally a victim would have to enable active content before this script will run, so attackers will often set content to be hidden until this point. In this case, I planned to ransom myself, so I set Word to run the content automatically. This is a simple setting change, and should not be overlooked as a possible vulnerable point on company networks.


Demolition
----------


My attack starts with the prepared email being sent to the “victim”, who clicks the link in the email that downloads a document from the trusted file sharing service. The Visual Basic script runs as soon as the document opens, pulling down the ransomware and running it automatically.


A few seconds later, the ransomware file can be seen in Process Explorer as a subprocess of WINWORD.EXE. The Windows Registry shows queries from the ransomware, beginning with CurrentControlSet entries, before moving on to restart settings which indicates that Conti is looking for a way to gain persistence on the system.


The machine starts running slowly as the ransomware encrypts files. If the user does not notice that there is something wrong, Conti will continue to encrypt new files added to the machine.



![From SPAM email to encryption](https://www.bleepstatic.com/images/news/ransomware/d/detonate/phishing-email-tt.jpg)**From SPAM email to encryption**
While slower system performance might be the first sign of a problem, there are some other indicators. Others include file extensions change with '.ZSSCI' appended to the file names (though different ransomware will use different extensions), and the file icons are changed to a blank page icon because the file type is no longer recognized. For Conti and most other modern ransomware, a readme.txt file is placed in any directory where files were encrypted.


The readme.txt file is the ransom note informing the victim of the attack, and providing payment instructions. Gone are the days of flashy ransom notes that replace the desktop background or web pages opened with a scary message and lots of bad gif images. Here we see that a .onion address is used to contact the attacker, which requires the use of a Tor browser, with an HTTPS alternative on the clear web.


The attacker also threatens to publish stolen data if ignored, in the spirit of the double-extortion methods being employed by the majority of ransomware gangs these days.



![Conti ransom note](https://www.bleepstatic.com/images/news/ransomware/d/detonate/ac-ransom-note.jpg)**Conti ransom note**
Necessity is the mother of invention
------------------------------------


At this point, there are few ways to get your data back. You could pay the ransom and hope the decryption key works, restore from clean backups if you have them, or find a time machine. Instead of funding criminals, shutting down during a recovery period, or inventing time travel, there are realistic ways to avoid becoming a victim.


Since no single approach can solve every problem, a multi-layered solution will be the most effective way to keep your data safe from this type of attack.


Organizations have stepped up their phishing training in recent years, which is a fantastic first step. Unfortunately, even the most well-trained individuals can be fooled by a well-crafted attack. It’s therefore imperative to have tools implemented to prevent the attack. Let’s take a look at what happens with protection in place.


With ransomware protection in place, the attack started out looking very similar to the attack on the unprotected system – up to a point. Conti still ran, accessed the registry, and began encrypting files. But then Conti suddenly closed and the Word document opens safely.


The difference this time was that the file entropy was being monitored and the software stopped the processes started up by Conti after only eight files were encrypted. The ransomware protection software automatically restored the encrypted from cached copies that were generated when the encryption began, saving the hassle and downtime associated with restoring from backups.



![Acronis Cyber Protect detecting malware](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Acronis Cyber Protect detecting malware**
Of course, stopping the attack before a payload is installed is always a preferred option. An advanced email security solution can prevent malicious emails from reaching your end-users, while a proper URL filter blocks access to known malicious URLs where payloads are be downloaded from.


No matter how complicated it is to protect an organization’s data, simulating an attack shows us that not all hope is lost. Through education, planning, and diligence, we can fight off these attacks by recognizing the signs of a possible attack, and implementing multi-layered solutions to automate the detection and response to attacks that come our way.


Start building your own multilayered protection plan with the unique integration of backup, disaster recovery, cybersecurity, and endpoint management in [Acronis Cyber Protect](http://(https://www.acronis.com/en-us/products/cyber-protect/?utm_source=bleepingcomputer&utm_medium=referral&utm_campaign=fy21-q2-bleepingcomputer-big-sp-ransomware).


*[Topher Tebow](http://twitter.com/TopherTebow) is a senior cybersecurity researcher at [Acronis](https://acronis.com/?utm_source=securityboulevard&utm_medium=referral&utm_campaign=fy21-q2-securityboulevard-sp) with a focus on malware tracking and analysis. Topher spent nearly a decade combating web-based malware before moving into endpoint protection. He has written technical content for several companies, covering topics from security trends and best practices, to the analysis of malware and vulnerabilities.* 


*In addition to being published in industry publications like Cyber Defense Magazine and Security Boulevard, Topher has contributed to articles by several leading publications.*




#### Tags:
[[ransomware]] [[Conti]] [[malware]] [[Topher]] [[Acronis]] [[cybersecurity]] [[Bleeping Computer]]
