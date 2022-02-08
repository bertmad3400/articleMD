# No Critical Bugs for Microsoft February 2022 Patch Tuesday, 1 Zero-Day
### This batch had zero critical CVEs, which is unheard of. Most (50) of the patches are labeled Important, so don't delay to apply the patches, security experts said.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178286
+ Date: 2022-02-08T20:24:17+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26141726/Windows-Abstract.jpg)

Oh, blessed day: Microsoft’s Patch Tuesday is a featherweight in comparison to some of its not-atypical, 10-ton security updates, with just 51 patches — none of them rated critical.


For February, Microsoft’s [releases](https://msrc.microsoft.com/update-guide/) address CVEs in Windows and Windows Components, Azure Data Explorer, Kestrel Web Server, Microsoft Edge (Chromium-based), Windows Codecs Library, Microsoft Dynamics, Microsoft Dynamics GP, Microsoft Office and Office Components, Windows Hyper-V Server, SQL Server, Visual Studio Code and Microsoft Teams.


Among these, Microsoft addressed one zero-day: [CVE-2022-21989](http://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21989), a Windows Kernel elevation-of-privilege vulnerability. And, one of the updates is for a CVE first published in 2013.


This crop is in addition to the 19 CVEs patched by Microsoft Edge (Chromium-based) earlier this month, which brings the February total to 70 CVEs.


Whaaa? No Critical CVEs?!
-------------------------


Of course, it’s not size that matters. But February’s patch-a-palooza is light not just in number of CVEs, but also in that it comes with nary a single patch that’s labeled critical.


Has that ever happened?


As of Monday afternoon, Dustin Childs, a researcher with Trend Micro’s Zero Day Initiative (ZDI) Zero Day Initiative (ZDI), was scratching his head on that one.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“It may have happened before, but I can’t find an example of a monthly release from Microsoft that doesn’t include at least one critical-rated patch,” Childs wrote in ZDI’s Patch Tuesday [analysis](https://www.zerodayinitiative.com/blog/2022/2/8/the-february-2022-security-update-review). “It certainly hasn’t happened in recent memory.”


Childs noted that this February’s volume “is in line with February releases from previous years, which (apart from 2020) tend to be around 50 CVEs.”


It follows the big batch that Microsoft [baked](https://threatpost.com/microsoft-wormable-critical-rce-bug-zero-day/177564/) for its January 2022 Patch Tuesday, when it addressed a total of 97 security vulnerabilities, including nine critical CVEs – one of which is a self-propagator with a 9.8 CVSS score, and six of which were listed as publicly known zero-days.


To add indigestion to overwork, the January patches immediately [blew up](https://threatpost.com/microsoft-yanks-buggy-windows-server-updates/177648/). Since their release on Jan. 11, the updates started breaking Windows, causing spontaneous boot loops on Windows domain controller servers, breaking Hyper-V and making ReFS volume systems unavailable.


“Unfortunate that the Jan 11 updates have a number of serious flaws that mean they are un-deployable,” lamented one Threatpost reader. “That means our servers are unpatched and vulnerable to other security risks due to other bugs, until the next set of patches come out.”


Of the patches released today – that awaited “next set of patches” — 50 are rated important and one is rated moderate in severity.


No Active Exploits (Yet)
------------------------


Microsoft listed none of the February bugs as being under exploit, though one is listed as publicly known as the time of release. But as ZDI’s Childs pointed out, the same was true of last month’s release – for two days, at any rate, after which the company revised [CVE-2022-21882](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-21882) to indicate that “Microsoft was aware of limited, targeted attacks that attempt to exploit this vulnerability.”


If Microsoft learns otherwise, or changes its corporate mind, Childs promised that ZDI will update its analysis.


As for the zero-day elevation of privilege vulnerability in the Windows Kernel, Satnam Narang, staff research engineer at Tenable, noted via email: “While Microsoft rates the vulnerability as ‘exploitation more likely,’ the complexity to exploit the vulnerability is high, because of the added legwork required to prepare the target.”


He added, “This type of vulnerability is often leveraged by an attacker once they’ve already compromised the target, either through the use of a separate vulnerability or malware.”


Full List of CVEs
-----------------


As it does, ZDI has put up the full list of CVEs released by Microsoft for this month.


Childs also delved into four of the more interesting bugs. Here’s what he had to say:


* + [CVE-2022-21984](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21984) – **Windows DNS Server Remote Code Execution Vulnerability:** This patch fixes a remote code-execution bug in the Microsoft DNS server. The server is only affected if dynamic updates are enabled, but this is a relatively common configuration. If you have this setup in your environment, an attacker could completely take over your DNS and execute code with elevated privileges. Since dynamic updates aren’t enabled by default, this doesn’t get a critical rating. However, if your DNS servers do use dynamic updates, you should treat this bug as critical.
	+ [CVE-2022-23280](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-23280) – **Microsoft Outlook for Mac Security Feature Bypass Vulnerability:** “This Outlook bug could allow images to appear in the Preview Pane automatically, even if this option is disabled. On its own, exploiting this will only expose the target’s IP information. However, it’s possible a second bug affecting image rendering could be paired with this bug to allow remote code execution. If you are using Outlook for Mac, you should double-check to ensure your version has been updated to an unaffected version.”
	+ [CVE-2022-21995](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21995) – **Windows Hyper-V Remote Code Execution Vulnerability:** “This patch fixes a guest-to-host escape in Hyper-V server. Microsoft marks the CVSS exploit complexity as high here, stating an attacker, ‘must prepare the target environment to improve exploit reliability.’ Since this is the case for most exploits, it’s not clear how this vulnerability is different. If you rely on Hyper-V servers in your enterprise, it’s recommended to treat this as a critical update.”
	+ [CVE-2022-22005](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-22005) – **Microsoft SharePoint Server Remote Code Execution Vulnerability:** “This patch fixes a bug in SharePoint Server that could allow an authenticated user to execute any arbitrary .NET code on the server under the context and permissions of the service account of SharePoint Web Application. An attacker would need ‘Manage Lists’ permissions to exploit this, by default, authenticated users are able to create their own sites and, in this case, the user will be the owner of this site and will have all necessary permissions.”


Tenable’s Narang also pointed out that Microsoft also patched four elevation-of-privilege vulnerabilities in its Windows Print Spooler, including two rated “exploitation more likely.”


“One of these two flaws, CVE-2022-21999, is credited to researchers at Sangfor, who were responsible for disclosing some of the [PrintNightmare](https://threatpost.com/microsoft-unpatched-printnightmare-zero-day/168613/) vulnerabilities last summer,” Narang observed. “Because of the ubiquity of Print Spooler, vulnerabilities like this have been leveraged by ransomware groups.”


Also of Note: A Dusty Old-Timer
-------------------------------


Danny Kim, principal architect at Virsec, noted that he found it interesting that Microsoft [republished](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2013-3900) a CVE from 2013 to notify customers that an update to Windows 10/11 is available that addresses the original CVE.


“The CVE allows an attacker to inject malicious code into a signed application without invalidating the file’s original signature,” he explained in an email to Threatpost on Tuesday. “In Windows, signatures are used to verify that a file has not been modified since it was released by the original vendor. With the ability to inject malicious code into ‘verified’ applications, the attacker can gain complete control over a system especially if the user who runs the application has administrative privileges.”


He said that the attacker can go as far as creating new user accounts with full access, allowing the attacker to login to the machine at will.


Though the CVE is originally from 2013, it highlights two concerning facts, he said: “Patching is a slow-moving solution, and applications need to be monitored at all times. Patching is a post-attack solution that moves too slowly to keep up with today’s attacks. Applications, even verified ones, cannot just be checked when they start execution – their behavior throughout the lifetime of the application needs to be monitored and verified against expected behavior.”


Apply Patches ASAP
------------------


In spite of the fact that there were no critical CVEs nor active exploits called out in the February Patch Tuesday release, security pros recommended, as they always do, that the patches should be applied as soon as possible.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Paris]] [[victim.country.name=France]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Windows]] [[Cves]] [[Childs]] [[Hyper-v]] [[Cve]] [[Zdi]] [[“this]] [[Dns]] [[Threatpost]] [[ThreatPost]]
#### CVE's
[[CVE-2022-21989]] [[CVE-2022-21882]] [[CVE-2022-21984]] [[CVE-2022-23280]] [[CVE-2022-21995]] [[CVE-2022-22005]] [[CVE-2022-21999]]

