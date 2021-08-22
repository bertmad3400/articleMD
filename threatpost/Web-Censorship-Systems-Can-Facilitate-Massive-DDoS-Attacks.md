# Web Censorship Systems Can Facilitate Massive DDoS Attacks
### Systems are ripe for abuse by attackers who can abuse systems to launch DDoS attacks. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168853)
+ Date: August 20, 2021  5:11 pm
+ Author: Tom Spring


## Article:
Researchers are warning internet censorship systems are ripe for abuse by a new type of distributed denial of service (DDoS) attack. The potential for abuse is concerning, researchers say, because attacks would take advantage of a type of reflection and amplification, which would be “extremely detrimental to any network” if carried out.


Netscout, which detailed the attack vector, dubbed the type of DDoS attack a Middlebox HTTP Reflection/Amplification (MBHTTP) misconfiguration vulnerability. They say attacks can produce DDoS volumes as high as a 700,000 to 1 amplification factor.


The type of attack is a HTTP Reflection/Amplification, meaning an attacker can both magnify the amount of malicious traffic they generate while obscuring the sources of the attack traffic. An HTTP-based DDoS attack sends junk HTTP requests to a target’s server tying up resources and locking out users from using a particular site or service.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Along with the risk of systems leveraged in massive DDoS attacks the censorship systems themselves would also be crippled, with traffic analysis tools knocked offline and permitted traffic blocked, according to researchers.


Tens of Millions of Devices Exposed
-----------------------------------


Netscout credits a joint team of researchers from the University of Maryland and the University of Colorado Boulder for [identifying the widespread configuration vulnerability](https://ieeexplore.ieee.org/document/9474303/). Netscout estimates that 200 million IP addresses can potentially be abused to launch attacks of this kind.


“Tens of millions of these devices are exposed and vulnerable to abuse from adversaries and approximately 18 million of these provide at least a 2:1 amplification factor, resulting in one of the most prolific types of reflectors/amplifiers available to adversaries,” wrote Roland Dobbins and Steinthor Bjarnason in [a technical analysis posted Friday](https://www.netscout.com/blog/asert/http-reflectionamplification-abusable-internet-censorship).


**Why Censorship Systems?**
---------------------------


Affected censorship systems, researchers found, are particularly susceptible to these type attacks because of three factors write researchers:


Netscout says many censorship systems are “suboptimal” in design and “implementation decisions allow spoofed requests for denied FQDNs and/or URIs to be synthesized by attackers in much the same way as other well-known reflection/amplification DDoS vectors.” This, they say results in amplified HTTP responses being directed towards the intended targets of the attack.


**Systems Open to Attack Because of Misconfiguration**
------------------------------------------------------


At the heart of the vulnerability is a common misconfiguration of censorship systems that responds to HTML block notification pages from Uniform Resource Identifiers (URI) in a specific way.


“[A] lack of enforcement regarding TCP three-way handshakes, ensure that attackers can spoof the IP addresses of their targets, selecting both the source and destination ports of their choice, in order to launch high-pps/-bps HTTP reflection/amplification attacks,” researchers wrote.


Attackers can easily cloak attacks as well.


“Skilled attackers are likely to choose source and destination ports intended to allow the amplified attack traffic to conform to common network access control policies, thus masquerading the attack traffic so that at first glance, it appears to be legitimate in the context of targeted applications, services, and infrastructure,” wrote Dobbins and Bjarnason.


**Mitigation Risk: The Recommendations**
----------------------------------------


Netscout recommends that network operators identify abuse-able censorship systems and remove them.


“The security researchers who discovered this attack methodology have published a bespoke fork of the [ZMap scanning software](https://ieeexplore.ieee.org/document/9474303/), along with an accompanying module, which can be used to identify abusable systems,” researchers wrote.


“Nationwide internet censorship threatens free and open access to communication and information for millions of users living inside of censoring regimes… We show that this poses an even greater threat to the internet than previously understood,” wrote researchers from the University of Maryland and the University of Colorado Boulder.




#### Tags:
[[DDoS]] [[HTTP]] [[Netscout]] [[ThreatPost]]
