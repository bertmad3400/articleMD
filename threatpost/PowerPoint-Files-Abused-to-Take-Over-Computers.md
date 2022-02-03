# PowerPoint Files Abused to Take Over Computers
### Attackers are using socially engineered emails with .ppam file attachments that hide malware that can rewrite Windows registry settings on targeted machines.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178182
+ Date: 2022-02-03T14:00:25+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2020/04/08162616/PowerPoint_Mouse.jpg)

Attackers are using an under-the-radar PowerPoint file to hide malicious executables that can rewrite Windows registry settings to take over an end user’s computer, researchers have found.


It’s one of a number of stealthy ways threat actors recently have been targeting desktop users through trusted applications they use daily, using emails that are designed to evade security detections and appear legitimate.


New research from Avanan, a Check Point company, has uncovered how a “little-known add-on” in PowerPoint – the .ppam file – is being used to hide malware. Jeremy Fuchs, cybersecurity researcher and analyst at Avanan, wrote in [a report published](https://www.avanan.com/blog/using-.ppam-files-to-wrap-executable-content) Thursday that the file has bonus commands and custom macros, among other functions.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Beginning in January, researchers observed attackers delivering socially engineered emails that include .ppam file attachments with malicious intent.


**Email Attack Vector**
-----------------------


One email observed in the campaign, for example, purported to be sending the recipient a purchase order. The attached .ppam file – named PO04012022 to appear legitimate – included a malicious executable, Fuchs said.


The payload executed a number of functions on the end user’s machine that were not authorized by the user, including installing new programs that create and open new processes, changing file attributes, and dynamically calling imported functions.


“By combining the potential urgency of a purchase order email, along with a dangerous file, this attack packs a one-two punch that can devastate an end-user and a company,” Fuchs wrote.


The campaign allows attackers to bypass a computer’s existing security – in this case, security provided by Google – with a file that’s rarely used and thus won’t trip an email scanner, he said.


“Plus, it shows the potential dangers of this file, as it can be used to wrap any sort of malicious file, including ransomware,” Fuchs wrote.


Indeed, in October, reports surfaced that attackers were using .ppam files to wrap ransomware, he said, citing [a report](https://www.pcrisk.com/removal-guides/14314-ppam-ransomware#:~:text=Discovered%20by%20Petrovic%2C%20Ppam%20is,placing%20it%20in%20all%20folders.) on the Ppam ransomware published in October by the cybersecurity portal [PCrisk](https://www.pcrisk.com/).


**Targeting Desktop Users**
---------------------------


The latest scam is one of several new email-based campaigns uncovered by researchers recently to target desktop users working on commonly used word-processing and collaboration apps like Microsoft Office, Google Docs and Adobe Creative Cloud. Attackers typically use email to deliver malicious files or links that steal user information.


In November, reports surfaced that scammers were using [a legitimate Google Drive collaboration feature](https://threatpost.com/scammers-google-drive-malicious-links/160832/) to trick users into clicking on malicious links in emails or push notifications that invited people to share a Google document. The links directed users to websites that stole their credentials.


Then a wave of phishing attacks that Avanan researchers [identified in December](https://threatpost.com/attackers-exploit-flaw-google-docs-comments/177412/) targeted mainly Outlook users, leveraging the “Comments” feature of Google Docs to send malicious links that also lifted credentials from victims.


Last month, the Avanan team reported on another scam that researchers observed in December in which threat actors were found [creating accounts within the Adobe Cloud suite](https://threatpost.com/adobe-cloud-steal-office-365-gmail-credentials/177625/) and sending images and PDFs that appear legitimate but instead deliver malware to Office 365 and Gmail users.


**Mitigations and Prevention**
------------------------------


To avoid allowing email scams to slip past corporate users, Fuchs recommended some typical precautions to security administrators that should be implemented consistently.


One is to install email protection that downloads all files into a sandbox and to inspect them for malicious content. Another is to take extra security steps – such as dynamically analyzing emails for indicators of compromise (IoCs) – to ensure the safety of messages coming into the corporate network, he said.


“This email failed an SPF check and there was an insignificant historical reputation with the sender,” Fuchs wrote of the phishing message observed by Avanan researchers. SPF, Sender Policy Framework, is an email authentication technique used to prevent spammers and other bad actors from sending messages spoofed to come from another domain name.


Corporations also should continuously encourage end users in their networks to contact their IT department if they see an unfamiliar file come over via email, he added.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=RTM]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Fuchs]] [[Avanan]] [[Google]] [[Emails]] [[Ppam]] [[Cybersecurity]] [[ThreatPost]]

