# Why are your IT people so miserable? Log4j2itis
### The biggest security problem of your life is happening right under your nose. Even if you don't know about it, your IT admins do.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3645709/why-are-your-it-people-so-miserable-log4j2itis.html
+ Date: 2021-12-29T03:40-05:00
+ Author: Steven J. Vaughan-Nichols


## Article:
![Article Image](https://images.idgesg.net/images/idge/imported/imageapi/2021/12/19/20/cso_nw_cloud_security_data_protection_encryption_movement_transition_by_metamorworks_gettyimages-1132912672_2400x1600-100826674-large-100914319-large.jpg?auto=webp&quality=85,70)

Instead of holiday toasts, do you hear screams and moans from your server room? Are your IT people sobbing inconsolably even when [Amazon Web Services (AWS) is running](https://www.computerworld.com/article/3644370/aws-outage-hit-collaboration-vendors-highlights-risk-of-cloud-based-tools.html)? Do you walk over sleeping system administrators and developers when you get to the office?

If that's happening to you, let me explain what’s happening. Your IT people — a *lot* of IT people — are suffering from Log4j2itis.

You may have seen some general news about it over the last couple of weeks, as even general news sources are picking up that it's bad news. As Jen Easterly, director of the the US Cybersecurity and Infrastructure Security Agency (CISA), said: "The [Log4j vulnerability is the most serious vulnerability](https://www.cnbc.com/video/2021/12/16/cisa-director-says-the-log4j-security-flaw-is-the-most-serious-shes-seen-in-her-career.html) I have seen in my decades-long career."

I've been at it longer than she has and in my never very humble [Twitter opinion](https://twitter.com/sjvn/status/1470816236095381511), "[#](https://twitter.com/hashtag/Log4Shell?src=hashtag_click)[Log4Shell](https://twitter.com/hashtag/Log4Shell?src=hashtag_click) may, with no exaggeration, be the worst IT [#security](https://twitter.com/hashtag/security?src=hashtag_click) problem of our generation."

That sounds really scary, because it is really scary. But what is it exactly? For the side of the story that requires you to have words like "security," "system administrator," or "developer" in your title, I’ve got the ugly details in my New Stack post: "[Log4Shell](https://thenewstack.io/log4shell-we-are-in-so-much-trouble/)[: We Are in So Much Trouble](https://thenewstack.io/log4shell-we-are-in-so-much-trouble/)."

If you're an ordinary mortal, here's what's going on and why it's such a major pain to deal with.

[Apache Log4j2](https://logging.apache.org/log4j/2.x/) is an extremely popular open-source Java logging library. If your Java program logs, well, pretty much anything, from the user's name to the number of times it calls some other program for help, odds are it uses Log4J2 to do the job.

That was fine. That was dandy. Everyone was happy. But, then a few weeks ago security investigators found that if you could make it log a line of malicious code, bad things would happen. How bad?  It has a "perfect" [Common Vulnerability Scoring System (CVSS)](https://www.first.org/cvss/) score of 10 out of 10. It's as bad a security vulnerability as there can ever be.

If any of your programs contain a vulnerable version of Logj42, they can be blasted with a remote code execution flaw attack. If successful, an attacker can do anything from [playing Doom on your servers](https://twitter.com/gegy1000/status/1469714451716882434) (seriously) to infecting every box on your network with the Mirai botnet to stiffing you with ransomware. Oh, and [government-sponsored hackers are now using the Log4j vulnerability as well](https://www.zdnet.com/article/log4j-flaw-now-state-backed-hackers-are-using-bug-as-part-of-attacks-warns-microsoft/). Just ask the [Belgian Defense Ministry, which was still recovering from an attack](https://www.zdnet.com/article/belgian-defense-ministry-confirms-cyberattack-through-log4j-exploitation/) just last week.

What might those programs be? Good question. [Thousands of widely used commercial programs are attackable](https://github.com/NCSC-NL/log4shell/tree/main/software). These include Apple iCloud; numerous Cisco programs; Minecraft client and server; Steam; Twitter; and many VMware programs.

And, if your crew or independent software vendors (ISV) wrote your programs with such software components as Apache Druid, Dubbo, Flink, Flume, Hadoop, Kafka, Solr, Spark, and Struts, they could be open to attack, too. This is a security hole that just keeps giving and giving.

The good news is there's a fix, three fixes actually, for Log4j2 vulnerabilities. The short version is if you update every copy of this troubled software library to [log4j 2.17.0](https://logging.apache.org/log4j/2.x/security.html), all will be well.

Aye, there's the rub. You must update *every* last one of them. And here's the really not-so-good part. Log4j is hidden away in millions of programs. Without a [software bill of materials (SBOM)](https://www.zdnet.com/article/linux-foundation-announces-new-open-source-software-signing-service/) for every application, you can't be sure you’ll find them all. And SBOM is a new concept. No one was making them last year, never mind seven years ago when Logj42 was first released.

So you must look for them. And, because Java programs hide their code in Russian-nesting doll structures such as Java archive files (JAR), finding the one program that needs patching can be a real pain. There are tools, such as the CISA [CVE-2021-44228\_scanner](https://github.com/CERTCC/CVE-2021-44228_scanner), that make life easier for your security and development team, but it's still a lot of work.

Imagine someone asked you to find every reference you ever made in documents to your CEO since 2014… without easy-to-use text search tools. It would be a nightmare, right? Now, imagine that if you don't find it your company’s IT infrastructure will collapse into a god-awful mess.

So, be kind to your IT staffers. Instead of drinking a New Year's Eve glass of champagne, they're likely to still be tracking down and cleaning up this mess. This is not going to end quickly and there will be many more related attacks to fend off before it's all done.

Happy new year?





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Spark]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Computerworld]]
#### CVE's
[[CVE-2021-44228]]

