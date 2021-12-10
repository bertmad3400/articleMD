# Sprawling Active Attack Aims to Take Over 1.6M WordPress Sites
### Cyberattackers are targeting security vulnerabilities in four plugins plus Epsilon themes, to assign themselves administrative accounts.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176933
+ Date: 2021-12-10 16:19:44+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2019/01/28092447/wordpress_plugin_vuln.jpg)

An active attack against more than 1.6 million WordPress sites is underway, with researchers spotting tens of millions of attempts to exploit four different plugins and several Epsilon Framework themes.


The goal, they said, is complete site takeover using administrative privileges.


The scope of the campaign in notable: The activity is coming from more than 16,000 different IP addresses, according to a Wordfence analysis. There were 13.7 million attacks in the first 36 hours.


**Problematic Plugins**
-----------------------


Researchers said that the attackers are aiming to exploit critical “unauthenticated arbitrary options update vulnerabilities” in the following plugins: ​​Kiwi Social Share (patched in 2018), and WordPress Automatic, Pinterest Automatic and PublishPress Capabilities (all patched this year).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“In most cases, the attackers are updating the ‘users\_can\_register’ option to enabled and setting the ‘default\_role’ option to `administrator,'” Wordfence researchers noted in a [Thursday analysis](https://www.wordfence.com/blog/2021/12/massive-wordpress-attack-campaign/). “This makes it possible for attackers to register on any site as an administrator, effectively taking over the site.”


The activity started in earnest on Dec. 8, according to Wordfence – possibly as the result of attackers becoming interested in arbitrary options update bugs in general after the PublishPress Capabilities  plugin was patched on Dec. 6.


Some of these have been exploited before. The Ninja Technologies Network, for instance, flagged a spike in activity specifically against the Kiwi Social Share bug in 2018, starting Dec. 6, shortly after it was patched.


“WordPress Kiwi Social Sharing plugin <2.0.11 is currently exploited since Dec. 6,” the firm said in a [short alert](https://blog.nintechnet.com/critical-vulnerability-in-wordpress-kiwi-social-sharing-plugin-actively-exploited/) at the time. “It allows attackers to modify the WordPress wp\_options table in order to create administrator accounts or, for instance, redirect the blog to another website.”


Affected versions are as follows:


* **[Kiwi Social Plugin](https://wordpress.org/plugins/kiwi-social-share/) <= 2.0.10** – Adds functionality to let site visitors share content on social media. 10,000+ installations.
* **[PublishPress Capabilities](https://wordpress.org/plugins/capability-manager-enhanced/) <= 2.3** – Allows admins to customize permissions for WordPress user roles, from administrators and editors to authors, contributors, subscribers and custom roles. 100,000+ installations.
* **[Pinterest Automatic](https://codecanyon.net/item/pinterest-automatic-pin-wordpress-plugin/2203314)** **<= 4.14.3** – Pins images from posts automatically to Pinterest.com. 7,400+ sales.
* **[WordPress Automatic](https://codecanyon.net/item/wordpress-automatic-plugin/1904470) <= 3.53.2** – Imports content to WordPress automatically. 28,000+ sales.


**Epic Epsilon**
----------------


The attackers are also targeting a function-injection vulnerability present in various Epsilon Framework themes, researchers said, which allows for remote code execution (RCE). Epsilon themes allow site builders to choose different flexible design elements to craft the way a website looks and is organized.


The affected themes (collectively installed on 150,000+ sites) are:


[Activello](https://wordpress.org/themes/activello/) <=1.4.0  

[Affluent](https://wordpress.org/themes/affluent/) <1.1.0  

[Allegiant](https://wordpress.org/themes/allegiant/) <=1.2.2  

[Antreas](https://wordpress.org/themes/antreas/) <=1.0.2  

[Bonkers](https://wordpress.org/themes/bonkers/) <=1.0.4  

[Brilliance](https://wordpress.org/themes/brilliance/) <=1.2.7  

[Illdy](https://wordpress.org/themes/illdy/) <=2.1.4  

[MedZone Lite](https://wordpress.org/themes/medzone-lite/) <=1.2.4  

NatureMag Lite – no patch, users should uninstall  

[NewsMag](https://wordpress.org/themes/newsmag/) <=2.4.1  

[Newspaper X](https://wordpress.org/themes/newspaper-x/) <=1.3.1  

[Pixova Lite](https://wordpress.org/themes/pixova-lite/) <=2.0.5  

[Regina Lite](https://wordpress.org/themes/regina-lite/) <=2.0.4  

[Shapely](https://wordpress.org/themes/shapely/) <=1.2.7  

[Transcend](https://wordpress.org/themes/transcend/) <=1.1.8


These same themes have anchored large-scale attacks before. In November 2020, Wordfence observed an operation that targeted this list with “probing attacks,” meant to test whether sites were unpatched and vulnerable. [That involved](https://www.wordfence.com/blog/2020/11/large-scale-attacks-target-epsilon-framework-themes/) 7.5 million attacks against more than 1.5 million websites, coming from more than 18,000 IP addresses.


This time, the attackers are attempting to again update arbitrary options in order to take over a site by creating an administrator account, researchers said.


**Time to Patch**
-----------------


“Due to the severity of these vulnerabilities and the massive campaign targeting them, it is incredibly important to ensure your site is protected from compromise,” according to Wordfence. “We strongly recommend ensuring that any sites running one of these plugins or themes has been updated to the patched version…Simply updating the plugins and themes will ensure that your site stays safe from compromise against any exploits targeting these vulnerabilities.”


To determine if a website has been compromised, admins can review the user accounts on the site to determine if there are any that are unauthorized, researchers recommended.


“If the site is running a vulnerable version of any of the four plugins or various themes, and there is a rogue user account present, then the site was likely compromised via one of these plugins,” they explained. “Please remove any detected user accounts immediately.”


Admins should also go to the http://examplesite[.]com/wp-admin/options-general.php page, and should ensure that the “Membership” setting and the “New User Default Role” are both correctly set, they said.


With WordPress powering [more than 30 percent](https://techjury.net/blog/percentage-of-wordpress-websites/#gref) of websites globally (455 million sites in total), the platform and third-party plugins will continue to be an attractive target for cyberattackers, especially as plugin bugs are not uncommon. For instance, in October [researchers discovered](https://threatpost.com/wordpress-plugin-bug-wipe-sites/175826/) a high-severity vulnerability in the Hashthemes Demo Importer plugin that allows subscribers to wipe sites clean of content.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***for the LIVE event!***





## Tags:

#### Action:
[[action.malware.name=Anchor]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Epic]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Regin]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Wordpress]] [[Plugins]] [[Wordfence]] [[Plugin]] [[Publishpress]] [[ThreatPost]]
#### urls
http://examplesite.com/wp-admin/options-general.php

