# Podcast: Could the Zoho Flaw Trigger SolarWinds 2.0?
### Companies are worried that the highly privileged password app could let attackers deep inside an enterprise’s footprint, says Redscan’s George Glass.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175553)
+ Date: October 18, 2021  4:55 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/12/18135402/solar-flare-e1608317663121.png)
A month ago, the FBI, CISA and the U.S. Coast Guard Cyber Command (CGCYBER) warned that state-backed advanced persistent threat (APT) actors are likely among those who’d been actively exploiting a [critical flaw in a Zoho-owned single sign-on](https://threatpost.com/cisa-fbi-state-backed-apts-exploit-critical-zoho-bug/174768/) and password management tool since early August.


At issue was a critical authentication bypass vulnerability in Zoho ManageEngine ADSelfService Plus platform that could lead to remote code execution (RCE) and thus open the corporate doors to attackers who can run amok, with free rein across users’ Active Directory (AD) and cloud accounts.


The Zoho ManageEngine ADSelfService Plus is a self-service password management and single sign-on (SSO) platform for AD and cloud apps, meaning that any cyberattacker able to take control of the platform would have multiple pivot points into both mission-critical apps (and their sensitive data) and other parts of the corporate network via AD.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


It is, in other words, a powerful, highly privileged application that can act as a convenient point of entry to areas deep inside an enterprise’s footprint, for both users and attackers alike.


In a recent Threatpost podcast, George Glass, head of threat intelligence at Redscan – a subdivision of the Kroll responder team that manages detection and response – said that the incident has worried the firm’s main clients, who are concerned that it could turn into a similar scenario to the the calamitous, widespread [SolarWinds](https://threatpost.com/solarwinds-financial-crisis-podcast/168677/) attacks in April.


In the SolarWinds supply-chain attacks, “a trusted third party is impacted by some sort of zero day where there is very little in the way of detection for new and complex threats,” Glass explained.


Incident responder teams try their best to maintain a good suite of detections for waves of follow-on activity after events like SolarWinds, but all bets are off when it comes to zero days like the Zoho flaw, Glass said.


“There’s always the chance [where] a new zero day comes along and there are no detections in place for that,” he said. “So we do our absolute best to keep ahead of that trend and track these vulnerabilities, test them ourselves against our sandbox environment. To essentially build these detections and try and stay at least in step with some of these APT threats.”


He came on the podcast to talk about Zoho and other recent vulnerabilities being exploited by APT groups – including [Azure OMIGOD](https://threatpost.com/azure-zero-day-supply-chain/169508/) and [Office MSHTML](https://threatpost.com/microsoft-mshtml-ryuk-ransomware/174780/) – and to outline the industries most at risk, how companies can mitigate that risk, and the steps companies should take if they become a victim of APT or other cyber attacks.


[Download the podcast here](http://traffic.libsyn.com/digitalunderground/101521_Kroll_George_Glass_mixdown.mp3), listen to the episode below or check out the lightly edited transcript beneath it.


***Also, check out our [podcast microsite](https://threatpost.com/microsite/threatpost-podcasts-going-beyond-the-headlines/), where we go beyond the headlines on the latest news.***




Lightly Edited Transcript
-------------------------


**Lisa Vaas:** Hello, and welcome to the Threatpost podcast. I’m your host, Lisa Vaas. My guest today is George Glass, head of threat intelligence at Redscan, which is a subdivision of the Kroll responder team that manages detection and response: kind of like an MSP. He’s here to talk about a recent alert from the FBI and two other U.S. cyber agencies about state- backed advanced persistent threats – APTs – and how they’ve likely been exploiting a flaw in the Zoho single sign on and password management solution since last month (August). Welcome to the Threatpost podcast, George.


**George Glass:** Thank you very much for having me today.


**Lisa Vaas:** Great. Well, I was hoping that before we dive into the vulnerabilities and what businesses should know about them, you might be able to tell us a little bit about what you do on the Kroll responder team and about your own background.


**George Glass:** Certainly. So my team is responsible for managing the threat intelligence side of detection and response. So that includes things like [undetectable] IOC [indications of compromise] procurement and I’m sending those out to detection technologies. We also manage vulnerability awareness, alerting our clients to new vulnerabilities that we believe they may be impacted by and providing them remediation advice for how to better secure their networks.


**Lisa Vaas:** Well, it sounds like you’re really at the forefront of companies that are experiencing threats, including these attacks from this APT. Could you give us some front-of-the-battle flavor about the details and key concerns these companies are facing with regards to the flaws, not only Zoho, but other vulnerabilities that are being exploited by this APT group?


Of course.


**George Glass:** Yeah. I think it’s fair to say that main clients are worried about a similar scenario to SolarWinds, whereby a trusted third party is impacted by some sort of zero day where there is very little in the way of detection for new and complex threats. We always try our best to maintain a very good suite of detections for follow -on activity.


But there’s always the chance [where] a new zero day comes along and there are no detections in place for that. So we do our absolute best to keep ahead of that trend and track these vulnerabilities, test them ourselves against our sandbox environment. To essentially build these detections and try and stay at least in step with some of these APT threats.


**Lisa Vaas:** As I understand it, you guys had already spotted the Zoho vulnerability, is that correct?


**George Glass:** Yes. There was an announcement to a responder and Redscan clients keeping them updated of some of the ways that threat actors are using the vulnerabilities in particular.


So it’s an APT threat and indeed ways of checking to see if vulnerable systems have already been compromised.


**Lisa Vaas:** And what are you seeing? Which industries are most at risk?


**George Glass:** Well some of these vulnerabilities tend to span the gamut. We are trusted by a lot of industry verticals to protect their estates.


But I think it’s fair to say that some of the more public facing clients are particularly at threat in terms of threat modeling things like transportation, technology, healthcare it’s not just the APT groups that are attacking these companies and so we’re seeing a lot of ransomware attacking such industry verticals.


There’s two very impactful threat groups, specifically targeting national infrastructure. And all industry verticals that are aligned with government in some way are potentially at risk.


**Lisa Vaas:** And you said that you’re seeing two APT groups. What are you talking about? Cyber espionage and ransomware?


**George Glass:** Yes, indeed. Yeah, the amount of money that ransomware groups have at their disposal now from a successful extortion attacks really does put them, in my opinion, in some of the same playing fields as advanced, persistent threat groups in terms of their resources that they can call on and some of the talent pool that is working for these groups.


So I think those two state-sponsored APT groups and ransomware threat groups are the two of most concern.


**Lisa Vaas:** So helping companies mitigate risk…?


**George Glass:** Well, that’s a very tricky thing. And I, I think it really depends on the company’s risk appetite: again, what resources they can deploy.


But you know, in a, in a slightly selfish way, I think that having a a good source of threat intelligence and the ability to understand vulnerabilities as they pop up, be these zero days or vulnerabilities that have patches available for them, understanding the potential impacts to your business, what operational risks a successful exploit could potentially lead to. And again, in this case, I’m thinking of cyberespionage and ransomware and choose where to apply the limited resources that you have to plugging those holes. Of course that’s not, doesn’t always go quite to plan.


But in those cases, it’s a case of defense in depth: running EDR and seeing tooling internally to catch the follow on activity after a successful exploits of a, you know, a potential zero day or something like.


**Lisa Vaas:** I hate telling these organizations the same thing, time and time, the obligatory and nagging part of every discussion on …well, let me ask you about what they should do if they do become a victim of an APT or any other kind of cyber attack.


**George Glass:** Well, I think it’s important as soon as a potential infection or an incursion by a threat group is detected in some way that the organization is immediately moved to an instant response setting and ideally they’d have instant response playbooks in place so that everyone knows what they’re doing, who to engage, what companies to engage, you know, what insurance they need to maybe rely on to pay for some of that. And allow the instant responders, all of the necessary resources they need to do their job effective.


Because I think in a lot of these cases, the threat actors hang around in the environment. They certainly know who’s being engaged. What response teams are doing to try to evict them from the net. And so it’s absolutely paramount that that instant response team have the ability to stay where they need to and do their job effectively.


**Lisa Vaas:** Who’s typically on an incident response team?


**George Glass:** Typically there’d be some digital forensics experts, obviously instant response experts who’re hopefully equipped with the correct threat intelligence to let them know where to look for a particular threat actor activity, people that can effectively communicate throughout the business as well to any relevant teams that may need to engage with that.


Public relations, all of the things that come with a Tier 1 incident.


**Lisa Vaas:** And of course Redscan would be in that group.


**George Glass:** Yes, absolutely. Yes. Redscan approaches a session ready to be engaged.


**Lisa Vaas:** I’m sure there are a lot of companies out there that are happy that you guys are there to help them out when things get bad. Well, thank you so much, George. We’re coming up against time limit here. Is there anything else you’d like to leave our listeners?


**George Glass:** I think what I’d like to leave everyone with is this year has been pretty significant for the amounts of zero day exploits and vulnerabilities that have been quickly patched, but indeed workarounds have been found extremely quickly after the patch and to maintain as much vigilance as possible on those devices that you know, are critical to your business, be that stuff that you’ve spun up over the pandemic to enable remote working, make sure they are monitored. Make sure you are patching efficiently. And have your instant response playbooks ready. Yeah.


**Lisa Vaas:** Talk about having to do it fast with the VMware vulnerability announced yesterday and being scanned with VMS. Well, thank you so much, George. I really appreciate you taking the time to come on the podcast and chat with us about these important issues.


**George Glass:** Thank you very much for having me.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Vaas:]] [[Glass:]] [[it’s]] [[Zoho]] [[Well,]] [[Threatpost]] [[Redscan]] [[podcast]] [[I’m]] [[ransomware]] [[ThreatPost]]
