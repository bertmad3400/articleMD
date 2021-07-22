# Akamai has trouble and the internet hiccups up again
### If your internet's acting up today, it's not you. It's the internet. Specifically, major content delivery network Akamai is having DNS trouble.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/akamai-has-trouble-and-the-internet-hiccups-up-again/)
+ Date: July 22, 2021 -- 18:48 GMT (19:48 BST)
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

You've heard it before, you'll hear it again. Once more with feeling, the internet is having real trouble as we move into July 22's early afternoon on the US East coast.  

According to reports on the [Outages list](https://puck.nether.net/mailman/listinfo/outages), which is the central mailing list for ISP and network operators to report and track major internet connection problems, and numerous [Reddit threads](https://www.reddit.com/r/sysadmin/comments/opgjk5/aws_outage/), the major Content Delivery Network (CDN) [Akamai](https://www.akamai.com/) is the root of the problem. 

Specifically, people are reporting that when they try to reach sites that use Akamai to host their [DNS CNAMEs](https://ns1.com/resources/cname) they can't reach them. The sites are fine. But, thanks to trouble on Akamai's DNS edge servers, your web browser, game application, whatever, can't reach the sites. They're not getting the right addresses so your local program doesn't know how to find them. 

Akamai has admitted it's having trouble. In a notification, Akamai stated: 


> We are aware of an [emerging issue with the Edge DNS service](https://edgedns.status.akamai.com/). We are actively investigating the issue. If you have questions or are experiencing impact due to this issue, please contact [Akamai Technical Support](https://www.akamai.com/us/en/support/). In the interest of time, we are providing you the most current information available, which is subject to changes, corrections, and updates.
> 
> 

Oops. 

[Akamai only has 9.6% of the CDN market](https://www.slintel.com/tech/cdn/akamai-market-share#faqs). But, its share is a very important one. Sites that depend on Akamai include Amazon Web Services, Microsoft, Delta Airlines, Oracle, Capital One, and AT&T. Yeah, you'll notice when those sites and the services they provide are offline. 

There are reports that [Akamai has a handle on the problem](https://www.cnbc.com/2021/07/22/several-major-websites-go-down-in-widespread-internet-outage.html) now. The status page site itself, as of 1:02 PM Eastern time, states that "This incident has been mitigated." Since it takes time for both problems and fixes to appear in the global DNS service, you may still have trouble reaching some sites or services. For example, I'm still having trouble using my Delta airlines app. 






So, be patient. By the end of the business day, Akamai, and your internet connection should be back to normal. 

**Related Stories:** 

* [A massive outage just took large sections of the internet offline](https://www.zdnet.com/article/a-massive-outage-just-took-large-sections-of-the-internet-offline/)
* [Major internet outages hit Northeast and Mid-Atlantic states](https://www.zdnet.com/article/major-internet-outages-hit-northeast-and-midatlantic-states/)
* [The internet is hanging in there despite the coronavirus](https://www.zdnet.com/article/the-internet-is-hanging-in-there-despite-the-coronavirus/)





#### Tags:
[[DNS]] [[ZDNet]]
