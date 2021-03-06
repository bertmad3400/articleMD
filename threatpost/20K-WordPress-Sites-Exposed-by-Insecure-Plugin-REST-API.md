# 20K WordPress Sites Exposed by Insecure Plugin REST-API
### The WordPress WP HTML Mail plugin for personalized emails is vulnerable to code injection and phishing due to XSS.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177866
+ Date: 2022-01-21T18:19:37+00:00
+ Author: Becky Bracken


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2019/04/23131246/WordPress-plugin-exploit.jpg)

More than 20,000 WordPress sites are vulnerable to malicious code injection, phishing scams and more as the result of a high-severity cross-site scripting (XSS) bug discovered in the WordPress Email Template Designer – WP HTML Mail, a plugin for designing custom emails.


The new vulnerability (CVE-2022-0218, CVSS score 8.3) was found by Wordfence researcher Chloe Chamberland, and was caused by a [faulty configuration in the REST-API routes](https://www.wordfence.com/blog/2022/01/unauthenticated-xss-vulnerability-patched-in-html-email-template-designer-plugin/) used to update the template and change settings, Chamberland explained in the disclosure.[![Password Management Webinar](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/12124026/specops_300x250_watch.jpg)](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/) Simply put, there was no authentication required to access the REST-API endpoint.


“Therefore, any user had access to execute the REST-API endpoint to save the email’s theme settings or retrieve the email’s theme settings,” Chamberland wrote. “[They] could inject malicious JavaScript into the mail template that would execute anytime a site administrator accessed the HTML mail editor.”


 


That means threat actors could add new users with administrative credentials, inject backdoors, implement site redirects, and use legitimate site templates to send phishing emails, among many other things — even site takeovers.


“Combined with the fact that the vulnerability can be exploited by attackers with no privileges on a vulnerable site, this means that there is a high chance that unauthenticated attackers could gain administrative user access on sites running the vulnerable version of the plugin when successfully exploited,” Chamberland said.


**Plugin Compatible with WooCommerce, Ninja Forms & Buddy Press**
-----------------------------------------------------------------


The plugin is installed across 20,000 sites and is compatible with other plugins run by WordPress sites with large followings like eCommerce platform [WooCommerce](https://threatpost.com/woocommerce-plugin-malicious/169063/), online form builder Ninja Forms and community builder plugin BuddyPress, Chamberland reported.


“We recommend that WordPress site owners immediately verify that their site has been updated to the latest patched version available, which is version 3.1 at the time of this publication,” Chamberland added.


This latest disclosure comes just a week after Risk Based Security released their findings that the number of [WordPress plugin vulnerabilities](https://threatpost.com/wordpress-bugs-exploded-2021-exploitable/177553/) exploded by triple digits in 2021.


In the same week, three [WordPress plugins](https://threatpost.com/plugins-vulnerability-84k-wordpress-sites/177654/) were reported with the same bug — exposing 84,000 sites running eCommerce add-ons to full site takeovers.


WordPress site administrators are advised by Chamberland to ensure they’re running the most up-to-date version, [WordPress Email Template Designer — WP HTML Mail](https://wordpress.org/plugins/wp-html-mail/) version 3.1.


“If you know a friend or colleague who is using this plugin on their site, we highly recommend forwarding this advisory to them to help keep their sites protected as this is a serious vulnerability that can lead to complete site takeover,” Chamberland cautioned.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Wordpress]] [[Chamberland]] [[Plugin]] [[Html]] [[Rest-api]] [[ThreatPost]]
#### CVE's
[[CVE-2022-0218]]

