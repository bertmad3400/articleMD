# Q&A: CISO sees 'enterprise' browser as easier way to monitor employee web use
### Bob Schuetter, CISO at Ashland Specialty Chemicals, has been piloting a new enterprise-specific browser as a way to secure web traffic and company data associated with SaaS applications.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3648968/qa-ciso-sees-enterprise-browser-as-easier-way-to-monitor-employee-web-use.html
+ Date: 2022-02-04T03:00-05:00
+ Author: Lucas Mearian


## Article:
![Article Image](https://images.idgesg.net/images/article/2019/11/cso_browser_security_by_thinkstock_497418668_1200x800-100817200-large.jpg?auto=webp&quality=85,70)

Over the past several years, [Ashland Specialty Chemicals](https://www.ashland.com/), a global specialty materials and chemical company with about 4,200 employees, has been downsizing. It shuttered its physical datacenter and adopted more of a software-as-a-service strategy for business apps such as Salesforce and Workday. With the shift to the cloud, the company also had to address keeping web traffic secure as its hybrid workforce accessed sensitive data online.

While the company continues to use more traditional, and costly, firewalls such as Cloud Access Security Brokers (CASB) and Secure Access Service Edge (SASE) to secure web gateways, it has also been testing an enterprise-specific browser from [a start-up company named Island](https://www.computerworld.com/article/3648597/start-up-emerges-with-an-enterprise-browser.html). 

ADVERTISEMENTThe Chromium-based browser offers a variety of granular security capabilities for controlling what users can access online. Admins can fully control last-mile actions, from advanced security demands to more basic data exfiltration protections such as copy, paste, download, upload, screenshots, and other activities that might expose critical data.

Bob Schuetter, CISO at Delaware-based Ashland, purchased 4,000 seats for the Island browser, though he has only been piloting it over the last six months with about 100 employees who downloaded it to their PCs. For Schuetter, the biggest benefits of browser-based security include controlling the data entry point and ease of use. His hope is to eventually consolidate security around the browser if it pans out.

[![headshot of Bob Schuetter](https://images.idgesg.net/images/article/2022/02/headshot1-100917920-small.jpg?auto=webp&quality=85,70)](https://images.idgesg.net/images/article/2022/02/headshot1-100917920-orig.jpg?auto=webp&quality=85,70 "<div class='credit'>Bob Schuetter</div>
<p>Bob Schuetter, CISO of Ashland Specialty Chemicals</p>
")
The following are excerpts from an interview with Schuetter: 

**What prompted you to pilot the Island browser?** "We got out of having a datacenter about five years ago. All of a sudden, your strategy as a much smaller company is lots of SaaS..., where you’re no longer doing a lot of internal development; you’re buying stuff as fast as the company can consume it. I think that’s the biggest piece. So, everything we used to do as security was kind of force the applications to work the way we wanted them to. We changed networking, we changed how the network flows, we tried to get everything coming into us so we can get visibility — break encryption.

"So...SaaS providers, they get point to point encryption, which is great for them, but terrible for us. They get security, but we can’t see anything.

"And, this was finally the opportunity to get security at the front. We’ve always tried to connect people to applications. We’ve changed how we’ve done it and kept on changing it. But this is the first opportunity we have to allow that true anytime-to-anywhere, any device, any platform. I don’t have to have an agent on that desktop.   
"You’re on my network. I can control the browser."

 **Are there tools you’d like to see added to the Island browser?** "There is still a lot of opportunity. It has started out as a good governance, a good data-privacy tool — so, kind of all those core base pieces. What we’re pushing for is how can I really fully integrate this. We’re a big detection group. We’d like to see advanced threat [detection]. We’d like to see how these things are happening. We’d like to get to the point within our detection platform where we get the little movie of exactly what the user did; so, no guessing what the user did.

"And that’s exciting. I think [Island] has everywhere to go with it."

ADVERTISEMENT**What other network edge security technologies did you have before Island?** "We have one of everything, like most people. So we’ve got a good CASB, we’ve got a good secure edge, we’ve got SASE and all that fun stuff and big things. But that whole process works by traffic shaping — by changing the flow of the natural application and forcing it into one place we want it, unencrypted and uninspected, and then do DLP [data loss prevention] and whatever else, and then let it go its own way.

"I like this one because it’s not intrusive; it’s built in. I don’t have to keep changing how the application works in order to get visibility.

"So, because you’re embedding security into the entry point — into how the user interacts with the application — I don’t have to worry about trying to grab it as it’s already going out. That’s kind of what a CASB is; it’s a network-based solution. Someone already did something, and now you’re trying to catch it through the network to stop it from happening. This way I can see it up front."

**What have been some of the other key advantages of an enterprise-specific browser?** "As you look at SaaS applications, like Salesforce or Workday, it was really hard to stop people from logging in from the outside with their own PCs. That’s part of the benefit of SaaS. As we’re getting what we’re calling sanctioned apps or approved apps, we’ll start to say, 'You know what? Salesforce, Workday, Office — you can only get to those through this browser now.' So, we’ll enforce people who are interacting with your SaaS through this browser.

ADVERTISEMENT"That’s the idea of the rollout — just put it out there. You can start by using it as just a regular browser, and then we start to enforce individual SaaS applications that are more sensitive and keep on growing that. Eventually, we’ll get to the point where there’s no need to have any other browsers.

**Is it relatively easy to roll out and administer?** "So far, it is. That’s why I laughed when they first pitched it to me: You’re going to try to sell me a browser? Browsers are ubiquitous now. Because it’s Chromium and based on the same experience you’re used to, users aren’t pushing back on it at all. It’s been an easy transition for the user base. We had it rolled out within a week or two.

"I think the only questions everyone in the company is dealing with right now is who owns this stuff because we’re converging so much of the network and firewalls. We’re converging now a browser and security — a browser and data loss prevention. I think the bigger question that will be in people’s minds is, who owns this now? Is it a security tool? Is it a productivity tool? Otherwise, there's no push back on it. It looks and feels just like Edge or Chrome."

**What features would you consider the most advantageous for your organization?**"I think the big use case right now is the ability to go further down in my third-party risk side. We had a number of new SaaS providers pop up. They don’t do logging; they don’t show you the logs or give you the logs — all these other things. So, getting all that information up front, right from the source, really evens things out. I can say ‘Yes’ [to new business projects] a lot faster than I could before. So, [it's] allowing the business to go fast and not having to wait on security to architect things, and put governance in place, and put DLP in place, and get the data flows right. If you guys are OK using the browser, I’ll turn on those features. Let’s go.

ADVERTISEMENT"So, speed is one of the selling points for us."

**How did you roll it out?**"We’re still rolling out the step-by-step enforcement piece. That’s the good news about it. You don’t need to go all in all at once. You can choose pockets and groups and roll it out as you get more comfortable."

ADVERTISEMENT**What do you mean by "step-by-step" enforcement?** "Think about a traditional CASB, or a traditional proxy, or a traditional firewall; you’re having to bring your entire environment over all at once. So, it’s a big cutover day. We have these big cutover events: 'OK, we’re about to turn it on, and we’re about to start shaping all your network traffic through this thing… we hope it works.'

"[Now], we can just put this browser on your desktop and you’re kind of there. 'Try it out. Use it. Get used to it and let us know if there’s anything blatantly missing. Now try Salesforce though this. Can you use Salesforce or Workday through it? You good? Awesome. Now, I’m going to enforce it so you can only use this.'

ADVERTISEMENT"So, it’s not that big, 'OK, guys. This weekend is the big cutover event.' You get to try this browser out and ease your company and the users into it."

**What’s the next step, rolling it out to more users?** "That’s the immediate component — bringing on more and more sanctioned or approved applications. So, the good news is you get good visibility into the types of cloud services you have, which ones you want to control, which ones you don’t want to. Which ones have sensitive information, and which ones don’t.

ADVERTISEMENT"I think the larger step is the use-case scenarios. So, can you start thinking about bring your own devices [BYOD]? You can start thinking about other scenarios about how to give contractors access. Here’s a browser, download it, you can use your web authentication to get access into it almost like a guest VPN. Those use cases are the next bigger swings."

**Are you keeping in place your other network security measures for now?** "For now, yeah. That’s the benefit of this. It doesn’t step on anything. So, I don’t have to pull anything out if I don’t want to. But certainly, we have a number of redundant controls now. We’re going to have to take a look at them and see what other value there are in those existing tools as opposed to what value Island can bring natively. The opportunity is there, it seems like a natural progression."

ADVERTISEMENT



## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Saas]] [[Salesforce]] [[Browser?]] [[Apps]] [[Schuetter]] [[Casb]] [[Computerworld]]

