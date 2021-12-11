# Phishing attacks use QR codes to steal banking credentials
### A new phishing campaign that targets German e-banking users has been underway in the last couple of weeks, involving QR codes in the credential-snatching process.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/phishing-attacks-use-qr-codes-to-steal-banking-credentials/
+ Date: 2021-12-10T14:10:05-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/10/german_flag.jpg)

![Sophisticated phishing actors target Germans with QR codes](https://www.bleepstatic.com/content/hl-images/2021/12/10/german_flag.jpg?rand=122223843)


A new phishing campaign that targets German e-banking users has been underway in the last couple of weeks, involving QR codes in the credential-snatching process.


The actors are using a range of tricks to bypass security solutions and convince their targets to open the messages and follow the instructions.


The relevant report comes from researchers at [Cofense](https://cofense.com/blog/german-users-targeted-in-digital-bank-heist-phishing-campaigns/), who sampled several of these messages and mapped the actors' tactics in detail.


A clean delivery
----------------


The phishing emails are carefully crafted, featuring bank logos, well-structured content, and a generally coherent style.


Their topics vary, from asking the user to consent to data policy changes implemented by the bank or requesting them to review new security procedures.



![Phishing email impersonating a German bank](https://www.bleepstatic.com/images/news/u/1220909/Phishing/email(2).png)**Phishing email impersonating a German bank**  
*Source: Cofense*
This approach is a sign of careful planning, where the actors aren’t making the typical overblown claims of account compromise and don’t present the user with an urgent situation.


If the embedded button is clicked, the victim arrives at the phishing site after passing through Google’s feed proxy service 'FeedBurner.'



![Button leading to a re-direction through FeedBurner](https://www.bleepstatic.com/images/news/u/1220909/Phishing/redirection.png)**Button leading to a re-direction through FeedBurner**  
*Source: Cofense*
Additionally, the actors register their own custom domains that are used for these re-directions as well as for the phishing sites themselves.


This extra step aims to trick email and internet security solutions into not raising any flags during the phishing process.


The domains are newly registered sites on the REG.RU Russian registrar and follow a standard URL structure depending on the targeted bank.


Scan this QR code to give us your credentials
---------------------------------------------


In the most recent phishing campaigns, the threat actors use QR codes instead of buttons to take victims to phishing sites.


These emails do not contain clear-text URLs and are instead obfuscated through the QR codes, making it hard for security software to detect them.



![Email with QR code leading to phishing site](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Email with QR code leading to phishing site**  
*Source: Cofense*
QR codes have increased effectiveness as they are targeting mobile users, who are less likely to be protected by internet security tools.


Once the victim arrives on the phishing site, they are requested to enter their bank location, code, user name, and PIN.



![Login page on phishing site](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Login page on phishing site**  
*Source: Cofense*
If these details are entered on the phishing page, the user waits for validation and then is prompted to enter their credentials again due to them being incorrect.



![Verification screen on phishing site](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Verification screen on phishing site**  
*Source: Cofense*
This repetition is a common quality tactic in phishing campaigns to eliminate typos when the user enters their credentials the first time.


No matter how legitimate an email may look, you should avoid clicking on buttons, URLs, or even QR codes that will take you to an external site.


Whenever you are requested to enter your account credentials, always remember to first validate the domain you are on before you start typing.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Phishing]] [[Cofense]] [[Sitesource]] [[Bleeping Computer]]

