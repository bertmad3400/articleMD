# Lazarus hackers target defense industry with fake Lockheed Martin job offers | ZDNet
### The APT has previously masqueraded as Northrop Grumman and BAE Systems.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/lazarus-hackers-target-defense-industry-with-fake-lockheed-martin-job-offers/
+ Date: 2022-02-09 09:31:42
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/fdfea955ff090c234e9b45387c3d41e42db24ea6/2021/08/20/892938aa-dec1-45a5-a40a-5e1dcd76ce6d/shutterstock-327882299.jpg?width=770&height=578&fit=crop&auto=webp)

Lazarus has been tied to a new campaign attacking hopeful job applicants in the defense industry. 


The [advanced persistent threat](https://www.zdnet.com/article/lazarus-state-hacking-group-now-hides-payloads-in-bmp-image-files/) (APT) group has been impersonating Lockheed Martin in the latest operation. The Bethesda, Maryland-based company is involved in aeronautics, military technology, mission systems, and space exploration. 

Lockheed Martin generated $65.4 billion in sales in 2020 and has approximately 114,000 employees worldwide.  

Lazarus is a state-sponsored hacking group with [ties to North Korea](https://www.zdnet.com/article/snatchcrypto-campaign-plants-backdoors-in-crypto-exchanges-defi-blockchain-networks/). The prolific and sophisticated group is generally financially-motivated and is believed to be responsible for [serious attacks](https://www.zdnet.com/article/vyveva-lazarus-latest-weapon-strikes-south-african-freight/) in the past beginning with the WannaCry ransomware outbreak, as well as the $80 million heist against Bangladeshi Bank, assaults against freight companies, and South Korean supply chains.  

On February 8, Qualys Senior Engineer of Threat Research Akshat Pradhan revealed [a new campaign](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns) using Lockheed Martin's name to attack job applicants.  

In a similar way to past activities that abused the reputation of Northrop Grumman and BAE Systems, Lazarus is sending targets phishing documents pretending to offer employment opportunities.  

The documents, named *Lockheed\_Martin\_JobOpportunities.docx* and *Salary\_Lockheed\_Martin\_job\_opportunities\_confidential.doc*, contain malicious macros which trigger shellcode to hijack control flow, retrieve decoy documents, and create Scheduled tasks for persistence.  






Living Off the Land Binaries (LOLBins) are also abused to further the compromise of the target machine. However, when the malicious scripts attempted to pull in a further payload, an error was returned -- and so Qualys can't be sure what the final malware package was meant to achieve.  

"We attribute this campaign to Lazarus as there is significant overlap in the macro content, campaign flow, and phishing themes of our identified variants as well as older variants that have been attributed to Lazarus by other vendors," Pradhan says.  

This isn't the first time Lazarus has exploited job candidates or vacancies. [F-Secure](https://www.zdnet.com/article/lazarus-group-strikes-cryptocurrency-firm-through-linkedin-job-adverts/) has previously found samples of phishing emails, masquerading as job offers, that were sent to a system administrator belonging to a targeted cryptocurrency organization. 

In related research, Outpost24's Blueliv cybersecurity team has named Lazarus, Cobalt, and FIN7 as the [most prevalent](https://www.zdnet.com/article/fingers-point-to-lazarus-cobalt-fin7-as-key-hacking-groups-focused-on-finance-industry/) threat groups targeting the financial industry today. 

ZDNet has reached out to Lockheed Martin and we will update when we hear back.  

###  Previous and related coverage

* [Fingers point to Lazarus, Cobalt, FIN7 as key hacking groups attacking finance industry](https://www.zdnet.com/article/fingers-point-to-lazarus-cobalt-fin7-as-key-hacking-groups-focused-on-finance-industry/)
* [Lazarus hacking group now hides payloads in BMP image files](https://www.zdnet.com/article/lazarus-state-hacking-group-now-hides-payloads-in-bmp-image-files/)
* [Lazarus group strikes cryptocurrency firm through LinkedIn job adverts](https://www.zdnet.com/article/lazarus-group-strikes-cryptocurrency-firm-through-linkedin-job-adverts/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Threatactor:
[[threatactor.name=Cobalt Group]] [[threatactor.name=FIN7]] [[threatactor.name=Lazarus Group]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]] [[action.malware.name=WannaCry]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Bangladesh]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=South Korea]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Lockheed]] [[Phishing]] [[ZDNet]]

