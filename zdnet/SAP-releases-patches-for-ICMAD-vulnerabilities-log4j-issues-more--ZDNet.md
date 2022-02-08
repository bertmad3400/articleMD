# SAP releases patches for ICMAD vulnerabilities, log4j issues, more | ZDNet
### One of the vulnerabilities has a risk score of 10 and would allow attackers to execute serious malicious activities on SAP users.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/sap-releases-patches-for-icmad-vulnerabilities/
+ Date: 2022-02-08 22:18:00
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/f60e683c7a06da49e8d34505118376c28380458f/2021/11/12/41131561-f18b-47f0-9b2b-da9dbb88dc65/sap.jpg?width=770&height=578&fit=crop&auto=webp)

Three vulnerabilities with CVSS of 10, 8.1 and 7.5 have been [patched](https://wiki.scn.sap.com/wiki/display/PSR/SAP+Security+Patch+Day+-+February+2022) by SAP after being discovered by cybersecurity firm Onapsis. 

The patches were were part of a group of 19 security notes released by the company about a range of security issues. Three of the vulnerabilities related to log4j and had a CVSS of 10. 


The vulnerabilities found by Onapsis -- dubbed "ICMAD" -- allow attackers to execute serious malicious activities on SAP users, business information, and processes, which ultimately compromises unpatched SAP applications. The issues revolve around SAP's [Internet Communication Manager (ICM)](https://t.nylas.com/t1/116/47xwb0lgi87p1v64m73t7t380/8/d516c2a71ffea58b792af332dd795d35497b84f6206626821f2e7e33c5b90bd7), a core component of many of their applications. 

ICM is the SAP component that enables HTTP(S) communications in SAP systems. Because ICM is exposed to the internet and untrusted networks by design, vulnerabilities in this component have an increased level of risk, the companies explained. 

JP Perez-Etchegoyen, CTO at Onapsis, told *ZDNet* that with a single request, an attacker could be able to steal every victim session and credentials in plain text and modify the behavior of the applications. 

"Abusing these vulnerabilities could be simple for an attacker as it requires no previous authentication, no necessary preconditions, and the payload can be sent through HTTP(S)," Perez-Etchegoyen said. 

SAP has [released](https://t.nylas.com/t1/116/47xwb0lgi87p1v64m73t7t380/9/e295f037d723316a019c39c45af8af5d5a61ad65c1770c6822a9a97896427e32) [two security notes](https://t.nylas.com/t1/116/47xwb0lgi87p1v64m73t7t380/10/fe90596d4565ae1ed9290ae45af039f0aa133fe58554e87d150fe7f81ac627be) about the issues, and the Cybersecurity and Infrastructure Security Agency (CISA) [issued](https://www.cisa.gov/uscert/ncas/current-activity/2022/02/08/critical-vulnerabilities-affecting-sap-applications-employing) its own notice urging customers to implement the patch. 






"These vulnerabilities can be exploited over the internet and without the need for attackers to be authenticated in the target systems, which makes them very critical," said Mariano Nunez, CEO and Co-founder of Onapsis. 


He went on to explain that Onapsis Research Labs had been investigating HTTP Smuggling issues over the last year before discovering the SAP issues. 

Threat actors, according to Onapsis, can send malicious payloads leveraging these HTTP Smuggling techniques and successfully exploit SAP Java or ABAP systems with an HTTP request that is indistinguishable from a valid message. These vulnerabilities can be exploited in affected systems over the internet and pre-authentication, meaning they are not mitigated by multi-factor authentication controls, Onapsis added. 

"SAP has partnered with Onapsis to maintain secure solutions for our global customer base," said Richard Puckett, Chief Information Security Officer for SAP. "It is through collaboration with key partners like Onapsis that SAP can provide the most secure environment possible for our customers. We strongly encourage all SAP customers to protect their businesses by applying the relevant SAP security patches as soon as possible." 

SAP said it is not aware of any data breaches that resulted from threat actors exploiting the vulnerability but urged customers to apply the security notes. 

**Onapsis** [**released**](https://t.nylas.com/t1/116/47xwb0lgi87p1v64m73t7t380/14/9037f0fa9b8e7a954f32273d3ce00d8cce9b4c3dfcf52311cad59698c5f499c5) **a free tool that SAP customers can use to scan their systems for affected applications.**

Aaron Turner, vice president at Vectra, said that what we learned in March of 2021 with [the Hafnium attack](https://www.zdnet.com/article/everything-you-need-to-know-about-microsoft-exchange-server-hack/) targeting on-premises Exchange servers is being replayed in the SAP ecosystem. 

"SAP servers are extremely rich targets, with significant access to material business processes and generally have multiple privileged credentials stored and used on those servers. With the Onapsis research, they have uncovered an exploit path that allows attackers to gain access to those privileged credentials to move laterally within the on-premises network and also pivot into the cloud, as most SAP customers have federated their legacy SAP workloads with cloud-based ones," Turner said. 

"Just as Hafnium allowed attackers to pivot from on-prem Exchange to M365, this SAP attack path could allow the same. The SAP security updates will be critical ones to install, not just to protect those on-premises SAP servers but also any systems, on-prem or cloud, that may share credentials or trust relationships with those servers."





## Tags:

#### Threatactor:
[[threatactor.name=HAFNIUM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Onapsis]] [[Http]] [[On-premises]] [[ZDNet]]

