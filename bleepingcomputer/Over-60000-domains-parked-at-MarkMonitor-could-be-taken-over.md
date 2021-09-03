# Over 60,000 domains parked at MarkMonitor could be taken over
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/over-60-000-domains-parked-at-markmonitor-could-be-taken-over/)
+ Date: September 3, 2021
+ Author: Ax Sharma


## Article:
![domains](https://www.bleepstatic.com/content/hl-images/2017/10/02/Domain-Names.jpg)


Domain registrar MarkMonitor had left more than 60,000 parked domains vulnerable to domain hijacking.


MarkMonitor, now part of Clarivate, is a domain management company that "helps establish and protect the online presence of the world's leading brands - and the billions who use them."


The parked domains were seen pointing to nonexistent Amazon S3 bucket addresses, hinting that there existed a domain takeover weakness.


Researchers took over 800 root domains
--------------------------------------


This week, security engineer and bug bounty hunter [Ian Carroll](https://twitter.com/iangcarroll) saw his automation script flag hundreds of domains belonging to different organizations that were vulnerable to domain hijacking.


Carroll was then joined by [Nagli](https://twitter.com/naglinagli) and *[d0xing](https://twitter.com/d00xing)*who helped the engineer trace the source of the security weakness. All of the domains shared the same registrar—MarkMonitor.


[(Sub)domain takeover](https://developer.mozilla.org/en-US/docs/Web/Security/Subdomain_takeovers) refers to an unauthorized actor being able to serve the content of their choice on a domain they otherwise have no rights to or ownership of.


This can occur, for example, if the domain name has a canonical name (CNAME) DNS entry pointing to a host that is not providing any content for it.


Typically, this happens if the website hasn't been published yet or the virtual host has been removed from a hosting provider but the domain's DNS records continue to point to the host.


When such a scenario occurs, what follows is a 404 (not found) error message when one attempts to access the domain, indicating that a domain takeover weakness could exist.



![s3 bucket not found](https://www.bleepstatic.com/images/news/u/1164866/2021/Sep-2021/s3-bucket-not-found.jpeg)**Domains previously showed 404 "NoSuchBucket" found errors from Amazon S3 servers**  

Source: BleepingComputer
An attacker can then take over the vulnerable domain in the sense that they can begin serving their own content at the location where the domain's dangling DNS entry is pointing to.


"If *testing.example.com* is pointed towards Amazon S3, what will S3 do if that bucket hasn't been created yet? It will just throw a 404 error—and wait for someone to claim it," explains Carroll.


"If we claim this domain inside S3 before *example.com*'s owners do, then we can claim the right to use it with S3 and upload anything we want," continues the engineer in his [writeup](https://ian.sh/markmonitor).


That is exactly what happened when Carroll, along with other researchers, was able to take over more than 800 root domains, as a part of the research:




> 
> Apparently 90%+ of the domains being "protected" atm by [@markmonitor](https://twitter.com/markmonitor?ref_src=twsrc%5Etfw) are showing up as unclaimed S3 buckets on us-west-2 region, over 2000 subdomain takeovers the last hour [@iangcarroll](https://twitter.com/iangcarroll?ref_src=twsrc%5Etfw) [@d00xing](https://twitter.com/d00xing?ref_src=twsrc%5Etfw), hoping that [@markmonitor](https://twitter.com/markmonitor?ref_src=twsrc%5Etfw) will roll up a fix sooner rather than later.[#BugBounty](https://twitter.com/hashtag/BugBounty?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/3iGPAue1iw](https://t.co/3iGPAue1iw)
> 
> 
> — Nagli (@naglinagli) [August 28, 2021](https://twitter.com/naglinagli/status/1431724861383118851?ref_src=twsrc%5Etfw)


Issue impacted over 60,000 domains, lasted under an hour
--------------------------------------------------------


After Carroll emailed MarkMonitor's security contact, the researcher did not hear back. But, he noticed that the domains previously throwing S3 "bucket not found" errors gradually started showing the proper MarkMonitor landing page:



![markmonitor default parking page](https://www.bleepstatic.com/images/news/u/1164866/2021/Sep-2021/markmonitor-parking-page.jpg)**MarkMonitor default parking page now visible for previously vulnerable domains**  

Source: BleepingComputer
"After I sent an email to *security@markmonitor.com* that went unacknowledged, domains stopped pointing to S3 over an hour after it began," says Carroll.


"I claimed over 800 root domains in this timeframe, and other researchers had similar amounts of claimed domains," continued the engineer.


Carroll's main concern was, as many as 62,000 domains parked over at MarkMonitor could potentially be hijacked, and abused for phishing.


For example, using intel-gathering service *SecurityTrails*, the engineer identified highly valuable domains representing known brand names, including *google.ar*and *coinbase.ca*that would make great phishing candidates, should these be taken over:



![securitytrails alexa rank domains](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Highly ranked domains that could be potentially taken over for phishing**  

Source: Ian Carroll, via *SecurityTrails*
BleepingComputer reached out to both Amazon and MarkMonitor for learning more, and heard back from MarkMonitor's parent company, Clarivate:


"During a planned move of our parking page to the cloud, our DDoS protection vendor temporarily routed traffic in an unexpected manner for some domains using MarkMonitor's parking page service," a Clarivate spokesperson told BleepingComputer.


"Neither live domains nor DNS were impacted. We take the protection of the domains entrusted to us – including parked domains – extremely seriously, and we work every day to make sure we are following the best security practices and guidelines."


"This includes having active and static scanning, ongoing DNS monitoring, annual 3rd party penetration testing, and other security audits," continued Clarivate spokesperson.


Clarivate is also in the process of finalizing a bug bounty program.


MarkMonitor states, as soon as the unexpected behavior was identified, the company immediately reverted their DDoS vendor settings to point traffic to an internally-hosted web server's parked page.


Full detection, investigation, and remediation were completed in under an hour, says MarkMonitor.


Following their investigation, the registrar is not aware of any instances of malicious content being hosted for any parked page.


When asked what could companies do to better protect themselves against domain takeover weaknesses like these, Carroll said:


"Until cloud providers like Amazon move to prevent domain takeovers like this, companies need to be careful when pointing traffic to them, either via DNS records or otherwise," Carroll told BleepingComputer.


"This issue is not entirely the fault of MarkMonitor. While they need to be careful with handling parked domains, AWS is at fault for not being more stringent with claiming S3 buckets. Google Cloud, for example, has [required domain verification for years](https://cloud.google.com/storage/docs/domain-name-verification), rendering this [attack] useless," says the engineer in his blog post.


Amazon did not respond to our request for comment.


MarkMonitor stated to BleepingComputer that they continuously review their test cases and policies to identify and be alerted of such issues.


"We are also evaluating mechanisms to be alerted more quickly of any HTTP error responses from domains that are parked with our parking service, which may allow us to identify and react to unexpected behavior even more quickly in the future," concluded MarkMonitor spokesperson in their statement to BleepingComputer.




#### Tags:
[[MarkMonitor]] [[S3]] [[DNS]] [[BleepingComputer]] [[example,]] [[Source:]] [[domains,]] [[Clarivate]] [[BleepingComputer.]] [[Bleeping Computer]]
