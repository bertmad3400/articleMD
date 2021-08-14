# Black Hat: Novel DNS Hack Spills Confidential Corp Data
### Threatpost interviews Wiz CTO about a vulnerability recently patched by Amazon Route53’s DNS service and Google Cloud DNS. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168636)
+ Date: August 12, 2021  4:30 pm
+ Author: Tom Spring


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/12152519/wiz-cto.png)
LAS VEGAS – Amazon and Google patched a domain name service (DNS) bug that allowed attackers to snoop on the confidential networking settings of companies – revealing computer and employee names along with office locations and exposed web resources.


The vulnerability, outlined in a Black Hat USA 2021 talk last week, is a new class of vulnerabilities affecting major DNS-as-a-Service (DNSaaS) providers, according to researchers at the cloud security firm Wiz.


[Ami Luttwak](https://www.crunchbase.com/person/ami-luttwak), co-founder and CTO of Wiz, said the bug allows an adversary to conduct unprecedented reconnaissance on a target – namely any vulnerable corporate network that inadvertently allows this type of network eavesdropping.


![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)


While Amazon and Google have patched the bug, Luttwak warns the problem is likely widespread.


Threatpost caught up with Luttwak at Black Hat and in the video below.


Wiz revealed the vulnerability affecting DNSaaS providers Amazon Route53 and Google Cloud DNS, which both promptly patched the bug in February.


**Going Down the DNS Loophole**
-------------------------------


“We found a simple loophole that allowed us to intercept a portion of worldwide dynamic DNS traffic going through managed DNS providers like Amazon and Google. Essentially, we ‘wiretapped’ the internal network traffic of 15,000 organizations (including Fortune 500 companies and government agencies) and millions of devices,” [Wiz wrote in a technical breakdown](https://www.wiz.io/blog/black-hat-2021-dns-loophole-makes-nation-state-level-spying-as-easy-as-registering-a-domain) of the bug.


Luttwak calls what he found a “loophole” within the process used to handle the now obsolete dynamic DNS within modern DNS server configurations.


“We registered a new domain on the Route 53 platform with the same name as their official DNS server. (Technically, we created a new ‘hosted zone’ inside AWS name server ns-1611.awsdns-09.co.uk and named it ‘ns-852.awsdns-42.net’),” researchers explained.


Next, researchers gained control of the hosted zone by registering thousands of domain name servers as the same name as the DNSaaS official DNS server. “Whenever a DNS client queries this name server about itself (which thousands of devices do automatically to update their IP address within their managed network – more on that in a minute), that traffic goes directly to our IP address,” Wiz wrote.


What researchers observed next was a flood of dynamic DNS traffic from Windows machines that were querying the “hijacked name server” about itself. In all, researchers profiled 15,000 organizations (some Fortune 500 companies), 45 U.S. government agencies and 85 international government agencies.


**Misconfiguration or Vulnerability?**
--------------------------------------


DNSaaS providers Route53 and Google Cloud DNS fixed the issue by disallowing the type of copycat registration that mirrored their own DNS server.


As for Microsoft, researchers said that the company considered this to be a misconfiguration issue.


“Microsoft could provide a global solution by updating its dynamic DNS algorithm. However, when we reported our discovery to Microsoft, they told us that they did not consider it a vulnerability but rather a known misconfiguration that occurs when an organization works with external DNS resolvers,” researchers said.


Luttwak said that companies can avoid this type of DNS exploitation by configuring their DNS resolvers properly so dynamic DNS updates do not leave the internal network.


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[DNS]] [[Google]] [[Luttwak]] [[DNSaaS]] [[server.]] [[ThreatPost]]
