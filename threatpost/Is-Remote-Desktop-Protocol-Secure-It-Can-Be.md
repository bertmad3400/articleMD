# Is Remote Desktop Protocol Secure? It Can Be
### Matt Dunn, associate managing director in Kroll’s Cyber Risk practice, discusses options for securing RDP, which differ significantly in terms of effectiveness.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167719)
+ Date: July 13, 2021  10:50 am
+ Author: Matt Dunn


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/13103737/RDP-e1626187071361.jpg)
Most of the problems with setting up Remote Desktop Protocol (RDP) for remote work involves making RDP accessible via the public internet. RDP itself is not a secure setup and therefore requires additional security measures to keep workstations and servers protected. Without proper security protocols in place, organizations face several potential risks, including the increased risk of cyberattacks. The typical targets of these attacks tend to be small businesses because they often lack the resources needed to protect against and respond to these threats.


Cybercriminals have taken notice of the increased adoption of RDP and are taking advantage of the vulnerabilities that accompany these exposed servers. Between Q1 and Q4 2020, [attacks against RDP surged by 768 percent](https://www.infosecurity-magazine.com/news/remote-desktop-protocol-attacks/). A [report](https://www.kroll.com/en/insights/publications/cyber/ransomware-attack-trends-2020) published by Kroll in October identified that 47 percent of ransomware attacks were preceded by RDP compromise.


Threat actors looking for RDP servers to exploit also have no trouble doing so. Shodan, a search engine designed to scan for devices with certain ports or protocols exposed to the internet, has found over 4 million RDP ports exposed, and at least 14,000 Windows RDP servers that are reachable from the internet.


In many cases, servers with RDP publicly accessible to the internet have failed to enable multi-factor authentication (MFA). This means that an attacker who compromises a user account by exposing a weak or reused password through a brute force attack can easily gain access to a user’s workstation via RDP.


With this initial compromise, the attacker will likely be able to gain full access to an organization’s exposed network. This can occur because these types of accounts are managed at the domain level by a centralized system, meaning that the same credentials are used for all systems.


Exploitation of these vulnerabilities only involves determining account credentials to access a system, and therefore, even the most unsophisticated attackers have the ability to exploit RDP. Even though the attack itself does not require much skill, the impact can be quite significant. These attacks can compromise an organization’s server and result in the potential loss of remote access service.


Why Cyber Threat Actors Exploit RDP
-----------------------------------


RDP vulnerabilities are a popular, common exploit among cybercriminals for a number of different reasons. Some of the most common objectives of an RDP attack are distributed denial of service (DDoS) attacks and ransomware delivery.


In a distributed denial-of-service (DDoS) attack, the goal is to send as much data as possible to a target website or server in order to overwhelm it and knock it offline. DDoS attackers use a variety of different methods for accomplishing this, such as large botnets or a technique called DDoS amplification, which takes advantage of a service that sends a much larger response than the initial request. DDoS attackers will send traffic to these services while masquerading as their target. The target website or server is then flooded with much more data than the attacker sends.


RDP servers are [potential DDoS amplifiers](https://www.zdnet.com/article/windows-rdp-servers-are-being-abused-to-amplify-ddos-attacks) with an amplification factor of 85.9. Therefore, attackers can abuse these services to send massive amounts of traffic to their targets, knocking them offline. The growing threat against RDP makes it vital for organizations to install anti-DDoS protections on their Internet-facing systems.


The growing use of RDP during the COVID-19 pandemic made it the [most common delivery mechanism for ransomware](https://www.zdnet.com/article/top-exploits-used-by-ransomware-gangs-are-vpn-bugs-but-rdp-still-reigns-supreme/) in 2020. After using RDP to gain access to an organization’s network, ransomware operators are then able to explore the network and plant ransomware on high-value systems. Additionally, some threat actors have augmented their ransomware tactics by exfiltrating sensitive data prior to encrypting a victim’s files and then extorting the victim by threatening to post the data on “shaming sites” if the ransom demands are not met.


The ease of exploiting ransomware has inspired some ransomware gangs to use it almost exclusively as an attack vector.


Options for Securing RDP
------------------------


RDP is a significant risk to an organization’s security. Several different options exist for securing RDP, which differ significantly in terms of effectiveness and usability.


One potential solution for protecting RDP against attack is limiting access to RDP solutions.  This could be accomplished by implementing access control lists (ACLs) that only permit RDP connections from specific IP addresses.


While this could work in theory, in practice, it is not a good solution for many reasons, including:


Virtual private networks (VPNs) are a commonly used remote-access solution. They are designed to provide an encrypted tunnel for network traffic between a remote user and the enterprise network. VPNs also support security solutions like MFA that help to mitigate the threat of compromised accounts.


However, while VPNs are a commonly used solution and a defense-in-depth security measure, [they have vulnerabilities](https://threatpost.com/hacked-data-limevpn-dark-web/167492/) and are often targeted by cyber threat actors attempting to deploy malware. VPN users must recognize their inherent weaknesses and upload security patch upgrades when provided.


This means that deploying VPN infrastructure may create additional vulnerabilities in an organization’s network. In fact, VPN vulnerabilities [are among the most commonly exploited](https://www.darkreading.com/perimeter/attackers-heavily-targeting-vpn-vulnerabilities-/d/d-id/1340770) by cyber-threat actors and are close behind RDP as ransomware delivery vectors.


The problem with IP-based ACLs and VPNs is that they focus on securing the initial access point to an organization’s network. A better approach to secure remote work considers both the route in and the systems that an employee or attacker can access remotely.


The best solution for securing RDP is to couple it with a virtual desktop solution—such as Citrix or VMware Horizons—that uses single sign-on for user authentication. With a virtual desktop solution, an organization can implement MFA to control access and have better visibility and control over remotely accessible endpoints and the data that they store, process and transmit. This increased visibility and control helps to prevent lateral movement of threats within the network and makes it easier to implement secure remote access.


Conclusion
----------


Organizations that are using RDP have the potential for a lot of vulnerabilities or opportunities available for exploitation by bad actors. It’s wise to consider a dedicated remote work security assessment can help to identify security gaps in your network and provides tips and tricks to strengthen the security of your network.


***Matt Dunn is associate managing director in Kroll’s Cyber Risk practice.***


***Enjoy additional insights from Threatpost’s InfoSec Insider community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[RDP]] [[ransomware]] [[DDoS]] [[VPNs]] [[MFA]] [[VPN]] [[ThreatPost]]
