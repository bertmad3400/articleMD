# SSL certificate research highlights pitfalls for company data, competition
### Analysis reveals hidden risks for organizations that do not monitor their certificate usage.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/ssl-certificate-research-highlights-pitfalls-for-company-data/)
+ Date: November 5, 2021
+ Author: Charlie Osborne


## Article:
Unknown

Research into how the enterprise handles and deploys security certificates has revealed risks to data that may be overlooked. 


On Thursday, the Detectify Labs team [published a report](https://blog.detectify.com/2021/11/04/new-research-are-ssl-certificates-leaking-company-secrets/) based on the initial analysis of public SSL/TLS certificates, conducted from June 2021.

The team says that there are "pitfalls" to the deployment of these certificates that "can lead to company data being exposed or compromised by malicious actors." 

SSL/TLS certificates, issued by certificate authorities (CA), are used to authenticate and secure connections made through a browser. Encryption is used to protect communication streams during online sessions.  

When important information is transferred -- including the submission of personal data or when financial transactions are performed -- encryption via certificates is key to preventing theft, eavesdropping, and Man-in-The-Middle (MiTM) attacks.  

"SSL/TLS certificates make the internet a safer place, but many companies are unaware that their certificates can become a looking glass into the organization -- potentially leaking confidential information and creating new entry points for attackers," the cybersecurity researchers said.  

The Detectify analysis included the examination of over 900 million SSL/TLS certificates and associated events generated from issuing organizations including Google, Amazon, Let's Encrypt, and Digicert, made possible through public data points. While the investigation is ongoing, the team has highlighted some of the risks associated with SSL certificates in particular. 






The first problem is that the "overwhelming majority of newly certified domains" have been given descriptive names. According to Detectify researcher Fredrik Nordberg Almroth, this may appear harmless, but if certification is issued at a development stage, this can give competitors time to undermine new companies or products before they reach the market.  

In addition, wildcard certificates, often a less expensive option for businesses, may be susceptible to Application Layer Protocols Allowing Cross-Protocol Attack (ALPACA). Approximately 13% of the data set related to wildcard use.  

The US National Security Agency (NSA) warned of [ALPACA](https://media.defense.gov/2021/Oct/07/2002869955/-1/-1/0/CSI_AVOID%20DANGERS%20OF%20WILDCARD%20TLS%20CERTIFICATES%20AND%20THE%20ALPACA%20TECHNIQUE_211007.PDF) in October this year. The attack vector can be used to trick servers with unencrypted protocols to steal cookies, user data, or to perform cross-site scripting (XSS) attacks.  

These are only two potential risks associated with security certificates, but the team says there is more to examine.  

"We have only just begun digging into the data," Almroth commented. "There are several ways an attacker could use public information about SSL/TLS certificates to map out a company's attack surface to understand where the weaknesses are. For example, an attacker could see if a certificate is about to expire or has been signed using a weak signature algorithm. The latter can be exploited to listen in on website traffic or create another certificate with the same signature -- allowing an attacker to pose as the affected service." 

So, what can organizations do in the meantime? Detectify recommends that you do implement SSL/TLS certificates, but it is also necessary to continually monitor them for weaknesses or suspicious behavior.  

Past research has [also found](https://www.zdnet.com/article/most-ssl-certificate-misissuance-caused-by-software-bugs-and-rule-misinterpretations/) that software bugs and the misinterpretation of industry standards are normally the cause for incorrectly-issued SSL certificates. 

In other [certificate news this week](https://www.zdnet.com/article/expired-certificate-downs-windows-11-snipping-tool-s-mode-start-menu-and-settings-page/), Microsoft said that a certificate that expired on October 31 has impacted Windows 11 features including the built-in snipping tool, touch keyboard, and voice typing. A fix is set to be pushed to users affected by the issue.  

###  Previous and related coverage

* [Expired certificate downs Windows 11 snipping tool, S mode start menu and settings page](https://www.zdnet.com/article/expired-certificate-downs-windows-11-snipping-tool-s-mode-start-menu-and-settings-page/)
* [Most SSL certificate misissuance caused by software bugs and rule misinterpretations](https://www.zdnet.com/article/most-ssl-certificate-misissuance-caused-by-software-bugs-and-rule-misinterpretations/)
* [Apple strong-arms entire CA industry into one-year certificate lifespans](https://www.zdnet.com/article/apple-strong-arms-entire-ca-industry-into-one-year-certificate-lifespans/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[SSL/TLS]] [[certificates,]] [[Detectify]] [[SSL]] [[ZDNet]]
