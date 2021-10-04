# Facebook Outage Drags Down Instagram, WhatsApp, Messenger, Oculus VR
### They were all flat on their faces for hours on Monday, throwing off DNS error messages or other server-related errors. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175308)
+ Date: October 4, 2021  4:40 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/04162346/facebook-e1633379038745.jpeg)
As of Monday afternoon, Facebook had been flat on its face for hours, suffering a simultaneous worldwide outage not only on its main site, but also at its Instagram, WhatsApp, Messenger and Oculus VR subsidiaries.




The [New York Times](https://www.nytimes.com/live/2021/10/04/business/news-business-stock-market) reported that Facebook’s internal communications platform, Workplace, was also dragged offline, “leaving most employees unable to do their jobs.” It’s been a thumb-twiddling afternoon, the Times reported, with two Facebook employees comparing it to a “snow day.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

On Twitter, the hashtag [#facebookdown](https://twitter.com/search?q=%23facebookdown&src=typed_query) was turning up predictable hilarity, transmitting blissful relief at the notion of a rainbow-bedrenched, Facebook-less world.




The reasons for the outage are unclear, but judging by the error message being thrown off by Facebook’s and WhatsApp’s domains – as shown in the screen captures below – it’s a DNS problem.


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/04153236/WhatsApp-error-msg-300x245.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/04153236/WhatsApp-error-msg.jpg) [![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/04153242/FB-DNS-error-300x194.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/04153242/FB-DNS-error.jpg)


 


As of 15:29 EDT, Instagram’s site was displaying a “5xx Server Error” error.


BGP Bye-Byes
------------


Cloudflare CTO John Graham-Cumming said in a series of tweets that the company saw Facebook disappear from the internet “in a flurry of BGP updates” between 15:50 UTC and 15:52 UTC:



In other words, Facebook’s border gateway protocol (BGP) routes were kaput, meaning that it had lost the protocols that make routing decisions based on paths, network policies or rule-sets configured by a network administrator.


Two Facebook security team members who requested anonymity told the New York Times that it’s unlikely that a cyberattack was behind the mass outages, given that “the technology behind the apps was still different enough that one hack was not likely to affect all of them at once.”


Outage Coincides with Facebook’s Media Circus
---------------------------------------------


[The Verge](https://www.theverge.com/2021/10/4/22708989/instagram-facebook-outage-messenger-whatsapp-error) reports that Facebook’s fiefdom skidded offline just as Facebook’s global head of safety, Antigone Davis, was live on CNBC. She was there to defend her employer against a [whistleblower’s accusations](https://www.theverge.com/2021/10/3/22707860/facebook-whistleblower-leaked-documents-files-regulation) that Facebook values product optimization so much that it has embraced algorithms that amplify hate speech, as well as to address Facebook’s handling of research data [that suggests Instagram is harmful to teens](https://www.theverge.com/2021/9/29/22701445/facebook-instagram-mental-health-research-pdfs-documents).


Saryu Nayyar, CEO of Gurucul, said that if the Facebook outage does turn out to be caused by attackers, they’re probably pissed off about Facebook’s business practices.


“As more facts about Facebook and its business practices become public, its users’ anger seems to be on the rise,” she noted via email to Threatpost on Monday. “If they are attackers, they respond by attacking – in this case, possibly a DDoS attack that flooded the company’s DNS server.”


In any event, the company is working on the problems: “We’re aware that some people are having trouble accessing our apps and products,” [said](https://twitter.com/andymstone/status/1445058088436908045) Facebook police communications director Andy Stone. “We’re working to get things back to normal as quickly as possible, and we apologize for any inconvenience.”


When The Verge checked out [Down Detector](https://downdetector.com/status/facebook/) before publishing its 12:01 EDT report on the issues, it looked like the problems were global. Outages spiked around noon EDT and were still coming down from that high as of 15:09 EDT, but the situation clearly hadn’t completely resolved.


The Verge also reported that users of the Oculus’s virtual reality technology can load games – if they’ve already installed and the browser works – but that Oculus social features are down, and users can’t install new games.


The Internet Is Still a Fragile Web
-----------------------------------


Bill Lawrence, CISO of SecurityGate, told Threatpost on Monday that outages like this one show little progress since the distributed denial-of-service [(DDoS) attack on Dyn](https://threatpost.com/dyn-confirms-ddos-attack-affecting-twitter-github-many-others/121438/) in October 2016. That attack, which affected Twitter, GitHub and others provided lessons learned: To ward off such a scenario, many large organizations now protect against DNS loss by maintaining multiple DNS systems across different DNS providers.


Even so, five years after Dyn we still have parts of the internet that can still shatter when services like DNS get interrupted for some reason, he said. Thus, Lawrence said that it will be interesting to see what caused this lingering outage to “several jewels in the Facebook family.”


Gurucul’s Nayyar agreed with the New York Times’ sources inside Facebook’s security team who said that the company’s infrastructure is too diverse for a cyberattack to cripple. She said that it’s highly unlikely that Facebook hasn’t protected itself in similar fashion, she said.


“While the cause of Facebook’s problem isn’t yet clear, it would be amazing if they hadn’t already set up multiple DNS providers,” she commented.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Facebook]] [[Facebook’s]] [[DNS]] [[it’s]] [[Threatpost]] [[ThreatPost]]
