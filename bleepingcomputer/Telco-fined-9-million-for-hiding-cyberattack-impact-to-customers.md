# Telco fined €9 million for hiding cyberattack impact to customers
### The Greek data protection supervisory authority has imposed fines of 5,850,000 EUR ($6.55 million) to COSMOTE and 3,250,000 EUR ($3.65 million) to OTE, for leaking sensitive customer communication data due to insufficient security measures.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/telco-fined-9-million-for-hiding-cyberattack-impact-to-customers/
+ Date: 2022-02-01T05:27:49-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/10/28/5G_antenna.jpg)

![antenna](https://www.bleepstatic.com/content/hl-images/2021/10/28/5G_antenna.jpg?rand=1536787541)


The Greek data protection authority has imposed fines of 5,850,000 EUR ($6.55 million) to COSMOTE and 3,250,000 EUR ($3.65 million) to OTE, for leaking sensitive customer communication due to a cyberattack.


As the agency says in an [announcement](https://www.dpa.gr/el/enimerwtiko/prakseisArxis/epiboli-prostimoy-gia-peristatiko-parabiasis-prosopikon-dedomenon-kai-mi), COSMOTE infringed at least eight articles of the GDPR, including violating its duty to inform affected customers of the true impact of the incident.


OTE (Hellenic Telecommunications Organization) and COSMOTE belong to the same entity, OTE Group, which is the largest technology company in Greece, offering fixed and mobile telephony, broadband, and network communication services.


The hacking incident
--------------------


An internal investigation conducted by COSMOTE in 2020 revealed that a hacker social engineered one of its employees through LinkedIn and later used brute-forcing tools to derive the target's account credentials.


According to the findings of the investigation, the adversary used a Lithuanian IP address for accessing one of OTE's servers repeatedly.


The threat actor leveraged the account credentials to steal database files on five separate occasions. The size of the stolen data amounted to 48GB.


COSMOTE keeps call details on its servers for 90 days for service quality assurance, and maintains an anonymized version of the data for another 12 months for statistical analysis that helps in targeted service improvement.


As the [data protection authority probe](https://www.dpa.gr/sites/default/files/2022-01/4_2022%20anonym%20%282%29_0.pdf) discovered, the anonymization process wasn't properly done, and the data holding periods weren't strictly respected.


The impact
----------


The compromised server contained sensitive subscriber details and call data that concerned the period between September 1, 2020, and September 5, 2020.


More specifically, the exposed details include the following:


* Rough positional data of 4,792,869 unique COSMOTE subscribers.
* Age, gender, plan, and ARPU of 4,239,213 unique COSMOTE subscribers.
* MSISDN/CLI of 6,939,656 users of other telecommunication providers who communicated with customers of COSMOTE.
* MSISDN, IMEI, IMSI, and connected tower position for 281,403 roaming subscribers of COSMOTE.

The above information could be used for highly targeted social engineering, phishing, and even extortion in some cases.


Still, the impact of the hacking incident could be significant for targeted subscribers who may be high-interest individuals.





## Tags:

#### Action:
[[action.malware.name=Arp]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Greece]] [[victim.continent.name=Europe]] [[victim.country.name=Lithuania]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cosmote]] [[Ote]] [[Bleeping Computer]]

