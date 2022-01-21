# Over 90 WordPress themes, plugins backdoored in supply chain attack
### A massive supply chain attack compromised 93 WordPress themes and plugins to contain a backdoor, giving threat-actors full access to websites.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/over-90-wordpress-themes-plugins-backdoored-in-supply-chain-attack/
+ Date: 2022-01-21T10:34:01-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/02/08/supply-chain.jpg)

![chain](https://www.bleepstatic.com/content/hl-images/2021/02/08/supply-chain.jpg?rand=179594257)


A massive supply chain attack compromised 93 WordPress themes and plugins to contain a backdoor, giving threat-actors full access to websites.


In total, threat actors compromised 40 themes and 53 plugins belonging to AccessPress, a developer of WordPress add-ons used in over 360,000 active websites.


The attack was discovered by researchers at Jetpack, the creators of a security and optimization tool for WordPress sites, who discovered that a PHP backdoor had been added to the themes and plugins.


Jetpack believes an external threat actor breached the AccessPress website to compromise the software and infect further WordPress sites.


A backdoor to give complete control
-----------------------------------


As soon as admins installed a compromised AccessPress product on their site, the actors added a new “initial.php” file into the main theme directory and included it in the main “functions.php” file.


This file contained a base64 encoded payload that writes a webshell into the “./wp-includes/vars.php” file.



![Encoded payload writing the webshell](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/backdoor.png)**Encoded payload writing the webshell**  
*Source: Sucuri*
The malicious code completed the backdoor installation by decoding the payload and injecting it into the “vars.php” file, essentially giving the threat actors remote control over the infected site.


The only way to detect this threat is to use a core file integrity monitoring solution, as the malware deletes the “initial.php” file dropper to cover its tracks.


According to [Sucuri](https://blog.sucuri.net/2022/01/accesspress-themes-hit-with-targeted-supply-chain-attack.html) researchers who investigated the case to figure out the actors’ goal, threat actors used the backdoor to redirect visitors to malware-dropping and scam sites. Therefore, the campaign wasn’t very sophisticated.


It’s also possible that the actor used this malware to sell access to backdoored websites on the dark web, which would be an effective way to monetize such a large-scale infection.


Am I affected?
--------------


If you have installed one of the compromised plugins or themes on your site, removing/replacing/updating them won’t uproot any webshells that may have been planted through it.


As such, website administrators are advised to scan their sites for signs of compromise by doing the following:


* Check your wp-includes/vars.php file around lines 146-158. If you see a “wp\_is\_mobile\_fix” function there with some obfuscated code, you’ve been compromised.
* Query your file system for “wp\_is\_mobile\_fix” or “wp-theme-connect” to see if there are any affected files
* Replace your core WordPress files with fresh copies.
* Upgrade the affected plugins and switch to a different theme.
* Change the wp-admin and database passwords.

Jetpack has provided the following YARA rule that can be used to check if a site has been infected and detect both the dropper and the installed webshell.



```
rule accesspress_backdoor_infection
{
strings:
 
   // IoC's for the dropper
   $inject0 = "$fc = str_replace('function wp_is_mobile()',"
   $inject1 = "$b64($b) . 'function wp_is_mobile()',"
   $inject2 = "$fc);"
   $inject3 = "@file_put_contents($f, $fc);"
 
   // IoC's for the dumped payload
   $payload0 = "function wp_is_mobile_fix()"
   $payload1 = "$is_wp_mobile = ($_SERVER['HTTP_USER_AGENT'] == 'wp_is_mobile');"
   $payload2 = "$g = $_COOKIE;"
   $payload3 = "(count($g) == 8 && $is_wp_mobile) ?"
 
   $url0 = /https?:\/\/(www\.)?wp\-theme\-connect\.com(\/images\/wp\-theme\.jpg)?/
 
condition:
 
   all of ( $inject* )
   or all of ( $payload* )
   or $url0
}
```

Backdoors detected in September
-------------------------------


Jetpack first detected the backdoor in September 2021, and soon after, the researchers discovered that threat actors had compromised all free plugins and themes belonging to the vendor.


Jetpack believes that the paid AccessPress add-ons were likely compromised but didn’t test those, so this cannot be confirmed.


Most of the products had likely been compromised in early September from the timestamps.


On October 15, 2021, the vendor removed the extensions from the official download portal until the point of the compromise was located and fixed.


On January 17, 2022, AccessPress released new, “cleaned” versions for all the affected plugins.


However, the affected themes haven’t been cleaned yet, so migrating to a different theme is the only way to mitigate the security risks.


Users of AccessPress plugins and themes can read [Jetpack’s post](https://jetpack.com/2022/01/18/backdoor-found-in-themes-and-plugins-from-accesspress-themes/) for a complete list of the fixed products.


BleepingComputer attempted to contact AccessPress about the compromise, but the contact form is not working.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=P.A.S. Webshell]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Plugins]] [[Accesspress]] [[Jetpack]] [[Wordpress]] [[Websites]] [[Bleeping Computer]]

