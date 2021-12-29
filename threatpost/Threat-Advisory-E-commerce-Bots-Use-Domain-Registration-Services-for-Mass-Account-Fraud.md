# Threat Advisory: E-commerce Bots Use Domain Registration Services for Mass Account Fraud
### Jason Kent, hacker-in-residence at Cequence Security, discusses sneaky shopping bot tactics (i.e., domain parking) seen in a mass campaign, and what retail security teams can do about them.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177305
+ Date: 2021-12-29T19:13:45+00:00
+ Author: Jason Kent


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/05/19122836/Botnet2-e1621441729944.jpg)

While researching a recent large-scale bot campaign with CQ Prime Threat Research team lead, Dean Lendrum, we found attackers using domain parking and monetization services to register multiple domains, creating a large number of fake eCommerce accounts per domain.


TL; DR
------


* Analysis of shopping-bot campaign data uncovered more than 850,000 fake accounts associated with a relatively small number of domains.
* Clusters and common patterns point to domain-name registration and hosting services (like Namecheap); with parking, monetization and email forwarding being used to execute large-scale shopping bot campaigns.
* Retailers should analyze historic data to uncover patterns emanating from suspicious domains using the same hosting infrastructure. Patterns observed include irregular domain names, domain resolving to an untrusted web app, SSL not enabled.
* Send email account-creation verification or consider the use of multifactor authentication (MFA) when possible.


Details
-------


Like it or not, malicious bot managers are business people and they are always looking for ways to reduce the cost of their [eCommerce bot campaigns](https://threatpost.com/pandemic-grinchbots-surge-activity/176898/). Using domain parking and monetization services (e.g., Namecheap, ParkingCrew, etc.) is one way they can inexpensively create many fake accounts that they can then use in their large-scale bot campaigns. Fake accounts associated with the registered domains come complete with email-forwarding enabled. When used in the bot campaign, the emails will appear valid to the retailer, but behind the scenes, the forwarding service will just drop the mails.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


To demonstrate how easy this is to do, we were able to establish an account for $1.18 in less than five minutes using Namecheap, one of several domain parking solutions available. Getting started was as easy as depositing funds into a Namecheap account and using its API to call *namecheap.domains.create.* We now had a domain and an associated account with free VPN and business email for two months; free email forwarding forever; and SSL as an option at $10 per year.


Shortly thereafter we were able to begin monetizing the new domain via the Namecheap-ParkingCrew partnership; a common practice for threat actors, evidenced by bot forums boasting of the money being made via rogue traffic hitting their parked domains.


Attack Characteristics Observed
-------------------------------


When investigating any of the domains on their own, everything appears to be normal. But, when grouping the bad-acting domains by their companion web server A records and mail-redirect server MX records, clusters of behavior begin to form.


* 863,874 fake accounts were mapped to 1,810 domains, generating heavy bot traffic.
* Of those 1,810 domains, 440 were mapped to Namecheap and ParkingCrew, and only 255 of them had SSL enabled.


The lack of SSL is a clear sign that the domain is suspicious, given that nearly all legitimate domains will have it enabled. The only reason we can think of for the lack of SSL is the cost – it’s an added $10 per year, going back to the position that the bot operators are looking to reduce costs.


When analyzing suspected fraudulent user accounts and associated orders, retail security teams should investigate the email domain the web and email traffic are resolving to legitimate domains using tools like *mxlookup* and *dig.* If mail exchange servers are common between many different domains as shown in image 1, check the domain name and see if this resolves to a valid web application. Similarly, analyze whether many domains are pointing to a single web server A record and check the web application hosted, taking note of content, purpose and security features like SSL.


Implications of Mass Shopping Bot Campaigns
-------------------------------------------


Just as bots-as-a-service have made botting available to the masses, the use of domain registration and monetization services is another example of the commercialization of the botting industry. In this example, threat actors are able to easily create many thousands of fake accounts for use in their large-scale bot campaigns which in turn, impacts the entire business. Security and fraud teams are overwhelmed trying to separate legitimate from malicious. In some cases, infrastructure costs will spike due to the increased volume, while sales and marketing metrics are skewed wildly by the illegitimate traffic.


***Jason Kent is Hacker-in-Residence at [Cequence Security](http://www.cequence.ai).***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by visiting our [microsite](https://threatpost.com/microsite/infosec-insiders-community/).***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]] [[victim.industry.name=Retail]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ssl]] [[Large-scale]] [[Namecheap]] [[ThreatPost]]

