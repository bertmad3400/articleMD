# Microsoft Faces Wormable, Critical RCE Bug & 6 Zero-Days
### The large January 2022 Patch Tuesday update covers nine critical CVEs, including a self-propagator with a 9.8 CVSS score.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177564
+ Date: 2022-01-11T21:54:57+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26141726/Windows-Abstract.jpg)

Microsoft has addressed a total of 97 security vulnerabilities in its January 2022 Patch Tuesday update – nine of them rated critical – including six that are listed as publicly known zero-days.


The fixes [cover a swath](https://msrc.microsoft.com/update-guide/) of the computing giant’s portfolio, including: Microsoft Windows and Windows Components, Microsoft Edge (Chromium-based), Exchange Server, Microsoft Office and Office Components, SharePoint Server, .NET Framework, Microsoft Dynamics, Open-Source Software, Windows Hyper-V, Windows Defender, and Windows Remote Desktop Protocol (RDP).


“This is an unusually large update for January,” Dustin Childs, a researcher with Trend Micro’s Zero Day Initiative (ZDI), explained. “Over the last few years, the average number of patches released in January is about half this volume. We’ll see if this volume continues throughout the year. It’s certainly a change from the smaller releases that ended 2021 [Microsoft [patched 67 bugs](https://threatpost.com/exploited-microsoft-zero-day-spoofing-malware/177045/) in December].”


**Zero-Day Tsunami**
--------------------


None of the zero-days are listed as being actively exploited, though two (CVE-2022-21919 and CVE-2022-21836) have public exploit code available. They are:


* [**CVE-2021-22947**](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-22947): HackerOne-assigned CVE in open-source Curl library (RCE)
* [**CVE-2021-36976**](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-36976): MITRE-assigned CVE in open-source Libarchive (RCE)
* [**CVE-2022-21874**](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-21874): Local Windows Security Center API (RCE, CVSS score of 7.8)
* [**CVE-2022-21919**](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-21919): Windows User Profile Service (privilege escalation, CVSS 7.0)
* [**CVE-2022-21839**](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-21839): Windows Event Tracing Discretionary Access Control List (denial-of-service, CVSS 6.1).
* [**CVE-2022-21836**](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-21836): Windows Certificate (spoofing, CVSS 7.8).


“The [cURL bug] was actually disclosed by HackerOne back in September 2021,” Childs said in ZDI’s Patch Tuesday [analysis](https://www.zerodayinitiative.com/blog/2022/1/11/the-january-2022-security-update-review). “This patch includes the latest cURL libraries into Microsoft products. This is why this CVE is listed as publicly known. Similarly, the patch for the Libarchive library was also disclosed in 2021, and the latest version of this library is now being incorporated into Microsoft products.”


**Patch Immediately: Critical, Wormable Bug**
---------------------------------------------


Out of the critical bugs, a remote code-execution (RCE) issue in the HTTP protocol stack stands out for researchers, given that it’s wormable – i.e., an exploit could self-propagate through a network with no user interaction. It carries the most severe CVSS vulnerability-severity rating of the entire update, coming in at 9.8 on the 10-point scale.


The bug **([CVE-2022-21907](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21907))** can be exploited by sending specially crafted packets to a system using the HTTP protocol stack (http.sys) to process packets.


“The CVE targets the HTTP trailer support feature, which allows a sender to include additional fields in a message to supply metadata, by providing a specially-crafted message that can lead to remote code execution,” Danny Kim, principal architect at Virsec, explained via email.


“No user interaction, no privileges required and an elevated service add up to a wormable bug,” Childs warned. “While this is definitely more server-centric, remember that Windows clients can also run http.sys, so all affected versions are affected by this bug. Test and deploy this patch quickly.”


Kim noted that CVE-2022-21907 is a particularly dangerous CVE because of its ability to allow for an attack to affect an entire intranet once the attack succeeds.


“The CVE is the latest example of how software capabilities can be warped and weaponized,” he noted. “Although Microsoft has provided an official patch, this CVE is another reminder that software features allow opportunities for attackers to misuse functionalities for malicious acts.”


**Other Critical Security Holes for January 2022 – One Unpatched**
------------------------------------------------------------------


Another interesting critical-rated RCE issue is **[CVE-2022-21840](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21840)** in Microsoft Office, which, importantly, does not yet have a patch for Office 2019 for Mac and Microsoft Office LTSC for Mac 2021 (CVSS 8.8).


“Most Office-related RCE bugs are important-severity since they require user interaction and often have warning dialogs, too,” said Childs, noting that the Preview Pane is not the attack vector. “Instead, this bug is likely critical due to the lack of warning dialogs when opening a specially crafted file.”


Microsoft also patched **[CVE-2022-21846](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21846)** – a critical RCE bug in Microsoft Exchange Server reported by the National Security Agency, which is listed as “exploitation more likely” (CVSS 9.0). It’s one of three Exchange RCEs being fixed this month (the others are CVE-2022-21969 and CVE-2022-21855), all of which are listed as being “network adjacent,” meaning the attacker would need to be on a target network already to be successful.


Despite the “exploitation more likely” rating, “Microsoft notes the attack vector is adjacent, meaning exploitation will require more legwork for an attacker, unlike the ProxyLogon and ProxyShell vulnerabilities which were remotely exploitable,” Satnam Narang, staff research engineer at Tenable, said via email.


One of the zero-days is listed as critical too, it should be noted: **[CVE-2021-22947](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-22947)**, which is the one found in the open-source cURL library used by Windows to transfer data using various network protocols. It allows RCE leading to man-in-the-middle (MiTM) attacks, according to Automox researcher Maarten Buis.


“An attacker could carry out a MitM attack by exploiting how cURL handles cached or pipelined responses from IMAP, POP3, SMTP or FTP servers,” he explained in [a Tuesday posting](https://blog.automox.com/automox-experts-weigh-in-january-patch-tuesday-2022). “The attacker would inject the fake response, then pass through the TLS traffic from the legitimate server and trick curl into sending the attackers’ data back to the user as valid and authenticated.”


The public disclosure significantly increases the chances of exploit, he warned.


And, a privilege-escalation issue is unusually flagged as critical: **[CVE-2022-21857](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21857)** in Active Directory Domain Services (CVSS 8.8).


“This patch fixes a bug that allowed attackers to elevate privileges across an Active Directory trust boundary under certain conditions,” Childs said. “Microsoft deemed the flaw sufficient enough for a critical rating. This does require some level of privileges, so again, an insider or other attacker with a foothold in a network could use this for lateral movement and maintaining a presence within an enterprise.”


There’s another critical privilege-escalation issue, **[CVE-2022-21833](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21833)** in the Virtual Machine IDE Drive (CVSS 7.8), but the complexity is marked high. According to Automox, to exploit it, a threat actor would need to gain access to an underprivileged account, such as through an unsecure user password or an account with minimal access controls, to expose this vulnerability.


Thus, “seeing this bug in the wild would likely take quite a bit of work,” Childs said.


Two critical issues in the DirectX Graphics Kernel carry a rating of 7.8 out of 10 on the CVSS vulnerability-severity scale and allow RCE: **[CVE-2022-21912](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21912)** and **[CVE-2022-21898](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21898)**.


To exploit these, viewing a specially crafted media file could result in code execution, and are likely present in most systems, according to Automox researcher Jay Goodman.


“The DirectX graphics kernel is a subsystem that enables internal components like graphics cards and drives or external devices like printers and input devices,” he said. “Attackers could use these remote code execution vulnerabilities to deploy and execute code on a target system. This can allow attackers to easily take full control of the system as well as create a base of operations within the network to spread to other systems. Common and widespread vulnerabilities like these are critical for attackers trying to steal corporate data or infiltrating sensitive systems. It is important for organizations to patch and remediate within the 72 hour window to minimize exposure.”


And finally, there’s **[CVE-2022-21917](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21917)** in HEVC Video Extensions (RCE, CVSS 7.8).


“Successful exploitation would require an attacker to bait an authenticated user into opening a maliciously crafted media file, which would result in remote code execution on the victim’s machine,” explained Automox researcher Justin Knapp. “Microsoft does not provide mitigation recommendations aside from patching. However, most affected customers will automatically be updated via the Microsoft Store and guidance is provided to check the package version to ensure it has the current update.”


The monster Patch Tuesday couldn’t come at a worse time, noted Bharat Jogi, director of vulnerability and threat research at Qualys.


“This massive Patch Tuesday comes during a time of chaos in the security industry whereby professionals are working overtime to remediate Log4Shell – reportedly the worst vulnerability seen in decades,” he said via email. “Unpredictable events such as Log4Shell add significant stress to the security professionals dealing with such outbreaks.”


***Password******Reset: [On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):*** *Fortify 2022 with a password-security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken.****[Register & stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)****– sponsored by Specops Software.*


 





## Tags:

#### Action:
[[action.malware.name=Arp]] [[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Chaos]] [[action.malware.name=Conti]] [[action.malware.name=DustySky]] [[action.malware.name=FTP]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Windows]] [[Cve]] [[Cvss]] [[Childs]] [[“the]] [[Rce]] [[“this]] [[(cvss]] [[Automox]] [[ThreatPost]]
#### CVE's
[[CVE-2022-21919]] [[CVE-2022-21836]] [[CVE-2021-22947]] [[CVE-2021-36976]] [[CVE-2022-21874]] [[CVE-2022-21839]] [[CVE-2022-21907]] [[CVE-2022-21840]] [[CVE-2022-21846]] [[CVE-2022-21969]] [[CVE-2022-21855]] [[CVE-2022-21857]] [[CVE-2022-21833]] [[CVE-2022-21912]] [[CVE-2022-21898]] [[CVE-2022-21917]]

