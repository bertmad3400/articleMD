# High-Severity Intel Processor Bug Exposes Encryption Keys
### CVE-2021-0146, arising from a debugging functionality with excessive privileges, allows attackers to read encrypted files.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176355)
+ Date: November 15, 2021  3:52 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/03/30084352/intel-building-logo.jpg)
A security vulnerability in Intel chips opens the door for encrypted file access and espionage, plus the ability to bypass copyright protection for digital content.


That’s according to Positive Technologies (PT), which found that the vulnerability (CVE-2021-0146) is a debugging functionality with excessive privileges, which is not protected as it should be.


The high-severity privilege-escalation issue is rated 7.1 out of 10 on the CVSS vulnerability-severity scale.


“[The] hardware allows activation of test or debug logic at runtime for some Intel processors which may allow an unauthenticated user to potentially enable escalation of privilege via physical access,” according to Intel’s advisory, [issued last week](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00528.html).


In terms of scope, the vulnerability affects the Pentium, Celeron and Atom processors of the Apollo Lake, Gemini Lake and Gemini Lake Refresh platforms. These chips power laptops, mobile devices, embedded systems, medical devices and a variety of internet of things (IoT) offerings.


“According to a study by Mordor Intelligence, Intel ranks fourth in the IoT chip market, while its Intel Atom E3900 series IoT processors, which also contain the CVE-2021-0146 vulnerability, are used by car manufacturers in more than 30 models, including, according to unofficial sources, in Tesla’s Model 3,” PT noted in a writeup shared with Threatpost.


To address the issue, users should install the [UEFI BIOS](https://threatpost.com/intel-security-holes-cpus-bluetooth-security/166747/) updates published by manufacturers of each piece of electronic equipment. The following processor models are affected:


**CVE-2021-0146 Impact for End Users**
--------------------------------------


When it comes to impact, an exploit would allow cybercriminals to extract a device’s encryption key and gain access to information.


“One example of a real threat is lost or stolen laptops that contain confidential information in encrypted form,” said Mark Ermolov, a PT researcher who was credited with discovering the bug (along with PT’s Dmitry Sklyarov and independent researcher Maxim Goryachy).


The vulnerability is also dangerous because it facilitates the extraction of the root encryption key used in Intel’s Platform Trust Technology and Enhanced Privacy ID technologies, which are used to protect digital content from illegal copying, Ermolov added


“For example, a number of Amazon e-book models use Intel EPID-based protection for digital rights management,” he explained. “Using this vulnerability, an intruder might extract the root EPID key from a device (e-book), and then, having compromised Intel EPID technology, download electronic materials from providers in file form, copy and distribute them.”


Additionally, an exploit could allow cyberattackers to conduct targeted attacks across the supply chain, Ermolov noted.


“For example, an employee of an Intel processor-based device supplier could extract the Intel CSME firmware key and deploy spyware that security software would not detect,” he said.


***Want to win back control of the flimsy passwords standing between your network and the next cyberattack? Join Darren James, head of internal IT at Specops, and Roger Grimes, data-driven defense evangelist at KnowBe4, to find out how during a free, LIVE Threatpost event,*** [***“Password Reset: Claiming Control of Credentials to Stop Attacks,”***](https://bit.ly/3bBMX30) ***on Wed., Nov. 17 at 2 p.m. ET. Sponsored by Specops.***


[***Register NOW***](https://bit.ly/3bBMX30)***for the LIVE event!***




#### Tags:
[[]] [[ThreatPost]]
