# Garrett walk-through metal detectors can be remotely manipulated
### Two widely used walk-through metal detectors made by Garrett are vulnerable to many remotely exploitable flaws that could severely impair their functionality, thus rendering security checkpoints deficient.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/garrett-walk-through-metal-detectors-can-be-remotely-manipulated/
+ Date: 2021-12-21T10:23:54-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/21/garret-metal-detectors.jpg)

![Garret metal detector](https://www.bleepstatic.com/content/hl-images/2021/12/21/garret-metal-detectors.jpg)


Two widely used walk-through metal detectors made by Garrett are vulnerable to many remotely exploitable flaws that could severely impair their functionality, thus rendering security checkpoints deficient.


Garrett is a well-known US-based manufacturer of hand-held and walk-through metal detectors commonly deployed in security-critical environments such as sports venues, airports, banks, museums, ministries, and courthouses. 


Security researchers at [Cisco Talos](https://blog.talosintelligence.com/2021/12/vuln-spotlight-garrett-metal-detector.html) have discovered numerous vulnerabilities that could allow attackers to execute commands or read/modify information on the Garret iC Module version 5.0, which is the component that provides network connectivity to Garrett PD 6500i and Garrett MZ 6100.


The nine vulnerabilities disclosed in detail by Cisco Talos are:


* CVE-2021-21901 and CVE-2021-21903 – Stack-based buffer overflow vulnerabilities enable an unauthenticated threat actor to exploit a buffer overflow condition using a specially-crafted packet. CVSS v3: 9.8 (critical)
* CVE-2021-21904 – A directory traversal flaw in iC Module enabling an actor to send a specially-crafted command-line argument can lead to an arbitrary file overwrite. CVSS v3 score: 9.1 (critical)
* CVE-2021-21905 and CVE-2021-21906 – Two stack-based buffer overflow flaws that can be triggered by uploading a malicious file on the target device and forcing the system to call ‘readfile’. CVSS v3: 8.2 (high)
* CVE-2021-21902 – Authentication bypass vulnerability in the CMA run\_server of the iC Module, enabling a threat actor to launch a properly-timed network connection through a sequence of requests, leading to session hijacking. CVSS v3 score: 7.5 (high)
* CVE-2021-21908 and CVE-2021-21909 – Directory traversal flaws, allowing a threat actor to delete files on the target device by sending specially-crafted command line arguments. CVSS v3 score: 6.0 (medium)
* CVE-2021-21907 – A directory traversal vulnerability leading to local file inclusion via a specially-crafted command-line argument. CVSS v3 score: 4.9 (medium)

In CVE-2021-21901 and CVE-2021-21903, the iC Module exposes a discovery service on UDP port 6977. This opens up an exploitation path by broadcasting a specially-formatted UDP packet, forcing a reply with sensitive information.


Using this info, an attacker could craft a UDP packet with a sufficiently long CRC field leading to a buffer overflow, allowing remote code execution before any authentication.



![Crash indicating the exploitation of CVE-2021-21901](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/buffer_overflow.jpg)**Crash indicating the exploitation of CVE-2021-21901**  
*Source: Cisco Talos*
In CVE-2021-21904, the iC Module exposes an authenticated CLI over TCP port 6877. After a client authenticates, they are allowed to send plain-text commands to the device, and one of the potential commands is the creation of new “environment variables.”


These variables are underpinned by a key parameter, which is not sanitized or validated. As such, it can lead to unauthenticated arbitrary file creation and code execution as the root user.



![Handler function on new environment variables](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/details.jpg)**Handler function on new environment variables**  
*Source: Cisco Talos*
Cisco Talos disclosed the above flaws to Garrett on August 17, 2021, and the vendor fixed the identified issues on December 13, 2021.


Admins of walk-through Garrett Metal detectors are urged to upgrade their iC Module CMA software to the latest available version to resolve these vulnerabilities.


If you are unsure how to do that, contact your Garrett sales representative and ask for guidance.


As these vulnerabilities require access to the network used by the metal detector, they will not likely be targeted in mass by threat actors. However, [insider threats continue to be a problem](https://www.bleepingcomputer.com/news/security/former-ubiquiti-dev-charged-for-trying-to-extort-his-employer/) and are usually not detected until after the damage is done.


The US government recently [warned about insider threats](https://www.bleepingcomputer.com/news/security/cisa-releases-tool-to-help-orgs-fend-off-insider-threat-risks/) and released a self-assessment tool to help organizations determine their risk posture to insider attacks.


BleepingComputer has reached out to Garrett to learn more about the impact of these vulnerabilities but has not heard back.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Garrett]] [[Cvss]] [[V3]] [[Talos]] [[Specially-crafted]] [[Walk-through]] [[Udp]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-21901]] [[CVE-2021-21903]] [[CVE-2021-21904]] [[CVE-2021-21905]] [[CVE-2021-21906]] [[CVE-2021-21902]] [[CVE-2021-21908]] [[CVE-2021-21909]] [[CVE-2021-21907]]

