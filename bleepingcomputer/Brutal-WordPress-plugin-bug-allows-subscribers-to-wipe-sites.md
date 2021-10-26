# Brutal WordPress plugin bug allows subscribers to wipe sites
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/brutal-wordpress-plugin-bug-allows-subscribers-to-wipe-sites/)
+ Date: October 26, 2021
+ Author: Sergiu Gatlan


## Article:
![Brutal WordPress plugin bug allows subscribers to wipe sites](https://www.bleepstatic.com/content/hl-images/2021/02/11/WordPress-headpic.jpg)


A high severity security flaw found in a WordPress plugin with more than 8,000 active installs can let authenticated attackers reset and wipe vulnerable websites.


The plugin in question, known as [Hashthemes Demo Importer](https://wordpress.org/plugins/hashthemes-demo-importer/), is designed to help admins import demos for WordPress themes with a single, without dealing with installing any dependencies.


The security bug would allow authenticated attackers to reset WordPress sites and delete almost all database content and uploaded media.


Wordfence QA engineer and threat analyst Ram Gall [explained](https://www.wordfence.com/blog/2021/10/site-deletion-vulnerability-in-hashthemes-plugin/) that the plugin failed to properly perform nonce checks, leaking the AJAX nonce on vulnerable sites' admin dashboard for all users, "including low-privileged users such as subscribers."


As a direct consequence of this bug, logged-in subscriber-level users could abuse it to wipe all the content on sites running unpatched versions of Hashthemes Demo Importer.


"While most vulnerabilities can have destructive effects, it would be impossible to recover a site where this vulnerability was exploited unless it had been backed up," Gall added.



> 
> Any logged-in user could trigger the hdi\_install\_demo AJAX function and provide a reset parameter set to true, resulting in the plugin running it’s database\_reset function. This function wiped the database by truncating every database table on the site except for wp\_options, wp\_users, and wp\_usermeta. Once the database was wiped, the plugin would then run its clear\_uploads function, which deleted every file and folder in wp-content/uploads. — Ram Gall
> 
> 
> 


Subscriber, one of the types of users who could wipe vulnerable sites, is a default WordPress user role (just as Contributor, Author, Editor, and Administrator) often enabled on WordPress sites to allow registered users to write comments on the website's comment section.


They would typically only be able to edit their profile using the site's dashboard without access to other admin pages.


While Wordfence reported the vulnerability the bug to the plugin's development team on August 25, 2021, the developers did not reply to the disclosure messages for almost a month.


This prompted Wordfence to reach out to the WordPress plugins team on September 20, which led to the plugin's removal the same day and the release of a patch addressing the bug four days later, on September 24.


However, Hashthemes Demo Importer's developer did not mention the 1.1.2 release or the update on [the plugin's changelog page](https://wordpress.org/plugins/hashthemes-demo-importer/#developers) despite releasing a security update.




#### Tags:
[[plugin]] [[WordPress]] [[Hashthemes]] [[Wordfence]] [[Bleeping Computer]]
