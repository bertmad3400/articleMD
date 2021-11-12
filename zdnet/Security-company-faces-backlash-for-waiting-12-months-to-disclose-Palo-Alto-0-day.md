# Security company faces backlash for waiting 12 months to disclose Palo Alto 0-day
### Randori has faced a barrage of criticism for its decision to wait one year to publish a notice about a vulnerability it found in 2020.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/security-company-faces-backlash-for-waiting-12-months-to-disclose-palo-alto-0-day/)
+ Date: November 12, 2021
+ Author: Jonathan Greig


## Article:
Unknown

There has been considerable debate within the cybersecurity community about Randori, a security firm that waited one year before [disclosing a critical buffer overflow bug](https://www.randori.com/blog/cve-2021-3064/) it discovered in Palo Alto Networks' GlobalProtect VPN.

The zero-day -- which has a severity rating of 9.8 and was [first reported by ZDNet](https://www.zdnet.com/article/palo-alto-networks-patches-zero-day-affecting-firewalls-using-globalprotect-portal-vpn/) -- allows for unauthenticated, remote code execution on vulnerable installations of the product.

The issue affects multiple versions of PAN-OS 8.1 prior to 8.1.17, and Randori said it found numerous vulnerable instances exposed on internet-facing assets, in excess of 70,000 assets. It is used by a number of Fortune 500 companies and other global enterprises.

Aaron Portnoy, principal scientist at Randori, explained to ZDNet that in October 2020, his team was tasked with researching vulnerabilities with the GlobalProtect Portal VPN. By November 2020, his team discovered CVE-2021-3064, began authorized exploitation of Randori customers, and successfully landed it at one of their customers -- over the internet -- not just in a lab. 

They did not notify Palo Alto Networks until a few weeks ago, according to the timeline they provided.

Palo Alto Networks [released its own advisory](https://security.paloaltonetworks.com/CVE-2021-3064) about the issue, has patched it and said there is no evidence it has been exploited in the wild. 

But Randori's actions in the case have caused [considerable backlash](https://twitter.com/evacide/status/1458958013344092163) from some in the cybersecurity community, who [argue](https://twitter.com/hacks4pancakes/status/1458878534043242512) the company should not have waited 12 months before disclosing it to Palo Alto Networks. Portnoy has [released](https://twitter.com/aaronportnoy/status/1458899406925844493) multiple statement on Twitter defending the company from criticism. 






Others have taken issue with Randori's decision to use the 0-day in red team exercise and others questioned whether they held back notification of the issue in order to further publicize their work and their business. Despite the backlash, some have come to Randori's defense, arguing that their actions are commonplace.

David Wolpoff, Randori's CTO, told ZDNet that the company "weighed a lot of factors when determining disclosure to minimize industry harm," including analysis of the software, patch status, versioning issues, existing remediation strategies, and more.

"We cannot respond in granular detail, as we are intentionally staying away from disclosing technical details that would enable exploit. We would like to increase the transparency of our decision process because people didn't seem to grasp the nuance, but we still very much believe in our policy and our decision," Wolpoff said.

Randori would not answer questions about why they waited 12 months to disclose the vulnerability. 

But Wolpoff said there "are always concerns" and argued that the company is "acutely aware of the risks of having a capability like this."

Yet he argued that knowing about the vulnerability "doesn't increase the risk."

"If we knew about the bug or didn't, the risk profile to the public is the same. In this case -- a minor release within a major version of software -- we knew remedies already existed being recommended by the vendor," Wolpoff said. 

"This factored into our decision. We were aware of the nuance in regards to the PAN update, and it (along with other metrics) factored into our weighing of the risks associated."

Opinions among experts varied. Casey Ellis, founder and CTO at Bugcrowd, said vulnerability equity decisions are difficult to trust when there's an obvious commercial conflict of interest. 

Vulcan Cyber CEO Yaniv Bar-Dayan told ZDNet that there are several approaches to responsible vulnerability disclosure but most critical is the expediency of all involved parties, and an altruistic collaboration between researchers and responsible organizations. 

"Time is of the essence if the goal is systems and data security. The intent of vulnerability disclosure programs breaks down if the disclosure goals of researchers or vendor organizations ever deviate from pure security," Bar-Dayan said. "As an example, the recently announced Google Project Zero requires the full details of a vulnerability to be published within 90 days after discovery regardless of whether or not the vendor organization has provided a patch or mitigation option."

ThreatModeler CEO Archie Agarwal explained that there is a long tradition of cybersecurity professionals finding security holes in popular software and disclosing the vulnerability to the development company and then afterwards the public. 

The idea, Agarwal said, is that the 'good guys' find the problems before the 'bad guys.' 

"There is nothing ethically wrong with this practice as long as the disclosure is responsible and all efforts are made to coordinate with the company in terms of remediation and allowing them time to create a patch before it becomes publicly known as appears to be the case in this instance," Agarwal explained. 

"Legitimate bug bounties operate the same. The unfortunate part is criminals also see the public disclosure and are getting faster and faster at exploit development and so those not updating the patch fast enough are often left open to automated attacks."

J.J. Guy, CEO of Sevco Security, argued that the job of a red team is simple: emulate the adversary. 

"If adversaries are using 0-days, our red teams should be using them too. We can't prepare for the reality of how we'll react to compromise if red teams are pulling punches. Many organizations must protect high-value assets from real-world attacks by adversaries bringing this level of capability. It is extremely valuable for these orgs to practice their ability to detect and respond to 0-day. They know they must defend against unknowns," Guy said. 

"Software is not and never will be perfectly secure. There are an infinite number of 0days waiting to be discovered, so if your IT team believes they can patch all the holes, they're wrong."





#### Tags:
[[ZDNet]] [[cybersecurity]] [[Palo]] [[Wolpoff]] [[said.]] [[CEO]] [[ZDNet]]
