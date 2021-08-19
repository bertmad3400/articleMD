# Hackers can bypass Cisco security products in data theft attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/hackers-can-bypass-cisco-security-products-in-data-theft-attacks/)
+ Date: August 19, 2021
+ Author: Sergiu Gatlan


## Article:
![Hackers can bypass Cisco security products in data theft attacks](https://www.bleepstatic.com/content/hl-images/2021/02/03/Cisco.jpg)


Cisco said that unauthenticated attackers could bypass TLS inspection filtering tech in multiple products to exfiltrate data from previously compromised servers inside customers' networks.


In such attacks, the threat actors can exploit a vulnerability in the Server Name Identification (SNI) request filtering impacting 3000 Series Industrial Security Appliances (ISAs), Firepower Threat Defense (FTD), and Web Security Appliance (WSA) products.


"Using SNIcat or a similar tool, a remote attacker can exfiltrate data in an SSL client hello packet because the return server hello packet from a server on the blocked list is not filtered," Cisco [explained](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sni-data-exfil-mFgzXqLN).


"This communication can be used to execute a command-and-control attack on a compromised host or perform additional data exfiltration attacks."


So far, the Cisco Product Security Incident Response Team (PSIRT) is not aware of attackers or malware exploiting this security flaw in the wild.


Stealthy data exfiltration by abusing TLS
-----------------------------------------


SNIcat (Server Name Indication Concatenator) is a [stealthy exfiltration method discovered by mnemonic Labs](https://www.mnemonic.no/blog/introducing-snicat/) security researchers that bypasses security perimeter solutions and TLS inspection devices (e.g., web proxies, next-gen firewalls (NGFW) via TLS Client Hello packets.


"By using our exfiltration method SNIcat, we found that we can bypass a security solution performing TLS inspection, even when the Command & Control (C2) domain we use is blocked by common reputation and threat prevention features built into the security solutions themselves," the reearchers said.


"In short, we found that solutions designed to protect users, introduced them to a new vulnerability."



![SNIcat](https://www.bleepstatic.com/images/news/u/1109292/2021/SNIcat.jpg)Image: mnemonic Labs
Besides Cisco, mnemonic Labs have successfully tested SNIcat against products from [F5 Networks](https://support.f5.com/csp/article/K20105555) (F5 BIG-IP running TMOS 14.1.2, with SSL Orchestrator 5.5.8), [Palo Alto Networks](https://security.paloaltonetworks.com/CVE-2020-2035) (Palo Alto NGFW running PAN-OS 9.1.1), and Fortinet (Fortigate NGFW running FortiOS 6.2.3).


The researchers also developed a [proof of concept tool](https://www.mnemonic.no/blog/introducing-snicat/) that helps extract data from previously hacked servers via an SNI covert channel, using an agent on the compromised host and a command-and-control server that gathers the exfiltrated data.


"Cisco is investigating its product line to determine which products may be affected by this vulnerability," Cisco added.


"As the investigation progresses, Cisco will update this advisory with information about affected products."




#### Tags:
[[TLS]] [[SNIcat]] [[Bleeping Computer]]
