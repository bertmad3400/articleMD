# Defending the Supply Chain: Why the DDS Protocol is Critical in Industrial and Software Systems
### In 2021, a team of researchers from Trend Micro Research, TXOne, ADLINK, Alias Robotics, and ZDI  looked into the Data Distribution Service (DDS) standard and its implementations from a security angle. The full findings of this research will be presented in the S4X22 Conference in April 2022.

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/22/a/defending-the-supply-chain-why-dds-is-critical-in-industrial-and-software-systems.html
+ Date: 2022-01-27
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-the-supply-chain-why-the-dds-protocol-is-critical-in-industrial-and-software-systems/cover-2-defending-the-supply-chain-why-DDS-critical-industrial-software-industry.jpg)





***By Federico Maggi, Erik Boasson, Mars Cheng, Patrick Kuo, Chizuru Toyama, Víctor Mayoral Vilches, Rainer Vosseler, and Ta-Lun Yen***






![top-bar-decorative-context-DDS-critical-supply-chain](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-the-supply-chain-why-the-dds-protocol-is-critical-in-industrial-and-software-systems/top-bar-DDS-defending-the-supply-chain-critical-industrial-software-industry.jpg)





If there existed a prize for the most pervasive, critical, and least-known middleware technology, the Data Distribution Service ([DDS](https://www.omg.org/spec/DDS-SECURITY/1.1/PDF)) standard would certainly win it. When we first presented the results of this research at the [Black Hat Europe Briefings](https://www.blackhat.com/eu-21/briefings/schedule/index.html#the-data-distribution-service-dds-protocol-is-critical-lets-use-it-securely-24934), the audience appeared to be completely unaware (embarrassed, even) that the DDS drives railways, autonomous cars, airports, spacecrafts, diagnostic imaging machines, luggage handling, industrial robots, military tanks, and frigates for about a decade, with its adoption increasing steadily.


Given this technology's ubiquity, we decided to investigate further and discovered multiple security vulnerabilities, resulting in [13 new CVE IDs](https://www.cisa.gov/uscert/ics/advisories/icsa-21-315-02) for the six [most common DDS implementations](https://www.omg.org/dds-directory/vendor/list.htm). This includes one vulnerability in the standard specifications and other deployment issues in the DDS software ecosystem (including a fully open production system). These vulnerabilities have been patched or mitigated by the vendors since we reported them.






![figure1-defending-the-supply-chain-DDS-industrial-software](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-the-supply-chain-why-the-dds-protocol-is-critical-in-industrial-and-software-systems/fig1-DDS-defending-the-supply-chain-critical-industrial-software-industry.png)
Figure 1. We found exposed DDS systems in 34 countries, including vulnerable ones, identified via distinct IPs leaking data




By measuring the exposure of DDS services, in one month we found 643 distinct public-facing DDS services in 34 countries affecting 100 organizations via 89 internet service providers (ISPs). Of the DDS implementations by seven distinct vendors (one of which we were initially unaware of), 202 leaked private IP addresses (referring to internal network architecture details), and seven supposedly secret URLs. Some of these IP addresses expose unpatched or outdated DDS implementations, which are affected by some of the vulnerabilities that we’ve discovered and disclosed in November.


This research is from the collaboration of [Trend Micro Research](https://www.trendmicro.com/vinfo/us/security/research-and-analysis/) and [TXOne Networks](https://www.txone-networks.com/) (Federico Maggi, Mars Cheng, Patrick Kuo, Chizuru Toyama, Rainer Vosseler, and Ta-Lun Yen), [ADLINK Labs](https://www.adlinktech.com/en/Verification_Validation_Lab) (with Erik Boasson, one of the inventors and core developers of DDS), Alias Robotics (with Víctor Mayoral Vilches, Robotics Architect), and Trend Micro Zero Day Initiative ([ZDI](https://www.zerodayinitiative.com/)). We analyzed the specifications of DDS and the six implementations maintained by certified vendors with millions of deployments globally. During our research, we interviewed key DDS users and system integrators to collect their feedback on our findings and the importance of DDS for innovation in their respective sectors.


As a critical piece of technology that receives little attention and considering our findings, we encourage other researchers, DDS users, and implementors to promote security awareness about DDS and its ecosystem. Successful exploitation of these vulnerabilities in any of the critical sectors where DDS is used can have consequences, such as (including nomenclature referring to the ATT&CK ICS framework):


* loss of control ([T0827](https://collaborate.mitre.org/attackics/index.php/Technique/T0827))
* loss of safety ([T0880](https://collaborate.mitre.org/attackics/index.php/Technique/T0880))
* denial of service ([DoS](https://www.trendmicro.com/vinfo/us/security/definition/denial-of-service-dos), [T0814](https://collaborate.mitre.org/attackics/index.php/Technique/T0814)) via brute forcing ([T0806](https://collaborate.mitre.org/attackics/index.php/Technique/T0806))
* facilitate initial access ([TA0108](https://collaborate.mitre.org/attackics/index.php/Initial_Access)) via exploitation of remote services ([T0866](https://collaborate.mitre.org/attackics/index.php/Technique/T0866), [T0886](https://collaborate.mitre.org/attackics/index.php/Technique/T0886)) or supply chain compromise ([T0862](https://collaborate.mitre.org/attackics/index.php/Technique/T0862))
* allow attackers to perform discovery ([TA0102](https://collaborate.mitre.org/attackics/index.php/Discovery), [T0856](https://collaborate.mitre.org/attackics/index.php/Technique/T0856)) by abusing the discovery protocol
* abuse the protocol itself to create an efficient command and control channel ([T0869](https://collaborate.mitre.org/attackics/index.php/Technique/T0869))


According to our analysis, we recommend mitigations such as:


* vulnerability scanning ([M1016](https://attack.mitre.org/mitigations/M1016/))
* network intrusion prevention ([M1031](https://attack.mitre.org/mitigations/M1031/))
* network segmentation ([M1030](https://attack.mitre.org/mitigations/M1030/))
* filter network traffic ([M1037](https://attack.mitre.org/mitigations/M1037/))
* execution prevention ([M1038](https://attack.mitre.org/mitigations/M1038/))
* auditing ([M1047](https://attack.mitre.org/mitigations/M1047/))


Our findings apply worldwide and affect billions of devices across every vertical, including all critical applications such as [autonomous driving](https://www.rti.com/blog/2016/02/24/dds-proof-points-for-autonomous-cars/),[intelligent public transportation](https://www.adlinktech.com/en/ProRail), telecommunications, cloud, [healthcare](https://www.rti.com/ge2015dec), [consumer and industrial robotics](https://design.ros2.org/articles/ros_middleware_interface.html), and [defense systems](https://info.rti.com/hubfs/Datasheets/RTI_Datasheet_20002_Aerospace-Defense_V11_Web_0718.pdf).


Based on our findings and a demonstration of their impact to the DDS’s key sectors, we advocate for the continuous security testing of DDS and other related critical technology. We also provide actionable recommendations to use for a secure DDS integration. To help raise awareness on the importance of DDS security, we provide two examples showing how an attacker can amplify network traffic, leading to real-time and determinism issues or cause an autonomous vehicle to lose control and collide against objects when implemented without the proper security measures.


Given that DDS is little known yet quite ubiquitous, we encourage subject-matter experts to reuse our proofs of concept to raise awareness and help decision-makers allocate proper resources in securing current and future DDS deployments.











 


What is DDS and why is it critical?


DDS is a machine-to-machine technology used for publish-subscribe middleware applications in real-time** and embedded systems. This standard is maintained by the Object Management Group ([OMG](https://www.omg.org/)) and is used in all classes of critical applications to implement reliable communication layers between sensors, controllers, and actuators.


For example, when the artificial intelligence (AI) of an autonomous car needs to issue a “turn left” command, DDS is used to transport that command from the electronic control unit (ECU) (the car’s “brain”) down to the steering servomotors. The same instance also happens when speed sensors send information from the motor up to the ECU. We verified that the DDS runs successfully on [starter kit ECUs](https://www.renesas.com/us/en/products/automotive-products/automotive-system-chips-socs/r-car-h3-m3-starter-kit), making any autonomous vehicle based on this hardware and software stack susceptible to our findings.


Another example is when an airport operator inside the air traffic control tower needs to illuminate the runway of an airport. In modern airports, these [specific signals](https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap2_section_1.html) are transmitted via software, and DDS is used to ensure timely delivery of those commands. The average airport runway has thousands of control points: considering there are [more than 10,000](https://euflightcompensation.com/how-many-airports-are-there-in-the-world/) (expected to become 44,000) airports in the world, each with an [average of 2.5 runways](https://en.wikipedia.org/w/index.php?title=Runway&oldid=1057372302) (up to 36), even if only 1% of them would be using DDS (conservatively), this would make roughly 250,000 DDS nodes (up to 1.1M) in airports alone.


As seen in Figure 1, DDS is at the very beginning of the software supply chain, making it easy to lose track of. Because of this, DDS is attractive to attack or compromise for the resulting impact. Between 2020 and 2021, [66% of attacks](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2021) in the software industry targeted suppliers’ software. During our research, we encountered an exposed source-code repository hosting a proprietary implementation of DDS, which would have let an attacker infect the source code ([T0873](https://collaborate.mitre.org/attackics/index.php/Technique/T0873), [T0839](https://collaborate.mitre.org/attackics/index.php/Technique/T0839)).






![figure2-DDS-defending-the-supply-chain-critical-software-industrial](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-the-supply-chain-why-the-dds-protocol-is-critical-in-industrial-and-software-systems/figure3-DDS-defending-the-supply-chain-why-critical-industrial-software-industry.png)
Figure 2. DDS is a standardized software library used for software-based controlled systems, directly or via ROS 2




Autonomous driving, air-traffic control, cloud and virtualization, and connected healthcare are only some of the many applications of DDS technology.Notably, DDS is used by some of these agencies and organizations:


* National Aeronautics and Space Administration (NASA) at the [Kennedy Space Center](https://www.omgwiki.org/ddsf/doku.php?id=ddsf:public:applications:aerospace_and_defense:nasa_launch_and_control_systems)
* Siemens AG in [wind power plants](https://www.rti.com/news/siemens-wind-power)
* Volkswagen and Bosch for [autonomous valet parking systems](https://www.traficom.fi/sites/default/files/media/publication/TRA2020-Book-of-Abstract-Traficom-research-publication.pdf)
* Nav Canada and European ATM Performance CoFlight for [air-traffic control](https://www.airport-technology.com/uncategorised/newsnav-canada-improves-air-traffic-management-rti-platform)


DDS is the foundation of other industry standards including Open field Message Bus ([OpenFMB](https://openfmb.ucaiug.org/)) used for [smart-grid applications](https://github.com/rticommunity/openfmb-dds-demo), [Adaptive AUTOSAR](https://www.rti.com/blog/fresh-approach-to-enabling-flexible-vehicle-architectures), Medical Device Plug-and-Play ([MD PnP](https://mdpnp.org/MD_PnP_Program___OpenICE.html)) Interoperability Program, Generic Vehicle Architecture ([GVA](https://www.slideshare.net/RealTimeInnovations/generic-vehicle-architecture-dds-at-the-core)), and NATO GVA ([NGVA](https://www.omgwiki.org/ddsf/doku.php?id=ddsf:public:guidebook:03_user:07_gva#nato_generic_vehicle_architecture_components)). The Robot Operating System 2 (ROS 2), which is the de-facto standard operating system (OS) for robots and automation, has DDS as the default middleware. Notably, NASA’s recent [Space ROS](https://sam.gov/opp/eec121cac3bb483e93f04ce38714ed64/view) initiative will bring ROS 2 to space. DDS is also used for system-virtualization and cloud-computing applications, mainly to exchange data across machines and data centers.


***We acknowledge that “real-time” is used in a generic and non-strict (hard real-time) manner in DDS specifications. No actual discussion of the timing guarantees (hard real-time, firm real-time, or soft real-time) is provided in any of the reviewed documents, thereby we conclude that DDS targets remote, soft real-time communications at best, leaving firm and hard real-time interactions to other technologies.*


A vulnerability in the standard’s specifications


Like any other engineering product, DDS also has vulnerabilities in its code base and ecosystem (for example, development tools, cloud back-ends, Docker images, and integration libraries). One peculiar finding is an amplification vulnerability ([CVE-2021-38487](https://vuldb.com/?id.186691), [CVE-2021-38429](https://vuldb.com/?id.186687)) that lets a malicious actor trigger network-flooding attacks by spoofing a single DDS discovery packet. When compromised, this leads to service malfunction and breaking real-time properties of communication. Interestingly, this amplification vulnerability is evident just by reading the DDS standard specifications, which do not mandate proper checks that would avoid the corner cases that an attacker could exploit. We verified that the same exploit works unmodified against multiple products, confirming that it's not just an implementation-specific issue.






![figure4-defending-the-supply-chain-why-DDS-critical-industrial-software-industry](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-the-supply-chain-why-the-dds-protocol-is-critical-in-industrial-and-software-systems/fig4-DDS-defending-the-supply-chain-critical-industry-software.png)
Figure 3. By spoofing the participant locator, any participant can pretend to be anyone else, and the receiver is forced (following the specification requirement) to answer back until a valid acknowledgement is received




DDS development environment exposed to the internet


While monitoring for exposed continuous-integration/continuous-deployment (CI/CD) systems via Shodan, we found that one DDS developer left their custom CI/CD environment fully exposed to the internet with default credentials. Despite our numerous attempts to contact this vendor, including through vulnerability brokers and Computer Emergency Readiness Teams (CERTs), we received no response. Fortunately, the exposed system was properly locked down after a few months.


Left open, this could have let a malicious actor wipe, steal, or trojanize their most valuable intellectual property — the source code.






![figure4-defending-the-supply-chain-DDS-industrial-software-industry](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-the-supply-chain-why-the-dds-protocol-is-critical-in-industrial-and-software-systems/fig5-DDS-defending-the-supply-chain-critical-industry-software.jpg)
Figure 4. An exposed continuous integration system used by a DDS developer, with default access credentials in plaintext




What are the possible consequences?


An attacker armed with working exploits for these vulnerabilities could disrupt a target device’s normal operation through network DoS, move laterally, or (in some cases) control a machine. Since DDS is used in mission-critical applications, even a simple DoS capability can be used as a leverage for powerful extortion-based attacks, as we observed throughout 2020 and 2021. We found 643 unique IPs that expose DDS endpoints. Considering that DDS is supposed to only be deployed in a local network, 643 is a significant number. Moreover, some of these endpoints leak information about internal network structure such as private IPs.


For those endpoints’ characteristics and data, we were able to hypothesize the DDS product version that runs behind it. We can say all but four of them are vulnerable to at least one of our CVEs (compare the CVE table with the version column).


The network-reflection vulnerability affects both the specifications and most of the implementations. Eclipse CycloneDDS and GurumDDS are not affected, meaning that they have built-in mitigation measures (although they are still susceptible to reflection attacks). In addition, most of the implementations are affected by at least one vulnerability. The possibility of exploitation (T1210) may vary depending on the runtime environment. Notably, protections like stack canaries or address space layout randomization (ASLR), which are normally available in traditional endpoints, are not always implemented in embedded systems. 






![table1-defending-supply-chain-why-DDS-critical-industrial-software-industry](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/defending-the-supply-chain-why-the-dds-protocol-is-critical-in-industrial-and-software-systems/table1-DDS-defending-the-supply-chain-critical-industry-software.jpg)
Table 1. Summary of the vulnerabilities found and with assigned CVEs across the main DDS implementations and standard specification.




We listed just some of the results of compromise and attacks should these DDS vulnerabilities be left unsecured, along with the corresponding MITRE ATT&CK ICS taxonomy, such as loss of control (T0827), loss of safety (T0880), and denial of service (T0814) via brute forcing (T0806). In addition, some implementations are affected by stack- or heap-based overflow vulnerabilities, which can be exploited to facilitate initial access (TA0108) via exploitation of remote services (T0866, T0886). In any case, given that three popular DDS distributions are open source, supply-chain compromise (T0862) is also a viable scenario. By writing an automated network scanner, we demonstrate that it is possible for an attacker to perform automated discovery (TA0102, T0856) by abusing the built-in discovery protocol, or even to abuse the protocol itself to create an efficient command and control channel (T0869).


Remediation: Beyond patching


In the short term, we recommend mitigations such as periodic vulnerability scanning (M1016) to detect the presence of unpatched services, and the deployment of network intrusion prevention (M1031), network segmentation (M1030), and filtering of network traffic (M1037) to detect spoofed DDS messages and prevent the exploitation of the reflection vulnerability. We also recommend measures for execution prevention (M1038) to reduce the exploitation of memory errors, and periodic auditing (M1047).


When dealing with the security of critical software in the supply chain such as DDS, the most pressing need is to make the code base more amenable to the integration of automated security-testing tools. Taking fuzz-testing as a representative example. We advocate that all critical software libraries such as DDS should be developed with a strong orientation to security testing in addition to traditional unit testing. The situation has improved immensely thanks to initiatives such as [OSS-Fuzz](https://github.com/google/oss-fuzz), but there's still a significant gap between security engineers and software engineers. This results in tedious manual code reviews, unwanted modifications in the code to integrate security checks, and so on, delaying the wide scale adoption of available security tools.


The positive and engaging response to our disclosure by ADLINK, which went to the point of assisting Trend Micro researchers in creating [good fuzz targets](https://github.com/eclipse-cyclonedds/cyclonedds/tree/master/fuzz) against their own code base, should serve as an example to the entire software-engineering industry. Hopefully, this can serve as a role model to the entire software industry. 


Trend Micro solutions


[Trend Micro™ TXOne™ Networks](https://www.txone-networks.com/) [EdgeIPS Pro™](/en_us/business/products/iot/industrial-network-security/edge-ips-pro.html), [EdgeIPS™](/en_us/business/products/iot/industrial-network-security/edge-ips.html), and [EdgeFire™](https://www.txone-networks.com/products/portfolio/edgefire) customers are protected under this rule:


* 1137699 ICS DDS RTPS-mode Amplification Attack (CVE-2021-38429)








## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Healthcare]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.continent.name=Europe]] [[victim.city.name=Riga]] [[victim.country.name=Latvia]] [[victim.continent.name=Europe]] [[victim.country.name=Canada]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Dds]] [[Real-time]] [[Middleware]] [[Ics]] [[Cloud]] [[Trend Micro]]
#### CVE's
[[CVE-2021-38487]] [[CVE-2021-38429]]

