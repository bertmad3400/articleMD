# Fortinet fixes bug letting unauthenticated hackers run code as root
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/fortinet-fixes-bug-letting-unauthenticated-hackers-run-code-as-root/)
+ Date: July 20, 2021
+ Author: Ionut Ilascu


## Article:
![CVE-2021-32589 bug in FortiManager and FortiAnalyzer enables remote code execution without authentication](https://www.bleepstatic.com/content/hl-images/2021/04/02/Fortinet.jpg)


Fortinet has released updates for its FortiManager and FortiAnalyzer network management solutions to fix a serious vulnerability that could be exploited to execute arbitrary code with the highest privileges.


Both FortiManager and FortiAnalyzer are enterprise-grade network management solutions for environments with up to 100,000 devices. They are available as a physical appliance, as a virtual machine, in the cloud, or hosted by Fortinet.



Organizations can use the products to manage deploy and configure devices on the network as well as to collect and analyze the generated logs to identify and eliminate threats.


### Patch and workaround available


Fortinet has published a [security advisory](https://www.fortiguard.com/psirt/FG-IR-21-067) for the issue, which is currently tracked as CVE-2021-32589, saying that it is a use-after-free (UAF) vulnerability in FortiManager and FortiAnalyzer fgfmsd daemon.


This type of bug occurs when a section of memory is erroneously marked as free and a program then tries to use it, resulting in a crash.


However, Fortinet says that sending a specially crafted request to the “FGFM” port of a target device “may allow a remote, non-authenticated attacker to execute unauthorized code as root.”


The company highlights that FGFM is disabled by default on FortiAnalyzer and can be turned on only on some hardware models: 1000D, 1000E, 2000E, 3000D, 3000E, 3000F, 3500E, 3500F, 3700F, 3900E.


The products affected by [CVE-2021-32589](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32589) are the following:


If updating is not possible, one workaround is to disable FortiManager features on the FortiAnalyzer unit using the following command:


Credited for finding and responsibly reporting the vulnerability to Fortinet is Cyrille Chatras, a reverse engineer and pentester from Orange group that previously discovered and reported bugs in products from Nokia, Juniper, Red Hat, and in open-source Android [[1](http://www.nokia.com/notices/responsible-disclosure/), [2](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11146&actp=METADATA), [3](https://access.redhat.com/security/cve/cve-2018-7550), [4](https://source.android.com/security/overview/acknowledgements)].


CISA has also [published an advisory](https://us-cert.cisa.gov/ncas/current-activity/2021/07/19/fortinet-releases-security-updates-fortimanager-and-fortianalyzer) encouraging users and administrators to review the vulnerability information from Fortinet and apply the updates.




#### Tags:
[[Fortinet]] [[FortiAnalyzer]] [[FortiManager]] [[Bleeping Computer]]
