# Mozilla fixes critical bug in cross-platform cryptography library
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/mozilla-fixes-critical-bug-in-cross-platform-cryptography-library/)
+ Date: December 1, 2021
+ Author: Sergiu Gatlan


## Article:
![Mozilla fixes critical bug in cross-platform cryptography library](https://www.bleepstatic.com/content/hl-images/2021/05/26/Mozilla___logo.jpg)


Mozilla has addressed a critical memory corruption vulnerability affecting its cross-platform Network Security Services (NSS) set of cryptography libraries.


[NSS](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS) can be used to develop security-enabled client and server apps with support for SSL v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3 certificates, and various other security standards.


The security flaw was [found](https://bugs.chromium.org/p/project-zero/issues/detail?id=2237) by Google vulnerability researcher Tavis Ormandy in NSS versions before 3.73 or 3.68.1 ESR—who also dubbed it BigSig—and is now tracked as [CVE-2021-43527](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43527).


It can lead to a [heap-based buffer overflow](https://cwe.mitre.org/data/definitions/122.html) when handling DER-encoded DSA or RSA-PSS signatures in email clients and PDF viewers using vulnerable NSS versions (the bug has been fixed in NSS 3.68.1 and NSS 3.73).


The impact of successful heap overflow exploitation can range from program crashes and arbitrary code execution to bypassing security software if code execution is achieved.




> 
> This is a major memory corruption flaw in NSS, almost any use of NSS is affected. The Mozilla advisory is here <https://t.co/AL8suyLQFF> <https://t.co/uTQ2gqRZ5t>
> 
> 
> — Tavis Ormandy (@taviso) [December 1, 2021](https://twitter.com/taviso/status/1466085701536010241?ref_src=twsrc%5Etfw)


All versions released since October 2012 vulnerable
---------------------------------------------------


"Applications using NSS for handling signatures encoded within CMS, S/MIME, PKCS #7, or PKCS #12 are likely to be impacted," Mozilla [said](https://www.mozilla.org/en-US/security/advisories/mfsa2021-51/) in a security advisory issued today.


"Applications using NSS for certificate validation or other TLS, X.509, OCSP or CRL functionality may be impacted, depending on how they configure NSS."


"We believe all versions of NSS since 3.14 (released October 2012) are vulnerable," Ormandy [added](https://bugs.chromium.org/p/project-zero/issues/detail?id=2237) on the Project Zero issue tracker.


"Mozilla plan to produce a thorough list of affected APIs - but the summary is any standard use of NSS is affected. The bug is simple to reproduce and affects multiple algorithms."


Luckily, according to Mozilla, this vulnerability doesn't impact the Mozilla Firefox web browser. However, all PDF viewers and email clients which use NSS for signature verification are believed to be impacted.


NSS is [used](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/Overview) by Mozilla, Red Hat, Google, SUSE, and others in a wide variety of products, including:


* Firefox, Thunderbird, SeaMonkey, and Firefox OS.
* Open-source client applications such as Evolution, Pidgin, Apache OpenOffice, and LibreOffice.
* Server products from Red Hat: Red Hat Directory Server, Red Hat Certificate System, and the mod\_nss SSL module for the Apache webserver.
* Server products from Oracle (formerly Sun Java Enterprise System), including Oracle Communications Messaging Server and Oracle Directory Server Enterprise Edition.
* SUSE Linux Enterprise Server supports NSS and the mod\_nss SSL module for the Apache webserver.




#### Tags:
[[NSS]] [[PKCS]] [[Mozilla]] [[SSL]] [[Ormandy]] [[Bleeping Computer]]
