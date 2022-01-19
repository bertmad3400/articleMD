# Box 2FA Bypass Opens User Accounts to Attack
### A security bug in the file-sharing cloud app could have allowed attackers using stolen credentials to skate by one-time SMS code verification requirements.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177760
+ Date: 2022-01-19T18:30:44+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2019/01/11104331/2FA_two-factor-authentication.jpg)

A security hole in Box, the cloud-based file-sharing service, paved the way for busting its multifactor authentication (MFA), researchers said – and it’s the second such MFA bypass they have discovered in the service so far.


Clearly, the stakes are high – gaining access to a Box account could give cyberattackers access to a vast array of sensitive documents and data for both individuals and organizations. The company claims 97,000 companies and 68 percent of the Fortune 500 as customers.


Varonis Threat Labs researchers said the bypass worked on accounts that used one-time SMS codes for two-factor authentication (2FA) verification. In a proof-of-concept exploit, they were able to achieve the bypass by stealing a session cookie.


[![Password Management Webinar](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/12124026/specops_300x250_watch.jpg)](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)


“With increased pressure to adopt and enforce multi-factor authentication, many [software-as-a-service] providers now offer multiple MFA options to provide users a second line of defense against credential stuffing and other password attacks. “Like many applications, Box allows users without Single Sign-On (SSO) to, or SMS with a one-time passcode as a second step in authentication.”


When a user goes to log on with his or her credentials, Box generates the cookies and the user is asked to navigate to an SMS verification page, where the person is instructed to enter a one-time passcode sent to an enrolled mobile phone.


However, if the user doesn’t navigate to the verification page, no SMS code is generated, but a session cookie still is. It’s at this point that the bug came into play. A malicious threat actor trying to log in with stolen credentials could have skipped going to the SMS verification page, and could instead initiate the other MFA option provided by Box: Using an authenticator app, like Okta Verify or Google Authenticator.


If attackers were to do this, they could break into the target account by using a factor ID and code from their own Box account, the session cookie received by providing the victim’s credentials and their own authenticator app – no physical access to the victim’s phone is necessary.


“Box did not verify whether the victim was enrolled in [time-based one-time password] TOTP verification and did not validate that the authenticator app used belonged to the user that was logging in,” researchers explained in a [Tuesday analysis](https://www.varonis.com/blog/box-mfa-bypass-sms). “This made it possible to access the victim’s Box account without the victim’s phone and without notifying the user via SMS.”


The attack flow is as follows, according to Varonis:


* Attacker enrolls in MFA using an authenticator app and stores the device’s factor ID.
* Attacker enters a user’s email address and password on account.box.com/login.
* If the password is correct, the attacker’s browser is sent a new authentication cookie and redirects to: /2fa/verification.
* The attacker, however, does not follow the redirect to the SMS verification form. Instead, they pass their own factor ID and code from the authenticator app to TOTP verification endpoint: /mfa/verification.
* The attacker is now logged in to the victim’s account and the victim does not receive an SMS message.



Box has fixed the issue, but “we want to underscore that MFA implementations are prone to bugs, just like any other code,” researchers noted. “Our team has demonstrated not one, but two application flaws that allowed us to access a victim’s MFA-enabled Box account with only username and password. Spoiler alert: Box is [not the only major SaaS provider](https://threatpost.com/flaws-in-microsoft-365s-mfa-access-cloud-apps/159240/) that we’ve been able to bypass.”


The first bypass the researchers discovered worked on authenticator-based MFA.


“There are several issues that led to this vulnerability,” Zane Bond, director of product management at Keeper Security, said via email. “However, at the end of the day, this one sits in a similar bucket to many OAuth and SAML vulnerabilities that are found. The underlying technology is usually sound. These issues tend to stem from individual implementations, or errors in the implementation logic. Ultimately, every vendor is responsible for the correct implementation of a particular security control, and it’s not easy.”


**How to Protect Against MFA Bypasses**
---------------------------------------


MFA can provide a false sense of security, researchers noted – and organizations should ensure that bypasses are as rare as possible by implementing common-sense protections.


One of those is mobile phishing awareness training, according to Hank Schless, senior manager of security solutions at Lookout.


“Multifactor authentication is an effective way for an end user to validate their identity. However, it cannot differentiate between whether a user really is who they say they are,” he said via email. “The issue that Varonis highlights is that compromised user credentials could make additional authentication tools far less effective.”


Meanwhile, in order to mitigate the risk of unauthorized access to apps, data and infrastructure, even with legitimate credentials, organizations could also implement cloud access security broker (CASB) and zero trust network access (ZTNA) solutions, which detect anomalous user behavior and verify identity.


“In addition to securing the endpoint, organizations also need to be able to dynamically secure access and actions within both cloud and private apps,” Schless said. “This is where ZTNA and CASB solutions shine. By understanding the interactions between users, devices, networks and data, organizations can understand key indicators of a compromise that point to ransomware or massive data exfiltration taking place. Together, securing employee mobile endpoints as well as your cloud and private apps will help organizations create a solid security posture based in a zero-trust philosophy.”


Varonis researchers noted that CISOs should ask the following:


* Would I know if MFA was disabled or bypassed for a user across all my SaaS applications?
* How much data can an attacker access if they compromise a normal user account?
* Is any data unnecessarily exposed to too many users (or exposed publicly)
* If a user accesses data abnormally, will I get an alert?


“We recommend you start by securing data where it lives,” according to Varonis. “When you limit access and monitor the data itself, your likelihood of data exfiltration due to a perimeter bypass drops significantly.”





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Mfa]] [[Sms]] [[Varonis]] [[One-time]] [[Cloud]] [[ThreatPost]]

