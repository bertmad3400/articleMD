# AT&T Takes Steps to Mitigate Botnet Found Inside Its Network 
### AT&T is battling a modular malware called EwDoor on 5,700 VoIP servers, but it could have a larger wildcard certificate problem.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176711)
+ Date: December 2, 2021  12:35 pm
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/02121237/att-logo-e1638465174609.png)
AT&T is taking action to take down a botnet that had set up shop inside its network, infecting 5,700 VoIP servers that route traffic from enterprise customers to upstream mobile providers.


Researchers from Netlab, a network security division of Chinese tech giant Qihoo 360, first discovered what they characterized as a “brand-new botnet” attacking Edgewater Networks devices, using a vulnerability in [EdgeMarc Enterprise Session Border Controllers](https://ribboncommunications.com/products/service-provider-products/cloud-and-edge/session-border-controllers/session-border-controllers-edge-appliances), tracked as [CVE-2017-6079](https://nvd.nist.gov/vuln/detail/CVE-2017-6079). Attackers had accessed vulnerable servers to install a modular malware strain that researchers dubbed “EwDoor,” researchers disclosed in [a report](https://blog.netlab.360.com/warning-ewdoor-botnet-is-attacking-att-customers/) published earlier this week.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The flaw that attackers exploited is a hidden page in the EdgeMarc appliance that allows for user-defined commands such as specific iptables routes, etc., to be set. An attacker can use the page as a web shell to execute commands; however, the client side of the web application is not affected by the flaw.


Netlab eventually identified the devices as belonging to AT&T, which confirmed the existence of the botnet to analyst firm Recorded Future’s The Record.


“Based on the [fact that the] attacked devices are telephone-communication related, we presume that [the botnet’s] main purpose is [distributed denial of service] DDoS attacks, and gathering of sensitive information, such as call logs,” Netlab researchers wrote.


AT&T said it is taking “steps to mitigate” the botnet, and so far the company has not found evidence that it has been weaponized, according to [the report](https://therecord.media/att-takes-action-against-ddos-botnet-that-hijacked-voip-servers/) published on The Record Wednesday.


“We have no evidence that customer data was accessed,” AT&T said in an email, according to the report.


**Tracking a Botnet**
---------------------


Netlab researchers observed EwDoor undergoing four updates between Oct. 27 and Nov. 20 as they tracked the behavior of the botnet. The current version of the malware includes six major functions: Self-updating, port scanning, file management, DDoS attack, reverse shell and arbitrary command execution, they said.


Despite the size of the botnet, EwDoor’s functionality is fairly straightforward, researchers said. After installation on an infected device, it collects device information, then performs a few common tasks such as establishing persistence and other functions.


After this, the malware decrypts a tracker and obtains command-and-control (C2) by accessing the tracker, then finally reports the collected device information to C&C and executes its commands.


One interesting aspect of the botnet and the servers that have been commandeered by attackers is that researchers found that there were about 100,000 IPs using the same SSL certificate. SSL certificates act as identities for devices and are used to validate who is connecting to them and if they are connecting to the right system*.*


“We are not sure how many devices corresponding to these IPs could be infected, but we can speculate that as they belong to the same class of devices the possible impact is real,” researchers wrote.


**Wildcard SSL Certificates?**
------------------------------


Indeed, the discovery of so many IPs using the same certificates could signal that AT&T has a more systemic problem within its network that allowed for the creation of the botnet and could pave the way for other attacks, noted one security professional.


“Using the same SSL certificate for multiple devices is roughly similar to people making copies of the passport, which has only the family name and the whole extended family using the same passport,” noted Murali Palanisamy, chief solutions officer for AppViewX, in an email to Threatpost. “It also typically suggests that the default certificate is not replaced or updated.”


Certificates like this are called wildcard certificates, he said, and they expose devices to “application-layer protocols allowing cross-protocol attacks” (ALPACA), something that the [NSA warned about recently](https://www.itsecuritynews.info/nsa-warns-of-risks-posed-by-wildcard-certificates-alpaca-attacks/).


“One of the easiest ways to identify or fingerprint an application with default credentials is to check for default or same certificates across multiple devices,” Palanisamy explained. “This means either the device is not fully secured or configured with all the best practices.”


If this is the case, AT&T will have to “urgently take action” to secure any server or device exposed to an outside network to ensure that no one is accessing the network by exploiting unencrypted ports, he explained.


“The organization will also have to reimage and secure thousands of devices and look at the exposure they have and the back doors they have set up or accessed,” Palanisamy added.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://bit.ly/3bBMX30)***for the LIVE event!***




#### Tags:
[[AT&T]] [[botnet]] [[SSL]] [[malware]] [[Netlab]] [[ThreatPost]]
