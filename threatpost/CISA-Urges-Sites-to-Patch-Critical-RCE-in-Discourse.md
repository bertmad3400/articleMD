# CISA Urges Sites to Patch Critical RCE in Discourse
### The patch, urgently rushed out on Friday, is an emergency fix for the widely deployed platform, whose No. 1 most trafficked site is Amazon’s Seller Central. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175705)
+ Date: October 25, 2021  11:28 am
+ Author: Lisa Vaas


## Article:
Discourse – the ultra-popular, widely deployed open-source community forum and mailing list management platform – has a critical remote code-execution (RCE) bug that was fixed in an urgent update on Friday.


Tracked as [CVE-2021-41163](https://nvd.nist.gov/vuln/detail/CVE-2021-41163), the flaw is found in Discourse versions 2.7.8 and earlier. It’s rated with a tip-top CVSS severity score of 10 and should be considered an emergency fix.


Discourse is widely used and wildly popular, being known for topping competing forum software platforms in terms of usability. It offers features that have been popularized by social-media networks, such as infinite scrolling, live updates, drag-and-drop attachments and more.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


According to market-share and web-usage [statistics](https://www.similartech.com/technologies/discourse), the top website using Discourse is sellercentral.amazon.com, which sees a flood of 30 million monthly users. Discourse is also used to run the community forum for the popular radio show Car Talk.


Given Discourse’s widespread use, the Cybersecurity and Infrastructure Agency (CISA) on Sunday [urged developers](https://us-cert.cisa.gov/ncas/current-activity/2021/10/24/critical-rce-vulnerability-discourse) to either update to patched versions 2.7.9 or later to fix the bug or to apply the necessary workarounds.


The [exploit](https://nvd.nist.gov/vuln/detail/CVE-2021-41163) can be triggered by an attacker who sends a maliciously crafted request that can lead to RCE due to a lack of validation in subscribe\_url values.


Update or Apply the Workaround
------------------------------


The issue has been patched in the latest beta, stable and tests-passed versions of Discourse.


For those admins who can’t update to 2.7.9 or later, the workaround is to block requests that start with “/webhooks/aws path” at an upstream proxy.


The flaw is still undergoing technical analysis, but the researcher who discovered the vulnerability has [published a technical analysis](https://0day.click/recipe/discourse-sns-rce/) about it.


The details in his analysis – which he released just a day after the fix was issued – could be enough for attackers to exploit it. The researcher, “joernchen,” [told BleepingComputer](https://www.bleepingcomputer.com/news/security/cisa-urges-admins-to-patch-critical-discourse-code-execution-bug/) that he reported the issue to the Discourse team immediately upon finding it on Oct. 10 and that the patch itself made it easy to figure out how an exploit would work.


Although the software-as-a-service (SaaS) versions of Discourse were fixed as of Wednesday, there might still be many vulnerable deployments. A Shodan search pulled up 8,640 Discourse deployments on Monday morning.


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/25104333/shodan-discourse-scaled-e1635173031834.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/25104333/shodan-discourse-scaled-e1635173031834.jpg)


Can’t Fix It If You Don’t Know About It
---------------------------------------


Greg Fitzgerald, co-founder of Sevco Security, told Threatpost on Monday that this RCE vulnerability points to how tricky it’s getting for organizations to assess their attack surfaces.


“There is more data flowing around organizations than ever before,” he said via email. “There are more solutions installed than ever before. The diversity of devices, users and applications being used by the business is more complex than ever before.”


It’s therefore more important than ever to get asset inventory right, he continued. “All these ‘ever befores’ have made the task of creating an accurate IT asset inventory – and therefore understanding what your real attack surface looks like – incredibly challenging for companies,” Fitzgerald said. “Enterprises tend to do a really good job of patching the vulnerabilities that they know about quickly, but the real threats lurking under the surface for most organization are the IT assets they’ve forgotten about, which often create an easy path to data for attackers.”


Threatpost has reached out to Discourse for more details and to ask whether or not the team has seen any signs that the RCE has been exploited in the wild. We’ll update the story when we hear back.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[RCE]] [[Threatpost]] [[ThreatPost]]
