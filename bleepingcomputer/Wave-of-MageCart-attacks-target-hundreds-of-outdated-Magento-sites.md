# Wave of MageCart attacks target hundreds of outdated Magento sites
### Analysts have found the source of a mass breach of over 500 e-commerce stores running the Magento 1 platform and involves a single domain loading a credit card skimmer on all of them.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/wave-of-magecart-attacks-target-hundreds-of-outdated-magento-sites/
+ Date: 2022-02-09T13:24:08-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/15/credit-card.jpg)

![cart](https://www.bleepstatic.com/content/hl-images/2022/02/03/e-commerce.jpg?rand=186696954)


Analysts have found the source of a mass breach of over 500 e-commerce stores running the Magento 1 platform and involves a single domain loading a credit card skimmer on all of them.


According to Sansec, the attack became evident late last month when their crawler discovered 374 infections on the same day, all using the same malware.


The domain from where threat actors loaded the malware is naturalfreshmall[.]com, currently offline, and the goal of the threat actors was to steal the credit card information of customers on the targeted online stores.


Planting backdoors
------------------


Sansec's subsequent investigation unveiled that the attackers abused a known vulnerability in the Quickview plugin to inject rogue Magento admin users that could then run code with the highest privileges.


The abuse happens via adding a validation rule into the `customer_eav_attribute` table. This tricks the host app into crafting a malicious object, which is then used to create a simple backdoor (api\_1.php).


The validation rules for new customers are the clever part of the attack, as this triggers the payload to be injected into the sign-up page.



![Added rule in the website's database](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/added-rule.png)**Added rule in the website's database.**  
*Source: Sansec*
In addition to injecting the credit card skimmer, the hackers can also use the api\_1.php backdoor to execute commands on the remote server, leading to a complete site takeover.


In practice, though, siphoning payment details using MageCart atttacks (skimmers) is more beneficial to the threat actors; that's why this particular wave of attacks focused on doing precisely that.


Sansec points out that in an extreme case, the adversaries injected as many as 19 backdoors on a single e-commerce platform, possibly experimenting to figure out what works best for their purpose or just being very serious about its redundancy.



Magento 1 is still in use
-------------------------


Adobe has stopped supporting the Magento 1 branch of the popular e-commerce platform since June 30, 2020, but thousands of sites are still using the outdated software.


This makes the sites vulnerable to a wide range of hacker attacks, and by extension, puts the sensitive details of their customers at risk.


These details typically include credit card numbers, shipping addresses, names, phone numbers, email addresses, and generally all that's needed for placing an online order.


It is strongly recommended that all Magento admins [confirm they are using the latest version](https://devdocs.magento.com/guides/v2.4/extension-dev-guide/versioning/check-version.html) of the platform and upgrade if using older unsupported versions.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Magento]] [[Sansec]] [[E-commerce]] [[Bleeping Computer]]
