# Jenkins project's Confluence server hacked to mine Monero
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/jenkins-projects-confluence-server-hacked-to-mine-monero/)
+ Date: September 7, 2021
+ Author: Ionut Ilascu


## Article:
![Jenkins project's Confluence server hacked to mine Monero](https://www.bleepstatic.com/content/hl-images/2021/09/07/Jenkins.jpg)


Hackers exploiting the recently disclosed Atlassian Confluence remote code execution vulnerability breached an internal server from the Jenkins project.


While the attack is concerning because Jenkins is a popular open-source server for automating parts of software development, there is no reason that the project releases, plugins, or code have been impacted.



### Admins are being cautious


As [BleepingComputer reported](https://www.bleepingcomputer.com/news/security/atlassian-confluence-flaw-actively-exploited-to-install-cryptominers/) last week, after the proof-of-concept exploit code for CVE-2021-26084 became public, threat actors started to scan for vulnerable Atlassian Confluence instances to install cryptocurrency miners.


While many attackers used the exploit to install the open-source, cross-platform XMRig Monero cryptocurrency miner, they could also leverage the vulnerability for more damaging attacks.


Last week, administrators of the Jenkins project discovered that one of their deprecated Confluence server fell victim to one of these attacks.



“Thus far in our investigation, we have learned that the Confluence CVE-2021-26084 exploit was used to install what we believe was a Monero miner in the container running the service. From there an attacker would not be able to access much of our other infrastructure” - [Mark Waite](https://www.jenkins.io/blog/2021/09/04/wiki-attacked/), Jenkins Documentation Officer



Although there is no evidence suggesting that the attacker stole developer credentials, Jenkins project managers are being careful and have reset passwords for all accounts in the integrated identity system that also included the deprecated Confluence service.


The admins also said that they “are taking actions to prevent releases at this time until we re-establish a chain of trust with our developer community.” The affected Confluence service is no longer active and privileged credentials have been rotated.


CVE-2021-26084 is a remote code execution vulnerability in Atlassian Confluence that can be exploited without authentication. News about it emerged on August 25, when the company published a security advisory.


About a week later, technical details became publicly available along with proof-of-concept exploit code. Threat actors started leveraging so heavily that the U.S. Cyber Command (USCYBERCOM) [issued a warning](https://www.bleepingcomputer.com/news/security/us-govt-warns-orgs-to-patch-massively-exploited-confluence-bug/?mid=1#cid=5016532) about mass exploitation.



![US CyberCom warning about mass exploitation of CVE-2021-26084](https://www.bleepstatic.com/images/news/u/1100723/2021/USCyberComConfluence.jpg)source: [USCYBERCOM](https://twitter.com/cnmf_cyberalert/status/1433787671785185283)
 




#### Tags:
[[Jenkins]] [[Atlassian]] [[CVE-2021-26084]] [[Bleeping Computer]]
