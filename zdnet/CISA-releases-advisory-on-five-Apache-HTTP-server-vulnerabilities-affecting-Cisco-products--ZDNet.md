# CISA releases advisory on five Apache HTTP server vulnerabilities affecting Cisco products | ZDNet
### The government agency urged administrators to review Cisco's advisory and apply the necessary updates.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/cisa-releases-advisory-on-five-apache-http-server-vulnerabilities/
+ Date: 2021-12-09 22:59:14
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/6d0113523f5cf320ef44b5d02b5d4fc9a283df8c/2021/06/09/cf344a38-83a8-4965-a89d-e2ab3e7db290/cisco-sign.jpg?width=770&height=578&fit=crop&auto=webp)

CISA has [released a second advisory](https://www.cisa.gov/uscert/ncas/current-activity/2021/12/09/cisco-releases-security-advisory-multiple-products-affected-apache) about several Apache HTTP server vulnerabilities. Cisco [sent out a notice](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-httpd-2.4.49-VWL69sWQ) about the vulnerabilities in November, explaining that the Apache Software Foundation [disclosed five vulnerabilities](https://httpd.apache.org/security/vulnerabilities_24.html#2.4.49) affecting the Apache HTTP Server (httpd) 2.4.48 and earlier releases on September 16.

The IDs are CVE-2021-33193, CVE-2021-34798, CVE-2021-36160, CVE-2021-39275, CVE-2021-40438. 

Cisco noted that one of the vulnerabilities in the mod\_proxy module of Apache HTTP Server (httpd) could allow an unauthenticated, remote attacker to make the httpd server forward requests to an arbitrary server. 

Another could allow an attacker to exploit a vulnerability by sending a crafted HTTP request to a vulnerable device and a successful exploit could allow the attacker to get, modify, or delete resources on other services that may be inaccessible otherwise.

Cisco said in November, the Product Security Incident Response Team "became aware of exploitation attempts of the vulnerability identified by CVE-2021-40438."

Cisco said the products that are affected by the vulnerabilities include Cisco Cloud Services Platform 2100, Cisco Wide Area Application Services (WAAS), Cisco Wireless Gateway for LoRaWAN, Cisco TelePresence Video Communication Server (VCS), Cisco Expressway Series, Cisco UCS Manager, Cisco Network Assurance Engine, Cisco UCS Director Bare Metal Agent, Cisco UCS Central Software, Cisco Security Manager, Cisco Prime Optical for Service Providers, Cisco Prime Infrastructure, Cisco Prime Collaboration Provisioning, Cisco FXOS Software for Firepower 4100/9300 Series Appliances, Cisco Policy Suite and the Cisco Firepower Management Center.

The company added that it is investigating the following products: Cisco DNA Center, Cisco Unified Communications Domain Manager, Cisco Unified Communications Manager IM & Presence Service (formerly CUPS) and Cisco Smart Net Total Care - On-Premises. 






Some of the fixes are available now but others will be released in February, March, May and June of 2022. Administrators can find product-specific workarounds [in the Cisco notice](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-httpd-2.4.49-VWL69sWQ). 

Casey Ellis, CTO at Bugcrowd, said the vulnerabilities are critical in their impact and appear to be fairly easy to exploit.

Netenrich principal threat hunter John Bambenek told ZDNet that what stood out to him about the advisory is that the vulnerabilities were first known in August and an update to Apache was released in September. 

"Only now has Cisco issued their own advisory and begun the process to remediate the issue in their devices. Open source software makes up key components in many commercial offerings, however, patch and vulnerability management still pose problems, even for large enterprises," Bambenek said. 

"Devices with large control over environments the way Cisco devices do really ought to have come with more responsible scrutiny over updates to key components to their products."





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Http]] [[Ucs]] [[ZDNet]]
#### CVE's
[[CVE-2021-33193]] [[CVE-2021-34798]] [[CVE-2021-36160]] [[CVE-2021-39275]] [[CVE-2021-40438]]

