# WordPress sites are being hacked in fake ransomware attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/wordpress-sites-are-being-hacked-in-fake-ransomware-attacks/)
+ Date: November 16, 2021
+ Author: Bill Toulas


## Article:
![WordPress](https://www.bleepstatic.com/content/hl-images/2020/09/10/WordPress-war.jpg)


A new wave of attacks starting late last week has hacked close to 300 WordPress sites to display fake encryption notices, trying to trick the site owners into paying 0.1 bitcoin for restoration.


These ransom demands come with a countdown timer to induce a sense of urgency and possibly panic a web admin into paying the ransom.


While the 0.1 bitcoin (~$6,069.23) ransom demand is not particularly significant compared to what we see on high-profile ransomware attacks, it can still be a considerable amount for many website owners.



![Bogus site encryption message](https://www.bleepstatic.com/images/news/u/1220909/ransomware/encryption_page.png)**Bogus site encryption message**  
*Source: Sucuri*
Smoke and mirrors
-----------------


These attacks were discovered by cybersecurity firm Sucuri who was hired by one of the victims to perform incident response.


The researchers discovered that the websites had not been encrypted, but rather the threat actors modified an installed WordPress plugin to display a ransom note and countdown when 



![WordPress plugin used to display ransom notes and countdown](https://www.bleepstatic.com/images/news/security/w/wordpress/fake-ransomware-attack/wp-plugin.jpg)**WordPress plugin used to display ransom notes and countdown**  
*Source: Sucuri*
In addition to displaying a ransom note, the plugin would modify all the WordPress blog posts and set their 'post\_status' to 'null,' causing them to go into an unpublished state.


As such, the actors created a simple yet powerful illusion that made it look as if the site had been encrypted.


By removing the plugin and running a command to republish the posts and pages, the site returned to its normal status.


Upon further analysis of the network traffic logs, [Sucuri](https://blog.sucuri.net/2021/11/fake-ransomware-infection-spooks-website-owners.html) found that the first point where the actor's IP address appeared was the wp-admin panel.


This means that the infiltrators logged in as admins on the site, either by brute-forcing the password or by sourcing stolen credentials from dark web markets.


This was not an isolated attack but instead appears to be part of a broader campaign, giving more weight to the second scenario.


As for the plugin seen by Sucuri, it was Directorist, which is a tool to build online business directory listings on sites.


Sucuri has tracked approximately 291 websites affected by this attack, with [a Google search](https://www.google.com/search?q=%E2%80%9CFOR+RESTORE+SEND+0.1+BITCOIN%E2%80%9D) showing a mix of cleaned-up sites and those still showing ransom notes.


All of the sites seen by BleepingComputer in search results use the same [3BkiGYFh6QtjtNCPNNjGwszoqqCka2SDEc](https://www.blockchain.com/btc/address/3BkiGYFh6QtjtNCPNNjGwszoqqCka2SDEc) Bitcoin address, which has not received any ransom payments.


Protecting against site encryptions
-----------------------------------


Sucuri suggests the following security practices to protect WordPress sites from being hacked:


* Review admin users on the site, remove any bogus accounts, and update/change all wp-admin passwords.
* Secure your wp-admin administrator page.
* Change other access point passwords (database, FTP, cPanel, etc).
* Place your website behind a firewall.
* Follow reliable backup practices that will make restoration easy in the case of a real encryption incident.


As WordPress is commonly targeted by threat actors, it is also important to make sure all of your installed plugins are running the latest version.




#### Tags:
[[WordPress]] [[plugin]] [[wp-admin]] [[Bleeping Computer]]
