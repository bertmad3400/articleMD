# ‘Pay Ransom’ Screen? Too Late, Humpty Dumpty – Podcast
### Splunk’s Ryan Kovar discusses the rise in supply-chain attacks a la Kaseya & how to get ahead of encryption leaving your business a pile of broken shells. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168962)
+ Date: August 27, 2021  8:00 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/04/05152927/eggs-chickens-e1617650984482.jpeg)
Systems actively encrypted? Are they showing a screen that says “pay the ransom?”  

Too late: At that point, you’re probably toast. A few options, none great:


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“When you have systems that are actively encrypted and they’re showing a screen that says, ‘Pay your ransom,’ Humpty Dumpty has fallen off the wall,” according to Ryan Kovar, former DARPA engineer and current distinguished security strategist at [Splunk](https://www.splunk.com/), which is a software platform that searches, analyzes and visualizes the machine-generated data gathered from the websites, applications, sensors, devices, etc. that make up IT infrastructure and business.


“Eggshells are everywhere and you cannot put them back together. Again, you are now in a disaster recovery phase, not an investigation and detection phase, where I tend to look. Sorry about that,” he said.


Besides the sky-high ransoms and ferocious growth in attacks, there’s actually nothing new about the tactics, techniques and procedures (TTPs) that give ransomware a foothold, Kovar says. He’s been defending against the same TTPs used by nation states and criminal organizations for 20 years. “And the majority of places that you can actually protect your organization are all left of that, you know, left of the actual impact, right?” he said when he visited Threatpost podcast recently. “The encryption or any sort of thing like that, that’s the final phase of a ransomware attack.”


He alluded to [Sophos’s report](https://www.sophos.com/en-us/press-office/press-releases/2021/05/adversaries-spend-more-than-250-hours-undetected-in-target-networks-on-average.aspx), which found that by the point that systems/files have been encrypted, the attackers have been kicking back for a median dwell time of 11 days. According to Sophos’s [Active Adversary Playbook 2021](https://news.sophos.com/en-us/2021/05/18/the-active-adversary-playbook-2021/), the longest undetected intrusion lasted 15 months: a vast swath of time that organizations should use to scour their telemetry to detect threats before they fall off the wall and into the arms of extortionists.


“You have nine to 10 days of utilizing traditional techniques and tools that you have at your disposal to find a ransomware operator before they encrypt the data,” Kovar remarked.


How do you get to the left of that [Lockheed Martin Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html), where the “boom,” in this case, is encryption?


It’s bread-and-butter stuff, such as paying attention to spearphishing, where the majority of ransomware incidents start, he said: “Really boring stuff.”


For more “boring stuff” that can help to save your organization from turning into a pile of shells, check out Kovar’s advice on discovering how threat actors do reconnaissance, gain persistence and move laterally, along with his thoughts on the new crop of supply-chain attacks, with [Kaseya](https://threatpost.com/kaseya-attack-fallout/167541/) being a case in point.


[Download the podcast here](http://traffic.libsyn.com/digitalunderground/081921__Ryan_Kovar_Splunk_mixdown.mp3), listen to the episode below, or scroll down to read a lightly edited transcript.



***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


Lightly Edited Transcript
-------------------------


**Lisa Vaas:** Ryan, welcome to the Threatpost podcast.


**Ryan Kovar:** Thank you very much. I’m excited to be here.


**Lisa Vaas:** I am excited to have you. I just wanted to start off by reading your bio. It’s awesome. It mentions dogs. And it uses cyber as a verb. **Ryan** Kovar has over 20 years of experience of cyber and has done everything from pulling miles of cat five cable on an aircraft carrier to learning that he didn’t want to be a malware RE, is that research engineer?


**Ryan Kovar:** Reverse engineer. It was a big part of my job when I was at DARPA where human nation, state threats and looking at malware and trying to figure out what it does. And I took a wonderful course at sands led by Leonis Eltser on malware, reverse engineering, and I got today three and I was doing.


And by the end of day three, I realized that I was questioning everything in my life and my will to live and that I could always hire or work with an RE rather than being one. So it was a very pivotal point in my career.


**Lisa Vaas:** Oh, that’s awesome. You most recently were at DARPA on a team dedicated to detecting and mitigating advanced threats.


Then you move to Splunk as a distinguished security strategist. And you’re now teaching threat hunting. You’re attempting practical security research and solving fun problems for folks around the world. And here’s where the dogs come in. Kovar loves Bernese mountain dogs and wire data. And he despises printers.


I love that. Well, the print nightmare scenario is going on there.


**Ryan Kovar:** Well done. No, that’s a good fun for today’s today’s world and yeah, I can run 20, 35, $50 million LANs and networks, but if you try to have me print a form I will fail horribly. It would be you can put a gun to my head andI’d just dial down and say, I guess it’s over now.


This is my life.


**Lisa Vaas:** It’s good to know your limitations and to threaten, to threaten people who cross your boundaries. Well, I imagine, you know that working at Splunk has given you unmatchable insight into vulnerabilities that come from other unexpected places, similar to how they’re coming from supply chains, a la Kaseya and we did get you on here to talk about how Kaseya that the supply chain attacks are the latest example of how security vulnerabilities are coming from unexpected places. So what are these unexpected places besides supply chain attacks?


**Ryan Kovar:** The supply chain ones that are interesting if for no other reason.


Honestly, if I were, if you were to ask me to stack rank the last, you know, the five most interesting vulnerabilities or attacks in the last year, they’ve all been some sort of derivative of supply chain. I think the most interesting vulnerabilities and attacks that I’ve seen over the last year really have all been supply chains.


But what I think is probably the most interesting about them is that they are all different, right? If you looked at SolarWinds, that’s a very traditional, died in the wool, what we would define or NIST or MITRE would define as a supply chain attack. It’s a vendor with compromised, malicious code injected.


It was downloaded and executed very clear, but then there is this other vulnerability [in code testing company Codecov], which I think a lot of people heard about, but unless you’re kind of in the DevSecOps world might not have made a lot of sense. It was a vulnerability that occurred from a company where, you know, basically this company sold software that injects itself into the CIC pipeline for software developers and that they were manipulating things within Codecov that was then going downstream to these other companies and that was causing them to be breached.


So that’s another supply chain. And then. Kaseya, a lot of people would argue that’s not a supply chain attack. I would argue that it is, but it’s a matter of perspective from the angle of the customers of the MSPs who were affected by the vulnerability of Kaseya.


If I were to do the top five, the top three interesting things this year for me for vulnerabilities and attacks are all actually different derivatives of supply chain.


**Lisa Vaas:** Well, I guess it does depend on what you define as a supply chain. Certainly we’ve been hearing about multiple poisoning of code repositories.


So that’s that there’s for sure a supply chain.


**Ryan Kovar:** Yeah, there was that great research done early this year, where a developer put basically a harmless callback into open source Python and JavaScript libraries and waited for large companies to execute that library in their own development environment and have it reach out to his system.


Right. And that’s another example of that supply chain confusion, because those are all things that are chained. Some of the research I’ve been doing lately, my team, has been around persona you are. And what perspective you have as that persona defines what you think of as a supply chain. And then how do you actually detect the supply chain checks per persona?


So the way the DevSecOps personality would look at supply chain. It’s much different than how a traditional network defender or SOC operator would. And so a lot of our work right now is kind of, as silly as it sounds, we’re just having a problem with taxonomy and speaking about this, so we’ve heard about supply chain is nations and nation states attacking the medical supply chain for COVID vaccines, and that’s actually a whole different type of supply chain attack, you know, and, and it’s not a software supply chain attack. It’s actually attacking the supply chain of a national medical inventory.


If you talk to someone at a large defense, industrial base, like a Lockheed or Boeing or some company like that, they would define supply chain as the organization that supply them parts and how they look at supply chain and different persona and the same word, it’s pretty confusing. I think. So there’s a lot of ground to cover there for people to be more clear on.


**Lisa Vaas:** Yeah. I mean, it’s like if we look to the Suez Canal blockage, that’s certainly a supply chain, but in a very analog version of supply chain.


**Ryan Kovar:** Sure. And if that had been a cyber operation, for example, if one of those locks in the Suez canal had been attacked by an adversary to intentionally disrupt the supply chain of the world, you know, that’s another example where we’re we’re munching words together and mingling meanings.


**Lisa Vaas:** Well what difference does it make though? The taxonomy? I mean, people in the healthcare industry know what they’re talking about when they talk about their own COVID vaccine supply chain. I’m trying to visualize, what kind of problems you get into because of the taxonomy issue?


**Ryan Kovar:** Honest? the biggest issue, no one in the security world is an expert because everything moves too fast. Right? That might be a little bit of a controversial statement, but like some of the biggest technology that we depend on for day to day life now was only invented 2, 3, 5 years ago. So it’s difficult to call anyone in my opinion, that dyed in the wool expert on these things.


And so I say this because if you accept the hypothesis, We start discussing supply chain solutions or supply chain defenses. If you are not well-read and versed on the specific subject that you care about, you’re going to waste a lot of time and energy trying to implement defenses or technologies that are defending against a type of supply chain that you are not susceptible to.


I think the reason why MITRE ATT&CK has taken off and been so popular. Is because for the first time it provided a common taxonomy for defenders, researchers, attackers, CISOs, business leaders, news media and everyone to communicate with. And it’s going to be vital to have something similar on supply chain attacks.


**Lisa Vaas:** Okay, well, that’s fair enough. That’s interesting. Okay. So let me ask you you, you are going to be a good expert for us to hear from when it comes from things like resiliency and the costs associated with these attacks. I mean, I think you mentioned ransomware attack costs and we all know how crazy those are getting. When it comes to the concept of ransomware recovery, what insights do you have for us there?


**Ryan Kovar:** I think when we talk about ransomware and, you know, we’ve talked a lot of the news, especially after some of the recent breaches to CEOs to say on being no different than I, you know, I’m talking about names of companies using formal nouns, but we could just say dollar sign Acme company.


Right. There’s really doesn’t matter what one, they have a challenge to face: at some point, they have to make a business decision of, do I pay a ransom or not? And at that point it probably means you’ve gone down all the non-paying ransomware options and ransomware payments can be very expensive.


What most of the case studies I’ve read have shown is very rarely does paying the ransom actually cause you to recover data significantly quicker. That’s a little bit of a generalization, but the reality is that although the ransoms may work, they may get the decryption key, it does not result in an immediate cessation of attack or impact, right?


You still have to decrypt all these files, and it takes a long time. And on top of that, they’re not always a hundred percent successful and you still have downed systems, and modern day networks are incredibly interconnected. And so one system being down, well, you bring up another one, it may still mean that the other systems are down until you’ve brought up all these other systems, or you could have clusters of servers that require a certain number of servers to be all up and operational and to clear out any errors, you have to have them all up.


Right. So when I talked about the cost of ransomware, you know, it’s not just the paying the ransom and you’re done, you know, it’s not like you get the media equivalent that people think of as kidnapping, right? And if you pay your ransom, you get the human being back and everything’s fine. No, it’s much more complicated than that. It’d be almost like getting someone back, you know, we’ve got a coma and you’re reeling them back, right. There’s not an immediate return on that investment in some ways. And that’s where the cost comes in. In my view.


**Lisa Vaas:** Yeah. And I’ve, I’ve read studies that say that the actual cost of ransomware is something like 20% of the entire costs.


The rest of the lionshare being lost productivity, investigations, fixing the issues, yada yada, yada. Let me ask you, you’re in a position of power there over at Splunk. You’re looking at all this data coming from websites, apps, sensors, devices, etc. What can we do with that when it comes to these attacks? I mean, how do we make use of that?


**Ryan Kovar:** I and probably every other person in the world in cyber security spend a lot of time thinking about that. And to be honest, if I have the perfect solution you would be talking to Ryan Kovar, the CEO of the hottest new anti ransomware startup.


The reality is this is a very difficult problem to solve, but where I tend to focus is there’s an analogy that I use around ransomware, which is the majority of the times when you see it in the news or when I’m called, it’s a little bit of a Humpty Dumpty has fallen and there’s egg yolk all over the floor, right?


When you have systems that are actively encrypted and they’re showing a screen that says, pay your ransom, Humpty Dumpty has fallen off the wall. Eggshells are everywhere and you cannot put them back together. Again, you are now in a disaster recovery phase, not an investigation and detection phase where I tend to look.


There was a great [white paper](https://www.cert.govt.nz/it-specialists/guides/how-ransomware-happens-and-how-to-stop-it/) released by CERT New Zealand last week. I highly recommend anyone interested in ransomware reading it and they kind of break it out, all the ransomware phases into distinct areas. And what I like about it is it shows that ransomware is not a magical thing.


It has all the same TTPs as how I’ve been defending against nation states and criminal organizations for 20 years. And the majority of places that you can actually protect your organization are all left of that, you know, left of the actual impact, right? The encryption or any sort of thing like that.


That’s the final phase of a ransomware attack. And there’s a great white paper, I believe it’s by Sophos or Proofpoint. They say the dwell time for the average ransomware affiliate today is something like nine to 10, 10 days. So you have nine to 10 days of utilizing traditional techniques and tools that you have at your disposal to find a ransomware operator before they encrypt the data.


So in my background, we use a lot of the Lockheed Martin kill chain and the concept of being left of boom and boom in this case is encryption. So what I would stress and what I recommend to people is, really heavily, do your cybersecurity, bread and butter, your cyber hygiene left of encryption. How did they get on the network?


Something like 80 to 90% of all ransomware incidents start in spearfishing. How did they get persistence? How are they moving laterally? How are they doing reconnaissance in your network? These are all areas that the logs of transferring applies. There’s going to be logs. There’s going to be evidence.


There’s going to be detections that you can run. And if you can stop them there, you don’t have to worry about, can I pay the rent? Right. And on top of this, you get into things like network segmentation, and this is all really boring, you know, compliance and doing your, your, your day job every day. But that’s in reality the best way, in my opinion, to defeat ransomware.


**Lisa Vaas:** Fair enough. What are your thoughts on operational resiliency? I want to know how companies bounce back because I, as I complained about in my previous podcast, T-Mobile blocked me when I tried to change my pin earlier this week, and that didn’t strike me as operational resiliency.


**Ryan Kovar:** The biggest thing I can recommend and I have seen successful is planning and testing and doing it over and over again. I’m a big fan of doing tabletop exercises where you walk through step by step and kind of do worse scenario. I think you find a lot of the problems that you might have ahead of time.


The followup after that is saying like, okay, we were encrypted. Can we recover? And once again, I mean, I’ve long said the most thankless job in the world is a backup admin. No one cares about your job. If you do it right, a million times, it’s 1,000,001 that you screw up that they suddenly need to restore from.


And I think that’s kind of a similar area here where if you want to make sure that you’re protected against ransomware, There’s a couple areas that you need to invest time and money in. Right. Testing and verifying your backups is one of those typical critical areas, because then you will have options about paying or not paying the ransomware.


It’s much easier to restore from a backup than it is to restore from encrypted data. And you can have something in your control to viscerally test and be more resilient about. The other aspect is having people on Rolodex. Right? What you don’t want to have happen is a ransomware event. You’re a company that maybe, you know, maybe you’re a company that only makes a billion dollars a year, 500 million or 10 million.


Do you have the in-house expertise to start combating an encryption issue? Probably not. Maybe you do. Maybe you don’t, but you should have a plan for that. That can be a, a legal agreement that could be having an incident response firm on retaining. Or that could be outsourcing to a [managed detection and response, or MDR] team like Red Canary or some other company.


I’m not necessarily recommending off the top of my head, but I I’ve seen the great work that a company like Red Canary does around these things. And having those things as an option for you increases your resilience for defending and detecting and responding and recovery from ransomware.


**Lisa Vaas:** That all sounds super sensible. And it also gives me an idea for a series on unsung heroes. One focusing on backup admins.


**Ryan Kovar:** There you go. There they are the most unsung hero in the world, their critical job. And let me tell you no one, no one cares until they do.


**Lisa Vaas:** Exactly what we’re up against our time limit here, Ryan, any points you’d like to leave people with?


**Ryan Kovar:** I think the one thing that I can say is to fight and deal with things like ransomware or Kaseya, your number one advantage is having telemetry and having data to see. And if you can’t see when you’ve been attacked, if you can’t find things before they’re executing their ransomware, then you’re going to continue to be asking questions about resilience and do we pay or not pay? So I guess if there’s anything to leave with the biggest one is find your data. Look at your telemetry and try to stop it before the encryption happens.


**Lisa Vaas:** Take care of your data. Good enough for me. Thank you so much, Ryan. It’s been a real pleasure.


**Ryan Kovar:** Sure, absolutely. Listen, you have a great day.


**Lisa Vaas:** You too.




#### Tags:
[[ransomware]] [[Ryan]] [[that’s]] [[Vaas:]] [[know,]] [[Kovar:]] [[it’s]] [[you’re]] [[chain.]] [[It’s]] [[ThreatPost]]
