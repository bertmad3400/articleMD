# Tiny Font Size Fools Email Filters in BEC Phishing
### The One Font BEC campaign targets Microsoft 365 users and uses sophisticated obfuscation tactics to slip past security protections to harvest credentials.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176198)
+ Date: November 11, 2021  9:00 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/11084639/magnifying-glass-atop-computer-wireless-keyboard-850x567-1-e1636638409871.jpeg)
A new [business email compromise](https://threatpost.com/lewd-phishing-lures-business-explode/166734/) (BEC) campaign targeting Microsoft 365 users is using a range of sophisticated obfuscation tactics within phishing emails that can fool natural language processing filters and are undetectable to end users.


Researchers at [Avanan](https://www.avanan.com/), a CheckPoint company, first discovered the campaign – dubbed One Font because of the way it hides text in a one-point font size within messages – in September.


Attackers also are hiding links within the cascading style sheets (CSS) in their phishing emails: another tactic that serves to confuse natural language filters like Microsoft’s Natural Language Processing (NLP), researchers said in a [report](https://www.avanan.com/blog/the-onefont-attack-manipulation-and-obfuscation) posted online Thursday.


The One Font campaign also includes messages with links coded within the <font> tag, which – in combination with the other obfuscation techniques – also destroy the effectiveness of email filters that depend on natural language for their analysis, according to Jeremy Fuchs, a cybersecurity researcher at Avanan.


“This breaks semantic analysis, which leads many solutions to treat it as a marketing email, as opposed to phishing,” Fuchs wrote. “Natural language filters see random text; human readers see what the attackers want them to see.”


The recent campaign is similar to one Avanan researchers [discovered](https://www.avanan.com/blog/zerofont-phishing-attack) in 2018 called ZeroFont, which used similar tactics to get past Microsoft NLP in its Office 365 security protections. That campaign inserted hidden text with the font size of zero within messages to trip up email scanners that depend on natural language to weed out malicious emails.


Like that campaign, One Font also [targets Office 365 organizations](https://threatpost.com/office-365-phishing-campaign-kasperskys-amazon-ses-token/175915/) and can lead to BEC and ultimately endanger the corporate network if the messages aren’t flagged and users are duped into giving up their credentials, researchers said.


**Obfuscation Sophistication**
------------------------------


Indeed, since the ZeroFont campaign, cybercriminals have gotten increasingly sophisticated in their tactics to slip past the NLP used in common email filters, researchers said. Other techniques that Avanan researchers have observed include redirect tactics like [meta refresh](https://www.avanan.com/blog/metamorph-html-obfuscation-phishing-attack) that can disrupt NLP and bypass [Microsoft SafeLinks](https://www.avanan.com/blog/microsoft-safelinks-under-attack), they said.


Once it makes it to inboxes appearing to be a legitimate message, the One Font campaign uses typical phishing social-engineering tactics to get people’s attention. Attackers present what looks like a password-expiration notice, using urgent messaging to spur a potential victim into clicking on a malicious link.


That link carries them to a phishing page where they appear to be entering their credentials so they can change their passwords. Instead, threat actors are stealing their credentials to use for other cybercriminal activity, researchers said.


In their post, researchers demonstrated how specific phishing emails used a combination of tactics – specifically, links hidden within the CSS and links slipped within the <font> tag and then sized down to zero – that together confound natural language filters.


Because such obfuscation techniques are invisible to the end user, flagging such messages as malicious can be tricky, Fuchs noted. To avoid these messages slipping past filters, researchers recommend that organizations use a multi-tiered security solution that combines advanced artificial intelligence and machine learning, as well as static layers like domain and sender reputation, he wrote.


Using a security architecture that relies on more than one factor to block email and requiring corporate users to confirm with an IT department before engaging with any email that asks for a password change also can serve to mitigate attacks, Fuchs wrote.


*Image courtesy of [Debora Cartagena, USCDCP](https://pixnio.com/objects/electronics-devices/computer-components-pictures/magnifying-glass-atop-computer-wireless-keyboard).*


***Cybersecurity for multi-cloud environments is notoriously challenging. OSquery and CloudQuery is a solid answer. Join Uptycs and Threatpost on Tues., Nov. 16 at 2 p.m. ET for “***[***An Intro to OSquery and CloudQuery***](https://bit.ly/3wf2vTP)***,” a LIVE, interactive conversation with Eric Kaiser, Uptycs’ senior security engineer, about how this open-source tool can help tame security across your organization’s entire campus.***


[***Register NOW***](https://threatpost.com/webinars/multi-cloud-security-and-visibility-an-intro-to-osquery-and-cloudquery/?utm_source=uptycs&utm_medium=email&utm_campaign=event&utm_id=uptycs&utm_term=nov_event&utm_content=IA) ***for the LIVE event and submit your questions ahead of time via the registration page.***




#### Tags:
[[phishing]] [[said.]] [[Microsoft]] [[Fuchs]] [[wrote.]] [[NLP]] [[ThreatPost]]
