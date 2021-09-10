# Thousands of Fortinet VPN Account Credentials Leaked
### They were posted for free by former Babuk gang members who’ve bickered, squabbled and huffed off to start their own darn ransomware businesses, dagnabbit. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169348)
+ Date: September 9, 2021  6:49 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/09184513/boxing.jpeg)
Credentials pilfered from 87,000 unpatched Fortinet SSL-VPNs have been posted online, the company has [confirmed](https://www.fortinet.com/blog/psirt-blogs/malicious-actor-discloses-fortigate-ssl-vpn-credentials).


Or then again, maybe the number is far greater. On Wednesday, [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-leak-passwords-for-500-000-fortinet-vpn-accounts/) reported that it’s been in touch with a threat actor who leaked a list of nearly half a million Fortinet VPN credentials, allegedly scraped from exploitable devices last summer.


The news outlet has analyzed the file and reported that it contains VPN credentials for 498,908 users over 12,856 devices. BleepingComputer didn’t test the credentials but said that all of the IP addresses check out as Fortinet VPN servers.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


According to analysis done by [Advanced Intel](https://www.advintel.io/post/groove-vs-babuk-groove-ransom-manifesto-ramp-underground-platform-secret-inner-workings), the IP addresses are for devices worldwide. As the chart below shows, there are 22,500 victimized entities located in 74 countries, with 2,959 of them being located in the US.


A Creaky Old Bug Was Exploited
------------------------------


Fortinet hasn’t responded to either Threatpost’s or BleepingComputer’s requests for clarification on how many devices were compromised, though the company did confirm that the attackers exploited [FG-IR-18-384](https://www.fortiguard.com/psirt/FG-IR-18-384) / [CVE-2018-13379](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-13379): a path traversal weakness in Fortinet’s FortiOS that was discovered in 2018 and which has been [repeatedly](https://threatpost.com/election-systems-attack-microsoft-zerologon/160021/), [persistently](https://threatpost.com/apt-groups-exploiting-flaws-in-unpatched-vpns-officials-warn/148956/) [exploited](https://threatpost.com/hackers-exploit-flaw-cring-ransomware/165300/) [since](https://threatpost.com/nsa-security-bugs-active-nation-state-cyberattack/165446/) then.


Using the leaked VPN credentials, attackers can perform data exfiltration, install malware and launch ransomware attacks.


The bug, which recently made it to the Cybersecurity and Infrastructure Security Agency’s (CISA’s) list of the [top 30 most-exploited flaws](https://threatpost.com/cisa-top-bugs-old-enough-to-buy-beer/168247/), lets an unauthenticated attacker use specially crafted HTTP resource requests in order to download system files under the SSL VPN web portal.


[Fortinet fixed the glitch](https://www.fortiguard.com/psirt/FG-IR-18-384) in a May 2019 update (and has since then repeatedly urged customers to upgrade their devices to FortiOS 5.4.13, 5.6.14, 6.0.11, or 6.2.8 and above). But even if security teams patched their VPNs, if they didn’t also reset the devices’ passwords at the same time, the VPNs still might be vulnerable.


All in the Babuk Family
-----------------------


According to BleepingComputer, a threat actor known as Orange – the administrator of the newly launched RAMP hacking forum and a previous operator of the Babuk ransomware operation – was behind the leak of Fortinet credentials.


Orange, who reportedly split off from Babuk after gang members quarreled, is believed to now be in with the new Groove ransomware operation. On Tuesday, Orange created a post on the RAMP forum with a link to a file that allegedly contained thousands of Fortinet VPN accounts.


At the same time, a post promoting the Fortinet leak appeared on Groove’s data leak site.


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/09181910/Screen-Shot-2021-09-09-at-6.18.51-PM-e1631225980966-1024x595.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/09181910/Screen-Shot-2021-09-09-at-6.18.51-PM-e1631225999483.png)


Groove is a new ransomware gang that’s been active just since last month. It favors the [double extortion](https://threatpost.com/double-extortion-ransomware-attacks-spike/154818/) model of combining data compromise with threats to publish seized data.


According to a Wednesday [post](https://www.mcafee.com/blogs/enterprise/mcafee-enterprise-atr/how-groove-gang-is-shaking-up-the-ransomware-as-a-service-market-to-empower-affiliates) co-authored by researchers from Intel471 and McAfee Enterprise Advanced Threat Research (ATR), with contributions from Coveware, McAfee Enterprise ATR said that it believes with high confidence that Groove is associated with the Babuk gang, either as a former affiliate or subgroup.


Chatting Up the Ransomware ‘Artist’
-----------------------------------


On Tuesday, one of the Groove gang’s members decided to chat up [Advanced Intel researchers](https://u7061146.ct.sendgrid.net/ls/click?upn=4tNED-2FM8iDZJQyQ53jATURfcd4v3FHxX6gbihrPKiOsKVZWKogo5F6F12wmaozsXKHpRn-2BuwOKhxsw08i8Jv-2FwvO5fMxaC-2Fte96Z6WZovyPDvgaoAv118tKwZ5rO8iwUDyyIWPDHnMoXBJtaLTD2RabFZrrydZEg6RqJoehkdLk-3DUm1f_q07lK5GAAVvAnbc-2Fr-2FBDhAPhoMvwzp-2Bdh4wgfTcF0AUhu01ZMXdKNJrsN0iCyDU7ehW0N22Ype9yCK1TM6XYzQ9CpkZyf7pccI4YxuRF0BJuYEbml5ScFK0-2F-2FZqd-2FdTfxpBYaCF7SSTgcHUKKV76UPqxTA0p35WcvHO-2B-2FRJuzuH54khmPYQLlkSfPjUHNAEXmgG-2BAfkNgcNKoVR9B9stOpafLCBk3qkXifeCsD9qirBA0nFvpW7EKJZBqmyDuRJPZiat-2B-2BXYCIJyRqjlbli1cMzNiEtsWjfRjsB82fJ-2BuXkMJGLitr0yTHVhHoV-2B7vgARde73QCuABoV-2Fk8lDDaGpEQVoKiwlCAiZTq63zy5kUQ-3D), to give them an insider’s take on how the new ransomware syndicate was formed and how it recruits operators. That included “the ‘truth’ about the association of Babuk, [DarkSide](https://threatpost.com/darksides-servers-shutdown/166187/) and [BlackMatter](https://threatpost.com/ransomware-gangs-haron-blackmatter/168212/), and other insights on the inner relationships within the ransomware community,” as researchers Yelisey Boguslavskiy and Anastasia Sentsova explained.


According to their writeup, the Groove representative is likely a threat actor that goes by “SongBird”. The researchers described SongBird as a known character, being a former Babuk ransomware operator and creator of the RAMP forum – which was launched on July 11 and which caters to top ransomware operators plotting their attacks.


The screen capture below shows Advanced Intel’s translation of SongBird’s explanation of the platform: “RAMP is the result of my year-long work of manipulation by top journalists and media such as Bloomberg and others. I spent quite some time to promote this domain and I am very proud for all of the work I did! I declare this forum is a work of art!”


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/09183430/kitten-brag-1024x543.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/09183430/kitten-brag-e1631226887669.jpg)


According to Advanced Intel, RAMP was initially based on the former Babuk’s data leak website domain but has since relocated to a new domain.


SongBird was reportedly prompted to pull off their tell-all after the [disclosure of Babuk’s source code](https://threatpost.com/babuk-ransomware-builder-virustotal/167481/). The source code was uploaded to VirusTotal in July, making it available to all security vendors and competitors. At the time, it wasn’t clear how it happened, though Advanced Intel said on Wednesday that the code release was done by an actor using the alias DY-2.


The code release had repercussions, Advanced Intel said. “The incident caused a massive backlash from the underground community which once again provoked the release of the blog by SongBird,” according to the report.


SongBird told the researchers that the actor wanted to address “the issue of constant misinformation and misreporting originating from the Twitter community covering the ransomware subject.”


The actor denied any associations between DarkSide and BlackMatter, with the exception of both ransomware strains sharing the same source code: a circumstance that means the code “most likely has been purchased from one of the DarkSide affiliates,” SongBird wrote.


How to Protect Your VPN
-----------------------


You can check Fortinet’s advisory for a list of versions affected by the oft-exploited vulnerability that was at the heart of this credential scraping. Fortinet had the following recommendations for organizations that may have been running an affected version “at any time”:


Rajiv Pimplaskar, Veridium chief revenue officer, told Threatpost that the breach is “a stark reminder of today’s dangers with password-based systems. While enterprises and users are starting to adopt passwordless authentication methods like ‘phone as a token’ and FIDO2 for customer and Single Sign On (SSO) portals and enterprise applications, vulnerabilities still exist across entire categories of cases such as, 3rd party sites, VPN (Virtual Private Network) and VDI (Virtual Desktop Infrastructure) environments, all of which are particularly vulnerable in the current WFH explosion.


“Companies need to adopt a more holistic modern authentication strategy that is identity provider agnostic and can operate across all use cases in order to build true resiliency and ensure cyber defense against such actors,” he concluded.


**It’s time to evolve threat hunting into a pursuit of adversaries.** [**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **Threatpost and Cybersixgill for** [**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **and get a guided tour of the dark web and learn how to track threat actors before their next attack.** [**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **for the LIVE discussion on September 22 at 2 PM EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[ransomware]] [[Fortinet]] [[VPN]] [[Babuk]] [[time,]] [[DarkSide]] [[Threatpost]] [[ThreatPost]]
