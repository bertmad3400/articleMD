# Apache's new security update for HTTP Server fixes two flaws | ZDNet
### There's a fix for a critical flaw in Apache HTTP Server, the world's second most widely used web server.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/apaches-new-security-update-for-http-server-fixes-two-flaws/
+ Date: 2021-12-23 12:34:54
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/ea7ac6295d660f6dc417b96565181b3806869928/2021/10/11/589e7a4f-7c19-4fbc-af72-6ea6007375c0/engineer-it-worker-male-data-technology.jpg?width=770&height=578&fit=crop&auto=webp)

The Apache Software Foundation has released an update to address a critical flaw in its hugely popular web server that allows remote attackers to take control of a vulnerable system. 

The foundation has released version 2.4.52 of the Apache HTTP Server (web server) that addresses two flaws tracked as [CVE-2021-44790](https://nvd.nist.gov/vuln/detail/CVE-2021-44790) and [CVE-2021-44224](https://nvd.nist.gov/vuln/detail/CVE-2021-44224), which have respective CVSS severity scores of 9.8 (critical) and 8.2 (high) out of a possible 10. A score of 9.8 is very bad, and in recent weeks has only been topped by the Log4j vulnerability known as Log4Shell, which had a [severity score of 10 out of 10](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/).    


The first Apache web server flaw is a memory-related buffer overflow affecting Apache HTTP Server 2.4.51 and earlier. The Cybersecurity and Infrastructure Security Agency (CISA) [warns](https://www.cisa.gov/uscert/ncas/current-activity/2021/12/22/apache-releases-security-update-http-server) it "may allow a remote attacker to take control of an affected system". The less serious flaw allows for server side request forgery in Apache HTTP Server 2.4.7 up to 2.4.51.  

**SEE:** [**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/#link=%7B%22role%22:%22standard%22,%22href%22:%22http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22%3Cstrong%3EA%20winning%20strategy%20for%20cybersecurity%3C/strong%3E%22%7D) **(ZDNet special report)**

This release of Apache HTTP Server is the [latest generally available release](https://httpd.apache.org/security/vulnerabilities_24.html) of the new generation 2.4.x branch of Apache HTTPD from Apache's 26-year-old HTTP Server Project, which maintains an important and modern open-source HTTP server for Unix and Windows platforms. 

Apache HTTP Server is the second most widely used web server on the internet behind Nginx, [according to W3Techs](https://w3techs.com/technologies/overview/web_server), which estimates it's used by 31.4% of the world's websites. UK security firm Netcraft estimates 283 million websites [used Apache HTTP Server in December 2021](https://news.netcraft.com/archives/category/web-server-survey/), representing 24% of all web servers. 

The critical bug is apparently not under attack yet but the HTTPD team believes it has the potential to be weaponized.  






"The Apache httpd team is not aware of an exploit for the vulnerability though it might be possible to craft one," the Apache HTTPD team said.

"A carefully crafted request body can cause a buffer overflow in the mod\_lua multipart parser (r:parsebody() called from Lua scripts)," [Apache Foundation's Steffan Eissing explained on a mailing list](https://seclists.org/oss-sec/2021/q4/172) .

As Netcraft notes, Apache HTTP Server wasn't directly impacted by the Java-based Log4j error messaging library as it was written in C. However, even web servers written in non-Java languages may still have integrated the vulnerable Log4j library in a technology stack. IBM's web server, WebSphere, integrates Log4j and was vulnerable, but Netcraft found only 3,778 sites using it. 

The Apache Software Foundation has released three updates in the past week in the wake of the widespread Log4Shell vulnerability in Log4j version 2 branch. 

Cybersecurity agencies from the US, Australia, Canada, New Zealand and the United Kingdom [yesterday released guidance for organizations to address the bug](https://www.zdnet.com/article/cisa-cybersecurity-centers-from-australia-nz-uk-and-canada-release-log4j-advisory/). The bug is expected to take months to resolve because the Log4j library has been integrated as a [component into hundreds of software products from major vendors](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/), including IBM, Cisco, VMware, RedHat and Oracle. The library also ships with important frameworks, such as Apache's Struts2.  





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Net Crawler]] [[action.malware.name=njRAT]]

#### Industry:
[[victim.industry.name=Agriculture]]

#### Location:
[[victim.country.name=United Kingdom]] [[victim.continent.name=Europe]] [[victim.country.name=Canada]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=New Zealand]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Http]] [[Log4j]] [[Httpd]] [[Netcraft]] [[ZDNet]]
#### CVE's
[[CVE-2021-44790]] [[CVE-2021-44224]]

