# Cyberattackers Hit Data of 80K Fertility Patients
### FCI's security measures protected its electronic medical record system, but the attackers still got at extremely intimate data found in administrative files.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177467
+ Date: 2022-01-07T21:14:35+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/07161555/cropped-PIXNIO-2488683-1200x800-1-e1641589983726.jpeg)

The protected health information of nearly 80,000 patients of Fertility Centers of Illinois (FCI) may have been pawed over by cyber intruders following a cyberattack.


[FCI](https://www.fcionline.com/) runs four clinics across Illinois. [According to](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf) the U.S. Department of Health and Human Services (HHS) Office for Civil Rights’ data breach site, the breach – reported on Dec. 27 – affected 79,943 people.


FCI’s data breach notice ([PDF](https://www.fcionline.com/hubfs/notice%203.pdf)) said that the healthcare organization first detected suspicious activity on its internal systems on Feb. 1, 2021. A subsequent investigation indicated that security systems had blocked attackers from accessing patient EMR (electronic medical records) systems. However, the intruder(s) managed to access administrative files and folders.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


FCI said that it immediately launched a “thorough and comprehensive review” of its records to identify the files accessed, the information contained in those files and the individuals to whom that information pertained.


By Aug. 27, 2021, FCI had determined that information related to certain FCI patients was included in the set of files that had been improperly accessed. One positive finding so far: FCI said it’s “not aware of any actual or attempted misuse of patient information as a result of this incident.”


May it stay that way, given the severe harm that could be done with the dizzying array of highly sensitive personally identifying information (PII) that was involved: a trove that could be mined for financial fraud, [identity theft](https://threatpost.com/identity-theft-spikes-covid-19-relief/163577/), healthcare fraud and more.


A Treasure Trove of Compromised Data
------------------------------------


The accessed files included some patients’ names, employer-assigned ID numbers, passport numbers, Social Security numbers, financial account information, payment card information, treatment information, diagnosis, treating/referring physicians, medical record number, medical billing/claims information, prescription/medication information, Medicare/Medicaid identification information, health insurance group numbers, health insurance subscriber numbers, patient account numbers, encounter numbers, ill health/retirement information, master patient index, occupational-health related information, other medical benefits and entitlements information, other medical ID numbers, patkeys/reason for absence, sickness certificate, usernames and passwords with PINs or account login information, and medical facilities associated with patient information.


The Big Business of Extremely Intimate Data
-------------------------------------------


Stealing this kind of data is big business. One example: In October, a Las Vegas man and former medical records tech was [sentenced](https://threatpost.com/transnational-fraud-military-members/175298/) to 12.5 years of prison for stealing PII that was then used to fraudulently claim Department of Defense (DoD) and Veterans Administration (VA) benefits, particularly targeting disabled veterans.


The data of more than 3,300 U.S. military service members, military dependents and civilians employed by the DoD were compromised as part of what turned out to be a transnational cybercrime ring created to defraud them out of $1.5 million in military benefits from the DoD and the VA.


With regards to the FCI breach, the organization said that it immediately took steps to eliminate unauthorized access and brought in independent forensic investigators to investigate and remediate the matter, on top of additional security measures meant to further secure access to data, individual accounts, and equipment, including the implementation of enterprise identity verification software.


FCI has also bolstered employee security practices training and has offered a year’s worth of free credit monitoring and identity theft protection through Equifax.


“Please be assured that we have invested considerable resources to ensure that such a vulnerability does not exist in the future,” FCI concluded.


The New Year Has Had a Lot of Picking On Patients
-------------------------------------------------


Easier said than done, apparently. Unfortunately, the new year has ushered in an undiminished zest for [attacking healthcare information](https://threatpost.com/healthcare-prey-ransomware-cyberattacks/167525/).


Earlier this week, Florida’s Broward Health System announced that the most intimate medical data of 1,357,879 patients was [breached](https://threatpost.com/broward-breach-healthcare-supply-chain/177401/) in October: evidence of what security researchers said is a soft-bellied healthcare software supply chain that’s proved to be a juicy target for cybercriminals.


Healthcare organizations are also in the same log-jammed boat as every other sector: They’re hyper-focused on mitigating threats associated with the Apache Log4j [vulnerability](https://threatpost.com/ftc-pursue-companies-log4j/177368/) and trying to avoid the disastrous consequences if the [Log4Shell](https://threatpost.com/log4j-related-flaw-h2-database/177448/) [flaws](https://threatpost.com/third-log4j-bug-dos-apache-patch/177159/) are [exploited](https://threatpost.com/aquatic-panda-log4shell-exploit-tools/177312/).


Earlier this week, Microsoft reported that it saw rampant Log4j exploit [attempts and testing](https://threatpost.com/microsoft-rampant-log4j-exploits-testing/177358/) through the end of December.


The Acute Danger of Log4j for Healthcare
----------------------------------------


On Dec. 17, a week after the discovery of the Log4j flaw, the HHS 405(d) Task Group issued a brief ([PDF](https://405d-website-8459en001cm127.s3.amazonaws.com/Documents/405dSBAR-Log4j-Final.pdf)) outlining the risks associated with the vulnerability that could have catastrophic security implications for healthcare and other sectors.


“The exploitation allows the execution of any code which could result in compromise of the server, download of malicious binaries, or propagation of further attacks such as ransomware or a zero-day attack,” according to HHS’s alert.


It’s not even clear how many healthcare systems and devices could be affected by Log4Shell or what all the ways of exploitation might be, but it’s estimated that it could potentially affect hundreds of millions of devices, networks and/or software platforms, HHS said.


“Healthcare organizations are dependent on readily available devices and software that are vendor-supplied and connected to an external network to operate. These complex and interconnected devices affect patient safety and privacy,” according to HHS.


“They represent potential attack vectors across an organization like medical equipment such as bedside monitors that monitor vital signs during an inpatient stay,” the alert continued. “Or, they may be more complicated, like infusion pumps that deliver specialized therapies and require continual drug library updates. If an attacker gained access to the network through a vulnerability such as Log4j, they would be able to gain control of the software and could potentially disconnect devices from the network, therefore, causing a disruption to daily procedures and putting patient safety at risk.”


HHS explained that mainstream and well-known organizations, including cloud services, use Log4j software and may be vulnerable, including cloud applications that medical organizations use for Electronic Health Records (EHR) services and outsourced security services such as Software as a Service (SaaS).


Github maintains a running [list](https://github.com/cisagov/log4j-affected-db) of affected services and products.


Admin Account Used to Get at Data
---------------------------------


Ben Pick, Principal Consultant at app security provider [nVisium](https://nvisium.com/), noted that FCI stated that it followed reasonable practices to protect users and that an administrative account was used to obtain the data: the privileged kind of account from which attackers can do beaucoup damage. “These higher privileged accounts often have access to widespread data and act as a single point of failure, as evidenced by the large amount of user data exposed,” he told Threatpost via email.


His advice, in lieu of knowing the cause of the administrator’s account being compromised, is to limit access rights based on need to know.


Failing that, monitor, monitor, monitor, Pick advised: “When these privileged accounts cannot be limited, then strong monitoring must be enforced. This would alert when anomalous calls are made to indicate when an administrator may be performing an excessive amount of searches and possibly exfiltrating data.”


The Soft Spot of APIs
---------------------


Mac McMillan, CEO of CynergisTek, predicted in an [interview](https://healthitsecurity.com/features/top-healthcare-cybersecurity-predictions-for-next-year) with HealthITSecurity that in the new year, ransomware operators will shift their focus away from encryption and on to data exfiltration.


Blame the soft spot of APIs, he said: “As interoperability becomes more of a mainstream priority for healthcare organizations and we see more APIs that are being introduced between critical systems, I think we’re going to see a rise in the number of attacks that are focused on compromising those APIs.


“It’s another area where [we] don’t typically have a good, consistent approach across the board in healthcare with respect to testing APIs for security.”


This is particularly true given that healthcare organizations are now looking at an API change-over deadline: By year’s end – Dec. 31, 2022 – they’re required to migrate to [Fast Healthcare Interoperability Resources](https://ecqi.healthit.gov/fhir) (FHIR) APIs in order to enable seamless data sharing. Implementing the new data standards will likely cause enough turmoil that threat actors will be that much more attracted to APIs as a [network entry point](https://threatpost.com/top-3-api-vulnerabilities-cyberattackers/169048/), McMillan suggested.


Why Was FCI’s Regulated Data Outside of Network Monitoring?
-----------------------------------------------------------


Jake Williams, Co-Founder and CTO at incident response firm [BreachQuest](https://breachquest.com/), noted to Threatpost on Friday that it’s not uncommon for medical organizations to store patient data outside of their EHR system, and it sounds like that’s what happened here.


“As the article notes, the EMR was not compromised due to unspecified security measures,” Williams said via email.


“However, files (presumably on some network share) were accessed by threat actors. It wouldn’t surprise me to learn that the EMR enforces [multi-factor authentication] or doesn’t use domain authentication.”


Williams suggested that organizations take inventory of where they may have regulated data that may fall outside of normal monitoring and audit controls: a topic that Citrix [iterated](https://threatpost.com/apis-out-of-shadows-protect-your-business/169334/) in a September sponsored article on Threatpost.


“Those who don’t perform regular data inventory searches almost certainly have regulated data in their file shares – a location where it is just one phishing email away from compromise,” Williams said.


*Photo courtesy of* *[Marko Milivojevic](https://pixnio.com/author/milim84 "Marko Milivojevic")* *via [Pixnio](https://pixnio.com/media/young-woman-belly-massage-pregnancy-family)*. *[Licensing details](https://creativecommons.org/licenses/publicdomain/).*


**Password** **Reset:** **[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):** Fortify 2022 with a password security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the *new* password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken. **[Register & Stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)** – sponsored by Specops Software.





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Derusbi]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=RTM]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Healthcare]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Healthcare]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Fci]] [[Log4j]] [[Hhs]] [[Threatpost]] [[Emr]] [[ThreatPost]]

