# Memory Bugs in BlackBerry’s QNX Embedded OS Open Devices to Attacks
### The once-dominant handset maker BlackBerry is busy squashing BadAlloc bugs in its QNX real-time operating system used in cars in medical devices. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168772)
+ Date: August 18, 2021  10:30 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/18102035/BlackBerry_Logo.jpg)
The potential danger from a raft of memory-allocation bugs discovered by Microsoft in April has now spread to older versions of multiple BlackBerry QNX products.


The Cybersecurity Infrastructure and Security Agency (CISA) and BlackBerry warned in separate alerts Tuesday that threat actors can take over or launch denial of service attacks on devices and critical infrastructure by exploiting what are called BadAlloc bugs tied to BlackBerry’s QNX operating system (OS).


QNX is a real-time OS, used in embedded systems such as automobiles, medical devices and handsets. BlackBerry acquired the OS in 2010 when it bought Quantum Software Systems. Industries and devices using the affected QNX OS include aerospace and defense, heavy machinery, rail, robotics, industrial controls and medical devices. BlackBerry boasted [in 2019](https://www.blackberry.com/us/en/company/newsroom/press-releases/2019/blackberry-qnx-software-now-embedded-in-more-than-150-million-vehicles)  QNX is embedded in the infotainment systems of 150 million vehicles ranging from Audi, Ford, Kia and Volkswagen.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


BadAlloc, tracked as [CVE-2021-22156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-22156), is the name Microsoft’s Section 52 research group [gave](https://msrc-blog.microsoft.com/2021/04/29/badalloc-memory-allocation-vulnerabilities-could-affect-wide-range-of-iot-and-ot-devices-in-industrial-medical-and-enterprise-networks/) to 25 critical memory-allocation vulnerabilities [discovered in April](https://threatpost.com/microsoft-warns-25-critical-iot-industrial-devices/165752/) that at the time were believed to affect myriad vendors’ IoT and industrial devices.


“BlackBerry QNX RTOS is used in a wide range of products whose compromise could result in a malicious actor gaining control of highly sensitive systems, increasing risk to the nation’s critical functions,” according to the [CISA’s advisory](https://us-cert.cisa.gov/ncas/alerts/aa21-229a).


CISA warned that all BlackBerry programs with dependency on the C runtime library are affected by the vulnerability. “Because many affected devices include safety-critical devices, exploitation of this vulnerability could result in a malicious actor gaining control of sensitive systems, possibly leading to increased risk of damage to infrastructure or critical functions,” the agency said.


BlackBerry put out a [security advisory](https://support.blackberry.com/kb/articleDetail?articleNumber=000082334) of its own on a BadAlloc-related integer overflow vulnerability in the *calloc()* function of the C runtime library in specific versions of the BlackBerry QNX. The company said the flaw affects the BlackBerry QNX Software Development Platform (SDP) version 6.5.0SP1 and earlier, QNX OS for Medical 1.1 and earlier, and QNX OS for Safety 1.0.1 and earlier.


So far there is no evidence of active exploitation of BadAlloc on BlackBerry QXN devices, both the company and the CISA added.


**Improper Input Validation**
-----------------------------


Memory allocation is exactly what it sounds like–the basic set of instructions device makers give a device for how to allocate memory. BadAlloc vulnerabilities stem from a systemic issue in which memory-allocation implementations written throughout the years as part of devices and embedded software did not incorporate proper input validation, according to Microsoft. Without these validations, attackers can exploit the memory allocation function to perform a heap overflow, resulting in execution of malicious code on a target device.


BadAlloc bugs are attributed specifically to the usage of vulnerable memory functions that exist across devices, such as *malloc, calloc, realloc, memalign, valloc, pvalloc* and more. What makes them so pervasive is that they can exist in various aspects of devices, including RTOS, embedded SDKs, and C standard libraries.


CISA and Blackberry strongly urged in separate documentation that all organizations whose devices use affected QNX-based systems immediately update to the latest version of the technology and apply mitigations.


BlackBerry [warned](https://support.blackberry.com/kb/articleDetail?articleNumber=000082334) that there are no known workarounds for the vulnerability on BlackBerry QNX SDP version 6.5.0SP1 and earlier, QNX OS for Medical 1.1 and earlier, and QNX OS for Safety 1.0.1. However, to avoid exploitation, system administrators can ensure that only ports and protocols used by the application using the RTOS are accessible by blocking all others, the company said.


BlackBerry also advised that administrators follow network segmentation, vulnerability scanning, and intrusion detection best practices appropriate for use of the QNX product in their cybersecurity environment “to prevent malicious or unauthorized access to vulnerable devices.”


CISA also [strongly encouraged](https://us-cert.cisa.gov/ncas/alerts/aa21-229a) that critical infrastructure organizations and other organizations developing, maintaining, supporting, or using affected QNX-based systems contact BlackBerry to obtain patches for their products.




#### Tags:
[[QNX]] [[BadAlloc]] [[CISA]] [[devices,]] [[earlier,]] [[memory-allocation]] [[ThreatPost]]
