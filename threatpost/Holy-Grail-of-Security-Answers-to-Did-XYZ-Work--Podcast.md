# Holy Grail of Security: Answers to ‘Did XYZ Work?’ – Podcast
### Verizon DBIR is already funny, useful & well-written, and it just got better with mapping to MITRE ATT&CK TTPs. The marriage could finally bring answers to “What are we doing right?” instead of the constant reminders of what’s not working in fending off threats. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169192)
+ Date: September 7, 2021  8:00 am
+ Author: Lisa Vaas


## Article:
Get a glass. Pour in one shot of VERIS, aka the Vocabulary for Event Recording and Incident Sharing engine that generates Verizon’s funny, well-written, incredibly useful, annual Database Investigations Report ([DBIR](https://threatpost.com/verizon-pandemic-cyber-misery/166168/)). Next, add a shot of [MITRE ATT&CK](https://attack.mitre.org/): the curated knowledge repository of reported adversarial tactics, techniques, and procedures (TTPs).


Shake well, and you get what was poured out in late August: a [merged set of the frameworks](https://medium.com/mitre-engenuity/connecting-veris-and-mitre-att-ck-e3d00adbe5a4) that will provide even more detailed information about threats, enabling security teams and CSOs to look up a threat from a high level and then, for the first time, to drill down to the nitty-gritty for the TTPs that describe how attacks are pulled off.


Experts have embraced the merging of the two frameworks. John Bambenek, threat intelligence advisor at IT service management company Netenrich, told Threatpost that as it is, ATT&CK hasn’t really shown security team what needs to be done, “besides buy more security products.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“It’s good for strategic analysis, however, it’s wanting in driving tactical actions,” he said via email. “Combining with VERIS should enable more precise decisions by hunt teams, for instance, in looking for the adversary. Threat hunting is already searching for needles in a haystack. This work allows for more precise searching for the needles.”


Yair Manor, co-founder and CTO at threat coverage optimization platform provider CardinalOps, concurred: “The power of MITRE ATT&CK is that it became a common language across people, processes, and tools for describing TTPs,” he told Threatpost. “The VERIS + MITRE combination, if similarly adopted, can become that lingua franca among security teams to more holistically describe and catalog cybersecurity incidents, and exchange information between them. The combination of a unified language, structured data and data-driven decisions is foundational to allow the industry to join forces in the goal of threat coverage optimization.”


The Holy Grail of Security
--------------------------


It will be a heady brew: According to Alex Pinto, team lead of Verizon’s DBIR, the report’s focus will likely stay on security incidents, albeit with even more detailed information.


Beyond that, he expects that something new and wonderful may emerge from the new mapping: namely, the answers that security teams haven’t gotten in the past. “One of the holy grails of security is ‘Are we doing a good job at X?'” he said during a recent visit to the Threatpost podcast. “Because if you look at the way the DBR’s put together, it’s all about the failures. It’s all about, ‘These are all the things that happened that were bad,’ but we have a hard time tracking, ‘What are the things we were successful in stopping?'”


Imagine that: Something positive could come out of threat intel, instead of the typical pitter-patter of blood and guts, heartaches and bad headlines.


“One of the things you want to do with threat intelligence, whether it’s at the strategic or at the tactical level, is to use it to try to make sure your organization is learning from it,” pointed out Rich Struse, Director of MITRE Engenuity’s Center for Threat Informed Defense (CTID).


Struse and Pinto joined us to talk about the implications of this new mapping and to invite organizations everywhere to contribute and to help polish these powerful tools.


[Download the podcast here](http://traffic.libsyn.com/digitalunderground/Verizon_DBIR_take_2_mixdown.mp3), listen to the episode below, or scroll down to read a lightly edited transcript.



**It’s time to evolve threat hunting into a pursuit of adversaries.** [**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **Threatpost and Cybersixgill for** [**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **and get a guided tour of the dark web and learn how to track threat actors before their next attack.** [**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **for the LIVE discussion on September 22 at 2 PM EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**


Lightly Edited Transcript
-------------------------


**Lisa Vaas:** My guests today are Rich Struse, director of MITRE Engenuity Center for Threat Informed Defense – that’s CTID – and Alex Pinto, team lead of Verizon Data Breach Investigations Report: the very famous DBIR. They’re here to discuss a recently announced R&D project from CTID that’s supported by CTID members Verizon, the Center for Internet Security and Siemens AIG.


The project is to connect VERIS, which stands for Verizon’s Vocabulary for Event Recording and Incident Sharing and which is the framework that generates its famous DBIR, and the when and how described in MITRE ATT&CK. Rich and Alex are here to discuss this news and how connecting two of the most important cyber frameworks in the world can benefit security teams.


Welcome to the podcast, Rich and Alex.


**Alex Pinto:** Yeah, it’s great to be here.


**Lisa Vaas:** Super. My pleasure. Would you like to tell us a little bit about your backgrounds before we dive into the news?


**Alex Pinto:** My name is Alex, and I’m currently the team leader of the report team in Verizon.


And I’ve been over 20 years in security, at least the past seven have really been focusing on data science aspect. Of security. Driven by all the big data craze and things like that. And for the past three years, I have been leading the DBIR team and helping to put together the last two issues: the 2020, the 2021.


**Rich Struse:** And I’m Rich Struse. I’m the co-founder and director of the Center for Threat Informed Defense (CTID), which is a privately funded research and development center that we launched back in November of 2019 in MITRE Engenuity, which was launched at the same time, which is essentially a sister, a tech foundation, also a nonprofit that works alongside of MITRE to solve problems for a safer world.


And in that role, I’m really responsible for ensuring that the center and our members are working on impactful research and development projects, which we then make freely available to the world.


**Lisa Vaas:** Good work on both of your parts and your organizations. In [a blog](https://medium.com/mitre-engenuity/connecting-veris-and-mitre-att-ck-e3d00adbe5a4) on the news, Engenuity said that the move is going to allow for joint analysis of the information that ATT&CK describes.


As in, the behaviors that adversaries use to attack systems. Alongside with the incident, demographics and metadata that VERIS describes well. I want to hear all about that, but let me ask you, What’s the projected timeline for rollout?


**Rich Struse:** The project was actually released last week. So the project results are available on the center website and we released our projects on GitHub. So anyone who’s interested in taking a look at the methodology and then beginning to use it can do so today. That announcement was the announcement of the publication of the work.


We toiled away internally for a number of months between the centers’ R&D staff and our participants who supported this project. The project wrapped up last week.


**Lisa Vaas:** Thank you for that clarification. Well, tell me about it. Tell me in depth what’s going to change for security teams.


**Alex Pinto:** Well, I think it’s no secret both MITRE with the ATT&CK framework and Verizon with the VERIS standard, with both passionate about trying to help categorize and help, in a way, put things in buckets so they can be better measured and understood. We’re trying to figure out, really, what does the attack landscape look like … for everyone? But one thing that was very clear to both of us is that we were really looking at the problem from completely different perspectives. So VERIS very much has a top-down approach. As in, it’s very broad. So it will cover, quite frankly, all the different possibilities of what could potentially cause a data breach.


We go into places like environmental action on a breach, right? Quite literally the 20/21 DBIR: We had a tornado that hit a hospital, and medical records were spread across the county. So that is the data breach, but it’s not really one we’re used to thinking about in the cyber realm.


On a more operational risk approach for corporations to understand what are the specific ways they should be tackling, different likelihoods of data breaches for them. Not only on the more traditional “malware is happening” or “someone is hacking into our computers” realm.


On the other hand. Whereas it’s very broad, it lacks specificity, especially on these more technical aspects of a breach. Which is something that ATT&CK in the last, I don’t even know how many years, has been very good and very focused on that problem.


In fact, to describe exactly what are the technical steps for each one of those, right? So these are two standards that complement each other very well. And it has always been a desire, I believe from both our teams, to be able to, in a way, link them together. And this is something that actually has been a longstanding request if you may, right from people who are supportive of the standards.


So we believe that by putting those two different views, that top down from VERIS and the bottom up from ATT&CK, we can have something that looks like a more comprehensive standard that is up to the task of categorizing and documenting and potentially even fostering more sharing between different organizations.


**Lisa Vaas:** In your blog post, you describe how that’s going to feel for a user. Let’s say I’m sitting here, I’m trying to reverse engineer or figure out something. I’m on a security team. So I just plugged in, say, “It was Colonel Plum in the drawing room with the candle stick.” So what happens from there? We just go directly into this flow of the MITRE attack specificities?


**Alex Pinto:** Well, let me try to give you a more tangible example. Maybe this will be helpful. So ATT&CK, like I said, has been very good at handling the minutiae of specific attacks. And as such, several vendors, I mean, a large number of security vendors have been starting to [tune] their detection capabilities according to ATT&CK. So in a sense, I am concerned with lateral movements as an attack technique. So this specific product has those specific features or those specific detections that would combat this specific attack technique, right?


However, people are looking, everybody’s looking for coverage. In a way, “oh, I want to be able to defend against everything in ATT&CK.” While that is potentially impossible, or even at the very least cost inefficient. Would you be able to do all that coverage? So when you are relating this knowledge, this, this in a way boots on the ground approach of “which are the techniques that I have a capability to defend against with my security tools” with the kind of statistical overseen statistics from the DBIR as far as “well, actually for your industry in your region of the world, these are the things that are most likely to happen to you.” Or these are the most impactful kinds of attacks you may have, right? When you provide that linkage, right? In a way, what you’re providing for those companies is a blueprint of what potentially attacks.


ATT&CK map detections, at the bare minimum, they’re at the low watermark of what they are up against in their threat landscape. It provides a linkage between the kind of the strategic view that again, many CSOs and many … heads of security will look for. In data, in data analysis, like the DBIR with the actual, tangible improvements they could potentially do and the controls they could implement in their environments.


**Lisa Vaas:** OK. So what did R&D turn up? Anything surprising in hooking these two together?


**Rich Struse:** Well, I just wanted to make a point and then you may have more insight than, than I do actually, Alex, on this one, but you know, one of the key things that I’m really happy about with this project is that we took two well-established taxonomies. Essentially, we took two existing frameworks that really are designed with different purposes in mind, and we linked them together. We created the connective tissue that allows someone who has all the technical details about a particular incident or, you know, some stream of activity who wants to map it to some more of that. What VERIS is really good at capturing, or conversely, someone who has that bigger picture demographic, and now wants to go look to see if they can find the underlying technical detail, because ultimately, one of the things you want to do with threat intelligence, you know, whether it’s at the strategic or at the tactical level, is use it to try to make sure your organization is learning from it. So, you know, one of the key things is, “do I have this in my environment? Is this thing, which I just read a really humorous and well-written explanation of in the DBIR, is that something I need to worry about or that we’ve been impacted about?”


And that’s where having the description of the adversary behaviors, the TTPs, the tactics, techniques, and procedures that ATT&CK is all about, becomes really valuable. But I think the real thing I’m proud of is the fact that we just connected two great things. We’ve resisted the temptation to build a new thing or to take and add a bunch of “so what” information to ATT&CK.


Or for the VERIS team to take VERIS and expand it out to include all of ATT&CK. I think we approached this with a certain amount of humility to say, we have two good things here. Let’s just build bridges between them so people can link them.


**Lisa Vaas:** Well, congratulations. That is pretty awesome. Congratulations to both of your organizations. So, the DBIR has always been just a real pleasure to read. Everybody loves it. How’s it going to change now? It’s going to have a lot more depth to it. A lot of places to pivot to, I guess, to turn from the 10-mile view into on-the-ground nitty gritty?


**Alex Pinto:** Yeah, it really opens a lot of possibilities here. And the relationship between VERIS and ATT&CK, it’s something that ‘s always interested us, right? Because it dramatically expands the kind of data that we can collect. So everybody of course understands that the DBIR collects incident information from law enforcement, governments, IR partners. But we also collect what we call very broadly non-incident data. I’m doing air quotes. Which pretty much is information from security products. That could be helpful to understand the bigger picture. Ransomware of course has been a trend for a few years. Of course, we talked a lot about it on the last one, but when we need to add more color or more detail on this, we go to information from EDR providers that also shared their data. They anonymized data with us. So we do a different kind of analysis with those. Given that most security providers also have some sort of mapping with ATT&CK right now, we can make better use of the data they provide to us, having an automatic translation to VERIS, just using the mapping work that we did. And also it broadens the types of different data we could potentially collect and cover. I don’t expect the focus of the DBIR to change from the incidents, but I do believe that we’re going to be able to provide even more detailed information. One of the things, for instance, that we were barely touching on, which is one of the holy grails of security, is “are we doing a good job at X?” If you look at the way the DBIR is put together, it’s all about the failures. It’s all about, these are all the things that happened that were bad, but we have a hard time tracking, “What are the things we were successful in stopping?” For instance, if you look at malware-blocking information and you see that most of the malware that has been blocked, for instance, is a specific type of, let’s say trojan malware. And you look at the DBIR at the incident level data and there’s very little trojan percentage-wise, as far as one of the types of malware that’s being used.


That implies that we’re doing a good job stopping it, if that makes sense. But again, this takes two different levels of analysis. And this one, which is closer to the ground, as far as which malwares are blocked, it’s one that will help us a lot. Facilitate the analysis a lot for us. Given this ATT&CK to VERIS mapping.


**Lisa Vaas:** Well, great. Thank you, Alex. That makes a ton of sense that the mapping is going to give you a good idea of what’s working as opposed to constantly harping on what’s not working.


**Alex Pinto:** Yeah, we have some good news from time to time, right?


**Lisa Vaas:** Oh, we do need good news. Do you want to formally invite our listeners to get involved and explain how they might do that?


**Rich Struse:** There’s a couple of different ways. You know, sort of, from my perspective in the center, you know, we are encouraging, just like all of our R&D projects, which we make freely available to the world. You know, we want people to come and take a look at it, try to use it, tell us what we got. Tell us what we got wrong. We’re always looking for community contributions and enhancement requests, bug fixes and all of that, because ultimately, it’s the practitioners who are using this to try to link these two frameworks together who are going to tell us whether or not we got the right answer here. The other thing I would say though, is this work allows people to connect the ” so what?” in that sort of strategic view that Alex was talking about, not just with ATT&CK, but you know, one of the things we’ve been doing in the Center is releasing a range of projects and data sets that then connect ATT&CK to other things.


So for example, you know, if by looking at the DBIR, you understand a particular action attribute that is of concern to you. You then use this mapping we’re talking about today to map that, to attack techniques and sub- techniques, you can now, using other freely available [Center R&D] go and say, “all right, if I care about this TTP, this particular tactic and technique and procedure, what are the NIST 853 controls that I should be looking at?” Or “what are the Azure security capabilities?” So the AWS security capabilities leveraging the work that the center has done. So, you know, our perspective is we’re trying to continually build out this knowledge graph that is available to the community, so that individual defenders don’t have to go and do that knowledge discovery themselves, that they can actually leverage whether it’s the mapping from VERIS to ATT&CK or the mapping from ATT&CK to the NIST framework or to particular security capabilities in the cloud, whatever it is, we’re trying to make that much more systematic.


We’re trying to really, really reduce the barriers and the friction so that defenders can spend the vast majority of their time and energy, I don’t know, keeping us safe from the bad guys.


**Lisa Vaas:** I hope in the future, you guys will funnel some success stories my way. It’d be so interesting to talk to some defenders to give us a before and after perspective on this news, like “oh boy, this is what it would have been like before this new mapping,” and “this was what it was like after that.”


**Alex Pinto:** Sounds good.


**Lisa Vaas:** Well, we are running out of time. Is there anything else that you’d like to leave our listeners with? Final thoughts?


**Rich Struse:** Just wanted to make sure that people understood that, you know, this is like other Center R&D projects. The only way it works is because our members, the center members, we now have 28. Those organizations make a conscious effort to commit the expertise and time and resources, did not only do this work, but then do this work and have us release it to be freely available to the world. So I really want to thank not only Verizon, but Siemens, who supported and participated in this work.


And then the Center for Internet Security that participated in the project: without them as a whole, this project simply wouldn’t have existed. So you know, I think the community owes them all a thanks for doing this work and then making it available.


**Lisa Vaas:** Well, I join you in thanking them. Thank you, Siemens. And thank you CISA. Thank you so much. I really appreciate you coming on to chat about this great new development. So thank you very much. I hope we can get you back on in the future.


**Alex Pinto:** It’ll be a pleasure.


**Rich Struse:** Thanks for chatting.




#### Tags:
[[it’s]] [[know,]] [[ATT&CK]] [[VERIS]] [[Vaas:]] [[I’m]] [[Pinto:]] [[DBIR]] [[Well,]] [[right?]] [[ThreatPost]]
