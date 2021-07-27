# Three Zero-Day Bugs Plague Kaseya Unitrends Backup Servers
### The unpatched flaws include RCE and authenticated privilege escalation on the client-side: Just the latest woe for the ransomware-walloped MSP. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168180)
+ Date: July 27, 2021  11:43 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27112232/zero-day.jpeg)
There are three new, unpatched zero-day vulnerabilities in [Kaseya Unitrends](https://www.unitrends.com/products/enterprise-backup-software) that include remote code execution (RCE) and authenticated privilege escalation on the client-side.


The Dutch Institute for Vulnerability Disclosure (DIVD) on Monday issued a public [advisory](https://csirt.divd.nl/cases/DIVD-2021-00014/) warning that the service and clients should be kept off the internet until there’s a patch.


Kaseya Unitrends is a cloud-based enterprise backup and disaster recovery technology that’s delivered as either disaster recovery-as-a-service (DRaaS) or as an add-on for the Kaseya Virtual System/Server Administrator (VSA) remote management platform. The flaws are in versions earlier than 10.5.2.




> *Do not expose this service or the clients (running default on ports 80, 443, 1743, 1745) directly to the internet until Kaseya has patched these vulnerabilities.* —DIVD advisory
> 
> 


DIVD experts disclosed the three flaws last week.


DIVD Chairman Victor Gevers told [BleepingComputer](https://www.bleepingcomputer.com/news/security/researchers-warn-of-unpatched-kaseya-unitrends-backup-vulnerabilities/) that it’s only found a small number of vulnerable servers, but those vulnerable instances are located “in sensitive industries.”


Gevers explained the advisory was originally shared with 68 government CERTs as an amber alert under a coordinated disclosure. One of the recipients went on to share it with an organization’s Financial Services service desk. From there, an employee published DIVD’s amber alert on an online analyzing platform, where it became public.


“An employee uploaded the TLP: AMBER labeled directly to an online analyzing platform and shared its content to all participants of that platform,” Gevers told the outlet. “Because we do not have an account on that platform, we immediately requested removing this file.”


DIVD discovered the flaws on July 2 and reported them to Kaseya on July 3.


On July 14, the DIVD started daily scans to detect vulnerable Kaseya Unitrends servers. Once it finds vulnerable systems, the DIVD will notify server owners, either directly or via Gov-CERTs, CSIRTs and other trusted channels.


Threatpost has reached out to Kaseya to find out when we can expect a patch. BleepingComputer did the same but hadn’t heard back as of Tuesday morning.


Kaseya’s Mostly Bad Month to Date
---------------------------------


This is only the latest woe for Kaseya, a managed service provider (MSP), and its customers: It’s had a hellishly hot July that’s included a massive [ransomware attack](https://threatpost.com/kaseya-attack-fallout/167541/) by the REvil cybergang.


Woe begets woe nelly: Following the ransomware attack, threat actors were malspamming a [bogus Microsoft security update](https://threatpost.com/fake-kaseya-vsa-update-cobalt-strike/167587/) that dropped Cobalt Strike backdoors.


As Kaseya rushed [to restore](https://threatpost.com/kaseya-patches-zero-day-exploits/167548/) the software-as-a-service (SaaS) version of its [ransomware-clobbered](https://threatpost.com/kaseya-patches-zero-day-exploits/167548/) VSA, the SaaS deployment, as well as the patch for the on-premises version, hit a snag and was delayed.


On-premises customers were the main targets of the ransomware attacks: As of July 7, those attacks had led to the encryption of files for around 60 of Kaseya’s customers that use the on-premises version of the platform – many of which are MSPs themselves that use VSA to manage the networks of other businesses.


Kaseya finally caught a break last week when it got its hands on a [universal decryptor for REvil ransomware](https://threatpost.com/kaseya-universal-decryptor-revil-ransomware/168070/).


Hopefully, the uptick in the luck chart will keep trending up to cover these new zero days.![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[Kaseya]] [[DIVD]] [[Unitrends]] [[Gevers]] [[ransomware]] [[ThreatPost]]
