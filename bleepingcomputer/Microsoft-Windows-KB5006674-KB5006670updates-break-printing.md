# Microsoft: Windows KB5006674, KB5006670 updates break printing
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-kb5006674-kb5006670-updates-break-printing/)
+ Date: October 30, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft: Installing Windows KB5006674 breaks network printing](https://www.bleepstatic.com/content/hl-images/2021/09/01/windows-11-glow-glass.jpg)


Microsoft says Windows customers are experiencing issues with network printing after installing the Windows 11 [KB5006674](https://support.microsoft.com/help/5006674) and Windows 10 [KB5006670](https://support.microsoft.com/help/5006670) updates issued with this month's Patch Tuesday, on October 12.


Users attempting to connect to printers shared on Windows print servers might encounter multiple errors preventing them from printing over the network.


The errors Windows print clients will encounter after deploying KB5006674 include:


* **0x000006e4** (RPC\_S\_CANNOT\_SUPPORT)
* **0x0000007c** (ERROR\_INVALID\_LEVEL)
* **0x00000709** (ERROR\_INVALID\_PRINTER\_NAME)


The complete list of Windows platforms impacted by this issue includes:


* Client: Windows 11, version 21H2; Windows 10, version 21H1; Windows 10, version 20H2; Windows 10, version 2004; Windows 10, version 1909; Windows 10, version 1809; Windows 10 Enterprise LTSC 2019; Windows 10, version 1607; Windows 8.1; Windows 7 SP1
* Server: Windows Server 2022; Windows Server, version 20H2; Windows Server, version 2004; Windows Server, version 1909; Windows Server, version 1809; Windows Server 2008 SP2


As Redmond explains, this known issue affecting printing on both client and server Windows platforms is specific to printer servers which are more commonly found in enterprise environments.


Microsoft said it's working on finding a solution to allow print clients to establish RPC packet privacy connections to Windows print servers using RPC over SMB.


Users plagued by printing problems the last two weeks
-----------------------------------------------------


Windows 10 admins and users have been reporting widescale network printing issues in a [14-page forum topic](https://www.bleepingcomputer.com/forums/t/759880/kb5006670-network-printer-problems-again-this-month/) at BleepingComputerfor for the last two weeks since the October Patch Tuesday updates have been released.


While recounting their frustration and attempts to deal with the printing bugs, they came to the same conclusion: uninstalling the October cumulative updates resolves the printing problem.


Since then, the issues have gotten so bad that Windows admins have [resorted to replacing Windows DLLs](https://www.bleepingcomputer.com/forums/t/759880/kb5006670-network-printer-problems-again-this-month/?p=5269603) with older versions to re-enable printing.


The DLLs that admins are replacing to fix printing are localspl.dll, win32spl.dll, and spoolsv.exe.


While this approach removes fixes for Print Spooler vulnerabilities, it does avoid uninstalling the cumulative updates, which would get rid of all October security updates in the process.


Microsoft provides a workaround
-------------------------------


Customers impacted by these printing problems can now use an official workaround provided by Microsoft to fix the issue.


The steps should ONLY be taken on affected print servers that meet the following prerequisite: "print clients must have installed a Windows update released on or after January 2021 before the print server has installed" the October 2021 updates.


If the workaround requirements are met, Microsoft asks customers to "ensure that network security and VPN solutions allow print clients to establish RPC over TCP connections to print server over the following port range:"


* Default start port: 49152
* Default end port: 65535
* Port Range: 16384 ports


Redmond also provides the following articles for additional guidance:


* [How to configure RPC to use certain ports and how to help secure those ports by using IPsec](https://support.microsoft.com/topic/how-to-configure-rpc-to-use-certain-ports-and-how-to-help-secure-those-ports-by-using-ipsec-2a94b798-063a-479a-8452-9cf07ac613d9).
* [The default dynamic port range for TCP/IP has changed since Windows Vista and in Windows Server 2008](https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/default-dynamic-port-range-tcpip-chang)


Before disclosing this new issue, Microsoft said it fixed other Windows 11 known issues [causing printer installation fails](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-new-windows-11-printer-installation-issues/) and [prompts for admin credentials before every attempt to print](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-11-bug-may-only-allow-admins-to-print/) in enterprise environments.




#### Tags:
[[Windows]] [[Microsoft]] [[Server,]] [[RPC]] [[admins]] [[workaround]] [[Bleeping Computer]]
