# Microsoft warns of multi-stage phishing campaign leveraging Azure AD
### Microsoft's threat analysts have uncovered a large-scale, multi-phase phishing campaign that uses stolen credentials to register devices onto the target's network and use them to distribute phishing emails.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/microsoft-warns-of-multi-stage-phishing-campaign-leveraging-azure-ad/
+ Date: 2022-01-27T13:11:58-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/10/20/Microsoft_365_red.jpg)

![Microsoft warns of multi-stage phishing campaign leveraging Azure AD](https://www.bleepstatic.com/content/hl-images/2021/10/20/Microsoft_365_red.jpg?rand=62773040)


Microsoft's threat analysts have uncovered a large-scale, multi-phase phishing campaign that uses stolen credentials to register devices onto the target's network and use them to distribute phishing emails.


As the report highlights, the attacks manifested only through accounts that didn't have multi-factor authentication (MFA) protection, which made them easier to hijack.


The lures used for this purpose are DocuSign-themed emails that urge the recipient to review and sign the attached document.



![DocuSign lure sent in the first wave of the attack](https://www.bleepstatic.com/images/news/u/1220909/Phishing/docusign.jpg)**DocuSign lure sent in the first wave of the attack**  
*Source: Microsoft*
The embedded links take the victim to a phishing URL that imitates the Office 365 login page and pre-fills the victim's username for increased credibility.


The recipients of the second wave of emails are employees of the targeted firm and external targets such as contractors, suppliers, partners, etc.


Because these emails come from a trusted workspace, they aren't flagged by security solutions and carry an intrinsic element of legitimacy that boosts the actors' chances of success.



![Phishing attack chain](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/diagram(4).jpg)**Phishing attack chain**  
*Source: Microsoft*
A spam filter that wasn't
-------------------------


Microsoft's telemetry data indicates that the first phase of the attacks focused mainly on firms located in Australia, Singapore, Indonesia, and Thailand.


The actors attempted to compromise remote working employees, poorly protected managed service points, and other infrastructure that may operate outside strict security policies.


Microsoft's analysts were able to spot the threat by detecting anomalous creation of inbox rules, which actors did immediately after gaining control of a device part of the corporate network.


"Leveraging the Remote PowerShell connection, the attacker implemented an inbox rule via the New-InboxRule cmdlet that deleted certain messages based on keywords in the subject or body of the email message," -  [the report details.](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa/)



"The inbox rule allowed the attackers to avoid arousing the compromised users' suspicions by deleting non-delivery reports and IT notification emails that might have been sent to the compromised user."



The investigation that followed revealed that over a hundred mailboxes in multiple organizations had been compromised with malicious mailbox rules named "Spam Filter".


Registering on Azure AD
-----------------------


The actors attempted rogue device registration onto the organization's Azure AD instance, hoping to enforce policies that would facilitate lateral phishing.


Azure AD triggers an activity timestamp when a device attempts to authenticate, which was the second chance for defenders to discover potentially suspicious registrations.



![Suspicious registration event](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Suspicious registration event**  
*Source: Microsoft*
If the registration goes unnoticed, the actors are allowed to send messages from a recognized and trusted part of the domain using the stolen valid credentials on Outlook.


The second wave of phishing messages was much more voluminous than the first, counting over 8,500 SharePoint-themed emails with a "Payment.pdf" attachment.


This phishing campaign was crafty and moderately successful, but it wouldn't be nearly as effective if the targeted companies followed one of these practices:


* All employees had enabled MFA on their Office 365 accounts.
* Deploy endpoint protection solutions that can detect the creation of inbox rules.
* Azure AD device registration is closely monitored.
* Azure AD enrollment requires MFA.
* Zero trust policies are employed in all parts of the organization's network.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Indonesia]] [[victim.continent.name=Asia]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.city.name=Singapore]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.country.name=Thailand]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Microsoft]] [[Phishing]] [[Emails]] [[Inbox]] [[Bleeping Computer]]

