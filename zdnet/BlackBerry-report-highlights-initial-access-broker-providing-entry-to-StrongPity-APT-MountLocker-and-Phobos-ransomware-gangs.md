# BlackBerry report highlights initial access broker providing entry to StrongPity APT, MountLocker and Phobos ransomware gangs
### Named "Zebra2104," the initial access broker helped out a variety of cybercriminal groups and nation-states attacking businesses in Turkey and Australia.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/blackberry-report-highlights-initial-access-broker-providing-entry-to-strongpity-apt-mountlocker-and-phobos-ransomware-gangs/)
+ Date: November 5, 2021
+ Author: Jonathan Greig


## Article:
Unknown

A [new report](https://blogs.blackberry.com/en/2021/11/zebra2104) from BlackBerry has uncovered an initial access broker called "Zebra2104" that has connections to three malicious cybercriminal groups, some of which are involved in ransomware and phishing. 


The BlackBerry Research & Intelligence team found that Zebra2104 provided entry points to ransomware groups like MountLocker and Phobos as well as the StrongPity APT. The access was provided to a number of companies in Australia and Turkey that had been compromised.

The StrongPity APT targeted Turkish businesses in the healthcare space as well as smaller companies. BlackBerry said that from their research, they believe the access broker "has a lot of manpower or they've set up some large 'hidden in plain sight' traps across the internet."

The report said their investigation led them to believe that the MountLocker ransomware group had been working with StrongPity, an APT group dating back to 2012 that some alleged was a Turkish state-sponsored group. 

![zebra2104-fig08.png]()![zebra2104-fig08.png](https://www.zdnet.com/a/img/resize/5f7a4cd7a2668a595fcc64654b8fa75024812ee3/2021/11/05/f5958f97-ac4c-4441-9201-e9e988fc6efc/zebra2104-fig08.png?width=470&fit=bounds&auto=webp)Countries attacked by StrongPity.


 BlackBerry
 "While it might seem implausible for criminal groups to be sharing resources, we found these groups had a connection that is enabled by a fourth; a threat actor we have dubbed Zebra2104, which we believe to be an Initial Access Broker (IAB). There is undoubtedly a veritable cornucopia of threat groups working in cahoots, far beyond those mentioned in this blog," the researchers said, noting that they discovered the group while conducting research for a book about cyber threat intelligence.

"This single domain led us down a path where we would uncover multiple ransomware attacks, and an APT command-and-control (C2). The path also revealed what we believe to be the infrastructure of an IAB -- Zebra2104. IABs typically gain entry into a victim network then sell that access to the highest bidder on underground forums located in the dark web. Later, the winning bidder will deploy ransomware and/or other financially motivated malware within the victim's organization, depending on the objectives of their campaign." 


Their research began in April 2021, when they discovered curious behavior from domains that were identified previously in [a Microsoft report](https://www.microsoft.com/security/blog/2021/02/01/what-tracking-an-attacker-email-infrastructure-tells-us-about-persistent-cybercriminal-operations/) on servers that "had been serving malspam that resulted in varying ransomware payloads, such as Dridex, which we were able to corroborate."






A few of the domains had been involved in a phishing campaign that went after state government departments in Australia as well as real estate companies there in September 2020. With the help of other Microsoft reports, the researchers were able to trace the campaigns further to an indicator of compromise of a MountLocker intrusion.

"[Sophos has supposed](https://www.securitymagazine.com/articles/94954-sophos-identifies-connection-between-mount-locker-and-astro-locker-team-ransomware) that the MountLocker group has links to, or has in fact become, the recently emerged AstroLocker group. This is because one of the group's ransomware binaries has been linked to a support site of AstroLocker. It's possible that this group is trying to shed any notoriety or baggage that it had garnered through its previous malicious activities," the report added after explaining a number of technical links between the two groups. 

The BlackBerry Research & Intelligence team then used WHOIS registrant information and other data that led them to discover ties between the Phobos ransomware and MountLocker. 

"This new information presented a bit of a conundrum. If MountLocker owned the infrastructure, then there would be a slim chance of another ransomware operator also working from it (although it has happened before). In several instances, a delay was observed between an initial compromise using Cobalt Strike and further ransomware being deployed. Based on these factors, we can infer that the infrastructure is not that of StrongPity, MountLocker, or Phobos, but of a fourth group that has facilitated the operations of the former three. This is either done by providing initial access, or by providing Infrastructure as a Service (IaaS)," the report said. 

"An IAB performs the first step in the kill chain of many attacks; this is to say they gain access into a victims' network through exploitation, phishing, or other means. Once they have established a foothold (i.e., a reliable backdoor into the victim network) they then list their access in underground forums on the dark web, advertising their wares in the hopes of finding a prospective buyer. The price for access ranges from as little as $25, going up to thousands of dollars." 

Many IABs base their price on the annual revenue that the victim organization generates, creating a bidding system that allows any group to deploy whatever they want. 

![zebra2104-fig12.png]()![zebra2104-fig12.png](https://www.zdnet.com/a/img/resize/34c31c6ae680b3c13202a13fa909e2527c6dcead/2021/11/05/48db95fe-252d-4f0f-aa68-c09ea5bbaf9d/zebra2104-fig12.png?width=470&fit=bounds&auto=webp)
 BlackBerry
 "This can be anything from ransomware to infostealers, and everything in between. We believe that our three threat actors -- MountLocker, Phobos and StrongPity, in this instance – sourced their access through these means," The BlackBerry Research & Intelligence team explained.

The report notes that the domains resolved to IPs that were provided by the same Bulgarian ASN, Neterra LTD. While they wondered whether the access broker was based in Bulgaria, they surmised that the company was simply being taken advantage of. 

The researchers said the "interlinking web of malicious infrastructure" described throughout the report showed that cybercriminal groups mirrored the business world in that they are run like multinational enterprises. 

"They create partnerships and alliances to help advance their nefarious goals. If anything, it is safe to assume that these 'business partnerships' are going to become even more prevalent in future," the researchers said. 

"To counter this, it is only via the tracking, documenting, and sharing of intelligence in relation to these groups (and many more) that the wider security community can monitor and defend against them. This cooperation will continue to further our collective understanding of how cybercriminals operate. If the bad guys work together, so should we!"





#### Tags:
[[ransomware]] [[MountLocker]] [[StrongPity,]] [[ZDNet]]
