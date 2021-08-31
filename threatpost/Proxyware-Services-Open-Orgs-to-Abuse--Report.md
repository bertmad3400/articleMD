# Proxyware Services Open Orgs to Abuse – Report
### Services that let consumers resell their bandwidth for money are ripe for abuse, researchers warn. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169068)
+ Date: August 31, 2021  4:12 pm
+ Author: Tom Spring


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/31151856/bandwidth.jpg)
Services that allow consumers to resell their own internet bandwidth for profit to businesses that want to resell it are ripe for abuse, according to researchers.


The burgeoning business model is growing in popularity with consumers who earn about $1 for every 10GB of their bandwidth shared with services that include Honeygain, Nanowire, IPRoyal Pawns, Peer2Profit and PacketStream.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“These relatively new platforms were built with a legitimate purpose, but attackers quickly found ways to abuse them,” according to a report by [Cisco Talos posted Tuesday](https://blog.talosintelligence.com/2021/08/proxyware-abuse.html). Services are delivered as desktop and mobile applications. Apps fall into a category called proxyware, because they turn the device running the software into a type of proxy server.


Proxyware services are attractive to businesses that use them for internet-related traffic research, such as search engine optimization. The ability to access residential and geographically diverse IP addresses can be extremely helpful. Uses also include testing potential online advertising campaigns or circumventing commercial network restrictions.


For consumers, Cisco points out, proxyware services are “advertised as a means to circumvent geolocation checks on streaming or gaming platforms,” while at the same time allowing consumers to generate income for the use of their bandwidth.


Why Are Proxyware Services Potentially Dangerous?
-------------------------------------------------


Researchers found that abuse of the services – by consumers and adversaries – present a myriad of risks, including:


Growing Proxyware Trend Presents Cybersecurity Challenges
---------------------------------------------------------


“As proxyware has grown in popularity, attackers have taken notice and are now attempting to exploit this interest to monetize their malware campaigns,” according to the report’s co-authors: Edmund Brumaghin, threat researcher, and Vitor Ventura, outreach researcher, both with Cisco Talos.


Researchers say adversaries are currently using proxyware services to run malware campaigns and monetize the internet bandwidth of victims. They compare the trend with how adversaries surreptitiously installed [cryptocurrency mining software](https://threatpost.com/fake-ad-blocker-cryptominer-ransomware/164669/) on victims’ computers in an attempt to monetize CPU cycles.


“These applications pose significant privacy and operational risks to organizations as they may allow nefarious or abusive network traffic to appear as if it originates from their corporate networks resulting in reputational damages that may also lead to service disruption,” researchers wrote.


With regards to this report, Threatpost is waiting for Honeygain and Nanowire, two leading services in this space, to reply to requests for comment.


**Growing Trend and Associated Threats**
----------------------------------------


Pinpointing how many consumers are using these types of services is difficult. To gauge interest and the user-base of Honeygain, market leader of the niche, Cisco examined subscriber growth of the Honeygain subreddit on Reddit from zero in 2019 to close to 8,000 as of July 2021. According to Cisco’s investigation, Honeygain boasted a quarter million users, based on Honeygain’s reported responses to a survey of its customers.


Estimating how many legitimate companies use proxyware services is equally hard to determine.


“Investigating DNS activity associated with the API used by the Honeygain client, we identified a large number of queries being performed. This is another indicator that clearly demonstrates the popularity of this platform across the internet,” researchers wrote.


**Active Abuse: Proxyware Services Under Attack**
-------------------------------------------------


Cisco found a number of existing malware campaigns were distributing trojan-ized versions of the proxyware applications. “Threat actors are distributing the proxyware applications to monetize victims’ network bandwidth for the purposes of generating revenue,” researchers reported.


In other instances documented by Cisco, “threat actors are distributing malicious executables that pose as installers for legitimate proxyware applications like Honeygain. When executed, they will typically install the legitimate application, while also silently installing malware.”


As expected, adversaries adopt a number of different techniques, similar to those of malicious crypto-miners, both for running the application silently and maintaining process persistence.


**Proxyware as a Tor Alternative**
----------------------------------


For adversaries, abuse of proxyware services offers the added benefits of anonymity.


**“**We believe attackers are highly likely to abuse these proxyware platforms, as they can be used to disguise an attacker’s origin more efficiently than Tor, since the exit nodes cannot be cataloged,” researchers said.


For the services themselves, the illegitimate use of their platforms by adversaries can mean end-users are blocklisted due to activities they don’t even control, researchers said. “It (also) increases organizations’ attack surface, potentially creating an initial attack vector directly on the endpoint.”


**Security Teams: Consider Yourselves Warned**
----------------------------------------------


Cisco Talos classified proxyware as potentially unwanted applications (PUA) or potentially unwanted programs (PUP).


“These platforms may introduce significant risk to most corporate environments,” researchers noted.


Researchers said that an examination of the Honeygain platform revealed that “because of the way the communications are processed to facilitate the retrieval and delivery of content it may be possible to monitor the DNS activity of other platform users.”


Researchers said unencrypted content, such as HTTP traffic, could be intercepted and manipulated in transit by Honeygain nodes under adversarial control.


“These platforms also pose new challenges for researchers, since there is no way to identify a connection through these kinds of networks — the origin IP becomes even less meaningful in an investigation. Due to the various risks associated with these platforms, it is recommended that organizations consider prohibiting the use of these applications on corporate assets,” researchers advised.




#### Tags:
[[proxyware]] [[Honeygain]] [[Proxyware]] [[“These]] [[malware]] [[ThreatPost]]
