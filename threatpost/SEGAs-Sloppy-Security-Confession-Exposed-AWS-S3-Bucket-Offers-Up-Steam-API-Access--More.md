# SEGA's Sloppy Security Confession: Exposed AWS S3 Bucket Offers Up Steam API Access & More
### SEGA's disclosure underscores a common, potentially catastrophic, flub — misconfigured Amazon Web Services (AWS) S3 buckets.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177352
+ Date: 2022-01-04T20:49:39+00:00
+ Author: Becky Bracken


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/04154548/Sega.jpg)

Gaming giant SEGA Europe recently discovered that its sensitive data was being stored in an unsecured Amazon Web Services (AWS) S3 bucket during a cloud-security audit, and it’s sharing the story to inspire other organizations to double-check their own systems.


Researcher Aaron Phillips with VPN Overview worked with [SEGA Europe to secure the exposed data](https://vpnoverview.com/news/sega-europe-security-report/). Phillips explained SEGA’s disclosure is intended to help the wider cybersecurity community improve their own defenses.


“When vulnerabilities are discovered, information and knowledge sharing is of crucial importance,” Phillips wrote. “Organizations can learn from each other’s case studies and experiences, which enables them to better protect themselves and their users.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Why give the attackers the benefit of keeping this very common cloud security mistake a secret?


“In addition, it is much more desirable that a vulnerability is discovered and shared responsibly by a security researcher than by a hacker with criminal intention,” Phillips added.


**Steam Keys, SNS and CDNs Left Exposed**
-----------------------------------------


The laundry list of SEGA’s potentially exposed data is nauseating — API keys, internal messaging systems, cloud systems, user data and more.


The VPN Overview report provided a detailed disclosure that the exposed bucket held “multiple” sets of AWS keys, which could have provided malicious access to all of SEGA Europe’s cloud services.


In addition, the keys to SEGA’s Europe’s MailChimp and Steam API keys were left unprotected, meaning attackers could have sent out communications through SEGA Europe’s account, the report said.


The exposed S3 bucket could have also allowed access to both the simple notification service (SNS) used by the company’s IT team to communicate as well as 531 of SEGA Europe’s content delivery networks (CDNs), the team found.


“Often, third-party websites will link to a company’s CDN for an official version of an image or file,” the report added. “That creates the potential for a large secondary impact.”


The unsecured bucket also contained the sensitive data on “hundreds of thousands” of members of the Football Manager forums, Phillips added.


So far, “there are no indications malicious third parties accessed the sensitive data or exploited any of the mentioned vulnerabilities prior to the security researchers restricting access to the bucket,” Phillips emphasized.


Researchers found 26 vulnerable, public-facing SEGA domains that would have allowed attackers to upload malicious files and alter content, the report said. The analysts were also able to access files on three SEGA CDNs.


**Gaming Companies’ Data: ‘Treasure Troves’**
---------------------------------------------


That amount of sensitive data falling into the hands of a malicious actor could easily prove catastrophic for any organization, but Hank Schless with Lookout explained to Threatpost gaming companies continue to be of particular interest to attackers.


“Gaming companies possess a treasure trove of personal data, development information, proprietary code, and payment information that is highly valuable to threat actors,” Schless added. “With data [privacy laws like CCPA](https://threatpost.com/californias-tough-new-privacy-law-and-its-biggest-challenges/151682/) and GDPR, gaming companies need to be sure their data is protected as people from all over the world play their games.”


Indeed, leading companies like [Steam](https://threatpost.com/steam-gaming-delivering-malware/166784/), [Among Us](https://threatpost.com/tiktok-gamer-targets-among-us-steam/175546/), [Riot Games](https://threatpost.com/riot-games-job-fraud/176950/) and others have been hijacked and used to lure unsuspecting gamers into all sorts of scams. Phillips wrote he hopes this report demonstrates how something as simple as a misconfigured S3 bucket can cause catastrophic harm to an organization.


“This cybersecurity report should serve as a wake-up call for businesses to assess their cloud security practices,” Phillips added. “We hope other organizations follow SEGA’s lead by examining and closing apparent vulnerabilities before they are exploited by cybercriminals.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


*Cover image source: [Valve and SEGA](https://store.steampowered.com/curator/36333614/sale/SEGA60th).*





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Sega]] [[Phillips]] [[Cloud]] [[S3]] [[Cybersecurity]] [[ThreatPost]]

