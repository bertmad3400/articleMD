# Critical MQTT-Related Bugs Open Industrial Networks to RCE Via Moxa
### A collection of five security vulnerabilities with a collective CVSS score of 10 out of 10 threaten critical infrastructure environments that use Moxa MXview.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178399
+ Date: 2022-02-11T21:51:28+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2019/09/03102603/Software-Patch.jpg)

Critical security vulnerabilities in Moxa’s MXview web-based network management system open the door to an unauthenticated remote code execution (RCE) as SYSTEM on any unpatched MXview server, researchers warned this week.


The five bugs, affecting versions 3.x to 3.2.2, score a collective 10 out of 10 on the [CVSS vulnerability-severity scale](https://www.cisa.gov/uscert/ics/advisories/icsa-21-278-03), according to Claroty’s Team82 research team. Three of them can be chained together to achieve the aforementioned RCE (CVE-2021-38452, CVE-2021-38460 and CVE-2021-38458), but the others can be used to lift passwords and other sensitive information (CVE-2021-38456, CVE-2021-38454).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Moxa’s MXview network management software is designed for configuring and monitoring networking devices in industrial control systems (ICS) and operational technology (OT) networks. It has multiple components, Team82 noted in its [Thursday advisory](https://www.claroty.com/2022/02/10/blog-research-securing-network-management-systems-moxa-mxview/), including an [MQTT message broker](https://mqtt.org/) named Mosquitto that transfers messages to and from different components in the MXview environment.


“Moxa’s MXview is a significant player in the ICS and overall IoT market with their focus on converged networks – few network management vendors focus on this space, and therefore the significance of these vulnerabilities is high,” Bud Broomhead, CEO at Viakoo, said via email. “It’s worth noting that with manufacturing and line-of-business organizations using them, not all their end users will have the IT resources or knowledge to quickly remediate these vulnerabilities – making these high severity (10/10 score) vulnerabilities that much more dangerous.”


The bugs are patched in MXview version 3.2.4.


**A Vulnerable MQTT Environment**
---------------------------------


The implementation of MQTT is where the vulnerabilities lie, researchers explained.


“Sensitive information, such as credentials, is sent through the MQTT channels, and many callbacks are registered to perform certain actions whenever a message is sent,” they said. “Thus, accessing the MQTT will allow a malicious actor to exfiltrate sensitive data, and abuse other vulnerabilities…to execute remote commands.”


The MQTT protocol consists of a client that sends and receives messages, and a broker that routes messages to the appropriate clients. It also uses two roles, publisher and subscriber, to define how those messages are routed, Team82 researchers explained: “In order to distribute messages to the correct clients, the broker holds a list of topics, or channels, where publishers could send messages In order for a client to receive messages, it must subscribe to a topic. Whenever a message is sent to a specific topic, the broker distributes it to all subscribed users.”


The MXview software uses the MQTT server to distribute most of its IPC/RPC messages, they added, and most of the MXview APIs use the MQTT protocol to receive and handle requests. Mosquitto enables MQTT over Websockets, so that users can receive MQTT data via a web browser.


**Gaining MQTT Credentials**
----------------------------


The first chainable bug, CVE-2021-38452, is a file-read vulnerability that allows an unauthenticated attacker to read any file on the target operating system.


“Most of MXview’s web routes require a user to be authenticated,” according to Team82. “In most routes under the ResourceRoutes class, the sanitize-filename library is used in order to validate that the requested file does not contain malicious characters, namely path traversal characters (../).”


However, the server does not use the sanitize-filename library for one of the routes, called “/tmp.”


“This lack of validation allows a user to supply path-traversal characters that fetch arbitrary files,” according to the analysis. “Furthermore, since many passwords and configurations are saved on the disk as clear-text, a malicious user could use this unauthenticated file-read primitive to retrieve secret passwords and configurations (i.e., the password to the MQTT broker).”


**Achieving Remote Code Execution**
-----------------------------------


Once an attacker has access to the MQTT broker, CVE-2021-38454 and CVE-2021-38458 come into play to allow RCE through command injection. The former is an improper access-control issue that allows remote connections to internal communication channels. The latter is due to improper neutralization of special elements, which enables an attacker to remotely execute unauthorized commands, disable software, or read and modify otherwise inaccessible data.


The access-control bug, CVE-2021-38454, allows any MQTT broker user to execute arbitrary code with the highest privileges possible: NT AUTHORITY/SYSTEM. It is found in the validation mechanism for the ping route, which checks whether a given machine is alive by pinging it using the ICMP protocol.


“In the backend, the server validates the parameters given, and if they pass the validation check they are sent to a ping callback through the MQTT broker,” according to the analysis. “Later, an OnMessage callback is called, executing a ping cmd command using the given parameters. Because of the validation, a user could not append any malicious data to the ping command, thus preventing remote code execution through OS command injection.”


However, an attacker who has gained access to the MQTT system via the first vulnerability can inject a MQTT message directly to the MQTT broker.


“The OnMessage handler will still regard the message as if it was sent by the server, thus executing ping with the given parameters,” the researchers said. “Since we can inject the message directly into the MQTT queue, no validation or sanitation will be performed on the parameters when received by the callback, thus allowing any arbitrary value to be executed.”


The MQTT access bug could also be chained with CVE-2021-38458. It allows an unauthenticated user to write arbitrary files on the host server’s file system by abusing the MXview feature that allows users to add custom icons.


“An administrator does so by accessing a route that uploads a .PNG file to the web server and points to the new icon file,” according to Team82. “In order to restrict users from uploading files to any directory under any name, the server chooses the icon filename and instead saves only the file extension from the user-given file. The server then takes the user’s request, serializes it, and sends it to the MQTT broker, creating an action that will change a site’s icon. After the message is received, the onMessage callback is called with the created event, which results in the creation of the icon file.”


An attacker could abuse this by sending a malicious MQTT message containing path traversal characters, and inject it directly into the MQTT topic, they explained, thus resulting in the creation of arbitrary files on the host server’s file system.


“This is an impactful set of vulnerabilities,” Casey Ellis, founder and CTO at Bugcrowd, said via email. “Command injection via MQTT is an interesting and seldom discussed technique, and only goes to demonstrate the increasing complexity of the input vectors any given application may have. Proper sanitization is important everywhere, not just on real-time inputs which are exposed directly to users. MXview users would be well advised to patch as quickly as possible.”


**Information-Disclosure Bugs**
-------------------------------


As for the other two issues, CVE-2021-38460 allows password leakage, which may allow an attacker to obtain credentials through unprotected transport. And CVE-2021-38456 is because of the use of hard-coded passwords, which may allow an attacker to gain access to accounts using default passwords.


“Because [the bugs] are focused on converged networks it increases the likelihood of threat actors exploiting them in order to move laterally into corporate networks,” Broomhead said. “In addition, these vulnerabilities enable privilege-management exploits; vulnerabilities in privilege management almost always will be viewed as a high-level risk, especially given the damage that cybercriminals with root-level privileges can do such as placing malware, controlling critical infrastructure or covering the tracks of a threat actor.”


He added, “Adopting a [zero-trust architecture](https://threatpost.com/zero-trust-future-security-risks/177502/) can mitigate the risk of privilege-management vulnerabilities, but otherwise organizations must have methods to quickly remediate such a vulnerability.  Also worth noting is that many end users are not in IT; they are in manufacturing or line of business, and therefore may not have the knowledge or tools to quickly remediate these vulnerabilities, providing threat actors more time to exploit them.”


Mike Parkin, engineer at Vulcan Cyber, added: “Any vulnerability that gives privileged access to a system can be problematic, and the vulnerabilities discovered in MXview could be a serious issue for the users who have not patched. Fortunately, Moxa addressed these vulnerabilities shortly after they were discovered in Sept 2021 and released updated versions that are no longer vulnerable.  However, organizations that haven’t updated could find themselves the target of attack.”


***Join Threatpost on Wed. Feb 23 at 2 PM ET for a [LIVE roundtable discussion](https://threatpost.com/webinars/protect-sensitive-cloud-data/?utm_source=Website&utm_medium=Article&utm_id=Keeper+Webinar) “The Secret to Keeping Secrets,” sponsored by Keeper Security, focused on how to locate and lock down your organization’s most sensitive data. Zane Bond with Keeper Security will join Threatpost’s Becky Bracken to offer concrete steps to protect your organization’s critical information in the cloud, in transit and in storage. [REGISTER NOW](https://threatpost.com/webinars/protect-sensitive-cloud-data/?utm_source=Website&utm_medium=Article&utm_id=Keeper+Webinar) and please Tweet us your questions ahead of time @Threatpost so they can be included in the discussion.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=cmd]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Manufacturing]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Mqtt]] [[Mxview]] [[Team82]] [[“in]] [[ThreatPost]]
#### CVE's
[[CVE-2021-38452]] [[CVE-2021-38460]] [[CVE-2021-38458]] [[CVE-2021-38456]] [[CVE-2021-38454]]

