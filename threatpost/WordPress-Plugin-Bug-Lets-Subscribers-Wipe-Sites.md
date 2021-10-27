# WordPress Plugin Bug Lets Subscribers Wipe Sites
### The flaw, found in the Hashthemes Demo Importer plugin, allows any authenticated user to exsanguinate a vulnerable site, deleting nearly all database content and uploaded media.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175826)
+ Date: October 27, 2021  5:39 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/27165503/eraser-e1635368120664.jpeg)
Researchers have discovered a homicidal WordPress plugin that allows subscribers to wipe sites clean of content.


The high-severity security flaw is found in [Hashthemes Demo Importer](https://wordpress.org/plugins/hashthemes-demo-importer/), a plugin that’s used in more than 8,000 active installations.


According to security researchers at Wordfence, the vulnerability allows any authenticated user to completely exsanguinate a vulnerable site, “permanently deleting nearly all database content as well as all uploaded media.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The HashThemes Demo Importer plugin is designed to let admins easily import demos for WordPress themes with a single click, without having to deal with dependencies such as XML files, .json theme options,.dat customizer files or .wie widget files.


In a Tuesday [writeup](https://www.wordfence.com/blog/2021/10/site-deletion-vulnerability-in-hashthemes-plugin/), Wordfence’s Ram Gall said that the Wordfence Threat Intelligence team initiated the disclosure process for the bug on Aug. 25. For nearly a month, the developer failed to respond, so Wordfence got in touch with the WordPress plugins team on Sept. 20.


WordPress Yanks Plugin, Puts Out Fix Lickety-Split
--------------------------------------------------


On the same day, the WordPress crew temporarily removed the Hashthemes Demo Importer from the repository, and a patched version was made available a few days later, on Sept. 24, although the plugin’s [changelog](https://wordpress.org/plugins/hashthemes-demo-importer/#developers) makes no mention of it.


Plugin Chopped Nearly Every Database Table
------------------------------------------


Wordfence’s Gall explained that the Hashthemes demo importer plugin hadn’t performed capability checks for many of its Ajax actions. Ajax is a JavaScript-based technology that allows a web page to fetch new information and present itself without refreshing the page.


“While it did perform a nonce check, the AJAX nonce was visible in the admin dashboard for all users, including low-privileged users such as subscribers,” according to the Wordfence writeup. “The most severe consequence of this was that a subscriber-level user could reset all of the content on a given site.


Specifically, any logged-in user could trigger the hdi\_install\_demo Ajax function and provide a reset parameter set to true, Gall wrote, resulting in the plugin running its database\_reset function.


“This function wiped the database by truncating every database table on the site except for wp\_options, wp\_users, and wp\_usermeta,” Gall continued. “Once the database was wiped, the plugin would then run its clear\_uploads function, which deleted every file and folder in wp-content/uploads.”


Let’s Hear It for Backups
-------------------------


Gall said that the vulnerability should remind us of the importance of backups for a site’s security. “While most vulnerabilities can have destructive effects, it would be impossible to recover a site where this vulnerability was exploited unless it had been backed up,” he wrote. Given that the vulnerability can lead to complete site takeover, he asked that if you know of somebody using this plugin on their site, please do give them a heads-up.


Plugins Expand the Attack Surface
---------------------------------


Rick Holland, CISO and vice president of strategy at digital risk protection vendor Digital Shadows, noted that the plugin vulnerability highlight the increased attack surface that third-party code ushers in, the same as browser extensions.


That’s up to software vendors to deal with: “Software companies are responsible for their code and the code that runs on top of their code,” Holland told Threatpost via email.


Jake Williams, co-founder and CTO at incident response firm BreachQuest, said that the incident highlights the complexity of vulnerability management. “Not only do organizations need to know the content management systems they are running, but also the plugins that are running on those systems too,” he told Threatpost on Wednesday. “This is yet another example of supply chain security where the WordPress system was trustworthy, but the plugin (which the security team probably doesn’t even know was installed) left them vulnerable.


Only Brats Demolish Sites
-------------------------


Williams also noted that this kind of flaw attracts jerks, as opposed to financially motivated attackers. “I don’t think the majority of threat actors are interested in wiping databases and content in WordPress sites,” he told Threatpost on Wednesday. “It’s counter to the goals of most threat actors. That said, I do expect that some people will go and target these systems for fun, so it is a serious risk.”


Holland concurred: “Destructive threat actors, hacktivists, or actors deleting sites for the ‘lulz’ would be most interested in this sort of vulnerability,” he said.


It wouldn’t be tough to take advantage of such a flaw, either, Holland added: “Exploiting this vulnerability does require authentication, but given password use and account takeovers, that bar isn’t as high as it should be.”


How to Weave Security Into WordPress
------------------------------------


Leo Pate, managing consultant at application security company nVisium, noted that WordPress is just like any software: Namely, it’s made by fallible humans. “Its developers and those that make WordPress components, such as plugins and templates, are bound to make mistakes” he said in an email to Threatpost on Wednesday. He sent over the following cheatsheet on how to look holistically at a WordPress environment and to incorporate security into all of its components: server, network and app layers.


His advice includes:


Within the WordPress plugin portal, users can see information that includes:


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[WordPress]] [[plugin]] [[Threatpost]] [[Hashthemes]] [[Wordfence]] [[plugins]] [[Wednesday.]] [[ThreatPost]]
