# WooCommerce Pricing Plugin Allows Malicious Code-Injection
### The popular Dynamic Pricing and Discounts plugin from Envato can be exploited by unauthenticated attackers.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169063)
+ Date: August 31, 2021  12:12 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/03/13163335/work-from-home-e1584131629686.jpg)
A pair of security vulnerabilities in the WooCommerce Dynamic Pricing and Discounts plugin from Envato could allow unauthenticated attackers to inject malicious code into websites running unpatched versions. This can result in a variety of attacks, including website redirections to phishing pages, insertion of malicious scripts on product pages and more.


The plugin, which has 19,700+ sales on Envato Market, offers [a variety of pricing and promotion tools](https://codecanyon.net/item/woocommerce-dynamic-pricing-discounts/7119279) for online retailers, including special offers, bulk pricing, tiered pricing, bundle pricing, deals of the day, flash sales, wholesale pricing, member pricing, individual pricing, loyalty programs, behavioral pricing, location-based pricing and so on. It also supports conditional price increase and extra fees.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

According to researchers at the Ninja Technologies Network, the two unauthenticated vulnerabilities affect version 2.4.1 and below. The first is a high-severity stored cross-site scripting (XSS) bug; the second is a medium-severity settings export problem.


The XSS bug exists in the \_\_construct method of the “wc-dynamic-pricing-and-discounts/classes/rp-wcdpd-settings.class.php” script, according to a [Tuesday writeup](https://blog.nintechnet.com/woocommerce-dynamic-pricing-and-discounts-plugin-fixed-multiple-vulnerabilities/) from NinTechNet.


“It lacks a capability check and a security nonce and thus is accessible to everyone, authenticated or not,” researchers explained. “An unauthenticated user can import the plugin’s settings. Because some fields aren’t sanitized, the attacker can inject JavaScript code into the imported JSON-encoded file.”


If successful, the code will be executed on every product page of the WooCommerce e-shop, they added. Additionally, attackers could replace JavaScript code with any HTML tags, such as a Meta Refresh tag, which could be used to redirect visitors and customers to a malicious website.


Also, the import function lacks a security nonce to prevent against cross-site request forgery (CSRF) attacks, where a user can submit unauthorized commands from a site that the web application trusts.


The second bug exists because a core export function lacks a capability check and is accessible to everyone, authenticated or not.


“An unauthenticated user can export the plugin’s settings, inject JavaSript code into the JSON file and reimport it using the previous vulnerability,” according to NinTechNet.


The issues are patched in version 2.4.2, though the CSRF check is still not fixed, researchers warned.


Users of WooCommerce, the popular e-commerce platform for WordPress, are [no strangers](https://threatpost.com/woocommerce-card-skimmer-malware/154699/) to having to patch security problems, and it’s important to keep on top of patching. Last month for instance WooCommerce [rushed emergency fixes](https://threatpost.com/zero-day-attacks-woocommerce-databases/167846/) for a critical SQL-injection security vulnerability in the core platform and a related plugin that had been under attack as a zero-day bug, for instance. The bug could allow unauthenticated cyberattackers to make off with scads of information from an online store’s database – anything from customer data and payment-card info to employee credentials.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[pricing,]] [[WooCommerce]] [[ThreatPost]]
