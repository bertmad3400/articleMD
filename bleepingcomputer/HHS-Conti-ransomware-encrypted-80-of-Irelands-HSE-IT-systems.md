# HHS: Conti ransomware encrypted 80% of Ireland's HSE IT systems
### A threat brief published by the US Department of Health and Human Services (HHS) on Thursday paints a grim picture of how Ireland's health service, the HSE, was overwhelmed and had 80% of its systems encrypted during last year's Conti ransomware attack.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/hhs-conti-ransomware-encrypted-80-percent-of-irelands-hse-it-systems/
+ Date: 2022-02-04T11:01:14-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2020/10/29/0_Hospital.jpg)

![HHS: Conti ransomware encrypted 80% of Ireland's HSE IT systems](https://www.bleepstatic.com/content/hl-images/2020/10/29/0_Hospital.jpg)


A threat brief published by the US Department of Health and Human Services (HHS) on Thursday paints a grim picture of how Ireland's health service, the HSE, was overwhelmed and had 80% of its systems encrypted during [last year's Conti ransomware attack](https://www.bleepingcomputer.com/news/security/irelands-health-services-hit-with-20-million-ransomware-demand/).


This led to [severe disruptions of healthcare services](https://healthservice.hse.ie/staff/news/general/hse-it-cyber-attack-clinical-guidance.html) throughout Ireland and exposed the information of thousands of Irish people who received COVID-19 vaccines before the attack after roughly 700 GB of data (including protected health information) was stolen from HSE's network and sent to attackers' servers.


The short incident report [[PDF](https://www.hhs.gov/sites/default/files/lessons-learned-hse-attack.pdf)], based on a PwC independent post-incident review [[PDF](http://www.hse.ie/eng/services/publications/conti-cyber-attack-on-the-hse-full-report.pdf)] commissioned by the Board of the HSE in June 2021, reveals that the impact of this attack on HSE's IT environment was primarily caused by the organization's lack of preparedness to deal with such an incident.


"The HSE did not have a single responsible owner for cybersecurity, at senior executive or management level at the time of the incident. There was no dedicated committee that provided direction and oversight of cybersecurity and the activities required to reduce the HSE's cyber risk exposure," the HHS Cybersecurity Program said.


"The lack of a cybersecurity forum in the HSE hindered the discussion and documentation of granular cyber risks, as well as the abilities to identify and deliver mitigating controls. The HSE did not have a centralized cybersecurity function that managed cybersecurity risk and controls."


To top it all off, the HSE also had no security monitoring solutions deployed to help investigate and respond to security threats detected across its IT environment.


This led to a lack of response to Conti operators' malicious activity, which was far from stealthy, seeing that Cobalt Strike beacons deployed on multiple HSE servers starting with May 7, 2021, were detected by endpoint antivirus solutions, with the alerts being ignored.


"The impact of the ransomware on the IT environment was reported by the HSE's management to lead to 80% encryption," the HHS added.


"The impact of the ransomware attack on communications was severe, as the HSE almost exclusively used on-premise email systems (including Exchange) that were encrypted, and therefore unavailable, during the attack."



![HSE Conti ransomware incident timeline](https://www.bleepstatic.com/images/news/u/1109292/2022/HSE_Conti_ransomware_incident_timeline.png)*HSE Conti ransomware incident timeline (PwC/HSE)*
Luckily, [the Conti ransomware gang gave the HSE a free decryptor to restore systems](https://www.bleepingcomputer.com/news/security/conti-ransomware-gives-hse-ireland-free-decryptor-still-selling-data/), with the added warning that the attackers would still sell or publish the stolen data if the HSE did not pay a $20 million ransom.


"We are providing the decryption tool for your network for free. But you should understand that we will sell or publish a lot of private data if you will not connect us and try to resolve the situation," the Conti ransomware gang said on the negotiation chat page.


"The HSE is aware that an encryption key have been provided," the Irish Department of Health told BleepingComputer at the time. "However further investigations have to be conducted to assess if it will work safely, prior to attempting to use it on HSE systems."


Although the incident led to widespread disruption across Ireland's healthcare services, Taoiseach Micheál Martin, the Prime Minister of Ireland, [said](https://twitter.com/rtenews/status/1393269632904138757) that the HSE would not be paying any ransom.


Following the attack, an archive containing samples of stolen HSE files containing patient data was subsequently uploaded to the VirusTotal malware scanning site.


An Irish court later ordered VirusTotal to [provide any info on subscribers who downloaded or uploaded the confidential data](https://www.bleepingcomputer.com/news/security/virustotal-ordered-to-reveal-private-info-of-stolen-hse-data-downloaders/) (including email addresses, phone numbers, IP addresses, or physical addresses) stolen from Ireland's national health care network.


The archive of stolen HSE data was downloaded 23 times by VirusTotal subscribers before the service removed it on May 25, 2021, according to [The Journal](https://www.thejournal.ie/high-court-hse-cyber-attack-5480952-Jun2021/).





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=RTM]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Healthcare]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Hse]] [[Ransomware]] [[Conti]] [["the]] [[Cybersecurity]] [[(including]] [[Virustotal]] [[Bleeping Computer]]

