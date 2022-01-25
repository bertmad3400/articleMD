# Segway Hit by Magecart Attack Hiding in a Favicon
### Visitors who shopped on the company's eCommerce website in January will likely find their payment-card data heisted, researchers warned.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177971
+ Date: 2022-01-25T20:35:56+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/25150639/segway-city-tour-scaled-e1643141220954.jpeg)

Segway, maker of the iconic – and much-spoofed – personal motorized transporter familiar from guided city tours everywhere, has been serving up a nasty credit-card harvesting skimmer via its website – likely linked to Magecart Group 12.


That’s according to Malwarebytes, which noted that “We already have informed Segway so that they can fix their site, but are publishing this blog now in order to raise awareness.” Segway, which is now owned by Chinese company Ninebot, did not immediately return a request for confirmation that the site is cleaned.


Magecart is a loose umbrella term encompassing various affiliated groups of financially motivated cybercriminals who all employ a similar skimming malware to harvest information – in particular payment-card information – that shoppers enter into checkout pages on eCommerce websites. Magecart 12 is one of the [latest iterations](https://threatpost.com/magecart-server-side-itactics-changeup/166242/) of the group, known for consistently switching up its tactics.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Typically, across Magecart groups, the skimmers are injected into unsuspecting merchant websites be exploiting vulnerable versions of popular eCommerce platforms, such as outdated iterations of Magento or WooCommerce. That’s what researchers believe may have happened here.


“While we do not know how Segway’s site was compromised, an attacker will usually target a vulnerability in the CMS itself or one of its plugins,” the team explained, in a [Monday posting](https://blog.malwarebytes.com/threat-intelligence/2022/01/segway-store-compromised-with-magecart-skimmer/). “The hostname at store.segway[.]com is running Magento, the popular content management system (CMS) used by many eCommerce sites and also a favorite among Magecart threat actors.”


In terms of this campaign’s specific characteristics, Malwarebytes analysts estimated that the skimmer has been active since about Jan. 6, and that it has so far exposed victims in the United States (which makes up 55 percent of site visitors), Australia (39 percent), Canada (3 percent), the UK (2 percent) and Germany (1 percent).


“The compromise of the Segway store is a reminder that even well-known and trusted brands can be affected by Magecart attacks,” Malwarebytes noted. “While it usually is more difficult for threat actors to breach a large website, the payoff is well worth it.”


**Hiding Inside a Favicon**
---------------------------


Researchers debugged the skimmer’s loader and was able to reveal its command-and-control (C2) URL, booctstrap[.]com, which is a known skimmer domain that’s been active since November. They also observed a piece of JavaScript, disguised as a file named “Copyright,” which isn’t inherently malicious itself but which dynamically loads the skimmer. The approach means that the skimmer is invisible to anyone inspecting the HTML source code, they explained.


Also of interest is the fact that the threat actors are embedding the skimmer inside a favicon.ico file. Favicons are small icon images that link to other websites.


“If you were to look at it, you’d not notice anything because the image is meant to be preserved,” according to the posting. “However, when you analyze the file with a hex editor, you will notice that it contains JavaScript starting with an eval function.”


Uriel Maimon, senior director of emerging technologies at cybersecurity company PerimeterX, noted that this type of innovation is becoming more common.


“Magecart attackers continue get more creative with their techniques in order to evade detection, especially given advancements in security solutions over the years,” he said via email. “By hiding the skimmer script inside a favicon pretending to display the site’s copyright, neither manual code reviews, static code analysis or scanners could have detected this easily.”


**Assume Magecart is Coming After Your eCommerce Site**
-------------------------------------------------------


The skimmer itself is a [known quantity](https://blog.sucuri.net/2020/04/web-skimmer-with-a-domain-name-generator.html), researchers noted – it’s cropped up in campaigns since at least 2020, including those carried out by Magecart 12.


Further, the Magecart cybercriminal group overall has been operating for several years and has skimmed from many large organizations, stealing names, emails, credit-card information and more, all of which sells on the Dark Web for profit. Their activity is vociferous: A recent Risk IQ report in December [found that](https://www.riskiq.com/blog/external-threat-management/woocommerce-magecart/) a Magecart attack on a website happens once every 16 seconds.


Because of all of that, eCommerce merchants should assume they’re being targeted, noted James McQuiggan, security awareness advocate at KnowBe4.


“In this situation, cybercriminals…have about sixteen lines of code injected into the application for credit-card processing,” McQuiggan said via email. “Organizations must monitor web traffic for applications sending data to unknown locations. A robust change-management program to monitor code changes to sites and third-party products can reduce the risk of a successful attack and maintain a solid cyber resiliency.”


E-commerce businesses could also use a a real-time monitoring solution that detects access to sensitive fields and attempts to exfiltrate personally identifiable information from the client side, Maimon said.


“It is important that users of Magento understand the need to disrupt the web attack lifecycle by stopping the theft of account and identity information from their site, and implement a solution to help do that,” he explained. “Taking action before it is too late will also help prevent damage to the brand’s reputation as well as limit potential liability for non-compliance.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Germany]] [[victim.continent.name=Europe]] [[victim.country.name=Canada]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Magecart]] [[Segway]] [[Ecommerce]] [[Percent)]] [[Credit-card]] [[Website]] [[Malwarebytes]] [[Websites]] [[Magento]] [[ThreatPost]]

