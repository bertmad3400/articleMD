# ‘Elephant Beetle’ spends months in victim networks to divert transactions
### A financially-motivated actor dubbed 'Elephant Beetle' is stealing millions of dollars from organizations worldwide using an arsenal of over 80 unique tools and scripts.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/elephant-beetle-spends-months-in-victim-networks-to-divert-transactions/
+ Date: 2022-01-05T08:00:00-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/04/elephant.jpg)

![elephant](https://www.bleepstatic.com/content/hl-images/2022/01/04/elephant.jpg?rand=216347998)


A financially-motivated actor dubbed 'Elephant Beetle' is stealing millions of dollars from organizations worldwide using an arsenal of over 80 unique tools and scripts.


The group is very sophisticated and patient, spending months studying the victim's environment and financial transaction processes, and only then moves to exploit flaws in the operation.


The actors inject fraudulent transactions into the network and steal small amounts over long periods, leading to an overall theft of millions of dollars. If they are spotted, they lay low for a while and return through a different system.


The expertise of 'Elephant Beetle' appears to be in targeting legacy Java applications on Linux systems, which is typically their entry point to corporate networks.


The actor's TTPs are exposed in a detailed technical report which the Sygnia Incident Response team shared with Bleeping Computer before publication.


Exploiting flaws and blending with normal traffic
-------------------------------------------------


'Elephant Beetle' prefers to target known and likely unpatched vulnerabilities instead of buying or developing zero-day exploits.


Sygnia researchers have observed the group for two years and can confirm the the threat actors exploiting the following flaws:


* Primefaces Application Expression Language Injection (CVE-2017-1000486)
* WebSphere Application Server SOAP Deserialization Exploit (CVE-2015-7450)
* SAP NetWeaver Invoker Servlet Exploit (CVE-2010-5326)
* SAP NetWeaver ConfigServlet Remote Code Execution (EDB-ID-24963)

All four of the above flaws enable the actors to execute arbitrary code remotely via a specially crafted and obfuscated web shell.



![An example of SAP exploitation](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/SAP_exploit.jpg)**An example of SAP exploitation**  
*Source: Sygnia*
The actors need to conduct long-term surveillance and research, so the next primary goal is to remain undetected for several months.


To achieve this, they try to blend with regular traffic by mimicking legitimate packages, disguising web shells as font, image, or CSS and JS resources, and using WAR archives to pack payloads.



![Webshells hiding in resource folders](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/webshells.jpg)**Webshells hiding in resource folders**  
*Source: Sygnia*
"The Elephant Beetle thieves will also try and literally overwrite non-threatening files, as they slowly prepare for the true attack," details the [Sygnia report](https://blog.sygnia.co/elephant-beetle-an-organized-financial-theft-operation).


"Another technique that was used by the threat actor was modifying or replacing completely the default web page files. – i.e., replacing the iisstart.aspx or default.aspx on IIS web servers."


"Using this technique allowed the threat group two things – the first is an almost guaranteed access to their web shell from other servers or from the internet, because the routes for this are often allowed by default."


Moving laterally through custom backdoors
-----------------------------------------


After the first web server has been compromised, the threat actor uses a custom Java scanner that fetches a list of IP addresses for a specific port or HTTP interface.


This tool is highly versatile and configurable, and Sygnia reports seeing it used extensively in the observed 'Elephant Beetle' operations.


Having identified potential internal server pivoting points, the actors use compromised credentials or RCE flaws to spread laterally to other devices in the network.



![Elephant Beetle lateral movement](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Elephant Beetle lateral movement**  
*Source: Sygnia*

> 
> "The threat group moves laterally within the network mainly through web application servers and SQL servers, leveraging known techniques such as Windows APIs (SMB/WMI) and 'xp\_cmdshell', combined with custom remote execution volatile backdoors." - Sygnia.
> 
> 
> 


The group uses two one-liner backdoors that facilitate lateral movement; a Base64 encoded PowerShell and a Perl back-connect backdoor.



![The Perl backdoor used by the actors](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**The Perl backdoor used by the actors**  
*Source: Sygnia*
The first backdoor simulates a web server and binds a remote code execution channel to target ports, while the second one executes an interactive shell for C2 communication (command reception and output).


In some rare cases, the hackers used a third backdoor for shellcode execution on the host via an encrypted tunnel created using a set of hardcoded certificates.


Attribution and defense tips
----------------------------


'Elephant Beetle' uses Spanish code variables and file names, and the majority of the C2 IP addresses they use are based in Mexico.


Also, the Java-written network scanner was uploaded to Virus Total from Argentina, probably during the early development and testing phase.


As such, the group appears to be connected to Latin America and may have a relation or overlap with the [actor FIN13](https://www.mandiant.com/resources/fin13-cybercriminal-mexico), tracked by Mandiant.


Some basic advice to defend against this actor includes:


* Avoid using the 'xp\_cmdshell' procedure and disable it on MS-SQL servers. Monitor for configuration changes and the use of 'xp\_cmdshell'.
* Monitor WAR deployments and validate that the packages deployment functionality is included in the logging policy of the relevant applications.
* Hunt and monitor for the presence and creation of suspicious .class file in the WebSphere applications temp folders.
* Monitor for processes that were executed by either web server parent services processes (i.e., 'w3wp.exe', 'tomcat6.exe') or by database-related processes (i.e., 'sqlservr.exe').
* Implement and verify segregation between DMZ and internal servers.

Finally, make sure to grab the indicators of compromise (IoC) from Sygnia's report that will help you hunt for 'Elephant Beetle' proactively.


Considering that this actor is exploiting old and unpatched vulnerabilities for the initial compromise, it is crucial to keep all of your applications updated with the latest security patches.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=P.A.S. Webshell]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mexico]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Argentina]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Sygnia]] [[Backdoors]] [[Bleeping Computer]]
#### CVE's
[[CVE-2017-1000486]] [[CVE-2015-7450]] [[CVE-2010-5326]]

