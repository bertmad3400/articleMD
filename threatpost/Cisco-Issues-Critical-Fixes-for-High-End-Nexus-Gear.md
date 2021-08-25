# Cisco Issues Critical Fixes for High-End Nexus Gear
### Networking giant issues two critical patches and six high-severity patches. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168939)
+ Date: August 25, 2021  6:48 pm
+ Author: Tom Spring


## Article:
![cisco patch DCNM](https://media.threatpost.com/wp-content/uploads/sites/103/2020/07/30102437/cisco-patch.png)
Cisco Systems released six security patches tied to its high-end 9000 series networking gear ranging in importance from critical, high and medium severity.


The most serious of the bugs patched by Cisco (rated 9.1 out of 10) could allow a remote and unauthenticated adversary to read or write arbitrary files on to an application protocol interface used in Cisco 9000 series switches designed to manage its software-defined networking data center solution.


This critical vulnerability, tracked as [CVE-2021-1577](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-capic-frw-Nt3RYxR2), impacts Cisco Application Policy Infrastructure Controller (APIC) and Cisco Cloud Application Policy Infrastructure Controller (Cloud APIC). APIC is the main architectural component of the Cisco Application Centric Infrastructure, which runs on Cisco Nexus 9000 Series node.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“This vulnerability is due to improper access control. An attacker could exploit this vulnerability by using a specific API endpoint to upload a file to an affected device,” wrote Cisco in its Wednesday security bulletin. Affected products are Cisco APIC and Cisco Cloud APIC.


As with each of the bugs and fixes announced Wednesday, Cisco said mitigations are available for each of the vulnerabilities and it is not aware of any publicly known exploits for those bugs patched. The release Wednesday, which included 15 patches in all, were part of a Cisco “bundled publication” of security fixes for its Firepower eXtensible Operating System and is Linux kernel compatible NX-OS software.


**A Nexus of Bug Fixes**
------------------------


Cisco also addressed two high-severity Nexus 9000 bugs ([CVE-2021-1586](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9kaci-tcp-dos-YXukt6gM), [CVE-2021-1523](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9kaci-queue-wedge-cLDDEfKF)) and three medium-severity flaw ([CVE-2021-1583](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-naci-afr-UtjfO2D7), [CVE-2021-1584](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-naci-mdvul-vrKVgNU), [CVE-2021-1591](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nexus-acl-vrvQYPVe)). The two high-severity bugs (both with a base CVSS score of 8.6) are denial of service flaws.


“A vulnerability in the Multi-Pod or Multi-Site network configurations for Cisco Nexus 9000 Series Fabric Switches in Application Centric Infrastructure (ACI) mode could allow an unauthenticated, remote attacker to unexpectedly restart the device, resulting in a denial of service (DoS) condition,” wrote Cisco.


A second high-severity Nexus 9000 series vulnerability is described by Cisco as a flaw in its Fabric Switches ACI Mode Queue Wedge.


“[The flaw] could allow an unauthenticated, remote attacker to cause a queue wedge on a leaf switch, which could result in critical control plane traffic to the device being dropped. This could result in one or more leaf switches being removed from the fabric,” Cisco noted.


Cisco notes that mitigation for this bug requires “a manual intervention to power-cycle the device to recover” after patches have been applied. Affected are generation 1 model N9K (Nexus 9000) series fabric switches.


Critical QNX ‘BadAlloc’ Bugs – Nothing to See Here
--------------------------------------------------


On Wednesday, Cisco released a second critical advisory for its gear tied to a QNX operating system bug, [reported on August 17](https://threatpost.com/blackberrys-qnx-devices-attacks/168772/) by BlackBerry. That bug, according to BlackBerry, could allow threat actors to take over or launch denial of service attacks on devices and critical infrastructure by exploiting what are called BadAlloc bugs. QNX is BlackBerry’s real-time OS, used in embedded systems such as automobiles, medical devices and handsets.


While Cisco says none of its products are impacted by the QNX bug, it has rated the its advisory as critical. “Cisco has completed its investigation into its product line to determine which products may be affected by this vulnerability. No products are known to be affected,” [it wrote](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-qnx-TOxjVPdL).


The Cisco advisory outlines switch and router products that “leverage the affected QNX software”, however “Cisco has confirmed that the vulnerability is not exploitable on these platforms.”


Cisco products running QNX include:


 




#### Tags:
[[QNX]] [[Wednesday,]] [[high-severity]] [[bug,]] [[ThreatPost]]
