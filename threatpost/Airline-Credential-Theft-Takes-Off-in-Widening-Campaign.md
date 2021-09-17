# Airline Credential-Theft Takes Off in Widening Campaign
### A spyware effort bent on stealing cookies and logins is being driven by unsophisticated attackers cashing in on the initial-access-broker boom.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174264)
+ Date: September 16, 2021  2:26 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/16140859/Airplane-e1631815781464.jpg)
A two-year-old espionage campaign against the airline industry is ongoing, with [AsyncRAT](https://threatpost.com/attackers-discord-slack-malware/165295/) and other commodity remote-access trojans (RATs) helping those efforts take flight. The campaign can effectively be a bird strike to the business engine, so to speak, resulting in data theft, financial fraud or follow-on attacks, researchers said, who have uncovered new details about the perpetrators.


According to Tiago Pereira and Vitor Ventura at Cisco Talos, “Operation Layover” is likely the work of an unsophisticated threat actor based in Nigeria, which has been active on the cybercrime scene for at least six years in various campaigns against multiple sectors.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“[The attacker] doesn’t seem to be technically sophisticated, using off-the-shelf malware since the beginning of its activities without developing its own malware,” the researchers noted in a [Thursday posting](https://blog.talosintelligence.com/2021/09/operation-layover-how-we-tracked-attack.html). “The actor also buys the crypters that allow the usage of such malware without being detected, [and] throughout the years it has used several different cryptors, mostly bought on online forums… This shows that a small operation can run for years under the radar, while still causing serious problems for its targets.”


**Driven by an Initial Access Broker Boom**
-------------------------------------------


The goal has been to pilfer credentials and cookies, which the attacker can offer to more technically savvy cybercriminals, researchers said. These big-game hunters use them for initial access in much larger attacks involving ransomware or business email compromise (BEC) hits, they added.


And indeed, the cyber-underground market for initial access brokers (IAB) is [booming by all accounts](https://threatpost.com/booming-cyber-underground-market-initial-access-brokers/166965/). The business of gathering access to vulnerable organizations and then selling those to the highest bidder on the Dark Web has especially been on the rise as ransomware-as-a-service has grown in popularity, according to Stefano De Blasi, cyber-threat intelligence analyst at Digital Shadows.


“IABs have reached a significant level of success and notoriety in the past 18-24 months, given the parallel booming of the RaaS model,” he told Threatpost. “In this environment, IABs provide ransomware actors with a seemingly infinite pool of victims that are already compromised and thus merely require ransomware affiliates to deploy the malware.”


This market spells dollar signs (or perhaps [Bitcoin signs](https://threatpost.com/financial-cybercrime-cryptocurrency-public-ledgers/169987/)) for lower-level cybercriminals.


“The black market for web cookies, tokens and valid credentials is way too valuable when compared with the economy in their home countries for them to stop,” the Cisco Talos researchers noted. “These are the actors that feed the underground market of credentials and cookies, which can then be used by larger groups.”


They added, “These kinds of small operations tend to fly under the radar and even after exposure the actors behind them won’t stop their activity. They abandon the command-and-control (C2) hostnames — which in this case are free DNS-based and they may change the crypter and initial vector, but they won’t stop their activity.”


**The Attack Flight Plan**
--------------------------


The attacks, like many malware campaigns, start off with social-engineering emails, according to Pereira and Ventura. The attacker sends emails to targets, which spoof legitimate aerospace organizations. They purport to have a link to a PDF file; the “files” feature air travel-related names, referencing things like “trip itinerary details” and “bombardier.”


In reality, the links send users to a .VBS script hosted on Google Drive, which encrypts the final RAT payload and drops it onto the victim’s computer. The script is the Snip3 crypter, which remains under active development and which is offered as a crypter-as-a-service, according to [previous research](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader) from Morphisec.


It’s worth noting that Microsoft flagged parts of the campaign [back in May](https://threatpost.com/loader-aviation-spy-rats/166133/), offering a few additional technical details on the infection chain.


“Attackers use the remote access trojans for data theft, follow-on activity and additional payloads, including [Agent Tesla](https://threatpost.com/agent-tesla-microsoft-asmi/163581/), which they use for data exfiltration,” the computing giant tweeted. “The trojans continuously re-run components until they are able to inject into processes like RegAsm, InstallUtil, or RevSvcs. They steal credentials, screenshots and webcam data, browser and clipboard data, system and network into, and exfiltrate data often via SMTP Port 587.”


The Cisco Talos research team meanwhile more recently uncovered a few attacker-controlled domains used for command and control (C2) for the aviation effort, including akconsult[.]linkpc[.]net, which is being used to host the AsyncRAT payload. Since that server was using TLS to encrypt the C2 communications, the researchers then performed a search for other servers using the same certificate thumbprint – and uncovered eight more domains linked to the campaign, along with more than 50 individual malware samples.


“Most of the domains were first seen either in May or June 2021,” Pereira and Ventura explained. “The oldest of the list seemed to be active only for a couple of days, without many samples using it. However, the URL e29rava[.]ddns[.]net was always active with several samples using it as C2.” They went on to link it with 14 malicious VBS crypter files used in the aviation campaign.


**About the Campaign Pilot**
----------------------------


The researchers also made an effort to see what other details they could turn up about the threat actor.


For instance, using passive DNS telemetry, Pereira and Ventura compiled the list of IPs used by the domain akconsult[.]linkpc[.]net. The results show that roughly 73 percent of the IPs were based in Nigeria.


They also did a search using the “akconsult” keyword to “This search revealed a malware sample and a user handle [“Akconsult”] mentioned on the site hackingforum[.]net,” they said. “A search on this forum turned up several indicators of the actor’s [identity].”


For instance, in forum interactions, the user linked an email address — kimjoy44@yahoo[.]com — and a Telegram account — @pablohop, both of which were then linked to the aviation-themed campaign. On Skype, the threat actor’s email is associated with the username “abudulakeem123.”


The researchers were also able to link a few early campaigns (starting in 2013) to the akconsult keyword, and from there to another handle, “Nassief2018,” found on another popular hacking forum.


Other researchers have uncovered other information about the attackers:



> 
> Nigerian guy.  
> his name: "Samuel Eyiba"  
> Used phone number: +2349010725503   
> EML: kim.joy001@gmail.com  
> EML2: kimjoy44@yahoo.com
> 
> 
> nulled account: kimjoy  
> crypters account: kimjoy  
> hackforums account: Nassief2018  
> perfectmoney account: 8547265
> 
> 
> — .sS.! (@sS55752750) [May 14, 2021](https://twitter.com/sS55752750/status/1393283668962119685?ref_src=twsrc%5Etfw)
> 
> 



“Some of this information matches what we found on our own research, others are completely new and we have not been able to confirm this Twitter user’s claims,” Pereira and Ventura wrote.


John Bambenek, principal threat hunter at Netenrich, noted that this kind of breadcrumb research can offer a fairly complete picture of an adversary over time.


“The longer an adversary operates, the more likely they leave enough fingerprints to lead to accurate attribution,” he told Threatpost. “Every attack has a rich array of metadata that, in and of itself, may be meaningless, but the correlation of that metadata can lead to correlations and getting to know much more about attackers. The key of intelligence analysts is to extract all the metadata and attributes from those attacks and store them over long periods of time so they can identify those patterns over the long term.”


**Airline Attacks Not Likely to Be Grounded**
---------------------------------------------


Despite the cyberattackers’ relative lack of sophistication and tech acumen, they present a major threat to organizations, the Cisco Talos analysis concluded.


“Many actors can have limited technical knowledge but still be able to operate RATs or information-stealers, posing a significant risk to large corporations given the right conditions,” the researchers said. “In this case, we have shown that what seemed like a simple campaign is, in fact, a continuous operation that has been active for three years, targeting an entire industry with off-the-shelf malware disguised with different crypters.”


And while cookies and credentials may be the main “gets” for now, there’s an opportunity for worse attacks down the line, according to Jake Williams, co-Founder and CTO at BreachQuest.


“The travel industry will always be a tempting target for threat actors,” he told Threatpost. “Many countries run nationalized airlines and can benefit from internal operations data, effectively learning from the mistakes of their competitors. But the really juicy information is the travel schedules and patterns of individuals.”


He added, “This information is useful by itself, but is especially intriguing when combined with external data about individuals, like the data acquired through the breaches of the [Office of Personnel Management](https://threatpost.com/fallout-over-opm-breach-report-begins/120461/), [Equifax](https://threatpost.com/equifax-settles-class-action-lawsuit/151873/) or health insurance organizations. This offers the threat actor information around the travel patterns of persons of interest, which will almost certainly allow them counterintelligence opportunities.”


***Rule #1 of Linux Security:**No cybersecurity solution is viable if you don’t have the basics down. **[JOIN](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)** Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the **[4 Golden Rules of Linux Security](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)**. Your top takeaway will be a Linux roadmap to getting the basics right! **[REGISTER NOW](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)**and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*




#### Tags:
[[malware]] [[“The]] [[Linux]] [[Ventura]] [[account:]] [[cookies,]] [[said.]] [[ransomware]] [[Threatpost.]] [[Talos]] [[ThreatPost]]
