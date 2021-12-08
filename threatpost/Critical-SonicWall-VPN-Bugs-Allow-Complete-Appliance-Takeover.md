# Critical SonicWall VPN Bugs Allow Complete Appliance Takeover
### Unauthenticated, remote attackers can achieve root-level RCE on SMA 100-series appliances.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176869
+ Date: 2021-12-08T19:16:54+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/12081341/code-malware.jpg)

Critical security vulnerabilities in SonicWall’s Secure Mobile Access (SMA) 100-series VPN appliances could allow an unauthenticated, remote user to execute code as root.


The SMA 100 line was created to provide end-to-end secure remote access to corporate resources, be they hosted on-prem, cloud or hybrid data centers. It also offers policy-enforced access control to applications after establishing user and device identity and trust.


The most severe of the bugs, officially an unauthenticated stack-based buffer overflow issue, carries a 9.8 out of 10 on the CVSS vulnerability-severity scale. If exploited, it could allow a remote unauthenticated attacker to execute code as a “nobody” user in the appliance, meaning the person enters as root. The adversary could go on to take complete control of the device, enabling and disabling security policies and access privileges for user accounts and applications.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The issue (CVE-2021-20038) arises because the strcat() function is used when handling environment variables from the HTTP GET method used in the appliance’s Apache httpd server.


“The vulnerability is due to the SonicWall SMA SSLVPN Apache httpd server GET method of mod\_cgi module environment variables use a single stack-based buffer using `strcat,'” according to SonicWall’s [security advisory](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0026), issued Tuesday.


**Other Critical SonicWall CVEs**
---------------------------------


CVE-2021-20038 is just one of many bugs the vendor addressed this week. Also of note is another group of bugs, collectively tracked as CVE-2021-20045, which sports a combined critical CVSS score of 9.4. These are file explorer heap- and stack-based buffer overflows allowing remote code execution (RCE) as root.


“This vulnerability is due to the sonicfiles RAC\_COPY\_TO (RacNumber 36) method which allows users to upload files to an SMB share and can be called without any authentication,” according to the advisory. “RacNumber 36 of the sonicfiles API maps to the upload\_file Python method and this is associated with filexplorer binary, which is a custom program written in C++ which is vulnerable to a number of memory-safety issues.”


There’s also CVE-2021-20043, with a critical CVSS score of 8.8, which is also a heap-based buffer overflow allowing root-level code execution, but it requires authentication to exploit. It’s found in the getBookmarks function and is also due to the unchecked use of strcat.


“This vulnerability is due to the RAC\_GET\_BOOKMARKS\_HTML5 (RacNumber 35) method that allows users to list their bookmarks,” according to the advisory.


The remaining bugs are a cornucopia of authenticated and unauthenticated vulnerabilities ranging in severity from CVSs 6.3 to 7.5, as seen in the chart below:


SonicWall has issued patches for the bugs, which affect versions of its SMA 200, 210, 400, 410 and 500v products. SMA 100 series appliances with WAF enabled are also affected by the majority of the bugs, it said. A complete list of affected devices and versions [can be found here](https://www.sonicwall.com/support/product-notification/product-security-notice-sma-100-series-vulnerability-patches-q4-2021/211201154715443/).


Jacob Baines of Rapid7 and Richard Warren of NCC Group were credited with the discovery of the vulnerabilities.


**Patch Now**
-------------


The vendor said that so far, there’s no evidence that these vulnerabilities are being exploited in the wild, but patching should be on the agenda given that SonicWall devices are a hot target for cyberattackers.


In July, SonicWall issued an urgent [security alert warning](https://threatpost.com/sonicwall-vpn-bugs-attack/167824/) customers that an “imminent ransomware campaign using stolen credentials” was actively targeting known vulnerabilities in the SMA 100 series and its Secure Remote Access (SRA) VPN appliances.


In March, it came to light that a new variant of the Mirai botnet [was targeting](https://threatpost.com/mirai-variant-sonicwall-d-link-iot/164811/) known vulnerabilities in SonicWall devices (as well as in D-Link and Netgear). And in January, security firm Tenable [warned that](https://www.tenable.com/blog/cve-2021-20016-zero-day-vulnerability-in-sonicwall-secure-mobile-access-sma-exploited) “highly sophisticated threat actors” were exploiting CVE-2021-20016, a critical SQL injection vulnerability in SMA 100 devices.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***for the LIVE event!***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Sonicwall]] [[Stack-based]] [[Cvss]] [[Rapid7]] [[ThreatPost]]
#### CVE's
[[CVE-2021-20038]] [[CVE-2021-20045]] [[CVE-2021-20043]] [[CVE-2021-20016]]

