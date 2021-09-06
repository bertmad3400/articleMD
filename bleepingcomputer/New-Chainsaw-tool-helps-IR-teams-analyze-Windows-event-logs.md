# New Chainsaw tool helps IR teams analyze Windows event logs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-chainsaw-tool-helps-ir-teams-analyze-windows-event-logs/)
+ Date: September 6, 2021
+ Author: Ionut Ilascu


## Article:
![New Chainsaw tool helps incident responders find relevant info in Windows event logs](https://www.bleepstatic.com/content/hl-images/2021/09/06/Chainsaw.jpg)


Incident responders and blue teams have a new tool called Chainsaw that speeds up searching through Windows event log records to identify threats.


The tool is designed to assist in the first-response stage of a security engagement and can also help blue teams triage entries relevant for the investigation.


### Built for incident responders


Windows event logs are a ledger of the system’s activities, comprising details about applications and user logins. Forensic investigators rely on these records, sometimes as the main source of evidence, to create a timeline of events of interest.


The difficulty with checking these records is that there’s a lot of them, especially on systems with a high logging level; sifting through for relevant information can and can be a time-consuming task.


Authored by [James D](https://twitter.com/FranticTyping), lead threat hunter at F-Secure’s Countercept division, [Chainsaw](https://github.com/countercept/chainsaw) is a Rust-based command-line utility that can go through event logs to highlight suspicious entries or strings that may indicate a threat.


The tool uses the [Sigma rule](https://github.com/SigmaHQ/sigma) detection logic to quickly find event logs relevant to the investigation.



“Chainsaw also contains built-in logic for detection use-cases that are not suitable for Sigma rules, and provides a simple interface to search through event logs by keyword, regex pattern, or for specific event IDs.”



F-Secure says that Chainsaw is specifically tailored for quick analysis of event logs in environments where a detection and response solution (EDR) was not present at the time of compromise.


In such cases, threat hunters and incident responders can use Chainsaw’s search features to extract from Windows logs information pertinent to malicious activity.


Users can use the tool to do the following:


* Search through event logs by event ID, keyword, and regex patterns
* Extract and parse Windows Defender, F-Secure, Sophos, and Kaspersky AV alerts
* Detect key event logs being cleared or the event log service being stopped
* Detect users being created or added to sensitive user groups
* Brute-force of local user accounts
* RDP logins, network logins etc.



![Chainsaw hunting and searching for relevant info in Windows event logs](https://www.bleepstatic.com/images/news/u/1100723/2021/ChainsawSearch_Hunt.jpg)**Chainsaw hunting for suspicious events and searching for mimikatz activity**
Apart from this, Sigma rule detection works for numerous Windows event IDs that include the following:


Available as an [open-source tool](https://github.com/countercept/chainsaw), Chainsaw uses the [EVTX parser](https://github.com/omerbenamram/evtx) library and the detection logic matching provided by F-Secure Countercept's [TAU Engine](https://github.com/countercept/tau-engine) library. It can output the results in ASCII table, CSV, or JSON.




#### Tags:
[[Chainsaw]] [[Windows]] [[Bleeping Computer]]
