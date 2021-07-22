# Industrial Networks Exposed Through Cloud-Based Operational Tech
### Critical ICS vulnerabilities can be exploited through leading cloud-management platforms.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168024)
+ Date: July 22, 2021  1:46 pm
+ Author: Becky Bracken


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/03/25130947/factory.jpg)
The benefits of using a cloud-based management platform to monitor and configure industrial control systems (ICS) devices are obvious — efficiency, cost-savings and better diagnostics just for starters. But new research found critical vulnerabilities in these platforms that could be used to paralyze operations if left unmitigated.


[An analysis](https://claroty.com/2021/07/21/blog-research-exploiting-vulnerabilities-in-the-ot-cloud-era/) by Claroty’s newly branded Team82 research team found striking vulnerabilities in the CODESYS and WAGO industrial systems, which make use of cloud-based automation for operational technology (OT) — a segment often referred to as “Industry 4.0.”



CODESYS has developed a cloud-based platform called Automation Server to manage programmable logic controllers (PLCs) remotely, which are the computers involved in managing physical industrial equipment. OT engineers using Automation Server can download logic and configure their PLCs through the cloud-based Automation Server management console.


WAGO PFC100/200 meanwhile is a series of PLCs that make heavy use of the CODESYS runtime, and most of the communication, configuration and programming of these PLCs is done through the CODESYS platform. These devices can also be managed by the CODESYS Automation Server platform, and engineers can remotely download logic to them.


The vulnerabilities, if exploited, can lead to serious consequences, including gaining control of industrial equipment and operations.


“A vulnerability in a Level 0/1 device such as a PLC can be leveraged to launch attacks targeting a cloud-based management system,” the Team82 report said. “And the reverse is also true: Weaknesses in the cloud platform and its peripherals can put an attacker in the driver’s seat for uncontrolled access to field devices and industrial processes.”


**CODESYS and WAGO Vulnerabilities**
------------------------------------


Analysts found three vulnerabilities in the CODESYS products:


They also found four bugs in two WAGO systems:


Several types of exploits are possible, but Claroty flagged a couple of note. In one proof-of-concept, they were able to modify a CODESYS Package Designer package to retrieve a user’s cloud credentials; the attack involves socially engineering a logged-in user to install it.


“The vulnerability we exploited stems from a lack of verification of the package source and its contents,” according to the report. “This makes it trivial to create a legitimate-looking CODESYS package that executes malicious code.”


The attack would allow access to the CODESYS cloud-based management console, from which adversaries can further exploit any managed PLCs connected to the console.


“The simplest thing attackers can do is modify or even stop the logic currently running on managed PLCs,” researchers said. “For example, an attacker could stop a PLC program responsible for temperature regulation of the production line, or change centrifuge speeds as was the case with Stuxnet. These types of attacks could lead to real-life damage and affect production times and availability.”


Also of note, researchers were able to achieve pre-authenticated remote code execution on the WAGO device, using two vulnerabilities  in the iocheckd protocol: CVE-2021-34566 and CVE-2021-34567. Chaining the exploits together enabled them to remotely attack the device and implant a webshell for further interaction and command execution, according to the analysis.


“Team82’s latest research was motivated by the reality that organizations in the Industry 4.0 era are incorporating cloud technology into their OT and industrial internet of things (IIoT) for simplified management, better business continuity and improved performance analytics,” Amir Preminger, vice president of research, at Claroty said. “In order to fully reap these rewards, organizations must implement stringent security measures to secure data in transit and at rest and lock down permissions.”


On the Hunt for Industrial Security Bugs
----------------------------------------


Both security teams and attackers are actively hunting for these types of holes in industrial network security. May’s crippling [ransomware attack on the Colonial Pipeline](https://threatpost.com/pipeline-crippled-ransomware/165963/) impacted the OT level, for example, interrupting fuel supplies to most of the East Coast of the U.S.


Just last week, Schneider Electric programmable logic controllers (PLCs) used in manufacturing, building automation and healthcare, were reported to have [vulnerabilities that allowed attackers](https://threatpost.com/unpatched-critical-rce-industrial-utility-takeovers/167751/) to gain root-level control.


And there are little signs  that the phenomenon of critical vulnerabilities coming to light is going to slow down anytime soon. Earlier this year, Claroty released research that showed a 33 percent increase in ICS disclosures since 2018 and warned that  legacy systems, now being managed in the cloud, are also [chock-full of security holes](https://threatpost.com/industrial-networks-hackable-security-holes/163708/).


“While ICS and SCADA vulnerability research is maturing, there are still many decades-old security issues yet uncovered,” the Claroty report from February explained. “For the time being, attackers may have an edge in exploiting them, because defenders are often hamstrung by uptime requirements and an increasing need for detection capabilities against exploitable flaws that could lead to process interruption or manipulation.”


For their part, WAGO and CODESYS were quick to respond with mitigations and patches for all of the reported vulnerabilities.


“We thank the CODESYS and WAGO teams for their swift response, updates and mitigations that benefit their customers and the ICS domain,” Preminger said.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 


 




#### Tags:
[[CODESYS]] [[WAGO]] [[PLCs]] [[cloud-based]] [[Claroty]] [[ICS]] [[cloud]] [[Team82]] [[ThreatPost]]
