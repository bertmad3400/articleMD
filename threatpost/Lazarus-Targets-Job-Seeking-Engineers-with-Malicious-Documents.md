# Lazarus Targets Job-Seeking Engineers with Malicious Documents
### Notorious North Korean APT impersonates Airbus, General Motors and Rheinmetall to lure potential victims into downloading malware.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167647)
+ Date: July 9, 2021  6:50 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2019/02/04145722/APT_Lazarus_APT.png)
The notorious [Lazarus](https://threatpost.com/lazarus-group-advanced-malware-framework/157636/) advanced persistent threat (APT) group has been identified as the cybergang behind a campaign spreading malicious documents to job-seeking engineers. The ploy involves impersonating defense contractors seeking job candidates.


Researchers have been tracking Lazarus activity for months with engineering targets in the United States and Europe, according to a [report published online](https://cybersecurity.att.com/blogs/labs-research/lazarus-campaign-ttps-and-evolution) by AT&T Alien Labs.


According to the report’s author, Fernando Martinez, emails sent to prospective engineering candidates by the APT purport to be from known defense contractors Airbus, General Motors (GM) and Rheinmetall.


Attached to the emails are Windows documents containing macro-based malware, “which has been developed and improved during the course of this campaign and from one target to another,” Martinez wrote.



“The core techniques for the three malicious documents are the same, but the attackers attempted to reduce the potential detections and increase the faculties of the macros,” he wrote.


The campaign is just the latest by Lazarus that targets the defense industry. In February, researchers linked [a 2020 spear phishing campaign](https://threatpost.com/lazarus-targets-defense-threatneedle-malware/164321/) to the APT that aimed at stealing critical data from defense companies by leveraging an advanced malware called ThreatNeedle.


Indeed, with its use of Microsoft Office Macros and compromised third-party infrastructure for communications, the latest attacks have Lazarus written all over them, remaining “in line with the Lazarus’ past campaigns,” Martinez wrote.


“Attack lures, potentially targeting engineering professionals in government organizations, showcase the importance of tracking Lazarus and their evolution,” he wrote. “We continue to see Lazarus using the same tactic, techniques, and procedures that we have observed in the past.”


**Expanding Campaign Against Engineers**
----------------------------------------


AT&T Alien Labs researchers previously had observed activity by Lazarus to try to lure victims with fake job opportunities from Boeing and BAE systems. They were alerted to the new campaign when Twitter users identified several documents from May to June of this year that were linked to Lazarus group using Rheinmetall, GM and Airbus as lures, Martinez wrote.


Specifically, those malicious documents were: “Rheinmetall\_job\_requirements.doc”: identified by [ESET Research](https://twitter.com/esetresearch/status/1389904254811394049); “General\_motors\_cars.doc*“*: identified by Twitter user [@1nternaut](https://twitter.com/1nternaut/status/1394050982632468481); and “Airbus\_job\_opportunity\_confidential.doc*“*: identified by [360CoreS](https://twitter.com/360CoreSec/status/1402920149754155010).


The campaigns using the three new documents have similarities in command and control (C&C) communication but different ways of executing malicious activity, researchers found.


Lazarus distributed two malicious documents related to Rheinmetall, a German engineering company focused on the defense and automotive industries. However, the second included “more elaborate content,” and thus went likely went unnoticed by victims, Martinez wrote.


One unique aspect of the macro contained in the initial malicious document is that it renames Certutil, a command-line program in Microsoft Docs installed as part of Certificate Services, in an attempt to obscure its activities.


The ultimate payload of the Rheinmetall document uses Mavinject.exe, a legitimate Windows component that has been used and abused before in malware activity, to perform arbitrary code injections inside any running process, Martinez wrote. Attackers use a compromised domain as the C&C server in this case, Martinez added.


The GM document included an attack vector similar to the Rheinmetall one with minor updates in the C&C communication process, researchers found. However, the C&C domain used in relation to this malicious activity, allgraphicart[.]com, no longer appears to be compromised, Martinez noted.


**Evolving Tactics**
--------------------


The Airbus document macro, like the Rheinmetall attack, used and renamed Certutil as an evasive maneuver and shared similar C&C communications tactics. However, it also demonstrated a progression of injection and execution processes that abandons the previous use of Mavinject to do its dirty work, researchers found.


“The macro executes the mentioned payload with an updated technique,” Martinez wrote. “The attackers are no longer using Mavinject, but directly executing the payload with explorer.exe, significantly modifying the resulting execution tree.”


Once the payload has been executed, the macro in the Airbus document waits for three seconds before creating of an .inf file in the same folder. Then, whether it was successfully executed or not, the macro will proceed to send the beacon to the C&C with the execution status and delete all the temporary files, attempting to eliminate any evidence of malicious activities, researchers said.


Given the historically prolific nature of Lazarus—[named “the most active” threat group](https://securelist.com/lazarus-threatneedle/100803/) of 2020 by Kaspersky —the latest attack against engineers “is not expected to be the last,” Martinez noted.


“Attack lures, potentially targeting engineering professionals in government organizations, showcase the importance of tracking Lazarus and their evolution,” he wrote.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Rheinmetall]] [[malware]] [[Mavinject]] [[ThreatPost]]
