# This sneaky hacking group targets old Java applications to break into networks | ZDNet
### Cybersecurity researchers warn about cyberattacks by 'Elephant Beetle' - which use over 80 tools and exploits legacy vulnerabilities to hide inside networks for months at a time.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/this-sneaky-hacking-group-targets-old-java-applications-to-break-into-networks/
+ Date: 2022-01-06 13:13:52
+ Author: Danny Palmer


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/065d07c4077f40f136b8819a9f03df4a39538d34/2021/08/06/c55fade0-6def-4c6d-b0b7-d501337b05d8/hands-on-a-keyboard-in-the-dark.jpg?width=770&height=578&fit=crop&auto=webp)

A highly organised and stealthy cyber-criminal operation is stealing millions of dollars from financial organisations in attacks that have been active for at least two years. 

The campaign has been [detailed by researchers at Israeli cybersecurity company Sygnia](https://blog.sygnia.co/elephant-beetle-an-organized-financial-theft-operation), who have dubbed the organised financial theft operation behind the attacks as 'Elephant Beetle'. 


These attacks are predominantly focused on financial organisations in Latin America, although researchers warned that the campaign could shift towards targets in other parts of the world. Researchers note that one of the breaches they uncovered when analysing Elephant Beetle campaigns was against the Latin American arm of an undisclosed US-based company. 

**SEE:**[**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/)**(ZDNet special report)**

Elephant Beetle campaigns take place over a long period, with those behind the attacks taking time to examine the financial systems of compromised victims in order to create fraudulent transactions hidden among regular activity, which adds up to millions of dollars being stolen.  

The entry point of the attacks is a focus on legacy Java applications running on Linux-based machines and web servers. The legacy nature of these systems means they're likely to [contain unpatched vulnerabilities](https://www.zdnet.com/article/these-software-bugs-are-years-old-but-businesses-still-arent-patching-them/) that can be exploited. 

Among these vulnerabilities are Primefaces Application Expression Language Injection ([CVE-2017-1000486](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-1000486)), WebSphere Application Server SOAP Deserialization Exploit ([CVE-2015-7450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-7450)), SAP NetWeaver Invoker Servlet Exploit ([CVE-2010-5326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2010-5326)), and SAP NetWeaver ConfigServlet Remote Code Execution ([EDB-ID-24963](https://vuldb.com/?id.8517)). 






In each case, the initial payload is a simple obfuscated web shell-enabling remote code execution, or a series of exploitations running different commands on the target machine. In total, the threat group uses an arsenal of over 80 unique tools and scripts to conduct the campaigns and identify additional security flaws while remaining undetected. 

To help stay under the radar, the attackers stick to smaller transactions that don't look suspicious on an individual basis, but when all the transactions against victims are added together, millions of dollars are being stolen. If an attempt at a transaction is detected and blocked, the attackers will lay low while remaining on the network for a few months, only to resume activity again once they feel the coast is clear. 

"Elephant Beetle is a significant threat due to its highly organised nature and the stealthy pattern with which it intelligently learns victims' internal financial systems and operations," said Arie Zilberstein, VP of incident response at Sygnia 

"Even after initial detection, our experts have found that Elephant Beetle is able to lay low, but remain deeply embedded in a compromised organization's infrastructures, enabling it to reactivate and continue stealing funds at any moment," he added. 

Analysis of incidents involving Elephant Beetle – along with phrases and keywords used in code, including 'Elephante' – suggests that the cyber criminals behind the attacks are Spanish-speaking. Researchers also note that many of the command and control servers used by Elephant Beetle appear to be located in Mexico. 

In addition to this, Sygnia's incident response team notes that the tools and techniques deployed by Elephant Beetle strongly resemble what [cybersecurity company Mandiant tracks as FIN13](https://www.mandiant.com/resources/fin13-cybercriminal-mexico), a cyber-criminal group focused on Mexico. 

**SEE: [Your cybersecurity training needs improvement because hacking attacks are only getting worse](https://www.zdnet.com/article/your-cybersecurity-training-needs-improvement-because-hacking-attacks-are-only-getting-worse/)** 

It's strongly believed Elephant Beetle is still actively compromising targets, but there are steps that organisations can take to avoid falling victim. Key to this is [applying patches and security updates](https://www.zdnet.com/article/this-one-change-could-protect-your-systems-from-attack-so-why-dont-more-companies-do-it/) to prevent attackers from exploiting known vulnerabilities in order to gain a foothold in networks. If legacy applications can't be patched, they should be isolated from the rest of the network when possible. 

"Particularly in the wake of widespread vulnerabilities like [Log4j](https://www.zdnet.com/article/log4j-flaw-attackers-are-making-thousands-of-attempts-to-exploit-this-severe-vulnerability/) that are dominating the industry conversation, organizations need to be apprised of this latest threat group and ensure their systems are prepared to prevent an attack," said Zilberstein. 

### **MORE ON CYBERSECURITY**

* [**Log4j flaw: Nearly half of corporate networks have been targeted by attackers trying to use this vulnerability**](https://www.zdnet.com/article/log4j-flaw-nearly-half-of-corporate-networks-have-been-targeted-by-attackers-trying-to-use-this-vulnerability/)
* [**This is how Formula 1 teams fight off cyberattacks**](https://www.zdnet.com/article/this-is-how-formula-1-teams-fight-off-cyberattacks/)
* [**Your cybersecurity training needs improvement because hacking attacks are only getting worse**](https://www.zdnet.com/article/your-cybersecurity-training-needs-improvement-because-hacking-attacks-are-only-getting-worse/)
* [**Phishing attacks: Police make 106 arrests as they break up online fraud group**](https://www.zdnet.com/article/phishing-attacks-police-make-106-arrests-as-they-break-up-online-fraud-group/)
* [**Ransomware: How banks and credit unions can secure their data from attacks**](https://www.zdnet.com/article/ransomware-how-banks-and-credit-unions-can-secure-their-data-from-attacks/)





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Israel]] [[victim.continent.name=Asia]] [[victim.country.name=Mexico]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cybersecurity]] [[Organisations]] [[Sygnia]] [[ZDNet]]
#### CVE's
[[CVE-2017-1000486]] [[CVE-2015-7450]] [[CVE-2010-5326]]

