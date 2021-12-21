# Two Active Directory Bugs Lead to Easy Windows Domain Takeover
### Microsoft is urging customers to patch two Active Directory domain controller bugs after a PoC tool was publicly released on Dec. 12.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177185
+ Date: 2021-12-21T16:46:02+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2020/09/15094855/microsoft-exploit.jpg)

A proof-of-concept tool has been published that leverages two Windows Active Directory bugs fixed last month that, when chained, can allow easy Windows domain takeover.


In a Monday [alert](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/sam-name-impersonation/ba-p/3042699), Microsoft urged organizations to immediately patch the pair of bugs, tracked as [CVE-2021-42287](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42287) and [CVE-2021-42278](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42278), both of which were fixed in its [November 2021 Patch Tuesday](https://threatpost.com/microsoft-nov-patch-tuesday-fixes-six-zero-days-55-bugs/176143/) release.


Both vulnerabilities are described as a “Windows Active Directory domain service privilege-escalation” bugs and are of high severity, with a CVSS criticality score of 7.5 out of 10.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“As always, we strongly advise deploying the latest patches on the domain controllers as soon as possible,” Microsoft advised.


Bugs Give Attackers ‘Straight Path’ to Admin Privileges
-------------------------------------------------------


The vulnerabilities allow attackers to easily jack up privileges to that of domain admin in unpatched [Windows Active Directory](https://threatpost.com/podcast-securing-active-directory-nightmare/168203/) domain services after impersonating a regular domain user, according to Microsoft’s advisory.


Domain administrators in Windows are users that can modify the configuration of Active Directory servers and can modify any content stored there. Domain admins can create new users, delete users and change their permissions; and can control authorization and authentication to Windows services.


“​When combining these two vulnerabilities, an attacker can create a straightforward path to a domain admin user in an Active Directory environment that hasn’t applied these new updates,” according to the security alert. “This escalation attack allows attackers to easily elevate their privilege to that of a Domain Admin once they compromise a regular user in the domain.”


On Dec. 11, a proof-of-concept (PoC) tool to exploit the bugs was publicly released on Twitter and GitHub, just a few weeks after Patch Tuesday November 2021. Multiple security researchers confirmed that it works and that the exploit is easy.




How to Tell if Systems Have Been Compromised
--------------------------------------------


Microsoft defines the exploit as SAM Name impersonation. Same Account Name (SAM) refers to the sAMAccountName attribute: a logon name used to support clients and servers from previous versions of Windows, such as Windows NT 4.0, Windows 95, Windows 98 and LAN Manager.


Microsoft’s research team published detailed guidance on detecting signs of exploitation and identifying compromised servers with a Defender for Identity advanced hunting query that sniffs out abnormal device name changes: changes that “should happen rarely to begin with,” it said. Defender for Identity is a cloud-based security tool that uses on-premises Active Directory signals to identify, detect and investigate advanced threats, compromised identities and malicious insider actions.


The query compares those name changes with a list of domain controllers in your environment, researchers said. “To investigate if these vulnerabilities might have been exploited in your environment before the hotfixes were deployed, we highly recommend you follow the step-by-step guide,” Microsoft recommended, providing these instructions:


1. The sAMAccountName change is based on event 4662. Please make sure to enable it on the domain controller to catch such activities. [Learn more of how to do it here.](https://docs.microsoft.com/en-us/defender-for-identity/configure-windows-event-collection#configure-object-auditing)
2. Open Microsoft 365 Defender and navigate to [Advanced Hunting](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/advanced-hunting-overview?view=o365-worldwide).
3. Copy the following query (which is also available in the Microsoft 365 Defender GitHub [Advanced Hunting query](https://github.com/microsoft/Microsoft-365-Defender-Hunting-Queries/blob/master/Privilege%20escalation/SAM-Name-Changes-CVE-2021-42278.md)):  

IdentityDirectoryEvents | where Timestamp > ago(1d) | where ActionType == “SAM Account Name changed” | extend FROMSAM = parse\_json(AdditionalFields)[‘FROM SAM Account Name’] | extend TOSAM = parse\_json(AdditionalFields)[‘TO SAM Account Name’] | where (FROMSAM has “$” and TOSAM !has “$”) or TOSAM in (“DC1”, “DC2”, “DC3”, “DC4”) // DC Names in the org | project Timestamp, Application, ActionType, TargetDeviceName, FROMSAM, TOSAM, ReportId, AdditionalFields
4. Replace the marked area with the naming convention of your domain controllers
5. Run the query and analyze the results which contains the affected devices. You can use [Windows Event 4741](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4741) to find the creator of these machines, if they were newly created
6. We recommend investigating these [compromised computers](https://docs.microsoft.com/en-us/defender-for-identity/investigate-a-computer) and determine that they haven’t been weaponized.
7. Make sure to update the devices with the following KBs: [KB5008102](https://support.microsoft.com/en-us/topic/kb5008102-active-directory-security-accounts-manager-hardening-changes-cve-2021-42278-5975b463-4c95-45e1-831a-d120004e258e), [KB5008380](https://support.microsoft.com/en-us/topic/kb5008380-authentication-updates-cve-2021-42287-9dafac11-e0d0-4cb8-959a-143bd0201041), [KB5008602](https://support.microsoft.com/en-us/topic/november-14-2021-kb5008602-os-build-17763-2305-out-of-band-8583a8a3-ebed-4829-b285-356fb5aaacd7).


“Our research team continues its effort in creating more ways to detect these vulnerabilities, either with queries or out-of-the-box detections,” Microsoft said.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Tosam]] [[ThreatPost]]
#### CVE's
[[CVE-2021-42287]] [[CVE-2021-42278]]

