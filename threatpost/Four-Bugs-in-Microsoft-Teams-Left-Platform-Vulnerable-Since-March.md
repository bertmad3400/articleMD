# Four Bugs in Microsoft Teams Left Platform Vulnerable Since March
### Attackers exploiting bugs in the “link preview” feature in Microsoft Teams could abuse the flaws to spoof links, leak an Android user’s IP address and launch a DoS attack.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177225
+ Date: 2021-12-22T14:03:05+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/22085506/microsoft-teams-mobile.jpg)

Four vulnerabilities in [Microsoft Teams](https://threatpost.com/microsoft-teams-patch-bypass-rce/158043/), unpatched since March, allowed link spoofing of URLs and opened the door to DoS attacks against Android users, researchers said.


Researchers from Positive Security discovered four bugs in the feature earlier this year and told Microsoft about the issues on March 10. So far, only one of the bugs—a bug allowing attackers to leak Android IP addresses—appears to have been patched by the company, researcher Fabian Bräunlein said [in a blog post](https://positive.security/blog/ms-teams-1-feature-4-vulns) published Wednesday.


Microsoft Teams is a collaboration tool that helps people working in different geographic locations work together online. For this reason, Teams usage of the platform has risen during the pandemic, making it an [increasingly attractive target](https://threatpost.com/microsoft-teams-phishing-office-365/160458/) for threat actors.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)Positive Security researchers “stumbled upon” the vulnerabilities when they were looking for a way to bypass Teams’ Electron’s Same-Origin Policy (SOP), he wrote in the report. SOP is security mechanism of browsers that aims to prevent websites from attacking each other.


Researchers discovered that one potential way to bypass the SOP in Teams is to abuse the link preview feature by letting the client generate a link preview for the target page, and then using the summary text or performing optical character recognition (OCR) on the preview image to extract information.


“In Teams, this preview is actually generated server-side by Microsoft,” something that’s possible because there is no end-to-end encryption present, Bräunlein explained. This means that the feature cannot be abused to leak information from the user’s local network—e.g., the Node.js debug server, he said.


“However, while investigating this feature, I stumbled upon a few unrelated vulnerabilities in its implementation,” Bräunlein said.


Bug Breakdown
-------------


Two of the four bugs discovered affected Microsoft Teams being used on any device and allow for server-side request forgery (SSRF) and spoofing, researchers said. The other two—dubbed “IP Address Leak” and “Denial of Service aka Message of Death” by researchers—affect only Android users.


The SSRF vulnerability allowed researchers to leak information from Microsoft’s local network and was discovered when Bräunlein tested the /urlp/v1/url/info endpoint for SSRF, he said.


“The URL is not filtered, leading to a limited SSRF (response time, code, size and open graph data leaked), which can be used for internal portscanning and sending HTTP-based exploits to the discovered web services,” Bräunlein explained.


Attackers can use the spoofing bug to beef up phishing attacks or hide [malicious links](https://threatpost.com/single-malicious-gif-opened-microsoft-teams-to-nasty-attack/155155/) in content sent to users, he said. This can be done by setting the preview link target “to any location independent of the main link, preview image and description, the displayed hostname or onhover text,” according to the post.


To abuse the Android DoS bug, a threat actor can send a message to someone using Teams via its Android app that includes a link preview with an invalid preview link target. This will crash the app continuously when the user tries to open the chat/channel with the malicious message, basically blocking users out of the chat or channel, Bräunlein explained.


Finally, attackers can use IP address leak bug—the only one Microsoft appears to have remedied—to intercept messages that include a link preview to point the thumbnail URL to a non-Microsoft domain. This is possible in link previews in which the backend fetches the referenced preview thumbnail and makes it available from a Microsoft domain, Bräunlein said.


“The Android client does not check the domain/does not have a CSP restricting the allowed domains and loads the thumbnail image from any domain,” he explained.


Microsoft’s Response
--------------------


Microsoft first responded to Positive Security on March 12, two days after its disclosure, and the two parties went “back-and-forth” for a couple of weeks on details of the spoofing issue.


Between March 25 and April 14, the company responded conclusively to each of the individual issues raised and eventually gave researchers the go-ahead to reveal its findings publicly, according to the post. Microsoft Wednesday did not immediately return request for comment on Positive Security’s report.


On March 25, the company decided not to patch the DoS and SSRF bugs, according to Bräunlein. Microsoft said it determined that the DoS bug “does not require immediate security service” because it is of  “low severity for temporary DoS that requires restart of application,” according to the post. Microsoft added that it would consider fixing the issue in a later version of the product.


In terms of the SSRF bug, Microsoft gave no reasoning for closing the case without a patch, saying only that the company “will not be fixing this vulnerability in the current version,” according to Positive Security.


Microsoft also declined to patch the Android IP address leak on April 4, determining that the issue “does not pose an immediate threat that requires urgent attention due to the general data sensitivity of the IP address data.”


The company did, however, share the report with the team responsible for the product, and a retest of all the bugs that Positive Security conducted on Dec. 15 demonstrated that the issue appears to have been patched, Bräunlein wrote.


On April 14, Microsoft also declined to address the URL spoofing issue, concluding that it also does not pose an immediate threat “because once the user clicks on the URL, they would have to go to that malicious URL which would be a giveaway that it’s not the one the user was expecting,” according to Positive Security.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Bräunlein]] [[Teams]] [[Android]] [[Ssrf]] [[Url]] [[Ip]] [[ThreatPost]]

