# Living Off the Land: How to Defend Against Malicious Use of Legitimate Utilities
### LOLBins help attackers become invisible to security platforms. Uptycs provides a rundown of the most commonly abused native utilities for Windows, Linux and macOS – and advice for protection.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177762
+ Date: 2022-02-01T14:00:08+00:00
+ Author: Threatpost


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/20170144/generic-hacker-laptop.jpg)

Living-off-the-land binaries (LOLBins) are no joke: Cyberattackers have been increasingly making use of them to hide their malicious work from security solutions. It’s time for threat hunters and IT security staff to familiarize themselves with how these are used in the attack chains of some of the most common enterprise malware.


LOLBins are legitimate utilities, libraries and other tools that are native to a given computing environment, which bad actors can hijack and bend to their own nefarious purposes. Since these tools are by their very nature trusted (and used for dozens of innocent daily activities), they tend to be invisible to many antivirus and other security platforms that fail to inspect scripts or monitor process behavior.


For instance, it’s tough for security tools to determine if activity like looking up local Domain Controllers using an admin tool is the work of cyberattackers performing recon, or just normal troubleshooting activity.


Using LOLBins is also an attractive approach for cybercriminals because they can use them to get around certain security restrictions. For instance, Application Allow-Listing prevents Windows OS from running code unless it has a valid digital certificate. Certain LOLBins utilities though are signed applications, which can in turn open untrusted, unsigned applications.


It’s unsurprising, then, that the Uptycs Threat Research team has seen a significant increase in the LOLBins being used in various stages of the MITRE ATT&CK framework. For instance, the utilities regsvr32.exe and rundll32.exe have seen spiking abuse levels, with both being used extensively by the Qbot and IcedID backdoor malwares over the course of the last year, as detailed in our latest [Quarterly Threat Bulletin.](https://www.uptycs.com/threat-research-quarterly-bulletin-2?utm_campaign=Threat%20Research&utm_source=threatpost&utm_medium=sponsored_article&utm_content=lolbins)


Similarly, the [Loki](https://threatpost.com/oil-gas-cyber-espionage-campaign/167639/) and [Agent Tesla](https://threatpost.com/agent-tesla-microsoft-asmi/163581/) spyware samples have been seen exploiting a Microsoft Equation Editor (EE) vulnerability in the EQNEDT32.exe Windows utility at high volume, using decoy documents in the execution phase of the attack lifecycle.


These are but the tip of the proverbial cybercrime iceberg.


The following is a rundown of the most commonly abused LOLBins for Windows, Linux and macOS.


Targeted Windows Utilities
--------------------------


Unsurprisingly, Windows has a large number of utilities that threat actors target for abuse.


***Powershell.exe Tactic: Execution and Command & Control***


PowerShell makes a perfect tool for adversaries to compromise a system. It provides attackers access to various Windows features which can be abused for downloading payloads, disabling Microsoft Defender and firewalls, executing fileless malware and so on.


***Mshta.exe Tactic: Defense Evasion***  

Mshta.exe is a Windows utility that executes Microsoft HTML Applications (HTA) files or JavaScript/VBScript files. Adversaries leverage mshta.exe for proxy execution of malicious HTA files or JavaScript or VBScript.


The infamous [TrickBot malware](https://threatpost.com/trickbot-malware-virtual-desktop-espionage/167789/), often used as a first-stage loader for ransomware and other payloads, has been leveraging mshta.exe for the past year.


***Regsvr32.exe Tactic: Defense Evasion***  

Regsvr32 is a Windows built-in utility that can be used to register and unregister service DLLs. Adversaries leverage regsvr32 to download suspicious scripts hosted on remote servers and execute it in memory.


Both the [Dridex](https://threatpost.com/covid-19-relief-checks-dridex-malware/164853/) and TrickBot malware families have leveraged regsvr32.exe in their infection routines.


***Wmic.exe Tactic: Execution***  

Wmic.exe is an executable which belongs to Windows Management Instrumentation (WMI). It provides an environment for accessing local or remote Windows system components.


Dridex malware leverages wmic to execute rundll32 in the Execution phase of its attack lifecycle, but adversaries may also abuse wmic.exe to achieve execution, discovery or lateral movement.


***EQNEDT32.exe Tactic: Execution***  

EQNEDT32.exe is a legitimate binary associated with Microsoft Equation Editor. Adversaries may exploit EQNEDT32.exe to execute arbitrary code; that’s the case, as mentioned, with the Agent Tesla and Loki malwares.


Targeted Linux Utilities
------------------------


In the third quarter of 2021, chattr and wget were seen to be the top abused Linux utilities.


***Chattr Tactic: Defense Evasion***  

The chattr function in Linux is used to set/unset certain attributes of a file. Adversaries use this for changing permission of the system files or to make their dropped files immutable so that a user cannot delete it.


The self-propagating [Kinsing malware](https://threatpost.com/self-propagating-malware-docker-ports/154453/) uses this utility to change permissions of SSH keys and password files in the defense-evasion phase of its attack lifecycle.


***Wget Tactic: Command & Control***  

The wget command is a Linux command line utility for downloading files from the internet. Adversaries use this for downloading next-stage payloads.


Malware families like the [Mirai botnet](https://threatpost.com/mirai-variant-sonicwall-d-link-iot/164811/) use wget to download the second stage of the malware in the C2 phase of its attack lifecycle.


***Setfacl Tactic: Defense Evasion***  

The setfacl utility is used in Linux to set, modify or remove the access control list (ACL) used to govern access to regular files and directories.


Kinsing malware uses setfacl to set executable permission on /bin/chmod in the defense-evasion phase of the attack lifecycle.


***Crontab Tactic: Persistence***  

In Linux, the crontab command opens the cron table for editing the list of tasks scheduled to run at regular time intervals on the system.


[Cryptocurrency in miners](https://threatpost.com/loudminer-cryptominer-linux/145871/) have been seen accessing cron entries to delete already-installed cron jobs and to install a new cron job in the persistence phase of the attack lifecycle.


***Rm Tactic: Defense Evasion***  

The rm command is used to delete files from Linux filesystem.


Many malware families, including the Mirai and [Gafgyt](https://threatpost.com/gafgyt-botnet-ddos-mirai/165424/) internet-of-things (IoT) botnets and various cryptocurrency coin-miners, use rm to self-destruct and delete their tracks in the defense evasion phase of the attack lifecycle.


Targeted macOS Utilities
------------------------


In the third quarter of 2021, the majority of observed macOS malware in the wild was contributed by the [Shlayer](https://threatpost.com/shlayer-mac-youtube-wikipedia/152146/) and [Bundlore](https://threatpost.com/apple-accidentally-notarizes-shlayer-malware/158818/) adware strains, both of which make heavy use of LOLBins.


***OpenSSL Tactic: Defense Evasion***  

OpenSSL is an open-source command-line tool that is commonly used to generate private keys, create CSRs, install SSL/TLS certificates and identify certificate information.


The Shlayer malware leverages OpenSSL often in conjunction with base64, to encode and decode malware and hide it from detection in the defense-evasion phase of the attack lifecycle.


***Curl Tactic: Command & control***  

curl is a macOS command-line tool used for transferring data using various network protocols.


The Bundlore malware leverages curl to download payloads in the C2 phase of the attack lifecycle.


***SQLite Tactic: Exfiltration***  

SQLite is a transactional SQL database engine present in macOS. It’s generally used to create databases that can be transported across machines.


Bundlore malware leverages SQLite to retrieve the history of downloaded files from the internet in the exfiltration phase of its attack lifecycle.


***Killall Tactic: Defense Evasion***  

killall is a macOS utility for terminating running processes on a system based on name.  

The Shlayer malware uses killall to kill the running script’s terminal window after bash script activity is completed.


***Funzip Tactic: Defense Evasion***  

funzip is a macOS utility that extracts a .ZIP or .GZIP file directly to output, from archives or other piped input.


Shlayer uses it with head or tail commands to extract a malicious binary with a password.


How to Defend Against LOLBins Attacks
-------------------------------------


While the above are the most commonly abused native utilities, there are yet more that bad actors are known to add into their coding mix. The good news however is that there are ways to combat the threat – most notably by deploying an endpoint detection and response (EDR) tool that tracks process invocation and inspect processes.


For instance, Uptycs’ EDR can determine if any of the common LOLBins are being used in an attack on a given environment. To make that happen, the Uptycs Threat research team has created more than 300 rules covering different LOLBins techniques used by cybercriminals in the MITRE ATT&CK framework, using the data from customer telemetry and threat-intelligence systems.


Other defense strategies include taking a multilayered approach to closing off low-hanging fruit when it comes to initial access. This includes using a range of technologies such as web scanning, email security, Next-Generation Firewalls (NGFW), Next-Generation Intrusion Prevention Systems (NGIPS), secure internet gateways (SIG) and of course, user education when it comes to password hygiene and phishing detection.


The use of LOLBins is only going to increase. Companies of all sizes should act now to ward off stealthy malware and keep their networks and endpoints safe.


***[Check out the Uptycs Resource Center for education, insight and original research on detections, cloud security, and compliance topics.](https://www.uptycs.com/resources#allutm_campaign=Threat%20Research&utm_source=threatpost&utm_medium=sponsored_article&utm_content=lolbins)***





## Tags:

#### Threatactor:
[[threatactor.name=Equation]]

#### Action:
[[action.malware.name=Agent Tesla]] [[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Bundlore]] [[action.malware.name=Dridex]] [[action.malware.name=IcedID]] [[action.malware.name=Kinsing]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=QakBot]] [[action.malware.name=Reg]] [[action.malware.name=Reg]] [[action.malware.name=Rover]] [[action.malware.name=Tor]] [[action.malware.name=TrickBot]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Education]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Malware]] [[Lolbins]] [[Windows]] [[Lifecycle]] [[Linux]] [[Macos]] [[Uptycs]] [[Microsoft]] [[Eqnedt32.exe]] [[Cron]] [[ThreatPost]]

