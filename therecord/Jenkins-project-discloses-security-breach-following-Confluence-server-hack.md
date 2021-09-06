# Jenkins project discloses security breach following Confluence server hack
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/jenkins-project-discloses-security-breach-following-confluence-server-hack/)
+ Date: September 6, 2021
+ Author: Catalin Cimpanu


## Article:
![Jenkins project discloses security breach following Confluence server hack](https://therecord.media/wp-content/uploads/2021/09/Jenkins-logo.png)

The developers of the [Jenkins server](https://www.jenkins.io), one of the most widely used open-source automation systems, said they suffered a security breach after hackers gained access to one of their internal servers and deployed a cryptocurrency miner.


Despite the intrusion and malware deployment, the Jenkins team downplayed the severity of the breach in a [statement](https://www.jenkins.io/blog/2021/09/04/wiki-attacked/) published on Saturday.


Jenkins admins said the hacked server, which hosted the now-defunct Jenkins wiki portal (wiki.jenkins.io), had already been deprecated [since October 2019](https://groups.google.com/g/jenkinsci-dev/c/lNmas8aBRrI/m/eL3u7A6qBwAJ) when the project moved its wiki and team collaboration systems from a self-hosted Atlassian Confluence server to the GitHub platform.


“At this time we have no reason to believe that any Jenkins releases, plugins, or source code have been affected,” the Jenkins team said over the weekend.


Following the discovery of the hack, Jenkins developers said they permanently took down the hacked Confluence server, rotated privileged credentials, and reset passwords for developer accounts.


### Breach part of the larger Confluence attack wave


The Jenkins breach is part of a recent wave of attacks exploiting [CVE-2021-26084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-26084) (also nicknamed Confluenza), an authentication bypass and command injection bug in Atlassian’s Confluence server.


As [The Record first reported](https://therecord.media/confluence-enterprise-servers-targeted-with-recent-vulnerability/) last Wednesday, attacks against Confluence servers began last week and ramped up after security researchers published a proof-of-concept exploit on GitHub.


Attacks exploded throughout the week, prompting US Cyber Command to issue a public warning on Friday, urging administrators to patch affected systems before they left for the US Labor Day extended weekend.





The attacks, which most deployed cryptocurrency miners, according to security firms [Bad Packets](https://twitter.com/bad_packets/status/1433159086913187841) and [Rapid7](https://www.rapid7.com/blog/post/2021/09/02/active-exploitation-of-confluence-server-cve-2021-26084/), are still ongoing.


According to internet monitoring project Censys, there are currently around 15,000 Atlassian Confluence servers that can be reached over the internet. 


[According to Censys](https://censys.io/blog/cve-2021-26084-confluenza/), on Sunday, September 5, there were 8,597 Confluence servers connected online and still vulnerable to CVE-2021-26084.


![Vulnerable-Confluence-Servers](https://www-therecord.recfut.com/wp-content/uploads/2021/09/Vulnerable-Confluence-Servers.png)Image: Censys



#### Tags:
[[Jenkins]] [[server,]] [[The Record]]
