# Adobe urges customers to upgrade after 500 stores breached through Magento platform | ZDNet
### Adobe ended support for the Magento 1 e-commerce platform in 2020 but hundreds of companies still use it.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/adobe-urges-customers-to-upgrade-after-500-stores-breached-through-magento-platform/
+ Date: 2022-02-10 17:55:51
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/cc4b2f0e6fefef4225f672d4714c5708d4f03cb2/2021/10/13/96368351-25fc-4a59-ade3-059e8eb15a54/e-commerce.jpg?width=770&height=578&fit=crop&auto=webp)

Adobe urged customers using the Magento 1 e-commerce platform to upgrade to the latest version of Adobe Commerce after security company Sansec [detected a mass breach](https://sansec.io/research/naturalfreshmall-mass-hack) of over 500 stores running the platform.

In a statement to ZDNet, Adobe said it ended support for Magento 1 on June 30, 2020. 

"We continue to encourage merchants to [upgrade](https://devdocs.magento.com/guides/v2.4/extension-dev-guide/versioning/check-version.html) to the latest version of Adobe Commerce for the most up-to-date security, flexibility, extensibility, and scalability," an Adobe spokesperson said. 

"At a minimum, we recommend Magento Open Source merchants on Magento 1 to upgrade to the latest version of Magento Open Source (built on Magento 2), to which Adobe contributes key security updates."

On Tuesday, Sansec released a report showing that hundreds of stores were the victim of a payment skimmer loaded from the naturalfreshmall.com domain. 




> More than 350 ecommerce stores infected with malware in a single day.  
>   
> Today our global crawler discovered 374 ecommerce stores infected with the same strain of malware. 370 of these stores load the malware via https://naturalfreshmall[.]com/image/pixel[.]js.
> 
> — Sansec (@sansecio) [January 25, 2022](https://twitter.com/sansecio/status/1486000220647444491?ref_src=twsrc%5Etfw)




 window.ZdnetFunctions.logWithLabel('%c One Trust ', "Service loaded: script\_twitterwidgets with class optanon-category-5");
 
"We invited victims to reach out to us, so we could find a common point of entry and protect other merchants against a potential new attack. The first investigation is now completed: attackers used a clever combination of an *SQL injection* (SQLi) and *PHP Object Injection* (POI) attack to gain control of the Magento store," the researchers explained. 

"Attackers abused a (known) leak in the Quickview plugin. While this is typically abused to inject rogue Magento admin users, in this case the attacker used the flaw to run code directly on the server."






In their examination of one attack, they found the threat actor left 19 backdoors on the system. They recommended victims use a malware scanner to identify all of the instances of malicious files or Magento code that had malicious code added to them.

Sansec noted that even though Adobe has ended support for Magento, thousands of businesses still use it. 

Magento has long been a source of issues for Adobe and the online merchants who use it. [In November](https://www.zdnet.com/article/hackers-targeted-thousands-of-online-retailers-to-steal-credit-card-details/), the [National Cyber Security Centre](https://www.ncsc.gov.uk/news/guidance-for-retailers-to-prevent-websites-becoming-black-friday-cyber-traps) (NCSC) identified a total of 4,151 retailers that had been compromised by hackers attempting to exploit vulnerabilities on checkout pages to divert payments and steal details. 

The majority of the online shops that cybercriminals exploited for payment-skimming attacks were compromised by [known vulnerabilities in the e-commerce platform Magento](https://www.zdnet.com/article/adobe-patches-magento-bugs-that-lead-to-code-execution-customer-list-tampering/). In February 2021, Magento [received](https://www.zdnet.com/article/adobe-patches-wave-of-critical-bugs-in-magento-acrobat-reader/) a slew of [security fixes](https://helpx.adobe.com/security/products/magento/apsb21-08.html) from Adobe. Specifically, Magento Commerce and Magento Open Source on all platforms were subject to a total of 18 bugs, varying in severity from critical to moderate. 

More than 2,000 Magento online stores [were hacked](https://www.zdnet.com/article/magento-online-stores-hacked-in-largest-campaign-to-date/) in September 2020, attacks that were also spotted by Sansec at the time. Attacks against sites running the now-deprecated Magento 1.x software [were anticipated](https://www.zdnet.com/article/between-200000-and-240000-magento-online-stores-will-reach-eol-next-year/) by Adobe, which issued the [first alert in November 2019](https://www.zdnet.com/article/adobe-discloses-security-breach-impacting-magento-marketplace-users/) about store owners needing to update to the 2.x branch.

Adobe's initial warning about impending attacks on Magento 1.x stores was later echoed in similar [security advisories issued by Mastercard and Visa](https://www.zdnet.com/article/adobe-mastercard-visa-warn-online-store-owners-of-magento-1-x-eol/).

Even the FBI [warned in 2020](https://www.zdnet.com/article/fbi-warns-about-attacks-on-magento-online-stores-via-old-plugin-vulnerability/) that hackers were exploiting a three-year-old vulnerability in a Magento plugin to take over online stores and plant a malicious script that records and steals buyers' payment card data.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=CHOPSTICK]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]] [[victim.industry.name=Retail]] [[victim.industry.name=Retail]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Magento]] [[Sansec]] [[Malware]] [[ZDNet]]
#### urls
https://naturalfreshmall.com/image/pixel.js.—

