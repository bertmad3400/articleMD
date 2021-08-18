# Kerberos Authentication Spoofing: Don’t Bypass the Spec
### Yaron Kassner, CTO at Silverfort, discusses authentication-bypass bugs in Cisco ASA, F5 Big-IP, IBM QRadar and Palo Alto Networks PAN-OS.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168767)
+ Date: August 18, 2021  9:19 am
+ Author: Yaron Kassner


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/18091740/kerberos-e1629292675908.jpg)
Authentication is the front gate to security systems, so if you bypass it, you can pretty much do whatever you want. You can log in as an admin and change configurations,  access protected resources and gain control of appliances to steal sensitive data from them. For these reasons, the authentication protocols used by security systems must be flawless. But in security, there’s no such thing as a flawless system, and implementation errors can lead to hazardous security vulnerabilities.


And that’s exactly what we discovered when analyzing four different security systems –  Cisco ASA, F5 Big-IP, IBM QRadar and Palo Alto Networks PAN-OS. All were vulnerable to bypass exploits because of the way they implemented the Kerberos and LDAP authentication protocols.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


To understand these vulnerabilities, one must first understand how the Kerberos authentication protocol works. It consists of three exchanges:


The Kerberos protocol is solid. It was developed at MIT and provides Single Sign On (SSO) for many large companies.


**Poor Configuration Can Lead to Attack**
-----------------------------------------


The four security systems we mentioned earlier can be configured to use Kerberos without its SSO capabilities. Instead, the user is prompted for a username and password when logging in, and the system asks for the TGT. In other words, the security system serves as both the client and the server.


One might think – if the client and server are the same, why do I need the client/server exchange? The password is verified during the Authentication Service exchange, so that should be enough. This thought process sounds legit, only they forgot the first rule of fight club: Don’t deviate from the spec.


**KDC Spoofing Attacks**
------------------------


In fact, this is not legit at all. Some would say it’s even illegitimate. Neglecting the Client/Server exchange can result in a [KDC spoofing vulnerability](https://www.securityfocus.com/bid/1616/discuss). Let’s look at it from an attacker’s perspective:


I want to authenticate to the system, but I don’t know the password. So maybe I’ll try to authenticate with a password of my choice – it’s most likely the wrong password, but the idea is to trick the system into thinking it’s the right password.


The system, being the Kerberos client, will reach out to the KDC to request a TGT. If this message is actually processed and answered by the real KDC, the attack will not work, because the KDC will notice that the password is wrong, and simply deny the authentication. But if we hijack the communication between the system and the KDC, then we can do some really evil stuff.


What if I pretend to be the KDC, and instead of returning an error, I return a fake TGT?


Well, in that case, during the TGS exchange, the KDC will reject my TGT. But I can hijack the TGS exchange communication as well and return a fake service ticket. Oh, but then the Client/Server exchange won’t work, because the server will reject my fake service ticket.


Then again, these four security vendors didn’t implement the Client/Server exchange at all. So I can just log in with my fake password to all these systems.


In reality, discovering these vulnerabilities was a bit more complicated than that, because each of the products implemented the Kerberos protocol a little bit differently, and this required changes to the original attack pattern. I encourage you to read more about each vulnerability in these blog posts – [CVE-2019-4545](https://www.silverfort.com/blog/third-kdc-spoofing-ibm-qradar-cve-2019-4545/), [CVE-2020-2002](https://www.silverfort.com/blog/silverfort-researchers-panw-pan-os-cve-2020-2002/), [CVE-2020-3125](https://www.silverfort.com/blog/cisco-vulnerability-cve-2020-3125/), [CVE-2021-23008](https://www.silverfort.com/blog/silverfort-researchers-discover-kdc-spoofing-vulnerability-in-f5-big-ip-cve-2021-23008/)


It’s interesting to see how these implementation errors can be overlooked by so many developers. We responsibly disclosed them to the four vendors and worked with them to issue fixes, so the users of the systems are safe now, but there is a lesson to be learned here.


Don’t deviate from the spec!


Acknowledgements:


The said vulnerabilities were discovered by Silverfort researchers Yoav Iellin, Dor Segal, Rotem Zach and me. The Big IP vulnerability was a joint effort with Thierry Van Steirteghem, who worked at Exclusive Networks at the time of discovery.


***Yaron Kassner is co-founder and CTO at Silverfort.***


***Enjoy additional insights from Threatpost’s InfoSec Insider community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[Kerberos]] [[KDC]] [[system,]] [[TGT.]] [[it’s]] [[Client/Server]] [[KDC,]] [[ThreatPost]]
