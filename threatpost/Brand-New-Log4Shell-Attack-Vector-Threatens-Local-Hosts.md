# Brand-New Log4Shell Attack Vector Threatens Local Hosts
### The discovery, which affects services running as localhost that aren't exposed to any network or the internet, vastly widens the scope of attack possibilities.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177128
+ Date: 2021-12-17T17:43:43+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/17121542/beaver-on-a-dam-a8b6a12-e1639761431383.jpg)

Defenders will once again be busy beavers this weekend: There’s an alternative attack vector for the ubiquitous Log4j [vulnerability](https://threatpost.com/apache-log4j-log4shell-mutations/176962/), which relies on a basic Javascript WebSocket connection to trigger remote code-execution (RCE) on servers locally, via drive-by compromise.


In other words, an exploit can affect services running as localhost in internal systems that are not exposed to any network.


That’s according to researchers at Blumira, who noted that the discovery eviscerates the notion that Log4Shell attacks [are limited to](https://threatpost.com/zero-day-in-ubiquitous-apache-log4j-tool-under-active-attack/176937/) exposed vulnerable web servers.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“This newly discovered attack vector means that anyone with a vulnerable Log4j version can be exploited through the path of a listening server on their machine, or local network through browsing to a website, and triggering the vulnerability,” researchers said in a Friday note to Threatpost.




---





**Check out all of our Log4Shell coverage:**



* [Relentless Log4j Attacks Include State Actors, Possible Worm](https://threatpost.com/log4j-attacks-state-actors-worm/177088/)
* [What the Log4Shell Bug Means for SMBs: Experts Weigh In](https://threatpost.com/log4shell-bug-smbs-experts/177021/)
* [How to Buy Precious Patching Time as Log4j Exploits Fly (Podcast)](https://threatpost.com/patching-time-log4j-exploits-vaccine/177017/)
* [Apache’s Fix for Log4Shell Can Lead to DoS Attacks](https://threatpost.com/apache-patch-log4shell-log4j-dos-attacks/177064/)
* [Where the Latest Log4Shell Attacks Are Coming From](https://threatpost.com/log4shell-attacks-origin-botnet/176977/)
* [Log4Shell Is Spawning Even Nastier Mutations](https://threatpost.com/apache-log4j-log4shell-mutations/176962/)
* [SAP Kicks Log4Shell Vulnerability Out of 20 Apps](https://threatpost.com/sap-log4shell-vulnerability-apps/177069/)
* [Zero Day in Ubiquitous Apache Log4j Tool Under Active Attack](https://threatpost.com/zero-day-in-ubiquitous-apache-log4j-tool-under-active-attack/176937/)











---






This means there are several new malicious use cases for an exploit, beyond the now-well-documented ability to open a shell with a single line of code to drop malware on internet-facing web servers.

“[New use cases include everything] from malvertisting to creating watering holes for drive-by attacks,” said Matthew Warner, CTO and co-founder of Blumira, in a technical post.



**Using WebSockets for Malicious Gain**
---------------------------------------


WebSockets enables communication between a web browser and web applications, like chats and alerting on websites. They generally allow the browser to quickly send data back and forth to these types of apps, but they’re also used for host-fingerprinting and port-scanning.


Warner explained in his posting that WebSockets is also fraught with security risk.


“WebSockets are not restricted by same-origin policies like a normal cross-domain HTTP request,” he explained. “They expect the server itself to validate the origin of the request. While they are useful, they also introduce a fair amount of risk as they do not include many security controls to limit their utilization.”


In the Log4j case, an attacker would make malicious requests via WebSockets to a potentially vulnerable localhost or local network server. The targets don’t have to be exposed to the internet.


“WebSockets have previously been used for port-scanning internal systems, but this represents one of the first remote code execution exploits being relayed by WebSockets,” said Jake Williams, co-founder and CTO at BreachQuest, via email. “This shouldn’t change anyone’s position on vulnerability management though. Organizations should be pushing to patch quickly and mitigate by preventing outbound connections from potentially vulnerable services where patching is not an option.”


**Local Attack Scenario for Log4Shell**
---------------------------------------


*Warner offered a detailed breakdown of his proof-of-concept (PoC) for the attack in [the posting](https://www.blumira.com/analysis-log4shell-local-trigger/); below is a truncated explanation.*


**Step 1:** From a watering-hole server with the affected Log4j2 vulnerability installed, an attacker would trigger a file path URL from the browser with a WebSocket connection. Blumira used a basic Javascript WebSocket connection in the PoC, but Warner noted that “this does not necessarily need to be localhost; WebSockets allow for connection to any IP and easily could iterate private IP space.”


**Step 2:** As the page loads, it will initiate a local WebSocket connection, connect to the vulnerable listening server, and connect out over an identified type of connection based on a Java Naming and Directory Interface (JNDI) connection string – a technique that’s similar to WebSockets’ localhost port-scanning used for fingerprinting hosts.


**Step 3:** Once the victim’s host connects to an open port to a local service or a service accessible to the host itself, an attacker can then drop an exploit string in path or parameters. “When this happens, the vulnerable host calls out to the exploit server, loads the attacker’s class, and executes it with java.exe as the parent process,” according to Warner.


**Detection and Remediation**
-----------------------------


The bad news is that this also a stealthy approach, according to the analysis: “WebSocket connections within the host can be difficult to gain deep visibility into, which increases the complexity of detection for this attack.” That’s because WebSocket connections silently initiate when a webpage loads, with no direct control by the client itself. However, Warner noted that there are ways to get around this.


To detect a possible attack, Warner recommended looking for instances of “.*/java.exe” being used as the parent process for “cmd.exe/powershell.exe.”


“This is potentially very noisy,” Warner said.


And finally, organizations should also make sure they’re set up to detect the presence of Cobalt Strike, TrickBot and related common attacker tools.


To identify where Log4j is used within local environments, there are publicly available scanning scripts, researchers noted, to identify the libraries used locally. Here are two:


* Windows PoSh – https://github.com/N-able/ScriptsAndAutomationPolicies/blob/master/Vulnerability%20-%20CVE-2021-44228%20(Log4j)/get-log4jrcevulnerability.ps1
* Cross platform – https://github.com/hillu/local-log4j-vuln-scanner/releases


To mitigate the risk completely, organizations should update all local development efforts, internal applications and internet-facing environments to Log4j 2.16 ASAP, including any custom applications.


In the meantime, users can implement egress filtering, which can restrict the callback required for the actual exploit to land, and can use tools like [NoScript Java-blocker](https://noscript.net/) on untrusted external sites to avoid Javascript triggering WebSocket connections.


“This news does mean that relying on web application firewalls, or other network defenses, is no longer an effective mitigation,” John Bambenek, principal threat hunter at Netenrich, said via email. “Patching remains the single most important step an organization can take.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=cmd]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=PS1]] [[action.malware.name=PS1]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=TrickBot]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Log4j]] [[Log4shell]] [[Websocket]] [[Websockets]] [[“this]] [[Javascript]] [[Localhost]] [[Blumira]] [[Port-scanning]] [[ThreatPost]]
#### urls
https://github.com/N-able/ScriptsAndAutomationPolicies/blob/master/Vulnerability%20-%20CVE-2021-44228%20(Log4j)/get-log4jrcevulnerability.ps1 https://github.com/hillu/local-log4j-vuln-scanner/releases
#### CVE's
[[CVE-2021-44228]]

