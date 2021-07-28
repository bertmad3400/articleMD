# Podcast: Why Securing Active Directory Is a Nightmare
### Researchers preview work to be presented at Black Hat on how AD “misconfiguration debt” lays out a dizzying array of attack paths, such as in PetitPotam. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168203)
+ Date: July 28, 2021  7:01 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27211434/nightmare-e1627434884417.jpeg)
This week, Microsoft [rushed out a fix](https://threatpost.com/microsoft-petitpotam-poc/168163/) for a Windows NT LAN Manager exploit dubbed “PetitPotam” that forces remote Windows systems to reveal password hashes that can be easily cracked.


The frenzy begs the question: Why is securing Microsoft Active Directory (AD) such a nightmare?


When security researcher Gilles Lionel first identified the bug last week, he also published proof-of-concept (PoC) exploit code to demonstrate the attack. The PoC demonstrated how a PetitPotam attack can be chained to an exploit targeting Windows Active Directory Certificate Services (AD CS), which provides public key infrastructure (PKI) functionality.



 


Attack paths in AD are a huge issue for enterprises. It’s not just PetitPotam; AD was also part of the problem during the [SolarWinds attacks](https://threatpost.com/mimecast-solarwinds-hack-security-vendor-victims/163431/).


SpecterOps researchers Lee Christensen and Will Schroeder, who recently published a report on abusing AD CS titled Certified Pre-Owned ([PDF](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)) that they’ll also be doing a session on at Black Hat next week, are trying to get the security community to think about the AD problem in terms of “misconfiguration debt”: as in, incremental misconfigurations that build up over time, such that attackers are virtually guaranteed to find an attack path to their objective on any network.


It’s a serious situation. AD is used by over 90 percent of the Fortune 1000 for identity and access management. Organizations need solutions that can simplify protection: solutions that can cut through the haze to gain better visibility into AD.


Christensen and Schroeder were kind enough to come on the Threatpost podcast to talk about the issue and to bring good tidings about new tools that can help. They were joined by their colleague Andy Robbins, a co-creator of a free and open-source attack path mapping tool called BloodHound.


See below for links to the tools that our guests discussed, as well as links to their paper and blog post.


You can [download the podcast here](http://traffic.libsyn.com/digitalunderground/072621_SpecterOps_Mixdown_1.mp3), listen to the episode below, or scroll down to read a lightly edited transcript.



Get the Tools
-------------


Below are links to the tools discussed in the podcast, as well as a link to the researchers’ blog post, plus a link to the full, 140-page white paper:


 


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.


Lightly Edited Transcript
-------------------------


**Lisa Vaas:** Welcome to the Threatpost podcast. I’m your host, Lisa Vaas. My guests today are Lee Christiansen and Will Schroeder, the SpecterOps researchers behind a recent report entitled Certified Pre-owned: Abusing Active Directory Certificate Servers, about attack paths in Microsoft Active Directory.


This is a huge issue for enterprises. In fact, Active Directory was part of the problem during the SolarWinds attack. We’re also joined by their colleague, Andy Robbins, a co-creator of a free and open- source attack path mapping tool called BloodHound. The trio will be hosting a session on this research at Black Hat.


Welcome, Lee, Will and Andy, it’s a pleasure to have you on the show. Could you give us a little about your backgrounds?


**Will Schroeder:** Sure. My name is Will Schroeder. My handle is @harmj0y on Twitter, GitHub and everywhere else. I’m a technical architect, with SpecterOps, and I’ve been involved in offensive security, PowerShell, Active Directory, attack tooling, these types of things for a good number of years.


**Lee Christensen:** My name is Lee Christiansen. I go by @tifkin\_ on Twitter, and I’m also a technical architect here at SpecterOps. And I’ve been involved with red teaming and research and development and capability development here at SpecterOps. Helping support our offensive services.


**Andy Robbins:** My name is Andy Robbins. I’m like you mentioned, Lisa I’m one of the co-creators of the free and open source tool BloodHound. Will is actually also a, one of the co-creators of that. My background is in managing Active Directory environments. And then for the past six or seven years also on the red team side, and now full time I work on BloodHound development.


**Lisa Vaas:** Well, great. Thank you so much. It’s a pleasure to have you here.


So take it away, gentlemen. We’re all eager to hear what a nightmare it is to secure Active Directory, how that’s worked in attackers’ favor and how security professionals are tackling the issue today. So go right on.


**Will Schroeder:** Yeah. I will say that, you know, one of the things people tend to ask is like why Active Directory is such a problem.


You know, it’s, there’s a lot of different parts to this answer. So I was kind of the first part and then lean and you can kind of follow on, but one of the things is that it’s definitely ubiquitous. So like 90, 95 percent of enterprises will use Active Directory in some form. So part of this, this means that attackers just need to refine their skills against Active Directory.


And they’re able to reuse those same attacks, tooling skills, and anything to attack a large number of organizations across the globe. So there’s definitely a really high attacker kind of payoff for investing in tooling and offensive research against Active Directory because it can be reused to attack a large number of organizations.


**Lee Christensen:** Yeah, I I’d say also another large aspect of this is that Active Directory is being central authentication system in most Windows environments. So that means it’s responsible for managing the users, the passwords and the accounts of just everybody and configuring, you know, the computers in the, in the entire organization and as such I like to say it has a large blast radius. So if something gets compromised in Active Directory, a lot of times the entire network can get compromised. And so there’s a lot of components to it as well that can be abused. And so like, depending on, you know, these different components you get access to, you can, you know, achieve other objectives.


So beyond just authentication so you can compromise, you know, a server, you can get access to the data. Just by abusing all of these features that come as a part of Active Directory.


**Andy Robbins:** Yeah, I think the only thing I would add so Will and Lee, you mentioned that Active Directory, it’s ubiquitous, it’s powerful.


And for most organizations it’s foundational, their entire business processes are built on and rely on the availability, stability, and security of Active Directory. The only other thing I would add is that while Active Directory is incredibly powerful for the business and for attackers, you know, from our perspective being attackers, it’s relatively easy to attack. It’s incredibly difficult to appropriately defend. I think the biggest reason for that in my mind is Active Directory and Windows both have this opacity to them in that it’s very difficult to answer the question of, who has control of any other object or who has control of the computer, or even the other way around: Given any user, any group, how powerful is that user or that group?


The built-in tooling that is afforded to admins in Windows and Active Directory makes it incredibly difficult to answer those questions. And so things like least privilege access that are supposedly best practice are totally impractical for most organizations to implement in the first place. Let alone maintain over time.


**Will Schroeder:** And the last thing I’ll add on to that last kind of point is just the complexity of Active Directory along with, you know, how easy it can occasionally be to where one of the things we’ve seen and a term we’ve tried to help kind of push is misconfiguration debt, where we see Active Directory has been in an environment for a long period of time.


These seemingly small changes, they might look, you know, innocuous or whatever can start to build up and can start to be chained together to result in unintentional environment compromise. So, and it’s difficult for administrators to see the impacts that those really small little changes might have on the, you know, the security of the entire system


**Lisa Vaas:** You’ve called it a nightmare to configure Active Directory.


**Will Schroeder:** It can be. All three of us have been involved in securing and attacking Active Directory for a long, you know, a large number of years. And as an example, the research that Lee and I performed on Active Directory Certificate Services that we’re talking about, at Black Hat, you know, introduces this whole additional, like attack surface that a lot of people didn’t really fully know about or understand that’s been around for decades, you know, this part of Active Directory and it provides a common way for organizations to misconfigure their environments in a different way that allows complete domain compromise. We’ve seen that a lot from departments, people. You know, weren’t even fully aware to the extent that, you know, their teams were running Active Directory Certificate Services or what the security implications could be.


So I think it’s a good example of even though the system has been around Active Directory has been around for a long time, there’s still things that pop up that we, as an industry or as organizations didn’t completely understand the security implications of. You can’t secure for things that you don’t fully understand, and it’s just, you know, more and more things seem to come up.


**Lee Christensen:** Yeah. I think that kind of speaks to kind of a problem. Our industry as a whole is deprecating and modernizing older technologies that we have. You look at things like Active Directory Certificate Services, or like some of the recent vulnerabilities that have been coming out and like spooler, and like these old technologies that have been around forever.


You know, they haven’t been stopped yet by Microsoft or others. like you look at other vendors to upgrade their technologies to modern technologies. So kind of maybe rewriting it in a more secure language or deprecating features. And so there’s, there tends to be a much higher focus on adding new features, which in the attacker’s eyes, that’s just adding more attack surface.


That’s more I can try and abuse and exploit, whereas there’s very little focus on, you know, turning off things that don’t need to be enabled anymore. Or, you know, a lot of this code was written maybe 20 years ago, let’s rewrite that and maybe a newer, safer language like Rust or, you know, just these newer languages that are just safer.


Rather than, you know, running these old, you know, dangerous memory, unsafe languages.


**Lisa Vaas:** Fair enough. And Andy, how about from your point of view?


**Andy Robbins:** Admins may do one thing in the environment. Maybe that one thing is they add a principal to a security group, or they grant a permission on a particular object.


Nothing in Active Directory happens in a vacuum. There are connections, and there are relationships between all these different objects. So because someone is added to a security group, that means that they gain all the privileges of that security group. And the privileges that that group had, can be abused to form full attack paths that then result in the compromise of a domain admin or an enterprise admin or whatever, and something that Will and Lee both mentioned as well, is that there’s all this misconfiguration debt that builds up over the years.


It’s built on older technology. So a lot of Active Directory was written 20 years ago. A lot of current Windows operating systems get code from Windows NT or maybe even Windows 95. And so these attack paths that present themselves or emerge from these disparate and seemingly unrelated configurations and user behaviors.


There’s nothing new, those attack paths they’ve been there the entire time, but they’ve been invisible to AD admins. And because you can’t see those attack paths, you can’t really hope to do anything about them.


**Lisa Vaas:** So it sounds like visibility is a huge issue.


**Andy Robbins:** Absolutely. Yes. Yeah.


And is that where the mapping come in, is that where BloodHound comes in?


Sure. Yeah. So we created, Will, Rowe Hunt and I created BloodHound from our red team perspective. What, six years ago? Five years ago in 2016. And we use it. We built it originally for that exact purpose, for mapping those attack paths. And what we discovered was that there was this tedious, but very reliable attack technique called derivative, local admin or identity snowball attack.


So our team, other teams, we all landed on that same kind of methodology. Especially as Microsoft was getting better and not having server side exploits all over the place and software vendors were getting better at the same organizations.


We’re getting better at their vulnerability management practices. And so the old- school, throw a Metasploit exploit, get a shell that started to go to the wayside. But these attack paths that we could find by hand, they had been there the entire time. We just didn’t really need to sniff them out with BloodHound.


BloodHound, totally automates the process of finding those attack paths for us. And so, the free and open source version of BloodHound. It is built for red teamers by red teamers for that particular use case. But it does offer that visibility that you’re talking about, Lisa, that you can easily answer questions like who is a local admin on this computer.


It’s actually amazingly difficult to answer that question just with Windows or who can perform the DC synced attack. Very hard to tell that and audit that with built-in tooling, from Microsoft, easy as pie with free and open source BloodHound. And so defenders, they can use that free software to see how big of a problem they have with attack paths.


And I’m here to tell you that the problem is usually pretty big. They can also use that free version of the software to easily audit those permissions, both inbound. So who has permissions, inbound against anything, but also outbound. So, you know, my user, they’re not supposed to have local admin. Where does it, and how does it, does it have local admin somewhere, maybe through a group membership, maybe through an attack path and they can use that free version of the software also to make really big wins on knocking out frankly, millions of attack paths with relatively minimal efforts. So making just little permission changes on this object here, making little user behavior changes for these users here can result in seeing those numbers of attack paths go down just with using the freestyle.


**Lisa Vaas:** That sounds like a good outcome, Andy, before we go on you used a term credential shuffling that I’m not familiar with. I can kind of guess what it might be, but do you want to just explain what that is?


**Andy Robbins:** Sure. Yeah. So let’s say that, you know, I’m just a, a low, normal user, you know, I’m doing my thing and you know, Let’s let’s say accounting, just as just give a canonical example and let’s say that, well, you know what, it turns out that I have local admin on the computer that Lee uses, and then it turns out that Lee has local admin on the computer that will use this.


And so even though I don’t directly have that local admin on Will’s computer, I can kind of go to Lee’s computer, steal his credential and then kind of shuffle it. And turn that into admin on Will’s computer so I can execute that attack path. Then in that context, it relies on credentials. And so that’s why the credential shuffle term originated.


But these attack paths are not limited whatsoever just to credentials, they’re control of other objects, control of certificate templates control of anything else control of no you, whatever you like.


**Lisa Vaas:** Thank you for that explanation. What are our security professionals doing about this problem right now?


**Will Schroeder:** You know a lot of security professionals, not all, but you know, many tend to focus on a particular attack or kind of whatever is new without holistically understanding, you know, the entire system of Active Directory and how it can really affect an organization with a lot of these new attacks.


So like for example, the PetitPotam type thing that’s shown up in the news over the last week, that’s kind of used in combination with our Active Directory Certificate Services research. That’s great to be able to use that attack and show that something can be compromised and the risks for an organization.


But that’s just part of this one huge system like Andy had talked about and the complexity of this, it takes time and effort to try to understand. Professionals don’t have a complete, full grasp over kind of the intricacies of the entire system and how those things can really affect.


Like, that’s why Lee and I started diving into the Active Directory Certificate Services, for example, because we didn’t fully understand it. And then we realized all these types of new attack paths and attacker tradecraft, and things kind of fell out of that reason.


**Lisa Vaas:** When did you start to delve into this issue and why? What prompted you to look at this?


**Lee Christensen:** We started researching this at the beginning of this year, so, and about January and I mean, we’d known about Active Directory Certificate Services. We’d heard about it, some of the attacks that you can perform against it, but we hadn’t really dove in. And then I was reading some documentation online one day and found an interesting line: I was like, I didn’t know that you could authenticate using a certificate .


Or to LDAP in a specific way. And I, I messaged that to Will, and that just kind of kicked off all of our research here. Originally we just thought we saw a couple of things that were interesting . We dug into it. Like we found all these different ways that you can abuse Active Directory Certificate Services.


So originally we just wanted to write up a, like a short little blog post on it. And then as we continued our research that blog post grew into a 140- page white paper. You know, all the different kinds of tradecraft that attackers can abuse and defenses using Active Directory Certificate Services.


Active Directory Certificate Services has been around since the year 2000. So it was really, really old and it’s been in most networks. Most large networks have it. And it’s just been kind of chugging away, kind of like the old boiler in a basement, it’s working, but you don’t necessarily know the state of it or like how good it is.


In alot of companies, it’s been working just fine, but they haven’t really inspected it that well. And so. Since we’ve started looking at things, we’ve just noticed some massive misconfigurations in it. And I would say probably in like 80 to 90% of the networks we’ve looked at so far, we’ve found ways to escalate privileges, to like take over the network through Active Directory Certificate Services.


And it just kind of highlights to us the. Kind of the how little people are looking at it and how over time, like these misconceived misconfigurations have led to an insecure.


**Lisa Vaas:** How are you finding the misconfigurations? Are these in the networks of clients? Is this something that you can search online for using specific scanning tools?


**Will Schroeder:** This, well, sometimes there might be a little bit of occasionally there’s kind of some exposure through something like shouting We don’t perform anything like that. We do a lot of consulting for large enterprises, so we do a lot of offensive and defensive engagement. So as we start to develop new research, a trade craft, we work with a lot of our operators, too.


Examine the security posture of like current networks that we’re doing engagement sort of assessment stuff. So all the stuff that we verified, which, you know, again, it’s, you know, it’s not a complete sample set, but you know, our, our kind of sample of networks is based on real-world data, but it is run from.


And assessment engagement or internal type perspective. It’s not a, from what we’ve done is not like exposed on like the borders of the internet or something that can be scanned externally.


**Lee Christensen:** And, and most of this is we we’ve written some tools to help us in your mind this information. So. One of these tools we’ve already released.


So when we released our paper, we released a defensive tool called PSP K I audit, which is a defensive auditing tool that will identify all of these issues that we, we researched. And so that’s a great tool, highly recommend defenders to use it. And then on the offensive side at black hat this year, we’re going to be releasing an offensive tool called certify and it.


It also performs a similar type of enumeration, but in a more, you know, kind of attacker friendly way and both sides, like we, we both tools will accomplish the same goal. It’s just kind of different audiences for who they’re targeted for.


**Will Schroeder:** I was going to say, and we chose to kind of self-embargo, the offensive tool release for about 45 days after we had the defensive guidance on the paper in a defender focused tool set. That’s very difficult to use offensively to try to get to everyone, like kind of, you know, like, you know, full disclosure about, you know, these are the issues.


Here’s how you can find them. We assume. At the time, and this was confirmed that additional people will start building a tech tooling based on the information. But we wanted to give, you know, a pretty good window before we actually release our offensive tooling. And we’re also working on integrating a numeration of all the certificate service misconfigurations into bloodhounds as well.


So that from an offensive and defensive standpoint people will be able to audit these and then secure them. Well that


**Lisa Vaas:** I’m glad you spoke up about that because I was going to ask actually what the attackers are using in a, in an offensive way to scan for misconfigured systems.


**Will Schroeder:** At this point, you can do use.


So most of this information can be a numerated through Active Directory through eldap the protocol that pulls information about different Active Directory objects. So once a reasonably sophisticated attacker based on the research, once they knew what the misconfigurations were, is not that difficult for them to write their own tooling.


Those types of misconfigurations because we, you know, outline what the problems are and we had to detail what the problems were. So we’d outlined them in detail in the paper. So it’s not that hard for people to build their own kind of queries for these types of things. And again, we also built the defensive one with PSP K audit, and then the offensive kind of package tool is going to be released, you know, in the week and a half or so at the blackout talk.


And, then of course, integrate into bloodhounds.


**Lisa Vaas:** Integrating BloodHound into your tools.


**Will Schroeder:** Oh, sorry. Where we’re integrating the enumeration for the misconfigurations into the bloodstream as a separate effort. Yes, I’m sorry.


**Lisa Vaas:** That was my own confusion. Well, great. Do you guys want to continue with more good stuff from your research?


Ah, because if not, I’m going ask you to maybe chat a little bit about how these situations plays into Active Directory, which arm, which you mentioned something


**Will Schroeder:** I’ll just, oh yeah. Oh, we’d love to definitely would love to talk about that and how the stuff kind of fits in. I will just say a couple, couple of, kind of final points on the certificate research specifically.


Sure. It’s like the had mentioned it’s. It’s been around for a long time. So it has its own misconfiguration debt. And a lot of people don’t fully understand Astra directory, Certificate Services, even people that know Active Directory, you don’t fully understand active directory certificate services.


So we found has been very easy for people to misconfigure in a very severe way. And while it’s not installed by default, it’s extremely common in almost every environment we’ve looked at. They’ve had active directory certificate services. And like they had mentioned in about 80 to 90% of environments, there has been.


Flaws that allowed, allowed escalation of privileges to take over environments. And there’s a lot. Yeah. What we call like attack their tradecraft around active directory certificate services beyond the escalation aspect. So there’s stealing certificates or current users, there’s it can effectively be a different method for credential thefts without touching privilege processes and things like this.


It can be a way to persist for user accounts and machine accounts. We’ve also developed a way to, if you can steal the private key for a certificate authority and active directory certificate services, you can forge your own certificates and definitely in a way they can’t be revoked. So there’s a huge amount of Tradecraft that we cover in the paper that we researched beyond just the escalation primitives.


Along with that, there’s definitely a big lack of detection and incident response guidance, and just knowledge surrounding active directory certificate services to our most environments. Like Leah, we had said, you know, we very rarely seen, you know, incident response reports where people talked about, oh, we investigate and what certificates might’ve been issued to these people or these principles.


And we revoke them. So most people just don’t have the knowledge or the tooling. To actually deal with this from a defensive or instant response standpoint. So we do outline what we can in the paper for that. But we’re hoping to bring light to this specifically from a defensive side, so people can start better on responding to things. I don’t know if there’s anything to …


**Lee Christensen:** A good example of that is when we mention how there’s a lack of incident response and kind of detection, guidance. Something that came out of our research, we understood that if we compromise a machine, we can steal, you know, a certificate from a user and by default inactive.


Environments those certificates last, like they’re valid for up to like two years. And why that’s really valuable to me is because even if they wipe the machine or they reset that user’s password I can still use that certificate to log on as that user it’s a completely separate form of it’s like a completely separate credential from the password.


So, and in our experience, you know, nobody does. Is looking to see if attackers have stolen certificates before. And so that was really enlightening to me of being like, “wow”. A lot of attackers could still have access to networks if they have certificates and incident responders, you know, we, we asked some of our, our defensive team members, you know, is active directory certificate services, part of the incident response process at the companies you’re working with.


And I’ve yet to see. An environment where active directory certificate services was explicitly called out. So that was, you know, this is another huge goal of ours with the research is to kind of encourage organizations to, you know, look on the defensive side and incident response side into directory certificate services.


Yeah.


**Lisa Vaas:** Two years is a lot of time to do a lot of damage. Yeah, well we’re, we’re getting close to our allotted time. But I know you guys had advice on what the security community should be doing about this issue. Do you want to aluminate that for us?


**Lee Christensen:** So, I mean, there’s, there’s definitely a lot of things that people can do. I think. It there’s a Mo it’s a multi-pronged approach. So for one, like, I think Microsoft and the industry in better in general needs to be better about equipping it, administrators, to understand the impact of their actions.


So when they’re configuring things like an it administrator is just trying to do his job, like somebody joined a company, they need to be, you know, maybe added to a network chair or added to a group in active directory. But the it administrator, when they do that, They may unknowingly be granting that user access to hundreds of computers in the network.


And they just don’t realize that. And so I think there’s a lack of visibility that could be improved by like Microsoft and this isn’t just specific to active directory, but you know, a lot of products or things in the cloud, people just don’t understand the implications of their ant of their actions.


And so I think kind of, you know, a lot of products need to be better. Explain that to tighty administrators when they perform actions, I think that’s a big thing organizations and product companies needed to be doing.


**Will Schroeder:** That’s something that bloodhound, obviously we built to try to facilitate that kind of on our own.


We do have you know, kind of, similar to that, there’s an enterprise version of BloodHound that we’re launching very soon. That’s focused from a defensive standpoint that there’ll be information, you know Andy. No specific website, but we’ll be publishing over the next few weeks. But it’s, you know, that whole attack path type management of understanding the complexity of the system as a whole is a very hard problem, but it’s something that we spend a lot of time and effort to try to help, you know, administrators and organizations really understand if there’s anything to add, Andy.


**Andy Robbins:** I would add so Lisa you’re like your question as, you know, what should organizations do? Which Microsoft do, what should other companies like us do? I think one of the things that we all need to do is acknowledged the truth that on-prem active directory is here to stay. And the jury of just migrating off of one identity platform to another, or the dream of implementing something like legacy ESA.


For the vast majority of organizations is never going to happen. It’s totally impractical. It’s not worth the cost and the benefits, the benefits are immeasurable and not the good kind of immeasurable. As in they are non-empirical. You can’t say that they’re going to go from one identity platform to the other, and that’s going to solve all the problems that you have right now.


And so, because of that, when the time comes for someone to make the decision, are we going to move off of on-prem AD onto something else? 999 times out of a thousand. The answer is no. And it’s because of those reasons and like what is mentioning as far as. Attack path management and these little configurations having much greater impact.


One of the, one of the problems with a lot of the recommendations that our field gives to organizations is that they’re, they’re couched under the guise of best practice. A lot of times best practice is impractical in practice. But the bigger thing is like, like will mentioned earlier is that a lot of the people running active directory, their primary job is to keep the lights on and to keep those critical businesses, business processes, running and security serves the business, not the other way around.


And so when a recommendation comes down that says you should. Use this group policy to enforce this particular security control. And then the customer will very rightfully ask why. And a lot of times their response is “it’s best practice or it will reduce your attack surface.” That kind of recommendation is so easy to say no to.


Because there’s no, there’s no empirical evidence for why that is actually going to help. And so product companies, services companies need to get better at explaining the benefits of implementing security controls that come at a cost, whether that’s financial or labor, so that when a recommendation comes down that says you should do X.


And you should do that because it’s going to reduce your exposure to attack paths by 75.2%. That’s much harder to say no to it’s much easier to say yes to as much, as much easier for internal AD folks who kind of sell that remediation to each other or for a security team to sell that remediation to an ADA team.




#### Tags:
[[know,]] [[it’s]] [[there’s]] [[Vaas:]] [[that’s]] [[It’s]] [[I’m]] [[don’t]] [[Schroeder:]] [[Windows]] [[ThreatPost]]
