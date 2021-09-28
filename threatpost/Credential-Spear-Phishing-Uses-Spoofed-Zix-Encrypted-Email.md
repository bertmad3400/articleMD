# Credential Spear-Phishing Uses Spoofed Zix Encrypted Email
### The spoofed email has targeted close to 75K inboxes, slipping past spam and security controls across Office 365, Google Workspace, Exchange, Cisco ESA and more.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175044)
+ Date: September 28, 2021  6:00 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/23070332/phishing-farm.jpg)
Armorblox researchers have spotted an ongoing credential-phishing attack that spoofs an encrypted Zix email – one coming, weirdly enough, from what looks like a legitimate domain associated with the Baptist religion.


At least, the threat actor is sending the phishing attack from “thefullgospelbaptist[.]com”: a domain that might be a deprecated or old version of a legitimate Baptist domain, fullgospelbaptist[.]org, which is a religious organization established in 1994.


In a [Tuesday post](https://www.armorblox.com/blog/blox-tales-zix-credential-phishing), researchers said that, to date, the fake-Zix encrypted email has targeted close to 75,000 inboxes and has slipped past embedded spam and security controls across Office 365, Google Workspace, Exchange, Cisco ESA and others.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


God isn’t sending encrypted Zix messages: If hapless users click on the spoofed email’s link, it will try to download a presumably unholy HTML file onto their system.


The attack is targeting a range of companies across sectors including state and local government, education, financial services, healthcare, and energy, selectively going after a mix of senior executives and cross-departmental employees.


In fact, Armorblox’s research team found that the attacker is cherry-picking targets, being careful to select no more than one employee in any single department, probably to forestall the “Hey, did you get this weird email?” chat among officemates.


The Bogus Zix Email
-------------------


Zix is a [key player](https://manometcurrent.com/email-encryption-market-size-share-growth-analysis-trend-and-forecast-research-report-by-2027key-player-are-cisco-systems-inc-micro-focus-international-plc-trend-micro-inc-sophos-group-plc/) in the email encryption market, right up there with Cisco Systems, Trend Micro, Proofpoint, Sophos and Norton LifeLock, et al.


Building on the name recognition alone helps the email to pass a sniff test it should rightfully flunk. But beyond the brand name alone, the email attack also uses a “gamut” of additional techniques to evade traditional security filters and to “pass the eye tests of unsuspecting end users,” Armorblox explained, including social engineering, exploiting a legitimate-looking Baptist domain and replication of existing workflows.


The subject header is “Secure Zix message.” The email body’s header reiterates that title and tells the intended victim that they’ve received a secure Zix message. Click on the “Message” button to check it out, the email instructs.


Armorblox provided screenshots of both a genuine Zix secure message and the spoofed Zix secure message notification. As you can see below, the two interfaces aren’t identical, but they’re close enough to trick unsuspecting users.


Satan Wants Select Employees to Click on ‘Message’
--------------------------------------------------


Clicking on the “Message” link in the email will trigger an attempted drive-by download of an HTML file named “securemessage.” Armorblox researchers couldn’t open that file in their virtual machine (VM) instance, since that’s not where the redirect appeared. Fortunately, by the time researchers wrote up the attack, most site blockers were erecting a block page to prevent systems from getting infected.


As far as the threat actor’s preferred prey goes, Armorblox had a few examples: For example, one of the SLED (state and local government and education) businesses that Armorbox counts as customers experienced an attack wherein the targets included the CFO, a director of operations, a director of marketing and a professor.


Another example: The credential phishers went after a wellness company, targeting the senior vice president of finance and operations, the president, and a utility email alias (member.services@company[.]com).


Why such a seemingly random spread? The researchers theorized that the attackers might have deliberately chosen their victims “to be across departments and to contain a good mix of senior leadership and individual contributors.”


As well, the attackers may have gone after people who don’t tend to turn to each other if they receive a suspicious email, Armorblox explained.


Slippery Techniques
-------------------


Armorblox summed up these techniques that the spoofed Zix email is using to evade traditional email security filters and watchful eyes:


It’s easy to see how getting an email that somebody bothered to encrypt could pique recipients’ curiosity. A May 2021 [report](https://www.securityadvisor.io/old-hacks-new-tricks/) from Security Advisor found that the curiosity effect – the desire to resolve uncertainty – has shown up as one of the top three cognitive biases to be exploited in phishing attacks, appearing in 17 percent of such attacks.


Armorblox researcher Abhishek Iyer told Threatpost on Monday that using legitimate (if unrelated) domains to send emails “is more about tricking security controls (i.e. bypassing authentication checks) than it is about tricking recipients, especially if the domains are not spoofed to look like the real thing.”


An example that Armorblox came across last year was a [Verizon credential phishing](https://www.armorblox.com/blog/blox-tales-verizon-credential-phishing/) campaign where the page was hosted on the website of a Wiccan coven. Another example: an [Amazon credential phishing](https://threatpost.com/amazon-phishing-campaigns-security-checks/157495/) campaign where the email was sent from the domain of Blomma Flicka Flowers, a small floral design company based out of Vermont. The campaign aimed to lift credentials and other personal information under the guise of Amazon package-delivery notices.


“Whether these domains are used to send the email or host the phishing page, the attackers’ intent is to evade security controls based on URL/link protection and get past filters that block known bad domains,” Iyer said via email.


Needless to say, the legitimate Baptist organization had nothing to do with the Zix campaign, he continued. “To host phishing pages on legitimate domains, attackers usually exploit vulnerabilities in the web server or the Content Management Systems (CMS) to host the pages without the website admins knowing about it.”


“System 1 thinking” is a reference to Daniel Kahneman’s book, “Thinking, Fast and Slow,” which delves into our brains’ two information processing and decision making systems, System 1 being “the automatic, unconscious, and fast mode of thinking, offering little to no rationale behind its actions.” System 2 thinking is what we need when we look into our inboxes: That’s the “slow, methodical, and analytical mode of thinking, skeptical and rational by default,” Armorblox explained.


“Security awareness training programs require us to operate in the System 2 mode of thinking, encouraging us to be suspicious of emails we receive,” Armorblox co-founder Arjun Sambamoorthy recommended in [a post](https://www.armorblox.com/blog/the-fault-in-our-emails-why-everyone-still-falls-for-phishing-attacks/) earlier this month.


Phishing Is Getting Harder to Spot
----------------------------------


In a recent column for Threatpost’s InfoSec Insider series, Troy Gill, manager of security research at Zix, discussed the most common ways sensitive data [is scooped up](https://threatpost.com/insider-outsider-data-loss-threats/167063/) by nefarious sorts. His thoughts on how easy it is for any of us to fall for increasingly sophisticated phishing attempts such as the Zix spoofed email:


“Everyone wants to believe that they wouldn’t fall victim to typical phishing scams. However, the truth is that these methods of intrusion are [getting harder to spot](https://threatpost.com/google-docs-host-attack/166998/) as cybercriminals become more savvy with their tactics. Cybercriminals continue to build on trickier spear-phishing strategies that rely on brand-new techniques and even more [deceitful tricks](https://threatpost.com/geek-squad-vishing-bypasses-email-security/167014/) that can catch even the most discerning person unaware.” —Troy Gill, [Threatpost InfoSec Insider column](https://threatpost.com/insider-outsider-data-loss-threats/167063/).


How to Protect Your Business
----------------------------


Armorblox provided this guidance and recommendations to keep the credential-phishers at bay:


The spoofed Zix email got past the security controls of Office 365, Google Workspace, Exchange, Cisco ESA and others. Armorbox recommended that for better protection coverage against email attacks, be they spear-phishing, [business email compromise](https://threatpost.com/ppe-covid-19-medical-supplies-bec-scams/154806/) (BEC) or credential phishing attacks like this one, “organizations should augment built-in email security with layers that take a materially different approach to threat detection.”


The screenshot below shows the spoofed Zix email with a Spam Confidence Level (SCL) score of -1. As Microsoft outlines in its [matrix of spam confidence level](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/spam-confidence-levels?view=o365-worldwide) (SCL) in Exchange Online Protection, a rating of -1 means that the message skipped spam filtering and was delivered, since it was assumed to be “from a safe sender, was sent to a safe recipient, or is from an email source server on the IP Allow List.”


“Since we get so many emails from service providers, our brains have been trained to quickly execute on their requested actions. It’s much easier said than done, but engage with these emails in a rational and methodical manner whenever possible,” researchers recommended. “Subject the email to an eye test that includes inspecting the sender name, sender email address, language within the email, and any logical inconsistencies within the email (e.g. *Why is a Zix link leading to an HTML download? Why is the sender email domain from a third-party organization?*).”


“Since all workplace accounts are so closely interlinked, sharing credentials to one of your accounts can prove to be very dangerous as cybercriminals send emails in your name to trick your customers, partners, acquaintances, and family members,” Armorblox said.


Its specific recommendations:


If you haven’t already, implement these hygiene best practices:


**Rule #1 of Linux Security:** No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.




#### Tags:
[[Zix]] [[Armorblox]] [[phishing]] [[emails]] [[Linux]] [[Threatpost]] [[HTML]] [[thinking,]] [[ThreatPost]]
