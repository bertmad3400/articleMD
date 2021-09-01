# Gutenberg Template Library & Redux Framework Bugs Plague WordPress Sites
### Two vulnerabilities in the site-building plugin could be useful tools in the hands of a skilled attacker, researchers warned.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169111)
+ Date: September 1, 2021  1:58 pm
+ Author: Tara Seals


## Article:
![wordpress plugin zero day](https://media.threatpost.com/wp-content/uploads/sites/103/2019/01/28092447/wordpress_plugin_vuln.jpg)
Two vulnerabilities have been found in the Gutenberg Template Library & Redux Framework plugin for WordPress, which is installed on more than 1 million websites. They could allow arbitrary plugin installation, post deletions and access to potentially sensitive information about a site’s configuration, researchers said.


The plugin, from developer Redux.io, offers various templates and building blocks for creating web pages within WordPress’ Gutenberg editor:


The first bug (CVE-2021-38312) rates 7.1 out of 10 on the CVSS scale, making it high-severity. It arises from the plugin’s use of the WordPress REST API, which processes requests to install and manage the blocks. It fails to authorize user permissions correctly, according to Wordfence.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“While the REST API Endpoints registered under the redux/v1/templates/ REST Route used a permission\_callback to verify a user’s permissions, this callback only checked whether or not the user sending the request had the edit\_posts capability,” Wordfence researchers noted in a [Wednesday posting](https://www.wordfence.com/blog/2021/09/over-1-million-sites-affected-by-redux-framework-vulnerabilities/).


That means that users with lower permissions, such as contributors and authors, could install any plugin in the WordPress repository via the redux/v1/templates/plugin-install endpoint, researchers said, or they could use the redux/v1/templates/delete\_saved\_block endpoint to erase posts.


The second, medium-severity vulnerability (CVE-2021-38314) rates 5.3 on the CVSS scale. It exists because the Gutenberg Template Library & Redux Framework plugin registers several AJAX actions available to unauthenticated users, one of which is deterministic and predictable, making it possible to uncover what the $support\_hash for a site would be.


“This $support\_hash AJAX action, which was also available to unauthenticated users, called the support\_args function in redux-core/inc/classes/class-redux-helpers.php, which returned potentially sensitive information such as the PHP version, active plugins on the site and their versions, and an unsalted md5 hash of the site’s AUTH\_KEY and SECURE\_AUTH\_KEY,” according to Wordfence.


Researchers added that an attacker could use the information to plan a website takeover using other vulnerable plugins.


Redux.io has issued a patch, in version 4.2.13.


Wordfence researchers said users should update their plugins as soon as possible: “While neither of these could be used directly to take over a site, both vulnerabilities could be useful tools in the hands of a skilled attacker,” they said.


WordPress Plugin Problems Persist
---------------------------------


These are only the latest WordPress plugin vulnerabilities to come to light. Other notable vulnerabilities this year include:


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[plugin]] [[WordPress]] [[Gutenberg]] [[ThreatPost]]
