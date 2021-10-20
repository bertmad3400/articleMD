# New PurpleFox botnet variant uses WebSockets for C2 communication
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-purplefox-botnet-variant-uses-websockets-for-c2-communication/)
+ Date: October 20, 2021
+ Author: Bill Toulas


## Article:
![PurpleFox](https://www.bleepstatic.com/content/hl-images/2021/10/20/purplefox.png)


The PurpleFox botnet has refreshed its arsenal with new vulnerability exploits and dropped payloads, now also leveraging WebSockets for C2 bidirectional communication.


Although it's mainly based in China, the [PurpleFox botnet](https://www.bleepingcomputer.com/news/security/purple-fox-malware-worms-its-way-into-exposed-windows-systems/) still has a global presence through hundreds of compromised servers.


Its activity starts with the execution of a PowerShell command that downloads a malicious payload from the specified URL, pointing to an available C2 server.


The payload used in recent campaigns tracked by researchers at [Trend Micro](https://www.trendmicro.com/en_us/research/21/j/purplefox-adds-new-backdoor-that-uses-websockets.html) is a long script that comprises three privilege escalation components.


These target Windows 7 to Windows 10 systems, but are limited to 64-bit systems only.


The flaws that are exploited by the latest PurpleFox variants are the following:


* Windows 7/Windows Server 2008 - CVE-2020-1054, CVE-2019-0808
* Windows 8/Windows Server 2012 - CVE-2019-1458
* Windows 10/Windows Server 2019 - CVE-2021-1732


PurpleFox detects the host system, selects the appropriate exploit, and then uses the PowerSploit module to load it.


An MSI package is also initiated from an admin-level process without requiring any user interaction, checking for older PurpleFox installations and replacing their components with new ones.


 


The backdoor that is installed on the host system is a DLL file obfuscated with the VMProtect file compressing utility.



![PurpleFox backdoor installation process](https://www.bleepstatic.com/images/news/u/1220909/Security/backdoor.png)**PurpleFox backdoor installation process**  

Source: TrendMicro
The malware also uses a rootkit driver that hides its files, registry keys, and processes, reducing the chances of being detected on the compromised server.


Opening a WebSocket channel and keeping it alive
------------------------------------------------


A new .NET backdoor retrieved from recent campaigns is dropped days after the initial intrusion to leverage WebSockets for C2 communications.


This component is responsible for setting up the communication configuration as well as for the initialization of cryptographic functions.


The use of WebSockets for communications is something unusual in the malware space, but PurpleFox shows that it can be very effective nonetheless.


The exchanged messages between the infected machine and the selected C2 server begin with negotiations for a session RSA encryption key, but even this first exchange is AES-encrypted using a default key.



![AES-encrypted exchange between the machine and the C2](https://www.bleepstatic.com/images/news/u/1220909/Security/AES%20encryption.png)**AES-encrypted exchange between the machine and the C2**  

Source: TrendMicro
By sending "keepalive" messages, the TCP connection is maintained for as long as needed.  


The list of WebSocket commands observed by TrendMicro is extensive, and although there are some discrepancies between different variants, the table below summarizes them all.



![Overview of WebSocket commands](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Overview of WebSocket commands**  

Source: TrendMicro
Currently, PurpleFox is still active and there’s a notable number of C&C servers controlling the WebSocket clients.


By doing some profiling of the targets, TrendMicro reports the most notable activity hotspots to be in the US, Turkey, UAE, Iraq, and Saudi Arabia.




#### Tags:
[[PurpleFox]] [[C2]] [[Windows]] [[TrendMicro]] [[WebSocket]] [[WebSockets]] [[Source:]] [[Bleeping Computer]]
