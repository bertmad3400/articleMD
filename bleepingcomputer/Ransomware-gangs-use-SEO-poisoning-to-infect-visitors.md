# Ransomware gangs use SEO poisoning to infect visitors
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/ransomware-gangs-use-seo-poisoning-to-infect-visitors/)
+ Date: October 28, 2021
+ Author: Bill Toulas


## Article:
![poison](https://www.bleepstatic.com/content/hl-images/2021/10/28/poison.jpg?rand=1502450743)


Researchers have spotted two campaigns linked to either the REvil ransomware gang or the SolarMarker backdoor that use SEO poisoning to serve payloads to targets.


SEO poisoning, also known as "search poisoning," is an attack method that relies on optimizing websites using 'black hat' SEO techniques to rank higher in Google search results.


Due to their high ranking, victims who land on these sites believe they are legitimate, and actors enjoy a heavy influx of visitors who look for specific keywords.


SEO for ransomware
------------------


According to the findings of the [Menlo Security](https://www.menlosecurity.com/blog/holy-seo-poisoning/) team, SEO poisoning by malware distributors is on the rise, with two notable examples being the Gootloader and SolarMarket campaigns.


The actors inject sites with keywords that cover over 2,000 unique search terms, including "sports mental toughness," "industrial hygiene walk-through," "five levels of professional development evaluation," and more.


The optimized sites appear in search results as PDFs that, when visited, prompt a user to download the document, as shown below.



![blue-jacket-of-the-quarter-write-up-examples](https://www.bleepstatic.com/images/news/security/seo-site.jpg)​**Malicious site prompting a visitor to download a PDF document**  
*Source: Menlo Security*
When they click on the download button, the users are redirected through a series of sites that ultimately drop a malicious payload.


The threat actors use these redirects to prevent their sites from being removed from the search results for hosting malicious content.


In these particular campaigns, the threat actors were either dropping REvil via Gootloader or the SolarMarker backdoor.


Exploiting a WordPress plugin vulnerability
-------------------------------------------


In the two campaigns spotted by the researchers, the actors didn't create their own malicious sites but instead hacked legitimate WordPress sites that already had a good Google search ranking.


The sites were hacked by abusing an undisclosed flaw in the 'Formidable Forms' WordPress plugin, which the hackers used to upload laced PDF into the '/wp-content/uploads/formidable/' folder.


If you are using this particular plugin, upgrading to version 5.0.10 or later is advisable, even though 5.0.07 was the most recent version spotted in the compromised set.


The industry verticals for the types of sites compromised in this campaign are shown in the chart below.


 



![Types of sites compromised with laced PDF files](https://www.bleepstatic.com/images/news/u/1220909/Security/types%20of%20sites.jpg)**Types of sites compromised with laced PDF files**  

Source: Menlo Security
As you can see from the image above, the attackers heavily targeted sites in the business category, likely because they commonly host PDFs in the form of guides and reports.


Spreading a wider net
---------------------


When modern encrypting ransomware first launched in 2012, threat actors would spread a wide net in their attacks in the hopes of infecting as many people as possible.


As ransomware gangs are now targeting high value companies for multi-million dollar payouts, this spray and pray approach is not seen as often as you likely will infect consumers who would not be willing to pay large ransoms.


However, BleepingComputer knows of one REvil affiliate who performed wide-scale attacks to infect consumers and small businesses alike.


Instead of demanding hundreds, if not millions of dollars as ransoms, this affiliate would demand between $1,500 and $7,500.


While it is not known if this affiliate utilized SEO poisoning attacks, this type of attack would have fit their model of indiscriminately targeting any kind of victims.




#### Tags:
[[SEO]] [[ransomware]] [[REvil]] [[Menlo]] [[PDF]] [[WordPress]] [[Bleeping Computer]]
