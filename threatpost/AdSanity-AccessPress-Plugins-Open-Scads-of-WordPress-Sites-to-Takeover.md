# AdSanity, AccessPress Plugins Open Scads of WordPress Sites to Takeover
### A critical security bug and a months-long, ongoing supply-chain attack spell trouble for WordPress users.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177932
+ Date: 2022-01-25T16:22:49+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2019/04/12095249/WordPress-patch-dlya-XSS-700x412.jpg)

The WordPress content management system (CMS) is offering admins more headaches this week, thanks to a pair of disparate but concerning security problems in add-ons for the platform.


The first issue affects the WordPress AdSanity plugin. It’s a critical security vulnerability that could allow remote code execution (RCE) and full site takeovers.


The second problem concerns a classic supply-chain attack, in which cybercriminals compromised 40 themes and 53 plugins belonging to AccessPress Themes in order to inject them with a webshell. Thus, any website that installed one of the compromised add-ons is also open to RCE and full takeover.


**AdSanity Plugin Allows RCE**
------------------------------


AdSanity is a light ad rotator plugin for WordPress. It allows the user to create and manage ads shown on a website as well as keep statistics on views and clicks, all through a centralized dashboard.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The bug, which carries a concerning 9.9 out of 10 rating on the CVSS vulnerability-severity scale, “could allow a low-privilege user to perform arbitrary file upload, remote code execution and stored cross-site scripting attacks,” according to researchers at the Ninja Technologies Network.


The issue (no CVE was assigned) arises thanks to broken access control, they explained in a [Tuesday writeup](https://blog.nintechnet.com/critical-vulnerability-in-wordpress-adsanity-plugin/). When users place an ad on a website, they upload a .ZIP file containing the materials. That process is managed inside the “adsanity/views/html5-upload.php” script, using the ajax\_upload function.


“That function is used to upload and extract the content of a .ZIP archive into the ‘wp-content/uploads/adsanity/{post\_id}/’ folder,” according to NinTechNet. “It only has a security nonce, accessible to any user with Contributor or above privileges, and a simple check to ensure there’s an index.html file inside the archive.”


In WordPress, the Contributor role’s permissions [are restricted](https://themeisle.com/blog/wordpress-user-roles/) to only three tasks – reading all posts, and deleting or editing their own posts. Contributors can’t publish new posts or upload media files, and so these permissions are usually assigned to one-time or limited-role content creators, freelancers and others who are less trusted to monkey around with a company’s website.


Because of the bug, though, a malicious Contributor can gain full access to a website’s backend through the AdSanity plugin. An exploit can be achieved by simply adding an index.php script inside a .ZIP archive to be uploaded, researchers noted.


“Its code will be loaded by the iframe instead of the index.html file, and executed inside the metabox each time a user accesses the ads manager in the backend,” they explained. “If the blog has a .htaccess file to prevent PHP code execution inside the /uploads/ folder, the attacker can easily override that protection by uploading another .htaccess [file].”


They added, “Additionally, the attacker can upload files with JavaScript code too, which could be used to target the administrator reviewing the post.”


The vulnerability was fixed in version 1.8.2, but after updating, site owners should still review user permissions and access to the plugin, warned NinTechNet.


“The new version doesn’t allow Contributor users to upload files but still allow Author+ users to do so, therefore if you have Author users registered on your blog, you may exercise extreme caution,” researchers explained.


**AccessThemes Backdoor Bonanza**
---------------------------------


Meanwhile, security researchers from Jetpack, while doing forensics on a compromised website, stumbled across a backdoored theme from AccessPress Themes that would allow remote attackers to execute code.


Jetpack researchers delved into the company’s library and quickly discovered that when it came to the free offerings, “all the themes and most plugins…were injected with a backdoor,” which would allow attackers to take full control of any website that has one of the compromised add-ons installed.


AccessPress Themes provides multiple free and paid themes and plugins that can be used to customize WordPress-powered sites – a whopping 64 themes and 109 plugins overall, collectively accounting for 360,000 installs, according to [its website](https://accesspressthemes.com/).


Unfortunately, the issue appears to be ongoing: “Most of the plugins have since been updated,” according to Jetpack’s advisory, [issued last week](https://jetpack.com/2022/01/18/backdoor-found-in-themes-and-plugins-from-accesspress-themes/). “However, the affected themes have not been updated, and are pulled from the WordPress.org theme repository.”


Of note, the issue affects offerings downloaded directly from the developer’s website; any AccessPress Themes offerings downloaded directly from WordPress.org are clean, researchers noted.


### **A Cookies-Based Webshell**


The infected extensions contain a dropper for a webshell, which was injected into the “inital.php” file,  located in the main plugin or theme directory.


“When run, it installs a cookie-based webshell in ‘wp-includes/vars.php,'” researchers explained. “The shell is installed as a function just in front of the ‘wp\_is\_mobile()’ function with the name of ‘wp\_is\_mobile\_fix().’ This is presumably to not arouse suspicion to anybody casually scrolling through the ‘vars.php’ file.”


Once the shell is installed, the dropper will load a remote image to a command-and-control (C2) server containing the URL of the infected site and information about which theme it uses. Then, it removes the dropper source file to avoid detection, according to the analysis.


The C2 can activate the webshell to execute code by sending a request with the user agent string “wp\_is\_mobile,” along with eight specific cookies. The backdoor then pieces together and executes a payload from these supplied cookies.


The researchers also spotted a second, slightly older variant of the backdoor directly embedded in the theme/plugin’s “functions.php” file, they said. However, in all cases, the offerings have all been compromised since September.


A full list of themes and versions compromised by the attack is available at the bottom of Jetpack’s [original advisory](https://jetpack.com/2022/01/18/backdoor-found-in-themes-and-plugins-from-accesspress-themes/), along with patch status.


Affected users should upgrade to a fixed version, if available – and if no safe version is available, they can replace it with the latest version from WordPress.org, researchers said.


“Please note that this does not remove the backdoor from your system, so in addition you need to reinstall a clean version of WordPress to revert the core file modifications done during installation of the backdoor,” the added.


**WordPress: A Juicy Target & Risk Center**
-------------------------------------------


WordPress plugins and themes continue to be [plagued with vulnerabilities](https://threatpost.com/wordpress-insecure-plugin-rest-api/177866/) – a state of affairs that’s somewhat baked into the ecosystem, noted Zach Jones, senior director of detection research at NTT Application Security.


“WordPress and its ecosystem sprang out of a DIY website movement that for better, and sometimes worse, is very open and accessible,” he told Threatpost. “Anyone can write a WordPress plugin and share it with the world. WordPress and its underlying language, PHP, are often an entry-point into web technologies for many adventurous and entrepreneurial self-starters, which is a boon to the ecosystem, but a challenge to its security. I’m speaking specifically from personal experience here as WordPress was a part of my early exposure to developing websites professionally, and I personally created (thankfully not published) WordPress plugins that in hindsight were riddled with vulnerabilities.”


And indeed, the open-source nature of the WordPress world has attracted vast numbers of developers, with varying degrees of security chops, pointed out Yehuda Rosen, senior software engineer at nVisium.


“Anyone can create and upload their own plugins, themes, and more — with no credentials or experience necessary to get started,” he told Threatpost. “There are more than 55,000 plugins available for anyone to download from WordPress.org right now, as well as over 9,000 themes — the vast majority written by coders who have little experience with security best practices.”


He added, “As a result, you now have a giant footprint with potentially vulnerable code being deployed to a massive amount of websites — which, of course, makes the WordPress ecosystem a very juicy target to would-be attackers.”


That also means that a dedicated attacker will almost certainly find vulnerabilities in WordPress plugins if they go to look for them.


“So, even if only 10 percent of plugins had security issues, the true number might be significantly higher with thousands of vulnerable themes,” Rosen said. “The open-source nature, along with the sheer number of deployments, virtually guarantees that security issues will be numerous.”


Even so, WordPress has been cited as powering more than 40 percent of all websites, totaling hundreds of millions of websites. And its reach actually extends even further, Rosen pointed out.


“WordPress isn’t just a blog software. Automattic – the company behind WordPress – has been silently taking over more areas of the web for years,” he said. “Some areas include spam prevention (Akismet), e-commerce (WooCommerce), social networking (BuddyPress), and even more seemingly random areas like job recruitment (WPJobBoard) or podcasting (Pocket Casts). All the above properties are built with WordPress as a core, with some calling it the most important software project on the internet.”


With that kind of scale, securing all of that infrastructure may seem daunting. Roy Horev, co-founder and CTO at Vulcan Cyber, noted that every site administrator should pitch in and make sure to perform the security basics.


“Anybody running WordPress should be savvy enough to know to stay on top of their security updates,” he told Threatpost. “Any time a technology is as pervasive as WordPress it becomes a popular target for hackers because they can count on a percentage of administrators not staying on top of updates for both the core platform and WordPress plugins. We’d recommend running a security audit of WordPress and its plugins at least quarterly, and responsibly updating the software as soon as new security releases become available.”


NTT’s Jones added, “From the perspective of corporate usage or WordPress, the big story here is that many organizations don’t do needed diligences to up-level WordPress, especially in terms of security. When choosing to use any framework or third-party software like a plugin, careful diligence must be undertaken to confirm that the additional risk introduced is known and controlled as part of an effective overall application security program.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=P.A.S. Webshell]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Dili]] [[victim.country.name=East Timor]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Wordpress]] [[Plugins]] [[Website]] [[Plugin]] [[Adsanity]] [[Accesspress]] [[Webshell]] [[Jetpack]] [[Wordpress.org]] [[Threatpost]] [[ThreatPost]]

