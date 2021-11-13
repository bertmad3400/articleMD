# FBI system hacked to email 'urgent' warning about fake cyberattacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/fbi-system-hacked-to-email-urgent-warning-about-fake-cyberattacks/)
+ Date: November 13, 2021
+ Author: Ionut Ilascu


## Article:
![FBI system hacked to email 'urgent' warning about fake cyberattacks](https://www.bleepstatic.com/content/hl-images/2021/11/10/FBI.jpg)


The Federal Bureau of Investigation (FBI) email servers were hacked to distribute spam email impersonating FBI warnings that the recipients' network was breached and data was stolen.


The emails pretended to warn about a “sophisticated chain attack” from an advanced threat actor known, who they identify as Vinny Troia. Troia is the head of security research of the dark web intelligence companies NightLion and Shadowbyte


The spam-tracking nonprofit SpamHaus noticed that tens of thousands of these messages were delivered in two waves early this morning. They believe this is just a small part of the campaign.


### Legitimate address delivers fake content


Researchers at the [Spamhaus Project](https://www.spamhaus.org/), an international nonprofit that tracks spam and associated cyber threats (phishing, botnets, malware), observed two waves of this campaign, one at 5 AM (UTC) and a second one two hours later.


The messages came from a legitimate email address - *eims@ic.fbi.gov* - which is from FBI’s Law Enforcement Enterprise Portal (LEEP), and carried the subject “**Urgent: Threat actor in systems**.”


All emails came from FBI’s IP address **153.31.119.142** (*mx-east-ic.fbi.gov*), Spamhaus told us.


![Fake cyber attack alert from legit FBI email address](https://www.bleepstatic.com/images/news/u/1100723/2021/SpamFBI_message.jpg)


The message warns that a threat actors has been detected in the recipients' network and has stolen data from devices.


Spamhaus Project told BleepingComputer that the fake emails reached at least 100,000 mailboxes. The number is a very conservative estimate, though, as the researchers believe “the campaign was potentially much, much larger.”


In a [tweet](https://twitter.com/spamhaus/status/1459451401269043201) today, the nonprofit said that the recipients were scraped from the American Registry for Internet Numbers ([ARIN](https://www.arin.net/)) database.


While this looks like a prank, there is no doubt that the emails originate from FBI’s servers as the headers of the message show that it’s origin is verified by the DomainKeys Identified Mail (DKIM) mechanism.


The headers also show the following FBI internal servers that processed the emails:


* dap00025.str0.eims.cjis
* wvadc-dmz-pmo003-fbi.enet.cjis
* dap00040.str0.eims.cjis


The FBI confirmed that the content of the emails is fake and that they were working on solving the issue as their helpdesk is flooded with calls from worried administrators.


### Aimed to discredit security researcher


Whoever is behind this campaign was likely motivated to discredit Vinny Troia, the founder of dark web intelligence company Shadowbyte, who is named in the message as the threat actor responsible of the fake supply-chain attack.


Members of the RaidForums hacking community have a long standing feud with Troia, and commonly deface websites and perform minor hacks where they blame it on the security researcher.


Tweeting about this spam campaign, Vinny Troia [hinted](https://twitter.com/vinnytroia/status/1459515619838251010) at someone known as “[pompomourin](https://twitter.com/pompompur_in),” as the likely author of the attack. Troia says the individual has been associated in the past with incidents aimed at damaging the security researcher’s reputation.


Speaking to BleepingComputer, Troia said that “my best guess is 'pompomourin' and his band of minions [are behind this incident].”



“The last time they [pompompurin] hacked the national center for missing children’s we site blog and put up a post about me being a pedophile” - Vinny Troia



This assumption is further supported by the fact that 'pompompurin' contacted Troia a few hours before the spam email campaigns started to simply say “enjoy,” as a warning that something involving the researcher was about to happen.


Troia said that 'pompompurin' messages him every time they start an attack to discredit the researcher.




#### Tags:
[[Troia]] [[emails]] [[Spamhaus]] [[FBI’s]] [[Bleeping Computer]]
