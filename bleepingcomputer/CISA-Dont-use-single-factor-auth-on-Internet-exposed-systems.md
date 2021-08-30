# CISA: Don’t use single-factor auth on Internet-exposed systems
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/cisa-don-t-use-single-factor-auth-on-internet-exposed-systems/)
+ Date: August 30, 2021
+ Author: Sergiu Gatlan


## Article:
![CISA: Don’t use single-factor authentication on Internet-exposed systems](https://www.bleepstatic.com/content/hl-images/2021/07/01/CISA.jpg)


Single-factor authentication (SFA) has been added today by the US Cybersecurity and Infrastructure Security Agency (CISA) to a very short list of cybersecurity bad practices it advises against.


CISA's [Bad Practices catalog](https://www.cisa.gov/BadPractices) includes practices the federal agency has deemed "exceptionally risky" and not to be used by organizations in the government and the private sector as it exposes them to an unnecessary risk of having their systems compromised by threat actors.


They are exceptionally dangerous for orgs that support Critical Infrastructure or National Critical Functions (NCFs) responsible for national security and economic stability, as well as the public's safety.


Furthermore, these dangerous practices are "especially egregious" on Internet-exposed systems that threat actors could target and compromise remotely.


Orgs advised to switch to multi-factor authentication
-----------------------------------------------------


As the federal cybersecurity agency said, SFA (a low-security authentication method that only requires users to provide a username and a password) is "exceptionally risky" when used for remote authentication or logging into an account with administrative permissions.


"The use of single-factor authentication for remote or administrative access to systems supporting the operation of Critical Infrastructure and National Critical Functions (NCF) is dangerous and significantly elevates risk to national security, national economic security, and national public health and safety," CISA says.


Attackers can quickly gain access to systems protected using this low-security method given that passwords can be easily stolen or guessed via various techniques (e.g., phishing, keylogging, network sniffing, social engineering, malware, brute-force attacks, credential dumping).


To top it all off, admins sharing the same password and password reuse also increases the risk of attackers compromising SFA-protected systems.


Switching to [multi-factor authentication (MFA)](https://www.bleepingcomputer.com/tag/mfa/) makes it a lot harder or even impossible for threat actors to pull off a successful attack.


A [joint study](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html?/en-US/index.html) by Google, New York University, and University of California San Diego found that using MFA can block up to 100% of automated bots, 99% of bulk phishing attacks, and roughly 66% of targeted attacks.


Microsoft Director of Identity Security Alex Weinert also [said](https://techcommunity.microsoft.com/t5/Azure-Active-Directory-Identity/Your-Pa-word-doesn-t-matter/ba-p/731984/?/en-US/index.html) that "your password doesn’t matter, but MFA does! Based on our studies, your account is more than 99.9% less likely to be compromised if you use MFA."


The only two other entries on the Bad Practices list are the use of end-of-life (or out-of-support) software and default (or known) credentials.


Admins and IT pros asked to help
--------------------------------


CISA has also opened a [GitHub Bad Practices discussions page](https://github.com/cisagov/bad-practices/discussions) to allow IT professionals and admins to provide feedback and share their expertise on defending against them.


Additional cybersecurity bad practices the agency is potentially considering to add to the list include:


* using weak cryptographic functions or key sizes
* flat network topologies
* mingling of IT and OT networks
* everyone's an administrator (lack of least privilege)
* utilization of previously compromised systems without sanitization
* transmission of sensitive, unencrypted/unauthenticated traffic over uncontrolled networks
* poor physical controls


"Although these Bad Practices should be avoided by all organizations, they are especially dangerous in organizations that support Critical Infrastructure or National Critical Functions," CISA [added](https://us-cert.cisa.gov/ncas/current-activity/2021/08/30/cisa-adds-single-factor-authentication-list-bad-practices).


"CISA encourages all organizations to review the [Bad Practices webpage](https://www.cisa.gov/BadPractices) and to engage in the necessary actions and critical conversations to address Bad Practices."




#### Tags:
[[CISA]] [[cybersecurity]] [[Bleeping Computer]]
