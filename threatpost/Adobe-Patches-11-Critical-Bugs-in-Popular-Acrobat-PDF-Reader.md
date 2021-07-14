# Adobe Patches 11 Critical Bugs in Popular Acrobat PDF Reader
### Adobe July patch roundup includes fixes for its ubiquitous and free PDF reader Acrobat 2020 and other software such as Illustrator and Bridge.  

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167743)
+ Date: July 13, 2021  2:55 pm
+ Author: Tom Spring


## Article:
Eleven critical bugs in Adobe’s popular and free PDF reader, Acrobat, open both Window and macOS users to attacks ranging from an adversary arbitrarily executing commands on a targeted system to data leakage tied to system-read and memory flaws.


In a Tuesday security bulletin, [which included patches for all flaws](https://helpx.adobe.com/security.html/security/security-bulletin.ug.html), the company reported that Windows and macOS versions of Acrobat were equally vulnerable. Adobe added however that it was not aware of any abuse of the bugs in the wild.


The free Acrobat Reader 2020 and PDF-creation and editing software Acrobat 2020 were among the list of those programs with critical bugs patched. Adobe also patched Acrobat DC, Acrobat DC Reader, Acrobat Reader 2017 and Acrobat 2017. In all, Adobe patched 20 Acrobat bugs, with nine rated important.  

Two of the most serious Acrobat vulnerabilities are use-after-free flaws ([CVE-2021-28641, CVE-2021-28639](https://helpx.adobe.com/security/products/acrobat/apsb21-51.html)) that, in a worst case scenario, allow an adversary to execute code arbitrarily on targeted systems or just create application crashes.


One of the more interesting critical bugs patched is a type of vulnerability called an “uncontrolled search path element” flaw (CVE-2021-28636). The vulnerability class also goes by the names DLL preloading, insecure library loading and dependency confusion. It’s unclear how the weakness was introduced to Adobe Acrobat. The security bulletin links to a generic description of the flaw which states:


“The product uses a fixed or controlled search path to find resources, but one or more locations in that path can be under the control of unintended actors… In some cases, the attack can be conducted remotely, such as when SMB or WebDAV network shares are used,” according to a [MITRE description of the vulnerability](https://cwe.mitre.org/data/definitions/427.html) type.


**Adobe Illustrator and Bridge, Also Patched**
----------------------------------------------


Additional Adobe products were also part of the vendor’s roundup of fixes, Bridge, Framemaker Dimension and Illustrator.


Four [critical bugs](https://helpx.adobe.com/security/products/bridge/apsb21-53.html) in Adobe’s Bridge, a free app for managing digital assets, were patched. These include a heap-based buffer-overflow flaw (CVE-2021-28624), improper input-validation vulnerability (CVE-2021-35991) and two arbitrary code-execution bugs (CVE-2021-35989, CVE-2021-35990).


A heap-based buffer overflow allows for arbitrary code execution by an adversary causing either a program crash, infinite loop restart of a program or a type of denial-of-service attack based on CPU or memory overconsumption. Trend Micro Zero Day Initiative researcher Tran Van Khang is credited for identifying the bug.


One critical flaw ([CVE-2021-28596](https://helpx.adobe.com/security/products/framemaker/apsb21-45.html)) was reported, and patched, in Adobe’s Windows version of its high-end document processing software FrameMaker. This arbitrary code-execution bug is classified as an out-of-bounds write vulnerability, meaning an adversary could create an exploit that target’s a systems memory, where the malicious software writes data past the end, or before the beginning, of the intended memory buffer. This can either corrupt data, or crash a targeted system or allow a hacker to execute code on the targeted system.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[]] [[ThreatPost]]
