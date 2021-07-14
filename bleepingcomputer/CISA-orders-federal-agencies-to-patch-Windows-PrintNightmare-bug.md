# CISA orders federal agencies to patch Windows PrintNightmare bug
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/cisa-orders-federal-agencies-to-patch-windows-printnightmare-bug/)
+ Date: July 13, 2021
+ Author: Sergiu Gatlan


## Article:
![CISA orders federal agencies to patch Windows PrintNightmare bug](https://www.bleepstatic.com/content/hl-images/2021/04/21/CISA.jpg)


A new emergency directive ordered by the Cybersecurity and Infrastructure Security Agency (CISA) orders federal agencies to mitigate the actively exploited Window Print Spooler vulnerability on their networks.


CISA issued the Emergency Directive 21-04 after [Microsoft released security updates](https://www.bleepingcomputer.com/news/security/microsoft-printnightmare-security-updates-work-start-patching/) on Friday to address the vulnerability dubbed [PrintNightmare](https://www.bleepingcomputer.com/tag/printnightmare/) in all supported Windows versions.



The security flaw (tracked as CVE-2021-34527) enables [attackers to take over affected servers](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/) via remote code execution (RCE) with SYSTEM privileges.


As CISA explained, the emergency actions required are a direct result of unacceptable risks to Federal Civilian Executive Branch agencies posed by PrintNightmare bug's exploitation in ongoing attacks.


"CISA has validated various proofs of concept and is concerned that exploitation of this vulnerability may lead to full system compromise of agency networks if left unmitigated," CISA [said](https://cyber.dhs.gov/ed/21-04/).


"This determination is based on the current exploitation of this vulnerability by threat actors in the wild, the likelihood of further exploitation of the vulnerability, the prevalence of the affected software in the federal enterprise, and the high potential for a compromise of agency information systems."


Emergency Directive required actions
------------------------------------


To comply with the Emergency Directive 21-04, US federal agencies are required to take the following actions:


1. By 11:59 pm EDT, Wednesday, July 14, 2021, Stop and Disable the Print Spooler service on all Microsoft Active Directory (AD) Domain Controllers (DC).
2. By 11:59 pm EDT, Tuesday, July 20, 2021, apply the **July 2021 cumulative updates** to all Windows Servers and Workstations.
3. By 11:59 pm EDT, Tuesday, July 20, 2021, for all hosts running Microsoft Windows operating systems (other than domain controllers under action #1) complete either Option 1, 2, or 3 as [detailed in the directive](https://cyber.dhs.gov/ed/21-04/).
4. Validate Registry and/or Group Policy settings from options 1, 2, and 3 above are properly deployed.
5. By 11:59 pm EDT, Tuesday, July 20, 2021, ensure technical and/or management controls are in place to ensure newly provisioned or previously disconnected servers and workstations are updated and have the settings defined above in place before connecting to agency networks.
6. By 12:00 pm EDT, Wednesday, July 21, 2021, submit a completion report using the [provided template](https://cyber.dhs.gov/assets/report/ED_21-04_Template_v1.xlsx).


CISA added that the Emergency Directive would remain in effect until all agencies have gone through and applied all required actions or the directive "is terminated through other appropriate action.


In related news, CISA also published a [notification on the PrintNightmare zero-day](https://www.bleepingcomputer.com/news/security/cisa-disable-windows-print-spooler-on-servers-not-used-for-printing/) on July 1st, encouraging security professionals to disable the Windows Print Spooler service on all systems not used for printing.


Microsoft has [clarified the PrintNightmare patch guidance](https://www.bleepingcomputer.com/news/security/microsoft-printnightmare-security-updates-work-start-patching/) and shared the steps required to correctly patch the critical vulnerability on Friday after multiple security researchers [tagged the patches as incomplete](https://www.bleepingcomputer.com/news/microsoft/microsofts-incomplete-printnightmare-patch-fails-to-fix-vulnerability/).


More information and further guidance are available in the [KB5005010](https://support.microsoft.com/en-us/topic/kb5005010-restricting-installation-of-new-printer-drivers-after-applying-the-july-6-2021-updates-31b91c02-05bc-4ada-a7ea-183b129578a7) support document and in Microsoft's [CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) security advisory.


Since the Print Spooler service is enabled by default on most Windows client and server platforms, the risk of future attacks targeting unpatched systems is significant.


Applying Microsoft's July 2021 cumulative updates is the easiest way to ensure that attackers will not breach your network.




#### Tags:
[[CISA]] [[Microsoft]] [[Windows]] [[EDT]] [[PrintNightmare]] [[59]] [[Bleeping Computer]]
