# Microsoft adds Fusion ransomware attack detection to Azure Sentinel
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-adds-fusion-ransomware-attack-detection-to-azure-sentinel/)
+ Date: August 9, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft adds Fusion ransomware detection to Azure Sentinel](https://www.bleepstatic.com/content/hl-images/2021/08/09/Azure-Sentinel.jpg)


Microsoft says that the Azure Sentinel cloud-native SIEM (Security Information and Event Management) platform is now able to detect potential ransomware activity using the Fusion machine learning model.


[Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview) uses built-in artificial intelligence (AI) technology to quickly analyze vast volumes of data across enterprise environments, hunting for potential threat actor activity.



It also employs machine learning tech known as [Fusion](https://docs.microsoft.com/en-us/azure/sentinel/fusion) to detect and trigger multi-stage attack alerts by identifying sets of suspicious activities and abnormal behavior spotted at various attack stages.


Azure Sentinel couples several of these alerts to generate incidents even when there's limited or missing information, making them highly difficult to catch otherwise.


Microsoft [announced](https://techcommunity.microsoft.com/t5/azure-sentinel/what-s-new-fusion-detection-for-ransomware/ba-p/2621373) today that its cloud-based SIEM now supports Fusion detections for possible ransomware attacks and triggers high severity *Multiple alerts possibly related to Ransomware activity detected* incidents.


For instance, Azure Sentinel will generate ransomware attack incidents after detecting the following alerts within a specific timeframe on the same host:


* Azure Sentinel scheduled alerts (informational): **Windows Error and Warning Events**
* Azure Defender (medium): **'GandCrab' ransomware was prevented**
* Microsoft Defender for Endpoint (informational): **'Emotet' malware was detected**
* Azure Defender (low): **'Tofsee' backdoor was detected**
* Microsoft Defender for Endpoint (informational): **'Parite' malware was detected**


To detect potential ongoing ransomware attacks, Azure Sentinel can use the following data connectors to collect data from the following sources: [Azure Defender (Azure Security Center)](https://docs.microsoft.com/en-us/azure/sentinel/connect-azure-security-center), [Microsoft Defender for Endpoint](https://docs.microsoft.com/en-us/azure/sentinel/connect-microsoft-defender-advanced-threat-protection), [Microsoft Defender for Identity](https://docs.microsoft.com/en-us/azure/sentinel/connect-azure-atp), [Microsoft Cloud App Security](https://docs.microsoft.com/en-us/azure/sentinel/connect-cloud-app-security), and [Azure Sentinel scheduled analytics rules](https://docs.microsoft.com/en-us/azure/sentinel/tutorial-detect-threats-built-in#scheduled).



![Fusion ransomware detection incident](https://www.bleepstatic.com/images/news/u/1109292/2021/Fusion%20ransomware%20detection%20incident.png)*Fusion ransomware detection incident (Microsoft)*
Admins advised to consider systems as 'potentially compromised'
---------------------------------------------------------------


"Incidents are generated for alerts that are possibly associated with Ransomware activities, when they occur during a specific time-frame, and are associated with the Execution and Defense Evasion stages of an attack," Microsoft [explains](https://docs.microsoft.com/en-us/azure/sentinel/whats-new#fusion-detection-for-ransomware-public-preview).


"You can use the alerts listed in the incident to analyze the techniques possibly used by attackers to compromise a host/device and to evade detection."


Following a ransomware attack scenario detected by Fusion in Azure Sentinel, admins are advised to consider the systems as "potentially compromised" and take immediate actions.


Microsoft provides the following recommended steps for analyzing the techniques used by attackers during the potential attack:


1. Isolate the machine from the network to prevent potential lateral movement.
2. Run a full antimalware scan on the machine, following any resulting remediation advice.
3. Review installed/running software on the machine, removing any unknown or unwanted packages.
4. Revert the machine to a known good state, reinstalling the operating system only if required and restoring software from a verified malware-free source.
5. Resolve recommendations from alert providers (e.g., [Azure Security Center](https://docs.microsoft.com/en-us/azure/security-center/security-center-recommendations) and [Microsoft Defender](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/tvm-security-recommendation)) to prevent future breaches.
6. Investigate the entire network to understand the intrusion and identify other machines that might be impacted by this attack.




#### Tags:
[[Microsoft]] [[ransomware]] [[(informational):]] [[Bleeping Computer]]
