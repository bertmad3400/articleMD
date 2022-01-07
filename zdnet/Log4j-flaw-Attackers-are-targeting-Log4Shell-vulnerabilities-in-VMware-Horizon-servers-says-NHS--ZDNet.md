# Log4j flaw: Attackers are targeting Log4Shell vulnerabilities in VMware Horizon servers, says NHS | ZDNet
### NHS Digital issues an advisory urging organisations to take action to protect themselves.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/log4j-flaw-attackers-are-targeting-log4shell-vulnerabilities-in-vmware-horizon-servers-says-nhs/
+ Date: 2022-01-07 15:48:14
+ Author: Danny Palmer


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/7d1c3f8fa1c4d1b23d8c8758d2f7573d3a5e4293/2022/01/07/941f9075-33c1-45f0-9d21-7d4d1067f421/getty-medical-professionals-at-a-computer.jpg?width=770&height=578&fit=crop&auto=webp)

The UK's National Health Service (NHS) has issued a warning that hackers are actively targeting Log4J vulnerabilities and is recommending that organisations within the health service apply the necessary updates in order to protect themselves. 

[An advisory by NHS Digital](https://digital.nhs.uk/cyber-alerts/2022/cc-4002#remediation-steps) says that an 'unknown threat group' is attempting to exploit a [Log4j vulnerability](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/) ([CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228)) in VMware Horizon servers to establish web shells which could be use to distribute malware, ransomware, steal sensitive information and other malicious attacks. 

It's unclear if the warning has been issued because attacks targeting NHS systems have been detected, or if the advisory has been released as a general precaution because of the ongoing problem of the critical security vulnerability in Java logging library Apache Log4j [which was disclosed in December](https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/). 

"We are aware of an exploit and are actively monitoring the situation. We will support our partners with the system response to this critical vulnerability and will continue to provide guidance to NHS organisations," an NHS spokesperson told ZDNet. 

The attacks being warned against exploit the Log4Shell vulnerability in the Apache Tomcat service embedded within VMware Horizon. Once the weaknesses have been identified, the attack uses the Lightweight Directory Access Protocol (LDAP) to execute a malicious Java file that injects a web shell into the VM Blast Secure Gateway service 

If successfully exploited, attackers can establish persistence on the affected networks and use this to carry out a number of malicious activities. 

NHS Digital recommends that organisations known to be running Horizon servers take the appropriate action and apply the necessary patches in order to ensure networks can resist attempted attacks. 






"Affected organisations should review the VMware Horizon section of the VMware security advisory VMSA-2021-0028 and apply the relevant updates or mitigations immediately," [said the alert](https://digital.nhs.uk/cyber-alerts/2022/cc-4002#remediation-steps). 

Log4j is used in many forms of enterprise and open-source software, including cloud platforms, web applications and email services, meaning that there's a wide range of software in organisations around the world which could be at risk from attempts to exploit the vulnerability. 

[Cyber criminals were quick to scan for vulnerable systems after the vulnerability was disclosed](https://www.zdnet.com/article/log4j-flaw-nearly-half-of-corporate-networks-have-been-targeted-by-attackers-trying-to-use-this-vulnerability/) and a variety of cyber criminals and many took the opportunity to launch attacks including malware and ransomware campaigns. Attackers are still actively exploiting the vulnerability, [Microsoft has warned](https://www.zdnet.com/article/log4j-flaw-attacks-are-causing-lots-of-problems-microsoft-warns/). 

It's feared that the widespread use of Log4j in open-source software – to the extent that there's the potential that organisations may not know it's even part of the ecosystem – could result in the vulnerability [being a problem for years to come](https://www.zdnet.com/article/log4j-flaw-could-be-a-problem-for-industrial-networks-for-years-to-come/). 

The UK's National Cyber Security Centre (NCSC) is [among those which have issued advice to organisations on how to manage Log4j vulnerabilities](https://www.zdnet.com/article/log4j-flaw-10-questions-you-should-be-asking/) in the long run. 

**MORE ON CYBERSECURITY**

* [**Log4j flaw: Attackers are 'actively scanning networks' warns new CISA guidance**](https://www.zdnet.com/article/cisa-cybersecurity-centers-from-australia-nz-uk-and-canada-release-log4j-advisory/)
* [**Log4j flaw: This new threat is going to affect cybersecurity for a long time**](https://www.zdnet.com/article/log4j-flaw-this-new-threat-is-going-to-affect-cybersecurity-for-a-long-time/)
* [**Apache releases new 2.17.0 patch for Log4j to solve denial of service vulnerability**](https://www.zdnet.com/article/apache-releases-new-2-17-0-patch-for-log4j-to-solve-denial-of-service-vulnerability/)
* [**Khonsari ransomware, Nemesis Kitten are exploiting Log4j vulnerability**](https://www.zdnet.com/article/khonsari-ransomware-iranian-group-nemesis-kitten-seen-exploiting-log4j/)
* [**Log4j: Conti ransomware attacking VMware servers and TellYouThePass ransomware hits China**](https://www.zdnet.com/article/conti-ransomware-attacking-vmware-vcenter-servers-through-log4j-vulnerability/)





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Organisations]] [[Log4j]] [[Nhs]] [[Vmware]] [[Ransomware]] [[ZDNet]]
#### CVE's
[[CVE-2021-44228]]

