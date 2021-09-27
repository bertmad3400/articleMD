# 5 Steps to Securing Your Network Perimeter
### Ekaterina Kilyusheva, head of the Information Security Analytics Research Group at Positive Technologies, offers a blueprint for locking up the fortress.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175043)
+ Date: September 27, 2021  4:29 pm
+ Author: Ekaterina Kilyusheva


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/27162144/moat-e1632774120584.png)
When it comes to security, some of tomorrow’s biggest threats will come from yesterday’s vulnerabilities. In that regard, the network perimeter is a primary concern.


Network security has been discussed for years, and many best practices are well documented. And yet, according to [Positive Technologies research](https://www.ptsecurity.com/ww-en/analytics/vulnerabilities-corporate-networks-2020/), 84 percent of companies still have high-risk vulnerabilities on the perimeter, more than half (58 percent) have high-risk flaws with publicly available exploits, and – alarmingly — 26 percent are still vulnerable to WannaCry.


All of these factors, combined with the switch to remote work, have caused an increase in attacks exploiting vulnerabilities on the network perimeter, from five percent in Q1 2020 to 26 percent in the same quarter this year. One reason why companies can become targets is because low-skilled hackers often sell network access to more experienced criminal groups, such as ransomware operators. Exploits are now available for 10 percent of vulnerabilities detected on the perimeter, and that means even those without professional programming skills or experience in reverse engineering can exploit them.


So what measures should be taken to protect the network perimeter today, and which flaws are most commonly present in companies?


**Step 1. Get Rid of the Deadwood**
-----------------------------------


During a security assessment, even a cursory glance at any company’s services available online can say a lot about its security level. If only a few services are available, they’re usually protected by secure configuration and recent software updates that significantly facilitate eventual reconfiguration. Building a secure perimeter must start from resource inventory–in other words, from detecting and disabling active services that are not being used, as well as insecure protocols, and making sure that accessible interfaces truly need to be available online.


Which services are most frequently available to attackers? In Positive Technologies testing, we found every single company had TCP network ports 80 and 443 open on the perimeter. As a rule, these network ports have applications running on Apache HTTP Server, Apache Tomcat, Nginx and other web servers. By identifying a web server and its version, attackers can select relevant exploits.


Our research proved that 16 percent of web-server vulnerabilities have publicly available exploits. The availability of TCP network port 80 means that data can be exchanged via the HTTP protocol. And as we know, HTTP traffic is transmitted without encryption, meaning attackers can intercept it.


Analysis also revealed remote access and administration interfaces available on numerous resources, such as SSH, RDP or Telnet. Having these interfaces available to everyone on the internet is dangerous because they can allow any criminal to conduct brute-force attacks, so access to them should be limited.


Let’s remember that attacks on remote-access services have been among the main cybercrime trends of 2020 and 2021. Organizations should also abandon the use of Telnet (which was found in 21 percent of companies), because it transmits credentials in cleartext, and replace it with SSH. To make SSH connections more secure, use public key authentication, block SSH access for the root account, and use a non-standard port to guard against mass automated attacks.


At 84 percent of companies, TCP port 25 is open with the SMTP email service available on the perimeter. Data is transmitted in cleartext via SMTP, which means that just like with HTTP, attackers can intercept traffic and read corporate emails. In addition, insecure configuration of mail servers may leak corporate email addresses. The collected corporate email addresses can be used to brute-force credentials for network perimeter resources or remote access to the internal network, or to send phishing emails.


**Step 2. Keep Software Up-to-Date**
------------------------------------


Positive Technologies research found that almost half of all detected vulnerabilities (47 percent) can be eliminated by simply installing the latest software updates. However, the same research also found that all companies had problems with keeping software up to date.


In fact, we found software that had reached its end of life at 42 percent of organizations, and we know at that point, developers stop releasing security updates. For example, 32 percent of companies still use PHP 5 applications, even though support for that language ended in January 2019.


As a result, 30 percent of vulnerabilities detected in outdated software versions and web-application code are among the most dangerous program code errors, according to [MITRE](https://cwe.mitre.org/top25/archive/2019/2019_cwe_top25.html). This MITRE ranking includes the most common critical errors that can be easily found and exploited by attackers in order to steal information, cause denial of service, or obtain full control over a vulnerable application.


Our research into network vulnerabilities also found that more than half of companies have vulnerabilities allowing execution of arbitrary code on the server, and 16 percent of these flaws have publicly available exploits, meaning the organizations had not patched for known vulnerabilities.


Almost two-thirds (64 percent) of these vulnerabilities are of high severity. The most common vulnerability was [CVE-2017-12617](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-12617) in Apache Tomcat, which is dangerous because attackers can exploit it to upload a JSP file to a vulnerable server and execute code contained in this file.


In the worst case, this could let attackers breach the network perimeter and access the local network, opening up the possibility for them to then steal confidential data, encrypt files with ransomware, gain access to critical business systems or obtain full control over the infrastructure.


**Step 3. Make Sure Configurations Are Safe**
---------------------------------------------


Positive Technologies testing of network perimeters found that all companies had hosts that disclosed technical information: The contents of configuration files, routing to scanned hosts, OS versions and supported protocol versions.


The more information about the system attackers can collect, the higher the chance of a successful attack. Insecure configuration of services can also cause data leaks: For example, criminals can swipe detailed information about the system if the Community String value for the SNMP protocol — normally used to monitor various settings of network devices —  is set as public or private. Ensure that all interfaces are configured securely.


Pay particular attention to the versions of supported protocols. For example, insecure versions of the SSL/TLS protocol can lead to disclosure of confidential information (see vulnerabilities [CVE-2016-2183](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-2183), [CVE-2014-3566](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566) and [CVE-2013-2566](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-2566)).


Keep in mind that some vulnerabilities are related to the use of weak cryptographic mechanisms and keys. SSL certificates of 68 percent of companies use SHA-1 and MD5 hash functions. There are well-known attacks aimed at exploiting collisions in these algorithms, allowing attackers to compromise the certificate.


And, certificates at 53 percent of companies use RSA keys with a length of 1,024 bits or less. A weak secret RSA key in SSL/TLS allows an attacker to intercept a session by masquerading as a legitimate server. The recommended NIST length of an RSA key [is at least 2,048 bits](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf), so be sure to use strong cryptography.


**Step 4. Use an Effective Vulnerability Management Process**
-------------------------------------------------------------


International vulnerability databases annually publish information about thousands of new flaws. In addition, corporate IT infrastructures constantly go through changes, each of which potentially entails a security risk. All this makes vulnerability management a complex task.


Ensuring effective vulnerability management requires proper instrumental solutions, but with modern security assessment tools, companies can go beyond automating resource inventories and vulnerability searches to assess security policy compliance across the entire infrastructure.


**Step 5. Test the Robustness of the Perimeter**
------------------------------------------------


Combine automated scanning with penetration testing. Automated scanning is only the first step toward achieving an acceptable level of security; subsequent steps should include verification, triage and remediation of risks and their causes.


Some of these steps represent common sense, while others require a concerted strategy matched with enforced policies. But they are all necessary. The network perimeter is a dynamic arena — if the situation isn’t made better with effective security, it will surely get worse.


***Ekaterina Kilyusheva is head of the Information Security Analytics Research Group,* *Positive Technologies.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[perimeter,]] [[percent)]] [[TCP]] [[HTTP]] [[example,]] [[RSA]] [[ThreatPost]]
