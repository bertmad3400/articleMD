# Canopy Parental Control App Wide Open to Unpatched XSS Bugs
### The possible cyberattacks include disabling monitoring, location-tracking of children and malicious redirects of parent-console users.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175384)
+ Date: October 6, 2021  5:27 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/06/22120601/kids-apps-e1624377972972.jpg)
Canopy, a parental control app that offers a range of features meant to protect kids online via content inspection, is vulnerable to a variety of cross-site scripting (XSS) attacks, according to researchers.


The attacks could range from a sneaky kid disabling the monitoring to a much more serious third-party attack delivering malware to parental users.


Canopy offers sexting prevention, on-device photo protection (through image filtering), screen-time monitoring, child communication alerts for parents, smart content filtering for weeding out inappropriate websites, plus, for the parents, remote device management and the ability to control the use of the applications and websites their child uses.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


To perform such wonders, Canopy uses an artificial intelligence engine and VPN filtering – plus a healthy number of device permissions.


“The installation process involved authorizing a wide set of permissions including accessibility support, the ability to draw on top of other apps, installing a root CA and configuring a VPN,” explained Craig Young, security researcher at Tripwire, in a [report](https://www.tripwire.com/state-of-security/featured/analysis-of-a-parental-control-system/) published on Tuesday. “The app can also (optionally) act as a device administrator to prevent app removal…This privileged access can introduce considerable risk to the security of protected devices and the privacy of the children using those devices.”


**Rife with XSS Issues**
------------------------


It turns out that he’s not wrong to be concerned. Looking into the Android version of the app, Young discovered several opportunities to mount XSS attacks, which occur when malicious scripts are injected into otherwise benign and trusted websites.


That injection is usually carried out by entering malicious code into a web response or comment field and hitting enter, where the payload is then sent to a web server. Usually, these responses are validated on the server side so that malicious scripts are blocked. But in Canopy’s case, those checks are lacking in several areas, Young found.


Once a website is thus compromised, any visitor to the site is potentially a victim, either from a drive-by attack in a stored XSS scenario, or if the target can be convinced to click a link in a reflected XSS attack.


**Sneaky-Kid Concerns**
-----------------------


The first set of problems has to do with the potential for a wild child to get around the app’s protective gaze.


When Young tested a core Canopy function – blocking bad websites – he found that he was greeted with a block-notification page when he attempted to load a prohibited site on a test Android device. That notification page has a button allowing the child to ask his or her parents for access to the requested page anyway.


Young clicked the button from the test device but appended this response with a simple XSS payload script that creates a JavaScript pop-up on the parental website, to see what would happen. When he went to the portal, sure enough, the pop-up was there.


Then, he found the XSS worked in the opposite direction.


“I decided to deny the request and again insert an XSS payload as explanation text,” Young explained. “The protected phone received a notification about the response. When I opened this notification, I was again greeted with my XSS pop-up.”


The vulnerability arises because the system is failing to sanitize user inputs. The input field allows 50 characters, Young found, “which was plenty to source an external script.”


He said there are multiple ways to exploit the issue.


“An attacker (e.g. the monitored kid) can embed an attack payload within an exception request. Although there may be a wide range of ways a clever kid could abuse this vulnerability, the most obvious would be to automatically approve a request,” he said. “My first test was a payload to automatically click to approve the incoming request. This worked well, and I quickly got another payload working to automatically pause monitoring protection.”


**Canopy Attacks by Outsiders**
-------------------------------


While a variety of child-to-parent attacks could be carried out by a kid with some scripting knowledge, Young also found that more sinister offensives could be mounted.


For instance, he observed that the URL value in the block-notification page query (indicating which website is being denied) is displayed on the main page of the parent dashboard.


“I did a quick test of adding a script tag into the URL and loaded up the parent console,” he said, adding that he needed to play around with the syntax of the script for a while before getting a payload to “fire.” Now, “the JavaScript executed when loading the main page of the parent dashboard. We now can submit an exception request which takes control of the Canopy app when the parent simply logs in to check on the monitored devices.”


Further, because the attack involves a crafted URL being blocked, it becomes possible for attacks to come from completely external third-party sources, he noted. An attacker need only to establish a likely-to-be-blocked website with that appended script in its URL and convince a child to try to access it. When the notification about the access request goes to the parent console, the parents monitoring the account would become victims of the malicious script.


“Unfortunately, the attack surface for this vulnerability is quite a bit more substantial than what was discussed earlier with request explanation text,” Young said.


But that’s not all. It turns out that the Canopy API design could allow an external attacker to directly inject an XSS payload into a parent-account webpage by guessing the parent account ID. That would open the door to redirections to ads, exploits, malware and more. And most sinisterly, an attacker could hijack access to the parental control app itself, installed on the kid’s phone, and pull GPS coordinates from protected devices on the account.


“The account IDs are short numeric values, so it seems quite plausible that an attacker could seed the attack payload on every single parent account by simply issuing a block exception request for each ID value in sequence,” Young explained.


**No Patches for the Worst Canopy Attacks**
-------------------------------------------


Young said that he reached out to Canopy by phone and by email repeatedly, with little response, thus prompting his disclosure of the issues. The only fix the developer issued was to prevent the child-led attacks, he added.


“[Canopy] failed to do anything to protect against the parent to child XSS or XSS through the URL of a blocked page request before becoming unresponsive,” he said. “Canopy needs to implement sanitization of all user-input fields but has failed to do so. After repeated attempts to work with the vendor, we are publishing this report (with some details removed) so that others can learn from it and act accordingly.”


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





#### Tags:
[[XSS]] [[URL]] [[“The]] [[attacks,]] [[website]] [[said.]] [[ThreatPost]]
