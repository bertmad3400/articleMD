# The Apache Log4j team talks about the Log4Shell patching process
### The Record spoke with Christian Grobmeier, a member of the Apache Logging team and one of the developers who maintain the Log4j library.

## Information:
+ Source: The Record
+ Link: https://therecord.media/the-apache-log4j-team-talks-about-the-log4shell-patching-process/
+ Date: 2022-02-01T21:36:13+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2022/02/programmer.png)

On December 9, 2021, the internet learned of a major security bug in a little-known Java library named Apache Log4j. This little bug—codenamed Log4Shell—had one of the most significant impacts on the software landscape and triggered one of the most massive and well-coordinated patching drives in the recent history of the internet.


For the past month, government agencies, security firms, and IT experts alike have all worked together to audit Java-based applications, find which were vulnerable to Log4Shell attacks, worked with vendors to deliver patches, and then encouraged their customers to apply them as soon as possible.


At the heart of all of this has been the Apache Software Foundation and its Logging team, whose volunteers have been ardently maintaining the library for almost a decade and who have played a crucial role in having this vulnerability fixed in the first place.


The Record spoke with [Christian Grobmeier](https://www.linkedin.com/in/grobmeier/), a member of the Apache Logging team and one of the developers who maintain the Log4j library. The interview has been lightly edited for grammar and clarity.




---


**The Record: Tell us about yourself, your role at the Apache Software Foundation, and how you started helping on the Log4j project?**


**Christian Grobmeier:** About 20 years ago, I wanted to become a very good software developer. I had very good mentors but was curious about the software I used every day. Who wrote it, what did it look like. I dug deeper and learned about the Apache Software Foundation (ASF) and started contributing. I became a committer around 2007. I worked on Apache Commons Compress initially and then took an interest in Log4j. 


Eventually, I became a PMC member for Apache Logging and have also been active in other areas of the ASF, including as VP of Data Privacy.


**TR: Tell us how you first found out about the Log4Shell vulnerability and when was the first time you realized it would be a big deal?**


**CG:** The project realized the importance of this issue very quickly. Some of us first thought it was a security bug but didn’t see at first how big the issue was. When we understood how this could be exploited, we could see how big the problem was.


A CVE was filed, which eventually caused the media attention. 


**TR: There were some reports on Twitter about your team receiving abuse from some individuals. Any truth to those rumors or have people understood the situation you were put in and have generally been kind and helpful?**


**CG:** We’ve received supportive messages and messages that are beyond nasty. But a number of people clearly understand the nature of open source maintainership, and some have even jumped in to help with additional input, bug reports, or just read the source code as peer review.


Some people just sent messages of support.


**TR: There’s been much made about the lack of funding your project has received, which may have been contributed to a simple vulnerability like Log4Shell not being detected earlier. Has this changed in the meantime?**


**CG:** Many of the conversations around funding misunderstand the way software is developed at the ASF, our mission, and the nature of the vulnerability.


The vulnerability is not necessarily one that would have been caught if the Log4j team was “better funded.” We wouldn’t really describe it as a “simple” vulnerability. 


We believe that ASF projects are where communities should come together and do work for the public good. We would like to see more consumers of Log4j involved in development.



> We would like to see more consumers of Log4j involved in development.
> 
> Christian Grobmeier, Apache Software Foundation


**TR: Would more “eyes” on the code have helped uncover more security flaws? Would more people contributing and auditing the code be a better outcome of the Log4Shell aftermath?**


**CG:** We take security very seriously. It’s not at all clear that “funding” is a silver bullet to finding all security vulnerabilities.


At the ASF, we have an open and transparent development model. We would welcome security experts who want to get involved with Log4j or other projects to help review code and look for vulnerabilities.


**TR: How did friends react when they found out you were working on the project at the center of a major security crisis? Did this vulnerability have any impact on your private or professional life?**


**CG:** Some of my friends who know I contribute to Log4j reached out with support – including some friends I hadn’t heard from in years.


Professionally, I had an opportunity to help some customers upgrade, so that was good.


**TR: Did you or any of your team members have to take time off from your day job to deal with Log4Shell, or did you manage to squeeze fixing an internet IT meltdown in your free time?**


**CG:** The stress was very high for some of the Log4j team. It was not as hard on me as some of the other Log4j PMC [project management committee], some of whom missed a lot of sleep while actively working on the fix.


**TR: Which organizations in the private and government sector have helped your team with the Log4Shell aftermath more? Whom would you thank if you could?**


**CG:** The PMC would like to extend gratitude to the security researchers who filed security reports. We’d have loved having them look at the project before, and we hope they will continue to do so in the future. There is a list of credits on the CVEs and we’d like to thank everybody listed for working on them.


[Alvaro Muñoz](https://twitter.com/pwntester) played a special role with the JNDI vulnerability in general and even reported one of the CVEs later.


And I would like to add thanks to the companies that have helped provide extensive documentation and supported users in that way. Also, there are a bunch of Java developers on Twitter who spread the right information at the right time.


**TR: The Chinese government has suspended Alibaba from its cybersecurity platform for reporting the Log4Shell vulnerability to your project first, rather than its own security agencies, leaving government systems exposed. Where is your and your team’s stance on this controversial topic?**


**CG:** We prefer to stay politically agnostic when working on open source, but the earlier we get a report, the sooner we can fix it. The later the report, the higher the risk for all users. We think that the vulnerability was reported correctly in this case and hope that will continue.


**TR: Your team has patched a few bypasses for the original Log4Shell patch. Is something like Log4Shell hard to patch in general, or are those bypasses the result of a rushed patch, and everything is OK now?**


**CG:** What happened here is that we suddenly had many people looking at the code base and finding a few issues. A number of the fixes were unrelated to Log4Shell but were turned up in the review process after the initial vulnerability was discovered.


**TR: Were you surprised the vulnerability got weaponized so quickly? Did you hope for more time to refine the patch and have it spread across open and closed-source tools?**


**CG:** Of course, we would have liked more time to address it, but we understand that exploits can move quickly.


**TR: There are several cybersecurity talking-heads and news outlets calling Log4Shell the worst security bug ever discovered. Do you agree, or do you think it’s just recency bias, and there are far worst bugs that you would bug ahead of this one?**


**CG:** I wouldn’t agree it’s the worst ever. The industry has seen quite a few major security issues.


**TR: What are some of the good and bad parts in regards to the recent Log4Shell disclosure and media coverage? Anything that has annoyed you and your colleagues, or one thing that people got right or liked?**


**CG:** One good thing is that I loved how the Log4j community worked together. The collaboration has been amazing.


It has been disappointing to see how many users are still on Log4j 1.x – it’s been a distraction from responding to the Log4j 2.x issues. But a good thing is that people are now paying much more attention to their dependencies and understanding the need to look at the libraries they use daily.


**TR: Your team has now been at the center of a cybersecurity crisis. Can you share an anecdote from the Log4Shell disclosure and patching process that you think the world would want to know? Something that other FOSS dev teams should know or learn from your experience?**


**CG:** One colleague mentioned we should be careful how one reports security issues. Go to the project in question; talk to them privately first. Nothing worse than having the first report public on Twitter.


I also loved this quote of one of my colleagues very much: “*Be thankful when you get someone to post what they believe is a security vulnerability. Whether it is real or not it is a sign that your software is being reviewed. That is a great thing!*“





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Rover]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Log4shell]] [[Asf]] [[Grobmeier]] [[Pmc]] [[Cybersecurity]] [[The Record]]

