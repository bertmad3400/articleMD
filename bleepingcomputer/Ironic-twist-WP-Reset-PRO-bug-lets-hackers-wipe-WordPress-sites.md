# Ironic twist: WP Reset PRO bug lets hackers wipe WordPress sites
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/ironic-twist-wp-reset-pro-bug-lets-hackers-wipe-wordpress-sites/)
+ Date: November 10, 2021
+ Author: Sergiu Gatlan


## Article:
![Ironic twist: WP Reset PRO bug lets hackers wipe WordPress sites](https://www.bleepstatic.com/content/hl-images/2021/11/10/WordPress.jpg)


A high severity security flaw in the WP Reset PRO WordPress plugin can let authenticated attackers wipe vulnerable websites, as revealed by Patchstack security researchers.


It impacts only premium versions of the [WP Reset plugin](https://wpreset.com/), up to and including the 5.98 release. This plugin is designed to help admins reset their entire site or selected parts to speed up debugging and testing, as well as restore from built-in snapshots with a single mouse click.


WP Reset's free and open-source version is listed in the WordPress plugin repository as having [over 300,000 active installations](https://wordpress.org/plugins/wp-reset/). The developer claims on the official website that the number of users has surpassed 400,000.


Patchstack CTO Dave Jong [explained](https://patchstack.com/wp-reset-pro-critical-vulnerability-fixed/) that the authenticated database reset vulnerability (tracked as [CVE-2021-36909](https://patchstack.com/database/vulnerability/wp-reset/wordpress-wp-reset-pro-premium-plugin-5-98-authenticated-database-reset-vulnerability)) is caused by a lack of authorization and nonce token check and can be exploited by any authenticated user, including low-privileged users such as subscribers.


Exploitation only requires passing a query parameter like "*%%wp"*to delete all tables in the database with the prefix wp. The attacker can then visit the website's homepage to go through the WordPress installation process and create their own administrator account.


"It would wipe the site and would make it obvious that something happened, which is why it may not be exploited if a hacker has the intention to hide a backdoor or inject advertisements into the site," Jong told BleepingComputer.



> 
> The plugin registers a few actions in the admin\_action\_* scope. In the case of this vulnerability, it's admin\_action\_wpr\_delete\_snapshot\_tables. Unfortunately, the admin\_action\_* scope does not perform a check to determine if the user is authorized to perform said action, nor does it validate or check a nonce token to prevent CSRF attacks. — Dave Jong
> 
> 
> 


Critical issue for sites allowing open user registration
--------------------------------------------------------


Subscriber is a default WordPress user role (just as Contributor, Author, Editor, and Administrator), often enabled to allow registered users to write comments on WordPress sites' comment section. They are typically only able to edit their own profile using the site's dashboard without access to the other admin pages.


Patchstack CEO Oliver Sild told BleepingComputer that the bug is "quite critical especially to e-commerce and other sites that have any registration open."


While, at first sight, this bug seems to be useful only for destructive purposes, Sild told BleepingComputer that it could also be exploited to gain access to other sites on the same server.


"If there is an old site forgotten to a subdirectory (we see that a lot) that has that plugin installed and the server environment is connected, then this would allow getting access to other sites in the same environment," Sild said. "It's a quite destructive vulnerability in its nature."


The development team fixed the bug with the release of WP Reset PRO 5.99 on September 28, within 24 hours of Patchstack disclosure, by adding an authentication and authorization check.




#### Tags:
[[WordPress]] [[plugin]] [[WP]] [[Patchstack]] [[Bleeping Computer]]
