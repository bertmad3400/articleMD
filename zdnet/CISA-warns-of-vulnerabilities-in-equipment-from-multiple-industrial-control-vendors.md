# CISA warns of vulnerabilities in equipment from multiple industrial control vendors
### In the advisory, CISA said the issues were found in equipment from Eclipse, eProsima, GurumNetworks, Object Computing, Inc. (OCI), Real-Time Innovations (RTI) and TwinOaks Computing.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/cisa-warns-of-vulnerabilities-in-multiple-industrial-control-products/)
+ Date: November 12, 2021
+ Author: Jonathan Greig


## Article:
Unknown

CISA has [released](https://us-cert.cisa.gov/ncas/current-activity/2021/11/12/cisa-releases-advisory-vulnerabilities-multiple-data-distribution) a notice urging administrators to apply updates to a variety of industrial control systems after discovering vulnerabilities in multiple open-source and proprietary Object Management Group (OMG) Data-Distribution Service (DDS) implementations.

In the advisory, CISA said the issues were found in equipment from [Eclipse](https://projects.eclipse.org/projects/iot.cyclonedds), [eProsima](https://github.com/eProsima/Fast-DDS), GurumNetworks, [Object Computing, Inc. (OCI)](https://opendds.org/), [Real-Time Innovations (RTI)](https://support.rti.com/s/login/?ec=302&startURL=%2Fs%2F) and [TwinOaks Computing.](http://www.twinoakscomputing.com/coredx/download)

The equipment containing the vulnerabilities includes CycloneDDS, FastDDS, GurumDDS, OpenDDS, Connext DDS Professional, Connext DDS Secure, Connext DDS Micro and CoreDX DDS.

"Successful exploitation of these vulnerabilities could result in denial-of-service or buffer-overflow conditions, which may lead to remote code execution or information exposure," CISA [explained](https://us-cert.cisa.gov/ics/advisories/icsa-21-315-02).

They provided links to each company's patches or fixes for the issue but noted that GurumNetworks did not respond to their messages. CISA said organizations using GurumNetworks' tools should contact them directly. 

Dr. Dennis Hackney, head of industrial cybersecurity services development at ABS Group, told ZDNet that many industrial control system owners don't realize that their systems are full of open-source software, much like OpenDDS. 

"The reasons for this are multifaceted but often stem from the proprietary and tailored nature of each control system. OEMs and engineers develop solutions that are as functional as possible, and, without adding unnecessary costs. Be warned, by their very nature, ICS are open," Hackney explained. 






"They use connectivity called OPC which stands for Object Linking and Embedding (OLE) for Process Control, otherwise known as open process control specifications. Open refers to non-authenticated communication between computers and equipment. There are increasingly new authenticated models but that does not cover the majority of what are in operation today. The concern being, when there is a vulnerability in components like OpenDDS, there are limited options to control access and ensure quality of service due to the nature of ICS designs." 

OpenDDS vulnerabilities are a concern, he added, because these applications are based on a subscription model. 

The vulnerabilities are also concerning because they can be exploited remotely and have a low attack complexity, he said. 

"ICS owners might not know if they have these components installed in their systems and this causes a problem if the ICS OEMs and vendors do not release their uses of these vulnerable components. These vulnerabilities will result in loss of system availability and could result in loss of control (due to arbitrary code execution). 

Like CISA's notice, Hackney suggested affected organizations install the latest updates, isolate systems from business IT networks, utilize firewalls and secure remote access through VPNs. 

Other experts, like Netenrich principal threat hunter John Bambenek, explained that this advisory stood out because it impacts a wide variety of vendors and open-source solutions that address the data distribution layer of real-time systems. 

Typically a vulnerability only impacts specific products and the fact that all involved have released updates in a coordinated fashion shows that CISA is taking its role of protecting critical infrastructure and coordinating response between many organizations seriously, Bambenek said. 

"While CISA has said there are no known public exploits for these vulnerabilities, this announcement will certainly drive those attackers interested in attacking these systems to develop them quickly. Affected organizations should patch quickly while there is still time," Bambenek added. 





#### Tags:
[[CISA]] [[open-source]] [[Connext]] [[DDS]] [[ICS]] [[ZDNet]]
