# These are the top-level domains threat actors like the most
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/these-are-the-top-level-domains-threat-actors-like-the-most/)
+ Date: November 12, 2021
+ Author: Bill Toulas


## Article:
![internet-earth](https://www.bleepstatic.com/content/hl-images/2021/11/12/internet.jpg?rand=257517423)


​Out of over a thousand top-level domain choices, cyber-criminals and threat actors prefer a small set of 25, which accounts for 90% of all malicious sites.


Six out of the top 10 of these 25 top-level domains (TLD) are handled by authorities in developing countries, hosting a disproportionately large number of risky sites compared to their populations.



![Example of a TLD](https://www.bleepstatic.com/images/news/security/tld.png)**Example of a TLD**  
*Source: Unit42*
These stats are revealed in an in-depth analysis from researchers at Palo Alto Networks, who took a deep dive into the TLDs commonly used by threat actors and why they are being chosen.


The categories picked for analysis are malware, phishing, command and control (C2), and grayware (adware, 'joke malware,' spyware).


The worst cases
---------------


Using data collected on October 7th, 2020, Palo Alto Networks analyzed domains categorized by their Advanced URL Filtering service, and that met specific criteria.


"First, we only study domains categorized by the Advanced URL Filtering service, and we only consider registered domains (also called root domains). Additionally, we validate whether domains existed the past one year by checking zone files and passive DNS, and by issuing active DNS queries. We do not consider domains that we categorize as [parked](https://unit42.paloaltonetworks.com/domain-parking/), insufficient content or unknown for our calculations," explains the research by Palo Alto Networks Unit42.


"Further, when calculating reputation scores, we don’t consider domains [sinkholed](https://en.wikipedia.org/wiki/DNS_sinkhole#Applications) for preemptive measures as malicious. Finally, we only consider TLDs with at least a hundred domains, as smaller TLDs likely have policies in place restricting entities allowed to register domain names. This blog post is based on data collected on Oct. 7, 2021."


Using this data, Palo Alto Networks created the following summary table to give an overview of the malicious use of the top TLDs for each category and their cumulative distribution (CD). The higher the CD, the more that particular TLD is used for the category.



![TLDs with the highest volumes of malicious content distribution](https://www.bleepstatic.com/images/news/u/1220909/Tables/table.jpg)**Table 1: TLDs with the highest volumes of malicious content distribution**  
*Source: Unit42*
The most popular top-level domain is .com, which has an average ratio of malicious domains. Crooks tend to use it because it adds legitimacy and generally improves their success rates.


Those that fair the worse in the ‘cumulative distribution’ category are .xyz, .icu, .ru, .cn, .uk, and tk. This means that most of the bad stuff circulating the web in terms of volume comes from these domains.


The TLDs that distribute malware the most are .ga, .xyz, .cf, ,tk, .org, and .ml.


Phishing actors prefer to use .net domains, with .pw, .top, .ga, and .icu, following with notable volumes. However, the researchers found phishing to be one of the most evenly distributed categories, with 99% of the domains spreading across 92 different TLDs.


Grayware is being distributed through .org, .info, .co, .ru, .work, .net, and .club domains, indicative of the trickery that underpins this category of software.


Finally, C2 infrastructure usually relies on .top, .gq, .ga, .ml, .cf, .info, .cn, and .tk.


Palo Alto compiled the following table in terms of the rate of malicious domains compared to the total registrations for a TLD.


In the table below, the MAD score is the 'median of the absolute deviation,' which means that a higher score represents an unusually large number of malicious domain registrations for that TLD.



![TLDs with the highest rate of malicious domains](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**TLDs with the highest rate of malicious domains**  
*Source: Unit42*
Why does any of that matter?
----------------------------


The fact that the TLD domains for Tokelau, a small island in the Pacific, are in the top ten of all malicious categories means that the relevant registration authority is likely not following strict reviewing practices.


"One of the most fascinating stories in the domain name world is how .tk, the ccTLD of a small Pacific island called Tokelau, became one of the most populous TLDs in the world. Domain registrations contributed at one point [one-sixth of Tokelau's income](https://www.cnn.com/2012/06/13/tech/web/tokelau-domain-name-holder/index.html)," explains the [report by Palo Alto Networks](http://unit42.paloaltonetworks.com/top-level-domains-cybercrime/).


"Their TLD became popular by providing free domain registrations, where the source of income for the TLD operator is through advertisement rather than domain registration fees. Unfortunately, their domain registration policy also invites abuse, spam and a large amount of sensitive content, as we can observe in Table 1."


The same applies to .pw and .ws domains, controlled by the Republic of Palau and Western Samoa.


These countries offer cheap or even free domain registrations to generate income from ads running on sites.


This advertising model generates significant revenue from domain registrations but also opens the door for widescale abuse.


This, of course, doesn't mean that large TLDs such as .net, .org, and .xyz, can afford to relax against abusive registrations. On the contrary, the stats show that popular TLDs are more responsible for clearing up malicious registrations.


In many cases, legitimate domains on these larger TLDs are compromised by threat actors, so they were not registered with malicious intent.


Another reason why such reports are helpful is that they can help Internet security solutions strengthen their malicious domain detection algorithms.


These rates can be used as factors that are evaluated in conjunction with other elements to generate a total risk score when determining if security software or gateways should block an URL.




#### Tags:
[[TLDs]] [[Palo]] [[domains,]] [[TLD]] [[top-level]] [[Unit42]] [[.xyz,]] [[.ga,]] [[.org,]] [[Bleeping Computer]]
