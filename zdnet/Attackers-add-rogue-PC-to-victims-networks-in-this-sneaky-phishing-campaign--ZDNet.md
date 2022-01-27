# Attackers add rogue PC to victims' networks in this sneaky phishing campaign | ZDNet
### Attackers enroll Outlook on BYO devices with Azure AD and then spread SharePoint PDF lures.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/attackers-add-rogue-pc-to-victims-networks-in-this-sneaky-phishing-campaign/
+ Date: 2022-01-27 11:00:09
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/9436b7351af27e9f7e4b7092ebbcc008a01ac197/2022/01/27/cf77a5be-4a64-40b3-8f34-20346c4787ff/shutterstock-1613076505.jpg?width=770&height=578&fit=crop&auto=webp)

Microsoft has raised an alarm about a new multi-phase phishing campaign that first enrolls an attacker's BYOD device on a corporate network and then begins sending thousands of convincing phishing emails to further targets. 

The purpose of enrolling or registering a device on a target company's network was to avoid detection during later phishing attacks, according to Microsoft.   


Microsoft says "most" organizations that had enabled multi-factor authentication (MFA) for Office 365 were not impacted by phishing emails spread by attacker-controlled registered devices, but those that had not enabled MFA were all affected. 

**SEE:** [**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/#link=%7B%22role%22:%22standard%22,%22href%22:%22http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22%3Cstrong%3EA%20winning%20strategy%20for%20cybersecurity%3C/strong%3E%22%7D) **(ZDNet special report)**

The attack exploited instances where MFA was not enforced during the process of registering a new device with a company's instance of Microsoft's identity service, Azure Active Directory ([Azure AD](https://docs.microsoft.com/azure/active-directory/devices/manage-stale-devices)); or when enrolling a BYOD device to a mobile device management (MDM) platform like Microosft's Intune.

"While multiple users within various organizations were compromised in the first wave, the attack did not progress past this stage for the majority of targets as they had MFA enabled. The attack's propagation heavily relied on a lack of MFA protocols," [Microsoft said](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa/). 

"Enabling MFA for Office 365 applications or while registering new devices could have disrupted the second stage of the attack chain," it added. 






The first wave of the attack targeted organizations in Australia, Singapore, Indonesia, and Thailand, according to Microsoft. "Hundreds" of credentials stolen in this phase were then used in the second phase where a device was registered or enrolled, allowing for broader penetration of the target. 

The first phase relied on a DocuSign-branded phishing email requesting the recipient review and sign the document. It used phishing domains registered under the .xyz top level domain (TLD). Each email's phishing link was also uniquely generated and contained the target's name in the URL. The phishing link directed victims to a spoofed Office 365 login page. 

The attackers used stolen credentials to set up a connection with Exchange Online PowerShell and used this to create inbox rules that deleted messages based on keywords in the subject or body of the email, including 'junk', 'spam', 'phishing', 'hacked', 'password', and 'with you'. This was likely to to avoid detection.  

In the second phase, the attackers installed Microsoft's Outlook email client on to their own Windows 10 PC, which was then successfully connected to the victim's Azure AD. All the attackers had to do was accept Outlook's onboarding experience that prompts the user to register a device. In this case, the attackers were using credentials acquired in phase one. 

"An Azure AD MFA policy would have halted the attack chain at this stage," Microsoft notes. 

Azure AD does have tools to mitigate these threats by time-stamping and logging new device registrations. 

But with compromised credentials and a registered Windows 10 device with Outlook, the attackers could then launch the second phase, which involved sending "lateral, internal, and outbound" phishing messages to over 8,500 other email accounts. These messages used a SharePoint invitation to view a "Payment.pdf" file.  

"By using a device now recognized as part of the domain coupled with a mail client configured exactly like any regular user, the attacker gained the ability to send intra-organizational emails that were missing many of the typical suspect identifiers. By removing enough of these suspicious message elements, the attacker thereby significantly expanded the success of the phishing campaign."      


Accounts where victims clicked the link in the second wave were similarly subjected to automated rules that deleted emails containing the same keywords used in the first wave.

**SEE:** [**This mysterious malware could threaten millions of routers and IoT devices**](https://www.zdnet.com/article/this-mysterious-malware-could-threaten-millions-of-routers-and-iot-devices/#link=%7B%22linkText%22:%22This%20mysterious%20malware%20could%20threaten%20millions%20of%20routers%20and%20IoT%20devices%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/this-mysterious-malware-could-threaten-millions-of-routers-and-iot-devices/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

Microsoft offers directions to security teams that can revoke active sessions and tokens of compromised accounts, delete unwanted mailbox rules, and disable rogue devices registered with Azure AD.

Notably, Microsoft says organizations can reduce their attack surface by disabling "[basic authentication](https://docs.microsoft.com/en-gb/exchange/clients-and-mobile-in-exchange-online/disable-basic-authentication-in-exchange-online)", and in Exchange Online and by disabling Exchange Online Powershell for end users. Admins can also enable [Microsoft's new](https://www.zdnet.com/article/microsofts-new-security-feature-locks-hackers-out-with-gps/) "[conditional access control](https://docs.microsoft.com/en-gb/azure/active-directory/conditional-access/concept-conditional-access-cloud-apps#user-actions)". 

Microsoft in February [announced that](https://techcommunity.microsoft.com/t5/exchange-team-blog/basic-authentication-and-exchange-online-february-2021-update/ba-p/2111904), due to the pandemic, it was delaying its plan to turn off basic authentication in Exchange Online for legacy email authentication protocols, such as Exchange Web Services (EWS), Exchange ActiveSync (EAS), POP, IMAP, Remote PowerShell, MAPI, RPC, SMTP AUTH, and OAB. 

That move would eliminate instances where single factor authentication is used. Microsoft's replacement for basic authentication, dubbed Modern Authentication, enables both conditional access and MFA.    

Microsoft in September [said](https://techcommunity.microsoft.com/t5/exchange-team-blog/basic-authentication-and-exchange-online-september-2021-update/ba-p/2772210) it would "begin to permanently disable Basic Auth in all tenants, regardless of usage, with the exception of SMTP Auth", from October 1, 2022. 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Indonesia]] [[victim.continent.name=Asia]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.city.name=Singapore]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.country.name=Thailand]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Microsoft]] [[Phishing]] [[Mfa]] [[Emails]] [[ZDNet]]

