# Google Cloud hypervisor modified to detect cryptominers without agents
### Google has announced the public preview of a new Virtual Machine Threat Detection (VMTD) system that can detect cryptocurrency miners and other malware without the need for software agents.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/google-cloud-hypervisor-modified-to-detect-cryptominers-without-agents/
+ Date: 2022-02-07T12:05:03-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2020/10/16/Google-headpic.jpg)

![Google](https://www.bleepstatic.com/content/hl-images/2020/10/16/Google-headpic.jpg)


Google has announced the public preview of a new Virtual Machine Threat Detection (VMTD) system that can detect cryptocurrency miners and other malware without the need for software agents.


A significant problem for developers and enterprises using cloud-based virtual machines is the [constant targeting](https://www.bleepingcomputer.com/news/security/coinminer-campaigns-move-to-the-cloud-via-docker-kubernetes/) of threat actors who breach servers ([1](https://www.bleepingcomputer.com/news/security/attackers-deploy-cryptominers-on-kubernetes-clusters-via-argo-workflows/), [2](https://www.bleepingcomputer.com/news/security/huawei-cloud-targeted-by-updated-cryptomining-malware/), [3](https://www.bleepingcomputer.com/news/security/alibaba-ecs-instances-actively-hijacked-by-cryptomining-malware/), [4](https://www.bleepingcomputer.com/news/security/docker-hub-images-downloaded-20m-times-come-with-cryptominers/)) to install cryptominers. These miners utilize the GPU and CPU resources of the virtual machine while at the same time reducing the performance of legitimate applications.


Google's [2021 Threat Horizons Report](https://services.google.com/fh/files/misc/gcat_threathorizons_full_nov2021.pdf) claims that coin miner infections account for over 86% of all cases of compromise concerning cloud instances.


To detect threats running on virtual machines, cloud providers commonly install software agents that run within the server acting as security software.


However, these agents can cause a performance hit, and once a server is breached, threat actors can turn these agents off before deploying their malware.


Detect from the hypervisor, not the agent
-----------------------------------------


Google Cloud's engineers decided to follow a unique approach that doesn't involve agents or excessive signal and telemetry data collection to detect coin miners.


Instead, engineers modified Google Compute Engine hypervisor, the underlying emulation software that virtual machines run within, to include scanning capabilities that analyze the VMs memory, and likely network requests, for suspicious activity.


"Traditional endpoint security relies on deploying software agents inside a guest virtual machine to gather signals and telemetry to inform runtime threat detection,” explains Google in the announcement of this new feature.


"But as is the case in many other areas of infrastructure security, cloud technology offers the ability to rethink existing models."


"For Compute Engine, we wanted to see if we could collect signals to aid in threat detection without requiring our customers to run additional software."


As such, there is no impact on performance as software agents are no longer required.


The Virtual Machine Threat Detection (VMTD) feature is entering a public preview today and can be enabled from the Security Command Center.


Google has also shared an inactive miner [on GitHub](https://github.com/GoogleCloudPlatform/security-response-automation/blob/master/inactivated_miner.tar) that admins can use for testing to ensure that they have applied the correct settings on their instances.


No peeking
----------


Google Cloud ascertains its customers that safeguarding their trust in the service remains the utmost priority, and the VMTD workload inspections won’t compromise this in any way.


VMTD will not process memory from Confidential nodes, which are encrypted anyway. Additionally, it will remain an opt-in service that customers can either activate or choose not to use.


Limited roll-out
----------------


At first, the VMTD will be made available as a preview feature for customers of the Security Command Center (SCC) Premium, complementing Event Threat Detection and Container Threat Detection.


According to Google, these three layers of security combined don’t just address the menace of cryptocurrency miners but also ransomware and data exfiltration.


Additionally, SCC Premium customers will enjoy advanced risk mitigation features that help detect misconfigurations, vulnerabilities, and points of non-compliance with industry standards.


Admins can enable VMTD by opening the Settings page in Security Command Center, clicking on "MANAGE SETTINGS" under Virtual Machine Threat Detection, and then selecting a scope for VMTD.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=CHOPSTICK]] [[action.malware.name=Elise]] [[action.malware.name=Miner-C]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Google]] [[Vmtd]] [[Cloud]] [[Bleeping Computer]]

