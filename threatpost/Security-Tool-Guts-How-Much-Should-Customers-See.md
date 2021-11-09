# Security Tool Guts: How Much Should Customers See?
### Yaron Kassner, CTO of Silverfort, delves into the pros and cons of transparency when it comes to  cybersecurity tools’ algorithms.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176113)
+ Date: November 9, 2021  10:52 am
+ Author: Yaron Kassner


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/09104258/surgery-e1636472598246.jpeg)
Many cybersecurity tools use engines that calculate risk for events in customer environments. The accuracy of these risk engines is a major concern for customers, since it determines whether an attack is detected or not.


Therefore, organizations often request visibility into how a risk engine actually works. Let’s consider whether disclosing a security product’s algorithm is the best approach.


**The Pros of Visibility into a Risk Engine**
---------------------------------------------


On the one hand, providing visibility into a risk engine enables an organization to know exactly what it is buying and to test the capabilities in a proof of concept (PoC). It also provides the buyer with a sense of control. Some vendors allow customers to modify the parameters of their risk algorithm in order to fine-tune results based on their specific needs.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

But while this approach allows far greater customization, only a small number of companies have the resources and domain expertise required to make modifications that can distinguish between normal behavior and an attack.


In addition, understanding the risk algorithm enables customers to distinguish between bugs and algorithm limitations. Since risk algorithms are often based on machine learning and statistics, they are likely to detect most, but not 100 percent, of malicious scenarios. Knowing the risk algorithm lets you understand exactly why some scenarios were detected and others weren’t.


Furthermore, some knowledge of the risk engine’s functions can provide the confidence users need to use it to its full extent and to rely on it for blocking threats, rather than for detection only.


Finally, providing visibility into risk algorithms improves the science of cybersecurity. The more we share our knowledge as a community, the more advances we will make.


**The Risks of Visibility**
---------------------------


Nevertheless, there are strong considerations in favor of keeping risk algorithms secret.


First and foremost, a sophisticated attacker who knows the protections they’re dealing with can find ways to bypass them. We’ve all seen how antivirus software is repeatedly evaded by attackers and how threat actors continually evolve their tactics to avoid detection.


In addition, some algorithms are just hard to explain, such as risk scores that are calculated using deep neural networks.


Should we avoid deep learning and complicated algorithms for the sake of making risk engines easier to understand? I think not.


**The Compromise**
------------------


There’s a middle path. One way is to share enough details about risk engines without disclosing too much information that would degrade their effectiveness.


For example, we could share the inputs to an algorithm and provide examples for detection, without revealing its inner workings and the parameters it is using.


This approach can provide the basic information needed to gain customers’ trust, without revealing specifics that could be used by attackers to circumvent detection.


When deciding between visibility and secrecy of security risk algorithms, the industry should lean toward disclosure – that is, to the extent that it doesn’t compromise the defensive posture of customers.


*Image courtesy of the [U.S. Navy](https://www.flickr.com/photos/usnavy/23940189268).* 


***Cybersecurity for multi-cloud environments is notoriously challenging. OSquery and CloudQuery is a solid answer. Join Uptycs and Threatpost on Tues., Nov. 16 at 2 p.m. ET for “***[***An Intro to OSquery and CloudQuery***](https://bit.ly/3wf2vTP)***,” a LIVE, interactive conversation with Eric Kaiser, Uptycs’ senior security engineer, about how this open-source tool can help tame security across your organization’s entire campus.***


[***Register NOW***](https://bit.ly/3wf2vTP) ***for the LIVE event and submit questions ahead of time to Threatpost’s Becky Bracken at*** [***becky.bracken@threatpost.com***](mailto:becky.bracken@threatpost.com)***.***




#### Tags:
[[]] [[ThreatPost]]
