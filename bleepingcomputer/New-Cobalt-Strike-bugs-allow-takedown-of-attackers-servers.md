# New Cobalt Strike bugs allow takedown of attackers’ servers
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-cobalt-strike-bugs-allow-takedown-of-attackers-servers/)
+ Date: August 4, 2021
+ Author: Sergiu Gatlan


## Article:
![New Cobalt Strike bugs allow takedown of attackers’ servers](https://www.bleepstatic.com/content/hl-images/2021/07/15/Lights-Man-Action.jpg)


Security researchers have discovered Cobalt Strike denial of service (DoS) vulnerabilities that allow blocking beacon command-and-control (C2) communication channels and new deployments.


[Cobalt Strike](https://attack.mitre.org/software/S0154/) is a legitimate penetration testing tool designed to be used as an attack framework by red teams (groups of security professionals who act as attackers on their own organization's infrastructure to discover security gaps and vulnerabilities.)


However, Cobalt Strike is also used by threat actors (commonly seen used during ransomware attacks) for post-exploitation tasks after deploying so-called beacons, which provide them with persistent remote access to compromised devices.


Using these beacons, the attackers can later access the breached servers to harvest data or deploy second-stage malware payloads.


Targets on attackers' infrastructure
------------------------------------


SentinelLabs (the threat research team at SentinelOne) found the DoS vulnerabilities collectively tracked as **CVE-2021-36798** (and dubbed **Hotcobalt**) in the latest versions of Cobalt Strike's server.


As they discovered, one can register fake beacons with the server of a particular Cobalt Strike installation. By sending fake tasks to the server, one can crash the server by exhausting available memory.


The crash can render already installed beacons unable to communicate with the C2 server, block new beacons from being installed on infiltrated systems, and interfere with ongoing red team (or malicious) operations that used the deployed beacons.


"This lets a malicious actor cause memory exhaustion on the machine the Cobalt's server (the 'Teamserver') runs on, which makes the server unresponsive until it's restarted," [SentinelLabs said](https://labs.sentinelone.com/hotcobalt-new-cobalt-strike-dos-vulnerability-that-lets-you-halt-operations/).


"This means that live beacons cannot communicate to their C2 until the operators restart the server. Restarting, however, won't be enough to defend against this vulnerability as it is possible to repeatedly target the server until it is patched or the beacon's configuration is changed."


Since Cobalt Strike is also heavily used by threat actors for various nefarious purposes, law enforcement and security researchers can also employ the Hotcobalt vulnerabilities to take down malicious infrastructure.


On April 20, SentinelLabs has disclosed the vulnerabilities to CobaltStrike's parent company HelpSystems, who addressed them in Cobalt Strike 4.4, released earlier today.


Disclosure Timeline:
--------------------



04/20/2021 - Initial contact with HelpSystems for issue disclosure.  

04/22/2021 - Issue details disclosed to HelpSystems.  

04/23/2021 - HelpSystems confirmed the issue and asked for an extension until August 3rd.  

04/28/2021 - SentinelOne accepted the extension.  

07/18/2021 - Submitted CVE request to MITRE.  

07/19/2021 - CVE-2021-36798 was assigned and reserved for the specified issue.  

08/02/2021 - SentinelOne shared the publication date and post for review.  

08/02/2021 - HelpSystems reviewed and confirmed the post for publication.  

08/04/2021 - HelpSystems released Cobalt Strike 4.4, which contains a fix for CVE-2021-36798.



RCE and source code leak
------------------------


This is not the first vulnerability to affect CobaltStrike, with HelpSystems having patched [a directory traversal attack vulnerability in the team server](http://blog.cobaltstrike.com/2016/09/28/cobalt-strike-rce-active-exploitation-reported/) in 2016, leading to remote code execution attacks.


In November 2020, BleepingComputer also reported that the [source code for the Cobalt Strike post-exploitation toolkit had allegedly been leaked](https://www.bleepingcomputer.com/news/security/alleged-source-code-of-cobalt-strike-toolkit-shared-online/) in a GitHub repository.


As Advanced Intel's Vitali Kremez told BleepingComputer at the time, the leak was most likely the re-compiled source code of the 2019 Cobalt Strike 4.0 version.


Kremez also said that the possible leak of Cobalt Strike source code "has significant consequences for all defenders as it removes barriers of entry to obtaining the tool and essentially makes its easy for the crime groups to procure and modify code as needed on the fly."


While BleepingComputer contacted Cobalt Strike and their parent company Help Systems to confirm the source code's authenticity when the leak was discovered, we haven't heard back.




#### Tags:
[[HelpSystems]] [[SentinelLabs]] [[BleepingComputer]] [[Bleeping Computer]]
