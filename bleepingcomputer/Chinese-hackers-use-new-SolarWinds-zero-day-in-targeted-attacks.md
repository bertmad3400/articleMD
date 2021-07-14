# Chinese hackers use new SolarWinds zero-day in targeted attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/chinese-hackers-use-new-solarwinds-zero-day-in-targeted-attacks/)
+ Date: July 13, 2021
+ Author: Lawrence Abrams


## Article:
![Microsoft Defender](https://www.bleepstatic.com/content/hl-images/2021/07/07/Microsoft-Defender.jpg)


China-based hackers known to target US defense and software companies are now targeting organizations using a vulnerability in the SolarWinds Serv-U FTP server.


Today, SolarWinds released a security update for [a zero-day vulnerability in Serv-U FTP](https://www.bleepingcomputer.com/news/security/solarwinds-patches-critical-serv-u-vulnerability-exploited-in-the-wild/) servers that allow remote code execution when SSH is enabled.



According to SolarWinds, this vulnerability was disclosed by Microsoft, who saw a threat actor actively exploiting it to execute commands on vulnerable customer's devices.


Tonight, Microsoft revealed that the attacks are attributed with high confidence to a China-based threat group tracked as 'DEV-0322.'


"This activity group is based in China and has been observed using commercial VPN solutions and compromised consumer routers in their attacker infrastructure," says a new blog post by the Microsoft Threat Intelligence Center.


Microsoft says the DEV-0322 hacking group has previously targeted entities in the US Defense Industrial Base Sector and software companies.


"The DIB Sector is the worldwide industrial complex that enables research and development (R&D), as well as design, production, delivery, and maintenance of military weapons systems, subsystems, and components or parts, to meet U.S. military requirements," explains a [CISA document](https://www.cisa.gov/sites/default/files/publications/nipp-ssp-defense-industrial-base-2010-508.pdf) describing the DIB sector.


Attacks detected by Microsoft 365 Defender telemetry
----------------------------------------------------


Microsoft says they first learned of the attacks after Microsoft 365 Defender telemetry showed a normally harmless Serv-U process spawning anomalous malicious processes.


Some of the commands executed through the remote code execution vulnerability are listed below.


"We observed DEV-0322 piping the output of their *cmd.exe* commands to files in the Serv-U *\Client\Common\*folder, which is accessible from the internet by default, so that the attackers could retrieve the results of the commands," Microsoft explains in their [blog post](https://www.microsoft.com/security/blog/2021/07/13/microsoft-discovers-threat-actor-targeting-solarwinds-serv-u-software-with-0-day-exploit/).


Other commands would add a global admin user to the Serv-U FTP server configuration or launch batch files and scripts to likely install malware on the devices for persistence and remote access.


Microsoft says Serv-U users can check if their devices were compromised by checking the Serv-U *DebugSocketLog.txt* log file and looking for exception messages.


A "*C0000005; CSUSSHSocket::ProcessReceive*" exception could indicate that the threat actors attempted to exploit the Serv-U server, but the exception could be shown for other reasons as well.


An example exception seen in logs is displayed below.


Other signs that a device may have been compromised are:


* Recently created .txt files under the Client\Common\ folder.
* Serv-U spawned processes for mshta.exe, powershell.exe, cmd.exe, and processes running from C:\Windows\temp.
* Unrecognized global users in the Serv-U configuration.


BleepingComputer has reached out to Microsoft to learn more about what commands or malware were executed by the batch file and scripts but has not heard back.


*Update 7/14/21: Corrected article to indicate 'DEV-0322' is historically known to target Defense orgs.*




#### Tags:
[[Serv-U]] [[Microsoft]] [[exe]] [[SolarWinds]] [[FTP]] [[Bleeping Computer]]
