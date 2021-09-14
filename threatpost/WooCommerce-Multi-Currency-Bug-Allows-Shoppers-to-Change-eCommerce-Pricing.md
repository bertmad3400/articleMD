# WooCommerce Multi Currency Bug Allows Shoppers to Change eCommerce Pricing
### The security vulnerability can be exploited with a malicious CSV file.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169394)
+ Date: September 13, 2021  2:08 pm
+ Author: Tara Seals


## Article:
![magecart web skimmer](https://media.threatpost.com/wp-content/uploads/sites/103/2018/12/19142200/Click2Gov.jpeg)
A security vulnerability in the WooCommerce Multi Currency plugin could allow any customer to change the pricing for products in online stores.


WooCommerce is a popular eCommerce plugin for WordPress-powered websites; the Multi Currency plugin [allows e-tailers to set pricing](https://woocommerce.com/products/multi-currency/) for international shoppers; the plugin automatically detects a customer’s geolocation and displays pricing in the customer country’s currency, with the exchange rate set manually or automatically using current exchange rates. It has 7,700 sales on the Envato Marketplace.


According to the Ninja Technologies Network (NinTechNet), the issue is a broken access-control vulnerability in version 2.1.17 and below, impacting Multi Currency’s “Import Fixed Price” feature, which allows eCommerce sites to set custom prices, thus overwriting any prices calculated automatically by exchange rate.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“The import function, import\_csv(), is loaded by the wmc\_bulk\_fixed\_price AJAX hook in the “woocommerce-multi-currency/includes/import-export/import-csv.php” script,” according to a NinTechNet [analysis](https://blog.nintechnet.com/vulnerability-fixed-in-wordpress-woocommerce-multi-currency-plugin/) on Monday. “The function lacks a capability check and a security nonce, and therefore is accessible to all authenticated users, which includes WooCommerce customers.”


To exploit the problem, cyberattackers could upload a specially crafted [CSV file](https://www.bigcommerce.com/ecommerce-answers/what-csv-file-and-what-does-it-mean-my-ecommerce-business/) to the site, which uses a product’s current currency and the product ID. This allows them to change the price of one or multiple products, researchers explained.


“The vulnerability is particularly damaging for online shops selling digital goods because the attacker will have time to download the goods,” they said. “It is important to verify every order because the hack doesn’t change the product’s price in the backend, hence the shop manager may unlikely notice it immediately.”


To avoid becoming impacted, website admins should update to the latest version of the plugin, v. 2.1.18, which contains a patch.


WooCommerce users continue to face patching requirements lately. In late August, a pair of security vulnerabilities in the WooCommerce Dynamic Pricing and Discounts plugin from Envato [were disclosed](https://threatpost.com/woocommerce-plugin-malicious/169063/), which could allow unauthenticated attackers inject malicious code into websites running unpatched versions. This can result in a variety of attacks, including website redirections to phishing pages, insertion of malicious scripts on product pages and more.


And in July, a critical SQL-injection security vulnerability in the WooCommerce e-commerce platform and a related plugin [was found to be](https://threatpost.com/zero-day-attacks-woocommerce-databases/167846/) under attack as a zero-day bug. The exploitation prompted WooCommerce to release an emergency patch for the issue, which could allow unauthenticated cyberattackers to make off with scads of information from an online store’s database – anything from customer data and payment-card info to employee credentials.


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[WooCommerce]] [[plugin]] [[“The]] [[ThreatPost]]
