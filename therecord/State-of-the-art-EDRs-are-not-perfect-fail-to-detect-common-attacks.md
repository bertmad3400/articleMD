# State-of-the-art EDRs are not perfect, fail to detect common attacks
### A team of Greek academics has tested endpoint detection & response (EDR) software from 11 of today's top cybersecurity firms and found that many fail to detect some of the most common attack techniques used by advanced persistent threat actors, such as state-sponsored espionage groups and ransomware gangs.

## Information:
+ Source: The Record
+ Link: https://therecord.media/state-of-the-art-edrs-are-not-perfect-fail-to-detect-common-attacks/
+ Date: 2022-01-04T10:41:43+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2022/01/antivirus-EDR-robot-machine-learning-AI.jpg)

A team of Greek academics has tested endpoint detection & response (EDR) software from 11 of today’s top cybersecurity firms and found that many fail to detect some of the most common attack techniques used by advanced persistent threat actors, such as state-sponsored espionage groups and ransomware gangs.


“Our results indicate that there is still a lot of room for improvement as state-of-the-art EDRs fail to prevent and log the bulk of the attacks that are reported in this work,” said George Karantzas and Constantinos Patsakis, two academics from the University of Piraeus, in Athens, Greece.


### Typical attack scenario


The research, detailed in a paper published last year and titled “**An Empirical Assessment of Endpoint Detection and Response Systems against Advanced Persistent Threats Attack Vectors**“[[1](https://www.mdpi.com/2624-800X/1/3/21/htm), [2](https://arxiv.org/abs/2108.10422)], looked at [EDR software](https://en.wikipedia.org/wiki/Endpoint_detection_and_response), which is an evolution of the classic antivirus program that operates using both static and dynamic analysis methods to detect malware, but also monitors, collects, and aggregates data from endpoints in an attempt to detect malicious behavior that relies on more stealthy techniques, such as abusing legitimate apps to carry out attacks.


Today, EDRs combine everything from static file signature rules to advanced machine learning modules and are considered the top of the food chain in regards to security software. However, they are not perfect.


Karantzas and Patsakis’ research set out to find out how the EDRs from some of today’s largest companies fair in the face of various simple attacks that simulate common APT kill chains.


Their work included buying a mature expired domain to host malware payloads, securing the domain with a Let’s Encrypt SSL certificate, and hosting four types of files commonly used in attacks, such as:


* A Windows Control panel shortcut file (.cpl);
* A legitimate Microsoft Teams installer (that will load a malicious DLL);
* An unsigned portable executable (EXE) file;
* An HTML application (HTA) file.


Once executed, these four files would all abuse legitimate functions to load and run a Cobalt Strike Beacon backdoor.


The idea behind this attack chain is that these four files and the Beacon backdoor are regular payloads typically sent to victims part of spear-phishing email campaigns—and something that all EDRs are expected to either detect, block, or at least alert security teams when deployed inside corporate networks.


### Tested EDRs and results


The research team tested these attacks against EDR software from Carbon Black, CrowdStrike, ESET, Kaspersky, F-Secure, McAfee, Microsoft, Sentinel One, Sophos, Symantec, and Trend Micro. The results are in the table below:


![EDR-test-results](https://therecord.media/wp-content/uploads/2022/01/EDR-test-results-1024x411.png)
The results show that none of the tested EDRs had full coverage for all attack vectors, allowing threat actors a way to slip through a company’s defenses.


The research team argued that this opens the EDRs to situations where attackers could turn them off or at least disable their telemetry functions, effectively blinding defenders to what may be happening on an infected system and allowing threat actors to prepare further attacks on the local network.


But not all EDRs were tested part of this experiment.


Appearing last year in a vlog on the YouTube channel of John Hammond, a senior security at Huntress Labs, the researchers said that not all EDR vendors agreed to open their products for testing, and even some of the 11 products they tested was done with the help of intermediaries such as SOC and CERT teams.


However, Karantzas and Patsakis said that once their research went live, some vendors reached out and inquired about it and the ways they could improve their products.








## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Carbon]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=UPPERCUT]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Education]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Greece]] [[victim.continent.name=Europe]] [[victim.city.name=Athens]] [[victim.country.name=Greece]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Edrs]] [[Karantzas]] [[Patsakis]] [[Edr]] [[The Record]]

