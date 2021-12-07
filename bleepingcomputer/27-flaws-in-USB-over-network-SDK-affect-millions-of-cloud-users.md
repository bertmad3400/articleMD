# 27 flaws in USB-over-network SDK affect millions of cloud users
### Researchers have discovered 27 vulnerabilities in Eltima SDK, a library used by numerous cloud providers to remotely mount a local USB device.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/27-flaws-in-usb-over-network-sdk-affect-millions-of-cloud-users/
+ Date: 2021-12-07T10:15:44-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/07/dark_cloud.jpg)

![dark_cloud](https://www.bleepstatic.com/content/hl-images/2021/12/07/dark_cloud.jpg?rand=2101855918)


Researchers have discovered 27 vulnerabilities in Eltima SDK, a library used by numerous cloud providers to remotely mount a local USB device.


Due to the pandemic and the rising trend of working from home, organizations have begun to rely heavily on cloud-based services. This necessity also increased cloud providers utilizing Eltima's SDK that allow employees to mount local USB mass storage devices for use on their cloud-based virtual desktops.



![USB over Ethernet](https://www.bleepstatic.com/images/news/u/1220909/Security/connecting_USB_via_ethernet.jpg)**USB over Ethernet**  
*Source: Eltima*
However, as cloud desktop providers, including Amazon Workspaces, rely on tools like Eltima, SentinelOne warned that millions of users worldwide have become exposed to the discovered vulnerabilities.


The implications of exploiting the flaws are significant as they could allow remote threat actors to gain elevated access on a cloud desktop to run code in kernel mode.


"These vulnerabilities allow attackers to escalate privileges enabling them to disable security products, overwrite system components, corrupt the operating system, or perform malicious operations unimpeded," explained a new report by [Sentinel Labs](https://www.sentinelone.com/labs/usb-over-ethernet-multiple-privilege-escalation-vulnerabilities-in-aws-and-other-major-cloud-services/).


This elevated access could allow malware to steal credentials that threat actors can use to breach an organization's internal network.


In total, there are 27 vulnerabilities discovered by SentinelOne, with the CVE IDs listed below:



```
CVE-2021-42972, CVE-2021-42973, CVE-2021-42976, CVE-2021-42977, CVE-2021-42979, CVE-2021-42980, CVE-2021-42983, CVE-2021-42986, CVE-2021-42987, CVE-2021-42988, CVE-2021-42990, CVE-2021-42993, CVE-2021-42994, CVE-2021-42996, CVE-2021-43000, CVE-2021-43002, CVE-2021-43003, CVE-2021-43006, CVE-2021-43637, CVE-2021-43638, CVE-2021-42681, CVE-2021-42682, CVE-2021-42683, CVE-2021-42685, CVE-2021-42686, CVE-2021-42687, CVE-2021-42688
```

These vulnerabilities have been responsibly disclosed to Eltima, who has already released fixes for affected versions. However, it is now up to cloud services to upgrade their software to utilize the updated Eltima SDK.


According to SentinelOne, the affected software and cloud platforms are:


* Amazon Nimble Studio AMI, before 2021/07/29
* Amazon NICE DCV, below: 2021.1.7744 (Windows), 2021.1.3560 (Linux), 2021.1.3590 (Mac), 2021/07/30
* Amazon WorkSpaces agent, below: v1.0.1.1537, 2021/07/31
* Amazon AppStream client version below: 1.1.304, 2021/08/02
* NoMachine [all products for Windows], above v4.0.346 below v.7.7.4 (v.6.x is being updated as well)
* Accops HyWorks Client for Windows: version v3.2.8.180 or older
* Accops HyWorks DVM Tools for Windows: version 3.3.1.102 or lower (Part of Accops HyWorks product earlier than v3.3 R3)
* Eltima USB Network Gate below 9.2.2420 above 7.0.1370
* Amzetta zPortal Windows zClient
* Amzetta zPortal DVM Tools
* FlexiHub below 5.2.14094 (latest) above 3.3.11481
* Donglify below 1.7.14110 (latest) above 1.0.12309

It is important to note that Sentinel Labs hasn’t looked into all possible products that could incorporate the vulnerable Eltima SDK, so there could be more products affected by the set of flaws.


Also, some services are vulnerable on the client-side, others on the server-side, and a few on both, depending on code-sharing policies.


Defending against these vulnerabilities
---------------------------------------


Sentinel Labs clarifies that it has seen no evidence that threat actors have exploited these vulnerabilities. Still, now that a technical report has been released, we will likely see exploitation in the future.


Out of an abundance of caution, admins should revoke privileged credentials before applying the security updates, and logs should be scrutinized for signs of suspicious activity. 


Most vendors have patched the flaws and pushed them through automatic updates. However, some require end-user action to apply the security updates, like upgrading the client app to the latest available version.


Below is a list of fixes released by different vendors:


* Amazon – Released fixes to all regions on June 25, 2021
* Eltima – Released fixes on September 6, 2021
* [Accops](https://blogs.accops.com/responsible-disclosure-security-vulnerability-in-accops-usb-redirection-driver/) – Released fixes on September 5, 2021, and notified customers to upgrade. Additionally, released utility to detect vulnerable endpoints on December 4, 2021
* Mechdyne – Has not responded to the researchers yet
* Amzetta – Released fixes on September 3, 2021
* [NoMachine](https://knowledgebase.nomachine.com/SU10S00227) – Released fixes on October 21, 2021





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Eltima]] [[Cloud]] [[Sdk]] [[Usb]] [[Accops]] [[Sentinelone]] [[Hyworks]] [[Windows]] [[Amzetta]] [[Bleeping Computer]]
#### ipv4-adresses
3.3.1.102
#### CVE's
[[CVE-2021-42972]] [[CVE-2021-42973]] [[CVE-2021-42976]] [[CVE-2021-42977]] [[CVE-2021-42979]] [[CVE-2021-42980]] [[CVE-2021-42983]] [[CVE-2021-42986]] [[CVE-2021-42987]] [[CVE-2021-42988]] [[CVE-2021-42990]] [[CVE-2021-42993]] [[CVE-2021-42994]] [[CVE-2021-42996]] [[CVE-2021-43000]] [[CVE-2021-43002]] [[CVE-2021-43003]] [[CVE-2021-43006]] [[CVE-2021-43637]] [[CVE-2021-43638]] [[CVE-2021-42681]] [[CVE-2021-42682]] [[CVE-2021-42683]] [[CVE-2021-42685]] [[CVE-2021-42686]] [[CVE-2021-42687]] [[CVE-2021-42688]]

