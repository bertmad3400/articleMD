# Microsoft warns of easy Windows domain takeover via Active Directory bugs
### Microsoft warned customers today to patch two Active Directory domain service privilege escalation security flaws that, when combined, allow attackers to easily takeover Windows domains.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-warns-of-easy-windows-domain-takeover-via-active-directory-bugs/
+ Date: 2021-12-20T14:51:43-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/07/09/Windows.jpg)

![Microsoft warns of easy Windows domain takeover via Active Directory bugs](https://www.bleepstatic.com/content/hl-images/2021/07/09/Windows.jpg)


Microsoft warned customers today to patch two Active Directory domain service privilege escalation security flaws that, when combined, allow attackers to easily takeover Windows domains.


The company released security updates to address the two security vulnerabilities (tracked as [CVE-2021-42287](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42287) and [CVE-2021-42278](http://CVE-2021-42278) and reported by Andrew Bartlett of Catalyst IT) during the November 2021 Patch Tuesday.


Redmond's warning to immediately patch the two bugs — both allowing attackers to impersonate domain controllers — comes after a proof-of-concept (PoC) tool that can leverage these vulnerabilities was shared on Twitter and GitHub on December 11.


"When combining these two vulnerabilities, an attacker can create a straightforward path to a Domain Admin user in an Active Directory environment that hasn’t applied these new updates," Microsoft explains in an advisory published today.


"This escalation attack allows attackers to easily elevate their privilege to that of a Domain Admin once they compromise a regular user in the domain.


"As always, we strongly advise deploying the latest patches on the domain controllers as soon as possible."


Windows admins are urged to update devices exposed to attacks using the steps and information detailed in the following knowledgebase articles: [KB5008102](https://support.microsoft.com/en-us/topic/kb5008102-active-directory-security-accounts-manager-hardening-changes-cve-2021-42278-5975b463-4c95-45e1-831a-d120004e258e), [KB5008380](https://support.microsoft.com/en-us/topic/kb5008380-authentication-updates-cve-2021-42287-9dafac11-e0d0-4cb8-959a-143bd0201041), [KB5008602](https://support.microsoft.com/en-us/topic/november-14-2021-kb5008602-os-build-17763-2305-out-of-band-8583a8a3-ebed-4829-b285-356fb5aaacd7).


Researchers who tested the PoC stated that they were able to easily use the tool to escalate privileges from standard Active Directory user to a Domain Admin in default configurations.



![CVE-2021-42278 exploit tool in action](https://www.bleepstatic.com/images/news/u/1109292/2021/CVE-2021-42278_exploit_tool.jpg)*CVE-2021-42278 and CVE-2021-42287 exploit tool in action ([H*s*m](https://twitter.com/safe_buffer/status/1469742616505954323))*
How to detect exploitation, signs of compromise
-----------------------------------------------


Microsoft has also shared detailed guidance on detecting signs of exploitation in your environment and identifying potentially compromised servers using Defender for Identity advanced hunting query that looks for abnormal device name changes.


The step-by-step guide requires defenders to:


1. The sAMAccountName change is based on event 4662. Please make sure to enable it on the domain controller to catch such activities. [Learn more of how to do it here](https://docs.microsoft.com/en-us/defender-for-identity/configure-windows-event-collection#configure-object-auditing)
2. Open Microsoft 365 Defender and navigate to [Advanced Hunting](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/advanced-hunting-overview?view=o365-worldwide).
3. Copy the following query (which is also available in the Microsoft 365 Defender GitHub [Advanced Hunting query](https://github.com/microsoft/Microsoft-365-Defender-Hunting-Queries/blob/master/Privilege%20escalation/SAM-Name-Changes-CVE-2021-42278.md)):

```
IdentityDirectoryEvents
| where Timestamp > ago(1d)
| where ActionType == "SAM Account Name changed"
| extend FROMSAM = parse_json(AdditionalFields)['FROM SAM Account Name']
| extend TOSAM = parse_json(AdditionalFields)['TO SAM Account Name']
| where (FROMSAM has "$" and TOSAM !has "$")
        or TOSAM in ("DC1", "DC2", "DC3", "DC4") // DC Names in the org
| project Timestamp, Application, ActionType, TargetDeviceName, FROMSAM, TOSAM, ReportId, AdditionalFields
```
4. Replace the marked area with the naming convention of your domain controllers
5. Run the query and analyze the results which contain the affected devices. You can use [Windows Event 4741](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4741) to find the creator of these machines if they were newly created
6. We recommend investigating these [compromised computers](https://docs.microsoft.com/en-us/defender-for-identity/investigate-a-computer) and determining that they haven't been weaponized.

"Our research team continues its effort in creating more ways to detect these vulnerabilities, either with queries or out-of-the-box detections," Microsoft [added](http://techcommunity.microsoft.com/t5/security-compliance-and-identity/sam-name-impersonation/ba-p/3042699).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Mining]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Tosam]] [[Windows]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-42287]] [[CVE-2021-42278]]

