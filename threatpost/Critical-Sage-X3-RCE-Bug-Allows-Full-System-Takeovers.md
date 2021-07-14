# Critical Sage X3 RCE Bug Allows Full System Takeovers
### Security vulnerabilities in the ERP platform could allow attackers to tamper with or sabotage victims’ business-critical processes and to intercept data.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167612)
+ Date: July 7, 2021  2:34 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/07140358/ERP-e1625681098750.jpg)
Four vulnerabilities afflict the popular Sage X3 enterprise resource planning (ERP) platform, researchers found – including one critical bug that rates 10 out of 10 on the CVSS vulnerability-severity scale. Two of the bugs could be chained together to allow complete system takeovers, with potential supply-chain ramifications, they said.


Sage X3 is targeted at mid-sized companies – particularly manufacturers and distributors – that are looking for all-in-one ERP functionality. The system manages sales, finance, inventory, purchasing, customer-relationship management and manufacturing in one integrated ERP software solution.


Rapid7 researchers Jonathan Peterson, Aaron Herndon, Cale Black, Ryan Villarreal and William Vu, who discovered the issues (CVE-2020-7387 through -7390), said that the most severe of the flaws exist in the remote administrator function of the platform. As such, they said that there could be supply-chain ramifications to a successful attack ([a la Kaseya](https://threatpost.com/kaseya-patches-zero-day-exploits/167548/)) if the platform is being used by managed service providers to deliver functionality to other businesses.



“When combining CVE-2020-7387 and CVE-2020-7388, an attacker can first learn the installation path of the affected software, then use that information to pass commands to the host system to be run in the SYSTEM context,” the researchers said in a [Wednesday posting](https://www.rapid7.com/blog/post/2021/07/07/cve-2020-7387-7390-multiple-sage-x3-vulnerabilities/). “This can allow an attacker to run arbitrary operating system commands to create Administrator level users, install malicious software and otherwise take complete control of the system for any purpose.”


**Critical Authentication-Bypass Security Vulnerability**
---------------------------------------------------------


The critical bug (CVE-2020-7388) allows unauthenticated remote command execution (RCE) with elevated privileges in the AdxDSrv.exe component, according to Rapid7. AdxAdmin is a function that’s responsible for the remote administration of Sage X3 through the main console, researchers said – and an exploit could allow an adversary to execute commands on the server as the high-privileged “NT AUTHORITY/SYSTEM” user.


The administrative service is exposed on port TCP/1818 by default, under the process “AdxDSrv.exe.” The issue lies in the custom protocol that Sage X3 uses for interaction between the Sage X3 Console and AdxDSrv.exe, according to Rapid7.


The Sage X3 Console crafts a request to authenticate using a byte sequence that includes a password that’s been encrypted using a custom mechanism. In response, the AdxDSrv.exe sends four bytes, indicating that authentication was successful.


“These bytes are always prefixed with \x00\x00 and then two apparently random bytes, like so: ‘\x00\x00\x08\x14,'” researchers said.


After receiving a response that the authentication was successful, it’s then possible to execute remote commands, according to the advisory.


“First, the temporary directory is specified by the client with the name of the cmd file to be written to the server,” researchers explained. “The batch file, with the provided cmd file name, is written to disk with the ‘whoami’ command in it. After the AdxDSrv.exe service writes the temporary batch file to the named folder, it will execute it under the security context of the provided user credentials, via a Windows API call to CreateProcessAsUserAs.”


To exploit the issue and bypass the authentication process, a malicious actor could craft a special request to the exposed service. The cyberattacker would need to sidestep two components involved in sending a command to execute, researchers said.


First, the attackers must know the installation directory of the AdxAdmin service, so that they can specify the full path location to which to write the cmd file to be executed.


“Obtaining the installation’s directory can be done either with prior knowledge, educated guesswork, or via an unauthenticated, remote information disclosure vulnerability (CVE-2020-7387),” researchers said. “Installation path names tend to be fairly predictable when it comes to most enterprise software—nearly all users install to a default directory on one of a handful of drive letters.”


Secondly, the attackers must confound the authorization sequence that includes the encrypted password. This can be done using a series of packets that spoof the AdxDSrv.exe authentication and command protocol, but with one critical modification.


“An attacker can simply swap one byte and cause the service to ignore provided user credentials, and instead execute under the current AdxDSrv.exe process security context, which runs as NT AUTHORITY\SYSTEM,” researchers explained “A bit of fuzzing revealed that using ‘0x06’ instead of ‘0x6a’ during the start of the authorization sequence allows [the client] to opt out of authentication entirely. In this mode, the requested command is executed as SYSTEM instead of impersonating a provided user account.”


The issue affects V9, V11 and V12 versions of the platform.


**Medium-Severity Bugs in Sage X3**
-----------------------------------


The other three issues are rated medium in severity:


As mentioned, the bug tracked as CVE-2020-7387 allows attackers to uncover the pathname for the needed installation directory, for use in exploiting the critical RCE flaw.


“While fuzzing the authentication and command protocol used by AdxAdmin.exe as described in CVE-2020-7388, it was discovered that sending the first byte as ‘0x09’ rather than ‘0x6a,’ with three trailing null bytes, returned the installation directory without requiring any authentication,” researchers explained.


Meanwhile, CVE-2020-7389 is a system CHAINE variable script command-injection bug – but Sage said that it wouldn’t be fixing the issue since the functionality where the bug lives should only be available in development environments, not in production environments.


“Some web application scripts that allowed the use of the ‘System’ function could be paired with the ‘CHAINE’ variable in order to execute arbitrary commands, including those sourced from a remote SMB share,” according to the analysis. “The page can be reached via the menu prompts Development -> Script dictionary -> Scripts.”


And finally, the CVE-2020-7390 vulnerability is a [stored XSS bug](https://threatpost.com/unpatched-linux-marketplace-bugs-rce/167155/). Stored XSS, also known as persistent XSS, occurs when a malicious script is injected directly into a vulnerable web application. Unlike reflected XSS, a stored attack only requires that a victim visit a compromised web page. In this case, the issue exists on the “Edit” page for user profiles, with the fields for first name, last name and email fields vulnerable to a stored XSS sequence, researchers said.


A successful exploit could allow a regular user of Sage X3 to execute privileged functions as a currently logged-in administrator or to capture administrator session cookies for later impersonation as a currently logged-in administrator, according to Rapid7.


“[The bug] can only be triggered by an authenticated user, and requires user interaction [convincing the authenticated person to visit the correct webpage] in order to complete the attack,” researchers explained.


**Patching Information for Sage ERP Security Vulnerabilities**
--------------------------------------------------------------


The three eligible vulnerabilities were fixed in recent releases for Sage X3 Version 9 (those components that ship with Syracuse 9.22.7.2), Sage X3 HR & Payroll Version 9 (those components that ship with Syracuse 9.24.1.3), Sage X3 Version 11 (Syracuse  v11.25.2.6), and Sage X3 Version 12 (Syracuse v12.10.2.8). Note: There was no commercially available Version 10 of Sage X3.


If updates cannot be applied immediately, customers have other options for remediation, according to Rapid7:


“Generally speaking, Sage X3 installations should not be exposed directly to the internet, and should instead be made available via a secure VPN connection where required,” according to the analysis. “Following this operational advice effectively mitigates all four vulnerabilities, though customers are still urged to update according to their usual patch cycle schedules.”


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[X3]] [[exe]] [[AdxDSrv]] [[Rapid7]] [[XSS]] [[ERP]] [[CVE-2020-7387]] [[x00]] [[CVE-2020-7388]] [[AdxAdmin]] [[ThreatPost]]
