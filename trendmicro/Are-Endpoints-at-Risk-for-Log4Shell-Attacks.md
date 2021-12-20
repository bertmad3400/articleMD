# Are Endpoints at Risk for Log4Shell Attacks
### We created a free assessment tool for scanning devices to know whether it is at risk for Log4Shell attacks.

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/21/l/are-endpoints-at-risk-for-log4shell-attacks.html
+ Date: 2021-12-18
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/are-endpoints-at-risk-for-log4shell-attacks/log4shelldesktop-main.jpg)





The end of 2021 saw the emergence of the [Log4Shell](/en_us/research/21/l/patch-now-apache-log4j-vulnerability-called-log4shell-being-acti.html) (CVE-2021-44228) vulnerability, a critical vulnerability in the ubiquitous Java logging package Apache Log4j. Exploiting Log4Shell via crafted log messages can  allow an attacker to execute code on remote machines. The potential impact of this vulnerability is great enough that it scores a [10.0 rating based on CVSS version 3.x and a 9.3  rating based on CVSS version 2.0](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) in terms of critical risk — and it’s easy to see why.


This vulnerability has the potential to have far-reaching consequences due to the widespread use of Log4j. When a user with malicious intent manages to take control of the log messaging system and affect the relevant Log4J processes, it can lead to possible remote code execution attacks.


While the attacks so far have been directed at the server level, there could be a second wave of attacks that can put endpoints at risk.


Possible Attacks on Devices
===========================


A malicious actor can use the vulnerability to trigger attacks against consumer devices and even automobiles. For example, recent demonstrations from various researchers have shownhow [Apple iPhones](https://github.com/YfryTchsGD/Log4jAttackSurface/blob/master/pages/apple.md) and even Tesla automobiles can be compromised through simple exploit strings, after which commands can be issued and sensitive data stolen from the backend servers being used for these machines.


Servers remain the targets with the highest risk of Log4Shell attacks, especially internet-facing servers that are using vulnerable versions of Log4j since they are the easiest to compromise. This is followed by internal servers that are running vulnerable Log4j versions, but also have some sort of exposed service that can be compromised by access brokers. Finally, it is possible that malicious actors could begin targeting desktops that are running vulnerable versions of Log4j through certain desktop applications.


What Can You Do?


Backed by publicly-available open-source tools, we have created a [vulnerability scanning tool](https://resources.trendmicro.com/Log4shell-Vulnerability-assessment.html) that can cover all possible scenarios — including attacks on servers, desktops, and endpoints. The tool can help users check if they are indeed running applications that have a vulnerable version of Log4j.


Given that exploits for Log4Shell are already being weaponized, patching vulnerable machines should be a priority for everyone. Most software vendors have released advisories to help their customers navigate to an appropriate solution. It is highly recommended users apply vendor patches to their latest iteration as they become available. 









## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Log4j]] [[Log4shell]] [[Trend Micro]]
#### CVE's
[[CVE-2021-44228]]
