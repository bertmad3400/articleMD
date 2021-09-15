# Attackers Impersonate DoT in Two-Day Phishing Scam
### Threat actors dangled the lure of receiving funds from the $1 trillion infrastructure bill and created new domains mimicking the real federal site. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169484)
+ Date: September 15, 2021  9:06 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/15090435/fish-on-hook-e1631711087677.jpeg)
Threat actors impersonated the U.S. Department of Transportation (USDOT) in a two-day [phishing campaign](https://threatpost.com/office-365-phishing-attack-financial-execs/164925/) that used a combination of tactics – including creating new domains that mimic federal sites so as to appear to be legitimate – to evade security detections.


Between Aug. 16-18, researchers at e-mail security provider INKY detected 41 phishing emails dangling the lure of bidding for projects benefitting from a $1 trillion infrastructure package recently passed by Congress, according to [a report](https://www.inky.com/blog/attackers-impersonate-u.s.-department-of-transportation-to-harvest-microsoft-credentials) written by INKY’s Roger Kay, vice president of security strategy, that was published on Wednesday.


The campaign – which targeted companies in industries such as engineering, energy and architecture that likely would work with the USDOT – sends potential victims an initial email in which they’re told that the USDOT is inviting them to submit a bid for a department project by clicking a big blue button with the words “Click Here to Bid.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The emails themselves are launched from a domain, transportationgov[.]net, that was registered by Amazon on Aug. 16, Kay said. The date of its creation – revealed by WHOIS – seems to signal that the site was set up specifically for the phishing campaign.


To anyone familiar with government sites, the domain would appear suspicious given that government sites typically have a .gov suffix. However, “to someone reading through quickly, the domain name might seem at least somewhere in the ballpark of reality,” Kay observed.


**Fooling Targets**
-------------------


If people take the bait and click, they are led to a site, transportation.gov.bidprocure.secure.akjackpot[.]com, “with reassuring-sounding subdomains like ‘transportation,’ ‘gov,’ and ‘secure,'” Kay wrote. However, the base domain of the site, akjackpot[.]com, was actually registered in 2019 and “hosts what may or may not be an online casino that appears to cater to Malaysians,” he wrote.


“Either the site was hijacked, or the site owners are themselves the phishers who used it to impersonate the USDOT,” Kay noted.


Once on the fake bidding site, targets are then instructed to click on a “Bid” button and sign in with their email provider to connect to “the network.” It also instructed them to contact a fictitious person at another fake domain – specifically, mike.reynolds@transportationgov[.]us – with any questions.


Once victims closed the instructions, they were directed to an identical copy of the real USDOT website that the attackers created by copying HTML and CSS from the government’s site onto their phishing site.


In a twist, threat actors also copied and pasted in a real warning about how to verify actual U.S. government sites, which could alert savvy victims that they were being scammed by realizing that the phishing site domain ended in .com rather than .gov or .mil, Kay noted.


Once on the imposter USDOT site, targets are invited to click a red “Click Here to Bid” button that brings up a credential-harvesting form with a Microsoft logo and instructions to “Login with your email provider.” A first attempt to enter credentials is met with a [ReCAPTCHA challenge](https://threatpost.com/cyberattackers-captchas-phishing-malware/168684/) – often used by legitimate sites as an extra security device. However, attackers already captured credentials by this point, Kay noted.


If targets make a second attempt to enter credentials, a fake error message appears, after which they are directed to the real USDOT website – “an elegant but perhaps unnecessary flourish that phishers often execute as the final step of their sequence,” Kay wrote.


**Evading Detection**
---------------------


Though attackers didn’t use any particular new [phishing](https://threatpost.com/lewd-phishing-lures-business-explode/166734/) tricks in their campaign, it was the combination of tactics in a new pattern that allowed them to get the emails through secure email gateways, Kay said.


“By creating a new domain, exploiting current events, impersonating a known brand, and launching a credential-harvesting operation, the phishers came up with an attack just different enough from known strikes to evade standard detection methods,” he wrote.


Using newly created domains in particular allowed the phishing mails to slip through standard email authentication, i.e., SPF, DKIM, and DMARC, he observed.


“Since they were brand new, the domains represented [zero-day vulnerabilities](https://threatpost.com/google-chrome-zero-day-exploited/169442/); they had never been seen before and did not appear in threat intelligence feeds commonly referenced by legacy anti-phishing tools,” Kay wrote. “Without a blemish, these sites did not look malicious.”


**It’s time to evolve threat hunting into a pursuit of adversaries.** [**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **Threatpost and Cybersixgill for** [**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **and get a guided tour of the dark web and learn how to track threat actors before their next attack.** [**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **for the LIVE discussion on September 22 at 2 PM EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[phishing]] [[USDOT]] [[wrote.]] [[site,]] [[emails]] [[However,]] [[phishers]] [[noted.]] [[ThreatPost]]
