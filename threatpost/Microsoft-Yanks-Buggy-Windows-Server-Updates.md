# Microsoft Yanks Buggy Windows Server Updates
### Since their release on Patch Tuesday, the updates have been breaking Windows, causing spontaneous boot loops on Windows domain controller servers, breaking Hyper-V and making ReFS volume systems unavailable.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177648
+ Date: 2022-01-13T23:08:53+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/13180340/broken_windows-e1642115033472.jpg)

Microsoft has yanked the Windows Server updates it issued on Patch Tuesday after admins found that the updates had critical bugs that break three things: They trigger spontaneous boot loops on Windows servers that act as domain controllers, break Hyper-V and render ReFS volume systems unavailable.


The shattering of Windows was first reported by [BornCity](https://borncity.com/win/2022/01/12/windows-server-januar-2022-sicherheitsupdates-verursachen-boot-schleife/) on Tuesday, as in, on the same day that Microsoft released a mega-dump of 97 security updates in its [January 2022 Patch Tuesday](https://threatpost.com/microsoft-wormable-critical-rce-bug-zero-day/177564/) update. 


This month’s batch included the Windows Server 2012 R2 KB5009624 update, the Windows Server 2019 KB5009557 update and the Windows Server 2022 KB5009555 update, all of which are apparently buggy. 


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“Administrators of Windows Domain Controllers should be careful about installing the January 2022 security updates,” reported [BornCity](https://borncity.com/win/2022/01/12/windows-server-januar-2022-sicherheitsupdates-verursachen-boot-schleife/), which is a blog about information technology run by German freelance writer and physics engineer Günter Born. 


“I have now received numerous reports that Windows servers acting as domain controllers will not boot afterwards,” Born wrote. “Lsass.exe (or wininit.exe) triggers a blue screen with the stop error 0xc0000005. It can hit all Windows Server versions that act as domain controllers, according to my estimation.”


Domain controllers are servers that handle security authentication requests within a Windows domain. Microsoft’s Hyper-V, the other chunk of Windows being broken by the Windows Server updates, is a native hypervisor that can create virtual machines on x86-64 systems running Windows. 


The third thing that’s shattering due to the updates, Resilient File System (ReFS), is a file system that’s designed to maximize data availability, scale efficiently to large data sets across diverse workloads and provide data integrity with resiliency to corruption, as Microsoft [describes](https://docs.microsoft.com/en-us/windows-server/storage/refs/refs-overview) it. 


Born cited numerous reports from users who’ve concluded that the issue affects all supported Windows Server versions.


Multiple Reddit users confirmed the problems. [One commenter](https://www.reddit.com/r/sysadmin/comments/s21ae1/january_updates_causing_unexpected_reboots_on/) said that it “Looks like KB5009557 (2019) and KB5009555 (2022) are causing something to fail on domain controllers, which then keep rebooting every few minutes.”


Another Reddit contributor [said](https://www.reddit.com/r/sysadmin/comments/s1oqv8/kb5009543_january_11_2022_breaks_l2tp_vpn/) on Tuesday that they had just rebooted Win10 laptops that had the installed KB5009543 & KB5008876 updates and found that they’re also breaking L2TP VPN connections.


“Now their L2TP VPNs to different sites (All SonicWalls) are not working,” the Redditor said, citing an error message that read: “The L2TP connection attempt failed because the security layer encountered a processing error during initial negotiations with the remote computer.”


On Thursday, following the server update brouhaha, BleepingComputer [reported](https://www.bleepingcomputer.com/news/microsoft/microsoft-pulls-new-windows-server-updates-due-to-critical-bugs/) that Microsoft has pulled the January Windows Server cumulative updates, which are reportedly no longer accessible via Windows Update. As of Thursday afternoon, however, the company reportedly hadn’t pulled the Windows 10 and Windows 11 cumulative updates that were breaking L2TP VPN connections. 


Threatpost has reached out to Microsoft for comment and will update the story with any updates we receive.


When Patches Bite Back
----------------------


How do you convince organizations to patch promptly when patches sometimes don’t work – or, worse, when they cause outages on critical infrastructure such as directory controllers? 


It’s clearly a problem from a security perspective, experts say. “The [log4j](https://threatpost.com/microsoft-rampant-log4j-exploits-testing/177358/) difficulties of the past few weeks demonstrate that … we need organizations to apply security patches when they are available,” said John Bambenek, principal threat hunter at Netenrich. 


When patches don’t work, or worse, when they break things, it “provides the counter incentive to patching where organizations take a risk-averse approach to applying updates,” he told Threatpost on Thursday. “Downtime is easily measurable…the incremental risk of a security breach is not, which means cautious (instead of proactive) actions to patching will tend to win out.”


 It’s a painful tradeoff to make between keeping your operations going by using systems with known vulnerabilities versus keeping those systems fully secure but with added administrative effort, noted Bud Broomhead, CEO at Viakoo. “Organizations make these tradeoffs every day with IoT devices that fail to get patched quickly (or ever); however, it’s uncommon to see this with Windows Server, because there are such effective mechanisms through Windows Update to deliver and install patches quickly.”


Broomhead suggested that despite the testing Microsoft goes through in releasing an update, one best practice is to always install a new patch on a single machine before deploying more broadly. “This can help Windows Server administrators to assess their specific issues, and their tolerance for running under those conditions until a more stable patch is available,” he told Threatpost. 


That’s actually closer to the reality, noted Roy Horev, co-founder and CTO at Vulcan Cyber. “First, very rarely are patches ever directly applied straight from Microsoft, or any vendor, on Tuesday, or any other day, without first going through a series of tests to make sure they aren’t breaking things,” he pointed out. 


Even so, it’s tough to implement vendor patches and updates without breaking things, he told Threatpost via email – even if those patches are delivered straight from Redmond. “The eternal compromise between secure and/or stable production environments doesn’t rest just because the updates are coming from Microsoft,” Horev commented.


**Password** **Reset:** **[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):** Fortify 2022 with a password security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the *new* password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken. **[Register & Stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)** – sponsored by Specops Software.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Threatpost]] [[L2tp]] [[“the]] [[ThreatPost]]

