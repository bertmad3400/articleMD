# ProtonMail Forced to Log IP Address of French Activist
### The privacy-touting, end-to-end encrypted email provider erased its site’s “we don’t log your IP” boast after France sicced Swiss cops on it. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169242)
+ Date: September 7, 2021  12:07 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/07114806/Paris-protest-e1631029702922.jpeg)
The privacy-hugging, end-to-end encryption-providing email provider [ProtonMail](https://protonmail.com/) was forced to log the IP address of a French activist and turn it over to Europol, according to a French police report that came to light over the weekend.


The activist was arrested as a result.


In the wake of the news, users have been pelting the company with questions, in spite of ProtonMail swearing up and down that it doesn’t log IP addresses by default and that it only complies with local regulations – in this case, Swiss law.


Here’s a translation of the redacted police report, followed below by a tweet of that report:



Andy Yen, ProtonMail founder and CEO, on Sunday posted a [statement](https://www.reddit.com/r/ProtonMail/comments/pil6xi/climate_activist_arrested_after_protonmail/hbqha63/) about the incident to Reddit and followed up with a Monday [blog post](https://protonmail.com/blog/climate-activist-arrest/).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Yen pointed out that ProtonMail didn’t cooperate with French authorities when they asked for details about the user. Hence, French police sent a request to Swiss police via Europol and thus managed to force the company to hand over the IP address and device details of the French activist.


Yen pointed out that from the get-go, ProtonMail has said that the company can be legally compelled to log IP addresses. From his Monday post:



> There is a difference between security/privacy, and anonymity. As we wrote in our [public threat model](https://protonmail.com/blog/protonmail-threat-model/) (published back in 2014), “The internet is generally not anonymous, and if you are breaking Swiss law, a law-abiding company such as ProtonMail can be legally compelled to log your IP address.” This cannot be changed due to how the internet works. However, we understand this is concerning for individuals with certain threat models, which is why since 2017, we also provide [an onion site](http://protonmail.com/tor) for anonymous access (we are one of the only email providers that supports this).
> 
> 


As Yen pointed out, ProtonMail, which was originally developed by CERN and MIT scientists, added its own [Tor hidden service](https://threatpost.com/protonmail-gets-own-tor-accessible-onion-hidden-service/123192/) in 2017. Although the email service was already encrypted by design, the option to route traffic through Tor was meant to prevent eavesdroppers from listening in on users’ connections, in order to make the service more resistant to censorship and surveillance.


Aaccording to Yen’s Reddit post. “Under no circumstances however, can our encryption be bypassed, meaning emails, attachments, calendars, files, etc., cannot be compromised by legal orders.”


Policy Switcheroo
-----------------


Commenters on his Sunday Reddit post had asked pointed questions about whether ProtonMail has been in the habit of logging IP addresses and fingerprinting devices before Swiss authorities compelled the company to do so.



> So do you log our info (like IPs) or not? Do you keep a database of it? —Reddit commenter “fuckparalysis”
> 
> 


“This is obviously not done by default, but only if Proton gets a legal order for a specific account,” Yen said via Reddit.


As of Saturday, the company’s homepage promised that it doesn’t keep IP logs:



> No personal information is required to create your secure email account. By default, we do not keep any IP logs which can be linked to your anonymous email account. Your privacy comes first. —[Wayback Machine](https://web.archive.org/web/20210904001234/https://protonmail.com/)
> 
> 


But as of Monday, the company had minced that promise, which now reads:



> ProtonMail is email that respects privacy and puts people (not advertisers) first. Your data belongs to you, and our encryption ensures that. We also provide an [anonymous email](https://protonmail.com/tor) gateway. —[ProtonMail homepage](https://protonmail.com/)
> 
> 


 


ProtonMail also updated its privacy policy on Monday. It now reads: “If you are breaking Swiss law, ProtonMail can be legally compelled to log your IP address as part of a Swiss criminal investigation.”


From its Reddit statement:


“In this case, Proton received a legally binding order from the Swiss Federal Department of Justice which we are obligated to comply with. There was no possibility to appeal or fight this particular request because an act contrary to Swiss law did in fact take place (and this was also the final determination of the Federal Department of Justice which does a legal review of each case).”


It doesn’t matter what service you use, Yen wrote in the Reddit statement: Unless you manage to set up shop in a dinghy, service providers are subject to the authorities in whatever terra firma they’re based.


“No matter what service you use, unless it is based 15 miles offshore in international waters, the company will have to comply with the law,” according to his statement. “The Swiss legal system, while not perfect, does provide a number of checks and balances, and it’s worth noting that even in this case, approval from three authorities in two countries was required, and that’s a fairly high bar which prevents most (but obviously not all) abuse of the system.”


Under Swiss law, it’s obligatory for suspects to be notified that their data was requested, he added, which puts Switzerland a cut above most countries. ProtonMail hasn’t clarified the timing on when it handed over the activist’s data and when the company notified the user that they’d received a request for the user’s IP address and browser fingerprint.


Anti-Gentrification Surveillance Target
---------------------------------------


With regards to what Swiss law was broken to trigger authorities’ demand for the French user’s data, police were targeting a group called Youth for Climate, according to a [blog](https://secoursrouge.org/france-suisse-securite-it-ProtonMail-a-communique-a-la-police-ladresse-ip-de-militant%c2%b7es-anti-gentrification/) published by French left-wing political activists. According to a post on that site, after French police got the activist’s data, they figured out that the activists’ collective communicated via ProtonMail:



> The police also noticed that the collective communicated via a ProtonMail email address. They therefore sent a requisition (via EUROPOL) to the Swiss company managing the messaging system in order to find out the identity of the creator of the address. ProtonMail responded to this request by providing the IP address and the fingerprint of the browser used by the collective. It is therefore imperative to go through the tor network (or at least a VPN) when using a ProtonMail mailbox (or another secure mailbox) if you want to guarantee sufficient security.
> 
> 


The group has been protesting gentrification, real-estate speculation, Airbnb and high-end restaurants near Place Sainte Marthe in Paris. The protests have included [squatting](https://www.lemonde.fr/police-justice/article/2021/01/02/a-paris-bras-de-fer-entre-le-restaurant-le-petit-cambodge-et-des-squatteurs-contre-la-gentrification_6065035_1653578.html) in a long-abandoned building that was at one point rented by Le Petit Cambodge: A restaurant that was targeted by the Nov. 13, 2015 terrorist attacks in Paris.


According to [a Sept. 1 article](https://paris-luttes.info/recit-policier-de-sainte-marthe-15258?lang=fr) the group published to Paris-luttes.info, an anti-capitalist news website, there have been multiple arrests and legal actions taken against the protesters as their cause has expanded beyond the Paris neighborhood that birthed it.


**It’s time to evolve threat hunting into a pursuit of adversaries.** [**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **Threatpost and Cybersixgill for** [**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **and get a guided tour of the dark web and learn how to track threat actors before their next attack.** [**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **for the LIVE discussion on September 22 at 2 PM EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[ProtonMail]] [[IP]] [[Reddit]] [[doesn’t]] [[case,]] [[law,]] [[ThreatPost]]
