# Zero-Day Attacks on Critical WooCommerce Bug Threaten Databases
### The popular e-commerce platform for WordPress has started deploying emergency patches.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167846)
+ Date: July 15, 2021  4:50 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/15163744/woocommerce.jpg)
A critical SQL-injection security vulnerability in the WooCommerce e-commerce platform and a related plugin has been under attack as a zero-day bug, researchers have disclosed.


The exploitation prompted WooCommerce to release an emergency patch for the issue late on Wednesday. The bug could allow unauthenticated cyberattackers to make off with scads of information from an online store’s database – anything from customer data and payment-card info to employee credentials.


WooCommerce, a popular open-source e-commerce platform for websites running on WordPress, [is installed on](https://wordpress.org/plugins/woocommerce/) more than 5 million websites globally. It allows online merchants to create storefronts with various customizable options such as payment types accepted, shipping features, sales tax calculations and so on.



The related plugin affected by the bug is the WooCommerce Blocks feature, which is [installed on](https://wordpress.org/plugins/woo-gutenberg-products-block/) more than 200,000 sites. It helps merchants display their products on webpages.


The bug (CVE pending) was [originally reported](https://twitter.com/thedawgyg/status/1415479999705096194) by HackerOne security researcher Thomas DeVoss (dawgyg), who said via Twitter that he was able to pull together a working proof-of-concept exploit, but that he wouldn’t release details of the bug until after there’s been time for merchants to apply the patch.


So, technical details are scant apart from the fact that it allows SQL injection – a type of attack that allows a cyberattacker to interfere with the queries that an application makes to its database. Usually this is carried out by inserting malicious SQL statements into an entry field for execution.


**Exploitation in the Wild**
----------------------------


The extent of in-the-wild exploitation remains somewhat unclear.


“Our investigation into this vulnerability and whether data has been compromised is ongoing,” Beau Lebens, head of engineering for WooCommerce, said in [an advisory](https://woocommerce.com/posts/critical-vulnerability-detected-july-2021/). “We will be sharing more information with site owners on how to investigate this security vulnerability on their site…If a store was affected, the exposed information will be specific to what that site is storing but could include order, customer, and administrative information.”


[According to](https://www.wordfence.com/blog/2021/07/critical-sql-injection-vulnerability-patched-in-woocommerce/) researchers at Wordfence, there is “extremely limited evidence of [exploitation] attempts and it is likely that such attempts were highly targeted.”


That said, one user noted in the comments section of the WooCommerce advisory that unusual activity had been observed.


“Just hours before your announcement and email, the site I manage saw a massive spike in network traffic before effectively locking out administrative logins and presenting various bizarre messages,” the user said. “When I SSH’d into the live environment, the console reported that there were 4 failed login attempts since my last login. So far as I could tell there was no apparent vandalism and the failed logins had their IP banned. It seems a little too coincidental.”


To forensically determine if a site has been impacted, Wordfence researchers suggested that a review of log files may show indications:


“Look for a large number of repeated requests to /wp-json/wc/store/products/collection-data or ?rest\_route=/wc/store/products/collection-data in your log files,” they noted. “Query strings which include %2525 are an indicator that this vulnerability may have been exploited on your site.”


The vulnerability affects versions 3.3 to 5.5 of the WooCommerce plugin and WooCommerce Blocks 2.5 to 5.5 plugin. Lebens said that the company has created a patch fix “for every impacted version (90+ releases) which was deployed automatically to vulnerable stores.”


However, that automatic deployment is not instantaneous, and users in the advisory’s comments section were reporting not getting the updates as of Thursday afternoon, so “we’re urging everyone check and manually update if needed just in case,” WooCommerce said. The advisory includes a table listing all 90 patched versions.


“Store owners using older versions can update to the latest version in their branch,” advised Wordfence researchers. “For example, if your storefront is using WooCommerce version 5.3, you can update to version 5.3.1 to minimize the risk of compatibility issues.”


WooCommerce is also recommending administrative password resets after updating to provide additional protection.


The open-source platform is no stranger to security bugs: Last fall, it patched two high-severity cross-site scripting flaws, in [a process that took](https://threatpost.com/woocommerce-plugin-bug-allows-site-takeover/159364/) three bites at the apple to get the fix right.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[WooCommerce]] [[plugin]] [[Wordfence]] [[3]] [[5]] [[ThreatPost]]
