# 2FA Bypassed in $34.6M Crypto.com Heist
### In a display of 2FA's fallibility, unauthorized transactions approved without users' authentication bled 483 accounts of funds.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177846
+ Date: 2022-01-20T23:14:23+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2020/03/12095432/bank-robbery.jpg)

Early Thursday morning, Crypto.com acknowledged that it had lost $34.65 million worth of cash, Bitcoin and Ethereum after getting ransacked in an attack that slipped fat transactions past two-factor authentication (2FA).


Users had complained over the weekend that their accounts had been drained: thievery that the cryptocurrency exchange initially denied. On Sunday, Crypto.com [wrote on Twitter](https://twitter.com/cryptocom/status/1482936866001207296) that “a small number of users [are] reporting suspicious activity on their accounts,” but that “all funds are safe.”


On Monday, the company’s CEO, Kris Marszalek, [reiterated in a tweet](https://twitter.com/BENBALLER/status/1483188044781928449) that “no customer funds were lost.”



> 
> We have a small number of users reporting suspicious activity on their accounts. 
> 
> 
> We will be pausing withdrawals shortly, as our team is investigating. All funds are safe.
> 
> 
> — Crypto.com (@cryptocom) [January 17, 2022](https://twitter.com/cryptocom/status/1482936866001207296?ref_src=twsrc%5Etfw)
> 
> 



Now, Crypto.com has acknowledged that yes, the total amount of the loss is well over $300 million – far more than was initially estimated – but that all customers had been reimbursed.


The company also said that the robbers pulled it off by blowing past the exchange’s 2FA system.


[![Password Management Webinar](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/12124026/specops_300x250_watch.jpg)](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)  

In spite of customers having reported losses over the weekend, Crypto.com’s Thursday [statement](https://crypto.com/product-news/crypto-com-security-report-next-steps) said that the heist happened on Monday at about 12:46 a.m. UTC.


That’s when the exchange’s risk monitoring systems picked up on unauthorized transactions coming out of 483 accounts and being approved without users’ 2FA authentication. The company didn’t immediately respond to Threatpost’s request for clarification on the timeline or an update on its investigation.


Crypto.com immediately suspended withdrawals on the platform as it investigated. The exchange fully restored the affected accounts, revoked all 2FA tokens and added additional security hardening measures, requiring all customers to re-login and set up their 2FA token.


Withdrawals were suspended for about 14 hours, and withdrawals resumed on Tuesday at 5:46 PM UTC.


Before it clammed up on withdrawals, Crypto.com lost 836.26 ETH and 443.93 BTC, which equaled around $15.54 million and $19.04 million, respectively, as of Thursday afternoon. The exchange reported that it lost $66,200 worth of other currencies, as well.


On Wednesday, Crypto.com CEO Kris Marszalek had [acknowledged the theft](https://twitter.com/BloombergLive/status/1483841347824099330) in an online interview with Bloomberg*,* confirming that around 400 user accounts were indeed compromised and had funds drained as a result. At the time, Marszalek didn’t give details of how, exactly, attackers pulled off the breach.


He downplayed the value of the lost funds, remarking that “One has to remember that, given the scale of the business, these materials are not particularly material,” and adding that “customer funds were never at risk.”



> 
> JUST IN: CEO [@cryptocom](https://twitter.com/cryptocom?ref_src=twsrc%5Etfw)’s Kris Marszalek discusses the site's recent hack with [@BloombergTV](https://twitter.com/BloombergTV?ref_src=twsrc%5Etfw)’s [@emilychangtv](https://twitter.com/emilychangtv?ref_src=twsrc%5Etfw). "Customer funds were never at risk." [#TheYearAhead](https://twitter.com/hashtag/TheYearAhead?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/YlCtGO60t5](https://t.co/YlCtGO60t5)
> 
> 
> — Bloomberg Live (@BloombergLive) [January 19, 2022](https://twitter.com/BloombergLive/status/1483841347824099330?ref_src=twsrc%5Etfw)
> 
> 



Trash that 2FA
--------------


Crypto.com said that it’s junked its 2FA “in an abundance of caution” and has migrated to a “completely new 2FA infrastructure.”


“2FA tokens for all users worldwide were subsequently revoked to ensure the new infrastructure was in effect,” the exchange said. “We have mandatory 2FA policies on both the frontend and backend to protect users during this revocation phase, as outflows such as withdrawals have a requirement to setup and use 2FA in order to withdraw.”


On Tuesday, Crypto.com also introduced an additional layer of security, adding a mandatory 24-hour delay between registration of a new whitelisted withdrawal address and first withdrawal. There will be a time cushion in between notifications of withdrawal addresses having being added, to give users enough time “to react and respond,” the exchange said. The notifications will also include instructions on contacting the exchange if the address whitelisting was unauthorized.


Crypto.com said that it’s done a full, internal audit of its infrastructure and has implemented additional, unspecified security-hardening measures. It’s also brought in third-party security firms to perform additional security checks on its platform and to initiate “additional threat intelligence services.”


The exchange plans to release additional end-user security features as it moves away from 2FA and on to what it called “true” multi-factor authentication (MFA).


Finally, Crypto.com is introducing the Worldwide Account Protection Program (WAPP) to offer additional protection and security for user funds held in the Crypto.com App and the Crypto.com Exchange. Designed to protect user funds against unauthorized withdrawals, WAPP restores funds up to USD $250,000 for qualified users.


To qualify for WAPP, users are required to enable MFA on all transaction types where it’s available, set up an anti-phishing code at least 21 days prior to the reported unauthorized transaction, keep off of jailbroken devices, file a police report and provide a copy of it to Crypto.com, and complete a questionnaire to support a forensic investigation.


“The safety of our customers’ funds is our highest priority, and we are continually enhancing our Defence-in-Depth security and protection measures,” Marszalek said in Thursday’s release. “While we are reminded of the existence of bad actors intent on committing fraud, this new Worldwide Account Protection Program, along with our new MFA infrastructure, gives our users unprecedented protection of their funds, and hopefully, peace of mind.”


What’s So Feeble About 2FA?
---------------------------


2FA combines …


* Something you know, such as a password or PIN,
* Something you have, such as a smart card or USB token, and/or
* Something you are, such as voice prints, fingerprints or iris prints.


Unfortunately, the “something you know” slice of the pie is often a cruddy, easily guessed or phished password.


MFA is considered stronger than 2FA in that it adds more factors of authentication, eliminating security threats associated with 2FA. As it is, there are [several ways](https://resources.infosecinstitute.com/topic/ethical-hacking-top-6-techniques-for-attacking-two-factor-authentication/) to attack 2FA, including but not limited to:


**Social engineering.** As Coinbase [noted](https://threatpost.com/mfa-glitch-coinbase-customers-robbery/175290/) when 6,000 of its customers got ripped off in October 2021, users’ email addresses, passwords, phone numbers and personal email inboxes are often gleaned through phishing attacks or other social engineering techniques that trick victims into disclosing their login credentials.


“Since cryptocurrency is still a relatively new technology, it presents an opportunity for threat actors to socially engineer targets,” observed Hank Schless, senior manager, security solutions at Lookout. “Crypto investors are constantly looking for an edge in the market or what the next big currency that’s going to explode in value. Attackers can use this thirst for information to get users to download malicious apps or share login credentials for legitimate trading platforms they use.”


An attacker can then use the malicious app to exfiltrate additional data from the device it’s on or take the login credentials they’ve stolen and try them across any number of cloud apps used for both work and personal life, Schless told Threatpost on Thursday.


“In order to increase the likelihood of success, attackers target users across both mobile devices and cloud platforms,” he continued. “For example, at Lookout, we discovered almost 200 [malicious cryptocurrency apps](https://threatpost.com/cloud-cryptomining-swindle-google-play/167581/) on the Google Play Store. Most of these applications advertised themselves as mining services in order to entice users to download them.”


**Cookie session hijacking.** Cookie theft, also called [session hijacking](https://cwatch.comodo.com/blog/website-security/what-is-session-hijacking/) or pass-the-cookie attack, involves a crook inserting themself between a computer and a server in order to steal what’s known as a [magic cookie](https://en.wikipedia.org/wiki/Magic_cookie): a session that authenticates a user to a remote server. After stealing the cookie, an intruder can monitor and potentially capture everything from the account and can take full control of the connection. We saw it happen to Google in October 2021, when it caught and brushed off a bunch of [cookie-stealing YouTube channel hijackers](https://threatpost.com/google-youtube-channel-hijackers-cryptocurrency-scams/175617/) who were running cryptocurrency scams on, or auctioning off, ripped-off channels.


**Duplicate code generators.** As security journalist Brian Krebs has [reported](https://krebsonsecurity.com/2021/09/the-rise-of-one-time-password-interception-bots/), these days, there are bot-based services that make it “relatively easy” for crooks to phish one-time passwords (OTPs) from targets. They’re designed to trick victims into giving up those OTPs, which crooks can use to take over an account, assuming they’ve first filched a target’s login credentials. In the earlier days of authentication, attackers have also [used trojans](https://threatpost.com/hackers-using-trojans-steal-one-time-passwords-082009/72953/) to intercept OTPs.


‘That’s Where the Money Is’
---------------------------


Neil Jones, cybersecurity evangelist for Egnyte, wasn’t surprised by the fact that crooks would target a cryptocurrency exchange, nor that they got away with $34.6M. After all, just like Willie Sutton answered when asked why he robbed banks, “That’s where the money is.”


No, what surprised Jones was that nearly 500 users got robbed.


He pulled out a few lessons from the security breach, including:


1. The importance of an effective 2FA solution that prompts end-users for additional verification when large transactions occur unexpectedly.
2. The need for a current- and road-tested incident response plan.
3. The requirement for end users to be notified promptly and accurately when cyberattacks take place, to help protect brand reputation.


Don’t change that Bat Channel, kids, as more breaches are inevitable, Jones told Threatpost on Thursday. Companies “should keep posted for developments in this space, as this likely isn’t the last breach you’ll see in the cryptocurrency markets,” he predicted.


Rick Holland, chief information security officer and vice president or strategy at Digital Shadows, told Threatpost that Crypto.com is a significant cryptocurrency exchange, and hence makes an inviting target for criminals. “The cryptocurrency space is a perfect storm of opportunity for cybercriminals,” Holland observed. “It is cross-border, unregulated, speculative, and experiencing a gold rush of vulnerable investors who don’t understand the risks. There is also a higher bar for technical knowledge if you want to invest in crypto.”


He gave an example: using an offline hardware wallet (e.g., Ledger) which he praised as “a great way to reduce the risk of losing your crypto should an exchange be compromised.” However, it’s easier said than done for the technically non-savvy, he noted: “Setting up one of these wallets and moving your crypto from exchanges isn’t trivial, and is too high of a bar for many crypto investors. Ordinary people struggle with passwords, so using 24-word seed phrases on top of them doesn’t make for the most practical user experience.”


As for what crypto platform providers like Crypto.com should do to avoid massive breaches like this one, Lookout’s Schless had a recommendation: “Ensure that employees are protected and don’t become conduits for cybercriminals to make their way into the infrastructure,” he told Threatpost.


“Employees are constantly targeted by mobile phishing and other attacks that would give a cybercriminal a backstage pass to the company’s infrastructure,” Schless expounded.


It’s advisable to throw some upper-tier security at the risk, he said: “The risk of this happening can be reduced by implementing a powerful combination of a unified mobile threat defense (MTD) and cloud access security broker (CASB) solution that can protect the user on the endpoint and recognize anomalous activity indicative of a compromised employee account.”





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Finance]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Crypto.com]] [[2fa]] [[Marszalek]] [[Threatpost]] [[Schless]] [[Ceo]] [[Mfa]] [[“the]] [[Apps]] [[Cloud]] [[ThreatPost]]

