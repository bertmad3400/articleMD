# WordPress plugin bug lets attackers inject code into vulnerable sites
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/wordpress-plugin-bug-lets-attackers-inject-code-into-vulnerable-sites/)
+ Date: October 27, 2021
+ Author: Catalin Cimpanu


## Article:
![WordPress plugin bug lets attackers inject code into vulnerable sites](https://therecord.media/wp-content/uploads/2021/10/WordPress.jpg)

A security flaw found in a popular WordPress plugin installed on more than one million websites allows attackers o inject malicious code into vulnerable sites.


Discovered by Wordfence, a provider of web firewalls for WordPress sites, the vulnerability impacts a plugin that integrates the OptinMonster sales, marketing, and newsletter platform inside WordPress websites.


“These flaws made it possible for an unauthenticated attacker, **meaning any site visitor**, to export sensitive information and add malicious JavaScript to WordPress sites, among many other actions,” said Wordfence security researcher Chloe Chamberland.


According to a [technical report](https://www.wordfence.com/blog/2021/10/1000000-sites-affected-by-optinmonster-vulnerabilities/) published earlier today, Chamberland blamed the issue on poor coding.


Namely, Chamberland said the plugin had left many of the OptinMonster API endpoints open to commands via the sites where the plugin was installed.


Chamberland said an attacker could query these API endpoints and get details about the site, including their OptinMonster API key.


The attacker could then use this API key to make changes to the site’s OptinMonster marketing and sales campaigns and add their own malicious code to the popups the plugin was showing to site visitors.


Chamberland said the Wordfence team reported the issue to OptinMonster in late September and that the company released a temporary patch a day later, with a full patch delivered on October 7, via the [OptinMonster 2.6.5](https://wordpress.org/plugins/optinmonster/#developers) release.


Additionally, since the company couldn’t tell if the issue had been previously exploited, OptinMonster also invalidated all API keys and forced customers to generate new ones.


Wordfence disclosed the issue today to give the plugin’s more than one million users time to update their sites before mass-exploitation of the issue is most likely to begin.





#### Tags:
[[OptinMonster]] [[plugin]] [[API]] [[WordPress]] [[Chamberland]] [[Wordfence]] [[The Record]]
