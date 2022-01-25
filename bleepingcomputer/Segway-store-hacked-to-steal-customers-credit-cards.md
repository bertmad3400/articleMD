# Segway store hacked to steal customers' credit cards
### Segway's online store was compromised to include a malicious Magecart script that potentially allowed threat actors to steal credit cards and customer information during checkout.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/segway-store-hacked-to-steal-customers-credit-cards/
+ Date: 2022-01-25T09:59:33-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/25/segway.jpg)

![segway](https://www.bleepstatic.com/content/hl-images/2022/01/25/segway.jpg?rand=873755438)


Segway's online store was compromised to include a malicious Magecart script that potentially allowed threat actors to steal credit cards and customer information during checkout.


Segway is the maker of the iconic two-wheeled self-balancing personal transporters and a range of [other types](https://www.bleepingcomputer.com/news/security/security-flaws-are-everywhere-even-in-segway-hoverboards/) of human transportation devices.


These personal vehicles are typically used by security personnel in patrols, tourists in city tours, golfers, in various logistic applications, and for short-distance leisure rides.


Malicious favicons load malicious scripts
-----------------------------------------


MageCart attacks are when threat actors compromise a site to introduce malicious scripts that steal credit card and customer information when people make a purchase.


However, security software has gotten better over the past few years at detecting these malicious scripts, forcing threat actors to develop better ways to hide them.


One such way is to embed the malicious credit card skimmer in normally innocuous favicon files, image files used to display a small icon (usually the site's logo) in a web page's tab.


According to a report by [Malwarebytes Labs](https://blog.malwarebytes.com/threat-intelligence/2022/01/segway-store-compromised-with-magecart-skimmer/), threat actors added JavaScript to Segway's online store (store.segway.com) that pretended to display the site's copyright. In reality, the script loaded an external favicon that contained the malicious credit card stealing script.



![The external URL used for loading the remote resource](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/skimmer-url.jpg)**The external URL used for loading the malicious favicon**  
*Source: Malwarebytes*
While this malicious favicon file does contain an image and is properly displayed by the browser, it also included the credit card skimmer script used to steal payment information. However, this script won't be seen unless you analyze it using a hex editor, as shown below.



![Skimmer loading function embedded in the favicon](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/skimmer-icon.png)**Skimmer loading function embedded in the favicon**  
*Source: Malwarebytes*
This technique has been [well-documented](https://www.bleepingcomputer.com/news/security/hackers-abuse-lookalike-domains-and-favicons-for-credit-card-theft/) and employed by skillful Magecart groups [since 2020](https://www.bleepingcomputer.com/news/security/hackers-hide-credit-card-stealing-scripts-in-favicon-exif-data/) to compromise the websites of [Claire's](https://www.bleepingcomputer.com/news/security/accessories-giant-claires-hacked-to-steal-credit-card-info/), [Tupperware](https://www.bleepingcomputer.com/news/security/tupperware-site-hacked-with-fake-form-to-steal-credit-cards/), [Smith & Wesson](https://www.bleepingcomputer.com/news/security/smith-and-wesson-web-site-hacked-to-steal-customer-payment-info/), [Macy's](https://www.bleepingcomputer.com/news/security/macys-customer-payment-info-stolen-in-magecart-data-breach/), and [British Airways](https://www.bleepingcomputer.com/news/security/british-airways-fell-victim-to-card-scraping-attack/).


Magecart Group 12
-----------------


Malwarebytes says the attackers responsible for the compromise are part of the [Magecart Group 12](https://www.bleepingcomputer.com/news/security/magecart-group-12-targets-opencart-websites/) group, a financially motivated collective that has been stealing credit card details since [at least 2019](https://www.bleepingcomputer.com/news/security/magecart-skimmer-hits-hundreds-of-sites-in-ad-supply-chain-attack/).


The researchers say the malicious code has been active on Segway's website since at least January 6, 2021, and that they contacted the company to inform them of the attack.


BleepingComputer has confirmed that at the time of writing this, the malicious code is [still present on the site](https://web.archive.org/web/20220121053034/https://store.segway.com/) and is blocked by numerous security products.



![ESET blocking access to Segway's online store](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**ESET blocking access to Segway's online store**
Malwarebytes' analysts believe that the Magecart actors exploited a vulnerability in the Magento CMS used by the store or in one of its plugins to inject their malicious code.


The telemetry data shows that most customers of the Segway store come from the United States (55%), while Australia follows at second place with a significant 39%.


BleepingComputer has contacted Segway to learn more about this attack but did not receive a response at this time.


How to stay safe
----------------


The Segway store compromise is yet another example of how threat actors can target even the sites of renowned brands with a long history of trustworthiness.


Consumers should pay with electronic methods, one-time cards, cards with strict charging limits, or simply choose cash on delivery if possible to avoid these types of attacks.


Additionally, using an internet security tool that detects and stops malicious JavaScript from loading on checkout pages could save you the trouble of having your credit card details stolen.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Segway]] [[Magecart]] [[Malwarebytes]] [[Favicon]] [[Bleeping Computer]]

