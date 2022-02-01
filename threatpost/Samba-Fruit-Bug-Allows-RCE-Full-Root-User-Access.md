# Samba ‘Fruit’ Bug Allows RCE, Full Root User Access
### The issue in the file-sharing and interop platform also affects Red Hat, SUSE Linux and Ubuntu packages.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178141
+ Date: 2022-02-01T20:02:02+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/02/01150048/Fruit-Stock-Photo-scaled-e1643745670878.jpeg)

A critical severity vulnerability in the Samba platform could allow attackers to gain remote code execution with root privileges on servers.


Samba is an [interoperability suite](https://www.samba.org/samba/docs/SambaIntro.html) that allows Windows and Linus/Unix-based hosts to work together and share file and print services with multi-platform devices on a common network, including SMB file-sharing. Gaining the ability to execute remote code as a root user means that an attacker would be able to read, modify or delete any files on the system, enumerate users, install malware (such as cryptominers or ransomware), and pivot to further into a corporate network.


The bug ([CVE-2021-44142](https://bugzilla.samba.org/show_bug.cgi?id=14914)) specifically is an out-of-bounds heap read/write vulnerability in the VFS module called “vfs\_fruit.” It affects all versions of Samba prior to v.4.13.17, and carries a rating of 9.9 out of 10 on the CVSS security-vulnerability severity scale. Additionally, some Samba-supporting Red Hat, SUSE Linux and Ubuntu packages [are also affected](https://kb.cert.org/vuls/id/119678).


**‘Fruits’ of an Attacker’s Labor**
-----------------------------------


The “fruit” module is used to provide “enhanced compatibility with Apple SMB clients and interoperability with a Netatalk 3 AFP fileserver,” through the use of extended file attributes (EA), according to company documentation.


“The specific flaw exists within the parsing of EA metadata when opening files in smbd [i.e., the server daemon that provides filesharing and printing services to Windows clients],” according to a [Monday advisory](https://www.samba.org/samba/security/CVE-2021-44142.html) from Samba. “The problem in vfs\_fruit exists in the default configuration of the fruit VFS module using [specific modules] fruit:metadata=netatalk or fruit:resource=file.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


There are two caveats to exploitability: If the VFS module has different settings than the default values, the system is not affected by the security issue, according to Samba.


Also, the attacker must have write access to a file’s extended attributes for successful exploitation.


However, “this could be a guest or unauthenticated user if such users are allowed write access to file extended attributes,” the company warned.


Samba credited Orange Tsai from DEVCORE with finding the bug.


**How to Mitigate CVE-2021-44142**
----------------------------------


Samba 4.13.17, 4.14.12 and 4.15.5 are the [patched versions](https://www.samba.org/samba/security/); administrators are urged to upgrade to these releases as soon as possible.


There is also a workaround available, according to the company, which involves removing the “fruit” module from the list of VFS objects in Samba configuration files: “Remove the ‘fruit’ VFS module from the list of configured VFS objects in any ‘vfs objects’ line in the Samba configuration smb.conf.”


Admins could also conceivably change the default settings for the the fruit:metadata or fruit:resource modules, but Samba warned that this would cause “all stored information to be inaccessible and will make it appear to macOS clients as if the information is lost.”


“The first thing enterprises need to do is apply the appropriate patches to known Samba installations, but these types of vulnerabilities are more difficult to fully mitigate than it may seem,” said Greg Fitzgerald, co-founder of Sevco Security, via email. “Even when all known instances are effectively patched, that still leaves forgotten or abandoned instances vulnerable. Every enterprise has IT assets that have fallen through the cracks.”


He added, “It’s gotten to the point where attackers are often more familiar with the networks they’re targeting than the security teams in charge of safeguarding those networks. It only takes one unpatched instance to create an opportunity for malicious actors to hit paydirt, and they’re counting on the fact that IT and security teams can’t create a comprehensive and accurate IT asset inventory.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Miner-C]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Vfs]] [[“the]] [[ThreatPost]]
#### CVE's
[[CVE-2021-44142]]

