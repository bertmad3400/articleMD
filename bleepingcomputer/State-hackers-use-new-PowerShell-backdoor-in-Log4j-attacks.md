# State hackers use new PowerShell backdoor in Log4j attacks
### Hackers believed to be part of the Iranian APT35 state-backed group (aka 'Charming Kitten' or 'Phosphorus') has been observed leveraging Log4Shell attacks to drop a new PowerShell backdoor.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/state-hackers-use-new-powershell-backdoor-in-log4j-attacks/
+ Date: 2022-01-11T18:17:45-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j___logo.jpg)

![Apache Log4j](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j___logo.jpg)


Hackers believed to be part of the Iranian APT35 state-backed group (aka 'Charming Kitten' or 'Phosphorus') has been observed leveraging Log4Shell attacks to drop a new PowerShell backdoor.


The modular payload can handle C2 communications, perform system enumeration, and eventually receive, decrypt, and load additional modules.


Log4Shell is an exploit for CVE-2021-44228, a critical remote code execution vulnerability in Apache Log4j disclosed in December.


According to researchers from Check Point, APT35 was among the first to leverage the vulnerability before targets had an opportunity to apply security updates, scanning for vulnerable systems mere days after its public disclosure.


Check Point, who has been following these attempts, attributes the exploit activity to APT35 as the threat actor's attacks were hastily set up using previously exposed infrastructure known to be used by the group.


However, as part of their research, the analysts also spotted something new in the form of a PowerShell modular backdoor named 'CharmPower.'


A modular backdoor for multiple tasks
-------------------------------------


The exploitation of CVE-2021-44228 results in running a PowerShell command with a base64-encoded payload, eventually fetching the 'CharmPower' module from an actor-controlled Amazon S3 bucket.



![Infection chain diagram on latest APT35 campaign](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/infection-chain(1).jpg)**Infection chain diagram on latest APT35 campaign**  
*Source: Check Point*
This core module can perform the following main functions:


* **Validate network connection** – Upon execution, the script waits for an active internet connection by making HTTP POST requests to google.com with the parameter hi=hi.
* **Basic system enumeration** – The script collects the Windows OS version, computer name, and the contents of a file Ni.txt in $APPDATA path; the file is presumably created and filled by different modules that will be downloaded by the main module.
* **Retrieve C&C domain** – The malware decodes the C&C domain retrieved from a hardcoded URL hxxps://s3[.]amazonaws[.]com/doclibrarysales/3 located in the same S3 bucket from where the backdoor was downloaded.
* **Receive, decrypt, and execute follow-up modules**.

The core module keeps sending HTTP POST requests to the C2 that either go unanswered or receive a Base64 string which initiates the downloading of an additional PowerShell or C# module.


'CharmPower' is responsible for decrypting and loading these modules, and these then establish an independent channel of communication with the C2.



![Decoding additional modules fetched by the C2](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/decoding-module.jpg)**Decoding additional modules fetched by the C2**  
*Source: Check Point*
The list of modules to be sent to the infected endpoint is generated automatically based on the basic system data retrieved by CharmPower during the reconnaissance phase.


The additional modules sent by the C2 are the following:


* **Applications** – Enumerates uninstall registry values and uses the "wmic" command to figure out which applications are installed on the infected system.
* **Screenshot** – Captures screenshots according to a specified frequency and uploads them to an FTP server using hardcoded credentials.
* **Process** – Grabs running processes by using the tasklist command.
* **System information** – Runs the "systeminfo" command to gather system information. Has many more commands but are commented out.
* **Command Execution** – Remote command execution module featuring Invoke-Expression, cmd, and PowerShell options.
* **Cleanup** – Module to remove all traces left in the compromised system, like registry and startup folder entries, files, and processes. It's dropped at the very end of the APT35 attacks.


![Cleanup module erasing all traces of activity](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Cleanup module erasing all traces of activity**  
*Source: Check Point*
Similarities with old backdoors
-------------------------------


[Check Point](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/) noticed similarities between 'CharmPower' and an Android spyware used by APT35 in the past, including implementing the same logging functions and using an identical format and syntax.


Also, the "Stack=Overflow" parameter in C2 communications is seen on both samples, which is a unique element only seen in APT35 tools.



![Same parameter used in both malware samples](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Same parameter used in both malware samples**  
*Source: Check Point*
These code similarities and infrastructure overlaps allowed Check Point to attribute the campaign to APT35.


'CharmPower' is an example of how quickly sophisticated actors can respond to the emergence of vulnerabilities like CVE-2021-44228 and put together code from previously exposed tools to create something potent and effective that can go past security and detection layers.





## Tags:

#### Threatactor:
[[threatactor.name=APT3]] [[threatactor.name=Magic Hound]] [[threatactor.name=Magic Hound]] [[threatactor.name=Magic Hound]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=FTP]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Systeminfo]] [[action.malware.name=Systeminfo]] [[action.malware.name=Tasklist]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Apt35]] [[Powershell]] [[C2]] [[Cve-2021-44228]] [[Bleeping Computer]]
#### urls
hxxps://s3.amazonaws.com/doclibrarysales/3
#### CVE's
[[CVE-2021-44228]]

