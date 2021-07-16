# Microsoft: New Unpatched Bug in Windows Print Spooler           
### Another vulnerability separate from PrintNightmare allows for local elevation of privilege and system takeover.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167855)
+ Date: July 16, 2021  7:57 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/09/15073634/Microsoft-Office.jpg)
Microsoft has warned of yet another vulnerability that’s been discovered in its Windows Print Spooler that can allow attackers to elevate privilege to gain full user rights to a system. The advisory comes on the heels of patching two other remote code execution (RCE) bugs found in the print service that collectively became known as PrintNightmare.


The company released [the advisory](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34481) late Thursday for the latest bug, called Windows Print Spooler Elevation of Privilege Vulnerability and tracked as [CVE-2021-34481](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34481). Microsoft credits Dragos vulnerability researcher Jacob Baines for identifying the issue.


The vulnerability “exists when the Windows Print Spooler service improperly performs privileged file operations,” according to Microsoft.



Attackers who successfully exploit the bug can run arbitrary code with SYSTEM privileges, allowing them to install programs, view, change or delete data, or create new accounts with full user rights, the company said. To do so, however, the attacker would first need to have the ability to execute code on a victim’s system.


To workaround the bug, administrators and users should stop and disable the Print Spooler service, Microsoft said.


**Slightly Less of a ‘PrintNightmare’**
---------------------------------------


The vulnerability is the latest in a flurry of problems discovered in Windows Print Spooler, but seems slightly less dangerous, as it can only be exploited locally.


Indeed, [Baines told BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-shares-guidance-on-new-windows-print-spooler-vulnerability/) that while the bug is print driver-related, “the attack is not really related to PrintNightmare.” Baines plans to disclose more about the little-known vulnerability in [an upcoming presentation](https://defcon.org/html/defcon-29/dc-29-speakers.html#baines) at Def Con in August.


The entire saga surrounding Windows Print Spooler [began Tuesday, June 30](https://threatpost.com/poc-exploit-windows-print-spooler-bug/167430/), when a proof-of-concept (POC) for an initial vulnerability in the print service—tracked as CVE-2021-1675–was dropped on GitHub showing how an attacker can exploit the flaw to take control of an affected system.


The response to the situation soon turned into confusion. Though Microsoft released an [update for CVE-2021-1675](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1675) in it its usual raft of [monthly Patch Tuesday updates](https://threatpost.com/microsoft-patch-tuesday-in-the-wild-exploits/166724/), fixing what it thought was a minor elevation-of-privilege vulnerability, the listing was updated later in the week after researchers from Tencent and NSFOCUS TIANJI Lab figured out it could be used for RCE.


However, soon after it became clear to many experts that Microsoft’s initial patch didn’t fix the entire problem. The federal government even stepped in last Thursday, when CERT/CC [offered its own mitigation](https://threatpost.com/cisa-mitigation-printnightmare-bug/167515/) for PrintNightmare that Microsoft has since adopted–advising system administrators to disable the Windows Print Spooler service in Domain Controllers and systems that do not print.


To further complicate matters, Microsoft also last Thursday dropped [a notice](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) for a bug called “Windows Print Spooler Remote Code Execution Vulnerability” that appeared to be the same vulnerability, but with a different CVE number—in this case, CVE-2021-34527. The company explained that the second bug was similar to the earlier PrintNightmare vulnerability but also its own distinct entity.


Eventually, Microsoft last Wednesday [released an emergency cumulative patch](https://threatpost.com/microsoft-emergency-patch-printnightmare/167578/) for both PrintNightmare bugs that included all previous patches as well as protections for CVE-2021-1675 as well as a new fix for CVE-2021-34527.


However, that fix also [was incomplete](https://www.kb.cert.org/vuls/id/383432), and Microsoft continues to work on further remediations as it also works to patch this latest bug, CVE-2021-34481. In the meantime, affected customers should install the most recent Microsoft updates as well as use the workaround to avoid exploitation, the company said.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Microsoft]] [[Windows]] [[PrintNightmare]] [[Baines]] [[CVE-2021-1675]] [[ThreatPost]]
