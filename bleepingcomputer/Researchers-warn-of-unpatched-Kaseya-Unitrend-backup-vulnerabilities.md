# Researchers warn of unpatched Kaseya Unitrend backup vulnerabilities
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/researchers-warn-of-unpatched-kaseya-unitrend-backup-vulnerabilities/)
+ Date: July 26, 2021
+ Author: Lawrence Abrams


## Article:
![Kaseya](https://www.bleepstatic.com/content/hl-images/2021/07/05/Kaseya__headpic.jpg)


Security researchers warn of three new zero-day vulnerabilities in the Kaseya Unitrend service and advise users not to expose the service to the Internet.


Kaseya Unitrends is a cloud-based enterprise backup and disaster recovery solution that is offered as a stand-alone solution or as an add-on for the Kaseya VSA remote management platform.


Last week, the [Dutch Institute for Vulnerability Disclosure](https://csirt.divd.nl/) (DIVD) issued a TLP:AMBER advisory about three unpatched vulnerabilities in the [Kaseya Unitrends](https://www.unitrends.com/products/enterprise-backup-software) backup product.


While DIVD released this advisory under the TLP:AMBER designation, DIVD Chairman [Victor Gevers](https://twitter.com/0xDUDE) told BleepingComputer that it was originally shared with 68 government CERTs under a coordinated disclosure.


However, one of the recipients uploaded it to an online analyzing platform, where it became public to those with access to the service.


"Two days later, an Information Sharing and Analysis Center alerted us that one of the GovCERTs had forwarded the email to an organization's service desk operating in the Financial Services in that country," Gevers told BleepingComputer.


"An employee uploaded the TLP: AMBER labeled directly to an online analyzing platform and shared its content to all participants of that platform; because we do not have an account on that platform, we immediately requested removing this file."


The Kaseya Unitrend vulnerabilities
-----------------------------------


Yesterday, DIVD released a public advisory warning that zero-day vulnerabilities have been discovered in Kaseya Unitrends versions earlier than 10.5.2 and to not expose the service to the Internet.


"Do not expose this service or the clients (running default on ports 80, 443, 1743, 1745) directly to the internet until Kaseya has patched these vulnerabilities," reads DIVD's [advisory](https://csirt.divd.nl/cases/DIVD-2021-00014/).


The vulnerabilities affecting the Kaseya Unitrends backup service include a mixture of authenticated remote code execution, authenticated privilege escalation, and unauthenticated remote code execution on the client side.


Unlike the [Kaseya VSA zero-days](https://www.bleepingcomputer.com/news/security/kaseya-was-fixing-zero-day-just-as-revil-ransomware-sprung-their-attack/) used as part of the [July 2nd REvil ransomware attack](https://www.bleepingcomputer.com/news/security/revil-ransomware-hits-1-000-plus-companies-in-msp-supply-chain-attack/), these vulnerabilities are more difficult to exploit.


This is because a threat actor would need a valid user to perform remote code execution or privilege escalation on the publicly exposed Kaseya Unitrend service. Furthermore, threat actors would already need to have breached a customer network to exploit the unauthenticated client RCE.


DIVD discovered the vulnerabilities on July 2nd, 2021, and disclosed them to Kaseya on July 3rd. On July 14th, DIVD began scanning the Internet for exposed Kaseya Unitrend instances to identify vulnerable systems.


DIVD will attempt to inform owners of vulnerable systems to get them offline until a patch is released.


Gevers told BleepingComputer that the amount of vulnerable instances is low, but they have been found in sensitive industries.


BleepingComputer contacted Kaseya to learn when the patch will be released but has not heard back at this time.




#### Tags:
[[Kaseya]] [[DIVD]] [[Unitrend]] [[Unitrends]] [[BleepingComputer]] [[TLP]] [[Gevers]] [[Bleeping Computer]]
