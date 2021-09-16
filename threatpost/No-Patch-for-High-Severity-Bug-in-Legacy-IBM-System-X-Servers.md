# No Patch for High-Severity Bug in Legacy IBM System X Servers
### Two of IBM’s aging flagship server models, retired in 2020, won’t be patched for a command-injection flaw. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169491)
+ Date: September 15, 2021  3:01 pm
+ Author: Tom Spring


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/15150050/Servers-IBM.jpg)
Two legacy IBM System x server models, retired in 2019, are open to attack and will not receive security patches, according to hardware maker Lenovo. However, the company is offering workaround mitigation.


The two models, IBM System x 3550 M3 and IBM System x 3650 M3, are both vulnerable to command injection attacks. The bug allows an adversary to execute arbitrary commands on either server model’s operating system via a vulnerable application called Integrated Management Module (IMM).


IMM is used for systems-management functions. On the back panel of System x models, serial and Ethernet connectors use the IMM for device management. The flaw, [according to a Lenovo advisory posted Tuesday](https://support.lenovo.com/us/en/product_security/LEN-66347), is in the IMM firmware code and “could allow the execution of operating system commands over an authenticated SSH or Telnet session.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


SSH or Secure Shell is a cryptographic network communication protocol allowing two computers to communicate or share data. Telnet is another network protocol that allows remote users to log into another computer on the same network. Telnet, by default, does not encrypt data sent over its connection.


The bug, tracked as CVE-2021-3723, was disclosed on Wednesday and [bug hunter Denver Abrey](https://twitter.com/denver_a) is credited for finding it.


Eight vulnerabilities in a later version of IMM – called IMM2 – were [identified in June 2020](https://www.ibm.com/support/pages/node/6220270), three high-severity. These bugs were tied to flaws in client-side code responsible for implementing the SSH2 protocol, called libssh2.


Both the System x 3550 M3 and System x 3650 M3 were introduced [April 5, 2011](https://www.ibm.com/common/ssi/rep_ca/7/897/ENUS111-067/ENUS111-067.PDF) (PDF) as midsized businesses solutions. On June 30, 2015, Lenovo announced systems were both discontinued, but would receive security updates for five additional years.


According to the Lenovo security bulletin, software and security support for System x 3550 and 3650 [ended December 31, 2019](https://www.ibm.com/common/ssi/ShowDoc.wss?docURL=/common/ssi/rep_ca/8/760/ENUSJS19-0018/index.html&lang=en&request_locale=en).


“Lenovo has historically provided service and support for at least five years following a product’s withdrawal from marketing. This is subject to change at Lenovo’s sole discretion without notice. Lenovo will announce a product’s EOS date at least 90 days before the actual EOS date and in most cases longer,” wrote Lenovo.


On Wednesday Lenovo said it “recommends discontinuation of use” of both servers, but offered a “mitigation strategy”.


“If it is not feasible to discontinue use of these systems,” Lenovo recommended:


Lenovo did not indicate if it was aware of any active campaigns targeting the vulnerability.


**It’s time to evolve threat hunting into a pursuit of adversaries.** [**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **Threatpost and Cybersixgill for** [**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **and get a guided tour of the dark web and learn how to track threat actors before their next attack.** [**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **for the LIVE discussion on September 22 at 2 PM EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[Lenovo]] [[IMM]] [[models,]] [[M3]] [[ThreatPost]]
