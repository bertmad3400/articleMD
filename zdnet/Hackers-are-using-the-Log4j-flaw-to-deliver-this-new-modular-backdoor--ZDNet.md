# Hackers are using the Log4j flaw to deliver this new 'modular' backdoor | ZDNet
### Some state-backed hackers go to great lengths to cover their tracks. This Iran-backed group does not, according to Check Point.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/hackers-are-using-the-log4j-flaw-to-deliver-this-new-modular-backdoor/
+ Date: 2022-01-12 10:54:20
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/511e16eb270cba9e871a84a749767bc7c7ebc7ec/2022/01/12/a4fcadd3-6a9e-4b2e-b942-e7b7704ca490/shutterstock-1408496261.jpg?width=770&height=578&fit=crop&auto=webp)

Iran-backed hacking group Phosphorous or APT35 is using the Log4j vulnerability to distribute a new modular PowerShell toolkit, according to security firm Check Point. 

APT35 is one of [several state-backed hacking groups](https://www.zdnet.com/article/log4j-flaw-now-state-backed-hackers-are-using-bug-as-part-of-attacks-warns-microsoft/) known to have been developing tools to exploit public-facing Java applications that use vulnerable versions of the Log4j error-logging component.


Microsoft, which tracks the group as Phosphorous and has called it out for increasingly using ransomware in attacks, found it had [operationalized a Log4j exploit for future campaigns](https://www.zdnet.com/article/log4j-flaw-now-state-backed-hackers-are-using-bug-as-part-of-attacks-warns-microsoft/) less than a week after Log4Shell's December 9 disclosure. 

**SEE:** [**Log4j zero-day flaw: What you need to know and how to protect yourself**](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/#link=%7B%22linkText%22:%22Log4j%20zero-day%20flaw:%20What%20you%20need%20to%20know%20and%20how%20to%20protect%20yourself%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

[According to a further analysis by Check Point](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/), APT35's Log4j work was sloppy and "obviously rushed", using a basic publicly available JNDI exploit kit (now removed from GitHub) for attacks that were easy to detect and attribute. 

After exploiting Log4j on public-facing systems, the group uses what Check Point describes it as 'a PowerShell-based modular backdoor' for persistence, communication with a command and control (C&C) server, and command execution for additional modules. 

The main module of the attacker's PowerShell framework validates network connections, enumerates characteristics about a compromised system, retrieves the C&C domain from a hardcoded URL, and takes, decrypts and executes subsequent modules. After receiving information about compromised systems, the C&C server either issues no command or instructs the module to execute other modules that are written as PowerShell scripts or C# code. 






Back and forth communication between target and C&C runs continuously to determine what subsequent modules should be submitted to the target, according to Check Point. 

Each of the additional modules are responsible for encrypting data, exfiltration via the web or an FTP server, and sending execution logs to a remote server. 

But each module has unique capabilities, such as one for listing installed applications, another for taking screenshots, and more for listing running processes, enumeration, and executing predefined commands from the C&C. A final "cleanup module" is dropped at the end of collection activity that removes evidence, such as running processes created by previously used modules.

"The modules sent by the C&C are executed by the main module, with each one reporting data back to the server separately," explains Check Point. 

"This C&C cycle continues indefinitely, which allows the threat actors to gather data on the infected machine, run arbitrary commands and possibly escalate their actions by performing a lateral movement or executing follow-up malware such as ransomware."

On the quality of the group's work, Check Point had few compliments because, unlike most advanced persistent threats, they don't bother changing tools and infrastructure for new attacks and are known for making operational security (OpSec) blunders.

"The group is famous in the cybersecurity community for the number of OpSec mistakes in their previous operations, and they tend not to put too much effort into changing their infrastructure once exposed," Check Point notes. 

The firm says there are similar coding styles between the PowerShell scripts used for Log4Shell and the ones that the group used in [Android spyware detailed by Google's Threat Analysis Group in October](https://www.zdnet.com/article/google-were-sending-out-lots-more-phishing-and-malware-attack-warnings-heres-why/). 

Despite the US Cybersecurity and Infrastructure Security Agency's (CISA) [confirmation it had seen no major breaches](https://www.zdnet.com/article/cisa-director-we-have-not-seen-significant-intrusions-from-log4j/) arise from Log4j exploitation, Microsoft [assesses the Log4Shell issue as a "high-risk" situation](https://www.zdnet.com/article/ransomware-warning-hackers-are-using-log4j-flaw-as-part-of-their-attacks-warns-microsoft/) because it's difficult for organizations to know which applications, devices and services are affected. CISA also warned that attackers that have exploited Log4j may be waiting for alert levels to drop before using new but undetected footholds in targets.  





## Tags:

#### Threatactor:
[[threatactor.name=APT3]] [[threatactor.name=Magic Hound]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=FTP]] [[action.malware.name=FTP]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[C&c]] [[Powershell]] [[Apt35]] [[Log4shell]] [[ZDNet]]

