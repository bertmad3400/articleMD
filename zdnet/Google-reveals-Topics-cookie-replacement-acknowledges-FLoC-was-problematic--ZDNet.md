# Google reveals Topics cookie replacement, acknowledges FLoC was problematic | ZDNet
### The search company's second attempt to replace third-party cookies relies on the user's previous three weeks of browsing history to provide what it claims is a more anonymized, transparent way of service interest-based ads.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/google-reveals-topics-cookie-replacement-acknowledges-floc-was-problematic/
+ Date: 2022-01-25 17:51:35
+ Author: Michael Gariffo


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/1cbb17c7b2a7bafd51ea51d5e0b001d0183d515d/2020/12/17/ff2b70f6-b5e0-4148-914b-eac3f134b277/cookies.jpg?width=770&height=578&fit=crop&auto=webp)

Google has provided new information on the end of the troubled development process for the FLoC (Federated Learning of Cohorts) it had hoped to use as a replacement for cookies, and it has done so as part of its reveal of another proposed replacement: Topics. 


The search giant's first attempt to replace the third-party cookie with its own technology was met with [staunch opposition from some](https://www.zdnet.com/article/floc-off-vivaldi-declares-as-it-says-no-to-googles-tracking-system/), a [wary eye from others](https://www.zdnet.com/article/wordpress-could-treat-google-floc-as-a-security-issue/), and very little positive feedback. It originally committed, [in early 2021](https://www.zdnet.com/article/google-takes-next-steps-towards-privacy-first-web-devoid-of-third-party-cookies/), to ending third-party cookie support within its Chrome browser in 2022. At that time, Google intended for FLoC to replace cookies with a new technology which it claimed was far more anonymized and still able to yield conversion rates of 95% for every ad dollar spent. 

Obviously, things didn't work out quite as the company had hoped. It eventually ended the development of FLoC in July 2021, around the same time it announced that Chrome would continue supporting third party cookies [until at least mid-2023](https://www.zdnet.com/article/google-delays-chromes-cookie-blocking-changes/). The company had remained cagey on how it planned to move forward with its still-extant plans to replace the cookie until now. 

Dubbed simply "Topics," the new technology aims to track users anonymously using a new API designed to fulfill Google's four main privacy goals: 

* The technology must make it "difficult to reidentify significant numbers of users across sites using just the API."
* It should offer a viable replacement for "a subset of the capabilities of third-party cookies."
* Any recorded data must be "less personally sensitive" than what is being collected today.
* The API should be understandable to users and transparent in its intentions.

Google apparently feels its Topics API meets all of these criteria while still providing the data interest-based ads (IBAs) need to continue operating at a level similar to their current cookie-based endeavors. 

In addition to posting a [GitHub entry](https://github.com/jkarlin/topics) revealing the technical details of Topics, Google's Privacy Sandbox lead Ben Galbraith also held a press briefing in which he revealed additional parameters to several news outlets. Among them was the fact that Topics will initially attempt to track the user's behavior across up to 300-350 specific areas of interest. These areas are based on the [IAB Audience Taxonomy](https://iabtechlab.com/standards/audience-taxonomy/), which contains a much more comprehensive list of 1,500 or so trackable areas of interest.  

Google's GitHub post noted that this is an initial design, hinting at the fact that those 350, or so, might expand further in the future. According to Galbraith, if they do, they will not be expanding into what Google called "sensitive topics," which includes things like the user's race and gender. 






In practical operation, the Topics API lets the user's browser share three of their detected areas of interest when the user visits a site using IBAs. The API will randomly select those three from among the top five it detected. One topic will be chosen from the top five for each of the previous three weeks to give a better but still anonymized picture of the user's recent [online browsing history](https://www.zdnet.com/article/mozilla-research-browsing-histories-are-unique-enough-to-reliably-identify-users/). Google intends for users to be able to get personally involved with their Topics as well, noting that they will be able to disable the tracking of specific areas of interest while also being able to review what Topics have been chosen for them at any given point. 

This level of transparency and user control addresses two of the biggest issues Google heard about in feedback surrounding the failed FLoC proposal: that it was too opaque and added too much personalized "digital fingerprinting" data to the system. The company's aforementioned promise to avoid "sensitive" topics likewise addresses an unfortunate tendency that FLoC had for automatically creating ad cohorts around topics like gender and race. 

Google plans to begin testing Topics with external parties sometime later this quarter. It remains to be seen whether this technology will fare any better than FLoC or if Google will once again be forced to continue accepting [third-party cookies](https://www.zdnet.com/article/french-regulators-fine-google-and-facebook-combined-235-million-for-cookie-tracking/) within its Chrome browser for years to come. 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Google]] [[Api]] [[Third-party]] [[ZDNet]]

