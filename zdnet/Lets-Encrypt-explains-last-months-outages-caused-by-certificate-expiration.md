# Let's Encrypt explains last month's outages caused by certificate expiration
### Fortinet, Shopify and others reported issues last month thanks to the expiration of a root certificate provided by Let's Encrypt.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/lets-encrypt-explains-those-outages-last-month/)
+ Date: October 29, 2021
+ Author: Jonathan Greig


## Article:
Unknown

Dozens of websites and services [reported issues late last month](https://www.zdnet.com/article/fortinet-shopify-others-report-issues-after-root-ca-certificate-from-lets-encrypt-expires/) thanks to the expiration of a root certificate provided by Let's Encrypt, one of the largest providers of HTTPS certificates.


Let's Encrypt and other researchers [had long warned](https://letsencrypt.org/docs/dst-root-ca-x3-expiration-september-2021/) that the IdentTrust DST Root CA X3 would expire on September 30, and many platforms did heed the calls and updated their systems. But a few did not, causing a minor kerfuffle as users questioned why some of their favorite sites were not working as well as they should. 

Scott Helme, the founder of Security Headers, told *ZDNet* that he confirmed issues with Palo Alto, Bluecoat, Cisco Umbrella, Catchpoint, Guardian Firewall, Monday.com, PFsense, Google Cloud Monitoring, Azure Application Gateway, OVH, Auth0, Shopify, Xero, QuickBooks, Fortinet, Heroku, Rocket League, InstaPage, Ledger, Netlify and Cloudflare pages, but noted that there may have been more that went unreported.

[Millions of websites](https://www.zdnet.com/article/lets-encrypt-issues-1-billionth-web-security-certificate/) rely on the services provided by Let's Encrypt, which operates as a free non-profit that makes sure the connections between your device and the internet are secure and encrypted.

Without them, some older devices will no longer be able to verify certain certificates. 

Josh Aas, executive director of the Internet Security Research Group at Let's Encrypt, told *ZDNet* that he was frustrated with how some outlets covered the September outages, with some implying it was a mistake or an accident. 

"We didn't forget that it was going to expire or anything. We've been planning for this for years. We knew that this was going to happen, and we've been literally planning for this for years. Because we've been planning this for years, a lot less stuff broke," Aas said. 






"The internet is a huge place. How many millions or billions of devices and servers and things like that are out there? Any time you change anything, stuff's going to break. I don't want to minimize any disruption that was frustrating to people, but all in all, it could have been worse."

Aas explained that there are three levels of certificates on the internet. There are certificates that websites have called end-entity certificates. Then there are two certificates issued by certificate authorities like Let's Encrypt: root certificates and intermediate certificates. 

Root certificates are the main things that browsers trust, and intermediate certificates are what organizations like Let's Encrypt use to issue to the websites. 

Aas said, end-entity certificates are valid for about 90 days: the intermediate certificates are valid for about five years, and root certificates last for about 20 years. 

When one is set to expire, organizations like Let's Encrypt introduce a new one and ask websites to adopt it before the old one expires. 

"There's really nothing you can do about avoiding certificate expiration. Certificates expire; that is an intended thing. That's just what happens and that happens for a number of different reasons. We can't prevent it. It's designed to expire in that way. Every certificate authority works that way," Aas said.

Let's Encrypt worked with hundreds of websites to get them switched over. Still, the internet has grown significantly, making it difficult to get every website, phone, browser, laptop, and device changed over. 

Aas added that there were always going to be some number of devices and browsers that were not able to make the switch when the old certificate expired. 

"We try to keep that number as low as possible through outreach and giving people tools on how to be ready. But it doesn't get to everybody. The internet is too big for that," Aas explained. 

"We did our best to try to give advice and tell people what they can do to move to the new certificate. And it seems like a lot of people did that. A lot of stuff was fixed relatively quickly."

Aas noted that certificates are designed to expire to protect the set of cryptographic keys behind them. 

"There are two keys that are essentially just really long numbers that are related to each other, and that's how the cryptography behind certificates works. And one of those keys, called a private key, needs to be protected at all times. You don't tell other people. So websites have the private key for their own identity certificates, but certificate authorities like Let's Encrypt hold the private keys for root and intermediate certificates," Aas explained. 

"We have to make sure that nobody else ever finds out what those keys are. They are very heavily protected and guarded by us. But it's possible that somebody could have gotten a copy of the key, and we don't know. As a general safeguard in the industry, we rotate keys every certain amount of time depending on the risk profile and things like that. So, certificate expiration is essentially a mechanism for rotating cryptographic keys on the internet over a certain time to ensure that these keys are never compromised. The longer a key is in use, the more likely it is that there's an issue."

One of Let's Encrypt's root certificates was issued in 2015, and a second one was issued in 2020. The next expiration for these root certificates will be in 15 years and 20 years, respectively. 

The root that expired last month -- IdentTrust DST Root CA X3 -- was issued in 2000. Aas noted that the certificate authority industry started in the late 90s and early 2000s, meaning many of the certificates issued back then are starting to expire. 

"They are sort of clustered in that time period when all these CAs started, so I think we're going to see more and more of these. Every time one of these things expires and causes some issues on the internet, we as a community of people who operate these devices and certificate authorities get a little better at managing the problem," Aas said. 

While users and websites dealt with issues last month, Aas said the silver lining is that it was practice for the next time a certificate expires. 

He urged anyone with more questions about the topic to head to Let's Encrypt's Community Support Forum. 

Other experts echoed what Aas said, explaining that root expirations are a rare but normal occurrence and a necessity in the certificate authority ecosystem.

Ed Giaquinto, CIO of Sectigo and an expert in digital certificates, said outages caused by root expirations are simply results of poor certificate lifecycle management. 

"If an enterprise does not have an accurate inventory of its certificates, including their chains to trusted roots, then outages due to expirations are inevitable. This is another example of how good certificate hygiene prevents outages," Giaquinto said.  

"A proper lifecycle management tool inventories and displays all relevant certificate information, including their expiration dates. Then, using automation, it replaces those certificates prior to expiration, enabling IT teams to be ahead of the game. We no longer exist in a world where we simply manage a few certificates for web front ends. PKI integrations have put certificates everywhere (ephemeral compute services, containers, program-to-program, B2B, and B2C communications, etc.), and proper management of the certificate lifecycle is crucial to preventing business outages."

Keyfactor chief security officer Chris Hickman echoed Giaquinto's comments, telling *ZDNet* that in most cases, the greatest issue is a lack of automation to distribute the new root CA certificate to those devices that need to trust it. 

In many organizations, the root CA certificate stores are not managed universally, Hickman explained, adding that this can lead to situations like only updating parts of the network but not the entity of all devices that need to trust the new root. 

Hickman suggested organizations bring all of their keys and certificates into a single inventory by integrating directly with network endpoints, key stores and CA databases for comprehensive visibility. 

He noted that the first signs of trouble emerged when the AddTrust CA expired in May 2020, causing widespread outages for streaming and payment services like Roku, Stripe and Spreedly. 

Now, products are being designed to manage Roots of Trust out of band to software updates -- but that process doesn't extend to legacy products, he added. 

"If you don't update your legacy roots, you can't push updates, resulting in potential device failure. With multiple root CAs set to expire in 2021, it's essential to ensure that updates can be sent efficiently and effectively to embedded and non-traditional operating systems, recognizing that many legacy devices may be unable to receive these updates," Hickman said. 

"Another wrinkle in all of this is UNIX-based systems, as these devices cannot accept certificates with expirations beyond the year 2038. This situation is poised to be a very big problem without a clear solution that has not received much attention to date." 





#### Tags:
[[websites]] [[certificates.]] [["We]] [[said.]] [[Hickman]] [[Encrypt,]] [[ZDNet]] [[years.]] [[years,]] [[certificates,]] [[ZDNet]]
