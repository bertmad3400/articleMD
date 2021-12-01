# 80K Retail WooCommerce Sites Exposed by Plugin XSS Bug
### The Variation Swatches plugin security flaw lets attackers with low-level permissions tweak important settings on e-commerce sites to inject malicious scripts.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176704)
+ Date: December 1, 2021  2:34 pm
+ Author: Becky Bracken


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/06/01131125/Bug-Digital.jpeg)
The plugin “Variation Swatches for WooCommerce,” installed across 80,000 WordPress-powered retail sites, contains a stored cross-site scripting (XSS) security vulnerability that could allow cyberattackers to inject malicious web scripts and take over sites.


Variation Swatches is designed to allow retailers using the WooCommerce platform for WordPress sites to show different versions of the same product, like a sweater in several colors. Unfortunately, vulnerable versions can also give users without administrative permissions — like customers or subscribers — access to the plugin’s settings, according to researchers from Wordfence.


“More specifically, the plugin registered the ‘tawcvs\_save\_settings,’ ‘update\_attribute\_type\_setting’ and ‘update\_product\_attr\_type’ functions, which were all hooked to various AJAX actions,” Wordfence’s Chloe Chamberland explained, in a [Wednesday posting](https://www.wordfence.com/blog/2021/12/xss-vulnerability-patched-in-plugin-designed-to-enhance-woocommerce/). “These three functions were all missing capability checks as well as nonce checks, which provide cross-site request forgery protection.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Giving low-permissioned users access to the “tawcvs\_save\_settings” function is particularly concerning, she said, because that access can be used to update the plugin’s settings and inject malicious web scripts that would execute whenever a site owner accessed the settings area of the plugin.


“As always, malicious web scripts can be crafted to inject new administrative user accounts or even modify a plugin or theme file to include a backdoor, which in turn would grant the attacker the ability to completely take over a site,” the researcher added.


The vulnerability (CVE-2021-42367) affected all users of the plugin until Nov. 23, when it was patched in [the new 2.1.2 version](https://wordpress.org/plugins/variation-swatches-for-woocommerce/).


**WordPress Users Plagued by Problems**
---------------------------------------


WordPress users are already grappling with cascading bugs, incidents and compromises. Last week for instance, GoDaddy, the world’s largest domain registrar, was breached — affecting 1.2 million customers along with various resellers of [GoDaddy Managed WordPress](https://threatpost.com/godaddy-breach-widens-reseller-subsidiaries/176575/).


In mid-Nov. another glitchy WordPress plugin let attackers display [a fake ransomware encryption message](https://threatpost.com/fake-ransomware-infection-wordpress/176410/) demanding about $6,000 to unlock the site. The threat was empty, all the users needed to do was delete the plugin, but had the attackers deployed actual ransomware the outcome could have been catastrophic.


And in late October, a [WordPress plugin bug](https://threatpost.com/wordpress-plugin-bug-wipe-sites/175826/) was discovered in the Hashthemes Demo Importer offering, that allowed users with simple subscriber permissions to wipe sites of all content.


To mitigate this latest plugin bug, Chamberland recommends  that users update their sites with the patched version of the Variation Swatches for WooCommerce.


***There’s a sea of unstructured data on the internet relating to the latest security threats.***[***REGISTER TODAY***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This***[***LIVE, interactive Threatpost Town Hall***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***, sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)**for the LIVE event!**


 




#### Tags:
[[plugin]] [[WordPress]] [[ThreatPost]]
