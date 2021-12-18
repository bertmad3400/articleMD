# This company was hit with ransomware, but didn't have to pay up. Here's how they did it | ZDNet
### Cyber criminals demanded $15 million for a decryption key and sent threatening messages to staff - but this company recovered its network without paying hackers a thing.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/this-company-was-hit-with-ransomware-but-didnt-have-to-pay-up-heres-how-they-did-it/
+ Date: 2021-12-17 10:08:00
+ Author: Danny Palmer


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/335e5992b3f268300ce1fa524643f8b246e25b3e/2021/12/09/74e1af48-5c31-4761-9431-00fb5e28f656/a-man-eating-breakfast-and-drinking-a-coffee-at-a-desk.jpg?width=770&height=578&fit=crop&auto=webp)

There's never a good time for an organisation to fall victim to a [ransomware attack](https://www.zdnet.com/article/ransomware-an-executive-guide-to-one-of-the-biggest-menaces-on-the-web/), but for Matthew Day, CIO of Langs Building Supplies, a phone call on May 20, 2021 came at perhaps the worst possible time – before dawn, just as he was about to take time off for the first time in a long time. 

"I was going on my holidays. But I got a phone call at four o'clock in the morning, saying basically 'I can't log in, what's going on?'" he says. 

Day got up and made the 30-minute drive to his office in Brisbane, Australia where the construction, building supplies and home-building company is based, all the while thinking about what the problem could be, perhaps a hardware failure or an unplanned outage?  


The answer became obvious when he arrived and tried to bring up the systems – a ransom note appeared and said: "You've been hacked." 

****SEE:**[**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/?ftag=CMG-01-10aaa1b)**(ZDNet special report)**** 

Langs had fallen victim to [Lorenz ransomware](https://www.zdnet.com/article/lorenz-ransomware-attack-victims-can-now-retrieve-their-files-for-free-with-this-decryption-tool/) and the cyber criminals who had encrypted multiple servers and thousands of files were demanding a payment of [$15 million in Bitcoin](https://www.zdnet.com/article/how-bitcoin-helped-fuel-an-explosion-in-ransomware-attacks/) in exchange for the decryption key. Like many ransomware attacks, the cyber criminals also said they'd stolen information and [threatened to leak](https://www.zdnet.com/article/ransomware-theres-been-a-big-rise-in-double-extortion-attacks-as-gangs-try-out-new-tricks/) [it if the ransom wasn't paid](https://www.zdnet.com/article/ransomware-theres-been-a-big-rise-in-double-extortion-attacks-as-gangs-try-out-new-tricks/). 

"The reality is that's a pretty scary proposition – but we were quickly able to isolate the attack and disconnect it from the network," says Day. 






He suspects that Langs was specifically targeted by the criminals behind the attack because of the nature of the business. At the time, the Queensland government was operating a response plan to keep the trade and construction industries in business, while much of Australia was still facing lockdown because of COVID-19. And if a building supplier like Langs was unable to do business, that could affect the whole programme for the regional construction industry. 

"It's a macro-level event – it's not just limited to Langs because if we can't supply a builder their goods because we're offline, they can't build that house. That just ratchets up more pressure," he says. 

Many victims of ransomware opt to [pay the ransom,](https://www.zdnet.com/article/ransomware-too-many-firms-are-still-willing-to-pay-up-if-attacked/) either because they feel they don't have any other choice or they perceive it as the easiest way to restore the network – although, even [with the decryption key](https://www.zdnet.com/article/irish-healthcare-ransomware-attack-three-quarters-of-servers-decrypted-but-disruption-to-services-will-continue-for-months/), it can be a long, drawn-out process. 

For Langs and Day, however, the idea of paying the ransom wasn't an option – and they had recovery software that allowed them to analyse what data had been encrypted or modified and restore the network from backups stored separately to the rest of the network within a matter of hours, with minimal disruption to services. 

"I was pretty confident about the data side of things – we use Rubrik. We make sure it's got multi-factor authentication (MFA) on it and doesn't have any shared credentials, so it's a walled garden," says Day. "These people immediately want to go after your backups because that ratchets up pressure, so if they can't get to your backups, you're in a good place." 

But this didn't stop the cyber criminals from [attempting to extort a ransom payment](https://www.zdnet.com/article/this-new-ransomware-encrypts-your-data-and-makes-some-nasty-threats-too/) – they emailed all the staff at Langs, claiming they'd stolen data and threatened to sell it on the dark web if a payment wasn't received by a particular date. 

While 13 gigabytes of data had left the network, it turned out to be ping traffic, so nothing that could be a security or privacy risk to Langs' customers or employees. Receiving the emails was a shock to staff, but Day was able to explain the situation and reassure people that, even though cyber criminals had contacted them, there was nothing to worry about. 

"You've got to communicate with people, explain it to them. We were able to show the business that they're [the cyber criminals] playing chicken and we're not going to blink first. So we didn't pay the ransom, the day came – and nothing happened," says Day. 

The investigation into the incident revealed that hackers initially gained access to the network via [a phishing email](https://www.zdnet.com/article/what-is-phishing-how-to-protect-yourself-from-scam-emails-and-more/). But this wasn't a run-of-the-mill basic phishing email; the attackers had done their research and sent it to a Langs employee from [the legitimate email account of a real employee](https://www.zdnet.com/article/this-cybersecurity-threat-costs-business-millions-and-its-the-one-they-often-forget-about/) at a supplier that they'd already compromised. 

****SEE****: **[**Cloud security in 2021: A business guide to essential tools and best practices**](https://www.zdnet.com/article/cloud-security-in-2021-a-business-guide-to-essential-tools-and-best-practices/)** 

Langs had set up allow lists to verify emails coming from known suppliers – and the attackers were able to take advantage, after examining emails sent and received by the compromised account and specifically tailoring the email that was sent to victims who opened it and unintentionally triggered the attack. 

"They responded to an order that we had sent them in the exactly correct manner; this was a really smart play for these guys. It came from a verified account, from a person at a time and in a way that was expected by the user, my staff member, with the correct formatting and quoted the correct valid number, so it wasn't a fake account, it wasn't a spoofed account, it was the real deal," explains Day. 

The email asked the user to visit a portal that looked exactly like the website of the supplier, except this one asked for a username and password – and because the victim had been duped into thinking they were responding to a message from a legitimate contact, they entered the information, inadvertently providing cyber criminals with login credentials that they exploited for initial access to the network. 

But Day doesn't place blame on the user, because the sophisticated and targeted nature of the phishing email means it would be difficult for most people to identify it as a suspicious message. 

"We can land planes, 99.9995% of the time, no worries, but it only takes that one decimal place to cause a massive incident, and this is no different – so I can't be too hard on my user for falling for this, because it looked legit," he says. 

That initial access with legitimate credentials allowed the attackers to snoop around the network without being noticed, laying down the foundations to encrypt as much as possible before triggering the ransomware attack. 

The data recovery and backup software meant that the impact of the ransomware attack was relatively mild, but it could have been much worse – and Day used the incident to examine how cyberscurity at Langs could be improved. 

****SEE:**[**Cybersecurity: Let's get tactical**](https://www.zdnet.com/topic/cybersecurity-lets-get-tactical/)**(ZDNet special feature)**** 

One of those tactics was ensuring that [multi-factor authentication](https://www.zdnet.com/article/multi-factor-authentication-use-it-for-all-the-people-that-access-your-network-all-the-time/) (MFA) was applied to a wider range of accounts. Day had previously pushed for it to be applied to users, but it was seen as a barrier to productivity. Looking back, he believes if the company had listened to his advice and applied multi-factor authentication, the attack could have been prevented from happening. 

"I should have stuck to my guns more about external access and MFA. Because we've been talking about it for quite a while and I was pushing for it, but the company pushed back because it was seen as an onerous burden on the users; one more thing that they have to learn and deal with," Day says. 

"If I'd had MFA, we could have stopped this particular attack in its tracks and I'm happy to say we can now have MFA on those external desktops." 

The way in which the attack originated via the compromised email of a supplier has also resulted in Langs taking a more hands-on approach to [the security of its supply chain](https://www.zdnet.com/article/supply-chain-attacks-are-the-hackers-new-favourite-weapon-and-the-threat-is-getting-bigger/), helping the suppliers and customers it deals with most to make their networks more resilient to cyberattacks. 

"We don't exist in our own little bubble, our bubble has to include our customers and suppliers in that supply chain life-cycle and make sure we secure it end to end," Day explains. 

Ransomware is [one of the most significant cybersecurity threats facing businesses today](https://www.zdnet.com/article/have-we-reached-peak-ransomware-how-the-internets-biggest-security-problem-has-grown-and-what-happens-next/), but even when organisations successfully fight off a ransomware attack without paying a ransom to cyber criminals, few are willing to talk about what happened. So, why is Day willing to speak about it [when so few others are](https://www.zdnet.com/article/businesses-dont-talk-about-being-victims-of-cyberattacks-that-needs-to-change/)? 

"Talking about it is a bit of an 'up yours' thing. I also want to empower other people to speak out about these things. If I speak about it, nothing bad happens – it just encourages other people to do it," he says. 

Day hopes speaking about the incident, how it happened and what was learned can help other businesses defend against ransomware, and crucially, help them [persuade boardrooms](https://www.zdnet.com/article/too-many-bosses-are-reluctant-to-spend-money-on-cybersecurity-then-they-get-hacked/) about the importance of taking cybersecurity threats seriously. 

"If, by coming forward and talking about these things, I encourage another CIO, IT manager or IT professional to go and have a conversation about how to protect their data, how they handle data governance, or cybersecurity planning and processes, so that they can protect the livelihoods of their their employees and their colleagues, it feels better," he says. 


###  **MORE ON CYBERSECURITY**

* [**Ransomware: Looking for weaknesses in your own network is key to stopping attacks**](https://www.zdnet.com/article/ransomware-looking-for-weaknesses-in-your-own-network-is-key-to-stopping-attacks/)
* [**Digital transformation is creating new security risks, and businesses can't keep up**](https://www.zdnet.com/article/digital-transformation-is-creating-new-security-risks-and-businesses-cant-keep-up/)
* [**Businesses don't talk about being victims of cyberattacks. That needs to change**](https://www.zdnet.com/article/businesses-dont-talk-about-being-victims-of-cyberattacks-that-needs-to-change/)
* [**Ransomware is the biggest cyber threat to business. But most firms still aren't ready for it**](https://www.zdnet.com/article/ransomware-is-now-the-most-urgent-cyber-threat-to-business-but-most-firms-arent-ready-for-it/)
* [**Ransomware: Even when the hackers are in your network, it might not be too late**](https://www.zdnet.com/article/ransomware-even-when-the-attackers-are-in-your-network-its-not-too-late-to-fight-back/)





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Construction]] [[victim.industry.name=Mining]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Langs]] [[Ransomware]] [[Cybersecurity]] [["i]] [[Multi-factor]] [[Emails]] [[Phishing]] [[Mfa]] [[ZDNet]]

