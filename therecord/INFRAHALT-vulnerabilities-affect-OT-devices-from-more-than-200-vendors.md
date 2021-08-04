# INFRA:HALT vulnerabilities affect OT devices from more than 200 vendors
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/infrahalt-vulnerabilities-affect-ot-devices-from-more-than-200-vendors/)
+ Date: August 4, 2021
+ Author: Catalin Cimpanu


## Article:
![INFRA:HALT vulnerabilities affect OT devices from more than 200 vendors](https://therecord.media/wp-content/uploads/2021/08/IOT-board-circuit.jpg)

* Forescout and JFrog researchers disclose INFRA:HALT vulnerabilities in the NicheStack TCP/IP library.
* The library is believed to have been used in OT and industrial devices from more than 200 vendors.
* More than 6,400 vulnerable devices are currently connected online.


Security researchers have disclosed today 14 vulnerabilities that impact a popular TCP/IP library commonly used in industrial equipment and Operational Technology (OT) devices manufactured by more than 200 vendors.


Collectively referred to as **INFRA:HALT**, the 14 vulnerabilities have been found as part of a joint research effort by the security teams at Forescout and JFrog.


#### Project Memoria, phase III


According to a [report](https://www.forescout.com/research-labs/infra-halt/) published today, the vulnerabilities affect [NicheStack](https://www.st.com/en/embedded-software/hcc-nichestack.html), a small C library provided by HCC Embedded that can be added to a device’s firmware and allow it to support internet connectivity and other networking functions.


Also known as a “TCP/IP stack,” these types of libraries are common in almost all devices; however, their code has hardly been reviewed in decades for security flaws.


In 2019, after the discovery of the [URGENT/11](https://www.armis.com/urgent11/) and [Ripple20](https://www.jsof-tech.com/disclosures/ripple20/) vulnerabilities impacting common TCP/IP stacks, the Forescout team launched [Project Memoria](https://www.forescout.com/research-labs/project-memoria/) as a dedicated research operation to look into the security of all of today’s most popular TCP/IP stacks.


The INFRA:HALT bugs announced today are the project’s third set of bugs after [Amnesia:33](https://www.forescout.com/research-labs/amnesia33/) and [NUMBER:JACK](https://www.forescout.com/blog/numberjack-forescout-research-labs-finds-nine-isn-generation-vulnerabilities-affecting-tcpip-stacks/).


But while the previous two research efforts focused on more common TCP/IP stacks used with routers, IoT devices, or web servers, this time around, the Forescout and JFrog teams had their sights on a library used for adding internet connectivity to industrial equipment typically found in factories, mines, pipelines, water treatment facilities, and other critical infrastructure working points.


“The new vulnerabilities allow for remote code execution, denial of service, information leak, TCP spoofing, or DNS cache poisoning,” researchers explained.


A full list of the bugs, along with descriptions, is available below:


![InfraHalt-list](https://therecord.media/wp-content/uploads/2021/08/InfraHalt-list.png)Image: Forescout
#### More than 6,400 OT devices are exposed online


To exploit any of the INFRA:HALT vulnerabilities, a threat actor would first need to gain access to a company’s internal network and not just its office network but its OT section, a separate network where all industrial equipment is recommended to be installed.


However, while the bulk of companies typically know how to safeguard their OT networks, this doesn’t mean that some don’t intentionally or accidentally expose industrial equipment online.


Around 6,400 OT devices were found connected to the internet in March this year when the Forescout and JFrog teams discovered the INFRA:HALT vulnerabilities.


![InfraHalt-Shodan](https://www-therecord.recfut.com/wp-content/uploads/2021/08/InfraHalt-Shodan.png)Image: Forescout
These devices are now vulnerable to attacks, and especially to attacks exploiting the CVE-2020-25928 and CVE-2021-31226 bugs that could allow attackers to take full control over a device remotely.





The good news for the more than 200 device vendors that use NicheStack is that HCC Embedded has [prepared patches](https://www.hcc-embedded.com/support/security-advisories) to address all issues.


The bad news is that by the time these patches make it into a firmware update and then the firmware is deployed on devices in the field, threat actors could have already exploited the INFRA:HALT issues to damage devices or even hinder OT operations.


Companies interested in finding if they use devices that run on the NicheStack TCP/IP stack, or other TCP/IP stacks previously identified as vulnerable in earlier research, can use Forescout’s Project Amnesia scanner, [available on GitHub](https://github.com/Forescout/project-memoria-detector).





#### Tags:
[[Forescout]] [[TCP/IP]] [[INFRA:HALT]] [[JFrog]] [[NicheStack]] [[teams]] [[The Record]]
