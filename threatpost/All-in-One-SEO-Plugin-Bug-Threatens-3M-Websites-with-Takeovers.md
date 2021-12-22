# All in One SEO Plugin Bug Threatens 3M Websites with Takeovers
### A critical privilege-escalation vulnerability could lead to backdoors for admin access nesting in web servers.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177240
+ Date: 2021-12-22T18:24:07+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2019/01/28092447/wordpress_plugin_vuln.jpg)

A popular WordPress SEO-optimization plugin, called [All in One SEO](https://wordpress.org/plugins/all-in-one-seo-pack/), has a pair of security vulnerabilities that, when combined into an exploit chain, could leave website owners open to site takeover. The plugin is used by [more than 3 million](https://wordpress.org/plugins/all-in-one-seo-pack/) websites.


An attacker with an account with the site – such as a subscriber, shopping account holder or member – can take advantage of the holes, which are a privilege-escalation bug and an SQL-injection problem, according to researchers at Sucuri.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“WordPress websites by default allow any user on the web to create an account,” researchers said in [a posting](https://blog.sucuri.net/2021/12/critical-vulnerabilities-in-all-in-one-seo-plugin-affects-millions-of-wordpress-websites.html) on Wednesday. “By default, new accounts are ranked as subscriber and do not have any privileges other than writing comments. However, certain vulnerabilities, such as the ones just discovered, allow these subscriber users to have vastly more privileges than they were intended to have.”


 


The pair is ripe for easy exploitation, according to Sucuri, so users should upgrade to the patched version, v. 4.1.5.3. Security researcher at Automattic Marc Montpas was credited with finding the bugs.


**Privilege Escalation and SQL Injection**
------------------------------------------


The more severe issue out of the two bugs is the privilege-escalation problem, which affects versions 4.0.0 and 4.1.5.2 of All in One SEO. It carries a critical rating of 9.9 out of 10 on the CVSS vulnerability-severity scale, due to its extreme ease of exploitation and the fact that it can be used to establish a backdoor on the web server.


The vulnerability “can be exploited by simply changing a single character of a request to upper-case,” researchers at Sucuri explained.


Essentially, the plugin can send commands to various REST API endpoints, and it performs a permissions check to make sure no one’s doing anything they’re not allowed to do. However, the REST API routes are case-sensitive, so an attacker need only alter the case of one character to bypass the authentication checks, according to the writeup.


“When exploited, this vulnerability has the capability to overwrite certain files within the WordPress file structure, effectively giving backdoor access to any attacker,” Sucuri researchers said. “This would allow a takeover of the website, and could elevate the privileges of subscriber accounts into admins.”


The second bug carries a high-severity CVSS score of 7.7 and affects versions 4.1.3.1 and 4.1.5.2 of All in One SEO.


Specifically, the issue lies in an API endpoint called “/wp-json/aioseo/v1/objects.” If attackers exploited the previous vulnerability to elevate their privileges to admin-level, they would gain the ability to access the endpoint, and from there be able to send malicious SQL commands to the back-end database to retrieve user credentials, admin information and other sensitive data, according to Sucuri.


All in One SEO users should update to the patched version to be safe, researchers said. Other defensive steps include:


1. Reviewing the administrator users in the system and removing any suspect ones;
2. Changing all administrator account passwords;
3. And adding additional hardening to the administrator panel.


**Plugin Paradise for Website Hackers**
---------------------------------------


WordPress plugins continue to be an attractive path to site compromise for cyberattackers, researchers noted. For instance, earlier in December, an active attack swelled against more than 1.6 million WordPress sites, with researchers spotting tens of millions of attempts to exploit four different plugins and several Epsilon Framework themes.


“WordPress plugins continue to be a major risk to any web application, making them a regular target for attackers,” Uriel Maimon, senior director of emerging technologies at PerimeterX, said via email. “Shadow code introduced via third-party plugins and frameworks vastly expands the attack surface for websites.”


The warning comes as new bugs continue to crop up. Earlier this month for instance, the plugin “Variation Swatches for WooCommerce,” installed across 80,000 WordPress-powered retail sites, [was found to contain](https://threatpost.com/retail-woocommerce-sites-plugin-xss-bug/176704/) a stored cross-site scripting (XSS) security vulnerability that could allow cyberattackers to inject malicious web scripts and take over sites.


In October, two high-severity vulnerabilities in Post Grid, a WordPress plugin with more than 60,000 installations, [were found to](https://threatpost.com/wordpress-plugin-flaws/159856/) open the door to site takeovers, according to researchers. To boot, nearly identical bugs are also found in Post Grid’s sister plug-in, Team Showcase, which has 6,000 installations.


Also in October, a [WordPress plugin bug](https://threatpost.com/wordpress-plugin-bug-wipe-sites/175826/) was discovered in the Hashthemes Demo Importer offering, which allowed users with simple subscriber permissions to wipe sites of all content.


“Website owners need to be vigilant about third-party plugins and frameworks and stay on top of security updates,” Maimon said. “They should secure their websites using web application firewalls, as well as client-side visibility solutions that can reveal the presence of malicious code on their sites.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]] [[action.malware.name=UPPERCUT]]

#### Industry:
[[victim.industry.name=Information]] [[victim.industry.name=Retail]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Wordpress]] [[Plugin]] [[Plugins]] [[Seo]] [[Websites]] [[Api]] [[ThreatPost]]
#### ipv4-adresses
4.1.5.3 4.1.5.2 4.1.3.1

