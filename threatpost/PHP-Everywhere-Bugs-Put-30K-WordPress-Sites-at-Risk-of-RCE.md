# PHP Everywhere Bugs Put 30K+ WordPress Sites at Risk of RCE
### The plug-in’s default settings spawned flaws that could allow for full site takeover but have since been fixed in an update that users should immediately install, Wordfence researchers said.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178338
+ Date: 2022-02-10T13:58:07+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2019/04/23131246/WordPress-plugin-exploit.jpg)

Tens of thousands of WordPress sites are at risk from critical vulnerabilities in a widely used plug-in that facilitates the use of PHP code on a site.


One of the bugs allows any authenticated user of any level – even subscribers and customers – to execute code that can completely take over a site that has the plugin installed, researchers have found.


Researchers from Wordfence Threat Intelligence discovered three critical vulnerabilities in [PHP Everywhere](https://wordpress.org/plugins/php-everywhere/), a plug-in installed on more than 30,000 WordPress sites, as they revealed in [a blog post](https://www.wordfence.com/blog/2022/02/critical-vulnerabilities-in-php-everywhere-allow-remote-code-execution/) published Tuesday. The plug-in does precisely what its name suggests, allowing WordPress site developers to put PHP code in various components of a site, including pages, posts and sidebars.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“These vulnerabilities are very easy to exploit and can be used to quickly and completely take over a site,” Wordfence’s Ram Gall wrote in the post. Wordfence provides security for WordPress websites.


The three vulnerabilities were due to default settings in the plug-in that have since been fixed by the plug-in’s developer after Wordfence notified him via a responsible disclosure process.


The Wordfence team emailed PHP Everywhere’s builder, [Alexander Fuchs](https://www.linkedin.com/in/alexander-fuchs-it/), on Jan. 4 and received an almost immediate response. He subsequently released a “largely rebuilt version of the plugin” that fixes all the issues on Jan. 10, Gall wrote. Wordfence urges all custodians of WordPress sites using the plug-in to immediately install the update.


**Critical Vulnerabilities**
----------------------------


The most dangerous of the flaws, “Remote Code Execution by Subscriber+ users via shortcode” and tracked as [CVE-2022-24663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24663), is associated with the plug-in’s inclusion of functionality that allows execution of PHP Code Snippets via WordPress shortcodes, researchers wrote. The bug earned a critical rating of 9.9 on the CVSS.


“Unfortunately, WordPress allows any authenticated users to execute shortcodes via the parse-media-shortcode AJAX action, and some plugins also allow unauthenticated shortcode execution,” Gall wrote in the post. “As such it was possible for any logged-in user, even a user with almost no permissions, such as a Subscriber or a Customer, to execute arbitrary PHP on a site by sending a request with the shortcode parameter set to [php\_everywhere]<arbitrary PHP>[/php\_everywhere].”


Executing this arbitrary PHP on a WordPress site typically allows for “complete site takeover,” researchers found.


The other two bugs are tracked as [CVE-2022-24664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24664) and [CVE-2022-24665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24665), respectively. Both of them earned the same CVSS score as the shortcode vulnerability, but were deemed slightly less severe by researchers because they require contributor-level permissions to exploit, Gall explained.


The former, “Remote Code Execution by Contributor+ users via metabox,” has to do with a default setting in PHP Everywhere that allowed all users with the edit\_posts capability to use the PHP Everywhere metabox.


“Unfortunately this meant that untrusted Contributor-level users could use the PHP Everywhere metabox to achieve code execution on a site by creating a post, adding PHP code to the PHP Everywhere metabox, and then previewing the post,” Gall wrote.


The third vulnerability, “Remote Code Execution by Contributor+ users via gutenberg block,” is associated with a default setting in PHP Everywhere that allowed all users with the edit\_posts capability to use the PHP Everywhere Gutenberg block.


“While it was possible to set this to admin-only, this was not set by default due to versions <= 2.0.3 not being able to add capability checks without disabling the Gutenberg Block editor,” Gall explained.


Unfortunately, this setting meant that Contributor-level users could execute arbitrary PHP code on a site by creating a post, adding the PHP everywhere block and adding code to it, and then previewing the post, he said.


**Risks and Protections**
-------------------------


WordPress plug-ins are a constant pain point for developers of sites built using the open-source content-management and website-creation system, often including vulnerabilities that threaten the security of WordPress sites.


Last month, [researchers discovered](https://threatpost.com/plugins-vulnerability-84k-wordpress-sites/177654/) three [WordPress plug-ins](https://threatpost.com/wordpress-plugin-bug-wipe-sites/175826/) with the same vulnerability that could allow an attacker, with site-administrator action, to update arbitrary site options on a vulnerable site and completely take it over. And last October, a WordPress plugin called [Hashthemes Demo Importer](https://wordpress.org/plugins/hashthemes-demo-importer/) allowed subscribers [to wipe sites completely clean](https://threatpost.com/wordpress-plugin-bug-wipe-sites/175826/) of their content.


Indeed, the number of exploitable WordPress plugin vulnerabilities [exploded in 2021](https://threatpost.com/wordpress-bugs-exploded-2021-exploitable/177553/), rising by triple digits, according to researchers from RiskBased Security.


For its part, Wordfence has offered mitigations of its own to users affected by the PHP Everywhere flaws. The company offered its premium users a firewall rule protecting against the PHP Everywhere vulnerabilities the same day researchers notified the plug-in’s developer. It later extended the firewall to other customers as well as users of the free version of Wordfence.


Wordfence also is offering WordPress users affected by the flaws Incident Response services via its [Wordfence Care](https://www.wordfence.com/products/wordfence-care/) service, according to the post.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Php]] [[Wordpress]] [[Wordfence]] [[Plug-in]] [[Plugin]] [[“remote]] [[Shortcode]] [[Metabox]] [[ThreatPost]]
#### CVE's
[[CVE-2022-24663]] [[CVE-2022-24664]] [[CVE-2022-24665]]

