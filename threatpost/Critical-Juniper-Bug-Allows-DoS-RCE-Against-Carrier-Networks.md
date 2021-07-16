# Critical Juniper Bug Allows DoS, RCE Against Carrier Networks
### Telecom providers, including wireless carriers, are at risk of disruption of network service if the bug in SBR Carrier is exploited.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167869)
+ Date: July 16, 2021  1:17 pm
+ Author: Tara Seals


## Article:
A critical remote code-execution vulnerability in Juniper Networks’ Steel-Belted Radius (SBR) Carrier Edition lays open wireless carrier and fixed operator networks to tampering.


The SBR Carrier server is used by telecom carriers to manage policies for how subscribers access their networks – by centralizing user authentication, delivering the appropriate level of access and ensuring compliance with security policies. It allows carriers to offer differentiated levels of service, multiply their revenue models and manage network resources.


The bug ([CVE-2021-0276](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11180&cat=SIRT_1&actp=LIST)) affects SBR Carrier versions 8.4.1, 8.5.0 and 8.6.0 that use extensible authentication protocol. Juniper issued a patch on Wednesday. It rates 9.8 out of 10 on the CVSS vulnerability-severity rating scale.



It’s a stack-based buffer-overflow vulnerability that an attacker can exploit by sending specially crafted packets to the platform, causing the [RADIUS daemon](https://en.wikipedia.org/wiki/RADIUS) to crash, according to Juniper’s advisory. This can result in RCE, and also denial-of-service (DoS) that would prevent phone subscribers from having a network connection.


The bug is just one of many that the networking giant patched [this week](https://kb.juniper.net/InfoCenter/index?page=content&channel=SECURITY_ADVISORIES&cat=SIRT_1&actp=&sort=datemodified&dir=descending&max=1000&batch=15&rss=true&itData.offset=0) across its carrier and enterprise product lines, including several high-severity bugs that could be exploited to carry out DoS attacks.


A Second RCE/DoS Bug
--------------------


One of these can also be used for RCE, Juniper said. That bug ([CVE-2021-0277](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11181&cat=SIRT_1&actp=LIST), with an 8.8 CVSS rating) is an out-of-bounds read vulnerability afflicting Junos OS (versions 12.3, 15.1, 17.3, 17.4, 18.1, 18.2, 18.3, 18.4, 19.1, 19.2, 19.3, 19.4, 20.1, 20.2, 20.3 and 20.4), and Junos OS Evolved (all versions).


Junos OS and Junos OS Evolved are network operating systems that power Juniper’s enterprise routers and switches. The former runs on FreeBSD, while the latter runs a version of Linux.


The issue exists in the processing of specially crafted LLDP frames by the Layer 2 Control Protocol Daemon (l2cpd). LLDP is the protocol that network devices use to broadcast their identity, capabilities and neighbors on a local area network (usually over wired Ethernet).


“Continued receipt and processing of these frames, sent from the local broadcast domain, will repeatedly crash the l2cpd process and sustain the DoS condition,” Juniper said in its advisory, issued Thursday.


In addition to the patch, this bug has a few workarounds. For instance, users can configure a device to not load the l2cpd daemon. However, if it’s disabled, certain protocols (RSTP, MSTP, VSTP, ERP, xSTP and ERP, among others) won’t work.


A second option is to configure target interfaces on the device to disable LLDP packet processing Or, for most switching platforms, it’s possible to implement packet filters via a firewall to discard LLDP packets with an EtherType of 0x88cc, according to the advisory.


Lastly, to reduce the risk of exploitation, users can implement off-system intrusion-detection systems and/or firewall filtering methods. These include “disallowing LLDP EtherType to propagate completely on local segments, or by filtering broadcast addressed LLDP packets or unicast addressed LLDP packets not originated from trusted sources targeted to trusted destinations,” the vendor explained.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[LLDP]] [[3]] [[Junos]] [[SBR]] [[RCE]] [[1]] [[l2cpd]] [[ThreatPost]]
