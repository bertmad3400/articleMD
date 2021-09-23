# FamousSparrow APT Wings in to Spy on Hotels, Governments
### A custom “SparrowDoor” backdoor has allowed the attackers to collect data from targets around the globe.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174948)
+ Date: September 23, 2021  10:08 am
+ Author: Tara Seals


## Article:
A cyberespionage group dubbed “FamousSparrow” by researchers has taken flight, targeting hotels, governments and private organizations around the world with a custom backdoor called, appropriately, “SparrowDoor.” It’s one of the advanced persistent threats (APTs) that targeted the ProxyLogon vulnerabilities earlier this year, according to ESET, though its activity has only recently come to light.


According to the firm, the backdoor’s malicious actions include the ability to: rename or delete files; create directories; shut down processes; send information such as file attributes, file size and file write time; exfiltrate the content of a specified file; write data to a specified file; or establish an interactive reverse shell. There’s also a kill switch to remove persistence settings and all SparrowDoor files from the victim machines.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“The targeting, which includes governments worldwide, suggests that FamousSparrow’s intent is espionage,” researchers noted.


**ProxyLogon Exploits and More**
--------------------------------


The ProxyLogon remote code execution (RCE) bug was disclosed in March, and was used by [more than 10 APT groups](https://threatpost.com/microsoft-exchange-cyberattacks-one-click-fix/164817/) to establish access via shellcode to Exchange mail servers worldwide in a flurry of attacks. According to ESET telemetry, FamousSparrow started to exploit the vulnerabilities the day following Microsoft’s release of a patch for the problem.


In FamousSparrow’s case, it used the bug to deploy SparrowDoor, which has been seen in other attacks (many of them against hotels), according to ESET. These additional campaigns have occurred both before and after ProxyLogon, and date back to August 2019, researchers noted.


Where they were able to determine the initial compromise vector, researchers found that FamousSparrow’s go-to *modus operandi* appears to be the exploitation of vulnerable internet-facing web applications.


“We believe FamousSparrow exploited known remote code-execution vulnerabilities in Microsoft Exchange (including ProxyLogon in March 2021), Microsoft SharePoint and Oracle Opera (business software for hotel management), which were used to drop various malicious samples,” according to ESET researchers.


They added, “This is another reminder that it is critical to patch internet-facing applications quickly, or, if quick patching is not possible, to not expose them to the internet at all.”


**The SparrowDoor Espionage Tool**
----------------------------------


Once a target is compromised, FamousSparrow infects the victim with a range of custom tools, according to [ESET’s analysis](https://www.welivesecurity.com/2021/09/23/famoussparrow-suspicious-hotel-guest/), released on Thursday. These include:


The loader installs SparrowDoor via [DLL search order hijacking](https://attack.mitre.org/techniques/T1574/001/), researchers noted.


“The legitimate executable, Indexer.exe, requires the library K7UI.dll to operate,” they explained. “Therefore, the OS looks for the DLL file in directories in the prescribed load order. Since the directory where the Indexer.exe file is stored is at the top priority in the load order, it is exposed to DLL search-order hijacking. And that is exactly how the malware gets loaded.”


Persistence is set through the registry Run key and a service that’s created and started using XOR-encrypted configuration data hardcoded in the binary, according to the writeup. Then, the malware establishes encrypted TLS connections to a command-and-control (C2) server on port 433, which can be proxied or not.


The malware then achieves privilege escalation by adjusting the access token of the SparrowDoor process to enable SeDebugPrivilege, which is a legitimate Windows utility that’s used to debug processes on computers other than one’s own. An attacker with SeDebugPrivilege can “debug processes owned by System, at which point they can inject code into the process and perform the logical equivalent of net localgroup administrators anybody/add, thereby elevating themselves (or anybody else) to administrator,” according to a [Microsoft writeup](https://devblogs.microsoft.com/oldnewthing/20080314-00/?p=23113).


After that, SparrowDoor sniffs out and sends the victim’s local IP address, a Remote Desktop Services session ID associated with the backdoor process, username and computer name to the C2, and waits for commands in return, in order to start its espionage campaign.


FamousSparrow mainly targets hotels, but ESET observed targets in other sectors, including governments, international organizations, engineering companies and law firms. The group has really come out of its shell, as it were: Attacks have been scattered globally, aimed at targets in Brazil, Burkina Faso, Canada, Israel, France, Guatemala, Lithuania, Saudi Arabia, South Africa, Taiwan, Thailand and the United Kingdom, according to the firm.


***Rule #1 of Linux Security:****No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*




#### Tags:
[[SparrowDoor]] [[Linux]] [[ProxyLogon]] [[FamousSparrow]] [[FamousSparrow’s]] [[noted.]] [[ESET]] [[Microsoft]] [[DLL]] [[malware]] [[ThreatPost]]
