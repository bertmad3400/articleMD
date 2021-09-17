# Porn Problem: Adult Ads Persist on US Gov’t, Military Sites
### Cities, states, federal and military agencies should patch the Laserfiche CMS post-haste, said the security researcher whose jaw dropped at 50 sites hosting porn and Viagra spam. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174794)
+ Date: September 17, 2021  1:16 pm
+ Author: Lisa Vaas


## Article:
U.S. military and government website subdomains have a sticky problem: They’re “quite vulnerable” to blackhat SEO tactics that result in persistent redirects to spammy Viagra ads and porn videos.


An example is one that showed up on a dot.mil subdomain on the Minnesota National Guard site (you can have your own fun searching on terms such as “buy generic and brand Viagra” on dot-gov and dot-mil sites: Plenty of these ads are still out there) that asks this question:



> How are erections measured while a man sleeps? Two small rings are placed around the penis, one at the tip and one at the base.
> 
> 


Edwards told [Motherboard’s Vice](https://www.vice.com/en/article/pkb5qy/why-government-and-military-sites-are-hosting-porn-and-viagra-adsovernm) – which first reported his findings – that the reason a lot of government websites are hosting these spammy ads is that an array of government agencies are using the same software: one that, it turns out, has a now-patched vulnerability that allowed third parties to push files to these sites without the site owners’ permission.


It’s called [Laserfiche](https://www.laserfiche.com/), and it’s made by a government software provider that produces content management systems and sells them to the Army, the Navy, the FBI and more, according to public procurement records such as this one for the City of Fort Worth ([PDF](https://publicdocuments.fortworthtexas.gov/CSODOCS/doc/191751/Page2.aspx?repo=City-Secretary&dbid=0)).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“This vulnerability created phishing lures on .gov and .mil domains that would push visitors into malicious redirects, and potentially target these victims with other exploits,” Edwards told Motherboard in an online chat.


Blackhat SEO campaigns featuring redirects have been going on for years, sometimes as [scareware](https://threatpost.com/seo-scareware-campaign-compromises-200k-websites-111709/73121/) but, when it comes to redirects to porn, mostly as trolling. Historically they’ve disappeared quickly as visitors have reported them, Edwards pointed out.


But these new exploits, which Edwards has tracked over the past year and detailed in the video below, are more sophisticated and don’t mop up so easily.


You can see the attraction: search engine optimization (SEO) massively benefits from the dot-gov domain, and the longer a domain can cling to government or military sites, the better off its SEO credibility.


Edwards has spotted these ads on subdomains including on [Senator John Tester’s site](https://twitter.com/thezedwards/status/1375118316021280772) and the Minnesota National Guard one above, which you might have mistaken for a legitimate site about a clinical health trial until you clicked through and found Viagra spam. That Minnesota spam has been taken down, but you can read the [original post](https://web.archive.org/web/20210914181655/https://webcache.googleusercontent.com/search?q=cache%3Acxm1jQe2uNEJ%3Ahttps%3A%2F%2Fminnesotanationalguard.ng.mil%2Fdocuments%2F2019%2F12%2Ffamily-statement-for-sgt-kort-m-plantenberg.pdf+&cd=6&hl=en&ct=clnk&gl=us) on the web archive.


The issue is there’s an open-redirect problem: The redirects are cached through inappropriate domain names and, if clicked, will send visitors to porn subdomains on the dot-mil and dot-gov sites.


Edwards said that he’s seen the problem on about 50 different government subdomains over the years, but typically they disappear fast: “You can report them [and] they disappear relatively quickly because I think people see them, and it’s jarring, so people report them,” he said in the video.


Not so with Canadian pharmacy redirects he’s been finding: “They’re extremely sophisticated and they seem to be persistent,” he said. “What’s kind of wild about them [is that] all of these scams are trying to persist their SEO benefits that they get from dot-gov domains so … by keeping their Canadian pharmacy URL and various content like Viagra and the products that they sell on a dot-gov compromised page for a significant period of time. It will increase, or it should theoretically increase, not only in Google but other search engines, basically, the domain credibility of these random Canadian pharmacies.”


Below is a screenshot taken on Friday at 10:35 ET that shows search results for the term “buy generic and brand Viagra” on .gov websites. A Canada pharmacy’s ad for Viagra places high up in search results: It’s the third returned site.


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/17103844/091721-web-search-on-buy-generic-viagra--1024x719.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/17103844/091721-web-search-on-buy-generic-viagra--e1631889539268.jpg)


Tracing It to Laserfiche
------------------------


Edwards told Vice that he traced the dicey uploads to Laserfiche after he found an Idaho.gov domain hosting the offending files and displaying a specific Laserfiche error message. A Google search also found ads for in-game currency for the hugely popular Roblox game platform and others advertising alleged Xbox gift card generators.


When Edwards approached Laserfiche about the problem, the company said that a vulnerability “allows an unauthorized party to temporarily upload files to a site,” according to a copy of an email that Edwards shared with Vice.


Anti-Porn, Etc. Patch Now Available
-----------------------------------


Laserfiche [publicly disclosed](https://support.laserfiche.com/kb/1014315/laserfiche-forms-portal-file-upload-vulnerability) that vulnerability and issued a critical security update today, on Friday. According to its disclosure, the Laserfiche forms portal file upload vulnerability is actively being exploited, enabling unauthenticated third parties to use Laserfiche Forms to “temporarily host uploaded files for distribution.”


Valid customer form submission data isn’t affected, Laserfiche said, and isn’t accessible to unauthenticated third parties. The security updates – to Laserfiche Forms 10.4.5 – address this vulnerability “by reducing the time frame where the temporary file download link is active,” the company said.


There are mitigations available for users who can’t immediately install updates on externally accessible Laserfiche Forms servers, though that is, indeed, what Laserfiche recommended.


“The Laserfiche Forms 10.x security updates modify the default behavior of public forms to no longer provide a download link,” Laserfiche said in its update.


Laserfiche also provided a [cleanup tool](https://support.laserfiche.com/kb/1014322/laserfiche-forms-public-portal-file-cleanup-tool) for Laserfiche Forms public portals to help affected customers scrub their portals clean.


Edwards told Vice that installing the patch should be done post-haste: “There are a significant number of cities, states and federal agencies, including military agencies, which use Laserfiche and should immediately install the patch and determine whether the other remediation steps are required,” the researcher said. “For any Laserfiche vendors who are using an older version of software that does not have the fix yet, those agencies should be encouraged to either upgrade their software, or stay on alert.”


**Rule #1 of Linux Security:** No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.




#### Tags:
[[Laserfiche]] [[dot-gov]] [[Linux]] [[SEO]] [[Viagra]] [[said.]] [[ThreatPost]]
