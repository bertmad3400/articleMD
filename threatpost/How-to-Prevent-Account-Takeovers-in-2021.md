# How to Prevent Account Takeovers in 2021
### Dave Stewart, Approov CEO, lays out six best practices for orgs to avoid costly account takeovers.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175090)
+ Date: September 28, 2021  5:36 pm
+ Author: David Stewart


## Article:
Data breaches and hacking put internet users at risk of account takeover, if cybercriminals successfully gain access to valid login credentials. There are [reckoned to be](https://solutionsreview.com/identity-management/intuit-informs-turbotax-customers-of-account-takeovers/) in excess of  8.4 million discrete passwords currently circulating online, more than 3.5 billion of which are tied to active email addresses.


Every data breach that exposes usernames and passwords creates more assets to be sold on the Dark Web, and used in scripts to fuel credential-stuffing activities.


Fortunately, there are steps organizations can take to prevent cybercriminal success, which we’ll get to in a bit.


Epidemic: Credential Stuffing
-----------------------------


Credential stuffing is a [cyberattack mechanism](https://threatpost.com/spotify-credential-stuffing-cyberattack/163672/) that relies on brute force, but eliminates the need for hackers to spend time and resources trying to guess individual passwords. Instead, they can turn to lists of valid credentials that have been uncovered through previous data breaches in other platforms.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Unfortunately, many people still tend to reuse their passwords and security-verification questions across a range of websites. So using credentials exposed by a data breach, cybercriminals can enjoy a higher success rate and reduced effort in their attempts to gain access to existing accounts.


To assist them, an entire underground economy has emerged, selling specialist tools and stolen personal data to fuel automated credential-stuffing campaigns. Automated bots and scripts are popular with perpetrators of online fraud, as the automation enables them to maximize their investment returns and achieve wider coverage in their account takeover attempts. Sophisticated bots are capable of bypassing many fraud prevention solutions.


Some perpetrators hire cheap human labor, for staging larger scale account takeover attacks. These human operatives can more easily work around fraud protection measures, such as Captchas, designed to identify bots. They can provide the required level of human interaction needed to deal with these challenge-response mechanisms.


Likewise, hacker intervention can occasionally circumvent standard authentication measures for blocking account takeover fraud. For instance, multi-factor authentication (MFA) routines that require users to respond to a one-time password (OTP) or SMS text code can [be intercepted or delayed, using the right tools](https://securityintelligence.com/posts/massive-fraud-operation-evil-mobile-emulator-farms/).


These issues are having a significant impact. The security and content delivery organization [Akamai detected](https://www.akamai.com/uk/en/resources/our-thinking/state-of-the-internet-report/global-state-of-the-internet-security-ddos-attack-reports.jsp#:~:text=2021%20State%20of%20the%20Internet%20/%20Security%20Research,to%20exploit%20any%20vulnerability%20the) 193 billion credential stuffing attacks worldwide in 2020. A single day saw over a billion assaults, in a year in which the financial services industry suffered 3.45 billion credential-stuffing attacks.


Financial services are a prime target. Successful perpetrators can go on to siphon funds from existing user accounts, commit credit card fraud, extort enterprises and other nefarious activities. But the damage isn’t limited to the finance sector.


In its [State of Secure Identity report](https://auth0.com/resources/upcoming-webinars/state-of-security-identity-report-session-one#:~:text=The%202021%20Auth0%20State%20of%20Secure%20Identity%20report,and%20the%20adoption%20rates%20for%20identity%20protection%20technologies.) for 2021, Auth0 revealed that credential-stuffing accounted for 16.5 percent of login attempts on its platform during the first three months of the year. Their report notes that the top two industries most affected by credential stuffing attacks are retail, and the combined sector of travel and leisure. Application programming interfaces (APIs) are major targets for credential-stuffing attacks since they provide a convenient channel for automated traffic.


It’s worth noting that, during the first 90 days of 2021, breached passwords were detected at an average of more than 26,600 per day. Their extreme vulnerability is making passwords largely redundant as an effective security measure.


6 Measures to Deal with Account Takeover
----------------------------------------


There’s no single “magic bullet” to remedy the issues of credential stuffing and account takeover. Rather, the solution must come from a judicious [mix of techniques](https://www.csoonline.com/article/3448558/credential-stuffing-explained-how-to-prevent-detect-and-defend-against-it.html) and cybersecurity best practices. Here’s a rundown of what to consider:


Attackers often configure their credential stuffing tools to imitate the behavior of legitimate users, and employ proxies to distribute their access requests across different IP addresses. One possible sign of an assault is a marked increase in login failure rates over a short time period.


This should be mandatory for all high-risk use cases, such as user accounts that have recorded a suspiciously high number of failed login attempts. It should be noted, as discussed above, 2FA can be bypassed, so it can’t be relied upon on its own.


Organizations should continuously monitor the internet for public disclosures of data breaches and exposed email addresses. All compromised accounts should be earmarked for mandatory password reset and 2FA moving forward.


Account holders should be encouraged to use reputable password-management software. These platforms typically provide tools for generating truly strong passwords and negate the need to reuse passwords. They also eliminate the need for users to have to remember them – a standard objection to strong password implementation.


It is vital to authenticate the app as well as the user, in order to control access to your back end services and prevent brute force attacks from bots or scripts. Alongside 2FA, this can provide a very effective barrier to scripted attacks.


The [zero-trust framework](https://www.crowdstrike.com/cybersecurity-101/zero-trust-security/) requires all account holders or users of a platform to undergo authentication, authorization, and continuous validation before gaining access to applications and data. If user credentials don’t work inside scripts, hackers will soon get bored of stealing them. This is the real solution to prevent data breaches – reduce the value of the data to zero.


Credential-stuffing attacks, utilizing user names/passwords extracted from unconnected data breaches, are one of the most common account takeover mechanisms. The simplest way to prevent such exploits is to understand that user names/passwords on their own are not enough to gain access to back-end systems.


Adding a requirement for appropriate and independently verified additional factors (eg 2FA, biometrics, app authentication) to gain access to your servers will make your business dramatically less likely to suffer account takeover attacks.


***David Stewart is CEO at Approov.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[credential-stuffing]] [[attacks.]] [[addresses.]] [[ThreatPost]]
