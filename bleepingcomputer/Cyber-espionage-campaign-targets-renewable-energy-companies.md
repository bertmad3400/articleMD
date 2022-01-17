# Cyber espionage campaign targets renewable energy companies
### A large-scale cyber-espionage campaign targeting primarily renewable energy and industrial technology organizations have been discovered to be active since at least 2019, targeting over fifteen entities worldwide.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/cyber-espionage-campaign-targets-renewable-energy-companies/
+ Date: 2022-01-17T11:38:01-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/17/windmills.jpg)

![Wind Turbines](https://www.bleepstatic.com/content/hl-images/2022/01/17/windmills.jpg)


A large-scale cyber-espionage campaign targeting primarily renewable energy and industrial technology organizations have been discovered to be active since at least 2019, targeting over fifteen entities worldwide.


The campaign was discovered by security researcher [William Thomas](https://twitter.com/BushidoToken), a Curated Intelligence trust group member, who employed OSINT (open-source intelligence) techniques like DNS scans and public sandbox submissions.


Thomas' analysis revealed that the attacker uses a custom 'Mail Box' toolkit, an unsophisticated phishing package deployed on the actors' infrastructure, as well as legitimate websites compromised to host phishing pages.


Most of the phishing pages were hosted on "*.eu3[.]biz", "*.eu3[.]org", and "*.eu5[.]net" domains, while the majority of the compromised sites are located in Brazil ("*.com[.]br").


Targeting the renewable energy sector
-------------------------------------


The phishing campaign's goal is to steal the login credentials of those working for renewable energy firms, environmental protection organizations, and industrial technology in general.


Examples of organizations [targeted by the phishing attacks](http://blog.bushidotoken.net/2022/01/tracking-renewable-energy-intelligence.html) include:


* Schneider Electric
* Honeywell
* Huawei
* HiSilicon
* Telekom Romania
* University of Wisconsin
* California State University
* Utah State University
* Kardzhali Hydroelectric Power Station (Bulgaria)
* CEZ Electro (Bulgaria)
* California Air Resources Board
* Morris County Municipal Utilities Authority
* Taiwan Forestry Research Institute
* Carbon Disclosure Program
* Sorema (Italian recycling firm)


![Phishing sites set up for stealing employee credentials](https://www.bleepstatic.com/images/news/u/1220909/Phishing/enter_creds.png)**Phishing sites set up for stealing employee credentials**  
*Source: blog.bushidotoken.net*
The researcher couldn't retrieve any samples of the phishing emails used in the campaign, but Thomas believes the emails used a "Your Mail Box storage is full" lure based on the landing pages.


Unknown actor
-------------


Thomas couldn't attribute this campaign to any specific actors, but evidence points to two clusters of activity, one from APT28 (aka FancyBear) and one from Konni (North Korea actors).


Google Threat Analysis Group researchers have recently found phishing activity attributed to APT28, which uses several "eu3[.]biz" domains.



An overlap point for both groups is that the hostnames used for phishing credentials are owned by Zetta Hosting Solutions, a name that has appeared in many analyst reports recently.


"Konni" used Zetta Hosting Solution domains in [the Diplomat-targeting campaign](https://www.bleepingcomputer.com/news/security/hackers-take-over-diplomats-email-target-russian-deputy-minister/) uncovered by [Cluster25](https://cluster25.io/wp-content/uploads/2022/01/Konni_targeting_Russian_diplomatic_sector.pdf), and also in a T406 (Korean hackers) campaign analyzed by [Proofpoint](https://www.proofpoint.com/sites/default/files/threat-reports/pfpt-us-tr-threat-insight-paper-triple-threat-N-Korea-aligned-TA406-steals-scams-spies.pdf).


Thomas explained to BleepingComputer that many APT hacking groups use Zetta in malicious campaigns.



> 
> "Zetta is used a lot by APTs and malware, and I'd be very surprised if they didn't know. They're not a huge company. Threat actors also like these types of free hostname services where they can setup infrastructure quickly, freely, and anonymously." - Thomas.
> 
> 
> 


However, the researcher underlined that he doesn't have proof or concrete evidence that Zetta Hosting is knowingly helping malicious campaigns.


Focus on Bulgaria and potential motive
--------------------------------------


Apart from the two entities mentioned in the victimology section above, the researcher has noticed a small cluster of activity from 2019 linked to the same infrastructure targeting multiple Bulgarian banks.



![Phishing URLs targeting Bulgarian banks](https://www.bleepstatic.com/images/news/u/1220909/Phishing/bulgarian_banks.png)**Phishing URLs targeting Bulgarian banks**  
*Source: blog.bushidotoken.net*
The researcher believes that the adversary is financially supported by entities interested in fossil fuels, particularly someone selling energy to Bulgaria who sees [renewables](https://balkangreenenergynews.com/2-gw-of-renewable-energy-projects-apply-for-grid-connection-in-bulgaria/) as a threat.


The previous targeting of banks could be an attempt to gather intelligence on the [funding and construction](https://renewablesnow.com/news/axpo-bulgaria-preparing-pilot-ppas-seen-crucial-for-expanding-renewable-capacity-756525/) of new renewable energy facilities.


APT28 is a Russian group linked to the state, and Bulgaria is known to import [significant amounts of Russian natural gas](http://www.gazpromexport.ru/en/partners/bulgaria/), so the link between this campaign and the particular actors has a logical basis, even if it's not proven at this point.





## Tags:

#### Threatactor:
[[threatactor.name=APT28]] [[threatactor.name=APT28]] [[threatactor.name=Putter Panda]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Carbon]] [[action.malware.name=Elise]] [[action.malware.name=KONNI]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Construction]] [[victim.industry.name=Education]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Oman]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.country.name=Bulgaria]] [[victim.continent.name=Europe]] [[victim.country.name=Romania]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Brazil]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Phishing]] [[Zetta]] [[Apt28]] [[Bleeping Computer]]

