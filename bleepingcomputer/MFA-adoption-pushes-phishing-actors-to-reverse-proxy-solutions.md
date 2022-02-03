# MFA adoption pushes phishing actors to reverse-proxy solutions
### The rising adoption of multi-factor authentication (MFA) for online accounts pushes phishing actors to use more sophisticated solutions to continue their malicious operations, most notably reverse-proxy tools.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/mfa-adoption-pushes-phishing-actors-to-reverse-proxy-solutions/
+ Date: 2022-02-03T09:42:15-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/15/phishing-good-bad.jpg)

![Phishing](https://www.bleepstatic.com/content/hl-images/2021/12/15/phishing-good-bad.jpg)


The rising adoption of multi-factor authentication (MFA) for online accounts pushes phishing actors to use more sophisticated solutions to continue their malicious operations, most notably reverse-proxy tools.


The COVID-19 pandemic has changed the way people work forever, proving that it's possible and sometimes even preferable to work from home.


This has increased security risks for companies, many of which can be mitigated by using MFA to protect their employees' accounts.


Even Google, a key internet services provider, has recently decided to enforce two-factor authentication (2FA) on all Google accounts through [a staged auto-enrollment process](https://www.bleepingcomputer.com/news/google/google-to-auto-enroll-150-million-user-accounts-into-2fa/).


With MFA, a user must provide a second authentication factor apart from their account's password to access it. This factor can be a one-time code sent via SMS or email, a token, or a unique cryptographic key.


This additional step creates a practical problem for phishing actors, as stealing the account credentials is no longer enough for them to assume control of them.


Natural evolution
-----------------


The increasing use of MFA has pushed phishing actors to use transparent reverse proxy solutions, and to cover this rising demand, reverse proxy phish kits are being made available.


A reverse proxy is a server that sits between the Internet user and web servers behind a firewall. The reverse proxy then forwards visitors' requests to the appropriate servers and sends back the resulting response. This allows a webserver to serve requests without making itself directly available on the Internet.


As detailed in a report published today by [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/mfa-psa-oh-my), new phishing kits have emerged that offer templates to create convincing login web pages that mimic popular sites.


These newer kits are more advanced because they now integrate an MFA snatching system, which enables threat actors to steal login credentials and MFA codes that would normally protect the account.


As depicted below, when a victim logs into the phishing page, the kit sends the MFA to the genuine online service, intercepts the session cookie, and optionally forwards it to the victim.



![How reverse proxy attacks work](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/proxy.png)**How reverse proxy phishing attacks work**  
*Source: Proofpoint*
This allows the victim to log in to the actual site and raise no suspicions. Meanwhile, the threat actors have stolen both the credentials and the cookie needed to access the account.


Proofpoint has seen three kinds of phishing kits that employ reverse proxying systems, one using Modlishka, another using Muraena/Necrobrowser, and one relying on Evilginx2.


**Modlishka** is the least sophisticated of the bunch, created as a demonstration in 2018, but it’s still capable of harvesting a victim’s session even when push notification systems are employed.


**Necrobrowser**was released in 2019, offering additional capabilities such as auto-login, password changing, disabling Google Workspace notifications, dumping emails, changing SSH session keys, downloading repositories from GitHub, etc.


**Evilginx2** relies on a proprietary system of configurable “phishlets” which enable threat actors to target any site they want. The kit features several pre-installed “phishlets” too, so one can get started right away.



![Some of the phislets offered by Evilginx2 out of the box](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/evilgnx.png)**Some of the phislets offered by Evilginx2 out of the box**  
*Source: Proofpoint*
A blind spot in security
------------------------


Although the existence and implications of these tools have been well documented, the problem remains largely unaddressed, and as more phishing actors turn to using them, making MFA less secure.


One way to tackle the problem is to identify the man-in-the-middle pages used in these attacks. However, as the findings of [a recent study](https://catching-transparent-phish.github.io/catching_transparent_phish.pdf) have shown, only about half of those are blocklisted at any given time.


The constant refresh of domains and IP addresses used for reverse proxy attacks reduces the effectiveness of blocklists, as most of these last between 24 and 72 hours.


As such, the only method that may fight the problem is to add client-side TLS fingerprinting, which could help identify and filter MITM requests.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Epic]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Phishing]] [[Mfa]] [[Proofpoint]] [[Google]] [[Evilginx2]] [[Bleeping Computer]]

