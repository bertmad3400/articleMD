# PHP Everywhere RCE flaws threaten thousands of WordPress sites
### Researchers found three critical remote code execution (RCE) vulnerabilities in the PHP Everywhere plugin for WordPress, used by over 30,000 websites worldwide.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/php-everywhere-rce-flaws-threaten-thousands-of-wordpress-sites/
+ Date: 2022-02-09 21:33:18+00:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/02/11/WordPress-headpic.jpg)

![WordPress logo](https://www.bleepstatic.com/content/hl-images/2021/02/11/WordPress-headpic.jpg)


Researchers found three critical remote code execution (RCE) vulnerabilities in the 'PHP Everywhere' plugin for WordPress, used by over 30,000 websites worldwide.


PHP Everywhere is a plugin that allows WordPress admins to insert PHP code in pages, posts, the sidebar, or any Gutenberg block, and use it to display dynamic content based on evaluated PHP expressions.


Three RCE flaws
---------------


The three vulnerabilities were discovered by security analysts at [Wordfence](https://www.wordfence.com/blog/2022/02/critical-vulnerabilities-in-php-everywhere-allow-remote-code-execution/) and can be exploited by contributors or subscribers, affecting all WordPress versions from 2.0.3 and below.


Here's a short description of the flaws:


* [**CVE-2022-24663**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24663) – Remote code execution flaw exploitable by any subscriber  by allowing them to send a request with the ‘shortcode’ parameter set to PHP Everywhere, and execute arbitrary PHP code on the site. (CVSS v3 score: 9.9)
* [**CVE-2022-24664**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24664) – RCE vulnerability exploitable by contributors via the plugin’s metabox. An attacker would create a post, add a PHP code metabox, and then preview it. (CVSS v3 score: 9.9)
* [**CVE-2022-24665**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24665) – RCE flaw exploitable by contributors who have the ‘edit\_posts’ capability and can add PHP Everywhere Gutenberg blocks. Default security setting on vulnerable plugin versions isn’t on ‘admin-only’ as it should be. (CVSS v3 score: 9.9)

While the last two flaws aren't easily exploitable as they require contributor-level permissions, the first vulnerability is a lot more open to broader exploitation as it can be exploited by just being a subscriber on the site.


For example, a logged-in customer on a site is considered a ‘subscriber,’ so merely registering on the target platform would be enough to gain enough privileges for malicious PHP code execution.


In all cases, executing arbitrary code on a site can lead to a complete site takeover, which is the worst possible scenario in website security.


Fix only for Block editor
-------------------------


Wordfence’s team discovered the vulnerabilities on January 4, 2022, and informed the author of PHP Everywhere of its findings.


The vendor released a security update on January 10, 2022, with version 3.0.0, which took a major version number bump because it required a substantial code rewrite.


While the developers fixed the update last month, it is not uncommon for admins to not regularly update their WordPress site and plugins. According to the [download stats](http://api.wordpress.org/stats/plugin/1.0/downloads.php?slug=php-everywhere) on WordPress.org, only 15,000 installs out of 30,000 have updated the plugin since the bugs were fixed.


Therefore, due to the severity of these vulnerabilities, all users of PHP Everywhere are strongly advised to make sure they have upgraded to PHP Everywhere version 3.0.0, which is [the latest available at this time](https://wordpress.org/plugins/php-everywhere/).


Note that if you’re using the Classic Editor on your site, you will need to uninstall the plugin and find another solution for hosting custom PHP code on its components.


That is because version 3.0.0 only supports PHP snippets via the Block editor, and it’s unlikely that the author will work on restoring functionality for the sun-setting Classic.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Php]] [[Plugin]] [[Wordpress]] [[Rce]] [[(cvss]] [[V3]] [[Bleeping Computer]]
#### CVE's
[[CVE-2022-24663]] [[CVE-2022-24664]] [[CVE-2022-24665]]

