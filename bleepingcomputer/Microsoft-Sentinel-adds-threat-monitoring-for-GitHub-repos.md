# Microsoft Sentinel adds threat monitoring for GitHub repos
### Microsoft says its cloud-native SIEM (Security Information and Event Management) platform now allows to detect potential ransomware activity using the Fusion machine learning model.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-sentinel-adds-threat-monitoring-for-github-repos/
+ Date: 2022-02-02T11:29:36-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/08/09/Azure-Sentinel.jpg)

![Microsoft Sentinel adds threat monitoring for GitHub repos](https://www.bleepstatic.com/content/hl-images/2021/08/09/Azure-Sentinel.jpg)


Microsoft Sentinel now comes with support for continuous GitHub threat monitoring, which helps keep track of potentially malicious events after ingesting GitHub enterprise repository logs.


[Microsoft Sentinel](https://azure.microsoft.com/en-us/services/microsoft-sentinel/) (previously known as Azure Sentinel) is Redmond's cloud-native SIEM (Security Information and Event Management) platform.


It uses artificial intelligence (AI) to analyze vast volumes of data, hunting for potential threat actor activity across enterprise environments.


"Today, together with Microsoft Sentinel, you can connect your enterprise-licensed GitHub repository environment to the Microsoft Sentinel workspace and ingest the GitHub audit log – tracking events such as new repository creation or deletion, counting the number of repository clones, and more," Microsoft explained.


"It is highly important to track the different activities in the company's GitHub repository, to identify suspicious events, and to have the ability to investigate anomalies in the environment."


The Microsoft Sentinel GitHub threat monitoring only works with GitHub enterprise licenses, and it comes with analytics rules to trigger alerts on suspicious events and one workbook for visualizing data.



![Microsoft Sentinel GitHub alerts](https://www.bleepstatic.com/images/news/u/1109292/2022/Sentinel_GitHub_alerts.jpg)*Microsoft Sentinel GitHub alerts (Microsoft)*
Alerts that will show up on the Microsoft Sentinel dashboard triggered by the new analytics rules include:


1. **Repository was created:**each time a repository is created in the GitHub environment connected to the Microsoft Sentinel workspace.
2. **Repository was destroyed**: each time a repository is destroyed in the GitHub environment.
3. **A payment method was removed:**each time there's an action with the payment method configured for the GitHub repository.
4. **OAuth application**: each time a client secret was removed.

Using the workbook, security teams can also keep track of members being added and removed from a GitHub repo, newly added repositories, and how many times each repo was forked or cloned.


You can find detailed instructions on connecting enterprise-licensed GitHub repository to your Microsoft Sentinel workspace in [this Tech Community blog post](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/microsoft-sentinel-continuous-threat-monitoring-for-github/ba-p/3037154).


In December, Microsoft added an [Apache Log4j Vulnerability Detection solution](https://docs.microsoft.com/en-us/azure/sentinel/whats-new#apache-log4j-vulnerability-detection-solution-public-preview) in public preview to help customers detect and investigate signals linked to the exploitation of [Log4Shell vulnerabilities](https://www.bleepingcomputer.com/tag/log4shell/).


Microsoft Sentinel now also supports [mapping analytics rules to MITRE ATT&CK techniques](https://docs.microsoft.com/en-us/azure/sentinel/whats-new#support-for-mitre-attck-techniques-public-preview) which helps narrow down search results.


In August, Microsoft updated its SIEM platform with [new detections for possible ransomware attacks](https://www.bleepingcomputer.com/news/microsoft/microsoft-adds-fusion-ransomware-attack-detection-to-azure-sentinel/) using the Fusion machine learning model.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Github]] [[Bleeping Computer]]

