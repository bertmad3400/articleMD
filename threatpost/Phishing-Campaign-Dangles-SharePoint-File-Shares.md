# Phishing Campaign Dangles SharePoint File-Shares
### Attackers spoof sender addresses to appear legitimate in a crafty campaign that can slip past numerous detections, Microsoft researchers have discovered.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168356)
+ Date: August 4, 2021  10:44 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/04/02113430/Phishing-Lure-Fishing-Lure.jpg)
Attackers are using spoofed sender addresses and Microsoft SharePoint lures in a new phishing campaign that is “sneakier than usual” and can slip through the usual security protections in its aim to fool people into giving up their credentials, Microsoft researchers discovered.


Microsoft Security Intelligence researchers discovered the campaign targeting organizations that use Microsoft Office 365 by using the file-sharing aspect of SharePoint, they revealed in a [tweet](https://twitter.com/MsftSecIntel/status/1421232634357714947) on Tuesday.


The campaign spoofs display sender addresses that contain the target usernames and domains, as well as display names “that mimic legitimate services to try and slip through email filters,” researchers said.



Attackers send emails that “use a Sharepoint lure in the display name as well as the message,” researchers said. “This campaign is active with various lure themes,” they [tweeted](https://twitter.com/MsftSecIntel/status/1421232644566646785).


The email alerts a recipient to a file-share request from someone who appears to be a colleague that they may have missed and includes a link to a phishing page. To appear authentic, the file is said to contain some type of legitimate business content, such as staff reports, bonuses or price books, researchers noted.


If a user takes the bait, he or she is eventually directed to a phishing page that requires them to sign into Office 365 with their legitimate credentials, Microsoft said.


Given its widespread use among many enterprise and business customers, the SharePoint collaboration platform is [a popular target](https://threatpost.com/sharepoint-phish-ransomware-attacks/165671/) for threat actors.


In particular, its file-sharing capability, combined with spoofing, is a particularly effective way to trick victims into revealing credentials, observed Dora Tudor, a cyber security enthusiast with [Heimdal Security](https://heimdalsecurity.com/blog/).


“When it comes to email spoofing you might think that if the received email came from a trusted entity you can rely on it to be safe but, unfortunately, any links existing in the email may end up infecting you with malware,” she noted in [a blog post](https://heimdalsecurity.com/blog/new-phishing-attack-uses-compromised-sharepoint-website-as-a-lure/?web_view=true) Tuesday.


**Suspicious Signs**
--------------------


Despite the overall craftiness of this latest campaign, there are some telltale signs that something is amiss, according to Microsoft.


For one, the original sender addresses, which use variations of the word “referral,” also use various top-level domains, including the domain com[.]com, which is popularly used by phishing campaigns for spoofing and typosquatting, they noted [on Twitter](https://twitter.com/MsftSecIntel/status/1421232635502682118).


Other clues to the malicious intent of the campaign are found in its use of URLs that lead potential victims to the phishing page for entering their credentials, according to researchers.


Attackers use two URLs with malformed HTTP headers, they said. The primary phishing URL is a Google storage resource that directs to an AppSpot domain requiring the user to sign in “before finally serving another Google User Content domain with an Office 365 phishing page,” researchers said.


The second URL used in the campaign is found within the notification settings. This one leads to a compromised SharePoint site “that the attackers use to add legitimacy to the attack,” according to Microsoft.


Both URLs require potential victims to sign in to move on to the final page, “bypassing many sandboxes” on the way, [researchers said](https://twitter.com/MsftSecIntel/status/1421232642033287171).


Researchers provided [a query string on GitHub](https://twitter.com/MsftSecIntel/status/1421232644566646785) that can be run through Microsoft 365 Defender to flag any emails from the campaign that may have slipped past other gateways, they said.


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[phishing]] [[said.]] [[Microsoft]] [[credentials,]] [[SharePoint]] [[URLs]] [[ThreatPost]]
