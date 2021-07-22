# Microsoft just published a workaround for this important Windows 10 flaw
### Microsoft offers a workaround to a bug that could give attackers the ability to copy an organisation's password hashes for offline cracking.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-just-published-a-workaround-for-this-important-windows-10-flaw/)
+ Date: July 22, 2021 -- 09:58 GMT (10:58 BST)
+ Author: Liam Tung


## Article:
Unknown

Microsoft has released a workaround for a privilege elevation flaw that affects all versions of Windows 10 and could give attackers the ability to access data and create new accounts on systems. 

Microsoft this week confirmed a serious elevation of privilege flaw, tagged as CVE-2021-36934, that could allow a local attacker to run their own code with system privileges. 


While the bug is important, the attacker must have already gained the ability to execute code on the target system in order to exploit the flaw, [according to Microsoft](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36934). 

**SEE:** [**Network security policy**](https://www.techrepublic.com/resource-library/whitepapers/network-security-policy/?ftag=CMG-01-10aaa1b) **(TechRepublic Premium)**

The bug affects the Security Accounts Manager (SAM) database in all versions of Windows 10 from version 1809. It may be more urgent to patch or mitigate because details of the flaw are publicly available. 

The SAM database is a sensitive component of Windows 10 since it is the location for storing user accounts, credentials and domain information. While credentials are hashed in SAM, the flaw gives attackers the opportunity to exfiltrate the hashed credentials and crack them offline.    

"An elevation of privilege vulnerability exists because of overly permissive Access Control Lists (ACLs) on multiple system files, including the Security Accounts Manager (SAM) database," [Microsoft says in an advisory](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36934). 






"An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights."

[Per The Record](https://therecord.media/serioussam-bug-impacts-all-windows-10-versions-released-in-the-past-2-5-years/), the flaw was [found by Jonas Lyk](https://twitter.com/jonasLyk/status/1417205166172950531) over the weekend. The issue is being referred to as SeriousSAM. Lyk discovered shadow copies of SAM were available for attackers to exploit while probing a preview of Windows 11, Microsoft's next version of Windows. 

**SEE:** [**GDPR: Fines increased by 40% last year, and they're about to get a lot bigger**](https://www.zdnet.com/article/gdpr-fines-increased-by-40-last-year-and-theyre-about-to-get-a-lot-bigger/)

Security firm Blumira explains why CVE-2021-36934 is a serious flaw.  

"The SYSTEM and SAM credential database files have been updated to include the Read ACL set for all Users for some versions of Windows," [the company notes in a blogpost](https://www.blumira.com/sam-database-vulnerability/). 

"This means that any authenticated user has the capability to extract these cached credentials on the host and use them for offline cracking, or pass-the-hash depending on the environment configuration."

The [US CERT coordination center notes several more](https://www.kb.cert.org/vuls/id/506989) ways the bug can impact affected Windows 10 machines. An attacker could:

* Extract and leverage account password hashes.
* Discover the original Windows installation password.
* Obtain DPAPI computer keys, which can be used to decrypt all computer private keys.
* Obtain a computer machine account, which can be used in a [silver ticket attack](https://www.sans.org/blog/kerberos-in-the-crosshairs-golden-tickets-silver-tickets-mitm-and-more/).





#### Tags:
[[Windows]] [[Microsoft]] [[ZDNet]]
