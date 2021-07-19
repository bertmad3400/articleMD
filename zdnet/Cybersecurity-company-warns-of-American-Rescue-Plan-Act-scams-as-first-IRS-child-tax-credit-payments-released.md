# Cybersecurity company warns of American Rescue Plan Act scams as first IRS child tax credit payments released
### The credential harvesting sites are targeting those who don't know the IRS will automatically send the payment to you.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/cybersecurity-company-warns-of-american-rescue-plan-act-scams-as-first-irs-child-tax-credit-payments-released/)
+ Date: July 19, 2021 -- 21:22 GMT (22:22 BST)
+ Author: Jonathan Greig


## Article:
Unknown

Cybercriminals are taking advantage of the latest round of IRS payments being sent out to families across the US by launching dozens of credential harvesting sites masquerading as American Rescue Plan Act signup sites, according to a [new report from DomainTools](https://www.domaintools.com/resources/blog/american-rescue-plan-act-lures-in-the-wild).

Last week, the IRS began sending out the [first round of child tax credit](https://www.cnet.com/personal-finance/taxes/how-can-i-use-the-irs-child-tax-credit-portals-check-payments-add-bank-details-opt-out/) payments that were part of the larger American Rescue Plan Act passed earlier this year. The payments will be sent automatically by the IRS and require no sign-up. 

But cybercriminals have created a maze of associated websites all aiming to trick people into entering their personal information by pretending to be associated with the child tax credit payments, DomainTools' Chad Anderson explained. 

Anderson said that by analyzing historical WHOIS information and OSINT techniques, the cybersecurity company was able to tie this specific credential harvesting scam to GoldenWaves Innovations, a web development firm based in Nigeria. 

ZDNet called and emailed GoldenWaves for comment but received no response. 

The fake sites look exactly like government websites, explain the payments in detail and ask users to "apply now." One site, with the name "reliefcarefunds[.]com," asks for names, addresses, social security numbers, photos of drivers licenses and even your mother's maiden name. 

![american-rescue-plan-act-lures-in-the-wild-image-1.jpg]()![american-rescue-plan-act-lures-in-the-wild-image-1.jpg](https://www.zdnet.com/a/hub/i/r/2021/07/19/6906c5d0-b9f4-44c8-aa30-c6e8b06e38c5/resize/470xauto/bcda061ea4574def621a5c625054cc10/american-rescue-plan-act-lures-in-the-wild-image-1.jpg)The credential harvesting sites are meant to look exactly like government websites. 


 DomainTools
 That site was connected to "americaforgivenrelieffund[.]com" and both were registered and hosted through NameCheap. DomainTools was able to tie those two sites and 39 other domains to an email address: goldenwaves247@gmail[.]com.






Anderson said researchers found that many of the links associated with the email were also being sent out through Bitly link shortening links, which allowed the people behind the scam to name the link "Unemployment Insurance Relief During COVID-19 Outbreak | American Rescue Plan Act."

These links brought the researchers to other sites that were hosted on Garanntor and OVH, providing them with even more information about the creator and tying all of the sites to an email address registered in Ibadan, Nigeria.

"The city of Ibadan is a small, rural town which makes the registration information stand out as almost always technical contacts for Nigerian domains are located in Lagos, the capital city and technology center," Anderson wrote. "Additional searches reveal the same username participating in sales on cybercrime forums, Steam gaming, and other social media sites."


Anderson added that it is with "medium confidence" that DomainTools' researchers believe GoldenWaves Innovations -- which is also registered in Ibadan -- was a "legitimate web design firm in front of the identity document harvesting sites."

GoldenWaves Innovations has a working website with a CEO who has a full profile on LinkedIn. 

"Additionally, the historical WHOIS record unearths an address in New York, New York of 120 E 87th Street. This is an apartment building with condos ranging from $900,000 to $13,000,000 in the heart of Manhattan. While at first that seems strange for a company based in Nigeria, we can see from LinkedIn that one of the company's developers claims to live in New York City," Anderson said.

"Looking at the CEO's current contact information on LinkedIn we can see that GoldenWaves Innovations has a new website in goldenwaves[.]com[.]ng which is also tied to the same email address and registration information. This gives DomainTools researchers high confidence that all of these credential harvesting sites are linked to GoldenWaves Innovations in Nigeria. These sites along with any new ones that have cropped up were reported to Google Safe Browsing for blocking."

Anderson included a list of the domain names being used in the scam and told ZDNet that US law enforcement was informed about the sites. 

When asked why a seemingly legitimate business would tie itself to credential harvesting sites, Anderson said "it's certainly sloppy" but added that this proved the usefulness of historical WHOIS data.

Other cybersecurity experts, like Digital Shadows cyber threat intelligence analyst Stefano De Blasi, said that along with extracting credentials, impersonating domains are frequently leveraged to extract financial information, deploy malware on a victim's machine, and distribute disinformation content. 

"Additionally, users may be tricked into opening these malicious pages via spear-phishing emails or SMS, as well as being redirected there from other illegitimate websites. In both cases, if an attacker knows enough of social engineering techniques to pressure a victim into opening the URL and inserting their credentials," De Blasi told ZDNet. 

"Social engineering attacks remain a predominant initial attack vector for threat actors, thus certifying that they keep working on many people despite its rather simplistic approach. Registering these domains is a trivial task for most attackers, thanks to prepared phishing kits and tutorials that attackers can easily find in cybercriminal forums. However, when registering hundreds of malicious domains, a careless attacker may well leave some crucial pieces of evidence behind that can then be gathered and analyzed by security researchers to assess attribution."





#### Tags:
[[DomainTools]] [[GoldenWaves]] [[websites]] [[WHOIS]] [[ZDNet]] [[Ibadan]] [[LinkedIn]] [[ZDNet]]
