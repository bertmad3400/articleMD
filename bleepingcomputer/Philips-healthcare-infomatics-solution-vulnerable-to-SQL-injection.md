# Philips healthcare infomatics solution vulnerable to SQL injection
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/philips-healthcare-infomatics-solution-vulnerable-to-sql-injection/)
+ Date: November 5, 2021
+ Author: Bill Toulas


## Article:
![hospital](https://www.bleepstatic.com/content/hl-images/2021/10/18/hospital_ward.jpg?rand=125395396)


The Philips Tasy EMR, used by hundreds of hospitals as a medical record solution and healthcare management system, is vulnerable to two critical SQL injection flaws.


The vulnerabilities are tracked as [CVE-2021-39375](https://nvd.nist.gov/vuln/detail/CVE-2021-39375) and [CVE-2021-39376](https://nvd.nist.gov/vuln/detail/CVE-2021-39376), and both have a severity score of 8.8 in CVSS v3.


These are SQL injection flaws via two parameters, relying on the improper escaping of special characters in SQL commands.


The affected versions of the product are Tasy EMR HTML5 3.06.1803 and prior, so all organizations using the healthcare suite are urged to upgrade to version 3.06.1804 or later.


CISA has also released an advisory for the product, as it's widely deployed in many public and private health institutes, mainly in Argentina, Brazil, Colombia, Mexico, and the Dominican Republic.


"Organizations observing any suspected malicious activity should follow their established internal procedures and report their findings to CISA for tracking and correlation against other incidents," warned the [advisory](http://us-cert.cisa.gov/ics/advisories/icsma-21-308-01) from CISA.


According to Philips, the Tasy EMR is used by nearly 1,000 healthcare institutions around the world, and is the leading informatics solution in Latin America.


Data leaks in healthcare
------------------------


The Tasy EMR product holds sensitive medical records, patient care histories, medical supply details, financial and billing info, and general hospital management data.


As it is a central point for holding sensitive data, compromising it would lead to the exposure of a large number of people.


This becomes particularly problematic when hospitals are often forced to care for emergency patients without receiving consent for data processing.


The responsibility to secure this data often burdens public entities that have to work with limited resources and in difficult times imposed by a persisting pandemic.


These reasons are precisely why ransomware groups have [focused](https://www.bleepingcomputer.com/news/security/fbi-conti-ransomware-attacked-16-us-healthcare-first-responder-orgs/) on the [healthcare sector](https://www.bleepingcomputer.com/news/security/ryuk-ransomware-is-the-top-threat-for-the-healthcare-sector/) recently and why stealing files would be [enough on its own](https://www.bleepingcomputer.com/news/security/snapmc-hackers-skip-file-encryption-and-just-steal-your-files/) to initiate the extortion process.


Security measures
-----------------


Hospitals that use the Tasy EMR should upgrade to the latest available service pack, and Philips offers support on how to do that through its regional customer service teams.


Moreover, healthcare organizations should take steps to minimize the network exposure of similar systems, isolate them from external-facing networks, and deploy firewalls.


When doctors require remote access to these sensitive databases, they should always use VPN (Virtual Private Network) tools to connect to them.




#### Tags:
[[Tasy]] [[EMR]] [[SQL]] [[Bleeping Computer]]
