# Hundreds of millions of HP, Xerox, and Samsung printers vulnerable to new bug
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/hundreds-of-millions-of-hp-xerox-and-samsung-printers-vulnerable-to-new-bug/)
+ Date: July 20, 2021
+ Author: Catalin Cimpanu


## Article:
![Hundreds of millions of HP, Xerox, and Samsung printers vulnerable to new bug](https://therecord.media/wp-content/uploads/2021/07/HP-printer.jpg)

Security experts have found a severe vulnerability in a common printer driver used by HP, Xerox, and Samsung.


The bug, tracked as [CVE-2021-3438](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3438), has been present in the printer driver code since 2005 and impacts hundreds of millions of printers sold in the past 16 years.


“This vulnerability affects [a very long list](https://support.hp.com/us-en/document/ish_3900395-3833905-16/hpsbpi03724) of over 380 different HP and Samsung printer models as well as at least a dozen different [Xerox](https://securitydocs.business.xerox.com/wp-content/uploads/2021/05/cert_Security_Mini_Bulletin_XRX21K_for_B2XX_PH30xx_3260_3320_WC3025_32xx_33xx.pdf) products,” said Asaf Amir, a SentinelOne security researcher who discovered the issue and reported it to the affected companies in February this year.


Patches have been available for at least two months, but Amir has published his own [report](https://labs.sentinelone.com/cve-2021-3438-16-years-in-hiding-millions-of-printers-worldwide-vulnerable/) today to warn users about the severity of this vulnerability.


Described as a buffer overflow in a printer driver file called “SSPORT.SYS,” the bug could be abused for elevation of privilege attacks that allow locally installed malware or malicious code to gain ADMIN-level access to systems where the vulnerable driver is installed (an affected printer is connected).


“Among the obvious abuses of such vulnerabilities are that they could be used to bypass security products,” Amir said.


“Successfully exploiting a driver vulnerability might allow attackers to potentially install programs, view, change, encrypt or delete data, or create new accounts with full user rights,” the researcher added.


Furthermore, Amir also points out that some Windows systems may already have the vulnerable printer driver installed on their machines even without the user’s knowledge, something that happened when users connected one of the vulnerable printer models (see [HP](https://support.hp.com/us-en/document/ish_3900395-3833905-16/hpsbpi03724) and [Xerox](https://securitydocs.business.xerox.com/wp-content/uploads/2021/05/cert_Security_Mini_Bulletin_XRX21K_for_B2XX_PH30xx_3260_3320_WC3025_32xx_33xx.pdf) advisories) to their systems, and the driver was delivered via Windows Update.


Amir recommended that users check to see if their printer model is listed in the advisories and then install the latest printer driver update from the vendor’s website.


SentinelOne’s discovery comes two months after the security firm also found [a 12-year-old vulnerability in Dell’s DBUtil driver](https://therecord.media/dell-patches-12-year-old-driver-vulnerability-impacting-millions-of-pcs/) that could be abused in similar elevation of privilege attacks.





#### Tags:
[[]] [[The Record]]
