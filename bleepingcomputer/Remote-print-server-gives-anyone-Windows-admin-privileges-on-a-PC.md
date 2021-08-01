# Remote print server gives anyone Windows admin privileges on a PC
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/remote-print-server-gives-anyone-windows-admin-privileges-on-a-pc/)
+ Date: July 31, 2021
+ Author: Lawrence Abrams


## Article:
![PrintNightmare](https://www.bleepstatic.com/content/hl-images/2021/06/30/Printer.jpg)


A researcher has created a remote print server allowing any Windows user with limited privileges to gain complete control over a device simply by installing a print driver.


In June, a security researcher accidentally revealed a zero-day Windows print spooler vulnerability known as [PrintNightmare](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/) (CVE-2021-34527) that allowed remote code execution and elevation of privileges.


While Microsoft [released a security update](https://www.bleepingcomputer.com/news/security/microsoft-pushes-emergency-update-for-windows-printnightmare-zero-day/) to fix the vulnerability, researchers quickly figured out ways to [bypass the patch](https://www.bleepingcomputer.com/news/microsoft/microsofts-incomplete-printnightmare-patch-fails-to-fix-vulnerability/) under certain conditions.


Since then, researchers have continued to devise new ways to exploit the vulnerability, with one researcher creating an Internet-accessible print server allowing anyone to open a command prompt with administrative privileges.


Now anyone can get Windows SYSTEM privileges
--------------------------------------------


Security researcher and Mimikatz creator [Benjamin Delpy](https://twitter.com/gentilkiwi) has been at the forefront of continuing PrintNightmare research, releasing multiple bypasses and updates to exploits through [specially crafted printer drivers](https://www.bleepingcomputer.com/news/microsoft/windows-print-nightmare-continues-with-malicious-driver-packages/) and by abusing Windows APIs.


To illustrate his research, Delpy created an Internet-accessible print server at \\printnightmare[.]gentilkiwi[.]com that installs a print driver and launches a DLL with SYSTEM privileges.


Initially, the launched DLL would write a log file to the C:\Windows\System32 folder, which should only be writable by users with elevated privileges.




> 
> Want to test [#printnightmare](https://twitter.com/hashtag/printnightmare?src=hash&ref_src=twsrc%5Etfw) (ep 4.x) user-to-system as a service?  
> 
> (POC only, will write a log file to system32)  
>   
> 
> connect to \\<https://t.co/6Pk2UnOXaG> with  
> 
> - user: .\gentilguest  
> 
> - password: password  
>   
> 
> Open 'Kiwi Legit Printer - x64', then 'Kiwi Legit Printer - x64 (another one)' [pic.twitter.com/zHX3aq9PpM](https://t.co/zHX3aq9PpM)
> 
> 
> — Benjamin Delpy (@gentilkiwi) [July 17, 2021](https://twitter.com/gentilkiwi/status/1416429860566847490?ref_src=twsrc%5Etfw)


As some people did not believe his initial print driver could elevate privileges, on Tuesday, Delpy modified the driver to launch a SYSTEM command prompt instead.


This new method effectively allows anyone, including threat actors, to get administrative privileges simply by installing the remote print driver. Once they gain administrative rights on the machine, they can run any command, add users, or install any software, effectively giving them complete control over the system.


This technique is especially useful for threat actors who breach networks for the deployment of ransomware as it allows quick and easy access to administrative privileges on a device that helps them spread laterally through a network.


BleepingComputer installed Delpy's print driver on a fully patched Windows 10 21H1 PC as a user with 'Standard' (limited) privileges to test this technique.


As you can see, once we installed the printer and disabled Windows Defender, which detects the malicious printer, a command prompt was opened that gave us full SYSTEM privileges on the computer.



When we asked Delpy if he was concerned that threat actors were abusing his print server, he told us that one of the driving reasons he created it is to pressure "Microsoft to make some priorities" into fixing the bug.


He also said that it's impossible to determine what IP addresses belong to researchers or threat actors. However, he has firewalled Russian IP addresses that appeared to be abusing the print servers.


Mitigating the new printer vulnerability
----------------------------------------


As anyone can abuse this remote print server on the Internet to get SYSTEM level privileges on a Windows device, Delpy has offered several ways to mitigate the vulnerability.


These methods are outlined in a [CERT advisory](https://www.kb.cert.org/vuls/id/383432) written by [Will Dormann](https://twitter.com/wdormann), a vulnerability analyst for CERT/CC.


### Option 1: Disable the Windows print spooler


The most extreme way to prevent all PrintNightmare vulnerabilities is to disable the Windows Print spooler using the following commands.


However, using this mitigation will prevent the computer from being able to print.


### Option 2: Block RPC and SMB traffic at your network boundary


As Delpy's public exploit uses a remote print server, you should block all RPC Endpoint Mapper (`135/tcp`) and SMB (`139/tcp` and `445/tcp`) traffic at your network boundary.


However, Dormann warns that blocking these protocols may cause existing functionality to no longer work as expected.


"Note that blocking these ports on a Windows system may prevent expected capabilities from functioning properly, especially on a system that functions as a server," explained Dormann.


### Option 3: Configure PackagePointAndPrintServerList


The best way to prevent a remote server from exploiting this vulnerability is to restrict Point and Print functionality to a list of approved servers using the 'Package Point and print - Approved servers' group policy.



![Package Point and print - Approved servers group policy](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/p/print-spooler-queue-specific/approved-servers-policyt.jpg)**Package Point and print - Approved servers group policy**
This policy prevents non-administrative users from installing print drivers using Point and Print unless the print server is on the approved list. 


Using this group policy will provide the best protection against the known exploit but will not prevent a threat actor from taking over an allowed print server with malicious drivers.


Delpy has warned that this is not the end of Windows print spooler abuse, especially with new research being revealed this week at both the [Black Hat](https://www.blackhat.com/us-21/briefings/schedule/index.html#diving-into-spooler-discovering-lpe-and-rce-vulnerabilities-in-windows-printer-23315) and [Def Con](https://defcon.org/html/defcon-29/dc-29-speakers.html#baines) security conferences.




#### Tags:
[[Windows]] [[Delpy]] [[privileges.]] [[PrintNightmare]] [[However,]] [[Bleeping Computer]]
