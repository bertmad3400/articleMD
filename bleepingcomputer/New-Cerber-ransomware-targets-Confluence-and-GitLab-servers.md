# New Cerber ransomware targets Confluence and GitLab servers
### Cerber ransomware is back, as a new ransomware family adopts the old name and targets Atlassian Confluence and GitLab servers using remote code execution vulnerabilities.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/new-cerber-ransomware-targets-confluence-and-gitlab-servers/
+ Date: 2021-12-07T13:19:53-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/07/Cerber___ransomware.jpg)

![Cerber](https://www.bleepstatic.com/content/hl-images/2021/12/07/Cerber___ransomware.jpg)


Cerber ransomware is back, as a new ransomware family adopts the old name and targets Atlassian Confluence and GitLab servers using remote code execution vulnerabilities.


As ransomware began picking up pace in 2016, a [new Cerber ransomware operation emerged](https://www.bleepingcomputer.com/news/security/the-cerber-ransomware-not-only-encrypts-your-data-but-also-speaks-to-you/) that quickly became one of the most prolific gangs at the time. However, its activity slowly tapered off until it disappeared at the end of 2019.


Starting last month, a ransomware called Cerber once again reared its ugly head, as it began infecting victims worldwide with both a Windows and Linux encryptor.


[![Tweet by MalwareHunterTeam](https://www.bleepstatic.com/images/news/ransomware/c/cerber/new-atlassian-gitlab/mht-tweet.jpg)](https://twitter.com/malwrhunterteam/status/1467264298237972484)


The new version of Cerber is creating ransom notes named **\_\_$$RECOVERY\_README$$\_\_.html** and appending the .locked extension to encrypted files.


From the victims seen by BleepingComputer, the new Cerber ransomware gang is demanding ransoms ranging from $1,000 to $3,000.



![Cerber Tor payment site](https://www.bleepstatic.com/images/news/ransomware/c/cerber/new-atlassian-gitlab/cerber-tor-payment-site.jpg)**Cerber Tor payment site**  
*Source: BleepingComputer*
Emsisoft CTO and ransomware expert [Fabian Wosar](https://twitter.com/fwosar) examined the new variant and said it does not match the code of the older family. In particular, the new version uses the Crypto+++ library, while the older variant used Windows CryptoAPI libraries.


These code differences and the fact that the original Cerber did not have a Linux variant lead us to believe that a new threat actor has adopted the name, ransom note, and Tor payment site, and is not the original operation.


Targeting Confluence and GitLab servers
---------------------------------------


This week, security researchers and vendors have seen the new Cerber ransomware operation hacking servers using remote code execution vulnerabilities in Atlassian Confluence and GitLab.


[![Tweet from BoanBird](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](https://twitter.com/Boanbird/status/1467649361085894656)


Security researcher BoanBird shared [a sample](https://www.virustotal.com/gui/file/772cad26853c7d8ea8f1023f6e3cba219cc9bb1db1cd31ad2b979e59d3d9c631/detection/f-772cad26853c7d8ea8f1023f6e3cba219cc9bb1db1cd31ad2b979e59d3d9c631-1638789065) of the new Cerber ransomware with BleepingComputer which shows this new strain specifically targets the Atlassian Confluence folders listed below.



```
C:\Program Files\Atlassian\Application Data
C:\Program Files\Atlassian\Application Data\Confluence
C:\Program Files\Atlassian\Application Data\Confluence\backups
```

BoanBird also shared a link to the GitLab forums where admins disclosed that Cerber exploits a recently disclosed vulnerability in GitLab's ExifTool component.



![Cerber targeting GitLab servers as well](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Cerber targeting GitLab servers as well**
These vulnerabilities are tracked as [CVE-2021-26084](https://www.bleepingcomputer.com/news/security/atlassian-confluence-flaw-actively-exploited-to-install-cryptominers/)(Confluence) and [CVE-2021-22205](https://www.bleepingcomputer.com/news/security/over-30-000-gitlab-servers-still-unpatched-against-critical-bug/) (GitLab) and can be exploited remotely without authentication. Additionally, both vulnerabilities have publicly disclosed proof-of-concept (PoC) exploits, allowing attackers to breach servers easily.


A report released this week by [researchers at Tencent](https://s.tencent.com/research/report/140) shows that attacks deploying the new Cerber ransomware are mostly targeting the United States, Germany, and China.


Although the previous version of Cerber excluded targets in the CIS (Commonwealth of Independent States), Tencent's telemetry data from the recent attacks shows otherwise. Furthermore, BleepingComputer has also independently confirmed multiple victims in Russia, indicating that these threat actors are indiscriminate in who they target.



![Victims heatmap on the latest Cerber attacks](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Victims heatmap on the latest Cerber attacks**  
*Source: Tencent*
At this time, the best approach to protect against Cerber would be to apply the available security updates for Atlassian Confluence and GitLab.


However, as more servers are patched, we should expect the threat actors to target other vulnerabilities to breach servers.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Germany]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cerber]] [[Ransomware]] [[Gitlab]] [[Atlassian]] [[Bleepingcomputer]] [[C:\program]] [[Files\atlassian\application]] [[Tencent]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-26084]] [[CVE-2021-22205]]

