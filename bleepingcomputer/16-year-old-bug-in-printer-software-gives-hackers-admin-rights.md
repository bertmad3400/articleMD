# 16-year-old bug in printer software gives hackers admin rights
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/16-year-old-bug-in-printer-software-gives-hackers-admin-rights/)
+ Date: July 20, 2021
+ Author: Sergiu Gatlan


## Article:
![16-year-old bug in printer software gives hackers admin rights](https://www.bleepstatic.com/content/hl-images/2021/07/19/HP-Printer-Logo.jpg)


A 16-year-old security vulnerability found in an HP, Xerox, and Samsung printers driver allows attackers to gain admin rights on systems using the vulnerable driver software.


"This high severity vulnerability, which has been present in HP, Samsung, and Xerox printer software since 2005, affects hundreds of millions of devices and millions of users worldwide," according to a [SentinelOne report](https://s1.ai/HP-Printer-CVE) published today and shared with BleepingComputer in advance.



The security flaw tracked as [CVE-2021-3438](https://nvd.nist.gov/vuln/detail/CVE-2021-3438) is a buffer overflow in the **SSPORT.SYS** driver for specific printer models that could lead to a local escalation of user privileges.


As the researchers discovered, the buggy driver automatically gets installed with the printer software and will be loaded by Windows after each system reboot.


This makes it the perfect target for attackers who need an easy way to escalate privileges, since the bug can be abused even when the printer is not connected to the targeted device.



![Vulnerable driver set to load on system boot](https://www.bleepstatic.com/images/news/u/1109292/2021/Vulnerable%20driver%20set%20to%20load%20on%20system%20boot.png)*Vulnerable driver set to load on system boot (SentinelOne)*
Successful exploitation requires local user access which means that threat actors will need to first get a foothold on the targeted devices.


Once this is achieved, they can abuse the security bug to escalate privileges in low complexity attacks without requiring user interaction.


The result is that attackers with basic user privileges can elevate their privileges to SYSTEM and run code in kernel mode, potentially bypassing security products that would block their attacks or the delivery of additional malicious payloads.


"Successfully exploiting a driver vulnerability might allow attackers to potentially install programs, view, change, encrypt or delete data, or create new accounts with full user rights," SentinelOne explains.


"While we haven't seen any indicators that this vulnerability has been exploited in the wild up till now, with hundreds of millions of enterprises and users currently vulnerable, it is inevitable that attackers will seek out those that do not take the appropriate action."


Users urged to update ASAP
--------------------------


A list of affected printer models using the vulnerable driver can be found in [HP's security advisory](https://support.hp.com/us-en/document/ish_3900395-3833905-16/hpsbpi03724) and this [Xerox security mini bulletin](https://securitydocs.business.xerox.com/wp-content/uploads/2021/05/cert_Security_Mini_Bulletin_XRX21K_for_B2XX_PH30xx_3260_3320_WC3025_32xx_33xx.pdf).


HP, Xerox, and Samsung enterprise and home customers are urged to apply the patches provided by the two vendors as soon as possible.


"Some Windows machines may already have this driver without even running a dedicated installation file, since this driver comes with Microsoft Windows via Windows Update," the researchers added.


Earlier this year, SentinelOne researchers found a [12-year-old privilege escalation bug in Microsoft Defender Antivirus](https://www.bleepingcomputer.com/news/security/12-year-old-windows-defender-bug-gives-hackers-admin-rights/) (formerly Windows Defender) that can let attackers gain admin rights on unpatched Windows systems.


[Microsoft Defender Antivirus](https://www.microsoft.com/en-us/windows/comprehensive-security) is the default anti-malware solution on [more than 1 billion systems](https://news.microsoft.com/bythenumbers/en/windowsdevices) running Windows 10 per Microsoft's stats.




#### Tags:
[[Windows]] [[SentinelOne]] [[Microsoft]] [[Samsung]] [[Bleeping Computer]]
