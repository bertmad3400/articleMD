# 16-Year-Old HP Printer-Driver Bug Impacts Millions of Windows Machines
### The bug could allow cyberattackers to bypass security products, tamper with data and run code in kernel mode.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167944)
+ Date: July 20, 2021  9:31 am
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/02081934/printer.jpg)
Researchers have released technical details on a high-severity privilege-escalation flaw in HP printer drivers (also used by Samsung and Xerox), which impacts hundreds of millions of Windows machines.


If exploited, cyberattackers could bypass security products; install programs; view, change, encrypt or delete data; or create new accounts with more extensive user rights.


The bug (CVE-2021-3438) has lurked in systems for 16 years, researchers at SentinelOne said, but was only uncovered this year. It carries an 8.8 out of 10 rating on the CVSS scale, making it high-severity.



According to researchers, the vulnerability exists in a function inside the driver that accepts data sent from User Mode via Input/Output Control (IOCTL); it does so without validating the size parameter. As the name suggests, IOCTL is a system call for device-specific input/output operations.


“This function copies a string from the user input using ‘strncpy’ with a size parameter that is controlled by the user,” according to SentinelOne’s analysis, released on Tuesday. “Essentially, this allows attackers to overrun the buffer used by the driver.”


Thus, unprivileged users can elevate themselves into a SYSTEM account, allowing them to run code in kernel mode, since the vulnerable driver is locally available to anyone, according to the firm.


The [printer-based attack vector](https://threatpost.com/old-printer-vulnerabilities-die-hard/139318/) is perfect for cybercriminals, according to SentinelOne, since printer drivers are essentially ubiquitous on Windows machines and are automatically loaded on every startup.


“Thus, in effect, this driver gets installed and loaded without even asking or notifying the user,” explained the researchers. “Whether you are configuring the printer to work wirelessly or via a USB cable, this driver gets loaded. In addition, it will be loaded by Windows on every boot. This makes the driver a perfect candidate to target since it will always be loaded on the machine even if there is no printer connected.”


Weaponizing the bug might require chaining other vulnerabilities to achieve initial access into an environment. So far, no in-the-wild attacks have been observed.


“While we haven’t seen any indicators that this vulnerability has been exploited in the wild up till now, with hundreds of millions of enterprises and users currently vulnerable, it is inevitable that attackers will seek out those that do not take the appropriate action,” researchers warned.


**How to Fix the HP Printer-Driver Bug**
----------------------------------------


Since the bug has existed since 2005, it impacts a very long list of printer models, researchers noted; affected models and associated patches can be [found here](https://support.hp.com/us-en/drivers/printers) and [here](https://securitydocs.business.xerox.com/wp-content/uploads/2021/05/cert_Security_Mini_Bulletin_XRX21K_for_B2XX_PH30xx_3260_3320_WC3025_32xx_33xx.pdf).


Device-driver vulnerabilities are not uncommon, so SentinelOne also suggested reducing the attack surface with some best practices, including enforcing strong access control lists (ACLs), which control access to packages, folders, and other elements (such as services, document types and specifications) at the group level. And, it’s a good idea to verify user input and not expose a generic interface to kernel mode operations, they added.


“While HP is releasing a patch (a fixed driver), it should be noted that the certificate has not yet been revoked at the time of writing,” according to SentinelOne. “This is not considered best practice since the vulnerable driver can still be used in bring-your-own-vulnerable-driver (BYOVD) attacks.”


Some Windows machines may already have the vulnerable driver without even running a dedicated installation file, researchers warned, since it comes with Microsoft Windows via Windows Update.


“This high-severity vulnerability affects hundreds of millions of devices and millions of users worldwide,” according to SentinelOne. “The impact this could have on users and enterprises that fail to patch is far-reaching and significant.”


SentinelOne has found previous vulnerabilities such as a group affecting Dell’s firmware update driver that [remained hidden for 12 years](https://threatpost.com/dell-kernel-privilege-bugs/165843/). In that case, revealed in May, five high-severity security flaws in were found to impact potentially hundreds of millions of Dell desktops, laptops, notebooks and tablets. They could allow the ability to bypass security products, execute code and pivot to other parts of the network for lateral movement, according to SentinelLabs.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 




#### Tags:
[[SentinelOne]] [[Windows]] [[high-severity]] [[ThreatPost]]
