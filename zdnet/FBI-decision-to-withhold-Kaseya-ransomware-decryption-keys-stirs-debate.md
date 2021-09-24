# FBI decision to withhold Kaseya ransomware decryption keys stirs debate
### Many security experts defended the FBI's decision to leave Kaseya victims struggling with ransomware infections for weeks.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/fbi-decision-to-withhold-kaseya-ransomware-decryption-keys-stirs-debate/)
+ Date: September 24, 2021
+ Author: Jonathan Greig


## Article:
Unknown

This week, the Washington Post [reported](https://www.washingtonpost.com/national-security/ransomware-fbi-revil-decryption-key/2021/09/21/4a9417d0-f15f-11eb-a452-4da5fe48582d_story.html) that the FBI had the decryption keys for victims of the [widespread Kaseya ransomware attack](https://www.zdnet.com/article/updated-kaseya-ransomware-attack-faq-what-we-know-now/) that took place in July yet did not share them for three weeks. 

[Hundreds of organizations](https://www.zdnet.com/article/kaseya-ransomware-attack-1500-companies-affected-company-confirms/) were affected by the Kaseya [attack](https://www.zdnet.com/article/kaseya-urges-customers-to-immediately-shut-down-vsa-servers-after-ransomware-attack/), including dozens of hospitals, schools, businesses and even a supermarket chain in Sweden. 

Washington Post reporters Ellen Nakashima and Rachel Lerman wrote this week that the FBI managed to obtain the decryption keys because they accessed the servers of REvil, the Russia-based criminal gang that was behind the massive attack.


REvil [demanded](https://www.zdnet.com/article/kaseya-denies-paying-ransom-for-decryptor-refuses-comment-on-nda/) a $70 million ransom from Kaseya and thousands from individual victims [before going dark](https://www.zdnet.com/article/revil-websites-down-after-governments-pressured-to-take-action-following-kaseya-attack/) and shutting down significant parts of its infrastructure shortly after the attack. The group [has since returned](https://www.zdnet.com/article/revil-ransomware-group-resurfaces-after-brief-hiatus/), but many organizations are still recovering from the wide-ranging July 4 attack. 

Despite the large number of victims of the attack, the FBI did not share the decryption keys, deciding to hold on to them as they prepared to launch an attack on REvil's infrastructure. According to The Washington Post, the FBI did not want to tip off REvil operators by handing out the decryption keys.

The FBI also claimed "the harm was not as severe as initially feared" according to The Washington Post. 

The FBI attack on REvil never happened because of REvil's disappearance, officials told the newspaper. The FBI [eventually shared the decryption keys with Kaseya](https://www.zdnet.com/article/kaseya-says-it-has-now-got-the-revil-ransomware-decryption-key-and-it-works/) on July 21, weeks after the attack occurred. Multiple victims spoke to The Washington Post about the millions that were lost and the significant damage done by the attacks. 






Another law enforcement source eventually [shared the decryption keys with Bitdefender](https://www.zdnet.com/article/bitdefender-releases-universal-decryptor-for-revilsodinokibi-victims-hit-before-july-13/), which released a universal decryptor earlier this month for all victims infected before July 13, 2021. More than 265 REvil victims have used the decryptor, a Bitdefender representative told The Washington Post. 

During his [testimony in front of Congress](https://www.c-span.org/video/?514725-1/dhs-secretary-fbi-director-testify-global-threats-us&live) on Tuesday, FBI Director Christopher Wray laid blame for the delay on other law enforcement agencies and allies who they said asked them not to disseminate the keys. He said he was limited in what he could share about the situation because they are still investigating what happened.  

"We make the decisions as a group, not unilaterally. These are complex...decisions, designed to create maximum impact, and that takes time in going against adversaries where we have to marshal resources not just around the country but all over the world. There's a lot of engineering that's required to develop a tool," Wray told Congress. 

The revelation caused considerable debate among security experts, many of whom defended the FBI's decision to leave victims struggling to recover from the attack for weeks. 

Critical Insight CISO Mike Hamilton -- who [dealt with a particularly thorny situation](https://www.zdnet.com/article/kaseya-victim-struggling-with-decryption-after-revil-goes-dark/) where a Kaseya victim was left in the lurch after paying a ransom right before REvil disappeared -- said being careful about disclosing methods is a staple of the law enforcement and intelligence communities. 

"There is a 'tell' though, that we've confirmed ourselves. The FBI is quoted as saying that the damage wasn't as bad as they thought and that provided some time to work with. This is because the event wasn't a typical stealth infiltration, followed by pivoting through the network to find the key resources and backups. From all indications the only servers that were encrypted by the ransomware were the ones with the Kaseya agent installed; this was a smash-and-grab attack," Hamilton said. 

"If you had it deployed on a single server used to display the cafeteria menu, you could rebuild quickly and forget the whole thing happened. The fact that the world wasn't really on fire, again, created time to dig further into the organization, likely for the ultimate purpose of identifying individual criminals. Those organizations that WERE hit hard had the agent deployed on on-premises domain controllers, Exchange servers, customer billing systems, etc."

Sean Nikkel, senior threat intel analyst at Digital Shadows, said the FBI may have seen the need to prevent or shut down REvil's operations as outweighing the need to save a smaller group of companies struggling in just one attack. 

Because of REvil's [increasing scale of attacks](https://www.zdnet.com/article/fbi-attributes-jbs-ransomware-attack-to-revil/) and extortion demands, a quickly-developing situation requiring an equally fast response likely preempted a more measured response to the Kaseya victims, Nikkel explained, adding that it is easy to judge the decision now that we have more information but that it must have been a tough call at the time. 

"Quietly reaching out directly to victims may have been a prudent step, but attackers seeing victims decrypting files or dropping out of negotiations en masse may have revealed the FBI's ploy for countermeasures," Nikkel told ZDNet. 

"Attackers then may have taken down infrastructure or otherwise changed tactics. There's also the problem of the anonymous soundbite about decryption making its way into public media, which could also tip off attackers. Criminal groups pay attention to security news as much as researchers do, often with their own social media presence." 

Nikkel suggested that a better approach may have been to open backchannel communications with incident response firms involved to better coordinate resources and response, but he noted that the FBI may have already done this. 

BreachQuest CTO Jake Williams called the situation a classic case of an intelligence gain/loss assessment. 

Like Nikkel, he said it's easy for people to play "monday morning quarterback" and blame the FBI for not releasing the keys after the fact. 

But Williams did note that the direct financial damage was almost certainly more widespread than the FBI believed as it withheld the key to protect its operation. 

"On the other hand, releasing the key solves an immediate need without addressing the larger issue of disrupting future ransomware operations. On balance, I do think the FBI made the wrong decision in withholding the key," Williams said. 

"However, I also have the convenience of saying this now, after the situation played itself out. Given a similar situation again, I believe the FBI will release the keys unless a disruption operation is imminent (hours to days away). Because organizations aren't required to report ransomware attacks, the FBI lacked the full context required to make the best decision in this case. I expect this will be used as a case study to justify reporting requirements."

John Bambenek, principal threat hunter at Netenrich, said critics need to remember that first and foremost, the FBI is a law enforcement agency that will always act in a way that optimizes law enforcement outcomes. 

"While it may be frustrating for businesses that could have been helped sooner, law enforcement takes time and sometimes things don't work out as planned," Bambenek said. 

"The long term benefit of successful law enforcement operations is more important than individual ransomware victims."





#### Tags:
[[REvil]] [[Kaseya]] [[ransomware]] [[attack.]] [[said.]] [[Nikkel]] [[ZDNet]]
