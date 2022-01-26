# Let's Encrypt is revoking lots of SSL certificates in two days
### Let's Encrypt will begin revoking certain SSL/TLS certificates issued within the last 90 days starting January 28, 2022. The move could impact millions of active Let's Encrypt certificates.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/lets-encrypt-is-revoking-lots-of-ssl-certificates-in-two-days/
+ Date: 2022-01-26T05:38:12-05:00
+ Author: Ax Sharma


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2020/07/10/ssl-header.png)

![ssl](https://www.bleepstatic.com/content/hl-images/2020/07/10/ssl-header.png)


Let's Encrypt will begin revoking certain SSL/TLS certificates issued within the last 90 days starting January 28, 2022. The move could impact millions of active Let's Encrypt certificates.


As a non-profit certificate authority run by Internet Security Research Group (ISRG), Let's Encrypt provides X.509 certificates for Transport Layer Security encryption at no cost.


'Mis-issued' certificates to be revoked
---------------------------------------


Yesterday, ISRG was informed by a third party who examined Let's Encrypt's [Boulder code repo](https://github.com/letsencrypt/boulder) that there were "two irregularities" in the certificate authority's implementation of "TLS using ALPN" validation method [[1](https://datatracker.ietf.org/doc/html/rfc8737), [2](https://cabforum.org/wp-content/uploads/CA-Browser-Forum-BR-1.7.4_redline.pdf)].


Consequently, the certificate authority had to make [two changes](https://community.letsencrypt.org/t/changes-to-tls-alpn-01-challenge-validation/170427) to how its TLS-ALPN-01 challenge validation works.


"All active certificates that were issued and validated with the TLS-ALPN-01 challenge before 00:48 UTC on 26 January 2022 when our fix was deployed are considered mis-issued," [explains](https://community.letsencrypt.org/t/2022-01-25-issue-with-tls-alpn-01-validation-method/170450) Let's Encrypt Site Reliability Engineer (SRE), Jillian.


To comply with Let's Encrypt [Certificate Policy](http://Certificate%20Policy), which requires the certificate authority to invalidate a Certificate within 5 days under certain conditions, the non-profit will begin revoking certificates at 16:00 UTC on January 28th, 2022.


Note, however, not all certificates are affected by the improper implementation of "TLS using ALPN" validation method. This planned revocation will only apply to certificates issued with the flawed TLS-ALPN-01 validation method.


"We estimate [less than] 1% of active certificates are affected. Subscribers affected by revocations will receive e-mail notifications if their ACME account contains a valid e-mail address. If you are affected by this revocation and need help renewing your certificate please ask questions in this [thread](https://community.letsencrypt.org/t/questions-about-renewing-before-tls-alpn-01-revocations/170449)," further explains the engineer.


"We will be providing more details about this incident in the next few days."


As of November 2021, the number of all active Let's Encrypt certificates surpassed 221 million, as seen by BleepingComputer.


Therefore, the number of affected active certificates (1% or less) could possibly touch millions—if these were issued with the flawed TLS-ALPN-01 challenge validation.



![Let's Encrypt growth stats](https://www.bleepstatic.com/images/news/u/1164866/2022/January-2022/letsencrypt-revoke/letsencrypt-stats.jpg)**Let's Encrypt growth statistics and active certificates**(Let's Encrypt)
Users receiving e-mail notifications
------------------------------------


Site owners with the affected Let's Encrypt certificates are reporting receiving email notifications, instructing them to renew their certificates as the revocation is about to kick in.



![Let's Encrypt email notification](https://www.bleepstatic.com/images/news/u/1164866/2022/January-2022/letsencrypt-revoke/email-notification.jpg)**Let's Encrypt sending out email notifications** ([Twitter](https://twitter.com/stereotype32/status/1486245346678231040))
"If you received the e-mail, then your account has successfully obtained at least one certificate in the last 90 days that was validated using the TLS-ALPN-01 challenge," explains Let's Encrypt in the aforementioned thread.


"All certificates issued in the last 90 days and validated with TLS-ALPN-01 challenge are affected. You need to (force) renew the certificate according to your ACME client's directions. If your client requires you to make a configuration change, please remember to revert after your certificate is renewed!"


Given the short notice, [not all users may be pleased](https://twitter.com/0x663030623472/status/1486244517036675072) with Let's Encrypt's sudden but necessary move.


On the bright side, though, those using automated certificate management solutions like Caddy Web Server can rest easy.


"Sites using Caddy v2.4.2 or newer should not have to take any action when automated certificates are revoked. Enjoy your sleep," [touts](https://twitter.com/caddyserver/status/1486226944597233664) the team behind Caddy Web Server.


"Caddy automatically staples OCSP for all relevant certificates. It will refresh the staple about halfway through its validity period. If the next status is *Revoked*, Caddy will replace the certificate right away."





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Tls-alpn-01]] [[E-mail]] [[Bleeping Computer]]

