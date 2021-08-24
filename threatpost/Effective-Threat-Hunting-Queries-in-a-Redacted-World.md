# Effective Threat-Hunting Queries in a Redacted World
### Chad Anderson, senior security researcher for DomainTools, demonstrates how seemingly disparate pieces of infrastructure information can form perfect fingerprints for tracking cyberattackers’ infrastructure.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168864)
+ Date: August 24, 2021  8:00 am
+ Author: Chad Anderson


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/23103924/hunting-e1629729578301.jpg)
A decade ago, hunting for adversary infrastructure was often as simple as monitoring a domain registrant’s name or phone number in public WHOIS records. As bad actors have moved first toward privacy protection services and then gained further obscurity behind laws such as the General Data Protection Regulation (GDPR) and the California Consumer Privacy Act (CCPA), many in the cybersecurity industry have lamented the loss of unredacted WHOIS records as an end to effective hunting.


However, while registrant information certainly provided an easy solution for sloppy actors that included unique details, WHOIS information has never been as reliable or foolproof of a method as many made the information out to be.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Many reports share indicators of compromise (IoCs) as individual items, but the initial intent of IoCs were to be constructed more as composite objects. This is because a single IP address or domain name are not useful except for as a flat firewall rule for blocking traffic. As we are all aware, adversaries fluctuate their infrastructure over time and only by enumerating their tactics, techniques and procedures (TTPs) can we learn to recognize them in the wild. To discover new infrastructure and to track the changes and movement of an adversary over time, defenders need to learn to craft effective composites.


To accomplish this, we need to ask ourselves as defenders where the threat actor’s sphere of influence in infrastructure lies. The internet is a hierarchy, and different adversaries are able to influence different portions of that hierarchy. Any change to a piece in that stack shows a likely human intervention. These changes to mutables are the core constructs of what makes an effective hunting query, but first we have to understand over what part of the internet’s hierarchy our adversary commands influence.


As a note, these examples will be strictly vendor-agnostic as effective data sets for your organization will be highly dependent on your operational environment. Choosing the data sets that expose this information to you in an indexed and searchable manner is an important part of building out a cyber-threat intelligence (CTI) program.


A Phishing Kit
--------------


As an example, we can take a low-level phishing kit running on a shared hosting provider. The phish kit deployer could change service providers at any time, so to track the kit’s movement you would want a data set that relies heavily on searchability of on-page content.


With this data set you could look at headers provided, redirects used, loading order of objects and components in the DOM to find distinct mutables, to build a composite object for confirming this is the same actor using this kit. Perhaps something along the lines of:


● Login form contains a hidden field named “aff-id” with an alphanumeric string.  

● Page content was cloned from a CDN and sources cloned content on www4.phishedcompany.com instead of a load-balanced endpoint.  

● 404 page of the kit contains an odd phrasing.  

● On form submittal, the kit redirects you through a URL shortener link.


This content provides a solid fingerprint that any service that crawls websites could pick out and identify as this phish kit and, due to the “aff-id” field, the possibility to narrow down to a specific operator. While in the past a registrant name of “Mr. Phisher” might provide pivot points as malicious names were registered, this composite query provides a more accurate if slightly more difficult signature of activity. Indeed, in the past even adversaries with good operational security practices would already be using names like “John Smith” to provide far too many pivot points.


**A Ransomware C2**
-------------------


For an additional example we can take a ransomware command-and-control (C2) server. The affiliates behind most ransomware-as-a-service (RaaS) offerings have a decent modicum of operational security that would render registrant-based details useless to begin with, but once again every mutable bit of information on the network is able to be used as an indicator in building a composite fingerprint for tracking an actor.


In the case of a C2 we would most often be looking at a virtual private server (VPS) provider on a cloud service like Amazon’s AWS or Microsoft’s Azure. Users of those services almost never have a choice of the IP address they are assigned, so the controllable space for the attacker starts there. Since most C2 communication is encrypted and also won’t respond without a configured key, we also have a point where further down the hierarchy, at the content level, we lose any effective indicators to build a good composite query on unless we have samples of the malware to analyze. Perhaps in this case we could then be building a composite along the lines of:


● Use of XYZ or TOP TLDs.  

● Domain names always contain 14 characters.  

● Let’s Encrypt TLS certificate.  

● NS record points to same IP address as the server.  

● MX record active and verified to use Google services to send email.


On their own, each of these items is largely irrelevant. Hundreds of domains are registered each day within those TLDs and several dozen with that set of characters. New Let’s Encrypt certificates are generated by the thousands and it’s not uncommon for a domain to have a NS or MX record. However, once combined this composite hunting query will narrow down a result set far enough that defenders can easily discover new C2 infrastructure coming online.


**Conclusion**
--------------


Composite objects form the linchpin of effective hunting queries in a world where adversary operational security has become increasingly capable and privacy redaction has rendered many quick win registration details useless. Seemingly disparate pieces of infrastructure information, combined with knowledge of the adversary’s sphere of influence on infrastructure, can form perfect fingerprints for tracking new components in their toolset. While many components of these queries may be across varied data sets and vendors, an effective CTI program can make use of a wide range of open source and enterprise solutions to combine them for a more effective hunting strategy.


***Chad Anderson is senior security researcher for DomainTools.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[C2]] [[WHOIS]] [[IP]] [[ThreatPost]]
