# Microsoft warns of weeks-long malspam campaign abusing HTML smuggling
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/microsoft-warns-of-weeks-long-malspam-campaign-abusing-html-smuggling/)
+ Date: July 26, 2021
+ Author: Catalin Cimpanu


## Article:
![Microsoft warns of weeks-long malspam campaign abusing HTML smuggling](https://therecord.media/wp-content/uploads/2021/07/email-spam.jpg)

The Microsoft security team said it detected a weeks-long email spam campaign abusing a technique known as “**HTML smuggling**” to bypass email security systems and deliver malware to user devices.


HTML smugging, as explained by [SecureTeam](https://secureteam.co.uk/articles/information-assurance/what-is-html-smuggling/) and [Outflank](https://outflank.nl/blog/2018/08/14/html-smuggling-explained/), is a technique that allows threat actors to assemble malicious files on users’ device by clever use of HTML5 and JavaScript code.


The general idea behind an email-based HTML smuggling attack is to include a link to a file inside an email that, when scanned, does not look malicious, nor does it point to a file type that email security tools consider dangerous, such as EXE, DOC, MSI, and others.


However, the technique uses different HTML attributes such as “href” and “download,” along with JavaScript code to assemble the malicious file inside the user’s browser when they access the link.


As shown in the image below, spotted in recent attacks by Microsoft, the idea is to point the link via a “href” attribute to an octet stream that is assembled via JavaScriot inside the final file mentioned in the “download” attribute.


![HTML-smuggling](https://www-therecord.recfut.com/wp-content/uploads/2021/07/HTML-smuggling-1024x383.png)Image: Microsoft
The technique is not new and has been known at a theoretical level since the mid-2010s and abused by malware operators since [at least 2019](https://www.gdatasoftware.com/blog/2019/05/31695-strange-bits-smuggling-malware-github) and also spotted [throughout 2020](https://www.menlosecurity.com/blog/new-html-smuggling-attack-alert-duri/).


In a series of tweets on Friday, Microsoft said it’s been tracking an email spam campaign that has been going on for weeks that has been abusing HTML smuggling to drop a malicious ZIP file on user devices.


However, files contained inside the ZIP file will infect users with [Casbaneiro (Metamorfo)](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/), a banking trojan strain that targets Latin American users.





While Microsoft said Microsoft Defender for Office 365 could detect files dropped via HTML smuggling, the OS maker raised a sign of alarm on Friday for users who are not its customers or do not use email security products to scan incoming emails and who may not be aware of the technique.





#### Tags:
[[Microsoft]] [[HTML]] [[The Record]]
