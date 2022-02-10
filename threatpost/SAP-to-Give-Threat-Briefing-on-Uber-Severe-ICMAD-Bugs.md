# SAP to Give Threat Briefing on Uber-Severe ‘ICMAD’ Bugs
### SAP’s Patch Tuesday brought fixes for a trio of flaws in the ubiquitous ICM component in internet-exposed apps. One of them, with a risk score of 10, could allow attackers to hijack identities, steal data and more.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178344
+ Date: 2022-02-10T16:39:04+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/04/06142606/SAP2-e1617733579541.jpg)

There’s a trio of critical vulnerabilities, fixed on Tuesday, in SAP business applications that use the ubiquitous Internet Communication Manager (ICM): the component that gives SAP products the HTTPS web server they need to connect to the internet or talk to each other.


Also on Tuesday, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) issued a [security advisory](https://www.cisa.gov/uscert/ncas/current-activity/2022/02/08/critical-vulnerabilities-affecting-sap-applications-employing) about the bugs.


Security researchers from Onapsis – the security firm that specializes in security for SAP, Oracle, Salesforce, and other software-as-a-service (SaaS) platforms and that discovered the bugs – joined SAP in coordinating the release of [a Threat Report](https://onapsis.com/icmad-sap-cybersecurity-vulnerabilities?utm_campaign=2022-Q1-global-ICM-campaign-page&utm_medium=website&utm_source=third-party&utm_content=CISA-alert) describing the critical vulnerabilities onTuesday.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


As of Tuesday, Onapsis Research Labs had estimated that there were tens of thousands – approximately 40,000 – SAP customers running more than 10,000 potentially affected, internet-exposed SAP applications.


The vulnerabilities are tracked as CVE-2022-22536, CVE-2022-22532 and CVE-2022-22533. The first CVE, addressed in [Security Note 3123396](https://launchpad.support.sap.com/), received the tip-top risk score – a 10 out of 10. The other two CVEs received scores of 8.1 and 7.5, respectively.


SAP and Onapsis urged customers to apply both tSecurity Note 3123396 and [3123427](https://t.nylas.com/t1/116/4a3z713b1kum7z18ruaq7siqk/13/51ec755ca6f695096592b0335df2b6ec4ba279684d0ae63b9df0739442312162) without dealy..


Free Scanner Available
----------------------


Onapsis also provided a free, open-source vulnerability scanner tool to assist SAP customers in addressing these serious issues, available to download [here](https://github.com/Onapsis/onapsis_icmad_scanner).


In a [blog post](https://blogs.sap.com/2022/02/08/sap-partners-with-onapsis-to-identify-and-patch-cybersecurity-vulnerabilities/) published Tuesday, SAP Director of Security Response Vic Chung confirmed the severity of Onapsis’ findings


Chung said that if they aren’t remediated, the bugs – aka “ICMAD” – “will enable attackers to execute serious malicious activity on SAP users, business information and processes.”


Specifically, successful exploitation could lead to this frightening laundry list of cybersecurity hazards:


* Hijack of user identities, theft of all user credentials and personal information
* Exfiltration of sensitive or confidential corporate information
* Fraudulent transactions and financial harm
* Change of banking details in a financial system of record
* Internal denial of service attack that disrupts critical systems for the business


No Known Related Breaches – Yet
-------------------------------


“Since ICM is exposed to the internet and untrusted networks by design, vulnerabilities in this component have an increased level of risk,” Chung said.


The ICMAD bugs are critical memory-corruption vulnerabilities that should be patched promptly, given that ICM is a core component of SAP business applications – just one flavor of the business-critical apps that threat actors are actively targeting.


“As we have observed through recent threat intelligence, threat actors are actively targeting business-critical applications like SAP and have the expertise and tools to carry out sophisticated attacks,” said Mariano Nunez, CEO and co-founder of Onapsis. “The discovery and patching of the ICMAD vulnerabilities as well as those previously identified by Onapsis Research Labs, such as [RECON](https://onapsis.com/recon-sap-cyber-security-vulnerability) and [10KBLAZE](https://onapsis.com/resources/10kblaze), are essential to protecting the business-critical applications that power 92% of the Forbes Global 2000.”


As of Tuesday, SAP and Onapsis weren’t aware of any breaches related to the trio of bugs, but that’s clearly no reason to delay in applying the updates in [Security Note 3123396 [CVE-2022-22536]](https://launchpad.support.sap.com/) to affected SAP applications as soon as possible, they said.


What to Do
----------


Onapsis has prepared this on-demand [recording](https://hubs.ly/Q013KNxr0) that details what to do to avoid any damage.


As well, at noon ET on Thursday, Onapsis’ Nunez and SAP Chief Information Security Officer Richard Puckett will provide a [threat briefing](https://twitter.com/marianonunezdc/status/1491803623709310977) about the ICMAD vulnerabilities.



> 
> Join SAP's [#CISO](https://twitter.com/hashtag/CISO?src=hash&ref_src=twsrc%5Etfw) Richard Puckett and me on the threat briefing about the [#icmad](https://twitter.com/hashtag/icmad?src=hash&ref_src=twsrc%5Etfw) vulnerabilities. Make sure you have all the info to protect your business-critical SAP applications. Today at 12pm ET. [#sap](https://twitter.com/hashtag/sap?src=hash&ref_src=twsrc%5Etfw) [#onapsis](https://twitter.com/hashtag/onapsis?src=hash&ref_src=twsrc%5Etfw) [#research](https://twitter.com/hashtag/research?src=hash&ref_src=twsrc%5Etfw) [#cisa](https://twitter.com/hashtag/cisa?src=hash&ref_src=twsrc%5Etfw) [#icm](https://twitter.com/hashtag/icm?src=hash&ref_src=twsrc%5Etfw) [#security](https://twitter.com/hashtag/security?src=hash&ref_src=twsrc%5Etfw) <https://t.co/QObvbdN6sp>
> 
> 
> — Mariano Nunez (@marianonunezdc) [February 10, 2022](https://twitter.com/marianonunezdc/status/1491803623709310977?ref_src=twsrc%5Etfw)
> 
> 



***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Onapsis]] [[Business-critical]] [[Icmad]] [[Nunez]] [[ThreatPost]]
#### urls
https://t.co/QObvbdN6sp
#### CVE's
[[CVE-2022-22536]] [[CVE-2022-22532]] [[CVE-2022-22533]]

