# Feds Warn BlackMatter Ransomware Gang is Poised to Strike
### An advisory by the CISA, FBI and NSA reveals hallmark tactics of and shares defense tips against the cybercriminal group that’s picked up where its predecessor DarkSide left off.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175567)
+ Date: October 19, 2021  9:21 am
+ Author: Elizabeth Montalbano


## Article:
Federal authorities are warning businesses to shore up cybersecurity defenses as it carefully monitors the reemergence of the DarkSide ransomware gang, believed responsible for the [crippling Colonial Pipeline attack](https://threatpost.com/pipeline-biden-darkside-gas-bags/166112/) in May 2021.


The ransomware-as-a-service gang has regrouped under the moniker BlackMatter, according [to a joint advisory](https://us-cert.cisa.gov/ncas/alerts/aa21-291a) posted Monday by the Cybersecurity and Infrastructure Security Agency (CISA), FBI and the National Security Agency (NSA).


The advisory urges businesses to bolster defenses tied to user credentials and implement strong passwords and multi-factor authentication (MFA) to better thwart an anticipated uptick in BlackMatter criminal activity.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The [joint advisory](https://us-cert.cisa.gov/ncas/alerts/aa21-291a) also details what it believes are DarkSide tactics used by the BlackMatter group since they began tracking the revamped criminal organization in July 2021.


**Mitigations and Recommendations**
-----------------------------------


The advisory offers cyber defense tips and potential mitigations for attacks.


“Using embedded, previously compromised credentials, BlackMatter leverages the Lightweight Directory Access Protocol (LDAP) and Server Message Block (SMB) protocol to access the Active Directory (AD) to discover all hosts on the network,” according to the advisory. “BlackMatter then remotely encrypts the hosts and shared drives as they are found.”


Because of its tactic to use stolen credentials to breach networks, some of the primary mitigations for defending against BlackMatter attacks are related to how organizations handle user authentication and thus are practical fixes. The agencies recommend enforcing strong passwords and implementing MFA across networks to avoid allowing compromise with stolen credentials.


Using the detection signatures provided to identify BlackMatter activity on a network also can block placement of the group’s ransom note on the first share that is encrypted, “subsequently blocking additional SMB traffic from the encryptor system for 24 hours,” the agencies recommended.


Network-related mitigations such as limiting access to resources over the network and implementing network segmentation and traversal monitoring can prevent the group from leveraging persistence to access and encrypt more resources, according to the advisory.


The agencies recommended **removing unnecessary** **access to administrative shares****,** especially ADMIN$ and C$, and using **a host-based firewall** to only allow connections to administrative shares via SMB from a limited set of administrator machines.


Moreover, “adversaries use system and network discovery techniques for network and system visibility and mapping,” according to the advisory. “To limit an adversary from learning the organization’s enterprise environment, limit common system and network discovery techniques.”


Actions to support the latter include segmenting networks to prevent the spread of ransomware, and identifying, detecting and investigating abnormal activity and potential **traversal of the indicated ransomware with a networking monitoring tool****, according to the advisory.**


**DarkSide Revived**
--------------------


BlackMatter already has picked up where DarkSide left off when it closed down shop in May, with significant attacks against multiple U.S. critical infrastructure organizations, including two U.S. Food and Agriculture Sector cooperatives, according to the feds.


BlackMatter targeted Iowa-based farmer’s feed and grain cooperative [NEW Cooperative](https://www.newcoop.com/) in mid-September, and followed it up with [an attack](https://threatpost.com/crystal-valley-farm-coop-hit-with-ransomware/174928/) on Minnesota-based arm supply and grain marketing cooperative Crystal Valley cooperative in the same week. Earlier in the month, the group also targeted [Japanese tech giant Olympus](https://threatpost.com/blackmatter-ransomware-olympus/169423/) with a ransomware attack.


“Ransomware attacks against critical infrastructure entities could directly affect consumer access to critical infrastructure services,” according to the advisory. “BlackMatter actors have attacked numerous U.S.-based organizations and have demanded ransom payments ranging from $80,000 to $15,000,000 in Bitcoin and Monero.”


**Observed Tactics**
--------------------


Researchers used a [sample](https://www.virustotal.com/gui/file/706f3eec328e91ff7f66c8f0a2fb9b556325c153a329a2062dc85879c540839d) of BlackMatter ransomware and analyzed it in a sandbox environment to glean insight into how the group infiltrates targeted networks, according to the advisory. What they found is that the BlackMatter variant uses embedded admin or user credentials that were previously compromised and NtQuerySystemInformation and EnumServicesStatusExW to enumerate running processes and services, respectively.


“BlackMatter then uses the embedded credentials in the LDAP and SMB protocol to discover all hosts in the AD and the srvsvc.NetShareEnumAll Microsoft Remote Procedure Call (MSRPC) function to enumerate each host for accessible shares,” according to the advisory.


The observed variant also uses the embedded credentials and SMB protocol to remotely encrypt, from the original compromised host, all discovered shares’ contents, including ADMIN$, C$, SYSVOL, and NETLOGON, according to the feds.


Moreover, the threat actors use a separate encryption binary for Linux-based machines and also routinely encrypt ESXi virtual machines. “Rather than encrypting backup systems, BlackMatter actors wipe or reformat backup data stores and appliances,” according to the advisory.


The agencies also provide detection signatures for BlackMatter that organizations can use to see if the group has been active on their networks.




#### Tags:
[[BlackMatter]] [[advisory.]] [[DarkSide]] [[ransomware]] [[SMB]] [[mitigations]] [[“BlackMatter]] [[ThreatPost]]
