# CISA: BadAlloc impacts critical infrastructure using BlackBerry QNX
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/cisa-badalloc-impacts-critical-infrastructure-using-blackberry-qnx/)
+ Date: August 17, 2021
+ Author: Sergiu Gatlan


## Article:
![CISA: BadAlloc impacts critical infrastructure using BlackBerry QNX](https://www.bleepstatic.com/content/hl-images/2021/04/08/CISA.jpg)


CISA today warned that IoT and OT security flaws known as BadAlloc impact BlackBerry's QNX Real Time Operating System (RTOS) used by critical infrastructure organizations


[BadAlloc](https://www.bleepingcomputer.com/news/security/microsoft-finds-critical-code-execution-bugs-in-iot-ot-devices/) is a collection of 25 vulnerabilities are caused by memory allocation [Integer Overflow or Wraparound](https://cwe.mitre.org/data/definitions/190.html) bugs.


They were found by Microsoft researchers in standard memory allocation functions widely used in multiple real-time operating systems (RTOS), C standard library (libc) implementations, and embedded software development kits (SDKs).


Vulnerable IoT and OT devices directly affected by the BadAlloc flaws can be found on a large assortment of consumer, medical, and industrial networks.


BlackBerry QNX powers critical infrastructure systems
-----------------------------------------------------


[BlackBerry QNX's](https://blackberry.qnx.com/en/company/about-qnx) tech is used worldwide by over 195 million vehicles and embedded systems across a wide range of industries, including aerospace and defense, heavy machinery, rail, robotics, industrial controls, automotive, commercial vehicles, and medical.


Remote attackers could exploit devices running older versions of BlackBerry QNX products unpatched against BadAlloc to trigger denial-of-service conditions or execute arbitrary code on vulnerable QNX-based systems.


"BlackBerry QNX RTOS is used in a wide range of products whose compromise could result in a malicious actor gaining control of highly sensitive systems, increasing risk to the Nation’s critical functions," CISA [warned](https://us-cert.cisa.gov/ncas/alerts/aa21-229a).


"CISA strongly encourages critical infrastructure organizations and other organization developing, maintaining, supporting, or using affected QNX-based systems, to patch affected products as quickly as possible."


The US Food and Drug Administration (FDA) also [issued a separate warning](https://content.govdelivery.com/accounts/USFDA/bulletins/2ecf9d4) today alerting patients, health care providers, and manufacturers about the increased risk introduced by these vulnerabilities for medical devices incorporating vulnerable BlackBerry QNX software.


At the moment, CISA, the FDA, and BlackBerry are not aware of any exploitation of this vulnerability in the wild.


Mitigation recommendations
--------------------------


The warnings come after BlackBerry [disclosed earlier today](https://support.blackberry.com/kb/articleDetail?articleNumber=000082334) that BadAlloc (tracked as CVE-2021-22156) also impacts QNX Software Development Platform (SDP), QNX OS for Medical, and QNX OS for Safety.




The company also advises all affected QNX SDP, QNX OS for Safety, and QNX OS for Medical customers to update their QNX products as soon as possible using the following links (access to downloads requires a myQNX account):


* 6.5.0SP1 <https://www.qnx.com/download/feature.html?programid=59649>
* QNX OS for Safety 1.0.2 <https://www.qnx.com/download/group.html?programid=27165>
* QNX OS for Medical 1.1.1 <https://www.qnx.com/download/group.html?programid=26463>


If updating to a fixed release is not immediately possible, BlackBerry recommends ensuring that only ports and protocols used by RTOS apps are accessible, blocking all others, to mitigate the vulnerabilities


* where possible, ensure that their systems only connect to trusted isolated networks
* avoid exposing unnecessary interfaces (e.g., telnet, ftp, qconn, etc)
* locate system networks and remote devices behind firewalls and isolate them from the business network


CISA also urged strongly critical infrastructure organizations developing, maintaining, supporting, or using affected QNX-based systems to patch them ASAP.


The federal agency provides mitigation advice for potentially affected entities:


* **Manufacturers** of products that incorporate vulnerable versions should contact BlackBerry to obtain the patch.
* **Manufacturers of products who develop unique versions of RTOS software** should contact BlackBerry to obtain the patch code. **Note:** in some cases, manufacturers may need to develop and test their own software patches.
* **End users** of safety-critical systems should contact the manufacturer of their product to obtain a patch. If a patch is available, users should apply the patch as soon as possible. If a patch is not available, users should apply the manufacturer's recommended mitigation measures until the patch can be applied.




#### Tags:
[[QNX]] [[BadAlloc]] [[CISA]] [[QNX-based]] [[RTOS]] [[Bleeping Computer]]
