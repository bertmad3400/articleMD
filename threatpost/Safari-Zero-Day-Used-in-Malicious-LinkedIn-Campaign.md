# Safari Zero-Day Used in Malicious LinkedIn Campaign
### Researchers shed light on how attackers exploited Apple web browser vulnerabilities to target government officials in Western Europe. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167814)
+ Date: July 15, 2021  7:04 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/15070346/linkedin_generic.jpg)
Threat actors used a Safari zero-day flaw to send malicious links to government officials in Western Europe via LinkedIn before researchers from Google discovered and reported the vulnerability.


That’s the word from researchers from Google Threat Analysis Group (TAG) and Google Project Zero, who Wednesday [posted a blog](https://blog.google/threat-analysis-group/how-we-protect-users-0-day-attacks/) shedding more light on several zero-day flaws that they discovered so far this year. Researchers in particular detailed how attackers exploited the vulnerabilities—the prevalence of which are on the rise–before they were addressed by their respective vendors.


TAG researchers discovered the Safari WebKit flaw, tracked as [CVE-​2021-1879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-1879), on March 19. The vulnerability allowed for the processing of maliciously crafted web content for universal cross site scripting and was addressed by Apple in [an update](https://support.apple.com/en-us/HT212256) later that month.



Before the fix, researchers assert Russian-language threat actors were exploiting the vulnerability in the wild by using LinkedIn Messaging to send government officials from Western European countries malicious links that could collect website-authentication cookies, according to the post by Maddie Stone and Clement Lecigne from Google TAG.


“If the target visited the link from an iOS device, they would be redirected to an attacker-controlled domain that served the next-stage payloads,” they wrote.


The exploit, which targeted iOS versions 12.4 through 13.7, would turn off [Same-Origin-Policy](https://en.wikipedia.org/wiki/Same-origin_policy) protections on an infected device to collect authentication cookies from several popular websites–including Google, Microsoft, LinkedIn, Facebook and Yahoo–and then send them via WebSocket to an attacker-controlled IP, researchers wrote. The victim would need to have a session open on these websites from Safari for cookies to be successfully exfiltrated.


Moreover, the campaign targeting iOS devices coincided with others from the same threat actor—which Microsoft has identified as Nobelium–targeting users on Windows devices to deliver Cobalt Strike, researchers wrote. Security firm Volexity described one of these attacks [in a report](https://www.volexity.com/blog/2021/05/27/suspected-apt29-operation-launches-election-fraud-themed-phishing-campaigns/) posted online in May, the researchers added.


Nobellium is believed to be a Russia-based threat group responsible for the [expansive cyber-espionage SolarWinds](https://threatpost.com/feds-russia-culprit-solarwinds/162785/) campaign, which affected numerous U.S. government agencies and tech companies, including Microsoft.


**Other Zero-Day Attacks**
--------------------------


Google researchers also linked three additional zero-day flaws they identified this year to a commercial surveillance vendor, according to [Google TAG’s Shane Huntley](https://twitter.com/ShaneHuntley/status/1415340345500463113). Two of those vulnerabilities–[CVE-2021-21166](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21166) and [CVE-2021-30551](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30551)—were found in Chrome, and one, tracked as [CVE-2021-33742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33742), in Internet Explorer.


CVE-2021-21166 and CVE-2021-30551, two Chrome rendered remote-code execution (RCE) flaws, were identified separately but later believed to be used by the same actor, researchers wrote in the blog. Google researchers discovered the former in February and the latter in June.


“Both of these 0-days were delivered as one-time links sent by email to the targets, all of whom we believe were in Armenia,” Stone and Lecigne wrote. “The links led to attacker-controlled domains that mimicked legitimate websites related to the targeted users.”


When prospective victims clicked the link, they were redirected to a webpage that would fingerprint their device, collect system information about the client, and generate ECDH keys to encrypt the exploits, researchers wrote. This info—which included screen resolution, timezone, languages, browser plugins, and available MIME types—would then be sent back to the exploit server and used by attackers to decide whether or not an exploit should be delivered to the target, they said.


Researchers also identified a separate campaigned in April that also targeted Armenian users by leveraging CVE-2021-26411, an RCE bug found in Internet Explorer (IE). The campaign loaded web content within IE that contained malicious Office documents, researchers wrote.


“This happened by either embedding a remote ActiveX object using a Shell.Explorer.1 OLE object or by spawning an Internet Explorer process via VBA macros to navigate to a web page,” Stone and Lecigne explained.


At the time, researchers said they were unable to recover the next-stage payload, but successfully recovered the exploit after discovering an early June campaign from the same actors. Microsoft patched the flaw later that month, they said.


**Why There is an Increase in Zero-Days?**
------------------------------------------


All in all, security researchers have identified 33 [zero-day flaws](https://threatpost.com/kaseya-patches-zero-days-revil-attacks/167670/) so far in 2021, which is 11 more than the total number from 2020, according to the post.


While that trend reflects an increase in the number of these types of vulnerabilities that exist, Google researchers “believe greater detection and disclosure efforts are also contributing to the upward trend,” they wrote.


Still, it’s highly possible that attackers are indeed using more [zero-day exploits](https://threatpost.com/zero-day-wipe-my-book-live/167422/) for a few reasons, researchers noted. One is that the increase and maturation of security technologies and features means attackers also have to level up, which in turn requires more [zero-day vulnerabilities](https://threatpost.com/solarwinds-hotfix-zero-day-active-attack/167704/) for functional attack chains, they said.


The growth of mobile platforms also has resulted in an increase in the number of products that threat actors want to target—hence more reason to use zero-day exploits, researchers observed. Perhaps inspired by this increase in demand, commercial vendors also are selling more access to zero-days than in the early 2010s, they said.


Finally, the maturation of security protections and strategies also inspires sophistication on the part of attackers as well, boosting the need for them to use zero-day flaws to convince victims to install malware, researchers noted.


“Due to advancements in security, these actors now more often have to use 0-day exploits to accomplish their goals,” Stone and Lecigne wrote.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Google]] [[zero-day]] [[Lecigne]] [[Microsoft]] [[LinkedIn]] [[attacker-controlled]] [[websites]] [[ThreatPost]]
