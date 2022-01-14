# Three Plugins with Same Bug Put 84K WordPress Sites at Risk
### Researchers discovered vulnerabilities that can allow for full site takeover in login and e-commerce add-ons for the popular website-building platform.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177654
+ Date: 2022-01-14T14:07:36+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2017/11/06222231/WordPress-SQLi-bug.jpg)

Researchers have discovered three [WordPress plug-ins](https://threatpost.com/wordpress-plugin-bug-wipe-sites/175826/) with the same vulnerability that allows an attacker to update arbitrary site options on a vulnerable site and completely take it over. Exploiting the flaw does require some action from the site administrator, however.


On Nov. 5, 2021, the Wordfence Threat Intelligence team started a process to disclose a vulnerability researchers had found in “[Login/Signup Popup](https://wordpress.org/plugins/easy-login-woocommerce),” a [WordPress plug-in](https://threatpost.com/frontend-file-manager-wordpress-bugs/167687/) installed on more than 20,000 sites, Wordfence’s Chloe Chamberland wrote [in a post](https://www.wordfence.com/blog/2022/01/84000-wordpress-sites-affected-by-three-plugins-with-the-same-vulnerability/?utm_medium=email&_hsmi=200773868&_hsenc=p2ANqtz-8wONqcLAiQD8o__3dsSDSjuLwHX4hhqMgH_Vvhs-LcUGTU2JWYOvVeflfGHs_Uz1VP67vtVIWObFp9507lPzgx4OjFww&utm_content=200773868&utm_source=hs_email) published online Thursday.


However, a few days later they discovered that the flaw was present in two other plug-ins by the same developer, who goes by the online name of [XootiX.](https://xootix.com/) They are “[Side Cart Woocommerce (Ajax)](https://wordpress.org/plugins/side-cart-woocommerce/),” which has been installed on more than 60,000 sites, and “[Waitlist Woocommerce (Back in stock notifier)](https://wordpress.org/plugins/waitlist-woocommerce/),” which has been installed on more than 4,000.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Login/Signup Popup is a “simple and lightweight” plug-in aimed at streamlining a site’s registration, login and password reset processes, according to its description online. Side Cart Woocommerce – designed to work with the Woocommerce plugin for creating an e-commerce store – allows a site’s users to access items they’ve placed into a shopping cart using from anywhere on the site. Waitlist Woocommerce – also to be used with Woocommerce – adds the functionality of tracking demand for out-of-stock items to an e-commerce site.


As of now, all of the plug-ins have been updated and the flaw patched, according to the post. On Nov. 24, the developer released a patched version of Login/Signup Popup as version 2.3. Later, on Dec. 17, a patched version of Waitlist Woocommerce, version 2.5.2, was released; and a patched version of Side Cart Woocommerce, version 2.1, was released.


Still, the discovery of the bug’s multiple occurrences reflects an ongoing issue with WordPress plug-ins being riddled with flaws. Indeed, vulnerabilities in the plug-ins [skyrocketed](https://www.riskbasedsecurity.com/2022/1/11/wordpress-vulnerabilities-more-than-doubled-in-2021/) with triple-digit growth in 2021, according to RiskBased Security.


**How the Flaw Works**
----------------------


The vulnerability found by the Wordfence team is fairly straightforward, Chamberland wrote. All three plug-ins register the save\_settings function, which is initiated via a wp\_ajax action, they said.


In each of the plug-ins, “this function was missing a nonce check, which meant that there was no validation on the integrity of who was conducting the request,” according to the post.


What this sets up is a scenario in which an attacker can craft a request that would trigger the AJAX action and execute the function, Chamberland wrote. However, action from the site’s administrator – “like clicking on a link or browsing to a certain website while the administrator was authenticated to the target site” – is needed to fully exploit the flaw, she said.


In these cases, “the request would be successfully sent and trigger the action which would allow the attacker to update arbitrary options on that website,” she explained in the post.


Exploiting Arbitrary Options Update vulnerabilities in this way is something threat actors “frequently abuse,” allowing them to update any option on a WordPress website and to ultimately take it over, Chambers noted.


This latter privilege occurs if an attacker sets “the user\_can\_register option to true and the default\_role option to administrator so that they can register on the vulnerable site as an administrator,” she explained.


**Risks and Mitigations**
-------------------------


Though the fact that the flaws found in the plug-ins require administrator action makes them “less likely to be exploited,” they can have “significant impact” if they are exploited, Chamberland said.


“As such, it serves as an incredibly important reminder to remain aware when clicking on links or attachments and to ensure that you are regularly keeping your plug-ins and themes up to date,” she advised.


Recommended actions for WordPress users who use the plug-ins are to verify that their site has been updated to the latest patched version available for each of them. That would be version 2.3 for “Login/Signup Popup”, version 2.5.2 for “Waitlist Woocommerce (Back in stock notifier )”, and version 2.1 for “Side Cart Woocommerce (Ajax),” according to the post.


All Wordfence users are protected against the vulnerability, according to the post. Wordfence Premium users received a firewall rule to protect against any exploits targeting them on Nov. 5, and sites still using the free version of Wordfence received the same protection on Dec. 5.


**Password** **Reset:** **[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):** Fortify 2022 with a password security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the *new* password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken. **[Register & Stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)** – sponsored by Specops Software.





## Tags:

#### Threatactor:
[[threatactor.name=Rocke]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Plug-ins]] [[Woocommerce]] [[Wordfence]] [[Wordpress]] [[Chamberland]] [[ThreatPost]]

