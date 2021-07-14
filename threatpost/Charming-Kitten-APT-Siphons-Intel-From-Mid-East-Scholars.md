# ‘Charming Kitten’ APT Siphons Intel From Mid-East Scholars
### Professors, journalists and think-tank personnel, beware strangers bearing webinars: It’s the  focus of a particularly sophisticated, and chatty, phishing campaign.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167715)
+ Date: July 13, 2021  12:44 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/13123353/Charming-Kitten.jpg)
An Iran-linked advanced persistent threat (APT) group has taken a scholarly bent with its latest phishing campaign, which involves lengthy chats with professors, think tank higher-ups and journalists focused on Middle Eastern affairs.


The threat actor is Charming Kitten – aka a number of names, including TA453, APT35, Ajax Security Team, NewsBeef, Newscaster and Phosphorus. It’s an ever-evolving APT, and this is one of its more sophisticated campaigns, according to what Proofpoint researchers [reported](https://www.proofpoint.com/us/blog/threat-insight/operation-spoofedscholars-conversation-ta453) on Tuesday.


Not that the aims of this APT actor have been modest in the past. For example, in March, Charming Kitten launched a credential-stealing campaign that [targeted genetic, neurology and oncology](https://threatpost.com/charming-kitten-pounces-on-researchers/165129/) professionals.



Charming Kitten has also been tied to attacks on President Trump’s 2020 re-election campaign. In October 2019, researchers reported that the actor had added [new spearphishing techniques](https://threatpost.com/iran-linked-charming-kitten-touts-new-spearphishing-tactics/149109/) to its arsenal in what appeared to be a ramp-up of operations. Security researchers who tracked the [earlier phase of the campaign](https://threatpost.com/charming-kitten-iranian-2fa/139979/) in October 2018 saw attacks tailored to elude two-factor authentication in order to compromise email accounts and to monitor communications.


Focus Shifts to Brits
---------------------


The current campaign includes masquerading as British scholars; engaging in dialogue with targets; and linking to the website of a legitimate, world-class, already compromised academic institution in order to harvest credentials.


Proofpoint has named the campaign Operation SpoofedScholars and has linked it to the Iranian government, with the intention of what researchers believe is cyberespionage. This is “an APT who we assess with high confidence supports Islamic Revolutionary Guard Corps (IRGC) intelligence collection efforts,” according to the report.


This is a limited, “highly selective” campaign that, according to Proofpoint telemetry, is targeting fewer than 10 organizations. Charming Kitten is after people who have “information of interest to the Iranian government, including, but not limited to, information about foreign policy, insights into Iranian dissident movements, and understanding of U.S. nuclear negotiations,” according to the report.


This is a wash, rinse and repeat situation: The threat actor has previously targeted most of the targets identified by Proofpoint, they said.


Charming Kitten/TA453’s Sophistication Spikes
---------------------------------------------


The email conversations were benign, at first. They turned sinister when Charming Kitten provided a link to a boobytrapped website hosting a credential-harvesting page. That’s a step up from the APT’s historical tactics, techniques and procedures (TTPs), according to the report: “The use of a legitimate but actor-compromised website is an increase in sophistication compared to TA453’s historical [TTPs] of using actor-controlled credential phishing websites,” researchers wrote.


As far as attribution goes, Proofpoint analysts can’t independently confirm the link to Iran’s intelligence arm, the IRGC, as Proofpoint analysts discussed in the March campaign against medical professionals. That credentials-harvesting campaign was dubbed BadBlood because of its medical focus and the history of tensions between Iran and Israel. Still, the TTPs and the overall targeting jibe with IRGC intelligence collection priorities, they noted in Tuesday’s Operation SpoofedScholar report.



> *The IRGC, specifically the IRGC Intelligence Organization, collects intelligence and conducts operations in support of a variety of assigned responsibilities. According to the Meir Amit Intelligence and Terrorism Information Center’s November 2020 [report](https://www.terrorism-info.org.il/en/the-intelligence-organization-of-the-irgc-a-major-iranian-intelligence-apparatus/), some of the IRGC IO’s responsibilities include foiling political subversion, combating western cultural penetration, and supporting the arrest of Iranian dual nationals.* —Proofpoint.
> 
> 


Operation SpoofedScholars shows TTPs that are also similar to previous TA453 campaigns and “consistency with TA453’s historical targeting,” the analysts wrote, including using free email providers to spoof individuals familiar to their targets. Another similarity: The Operation SpoofedScholar campaign is also concentrated on credential phishing on specific individuals of interest, from whom the campaign seeks to siphon “sensitive email and contacts or initial access for future phishing campaigns,” analysts explained.


Masquerading as African & Oriental Scholars
-------------------------------------------


The specifics: Since at least January 2021, Charming Kitten/TA453 has been cyber-sidling up to UK scholars with the University of London’s School of Oriental and African Studies (SOAS) so as to solicit sensitive information.


Researchers said that the APT compromised this “highly regarded academic institution” to deliver personalized, credential-harvesting pages disguised as registration links. Identified targets included “experts in Middle Eastern affairs from think tanks, senior professors from well-known academic institutions, and journalists specializing in Middle Eastern coverage,” they explained.


“These connection attempts were detailed and extensive, often including lengthy conversations prior to presenting the next stage in the attack chain,” the report continues. “Once the conversation was established, TA453 delivered a ‘registration link’ to a legitimate but compromised website belonging to the University of London’s SOAS radio.”


Charming Kitten also targeted the personal email accounts of at least one of the APT’s targets.


The Chatty Early Phishing Attempts
----------------------------------


TA453 subsequently shifted tactics to deliver the registration link earlier in the phishing conversation, but initially, the campaign engaged in lengthy chats with targeted individuals.


As you can see below in the screenshot of one such conversation, TA453 employs actors with pretty decent English skills. The threat actor even claimed at one point to be up for talking via videoconference. The persona set up by the threat actor was also seen trying to gather mobile phone numbers, “possibly for mobile malware or additional phishing,” the researchers suggested. “TA453 repeatedly demonstrated a desire to connect with the target in real-time,” they added.


According to Proofpoint, the campaign started in early 2021 with the concoction of a bogus scholar: a “Dr.Hanns Bjoern Kendel, Senior Teaching and Research Fellow at SOAS University in London.” TA453 set up the email address “hannse.kendel4[@]gmail.com” for Dr. Utterly Bogus, in order to spark conversations with targets.


In the brief summary of one of the fraudulent conversations researchers observed, shown below, TA453 lured the target with an invitation to an online conference on “The US Security Challenges in the Middle East.”


TA453 wanted to talk with the target via phone to discuss the invitation, but the target was too slippery: The intended victim “hedged and emphatically stated that they wanted a written proposal with the details,” researchers described. TA453 ultimately acquiesced and forked over specifics about the purported conference. The conversation went back and forth as the threat actor tried to verify the target’s interest, with the ultimate gambit of providing a detailed invitation to the fake conference, as shown in the screen capture below.


The Phony ‘Webinar Control Panel’
---------------------------------


Analysts explained that once TA453 convinced a target to attend the bogus webinar, its persona sent a personalized link that led to a “Webinar Control Panel” on a legitimate but compromised website belonging to a research institution, [University of London’s SOAS](https://www.soas.ac.uk/). TA453 apparently gained elevated privileges that allowed the actor to create the credential-harvesting pages of one of SOAS’ legitimate sites – soasradio[.]org – that also hosts legitimate, SOAS-affiliated content.


TA453 bolstered credibility by setting up additional fake personas besides “Dr. Kendel.” The personas masqueraded as legitimate affiliates of SOAS to deliver the malicious links. As shown in the image of a credential-harvesting webpage shown below, TA453 offers targets the ability to use “OpenID” to log in via a list of email providers: Google, Yahoo, Microsoft, iCloud, Outlook, AOL, mail.ru, Email and Facebook. The website URI was “hxxps://soasradio[.]org/connect/?memberemailid= [RedactedInitials of Target]-[String of alphanumeric characters].”


When targets clicked on a particular provider, a pop-up box displayed the actual credential phishing box. The buttons for Google, Microsoft, and Email pre-filled the target’s email address, analysts detailed. It’s a good bet that TA453 planned to validate those credentials “immediately,” they hypothesized: “Based on the variety of email providers along with TA453’s insistence that the target log on when TA453 was online, Proofpoint assesses that TA453 was planning on immediately validating the captured credentials manually.”


Other spoofed scholars besides Dr. Hanns Kendel showed up months after the persona was first spotted, including Tolga Sinmazdemir, another individual associated with SOAS. The Sinmazdemir persona sent emails looking for contributions to a “DIPS Conference.” The kill chain would likely have been similar to the Dr. Kendel chain, researchers said.


The Dr. Kendel persona also re-emerged in mid-May, when it showed up with a different email address (hanse.kendel4[@]gmail.com) with the aim of, again, recruiting for a webinar.


Fending Off Operation SpoofedScholars
-------------------------------------


Proofpoint offered these specific mitigations against Operation SpoofedScholars:


Expect More of the Same
-----------------------


Proofpoint said that the company has “worked with the appropriate authorities to conduct victim notification.”


It’s highly likely that we’ll see TA453 again, likely using the same, more-sophisticated TTPs. Proofpoint concluded that the use of legitimate, compromised infrastructure marks an increase in the APT’s sophistication that will “almost certainly” be replicated in future campaigns.


“TA453 continues to iterate, innovate, and collect in support of IRGC collection priorities,” analysts said in conclusion. “While some of the identified selectors no longer appear to be active in TA453 operations, Proofpoint assesses with high confidence that TA453 will continue to spoof scholars around the world in support of TA453’s intelligence collection operations in support of Iranian government interests. Academics, journalists, and think tank personnel should practice caution and verify the identity of the individuals offering them unique opportunities.”


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[TA453]] [[Proofpoint]] [[phishing]] [[IRGC]] [[SOAS]] [[website]] [[TTPs]] [[Kendel]] [[SpoofedScholars]] [[credential-harvesting]] [[ThreatPost]]
