# How to fix printers asking for admins creds after PrintNightmare patch
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/how-to-fix-printers-asking-for-admins-creds-after-printnightmare-patch/)
+ Date: September 17, 2021
+ Author: Sergiu Gatlan


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/09/17/Windows-crack.jpg)


Some printers will request administrator credentials every time users try to print in Windows Point and Print environments due to a known issue caused by KB5005033 or later security updates addressing the PrintNightmare vulnerability.


This happens because, after installing these [PrintNightmare](https://www.bleepingcomputer.com/tag/printnightmare/) patches, only administrators are allowed to install or update drivers via Point and Print.


The request for admin credentials is triggered automatically in environments where the print server has a newer driver than the client attempting to print.


"Certain printers in some environments using Point and Print might receive a prompt saying, 'Do you trust this printer' and requiring administrator credentials to install every time an app attempts to print to a print server or a print client connects to a print server," [Microsoft explains](https://docs.microsoft.com/en-us/windows/release-health/status-windows-10-21h1#1692msgdesc).


"This is caused by a print driver on the print client and the print server using the same filename, but the server has a newer version of the file."


The complete list of impacted client and server platforms includes:


* Client: Windows 10, version 21H1; Windows 10, version 20H2; Windows 10, version 2004; Windows 10, version 1909; Windows 10, version 1809; Windows 10 Enterprise LTSC 2019; Windows 10 Enterprise LTSC 2016; Windows 10, version 1607; Windows 10 Enterprise 2015 LTSB; Windows 8.1; Windows 7 SP1
* Server: Windows Server 2022; Windows Server, version 20H2; Windows Server, version 2004; Windows Server, version 1909; Windows Server, version 1809; Windows Server 2019; Windows Server 2016; Windows Server 2012 R2; Windows Server 2012; Windows Server 2008 R2 SP1; Windows Server 2008 SP2


If you're not using [Point and Print](https://docs.microsoft.com/windows-hardware/drivers/print/introduction-to-point-and-print), you should not be affected by this issue, and you'll also be protected by default after installing security updates released since August 10.


Workaround available
--------------------


Microsoft added that the known issue could be solved by ensuring that the same printer driver version is installed on the print server and all clients within your environment.


"Verify that you are using the latest drivers for all your printing devices and where possible, use the same version of the print driver on the print client and print server," the company said.


If updating printer drivers across your environment does not fix these printing problems, you should reach out to your printer manufacturer (OEM) support team.


Additional information about this issue is available in the [Frequently asked questions section](https://support.microsoft.com/en-us/topic/kb5005652-manage-new-point-and-print-default-driver-installation-behavior-cve-2021-34481-873642bf-2634-49c5-a23b-6d8e9a302872#:~:text=Frequently%20asked%20questions) of the KB5005652 support document.


In related news, according to user reports, PrintNightmare security updates released as part of this month's Patch Tuesday are also [breaking network printing](https://www.bleepingcomputer.com/news/security/new-windows-security-updates-break-network-printing/).


Windows administrators have been experiencing wide-scale network printing problems after installing the [fix for the last remaining PrintNightmare vulnerability](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-remaining-windows-printnightmare-vulnerabilities/).


BleepingComputer has reached out to Microsoft with questions about these ongoing issues but has not heard back.




#### Tags:
[[Windows]] [[PrintNightmare]] [[Server,]] [[Microsoft]] [[Bleeping Computer]]
