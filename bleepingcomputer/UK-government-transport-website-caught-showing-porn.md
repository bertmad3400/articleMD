# UK government transport website caught showing porn
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/uk-government-transport-website-caught-showing-porn/)
+ Date: November 25, 2021
+ Author: Ax Sharma


## Article:
![dft gov uk website](https://www.bleepstatic.com/content/hl-images/2021/11/25/dft-bg2.png)


A UK Department for Transport (DfT) website was caught serving porn earlier today.


The particular DfT subdomain behind the mishap, on most days, provides vital DfT statistics for the public and the department's business plan.


A very British thanksgiving
---------------------------


The UK DfT's *charts.dft.gov.uk* website was seen serving porn today, as confirmed by BleepingComputer.


In the past, the Charts subdomain has provided business plan documents and important [statistics](http://web.archive.org/web/20201019154536/http://charts.dft.gov.uk/statistics/) on various DfT services such as numbers on public transport utilization, roadway accessibility times, and driving tests.


Although the site is no longer reachable, as of a few hours ago, visiting *charts.dft.gov.uk* paved the way for some racy traffic:  



![UK gov DfT subdomain serving porn](https://www.bleepstatic.com/images/news/u/1164866/2021/Nov-2021/gov-uk-porn/gov-uk-porn.jpg)**UK gov DfT subdomain caught serving porn**(BleepingComputer)
The mishap was [first spotted](https://thecrow.uk/A-Gov.uk-site-dedicated-to-porn-Absolutely/) by *The Crow,* whichadditionally observed that the entire *dft.gov.uk* domain was itself made to redirect to a WordPress plugin page, while the Department appeared to investigate the issue.


In our tests, BleepingComputer observed the official *dft.gov.uk* website led to a password-protected WordPress page living at: *eu-hauliers.dft.gov.uk*.



![Dft-gov-uk needs password](https://www.bleepstatic.com/images/news/u/1164866/2021/Nov-2021/gov-uk-porn/wp-login.jpg)**The entire *dft.gov.uk* redirected to a password-protected WordPress page earlier today**(BleepingComputer)
The dangling... DNS
-------------------


Although the exact cause of the Charts mini-site serving porn is not known, [it appears](https://news.ycombinator.com/item?id=29343317) the subdomain did have a CNAME DNS record pointing to an Amazon S3 instance.


The offending (NSFW) instance is still up at *charts.dft.gov.uk.s3-website-eu-west-1.amazonaws.com,* showing illicit content. Fortunately, *charts.dft.gov.uk*no longer leads there.


What remains unclear is, if this was simply a case of [domain hijacking](https://www.bleepingcomputer.com/news/security/over-60-000-parked-domains-were-vulnerable-to-aws-hijacking/)—that is, a dangling AWS S3 instance that the Charts site pointed to, was claimed by a threat actor and made to serve adult content, or did an attacker obtain enough access to DfT's registrar's systems and changed the DNS entry for *charts.dft.gov.uk*.


The second scenario is more challenging to pull off and would raise some serious questions on how secure the DfT's digital infrastructure is.


This isn't the first time a government website was caught serving explicit content either.


In September this year, U.S. government websites were [spammed with viagra ads and adult content](https://www.bleepingcomputer.com/news/security/us-govt-sites-showing-porn-viagra-ads-share-a-common-software-vendor/) after attackers exploited a vulnerability in the Laserfiche Forms software product, used by multiple government sites.


In July, visitors to major news sites including *The Washington Post* and *HuffPost* saw the embedded videos in news stories [replaced with porn](https://www.bleepingcomputer.com/news/technology/major-news-sites-serve-porn-after-vidme-domain-takeover/) after the *vid.me* domain was acquired by a third party. 


The access to the main DfT website *dft.gov.uk* has since been restored. However, the sysadmins seem to have pulled the plug on *charts.dft.gov.uk* altogether, which is no longer accessible.


BleepingComputer contacted the UK DfT both via telephone and email prior to writing and we are awaiting their response.




#### Tags:
[[website]] [[UK]] [[subdomain]] [[charts.dft.gov.uk]] [[dft.gov.uk]] [[WordPress]] [[DNS]] [[Bleeping Computer]]
