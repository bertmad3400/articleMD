# New Windows PrintNightmare zero-days get free unofficial patch
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/new-windows-printnightmare-zero-days-get-free-unofficial-patch/)
+ Date: August 5, 2021
+ Author: Lawrence Abrams


## Article:
![Windows](https://www.bleepstatic.com/content/hl-images/2021/05/17/0_Windows-headpic.jpg)


A free unofficial patch has been released to protect Windows users from all new PrintNightmare zero-day vulnerabilities discovered since June.


Technical details and a proof-of-concept (PoC) exploit for a new [Windows print spooler vulnerability named 'PrintNightmare'](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/)  (CVE-2021-34527) was accidentally disclosed in June.


This vulnerability allows remote code execution and local privilege escalation by installing malicious printer drivers.


While Microsoft [released a security update](https://www.bleepingcomputer.com/news/security/microsoft-pushes-emergency-update-for-windows-printnightmare-zero-day/) for the remote code execution portion, researchers quickly bypassed the local privilege elevation component. Since then, Security researcher and Mimikatz creator [Benjamin Delpy](https://twitter.com/gentilkiwi) has been devising [further vulnerabilities targeting the print spooler](https://www.bleepingcomputer.com/news/microsoft/windows-print-nightmare-continues-with-malicious-driver-packages/) that remain unpatched.


These are critical vulnerabilities as they [allow anyone to gain SYSTEM privileges](https://www.bleepingcomputer.com/news/microsoft/remote-print-server-gives-anyone-windows-admin-privileges-on-a-pc/) on a local device, even a Domain Controller, simply by connecting to a remote Internet-accessible print server and installing a malicious print driver.


Once a threat actor gains SYSTEM privileges, it is game over for the system. If this is done on a Domain Controller, then the threat actor now effectively controls the Windows Domain.


Free PrintNightmare micropatch released
---------------------------------------


Mitigations for the zero-day PrintNightmare vulnerabilities are already available through the '[PackagePointAndPrintServerList](https://www.kb.cert.org/vuls/id/383432)' group policy, which allows you to specify a white list of approved print servers that can be used to install a print driver.


Enabling this policy, along with a fake server name, will effectively block Delpy's exploits as the print server will be blocked.


However, for those who want to install a patch and not try to understand advisories and fiddle with group policies, Mitja Kolsek, co-founder of the [0patch micropatching service](https://0patch.com/), has released a free micropatch that can be used to fix all known PrintNightmare vulnerabilities.


"We therefore decided to implement the group policy-based workaround as a micropatch, blocking Point and Print printer driver installation from untrusted servers. This workaround employs Group Policy settings: the "Only use Package Point and Print" first requires every printer driver is in form of a signed package, while the "Package Point and print - Approved servers" limits the set of servers from which printer driver packages are allowed to be installed." Kolsek explains in a [blog post](http://blog.0patch.com/2021/08/free-micropatches-for-malicious-printer.html).


"These settings are configurable via registry. Our patch modifies function DoesPolicyAllowPrinterConnectionsToServer in win32spl.dll such that it believes that PackagePointAndPrintOnly and PackagePointAndPrintServerList values exist and are set to 1, which enables both policies and keeps the list of approved servers empty."


You need to register a 0patch account and then install an agent on your Windows device to install the patch. Once installed, 0patch will automatically protect you from the PrintNightmare vulnerability and other unpatched bugs.



![0patch protecting against the PrintNightmare vulnerabilities](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/p/printnightmare/0patch/0patch-patches-installed.jpg)**0patch protecting against the PrintNightmare vulnerabilities**  
*Source: BleepingComputer*
In a test by BleepingComputer, once installed, if you attempt to install Delpy's malicious PrintNightmare driver, a message will appear stating that a policy has blocked the computer from connecting to the print queue, as shown below.



![](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/p/printnightmare/0patch/printnightmare-blocked.jpg)**0patch blocking PrintNightmare vulnerability**  
*Source: BleepingComputer*
While 0patch is an essential tool for blocking unpatched vulnerabilities, Delpy says that, in this particular case, [enabling the group policies](http://www.kb.cert.org/vuls/id/383432) that blocks exploitation of all known PrintNightmare bugs might be a better approach.


"If you push binaries to a computer to push settings … you can also push settings," Delpy told BleepingComputer.


"Doing so avoids altering process in memory, always a dangerous stuff that security product don't like (and MS does not support...)."




#### Tags:
[[PrintNightmare]] [[0patch]] [[Delpy]] [[Windows]] [[Bleeping Computer]]
