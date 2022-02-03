# Low-Detection Phishing Kits Increasingly Bypass MFA
### A growing class of phishing kits – transparent reverse proxy kits – are being used to get past multi-factor authentication using MiTM tactics.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178208
+ Date: 2022-02-03T22:10:32+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2019/09/26105755/fish-1.jpg)

More and more phishing kits are focusing on bypassing multi-factor authentication (MFA) methods, researchers have warned – typically by stealing authentication tokens via a man-in-the-middle (MiTM) attack.


As MFA continues to see widespread consumer and business adoption – a full 78 percent of respondents in a [recent poll](https://duo.com/blog/the-2021-state-of-the-auth-report-2fa-climbs-password-managers-biometrics-trend) said they used it in 2021 – cybercriminals have devoted resources into keeping up. According to an analysis from Proofpoint, MFA-bypass phishing kits are proliferating rapidly, “ranging from simple open-source kits with human readable code and no-frills functionality to sophisticated kits utilizing numerous layers of obfuscation and built-in modules that allow for stealing usernames, passwords, MFA tokens, Social Security numbers and credit-card numbers.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Researchers also noted that MFA-bypass kits represent a security blind spot, with the associated IP addresses and domains often skating by VirusTotal detection.


**Transparent Reverse Proxy Trickery**
--------------------------------------


According to Proofpoint, one of the phishing-kit approaches that’s particularly gaining steam is the use of transparent reverse proxies (TRPs), which enable attackers to insert themselves into existing browser sessions. This MiTM approach lets adversaries hide out and harvest information as it’s entered or appears on the screen.


This is a big departure from traditional phishing, which involves attackers creating copycat sites that mimic, say, an actual Windows log-in page in order to trick targets into entering their credentials. That traditional approach leaves plenty of room for red flags to be introduced, such as outdated logos, poor syntax, spelling errors and the like.


TRP kits show “the actual website to the victim,” researchers noted in a [Thursday analysis](https://www.proofpoint.com/us/blog/threat-insight/mfa-psa-oh-my). “Modern web pages are dynamic and change frequently. Therefore, presenting the actual site instead of a facsimile greatly enhances the illusion an individual is logging in safely.”


Meanwhile, attackers will hang out and steal session cookies, which can then be used by the threat actor to gain access to the targeted account without the need for a username, password or MFA token.


Proofpoint said that there are three TRP kits in particular that have seen upticks in use lately.


### **Modlishka**


Developed by a Polish security researcher, Modliska [has been on the scene](https://threatpost.com/2fa-broken-authentication/140776/) since late 2018. Proofpoint researchers said that it’s a simple affair, allowing users to phish just one site at a time. It uses a command line interface and has a GUI-based mechanism for stealing credentials and session information, they added.


“Modlishka also integrates Let’s Encrypt so it can make the fake domain landing page just a bit more believable by encrypting the traffic and providing the little padlock in the web bar,” they said. “[It’s also] capable of harvesting a victim’s session even when tech like Duo’s push notification authenticator is used.”


### **Muraena/Necrobrowser**


Muraena/Necrobrowser, first released in 2019, is a kit that comes in two parts, according to Proofpoint.


The first part is Muraena, which “runs server-side and uses a crawler to scan the target site to ensure it can properly rewrite all the traffic needed, to not alert the victim,” researchers explained. It harvests the victim’s credentials and session cookie, then deploys Necrobrowser.


“Necrobrowser is a headless browser, which is a browser without a GUI used for automation, that leverages the stolen session cookies to log into the target site and do things such as change passwords, disable Google Workspace notifications, dump emails, change SSH session keys in GitHub and download all code repositories,” according to Proofpoint.


### **Evilginx2**


Evilginx2 is a Golang kit, also originally created by a security researcher as a pen-testing tool.


Its hallmarks are an easy setup and the ability to use its pre-installed “phishlets,” which are yaml configuration files the engine uses to configure the proxy to the target site. Users can also create new phishlets.


“Utilizing these phishlets, you can configure the server to phish multiple brands at once,” according to Proofpoint. “Evilginx2 allows you to configure a custom subdomain and landing page URL for each as well.”


Once a victim clicks on the malicious link, they are taken to a secure page to log in, where the attackers lift the credentials, MFA codes and session cookies.


“The victim is either redirected to a different page or allowed to continue through to the page,” according to Proofpoint. “The threat actor is then able to use the stolen session cookie to log in as the victim where they can take multiple actions like changing the password, copying data or pretending to be the victim.”


While these tools aren’t new, they’re being increasingly used to bypass MFA, the firm noted, which is worrying given their lack of detection. Researchers from Stony Brook University and Palo Alto Networks developed a tool that managed to identify 1,200 MitM phishing sites. Yet, just 43.7 percent of those domains and 18.9 percent of their IP addresses showed up in VirusTotal – despite having lifespans of up to 20 or more days.


“As more companies follow Google’s lead and start requiring MFA, threat actors will rapidly move to solutions like these MitM kits,” according to researchers. “They are easy to deploy, free to use and have proven effective at evading detection. The industry needs to prepare to deal with blind spots like these before they can evolve in new, unexpected directions.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Education]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Proofpoint]] [[Mfa]] [[Phishing]] [[ThreatPost]]

